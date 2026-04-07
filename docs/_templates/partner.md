# 合作夥伴區塊模板

在 `partners.md` 或其他頁面新增合作夥伴時使用此模板。

---

## 單一夥伴卡片

```html
<div class="partner-card" markdown>

![機構名稱](assets/images/partners/機構名稱-logo.png){ .partner-logo }

### 機構名稱
合作內容簡述

</div>
```

## 完整夥伴區塊

```html
<div class="partner-grid" markdown>

<div class="partner-card" markdown>

![高雄榮總](assets/images/partners/高雄榮總-logo.png){ .partner-logo }

### 高雄榮民總醫院
提供醫療翻譯服務場域，共同推動多語言醫療服務。

</div>

<div class="partner-card" markdown>

![小港醫院](assets/images/partners/小港醫院-logo.png){ .partner-logo }

### 高雄市立小港醫院
合作進行移工健康檢查翻譯服務。

</div>

<div class="partner-card" markdown>

![義守醫院](assets/images/partners/義守醫院-logo.png){ .partner-logo }

### 義守大學附設醫院
共同培訓醫療翻譯志工。

</div>

</div>
```

## 圖片規格

- 格式：PNG（透明背景）
- 尺寸：300x200px（橫式）
- 命名：`機構名稱-logo.png`
- 路徑：`docs/assets/images/partners/`

## 分類建議

可依合作類型分區塊呈現：

```markdown
## 醫療機構

<div class="partner-grid" markdown>
<!-- 醫院夥伴 -->
</div>

## 教育機構

<div class="partner-grid" markdown>
<!-- 學校夥伴 -->
</div>

## 社區組織

<div class="partner-grid" markdown>
<!-- 社區夥伴 -->
</div>
```
