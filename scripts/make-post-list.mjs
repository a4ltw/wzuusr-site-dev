// 產生部落格文章清單 xlsx，供人工篩選
// 用法：node scripts/make-post-list.mjs
import fs from 'fs';
import path from 'path';
import pkg from 'xlsx';
const { utils: XLSX_utils, writeFile: XLSX_write, book_new } = pkg;

const BLOG_DIR = 'src/content/blog';
const OUTPUT = 't_ingredient/post-list.xlsx';

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return {};
  const fm = {};
  for (const line of match[1].split('\n')) {
    const [key, ...rest] = line.split(':');
    if (key && rest.length) fm[key.trim()] = rest.join(':').trim().replace(/^"|"$/g, '');
  }
  return fm;
}

const files = fs.readdirSync(BLOG_DIR).filter(f => f.endsWith('.md')).sort().reverse();

const rows = [['保留？', '檔名', '日期', '標題', '內文預覽']];

for (const file of files) {
  const content = fs.readFileSync(path.join(BLOG_DIR, file), 'utf8');
  const fm = parseFrontmatter(content);
  const body = content.replace(/^---[\s\S]*?---\n/, '').trim();
  const preview = body.replace(/!\[.*?\]\(.*?\)/g, '').trim().slice(0, 80);
  rows.push(['', file.replace('.md', ''), fm.date || '', fm.title || '', preview]);
}

fs.mkdirSync('t_ingredient', { recursive: true });
const wb = XLSX_utils.book_new();
const ws = XLSX_utils.aoa_to_sheet(rows);
ws['!cols'] = [{ wch: 6 }, { wch: 30 }, { wch: 12 }, { wch: 50 }, { wch: 80 }];
XLSX_utils.book_append_sheet(wb, ws, '文章清單');
XLSX_write(wb, OUTPUT);
console.log(`✓ 產生 ${OUTPUT}（共 ${rows.length - 1} 篇）`);
