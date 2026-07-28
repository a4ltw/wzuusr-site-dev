# 文藻小螺絲釘 WUTH

文藻外語大學「大學社會責任實踐計畫」（Wenzao USR: Tech with Heart）官方網站。

- **正式版**：https://wzuusr.org
- **開發版**：https://dev.wzuusr.org

## 專案簡介

文藻外語大學以多語專業，成立多國語國際醫療翻譯志工隊，進駐區域大型醫院，
共創外籍人士、新住民及移工就醫無障礙（SDGs 3），並服務外國弱勢孩童提升教育素養（SDGs 4）。

本網站原為 Wix 免費版網站，已全面搬遷至 Astro + Tailwind CSS，
提供跨裝置自適應的瀏覽體驗。

## 技術棧

- [Astro](https://astro.build/)（v6）— 靜態網站產生器
- [Tailwind CSS](https://tailwindcss.com/)（v4，CSS-first 設定，無 `tailwind.config.js`）
- Astro Content Collections — 管理歷年部落格文章
- 部署：GitHub Actions + GitHub Pages

## 開發

需求：Node.js >= 22.12.0

```bash
npm install       # 安裝依賴
npm run dev       # 本地開發伺服器（http://localhost:4321）
npm run build     # 建置靜態檔案至 dist/
npm run preview   # 預覽建置結果
```

## 專案結構

```
src/
├── components/       # Header、Footer、PageHero 等共用元件
├── layouts/           # BaseLayout 全站骨架
├── content/blog/      # 部落格文章（Astro Content Collections）
└── pages/             # 所有路由頁面
public/
└── images/            # 依分類放置的靜態圖片
```

詳細架構、頁面清單、開發慣例見 [`CLAUDE.md`](./CLAUDE.md)；
開發進度與待辦見 [`PLAN.md`](./PLAN.md)；
正式網域切換步驟見 [`SWITCHOVER.md`](./SWITCHOVER.md)。

## 部署

推送到 `astro` branch 會透過 GitHub Actions 自動建置並部署到 GitHub Pages。

## 授權

© 文藻小螺絲釘 WUTH（Wenzao USR: Tech with Heart）
