# BÁO CÁO ẢNH NỀN DỌC — CLIP TIKTOK TẬP 05

*Ngày: 24/11/2026 · Bộ ảnh: `assets/bg/tk05_*.png` (34 nền dọc 9:16)*
*Kế hoạch: `02_SAN_XUAT/TIKTOK/Tap05/KE_HOACH_CLIP_TAP05.md` (VN) · `Tap05_EN/` · `Tap05_JA/` · Mẫu báo cáo: `Tap04/BAO_CAO_ANH_NEN_DOC_TAP04.md`*

---

## 1. Tóm tắt

| Hạng mục | Số đo thật |
|---|---|
| Số nền dọc dựng | **34/34** — đủ cho **54 shot** của 5 clip (TK1 11 · TK2 10 · TK3 10 · TK4 11 · TK5 12) |
| Kích thước | **1080×1920 — 34/34 đúng**, sai số 0 |
| Nguồn | **12 nền AI thật** (MiniMax `connector__matrix__generate_image`, 9:16, area 2K, dùng ảnh 16:9 gốc `t5_*` làm ảnh tham chiếu) + **22 nền dự phòng** (cắt 9:16 từ ảnh nền 16:9 gốc — vì hết allowance) |
| Chi phí | **0 đồng** (không bật credit auto-consumption) |
| Shot thiếu nền | **0** ở cả VI / EN / JA · nền sai kích thước: **0** |
| Dòng `provenance.json` | **34** (12 dòng có `prompt` = AI thật · 22 dòng `prompt: null` = dự phòng) |
| Vùng chữ hook (y 270–730, x 120–780) | TB **43,8** (ngưỡng ≤ 58) · **0 ảnh** vượt |
| Vùng chữ phụ đề (y 996–1254, x 120–780) | TB **58,3** (ngưỡng ≤ 72) · **0 ảnh** vượt |
| Vệt sáng ngang trong vùng chữ | **0 ảnh** (ngưỡng 0,70) |
| H22 (mỗi nền ≤ 3 shot / ≤ 30 s) | **0 vi phạm** ở cả VI / EN / JA (đo theo `est_duration_s` trong spec) |
| Tổng dung lượng | ~103 MB (media bị `.gitignore` loại — không commit, L10) |

---

## 2. Quy trình đã chạy (tái lập được)

| Bước | Lệnh | Kết quả |
|---|---|---|
| 1 | `py -3 .work/_tk_scan_t05.py` | Quét `KE_HOACH_CLIP_TAP05.md` → 54 shot · 32 nền duy nhất · 1 tên nền không có ảnh gốc (`t5_closing_desk`) → `.work/_tk05_bg_needed.json` |
| 2 | `py -3 .work/_tk_gen_bg_t05.py 6` | Upload ref → `generate_image` (9:16, area 2K) → receipt `_tk_img_receipt_t05_b*.json` → lô 1–2 **12/12 thành công**, lô 3 trả `402` |
| 3 | `py -3 .work/_tk_download_imgs_t05.py` | Tải **12/12** ảnh AI về `.work/tk_img_raw_t05/` (node_id → `get_asset_url`) |
| 4 | `py -3 .work/_tk_postprocess_t05.py` | Cánh 9:16 → LANCZOS 1080×1920 + grade noir (sat 0,65 · contrast 1,15) + vignette 45 % + hạt phim 35mm + tối vùng chữ **strict** → 12 nền AI |
| 5 | `py -3 .work/_tk_fallback_crop_t05.py` | Dự phòng **20 nền còn thiếu** (0 đồng) |
| 6 | `py -3 .work/_tk_extra_bg_t05.py` | Dự phòng **2 nền tách thêm** cho TK4 (H22) |
| 7 | `py -3 .work/_tk_patch_bgname_t05.py` | Đổi tên nền `t5_*` → `tk05_*` trong 3 kế hoạch + 3 spec + tách 2 shot TK4 · kiểm chứng 6/6 file |
| 8 | `py -3 .work/_tk_h22_t05.py` | Đo H22 theo `est_duration_s` — **0 vi phạm** ở cả 3 ngôn ngữ |
| 9 | `py -3 .work/_tk_verify_final_t05.py` | 34 nền · 34/34 đúng kích thước · 0 vượt ngưỡng · 54/54 shot có nền × 3 ngôn ngữ · provenance 34 dòng đủ trường |

---

## 3. Danh sách 34 nền dọc và nguồn

| # | Nền dọc | Ảnh 16:9 gốc | Nguồn | Clip dùng |
|---:|---|---|---|---|
| 1 | `tk05_handwritten_note_floppy` | `t5_handwritten_note_floppy.jpg` | **AI thật** | TK1 #1 #2 |
| 2 | `tk05_newspaper_classified_494` | `t5_newspaper_classified_494.jpg` | **AI thật** | TK1 #3 |
| 3 | `tk05_purple_floppy_disk` | `t5_purple_floppy_disk.png` | **AI thật** | TK1 #4 |
| 4 | `tk05_digital_forensics_lab` | `t5_digital_forensics_lab.png` | **AI thật** | TK1 #5 |
| 5 | `tk05_metadata_screen` | `t5_metadata_screen.png` | **AI thật** | TK1 #6 #7 |
| 6 | `tk05_church_website_search` | `t5_church_website_search.png` | **AI thật** | TK1 #8 |
| 7 | `tk05_interrogation_confrontation` | `t5_interrogation_confrontation.png` | **AI thật** | TK1 #9 #10 |
| 8 | `tk05_amber_eyes_dossier_05` | `t5_amber_eyes_dossier_05.png` | **AI thật** | TK1 #11 · TK2 #10 · TK3 #10 · TK4 #11 · TK5 #1 (CTA) |
| 9 | `tk05_rader_house_park_city` | `t5_rader_house_park_city.png` | **AI thật** | TK2 #1 #2 · TK4 #2 #3 |
| 10 | `tk05_lutheran_church_exterior` | `t5_lutheran_church_exterior.png` | **AI thật** | TK2 #3 |
| 11 | `tk05_scout_camp_campfire` | `t5_scout_camp_campfire.png` | **AI thật** | TK2 #4 |
| 12 | `tk05_compliance_truck_street` | `t5_compliance_truck_street.png` | **AI thật** | TK2 #5 |
| 13 | `tk05_compliance_measuring_tape` | `t5_compliance_measuring_tape.png` | dự phòng | TK2 #6 |
| 14 | `tk05_two_faces_silhouette` | `t5_two_faces_silhouette.jpg` | dự phòng | TK2 #7 |
| 15 | `tk05_concrete_wall_divide` | `t5_concrete_wall_divide.framefix.png` | dự phòng | TK2 #8 |
| 16 | `tk05_family_dinner_warmth` | `t5_family_dinner_warmth.png` | dự phòng | TK2 #9 · TK4 #6 |
| 17 | `tk05_fear_of_oblivion` | `t5_fear_of_oblivion.png` | dự phòng | TK3 #1 |
| 18 | `tk05_detective_war_room` | `t5_detective_war_room.png` | dự phòng | TK3 #2 |
| 19 | `tk05_book_manuscript_desk` | `t5_book_manuscript_desk.png` | dự phòng | TK3 #3 #4 |
| 20 | `tk05_narcissist_mirror_shadow` | `t5_narcissist_mirror_shadow.png` | dự phòng | TK3 #5 #6 |
| 21 | `tk05_btk_signature_letter` | `t5_btk_signature_letter.png` | dự phòng | TK3 #7 |
| 22 | `tk05_factor_x_shadow` | `t5_factor_x_shadow.png` | dự phòng | TK3 #8 |
| 23 | `tk05_projection_mask` | `t5_projection_mask.png` | dự phòng | TK3 #9 |
| 24 | `tk05_kerri_rawson_tears` | `t5_kerri_rawson_tears.png` | dự phòng | TK4 #1 #4 #5 |
| 25 | `tk05_highway_takedown_arrest` | `t5_highway_takedown_arrest.png` | dự phòng | TK4 #7 |
| 26 | `tk05_shattered_mask_confession` | `t5_shattered_mask_confession.jpg` | dự phòng | TK4 #8 |
| 27 | `tk05_narcissistic_throne` | `t5_narcissistic_throne.png` | dự phòng | TK4 #9 (tách H22) |
| 28 | `tk05_darkened_house_exterior` | `t5_darkened_house_exterior.jpg` | dự phòng | TK4 #10 (tách H22) |
| 29 | `tk05_solitary_confinement_cell` | `t5_solitary_confinement_cell.png` | dự phòng | TK5 #2 |
| 30 | `tk05_redflag_rule_control` | `t5_redflag_rule_control.png` | dự phòng | TK5 #3 #4 |
| 31 | `tk05_redflag_shallow_affect` | `t5_redflag_shallow_affect.png` | dự phòng | TK5 #5 #6 |
| 32 | `tk05_redflag_secret_trophies` | `t5_redflag_secret_trophies.jpg` | dự phòng | TK5 #7 #8 |
| 33 | `tk05_redflag_narcissistic_hubris` | `t5_redflag_narcissistic_hubris.jpg` | dự phòng | TK5 #9 #10 |
| 34 | `tk05_closing_desk` | `t5_closing_typewriter_rose.png` | dự phòng | TK5 #11 #12 |

**Prompt dùng để sinh** (giống hệt bộ `tk01_*`…`tk04_*` đã xuất bán — xem `_tk_src_t05.py`):
*"A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, cold desaturated grey-blue palette… Recompose the scene of Picture 1 as a full-bleed vertical 9:16 illustration… keep the upper third and the lower third as quiet, dark, low-contrast shadow areas… strictly no text, no letters, no numbers, no signs, no logos, no watermark."*

---

## 4. Bẫy gặp được và cách xử lý

| # | Bẫy | Cách xử lý |
|---|---|---|
| **B1** | **Hết allowance MiniMax sau 12 ảnh** — lô 1–2 = 12/12 thành công, lô 3 trả `402` *"the plan allowance cannot cover this image generation and credit auto-consumption is turned off on this account… at least 100 credits of balance are required"*. Thử lại 1 ảnh lúc 08:52 → **vẫn `402`** ⇒ chặn cứng, không phải `429` tạm thời | Dừng pipeline AI, dự phòng **22 nền còn lại** bằng crop 9:16 từ ảnh 16:9 gốc (0 đồng). **Không** bật credit auto-consumption. Nâng lên AI thật: bật *Settings → Usage & model → Credits → credit auto-consumption* (phải là **credit đã mua**; credit check-in miễn phí không dùng được cho sinh ảnh) rồi chạy lại `.work/_tk_gen_bg_t05.py` → `_tk_download_imgs_t05.py` → `_tk_postprocess_t05.py` |
| **B2** | **`t5_closing_desk` không có ảnh gốc** trong `assets/bg/_raw/` | Khớp sang ảnh gốc **thật** của Tập 05: `t5_closing_typewriter_rose.png` (ảnh kết tập, dùng ở shot 5.10#1–#3 bản YouTube — xác nhận qua `Danh_Sach_Anh_Tap05.md`) |
| **B3** | **Cột Nền trong bảng shot + trường `bg` trong spec trỏ `t5_*`** (tên ảnh gốc 16:9) trong khi file dọc là `tk05_*` ⇒ script dựng video sẽ crash `THIEU NEN assets/bg/t5_*.png` (34 ảnh đó nằm ở `assets/bg/_raw/`) | `.work/_tk_patch_bgname_t05.py` đổi 54 token × 6 file (3 kế hoạch + 3 spec) → `tk05_*`, đúng quy ước Tập 02/03/04. Backup: `.work/_cu/tk05_bgname_20261124_1210/`. Regex chặn tiền tố `tk`/`tk0` để không ra `tk05_t5_x` |
| **B4** | **TK4 vi phạm H22**: 1 nền dùng **5 shot / 37,0 s** (VI) — vượt cả giới hạn 3 shot lẫn 30 s | Tách 2 shot sang 2 nền mới từ ảnh 16:9 gốc **chưa dùng** của Tập 05: `TK4.01#9` → `tk05_narcissistic_throne` (2.02·3.06 — chiếc ghế bành dưới ánh đèn độc tôn) · `TK4.01#10` → `tk05_darkened_house_exterior` (2.02#1–#2 — hiện trường nhà đơn lập trong đêm tối). Cả 2 nền khớp chủ đề "bóng ma gia đình" của TK4. Sau khi tách: **0 vi phạm H22** ở cả VI/EN/JA |
| **B5** | **Đo bằng RGB-average lúc crop nhưng QC đo bằng luminance L** ⇒ 2 nền lệch 0,9 điểm (72,9 > ngưỡng 72) | Sửa `darken_text_bands()` **đo bằng grayscale L** ngay trong lúc tối (giống `darken_bands_strict()` của bản AI) ⇒ đo lại sau khi sinh **0 ảnh** vượt |
| **B6** | **Ảnh AI 9:16 không bảo đảm vùng chữ tối** (bài học T35 của Tập 02) | `darken_bands_strict()` chọn `depth` theo 3 điều kiện: mean hook ≤ 58 · mean sub ≤ 72 · **không dòng nào > 70 % pixel vượt ngưỡng 120** ⇒ kết quả **0/34** vượt ngưỡng, 0 vệt ngang |
| **B7** | **Nguồn MiniMax 1536×2720 lệch ~0,4 % so với 9:16** | Cánh về đúng 9:16 **trước**, rồi mới LANCZOS 1080×1920 (nếu resize trực tiếp sẽ méo) |
| **B8** | **`upload_temp_url` hết hạn sau 1 giờ** | Upload ngay trước mỗi lô, không tái dùng URL cũ |
| **B9** | **File JPEG tải về bị cắt cụt** (`OSError: image file is truncated (98 bytes not processed)`) | Move file hỏng sang `.work/_cu/` + tải lại ⇒ **12/12** ảnh thô hợp lệ (`Image.verify()` OK) |

---

## 5. QC bằng mắt (H1 / H2 / H19 / H20) — **người dùng thực hiện**

Theo yêu cầu, phần soi mắt (chữ AI vẽ, lộ mặt, tràn viền, khớp nội dung lời thoại) **do người dùng QC**, không tự động hoá. Bộ 34 nền nằm ở `assets/bg/tk05_*.png` để soi trực tiếp.

Gợi ý thứ tự soi (nhóm rủi ro cao trước):
1. `tk05_metadata_screen` · `tk05_newspaper_classified_494` · `tk05_handwritten_note_floppy` — có màn hình / giấy tờ ⇒ dễ có chữ AI vẽ.
2. `tk05_lutheran_church_exterior` (hook mean 57,8 — sát ngưỡng 58) · `tk05_redflag_narcissistic_hubris` (57,7) · `tk05_two_faces_silhouette` (57,1) — nền sáng ở vùng đặt chữ.
3. `tk05_narcissistic_throne` · `tk05_darkened_house_exterior` — 2 nền tách thêm cho H22, chưa từng qua QC bằng mắt.

---

## 6. Việc còn lại (người dùng / lần sau)

1. **Soi mắt 34 nền** (mục 5) — quyết định nền nào phải sinh lại.
2. **Nâng 22 nền dự phòng thành AI thật** khi bật credit auto-consumption (xem B1). Ưu tiên theo mức độ "cắt mất chủ thể" / "ảnh chật 16:9": `two_faces_silhouette` → `redflag_secret_trophies` → `narcissistic_throne` → `darkened_house_exterior` → `shattered_mask_confession`.
3. **Dựng 5 clip 9:16** — bước 4 của `KE_HOACH_CLIP_TAP05.md` (cần 54 file WAV theo `SPEC_AUDIO_CLIP_TAP05.json`).
4. **Điền link YouTube Tập 05** vào 5 file caption (đang placeholder) + profile.
5. **Không commit media** (L10): 34 ảnh `assets/bg/tk05_*.png` bị `.gitignore` loại — chỉ commit tài liệu + script.

---

## 7. Script đã tạo (`.work/`)

`_tk_src_t05.py` (34 PAIRS + PROMPT) · `_tk_scan_t05.py` · `_tk_gen_bg_t05.py` · `_tk_download_imgs_t05.py` · `_tk_postprocess_t05.py` · `_tk_fallback_crop_t05.py` · `_tk_extra_bg_t05.py` · `_tk_patch_bgname_t05.py` · `_tk_h22_t05.py` · `_tk_verify_final_t05.py`
