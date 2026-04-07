# 貢獻指南 Contributing Guide

感謝您有興趣為文藻小螺絲釘網站貢獻內容！本指南將幫助您了解如何新增或修改網站內容。

---

## 目錄結構

```
docs/
├── index.md              # 首頁
├── about/                # 關於計畫
│   └── origin.md         # 計畫緣起
├── blog/                 # 活動部落格
│   ├── index.md          # 部落格首頁
│   └── posts/            # 文章目錄
│       └── YYYY-*.md     # 文章（依年份命名）
├── expo/                 # USR EXPO
├── materials/            # 數位教材
│   ├── index.md          # 總覽
│   ├── english.md        # 英文教材
│   ├── chinese.md        # 華文教材
│   └── animation.md      # 動畫/繪本
├── assets/               # 靜態資源
│   ├── images/           # 圖片
│   │   ├── team/         # 團隊照片
│   │   ├── partners/     # 合作夥伴 Logo
│   │   ├── awards/       # 獲獎照片
│   │   ├── materials/    # 教材縮圖
│   │   └── events/       # 活動照片
│   │       ├── 2021/
│   │       ├── 2022/
│   │       └── 2025/
│   └── files/            # 文件檔案
│       └── materials/    # 教材 PDF/PPTX
└── stylesheets/          # 自訂樣式
    └── extra.css
```

---

## 新增 Blog 文章

### 步驟

1. 在 `docs/blog/posts/` 建立新檔案
2. 檔名格式：`YYYY-標題關鍵字.md`（例如：`2025-oyster-camp.md`）
3. 複製下方模板，填入內容
4. 將圖片放到 `docs/assets/images/events/YYYY/`

### Front Matter 模板

```yaml
---
date: 2025-01-15
categories:
  - 活動
  - 社區服務
tags:
  - 2025
  - 蚵寮
  - AI
  - 永續
---
```

### 常用分類（Categories）

| 分類 | 說明 |
|------|------|
| 活動 | 一般活動報導 |
| 社區服務 | 在地社區服務 |
| 國際交流 | 柬埔寨、馬來西亞等 |
| 志工培訓 | 志工教育訓練 |
| 醫院服務 | 醫療翻譯服務 |
| 教師增能 | 教師社群活動 |

### 常用標籤（Tags）

- 年份：`2021`、`2022`、`2025`
- 地點：`蚵寮`、`旗山`、`小港`、`柬埔寨`
- 主題：`AI`、`永續`、`防疫`、`海洋`

---

## 圖片命名規範

### 新增圖片規範

使用 **有意義的名稱**，格式：`描述-YYYYMMDD.jpg`

**好的命名範例：**
```
team/計劃主持人-陳俊斌.jpg
events/2025/蚵寮營隊-20250115.jpg
awards/udr-expo-頒獎-20211125.jpg
partners/高雄榮總-logo.png
```

**避免的命名：**
```
10e09e_31a54bdb7_cc40a287.png  # Wix 匯出的亂碼
IMG_20250115.jpg               # 相機預設名稱
未命名.jpg                     # 無意義名稱
```

### 圖片格式建議

| 用途 | 格式 | 建議尺寸 |
|------|------|----------|
| 活動照片 | JPG | 1200px 寬 |
| 團隊頭像 | JPG/PNG | 400x400px |
| 合作夥伴 Logo | PNG（透明背景）| 300x200px |
| 教材縮圖 | PNG | 800x600px |

---

## CSS 元件使用指南

網站提供預設的 CSS 元件，可直接在 Markdown 中使用。

### 卡片格線

```html
<div class="card-grid" markdown>
<div class="usr-card" markdown>

### 卡片標題
卡片內容

</div>
</div>
```

### 團隊成員

```html
<div class="team-grid" markdown>
<div class="team-card" markdown>

![姓名](../assets/images/team/photo.jpg)

### 姓名
職稱

</div>
</div>
```

### 合作夥伴

```html
<div class="partner-grid" markdown>
<div class="partner-card" markdown>

![機構名稱](../assets/images/partners/logo.png){ .partner-logo }

### 機構名稱
合作內容說明

</div>
</div>
```

### 圖片畫廊

```html
<div class="image-gallery" markdown>

![說明1](path/to/image1.jpg)
![說明2](path/to/image2.jpg)
![說明3](path/to/image3.jpg)

</div>
```

### 統計數字

```html
<div class="stats" markdown>
<div class="stat-item" markdown>
<span class="stat-number">100+</span>
<span class="stat-label">標籤說明</span>
</div>
</div>
```

詳細的 CSS 元件說明請參考 [COMPONENTS.md](docs/stylesheets/COMPONENTS.md)。

---

## 新增頁面步驟

1. **建立 Markdown 檔案**
   ```
   docs/新頁面.md
   ```

2. **更新導航**
   編輯 `mkdocs.yml` 的 `nav` 區塊：
   ```yaml
   nav:
     - 首頁: index.md
     - 新頁面: 新頁面.md  # 新增這行
   ```

3. **本地預覽**
   ```bash
   mkdocs serve
   ```
   開啟 http://127.0.0.1:8000 預覽

4. **提交變更**
   ```bash
   git add .
   git commit -m "新增: 頁面名稱"
   git push
   ```

---

## 本地開發

### 環境設置

```bash
# 1. 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 2. 安裝依賴
pip install -r requirements.txt

# 3. 啟動開發伺服器
mkdocs serve
```

### 常用指令

| 指令 | 說明 |
|------|------|
| `mkdocs serve` | 啟動本地開發伺服器（支援熱重載）|
| `mkdocs build` | 建置靜態網站到 `site/` |
| `mkdocs build --strict` | 嚴格模式建置（檢查錯誤）|

---

## 提交規範

### Commit 訊息格式

```
類型: 簡短說明

類型包括：
- 新增: 新功能或新頁面
- 更新: 修改現有內容
- 修復: 修復錯誤
- 樣式: CSS 或排版調整
- 文件: 文件更新
```

**範例：**
```
新增: 2025 蚵寮 AI 永續探索營活動報導
更新: 團隊成員資訊
修復: 首頁連結錯誤
```

---

## 常見問題

### Q: 圖片沒有顯示？
- 確認路徑是否正確（使用相對路徑）
- 確認檔案已加入 `docs/assets/images/` 目錄
- 確認檔名沒有空格或特殊字元

### Q: 頁面沒有出現在導航？
- 確認已在 `mkdocs.yml` 的 `nav` 區塊加入頁面

### Q: 本地預覽正常但部署後有問題？
- 使用 `mkdocs build --strict` 檢查是否有警告
- 確認所有連結使用相對路徑

---

## 需要協助？

如有任何問題，歡迎：
- 在 GitHub 提交 Issue
- 聯絡計畫團隊
