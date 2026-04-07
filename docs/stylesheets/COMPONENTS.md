# CSS 元件文件

本文件說明 `extra.css` 中可用的 CSS 元件及其使用方式。

---

## CSS 變數

### 品牌色彩

```css
--usr-primary: #2196F3;      /* 主色（藍色）*/
--usr-primary-dark: #1976D2; /* 主色深色 */
--usr-accent: #FF9800;       /* 強調色（橘色）*/
--usr-accent-dark: #F57C00;  /* 強調色深色 */
--usr-success: #4CAF50;      /* 成功色（綠色）*/
```

### 間距系統（8px 基礎）

```css
--spacing-xs: 8px;   /* 極小 */
--spacing-sm: 16px;  /* 小 */
--spacing-md: 24px;  /* 中 */
--spacing-lg: 32px;  /* 大 */
--spacing-xl: 48px;  /* 極大 */
```

### 陰影

```css
--shadow-sm: 0 2px 4px rgba(0,0,0,0.1);   /* 小陰影 */
--shadow-md: 0 4px 8px rgba(0,0,0,0.15);  /* 中陰影 */
--shadow-lg: 0 8px 16px rgba(0,0,0,0.2);  /* 大陰影 */
```

### 圓角

```css
--radius-sm: 4px;   /* 小圓角 */
--radius-md: 8px;   /* 中圓角 */
--radius-lg: 16px;  /* 大圓角 */
```

---

## 卡片元件

### `.usr-card` - 一般資訊卡片

帶有左側色條的資訊卡片。

```html
<div class="usr-card" markdown>

### 卡片標題
卡片內容文字

</div>
```

**特性：**
- 左側藍色邊框
- 懸停時上浮效果
- 自動深色模式支援

### `.card-grid` - 卡片網格

自動響應式的卡片排列。

```html
<div class="card-grid" markdown>
  <div class="usr-card">卡片 1</div>
  <div class="usr-card">卡片 2</div>
  <div class="usr-card">卡片 3</div>
</div>
```

**變體：**
- `.card-grid` - 預設（最小寬度 280px）
- `.card-grid-2` - 兩欄變體（最小寬度 350px）
- `.card-grid-3` - 三欄變體（最小寬度 250px）

---

## 團隊元件

### `.team-grid` + `.team-card`

圓形頭像的團隊成員展示。

```html
<div class="team-grid" markdown>
  <div class="team-card" markdown>

![姓名](path/to/photo.jpg)

### 姓名
職稱

  </div>
</div>
```

**特性：**
- 頭像自動裁切為圓形
- 藍色邊框
- 懸停時上浮效果
- 響應式排列（最小寬度 200px）

---

## 合作夥伴元件

### `.partner-grid` + `.partner-card`

Logo 展示的合作夥伴區塊。

```html
<div class="partner-grid" markdown>
  <div class="partner-card" markdown>

![機構](path/to/logo.png){ .partner-logo }

### 機構名稱
合作說明

  </div>
</div>
```

**特性：**
- Logo 自動置中
- 最大尺寸限制（150x100px）
- 懸停時上浮效果

---

## 圖片畫廊

### `.image-gallery`

自動排列的圖片網格，支援 Lightbox 放大。

```html
<div class="image-gallery" markdown>

![說明1](path/to/image1.jpg)
![說明2](path/to/image2.jpg)
![說明3](path/to/image3.jpg)

</div>
```

**特性：**
- 自動響應式排列
- 圖片統一高度裁切
- 懸停時縮放效果
- 支援 glightbox 放大

---

## 統計數字

### `.stats` + `.stat-item`

數字展示區塊。

```html
<div class="stats" markdown>
  <div class="stat-item" markdown>
    <span class="stat-number">100+</span>
    <span class="stat-label">服務人次</span>
  </div>
  <div class="stat-item" markdown>
    <span class="stat-number">50+</span>
    <span class="stat-label">合作夥伴</span>
  </div>
</div>
```

### `.stats-section`

首頁用的統計區塊（更現代的樣式）。

```html
<div class="stats-section" markdown>
  <div class="stats" markdown>
    <!-- stat-items -->
  </div>
</div>
```

---

## Hero 區塊

### `.hero-section`

漸層背景的主視覺區塊。

```html
<div class="hero-section" markdown>

# 標題
副標題或說明文字

[按鈕文字](連結){ .usr-btn }

</div>
```

### `.hero-minimal`

簡約風格的 Hero 區塊。

```html
<div class="hero-minimal" markdown>

# 標題
<p class="subtitle">副標題</p>
<p class="tagline">標語</p>

<div class="cta-buttons" markdown>
[主要按鈕](連結){ .usr-btn .usr-btn-primary }
[次要按鈕](連結){ .usr-btn }
</div>

</div>
```

---

## 按鈕

### `.usr-btn`

基本按鈕（橘色）。

```html
[按鈕文字](連結){ .usr-btn }
```

### 按鈕變體

```html
[主要按鈕](連結){ .usr-btn .usr-btn-primary }  <!-- 藍色 -->
[外框按鈕](連結){ .usr-btn .usr-btn-outline }  <!-- 透明+白框 -->
```

---

## 時間軸

### `.timeline` + `.timeline-item`

垂直時間軸展示。

```html
<div class="timeline" markdown>
  <div class="timeline-item" markdown>

#### 2025 年
事件說明

  </div>
  <div class="timeline-item" markdown>

#### 2024 年
事件說明

  </div>
</div>
```

---

## 功能卡片

### `.feature-cards` + `.feature-card`

首頁功能展示用的卡片。

```html
<div class="feature-cards" markdown>
  <div class="feature-card" markdown>

<span class="icon">:material-school:</span>

### 功能標題
功能說明

  </div>
</div>
```

---

## 標籤

### `.tag`

小型標籤元素。

```html
<span class="tag">標籤文字</span>
<span class="tag tag-accent">強調標籤</span>
<span class="tag tag-success">成功標籤</span>
```

---

## 社群連結

### `.social-links`

社群媒體圖示列。

```html
<div class="social-links" markdown>
  <a href="https://fb.wzuusr.org">:fontawesome-brands-facebook:</a>
  <a href="https://ig.wzuusr.org">:fontawesome-brands-instagram:</a>
  <a href="https://yt.wzuusr.org">:fontawesome-brands-youtube:</a>
</div>
```

---

## 動畫

### `.animate-fade-in`

淡入上移動畫。

```html
<div class="animate-fade-in">
  <!-- 內容 -->
</div>
```

### `.pulse`

脈動效果（適用於強調元素）。

```html
<span class="pulse">:material-new-box:</span>
```

---

## 響應式斷點

元件在以下斷點會調整佈局：

| 斷點 | 說明 |
|------|------|
| `768px` | 平板以下，卡片改為單欄 |

---

## 深色模式

所有元件自動支援深色模式，使用 `[data-md-color-scheme="slate"]` 選擇器覆寫樣式。

背景色自動切換：
- 淺色模式：`--usr-card-bg: #ffffff`
- 深色模式：`--usr-card-bg: #2d2d2d`
