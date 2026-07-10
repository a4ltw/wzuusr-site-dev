// 用法：
//   node scripts/fetch-fb-posts.mjs fetch    ← 從 FB 抓原始資料存到 t_ingredient/fb-posts-raw.json
//   node scripts/fetch-fb-posts.mjs convert  ← 從 JSON 轉成 .md 和下載圖片
import fs from 'fs';
import path from 'path';

const TOKEN = fs.readFileSync('fb_token.md', 'utf8').trim();
const RAW_FILE = 't_ingredient/fb-posts-raw.json';
const BLOG_DIR = 'src/content/blog';
const IMAGES_BASE = 'public/images/events';

// ── API helpers ─────────────────────────────────────────────────────────────

async function api(endpoint) {
  const sep = endpoint.includes('?') ? '&' : '?';
  const res = await fetch(`https://graph.facebook.com/v25.0${endpoint}${sep}access_token=${TOKEN}`);
  const data = await res.json();
  if (data.error) throw new Error(`Graph API: ${data.error.message} (code ${data.error.code})`);
  return data;
}

async function downloadImage(url, dest) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  fs.writeFileSync(dest, Buffer.from(await res.arrayBuffer()));
}

// ── STEP 1: fetch ────────────────────────────────────────────────────────────

async function cmdFetch() {
  // 取粉專 page token
  console.log('取得粉專清單...');
  const accounts = await api('/me/accounts');
  console.log('你管理的粉專：');
  accounts.data.forEach(p => console.log(`  ${p.id}  ${p.name}`));

  const page = accounts.data.find(p =>
    p.name.includes('WHC') || p.name.includes('小螺絲釘') || p.name.includes('WUTH')
  );
  if (!page) throw new Error('找不到粉專，請確認上方清單中的名稱');
  console.log(`\n使用：${page.name} (${page.id})\n`);

  // 抓所有貼文
  const posts = [];
  let url = `https://graph.facebook.com/v25.0/${page.id}/posts`
    + `?fields=message,created_time,full_picture`
    + `&limit=25&access_token=${page.access_token}`;

  while (url) {
    const res = await fetch(url);
    const data = await res.json();
    if (data.error) throw new Error(data.error.message);
    posts.push(...(data.data || []));
    url = data.paging?.next || null;
    process.stdout.write(`\r  已取得 ${posts.length} 篇...`);
  }
  console.log('\n');

  fs.mkdirSync('t_ingredient', { recursive: true });
  fs.writeFileSync(RAW_FILE, JSON.stringify(posts, null, 2), 'utf8');
  console.log(`✓ 存到 ${RAW_FILE}（共 ${posts.length} 筆）`);

  const withText = posts.filter(p => p.message?.trim()).length;
  console.log(`  其中有文字內容的：${withText} 篇`);
}

// ── STEP 2: convert ──────────────────────────────────────────────────────────

function makeMarkdown(post, imagePaths) {
  const date = new Date(post.created_time).toISOString().split('T')[0];
  const firstLine = (post.message || '').split('\n')[0].trim().slice(0, 80);
  const title = firstLine || `活動紀錄 ${date}`;
  const body = (post.message || '').trim();
  const imgMd = imagePaths
    .map(f => `![](/${f.replace(/^public\//, '')})`)
    .join('\n\n');

  return [
    '---',
    `title: "${title.replace(/"/g, "'")}"`,
    `date: ${date}`,
    '---',
    '',
    body,
    imgMd ? '\n' + imgMd : '',
  ].join('\n').trimEnd() + '\n';
}

async function cmdConvert() {
  if (!fs.existsSync(RAW_FILE)) throw new Error(`找不到 ${RAW_FILE}，請先執行 fetch`);

  const posts = JSON.parse(fs.readFileSync(RAW_FILE, 'utf8'));
  console.log(`讀取 ${posts.length} 篇貼文，開始轉換...\n`);

  fs.mkdirSync(BLOG_DIR, { recursive: true });

  let created = 0, skipped = 0;

  for (const post of posts) {
    if (!post.message?.trim()) { skipped++; continue; }

    const date = new Date(post.created_time).toISOString().split('T')[0];
    const year = date.slice(0, 4);
    const imgDir = path.join(IMAGES_BASE, year);
    fs.mkdirSync(imgDir, { recursive: true });

    // 收集圖片 URL
    const imgUrls = new Set();
    if (post.full_picture) imgUrls.add(post.full_picture);
    const subs = post.attachments?.data?.[0]?.subattachments?.data || [];
    for (const s of subs) {
      if (s.media?.image?.src) imgUrls.add(s.media.image.src);
    }

    // 下載圖片
    const savedPaths = [];
    let idx = 0;
    for (const url of imgUrls) {
      const dest = path.join(imgDir, `${post.id}-${idx}.jpg`);
      try {
        await downloadImage(url, dest);
        savedPaths.push(dest);
      } catch (e) {
        console.warn(`  ⚠ 圖片下載失敗: ${e.message}`);
      }
      idx++;
    }

    const slug = `${date}-${post.id.slice(-8)}`;
    const mdPath = path.join(BLOG_DIR, `${slug}.md`);
    if (fs.existsSync(mdPath)) { skipped++; continue; }

    fs.writeFileSync(mdPath, makeMarkdown(post, savedPaths), 'utf8');
    console.log(`✓ ${slug}  ${(post.message || '').split('\n')[0].slice(0, 50)}`);
    created++;
  }

  console.log(`\n完成！建立 ${created} 篇，略過 ${skipped} 篇`);
}

// ── main ─────────────────────────────────────────────────────────────────────

const cmd = process.argv[2];
if (cmd === 'fetch') {
  cmdFetch().catch(e => { console.error('錯誤：', e.message); process.exit(1); });
} else if (cmd === 'convert') {
  cmdConvert().catch(e => { console.error('錯誤：', e.message); process.exit(1); });
} else {
  console.log('用法：');
  console.log('  node scripts/fetch-fb-posts.mjs fetch    # 從 FB 抓資料');
  console.log('  node scripts/fetch-fb-posts.mjs convert  # 轉成 .md 檔');
}
