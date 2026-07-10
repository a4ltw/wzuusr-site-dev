# wzuusr.org 正式切換 Runbook

> 目的：讓 wzuusr.org 從「轉址舊 Wix」正式改為 Astro 新站，三 repo 收成一個。
> 執行時機：A4 說「切換」的那天。預估 1–2 小時。
> 前身整備已於 2026-07-10 完成（見 `_task_state.md`）。

## 0. 前置確認（切換前必須全綠）

- [ ] dev.wzuusr.org 全站人工瀏覽過一輪（桌機＋手機）
- [ ] PLAN.md 優先待辦清空（fields placeholder 確認等）
- [ ] 通知計畫團隊切換時間

## 1. 把 Astro 專案推進 wzuusr.org repo

```bash
cd /home/asl/projects/wzuusr-site-dev
git remote add prod git@github.com:a4ltw/wzuusr.org.git
git push prod astro:astro
```

然後在 GitHub `a4ltw/wzuusr.org`：
- Settings → 把 default branch 改成 `astro`
- 舊 `master`（mkdocs）保留不刪，當歷史

## 2. 修改部署設定（在 astro branch 上）

`.github/workflows/deploy.yml`：
- `echo "dev.wzuusr.org" > dist/CNAME` 改成 `echo "wzuusr.org" > dist/CNAME`
- fb/ig/yt 轉址頁的複製已存在（`cp -r docs/fb dist/` 等），不用動
- 觸發 branch 維持 `astro`

GitHub Pages 設定：Settings → Pages → custom domain 填 `wzuusr.org`，勾 Enforce HTTPS。

## 3. 舊路徑轉址（不斷鏈）

- 在 `public/n/index.html` 放 meta-refresh 轉址到 `/`（舊 mkdocs 站掛在 /n 底下）
- 若要細緻一點，對照 mkdocs nav 產生對應轉址頁（/n/about/origin/ → /about/origin/ 等）；不做也可接受，/n/* 統一回首頁即可

## 4. join.wzuusr.org 改轉址

`a4ltw/wzuusr_join` repo：index.html 整個換成 meta-refresh 轉址到 `https://wzuusr.org/join/`，CNAME 檔保留（join.wzuusr.org 網域不變）。assets 可清空。

## 5. dev.wzuusr.org 的去留

建議保留 `wzuusr-site-dev` repo 當開發／預覽站（雙 repo：dev 推 dev.wzuusr.org，確認後 push 到 prod remote 部署正式站）。若不想維護兩個，就把 wzuusr-site-dev archive，之後直接在 wzuusr.org repo 開發。

## 6. 切換後驗證清單

- [ ] https://wzuusr.org 顯示 Astro 新站（不再轉 Wix）
- [ ] https://wzuusr.org/join、/activities、/materials 正常
- [ ] https://fb.wzuusr.org、ig、yt 子網域轉址仍通（若失效，檢查 DNS 與 Pages 網域設定——子網域的服務機制待查證）
- [ ] https://wzuusr.org/fb、/ig、/yt 路徑轉址仍通
- [ ] https://wzuusr.org/n/ 轉回首頁
- [ ] https://join.wzuusr.org 轉到 /join
- [ ] 手機開首頁與 join 頁無爆版
- [ ] Google 搜「文藻 USR」點舊連結不出 404

## 7. 善後

- [ ] `wzuusr_join` repo → GitHub Archive（轉址頁部署後）
- [ ] 舊 Wix 站保留不動（免費版，當歷史備份；完整備份已在 ~/backups/wzuusr_wix_backup_20260710.tar.gz）
- [ ] 更新兩邊 CLAUDE.md 與 PLAN.md 的網址說明
