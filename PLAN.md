# 文藻小螺絲釘 WUTH — Astro 新站開發計畫

> 從舊 Wix 網站全面搬遷至 Astro + Tailwind CSS 靜態網站。
> 開發完成後取代 wzuusr.org 的 Wix 轉址。

- **開發版**：https://dev.wzuusr.org（本 repo，branch: astro）
- **正式版**：https://wzuusr.org（目前轉址至 Wix）

---

## 頁面完成度

### ✅ 內容已填入

| 頁面 | 路徑 | 備註 |
|------|------|------|
| 首頁 | `src/pages/index.astro` | Hero、統計、關於計畫、最新活動卡片 |
| 計畫團隊 | `src/pages/team.astro` | PI、共同/協同主持人、助理全部填入 |
| 合作夥伴 | `src/pages/partners.astro` | 醫療、教育、國際三大分類 |
| 得獎記錄 | `src/pages/awards.astro` | 資料已填 |
| 新聞媒體 | `src/pages/news.astro` | 資料已填 |
| 計畫架構 | `src/pages/framework.astro` | 資料已填 |
| 實踐場域 | `src/pages/fields.astro` | 資料已填（有部分 placeholder 待確認） |
| 教師社群 | `src/pages/faculty.astro` | 資料已填 |
| 加入計畫 | `src/pages/join.astro` | 資料已填 |
| 聯絡我們 | `src/pages/contact.astro` | 資料已填 |
| 動畫繪本 | `src/pages/materials/animation.astro` | 資料已填 |
| 英文教材 | `src/pages/materials/english.astro` | 資料已填 |
| 華文教材 | `src/pages/materials/chinese.astro` | 資料已填 |
| 教材總覽 | `src/pages/materials/index.astro` | 資料已填 |
| 計畫緣起 | `src/pages/about/origin.astro` | 資料已填 |

### 🚧 只有框架、內容待填

| 頁面 | 路徑 | 待辦 |
|------|------|------|
| 活動部落格 | `src/pages/blog/index.astro` | 需整合 Astro Content Collections，匯入 22 篇文章 |
| 最新活動 | `src/pages/activities.astro` | 目前轉址到部落格，可評估是否需要獨立頁面 |
| USR EXPO（中） | `src/pages/expo/zh.astro` | 內容待從 Wix 搬移（PDF 提供） |
| USR EXPO（英） | `src/pages/expo/en.astro` | 內容待從 Wix 搬移（PDF 提供） |

---

## 待辦事項

### 🔴 優先（從 Wix 搬內容）

搬移方式：**瀏覽器列印成 PDF → 丟給 Claude 處理**

- [ ] USR EXPO 中文版（`expo/zh.astro`）
- [ ] USR EXPO 英文版（`expo/en.astro`）
- [ ] 確認 `fields.astro` 的 placeholder 內容是否正確

### 🟡 中期

- [ ] **部落格整合**：用 Astro Content Collections 把 `.archived/docs/blog/posts/` 的 22 篇 markdown 匯入，讓 `/blog` 頁面能列出文章
- [ ] **部落格文章補齊**：目前有 2020–2022、2025 年，缺 2023–2024 年的文章
- [ ] **圖片清點**：`public/images/` 目前圖片與各頁面的對應是否正確

### 🟢 後期

- [ ] **正式切換**：開發版確認 OK → 更新 `a4ltw/wzuusr.org` repo 取代 Wix 轉址
- [ ] **CMS 評估**：是否需要 Decap CMS 讓非工程師能新增文章

---

## 檔案結構

```
src/
├── components/
│   ├── Header.astro
│   ├── Footer.astro
│   └── PageHero.astro
├── layouts/
│   └── BaseLayout.astro
└── pages/
    ├── index.astro          首頁
    ├── team.astro           計畫團隊
    ├── partners.astro       合作夥伴
    ├── framework.astro      計畫架構
    ├── fields.astro         實踐場域
    ├── faculty.astro        教師社群
    ├── awards.astro         得獎記錄
    ├── news.astro           新聞媒體
    ├── activities.astro     最新活動
    ├── join.astro           加入計畫
    ├── contact.astro        聯絡我們
    ├── about/origin.astro   計畫緣起
    ├── blog/index.astro     活動部落格
    ├── expo/zh.astro        USR EXPO（中）
    ├── expo/en.astro        USR EXPO（英）
    └── materials/
        ├── index.astro      教材總覽
        ├── animation.astro  動畫繪本
        ├── english.astro    英文教材
        └── chinese.astro    華文教材

public/images/
├── hero/                    首頁 Hero 圖
├── team/                    團隊成員照片
└── partners/                合作夥伴 Logo
```
