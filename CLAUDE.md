# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

文藻外語大學 USR 計畫（小螺絲釘 WUTH）靜態網站，從 Wix 搬遷至 Astro + Tailwind CSS v4。

- **開發版**：https://dev.wzuusr.org（branch: `astro`）
- **正式版**：https://wzuusr.org（目前轉址至 Wix，開發完成後取代）
- **語言**：繁體中文（zh-TW）

## Build Commands

```bash
# 安裝依賴（Node >= 22.12.0）
npm install

# 本地開發伺服器（預設 http://localhost:4321）
npm run dev

# 建置靜態檔案至 dist/
npm run build

# 預覽建置結果
npm run preview
```

## Architecture

```
src/
├── components/
│   ├── Header.astro      導覽列（含 navItems 定義、行動選單）
│   ├── Footer.astro
│   └── PageHero.astro    通用頁面 Hero 元件
├── layouts/
│   └── BaseLayout.astro  全站 HTML 骨架（title、description props）
├── content/
│   └── blog/             部落格文章（Astro Content Collections）
│       └── YYYY-slug.md  front matter: title, date, description, tags, categories
├── content.config.ts     blog collection schema（zod 驗證）
├── pages/                所有路由，副檔名 .astro
│   ├── index.astro
│   ├── team/partners/awards/news/framework/fields/faculty/join/contact.astro
│   ├── about/origin.astro
│   ├── activities.astro  計畫動態（目前轉址部落格）
│   ├── blog/
│   │   ├── index.astro   文章列表
│   │   └── [...slug].astro  動態路由
│   ├── expo/zh.astro, en.astro
│   └── materials/
│       ├── index.astro, animation.astro, english.astro, chinese.astro
└── styles/
    └── global.css        Tailwind v4 + CSS 變數

public/
└── images/
    ├── hero/ team/ partners/ materials/ events/ expo/ framework/  圖片依分類放置
    └── logo.png
```

## Design Tokens

- **主色**：`#1a56a0`（CSS var: `--color-primary`）
- **強調色**：`#f97316`（CSS var: `--color-accent`）
- **字型**：Noto Sans TC（Google Fonts）
- **版面寬度**：`max-w-6xl mx-auto px-4`

## Key Patterns

**新增頁面**
1. 在 `src/pages/` 建立 `.astro` 檔
2. 使用 `BaseLayout` 並傳入 `title` 和 `description` props
3. 若需加進導覽列，在 `Header.astro` 的 `navItems` 新增項目

**新增部落格文章**
- 在 `src/content/blog/` 建立 `YYYY-slug.md`，必填 front matter：`title`、`date`

**Tailwind**：使用 v4（`@import "tailwindcss"`），設定在 `vite.plugins` 而非 `tailwind.config`，無需 `tailwind.config.js`

## Development Status

詳細進度與待辦見 `PLAN.md`。目前 `astro` branch 所有頁面內容已填入（含 USR EXPO 中英文），待補的是部落格 2023–2024 年的文章（目前有 2020–2022 + 2025，共 21 篇）。
