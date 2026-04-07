import os
import re
import html2text

# --- 設定 ---
source_html_dir = "wix_backup/usrdocument2018.wixsite.com/official"
docs_dir = "docs"
output_resource_list = "external_resources.txt"

# --- 頁首/頁尾的標記 (使用正則表達式) ---
# 這些標記用來識別並刪除區塊
header_markers = [
    r"top of page",
    r"本網站是在 Wix 建立.*?立即開始",
    r"文藻小螺絲釘 WUTH.*?Tech with Heart",
    r"Tech warms, love sustains, worldwide connection.",
    r"計畫團隊 Project team.*?更多 MORE", # 導覽列
    r"Use tab to navigate through the menu items."
]

footer_markers = [
    r"關於我們.*?©2020 Wenzao USR",
    r"聯絡我們",
    r"訂閱我們",
    r"bottom of page"
]

# --- 外部資源連結的正則表達式 (修正版) ---
external_link_pattern = re.compile(r'!?\[(.*?)\]\((https?://.*?)\)')

# --- 函式定義 ---

def clean_content(content):
    """ 刪除頁首和頁尾 """
    # 為了簡化，我們將整個內容視為一個字串處理
    # 找到第一個主要內容標題 (通常是 # 或 ## 開頭)
    first_heading_match = re.search(r'^#.*?', content, re.MULTILINE)
    
    start_index = 0
    if first_heading_match:
        start_index = first_heading_match.start()
    
    # 找到頁尾開始的地方 (修正版)
    footer_pattern = r'(關於我們|聯絡我們|訂閱我們|\(C\)2020 Wenzao USR)'
    footer_match = re.search(footer_pattern, content, re.IGNORECASE)
    end_index = len(content)
    if footer_match:
        end_index = footer_match.start()
        
    # 取中間的核心內容
    cleaned = content[start_index:end_index].strip()
    return cleaned

def find_external_resources(content):
    """ 找出所有外部連結 """
    return external_link_pattern.findall(content)

# --- 主程式 ---

all_external_links = set()

# 1. 處理所有 docs 資料夾內的 .md 檔案
print("---" + "階段 1: 清理現有的 Markdown 檔案" + "---")
for root, _, files in os.walk(docs_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    original_content = f.read()
                
                # 尋找外部資源
                links = find_external_resources(original_content)
                for _, link_url in links:
                    all_external_links.add(link_url)

                # 清理內容
                cleaned_content = clean_content(original_content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
                print(f"[成功] 清理了 {filepath}")

            except Exception as e:
                print(f"[失敗] 清理 {filepath} 時發生錯誤: {e}")

# 2. 特別處理 index.md (修正路徑)
print("\n" + "---" + "階段 2: 重新轉換並覆蓋 index.md" + "---")
# wget 將 official.html 存在上一層目錄
homepage_html_path = "wix_backup/usrdocument2018.wixsite.com/official.html"
homepage_md = os.path.join(docs_dir, "index.md")
try:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0
    with open(homepage_html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    markdown_content = h.handle(html_content)
    cleaned_content = clean_content(markdown_content)
    with open(homepage_md, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    print(f"[成功] 已重新轉換並清理 {homepage_md}")
except FileNotFoundError:
    print(f"[失敗] 找不到首頁 HTML 檔案: {homepage_html_path}")
except Exception as e:
    print(f"[失敗] 處理 index.md 時發生錯誤: {e}")

# 3. 清空 framework.md 和 news.md
print("\n" + "---" + "階段 3: 清空有問題的檔案以便手動填寫" + "---")
for f in ["framework.md", "news.md"]:
    filepath = os.path.join(docs_dir, f)
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write("# 此頁面內容待手動填寫\n")
        print(f"[成功] 已清空 {filepath}")
    except Exception as e:
        print(f"[失敗] 清空 {filepath} 時發生錯誤: {e}")

# 4. 將所有外部資源連結寫入檔案
print(f"\n" + "---" + "階段 4: 將外部資源連結寫入 {output_resource_list}" + "---")
if all_external_links:
    with open(output_resource_list, 'w', encoding='utf-8') as f:
        f.write("# 以下是專案中所有外部資源的連結列表\n")
        f.write("# 您需要手動下載這些資源，並將它們更新為本地路徑\n\n")
        # 分類
        images = sorted([link for link in all_external_links if re.search(r'\.(jpg|jpeg|png|gif|avif|bmp|svg)', link, re.I)])
        docs = sorted([link for link in all_external_links if re.search(r'\.(pdf|pptx|doc|docx|zip)', link, re.I)])
        other_links = sorted([link for link in all_external_links if link not in images and link not in docs])

        if images:
            f.write("---" + "圖片 (Images)" + "---" + "\n")
            for link in images:
                f.write(f"{link}\n")
            f.write("\n")

        if docs:
            f.write("---" + "文件 (Documents)" + "---" + "\n")
            for link in docs:
                f.write(f"{link}\n")
            f.write("\n")
        
        if other_links:
            f.write("---" + "其他連結 (Other Links)" + "---" + "\n")
            for link in other_links:
                f.write(f"{link}\n")

    print(f"[成功] 發現 {len(all_external_links)} 個外部連結，已更新 {output_resource_list}")
else:
    print("[資訊] 未發現外部資源連結。")

print("\n" + "--- 清理腳本執行完畢 ---")