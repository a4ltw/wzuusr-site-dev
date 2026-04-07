# 團隊成員區塊模板

在 `team.md` 或其他頁面新增團隊成員時使用此模板。

---

## 單一成員卡片

```html
<div class="team-card" markdown>

![姓名](assets/images/team/姓名.jpg)

### 姓名
職稱 / 系所

</div>
```

## 完整團隊區塊

```html
<div class="team-grid" markdown>

<div class="team-card" markdown>

![張三](assets/images/team/張三.jpg)

### 張三
計畫主持人 / 英文系

</div>

<div class="team-card" markdown>

![李四](assets/images/team/李四.jpg)

### 李四
共同主持人 / 應華系

</div>

<div class="team-card" markdown>

![王五](assets/images/team/王五.jpg)

### 王五
研究助理 / 英文系

</div>

</div>
```

## 圖片規格

- 格式：JPG 或 PNG
- 尺寸：400x400px（正方形）
- 命名：`姓名.jpg`（例如：`陳俊斌.jpg`）
- 路徑：`docs/assets/images/team/`

## 注意事項

- 每個 `team-card` 需要包在 `team-grid` 內
- `markdown` 屬性讓內部可使用 Markdown 語法
- 圖片會自動裁切成圓形並加上邊框
