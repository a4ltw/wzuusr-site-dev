# wzuusr-site-dev 開發計畫

> 本文件追蹤 dev.wzuusr.org（開發版網站）的工作進度。
> 開發完成後將取代正式站 wzuusr.org 的舊 Wix 轉址。

---

## 專案背景

文藻外語大學 USR 計畫網站，從舊 Wix 網站（usrdocument2018.wixsite.com/official）移植至 MkDocs Material 靜態網站。

- **開發版**：https://dev.wzuusr.org（本 repo：a4ltw/wzuusr-site-dev）
- **正式版**：https://wzuusr.org（repo：a4ltw/wzuusr.org，目前轉址至舊 Wix）
- **上線策略**：開發版完成 → 取代正式版的轉址 index.html → 全面切換

---

## 已完成

| 項目 | commit |
|------|--------|
| 初始化 dev.wzuusr.org，設定 GitHub Actions 部署、CNAME | 2b7d93b |
| 修復 extra.js 缺失的 404 錯誤 | 273fb43 |
| 修正 workflow 觸發 branch 為 main | 4d18419 |
| 內容對齊舊網站：修正 PI 姓名、補團隊真實 bio、修正合作夥伴名稱、場域改為圖片牆、首頁加「關於計畫」段落 | 5160423 |
| 標題文字改為錨點連結，隱藏 ¶ 符號 | 88cab1d |
| 視覺對齊舊網站：白色 Header/Tabs、膠囊按鈕、`.dark-section`、`.photo-grid` 等 CSS | 待提交 |

---

## 待辦事項

### 🔴 立即

- [ ] **提交 CSS 視覺改進**（`docs/stylesheets/extra.css` 有未提交變更）
  - 白色 Header / Tabs
  - 膠囊形狀按鈕（`border-radius: 50px`）
  - `.spaced-title`、`.dark-section`、`.photo-grid`、`.video-wrapper` 等新 class

---

### 🟡 短期（視覺完成度）

- [ ] **頁面 Hero Banner**：子頁面（團隊、夥伴等）加入全寬照片背景 + 置中白色標題的 banner 區塊
  - 新增 `.page-hero` CSS class
  - 需在 `team.md`、`partners.md` 等頁面套用

- [ ] **合作夥伴 Logo 改為圓形**：`docs/partners.md` 目前 logo 是方形，舊網站是圓形裁切
  - 在 `.partner-logo` 加上 `border-radius: 50%`

- [ ] **首頁 3 欄快速連結區塊**：舊網站首頁有「合作夥伴 / 主持團隊 / 教師社群」照片+文字卡片
  - 使用 `.photo-grid` + `.photo-grid-item` 實作
  - 需確認 3 張對應照片

- [ ] **Footer 改為 3 欄**：舊網站 Footer 有「關於我們 / 聯絡我們 / 訂閱我們」分欄
  - MkDocs Material 的 footer 需透過 `overrides/` 或 `custom_dir` 覆寫

---

### 🟡 中期（內容補齊）

- [ ] **動畫頁面 3 個缺失連結**（`docs/materials/animation.md`）
  - 海洋小衛士、珊瑚的彩色夢、烏魚的旅程（第 38、47、56 行）標註「影片連結待更新」
  - 需向製作組確認 YouTube 連結

- [ ] **華文教材頁面**（`docs/materials/chinese.md`）
  - 目前整頁只有「內容準備中」
  - 選項 A：補充實際教案 PDF / 下載連結
  - 選項 B：暫時從導航移除，有內容再加回來

- [ ] **補充 2023-2024 年部落格文章**（`docs/blog/posts/`）
  - 目前有 2020–2022、2025 年，缺 2023 和 2024 年
  - 參考 `docs/_templates/blog-post.md` 模板

---

### 🟢 後期

- [ ] **整合 Decap CMS**
  - 讓不熟悉 Git 的同事能透過網頁介面新增文章、上傳圖片
  - 做法：在 `docs/admin/` 新增 `index.html` 與 `config.yml`
  - 需設定 GitHub OAuth 或 Netlify Identity 作為認證
  - 完成後登入 `dev.wzuusr.org/admin/` 即可使用

- [ ] **正式切換**
  - 開發版視覺/內容確認 OK → 更新 `a4ltw/wzuusr.org` repo 的部署邏輯
  - 將 `site_url` 從 `https://dev.wzuusr.org` 改回 `https://wzuusr.org`
  - 移除舊 Wix 轉址的 `index.html`

---

## 關鍵檔案對照

| 頁面 | 路徑 |
|------|------|
| 首頁 | `docs/index.md` |
| 計畫團隊 | `docs/team.md` |
| 合作夥伴 | `docs/partners.md` |
| 實踐場域 | `docs/fields.md` |
| 動畫/繪本 | `docs/materials/animation.md` |
| 華文教材 | `docs/materials/chinese.md` |
| 自訂樣式 | `docs/stylesheets/extra.css` |
| 自訂 JS | `docs/javascripts/extra.js` |
| 部署設定 | `.github/workflows/deploy.yml` |
| 導航結構 | `mkdocs.yml` |
