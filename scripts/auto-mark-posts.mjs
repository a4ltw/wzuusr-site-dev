// 自動在 post-list.xlsx 的「保留？」欄標記 X：內文只有連結、無說明文字的貼文
// 用法：node scripts/auto-mark-posts.mjs
import fs from 'fs';
import path from 'path';
import pkg from 'xlsx';
const { readFile, writeFile, utils } = pkg;

const BLOG_DIR = 'src/content/blog';
const XLSX_FILE = 't_ingredient/post-list.xlsx';

// 判斷內文是否「只有連結、無說明」
function isLinkOnly(content) {
  const body = content.replace(/^---[\s\S]*?---\n/, '').trim();
  // 移除圖片 markdown
  const noImages = body.replace(/!\[.*?\]\(.*?\)/g, '').trim();
  // 移除所有 URL
  const noLinks = noImages.replace(/https?:\/\/\S+/g, '').trim();
  // 剩下的文字夠少（< 10 字）就算純連結貼文
  return noLinks.length < 10;
}

const wb = readFile(XLSX_FILE);
const ws = wb.Sheets['文章清單'];
const rows = utils.sheet_to_json(ws, { header: 1 });

let marked = 0;
for (let i = 1; i < rows.length; i++) {
  const slug = rows[i][1];
  if (!slug) continue;
  const mdPath = path.join(BLOG_DIR, `${slug}.md`);
  if (!fs.existsSync(mdPath)) continue;
  const content = fs.readFileSync(mdPath, 'utf8');
  if (isLinkOnly(content)) {
    rows[i][0] = 'X';
    marked++;
  }
}

const newWs = utils.aoa_to_sheet(rows);
newWs['!cols'] = [{ wch: 6 }, { wch: 30 }, { wch: 12 }, { wch: 50 }, { wch: 80 }];
wb.Sheets['文章清單'] = newWs;
writeFile(wb, XLSX_FILE);
console.log(`✓ 標記完成，共 ${marked} 篇標為 X`);
