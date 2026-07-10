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
| 計畫動態 | `src/pages/activities.astro` | 整合部落格文章列表 + Facebook 活動連結 |
| USR EXPO（中） | `src/pages/expo/zh.astro` | 完整中文文章已填入 |
| USR EXPO（英） | `src/pages/expo/en.astro` | 完整英文文章已填入 |
| 活動部落格 | `src/pages/blog/index.astro` | 301 轉址至 `/activities` |

---

## 待辦事項

### 🔴 優先

- [ ] **部落格文章補齊**：目前有 2020–2022、2025 年（共 21 篇），缺 2023–2024 年的文章
- [ ] 確認 `fields.astro` 的 placeholder 內容是否正確

### 🟡 中期

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
├── partners/                合作夥伴 Logo
├── materials/               教材封面圖
├── expo/                    EXPO 文章插圖
├── framework/               計畫架構圖
└── events/                  活動照片
```
