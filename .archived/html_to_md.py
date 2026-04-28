
import os
import html2text
import re

# 設定來源和目標路徑
source_dir = "wix_backup/usrdocument2018.wixsite.com/official"
target_dir = "docs"

# 建立 html2text 轉換器
h = html2text.HTML2Text()
h.ignore_links = False
h.body_width = 0

# 頁面對應關係 (HTML 檔名 -> Markdown 檔名)
# 我們需要手動配對，因為檔名可能不一致
page_map = {
    "official.html": "index.md",
    "計畫團隊.html": "team.md",
    "計畫團隊-1.html": "team.md", # 可能是重複或草稿
    "組織架構.html": "framework.md",
    "副本-數位教材-digital-instructional-materials.html": "materials/index.md",
    "副本-英文課程教材-materials-of-english-education.html": "materials/english.md",
    # 中文教材和動畫頁面需要確認檔名
    "媒體報導.html": "news.md",
    "媒體報導-1.html": "news.md", # 可能是重複或草稿
    "服務場域.html": "fields.md",
    "about-3.html": "awards.md", # 假設 about-3 是得獎資訊
    "副本-活動消息activity.html": "activities.md"
}

print("---" + "開始轉換 HTML 到 Markdown" + "---")

# 遍歷來源資料夾中的檔案
for filename in os.listdir(source_dir):
    if filename.endswith(".html") and filename in page_map:
        source_path = os.path.join(source_dir, filename)
        target_filename = page_map[filename]
        target_path = os.path.join(target_dir, target_filename)

        try:
            with open(source_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # 進行轉換
            markdown_content = h.handle(html_content)

            # 簡單清理一下 Wix 特有的殘留內容
            # 移除頁首頁尾的導覽部分 (這部分由 MkDocs 主題處理)
            # 這裡的正則表達式是猜測，可能不完全精準
            markdown_content = re.sub(r'(?s)(https://www.wix.com/lp/lp-website-builder.*?bottom of page)', '', markdown_content, flags=re.IGNORECASE)
            markdown_content = re.sub(r'(?s)top of page.*?Log In / Sign Up', '', markdown_content, flags=re.IGNORECASE)


            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            print(f"[成功] {source_path} -> {target_path}")

        except Exception as e:
            print(f"[失敗] 處理 {source_path} 時發生錯誤: {e}")

print("\n" + "---" + "轉換完成" + "---")
print("\n提醒：")
print("1. 腳本已將 HTML 文字內容轉換為 Markdown。請務必手動檢查每個 .md 檔案的格式是否正確。")
print("2. 圖片連結仍然指向網路上的 Wix 伺服器。您需要手動下載這些圖片到 `docs/assets/images` 並更新 Markdown 中的連結。")
print("3. `page_map` 中可能有些頁面對應不正確或缺失，需要您根據下載的 HTML 檔案手動補全。")
