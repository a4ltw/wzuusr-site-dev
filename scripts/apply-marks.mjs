// 根據 post-list.xlsx 的標記批次處理文章
// X → 刪除；L → 移至指定資料夾
import fs from 'fs';
import path from 'path';
import pkg from 'xlsx';
const { readFile, utils } = pkg;

const XLSX_FILE = 't_ingredient/post-list.xlsx';
const BLOG_DIR = 'src/content/blog';
const L_DEST = '/home/asl/G_WZULTC/1. WZULTC_協作資料夾/[網站]官方網站/t_ingredient';

const wb = readFile(XLSX_FILE);
const rows = utils.sheet_to_json(wb.Sheets['文章清單'], { header: 1 });

const marked = { X: [], L: [] };
for (const row of rows.slice(1)) {
  const [mark, slug] = row;
  if (!slug) continue;
  const m = String(mark || '').trim().toUpperCase();
  if (m === 'X' || m === 'L') marked[m].push(slug);
}

console.log(`X（刪除）：${marked.X.length} 篇`);
console.log(`L（移出）：${marked.L.length} 篇\n`);

// 刪除 X
let deleted = 0;
for (const slug of marked.X) {
  const p = path.join(BLOG_DIR, `${slug}.md`);
  if (fs.existsSync(p)) { fs.unlinkSync(p); deleted++; }
}
console.log(`✓ 已刪除 ${deleted} 篇`);

// 移動 L
fs.mkdirSync(L_DEST, { recursive: true });
let moved = 0;
for (const slug of marked.L) {
  const src = path.join(BLOG_DIR, `${slug}.md`);
  const dest = path.join(L_DEST, `${slug}.md`);
  if (fs.existsSync(src)) { fs.copyFileSync(src, dest); fs.unlinkSync(src); moved++; }
}
console.log(`✓ 已移動 ${moved} 篇至 ${L_DEST}`);

console.log(`\n剩餘文章：${fs.readdirSync(BLOG_DIR).filter(f => f.endsWith('.md')).length} 篇`);
