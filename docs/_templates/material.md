# 教材頁面區塊模板

在 `materials/` 目錄下的教材頁面新增教材時使用此模板。

---

## 教材表格（單一學校/單位）

```markdown
## 學校/單位名稱
School Name, Location

| 日期 | 教師 | 主題 | 下載 |
|------|------|------|------|
| YYYY/MM/DD | 教師姓名 | 課程主題 | [:material-download: 下載](../assets/files/materials/檔案名稱.pdf) |
| YYYY/MM/DD | 教師姓名 | 課程主題 | [:material-download: 下載](../assets/files/materials/檔案名稱.pptx) |

![課程照片](../assets/images/materials/課程照片.png)
```

## 教材表格（分系列）

```markdown
## 學校/單位名稱

### 系列一名稱

| 日期 | 主題 | 下載 |
|------|------|------|
| YYYY/MM/DD | 主題 (1) | [:material-download: 下載](../assets/files/materials/檔案名稱-1.pdf) |
| YYYY/MM/DD | 主題 (2) | [:material-download: 下載](../assets/files/materials/檔案名稱-2.pdf) |

### 系列二名稱

| 日期 | 主題 | 下載 |
|------|------|------|
| YYYY/MM/DD | 主題 (1) | [:material-download: 下載](../assets/files/materials/檔案名稱-1.pdf) |
| YYYY/MM/DD | 主題 (2) | [:material-download: 下載](../assets/files/materials/檔案名稱-2.pdf) |
```

## 檔案命名建議

```
files/materials/
├── sarawak/                    # 依地區分類
│   ├── greeting-sandra.pdf
│   └── place-olivia.pdf
├── keliao-elementary/          # 蚵寮國小
│   ├── under-the-sea.pdf
│   └── ocean-protection.pptx
└── keliao-junior/              # 蚵寮國中
    ├── under-the-sea-1.pdf
    └── ocean-pollution-1.pdf
```

## 教材圖片

縮圖放置於 `docs/assets/images/materials/`

建議命名：`學校簡稱-課程主題.png`

## 下載連結格式

MkDocs Material 使用 `:material-download:` 圖示：

```markdown
[:material-download: 下載](路徑/檔案.pdf)
```

會顯示為帶下載圖示的連結。
