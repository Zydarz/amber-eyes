# Báo cáo: Sinh ảnh nền Tập 26 & Tập 40 trên Kaggle GPU (25/11/2026)

> **Yêu cầu:** đọc `BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md`, kết nối Kaggle, tạo ảnh nền còn thiếu của **Tập 26** và **Tập 40**.
> **Kết quả:** **19 ảnh đã sinh** (T26: 9 · T40: 10) + **7 lượt sinh lại** để loại chữ AI ⇒ **Tập 26 đủ 176/176**, **Tập 40 đủ 154/154**. Cổng `map_shot_anh.py --check` ĐẠT cho cả hai tập.

---

## 1. Trạng thái trước khi sinh

Đếm theo quy ước dự án: **mỗi job trong `.work/bg_jobs_tapXX.json` = 1 ảnh `assets/bg/<tên job>.png`; cần sinh = job chưa có file.**

| Tập | Số job | Ảnh đã có | Cần sinh | Ghi chú |
|:---:|---:|---:|---:|---|
| 26 | 176 | 167 | **9** | 9 job hậu tố `…b` do tách lặp ảnh (mục VI.3 của báo cáo thống kê) |
| 40 | 154 | 145 | **10** | 5 ảnh thiếu file + 5 job `…b` do tách shot > 30 s (mục VI.4–VI.5) |

Tổng **19 ảnh**. Tất cả job này đã có trong `02_SAN_XUAT/Ho_So_Toi_Pham/TapXX/Bang_Shot_Anh_TapXX.md` ⇒ ảnh là bắt buộc, không phải ảnh dư.

---

## 2. Công cụ & thông số (theo `00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` v1.0)

| Hạng mục | Giá trị |
|---|---|
| Nơi chạy | Kaggle GPU (2 kernel riêng = 2 phiên VM độc lập) |
| Mô hình | `black-forest-labs/FLUX.2-klein-4B` (Apache-2.0 — thương mại được) |
| Kích thước | 1056×592 → resize **LANCZOS 2112×1188** (16:9 2K) |
| Inference | 5 steps · guidance 2.2 · `enable_model_cpu_offload()` · `vae.enable_tiling()` |
| Hậu kỳ | Color 0.65 → Contrast 1.15 → vignette 45 % → film grain (σ 1.8) |
| Prompt | 4 tầng: STYLE_PREFIX + cảnh + MOOD + NEGATIVE_SUFFIX |
| Seed | kho riêng `460013…460139` (không trùng các lô 15k/37k/30k/260k) |

**Vì sao 2 kernel chứ không 1 kernel chạy 2 worker:** đo được 16/11/2026 — 2 worker `cpu_offload` trong 1 phiên ⇒ 2 × 15–17 GB System RAM > 31 GB ⇒ OOM-Killer `-9`. Chỉ “2 kernel riêng” là an toàn (mục 5.2 tiêu chuẩn).

---

## 3. Các lô sinh (3 kernel)

| # | Kernel | Số ảnh | Kết quả | Seed | Thời gian |
|---|---|---:|---|---|---|
| 1 | `chiduong2026/amber-eyes-flux2-t26-40-miss-k1` | 10 | **10/10 OK** | 460013–460076 | ~75 s/ảnh |
| 2 | `chiduong2026/amber-eyes-flux2-t26-40-miss-k2` | 9 | **9/9 OK** (676 s) | 460083–460139 | ~75 s/ảnh |
| 3 | `chiduong2026/amber-eyes-flux2-t26-40-detext-k1` | 5 | **5/5 OK** | 470013–470041 | ~72 s/ảnh |
| 4 | `chiduong2026/amber-eyes-flux2-t40-map-detext2-k1` | 1 | **1/1 OK** | 480013 | ~70 s |
| 5 | `chiduong2026/amber-eyes-flux2-t40-map-detext3-k1` | 1 | **1/1 OK** | 490013 | ~70 s |

Tổng **26 lượt sinh** (19 ảnh + 7 lượt sinh lại) để có 19 ảnh dùng được. **0 đồng chi phí** (GPU Kaggle miễn phí).

---

## 4. QC — soi mắt 100 % (H2 / H19 / H20 / H26)

Cách kiểm: montage 4 cột × 5 hàng, ô 512 px (`qc_t26_t40_new.py` → `.work/qc_montage/t26_t40_new19.jpg`) **+** zoom full-res các vùng có vật dễ bị AI vẽ chữ.

**Lần 1 — phát hiện 5 ảnh có chữ AI (H26 trượt):**

| Ảnh | Lỗi | Cách sửa (luật detext mục 6.1) |
|---|---|---|
| `t40_a1_03b_…stereotype` | bìa tạp chí có chữ giả | bỏ giá tạp chí → tường trơn, thêm “no printed matter” |
| `t26_a2_05b_…no_adoption_search` | chồng giấy viết tay | bỏ chồng giấy → một quyển sổ bìa trắng trơn |
| `t26_a2_02b_…tea_table` | tranh treo có nét chữ | bỏ tranh → tường plaster trơn |
| `t40_a5_12b_…amber_threads` | màn hình có hàng chữ | màn hình chỉ có đồ thị trừu tượng, cấm menu/bảng |
| `t40_a2_28_…lonely_motel_neon` | biển gỉa có dãi ký tự | bỏ dãi ký tự → “no fascia text” |

**Lần 2 & 3 — riêng ảnh bản đồ T40:** sau lần 1 còn 2 bảng nhỏ trên bản đồ có chữ giả (lần 2) rồi còn 3 dòng chữ ở góc màn hình (lần 3) ⇒ sửa prompt lần 2 (bỏ legend/bảng) và lần 3 (chuyển màn hình sang trạng thái **tắt**, màn hình đen trắng trơn). Ảnh cuối: bản đồ trơn + sợi chỉ hổ phách + màn hình đen, **không còn ký tự nào** (đã soi zoom full-res).

**Kết quả cuối:**
- Kích thước: **19/19 đúng 2112×1188**.
- Chữ AI: **0** còn sót sau 3 lượt soi + zoom full-res.
- Người trong khung: chỉ ở dạng bóng / khuất mặt (H1/V5) — không lộ mặt nạn nhân hay nghi phạm.
- Không mô tả bạo lực, thương tích, thi thể (V9).
- Tập 26: **176 job / 176 ảnh, thừa 0**. Tập 40: **154 job / 154 ảnh, thừa 1** (xem mục 7).

---

## 5. Sổ xuất xứ `provenance.json` (L7)

- +16 dòng mới (19 ảnh lô đầu), 5 dòng cập nhật (lô detext), 1 dòng cập nhật (lô detext2), 1 dòng cập nhật (lô detext3) ⇒ **lượt này thêm 48 dòng mới + cập nhật 7 dòng**.
- **Bổ sung thêm 32 dòng cho 32 ảnh `_x` của Tập 26** — lô sinh 24/11/2026 trước đó quên ghi sổ (vi phạm L7). Seed **dựng lại** theo công thức lô `260000 + index*7 + 13` của `deploy_t26_30.py` (tại thời điểm đó Tập 26 đúng 32 job thiếu = 32 job `_x`); ghi rõ trong `ghi_chu` là seed dựng lại.
- Tổng sổ tại lúc kiểm: **6.181 dòng** (dự án có nhiều phiên làm song song nên tổng số còn tăng trong lúc chạy); **mọi ảnh `t26_*` và `t40_*` trên đĩa đều có dòng sổ (0 thiếu)**.
- Sao lưu trước khi sửa: `.work/_cu/provenance_backup_before_t26_t40_20261125.json`, `.work/_cu/provenance_backup_before_t26_x32_20261125.json`.

---

## 6. Cổng kiểm (H28)

```
py -3 .work/map_shot_anh.py --check 26   → ĐẠT · 176 shot · lỗi mapping 0 · ảnh thiếu file 0
py -3 .work/map_shot_anh.py --check 40   → ĐẠT · 154 shot · lỗi mapping 0 · ảnh thiếu file 0
```

---

## 7. Việc còn lại (cần người dùng quyết)

1. **Ảnh thừa Tập 40:** `assets/bg/t40_a5_27_final_amber_eyes_insignia_seal.png` (4,6 MB) là ảnh cũ đã bị job mới thay thế (đã có bản sao ở `.work/_cu/bg_old_20261125/t40_replaced/`). Mục VI.5 của báo cáo thống kê yêu cầu **xoá khỏi `assets/bg/`** để H22 không còn ảnh thừa ⇒ **chờ người dùng duyệt xoá** (L4: xoá thành phẩm phải hỏi).
2. **2 dòng sổ tên cũ** trong `provenance.json` (`t40_a2_14_political_campaign_office_posters`, `t40_a5_27_final_amber_eyes_insignia_seal`) chưa dọn — ảnh cũ đã bị thay, giữ dòng sổ làm lịch sử.
3. **`.work/_staging_bg_jobs/bg_jobs_tap40.json`** là bản cũ (chưa có 5 job `b`, tên cũ) — **không chạy `_sync_bg_jobs.py`** nếu chưa cập nhật, tránh ghi đè bản job mới.

---

## 8. Script đã tạo (tái lập được)

| File | Việc |
|---|---|
| `.work/kaggle_flux/deploy_t26_t40_missing.py` | dựng + đẩy 2 kernel cho 19 ảnh thiếu |
| `.work/kaggle_flux/watch_t26_t40_missing.py` | theo dõi, tải, giải nén, ghi `assets/bg/`, cập nhật `provenance.json` |
| `.work/kaggle_flux/fix_detext_t26_t40.py` | sửa prompt 5 ảnh chữ AI + đẩy kernel lô detext |
| `.work/kaggle_flux/watch_detext_t26_t40.py` | watcher lô detext (5 ảnh) |
| `.work/kaggle_flux/fix_detext2_t40_map.py` | sinh lại ảnh bản đồ (lần 2) |
| `.work/kaggle_flux/fix_detext2_map` → `watch_detext2_map.py` | watcher lô detext2 |
| `.work/kaggle_flux/fix_detext3` (chạy inline) + `watch_detext3_map.py` | sinh lại ảnh bản đồ (lần 3) + watcher |
| `.work/kaggle_flux/qc_t26_t40_new.py` | QC kích thước + job thiếu + ảnh thừa + montage soi mắt |
| `.work/kaggle_flux/patch_provenance_t26_x32.py` | bổ sung 32 dòng sổ cho ảnh `_x` Tập 26 |

**Media không commit** (L10): `assets/bg/*.png` nằm ngoài git; chỉ tài liệu + script + `provenance.json` + `bg_jobs_tap40.json` thay đổi trong working tree.
