# BÁO CÁO ẢNH NỀN DỌC — CLIP TIKTOK TẬP 04

*Ngày: 21/11/2026 · Bộ ảnh: `assets/bg/tk04_*.png` (23 nền dọc 9:16)*
*Kế hoạch: `02_SAN_XUAT/TIKTOK/Tap04/KE_HOACH_CLIP_TAP04.md` (VN) · `Tap04_EN/` · `Tap04_JA/` · Quy trình chung: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` mục 4 (Bước 4) + mục 14 (bản ghi Tập 02) · Mẫu báo cáo: `Tap03/BAO_CAO_ANH_NEN_DOC_TAP03.md`*

---

## 1. Tóm tắt

| Hạng mục | Số đo thật |
|---|---|
| Số nền dọc dựng | **23/23** — đủ cho **48 shot** của 5 clip (TK1 9 · TK2 11 · TK3 10 · TK4 9 · TK5 9) |
| Kích thước | **1080×1920 — 23/23 đúng**, sai số 0 |
| Nguồn | **6 nền AI thật** (MiniMax `connector__matrix__generate_image`, 9:16, area 2K, dùng ảnh 16:9 `t4_*` làm ảnh tham chiếu) + **17 nền dự phòng** (cắt 9:16 từ ảnh nền 16:9 gốc — vì hết allowance) |
| Chi phí | **0 đồng** |
| Shot thiếu nền | **0** · nền sai kích thước: **0** |
| Dòng `provenance.json` | **23** (6 dòng có `prompt` = AI thật · 17 dòng `prompt: null` = dự phòng) |
| Vùng chữ hook (y 270–730, x 120–780) | TB **44,7** (ngưỡng ≤ 58) · **0 ảnh** vượt |
| Vùng chữ phụ đề (y 996–1254, x 120–780) | TB **51,1** (ngưỡng ≤ 72) · **0 ảnh** vượt |
| Vệt sáng ngang trong vùng chữ | **0 ảnh** (ngưỡng 0) |
| Tổng dung lượng | 69,3 MB (media bị `.gitignore` loại — không commit, L10) |

**So sánh 4 bộ nền dọc đã có** (cùng phép đo):

| Bộ | Số ảnh | hook mean | sub mean | ảnh có vệt ngang | ảnh vượt ngưỡng |
|---|---:|---:|---:|---:|---:|
| `tk01_*` (đã đăng) | 16 | 41,6 | **82,1** | **5** | **11** |
| `tk02_*` | 26 | 31,3 | 61,4 | 1 | 0 |
| `tk03_*` | 28 | 45,1 | 53,4 | 0 | 0 |
| **`tk04_*` (bộ này)** | **23** | **44,7** | **51,1** | **0** | **0** |

⇒ Bộ `tk04_*` tối hơn `tk01_*` (bộ đã đăng) ở cả 2 vùng chữ, và là bộ sạch nhất: **0 vệt ngang, 0 ảnh vượt ngưỡng** — chữ trắng đọc tốt trên nền này.

---

## 2. Quy trình đã chạy (tái lập được)

| Bước | Lệnh | Kết quả |
|---|---|---|
| 1 | `py -3 .work/_tk_scan_t04.py` | Quét `KE_HOACH_CLIP_TAP04.md` → 48 shot · 23 nền duy nhất · phát hiện 5 tên nền không có ảnh gốc → `.work/_tk04_bg_needed.json` |
| 2 | `py -3 .work/_tk_src_montage_t04.py` | Contact sheet 23 ảnh nguồn 16:9 — soi mắt phong cách + khớp lại 5 nền vướng (mục 4) |
| 3 | `py -3 .work/_tk_gen_bg_t04.py run 2 0` | Upload ref → `generate_image` (9:16, area 2K) → receipt `_tk_img_receipt_t04_b*.json` → **6/23 thành công**, lô sau trả `402` |
| 4 | `py -3 .work/_tk_download_imgs_t04.py` | Tải **6/6** ảnh AI về `.work/tk_img_raw_t04/` (node_id → `get_asset_url`) |
| 5 | `py -3 .work/_tk_postprocess_t04.py` | LANCZOS 1080×1920 + grade noir (sat 0,65 · contrast 1,15) + vignette 45 % + hạt phim 35mm + tối vùng chữ **strict** → 6 nền AI |
| 6 | `py -3 .work/_tk_fallback_crop_t04.py` | Dự phòng **17 nền còn thiếu** (0 đồng) |
| 7 | `py -3 .work/_tk_fix_border_t04.py tk04_somerset_courtroom` | Cắt viền giả cổ còn sót trong ảnh gốc → làm lại crop 9:16 (mục 4, B3) |
| 8 | `py -3 .work/_tk_fix_dark_t04.py tk04_somerset_courtroom` | Tối thêm 1 bậc cho ảnh vừa cắt viền (hook 58,1 → 54,7) |
| 9 | `py -3 .work/_tk_measure_bg_t04.py` | Đo 23 ảnh + dựng contact sheet `.work/_tk04_montage.png` |
| 10 | `py -3 .work/_tk_qc_coverage_t04.py` | Phủ **48/48 shot** · 23/23 nền · provenance đủ |
| 11 | `py -3 .work/_tk_patch_bgname_t04.py` | Đổi tên nền `t4_*` → `tk04_*` trong 3 kế hoạch + 3 spec · kiểm chứng 6/6 file |

---

## 3. Danh sách 23 nền dọc và nguồn

| # | Nền dọc | Ảnh 16:9 gốc | Nguồn | Dùng ở shot |
|---:|---|---|---|---|
| 1 | `tk04_pyxis_station` | `t4_pyxis_station.png` | **AI thật** | TK1 #1 #2 #3 · TK5 #5 |
| 2 | `tk04_pyxis_drawer_ajar` | `t4_pyxis_drawer_ajar.jpg` | **AI thật** | TK1 #4 #5 |
| 3 | `tk04_pyxis_printout` | `t4_pyxis_printout.jpg` | **AI thật** | TK1 #6 |
| 4 | `tk04_neutral_letter` | `t4_neutral_letter.png` | **AI thật** | TK1 #7 · TK4 #5 |
| 5 | `tk04_institutional_bystander` | `t4_institutional_bystander.png` | **AI thật** | TK1 #8 · TK2 #10 · TK4 #7 |
| 6 | `tk04_closing_desk` | `t4_cullen_law_doc.png` | **AI thật** | TK1 #9 · TK2 #11 · TK3 #10 · TK4 #9 · TK5 #8 #9 |
| 7 | `tk04_nurse_station` | `t4_nurse_station.png` | dự phòng | TK2 #1 · TK5 #6 |
| 8 | `tk04_somerset_exterior` | `t4_somerset_exterior.png` | dự phòng | TK2 #2 #3 · TK4 #2 · TK5 #3 |
| 9 | `tk04_icu_night` | `t4_icu_night.png` | dự phòng | TK2 #4 |
| 10 | `tk04_cullen_silhouette` | `t4_cullen_silhouette.png` | dự phòng | TK2 #5 |
| 11 | `tk04_code_blue_aftermath` | `t4_code_blue_aftermath.png` | dự phòng | TK2 #6 |
| 12 | `tk04_breakroom_night` | `t4_breakroom_night.jpg` | dự phòng | TK2 #7 #8 |
| 13 | `tk04_corridor_shadow` | `t4_corridor_shadow.jpg` | dự phòng | TK2 #9 |
| 14 | `tk04_diner_exterior` | `t4_somerville_diner.jpg` | dự phòng | TK3 #1 #2 |
| 15 | `tk04_diner_booth` | `t4_diner_table.png` | dự phòng | TK3 #3 #7 #8 |
| 16 | `tk04_amy_scrubs` | `t4_amy_scrubs.jpg` | dự phòng | TK3 #4 #5 · TK5 #7 |
| 17 | `tk04_wire_closeup` | `t4_wire_recorder.png` | dự phòng | TK3 #6 |
| 18 | `tk04_interrogation_room` | `t4_interrogation_room.png` | dự phòng | TK3 #9 |
| 19 | `tk04_ten_hospitals_map` | `t4_ten_hospitals_map.jpg` | dự phòng | TK4 #1 #3 #4 |
| 20 | `tk04_case_file_open` | `t4_case_file_open.png` | dự phòng | TK4 #6 |
| 21 | `tk04_courtroom_bench` | `t4_judge_gavel.png` | dự phòng | TK4 #8 · TK5 #4 |
| 22 | `tk04_somerset_courtroom` | `t4_somerset_courtroom.jpg` | dự phòng | TK5 #1 |
| 23 | `tk04_boardroom_empty` | `t4_boardroom_empty.png` | dự phòng | TK5 #2 |

**Prompt dùng để sinh (giống hệt bộ `tk01_*`/`tk02_*`/`tk03_*` đã xuất bán):**
*"A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, cold desaturated grey-blue palette, faded eerie retro colors, decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style… Recompose the scene of Picture 1 as a full-bleed vertical 9:16 illustration… keep the upper third and the lower third as quiet, dark, low-contrast shadow areas… strictly no text, no letters, no numbers, no signs, no logos, no watermark."*

---

## 4. Bẫy gặp được và cách xử lý

| # | Bẫy | Cách xử lý |
|---|---|---|
| **B1** | **Hết allowance MiniMax sau 6 ảnh** (lô 1–3 = 6/6 thành công, lô 4 trả `402` *"the plan allowance cannot cover this image generation and credit auto-consumption is turned off on this account… at least 100 credits of balance are required"*). Thử lại lô khác → **vẫn `402`** ⇒ chặn cứng, không phải `429` tạm thời | Dừng pipeline AI, dự phòng **17 nền còn lại** bằng crop 9:16 từ ảnh 16:9 gốc (0 đồng). Nâng lên AI thật: bật **Settings → Usage & model → Credits → credit auto-consumption** (phải là **credit đã mua**, credit check-in miễn phí không dùng được cho sinh ảnh) rồi chạy lại `.work/_tk_gen_bg_extra_t04.py` → `_tk_download_imgs_t04.py` → `_tk_postprocess_t04.py` (script tự backup ảnh cũ vào `.work/_cu/` và cập nhật đúng dòng `provenance.json`) |
| **B2** | **5 tên nền trong kế hoạch KHÔNG tồn tại** ở `assets/bg/_raw/`: `t4_closing_desk`, `t4_courtroom_bench`, `t4_diner_booth`, `t4_diner_exterior`, `t4_wire_closeup` | Khớp lại theo **mô tả nội dung từng ảnh** trong `02_SAN_XUAT/Tap04/Danh_Sach_Anh_Tap04.md`: `closing_desk`→`t4_cullen_law_doc` (bìa hồ sơ trên bàn) · `courtroom_bench`→`t4_judge_gavel` (búa trên bàn xử) · `diner_booth`→`t4_diner_table` (bàn ăn trong quán) · `diner_exterior`→`t4_somerville_diner` (mặt tiền quán) · `wire_closeup`→`t4_wire_recorder` (thiết bị ghi âm bí mật). Giữ **nguyên tên `tk04_*`** trong clip để không phá bảng shot |
| **B3** | **`t4_somerset_courtroom.jpg` còn viền giả cổ màu kem** ở trên + dưới (đo: meanL 225 ở 25 hàng đầu, 222 ở 34 hàng cuối) ⇒ vi phạm V7 (ảnh phải tràn viền) | `.work/_tk_fix_border_t04.py` cắt viền kem ra khỏi ảnh gốc **trước khi** crop 9:16, rồi chạy lại `safe_text_zone` + `darken_text_bands`. Đo lại: mép trên 33,2 · mép dưới 33,8 (trước khi sửa: 114,5 / 113,2) |
| **B4** | **Crop 9:16 làm lệch chủ thể** (bất đắc kỳ thuật với ảnh 16:9) | `best_window()` chọn cửa sổ 9:16 có năng lượng nét cao nhất, lệch tối đa 22 % so với tâm ảnh; đã soi lại từng nền trên contact sheet — không nền nào mất chủ thể chính |
| **B5** | **`interrogation_room` đo được hook mean 58,3** (chỉ vượt 0,3) | `.work/_tk_fix_dark_t04.py` tối thêm 1 bậc ⇒ hook **54,9**, sub 46,2 |
| **B6** | **Ảnh AI 9:16 không bảo đảm vùng chữ tối** (bài học T35 của Tập 02) | `darken_bands_strict()` chọn `depth` theo 3 điều kiện: mean hook ≤ 58 · mean sub ≤ 72 · **không dòng nào > 70 % pixel vượt ngưỡng 120** ⇒ kết quả **0/23** vượt ngưỡng, 0 vệt ngang |
| **B7** | **Sai khác giữa cách đo RGB-average lúc crop và luminance L lúc đo lại** (bài học B5 của Tập 03) | Ảnh dự phòng tối tới mức "vừa chạm" ngưỡng theo RGB (55–58) thì khi đo lại bằng L vẫn có thể vượt ⇒ **luôn đo lại bằng luminance sau khi sinh**, rồi tối thêm nếu cần (`_tk_fix_dark_t04.py`) |
| **B8** | **URL ảnh tham chiếu `upload_temp_url` hết hạn sau 1 giờ** | Upload ngay trước mỗi lô, không tái dùng URL cũ |
| **B9** | **Chạy lại generator với `start index` sẽ GHI ĐÈ receipt của lô cũ** (bộ đếm `tag` khởi động lại từ `b1`) ⇒ mất `node_id` của 2 ảnh đã sinh thành công | Khôi phục bằng cách dựng lại receipt từ `node_id` đã in ra log (`tk04_pyxis_station` → `465602453520581`, `tk04_pyxis_drawer_ajar` → `465601074163895`) → tải lại qua `get_asset_url` (**node_id vĩnh viễn, không mất**). Lần sau: đặt `tag` theo timestamp, không theo chỉ số lô |

---

## 5. QC bằng mắt (H1 / H2 / H19 / H20 — soi 100 % nền mới)

- **Soi 100 %**: 23/23 nền dọc mới (contact sheet `.work/_tk04_montage.png` + tờ zoom 1:1 `.work/_tk04_zoom.png` cho 6 ảnh rủi ro cao: sân viền · tranh trong khung · chữ trên giấy · bản đồ).
- **Phong cách**: đúng graphic-novel noir của kênh (nét mực đen, chiaroscuro, palette xám–xanh lạnh, hạt phim 35 mm) — khớp bộ `tk01_*`/`tk02_*`/`tk03_*` đã đăng và khớp 51 ảnh 16:9 gốc của Tập 04.
- **Người thật chỉ hiện dạng bóng (H1/V5)**: `cullen_silhouette` (quay lưng hoàn toàn, không mặt) · `amy_scrubs` (không có người; chỉ đồng phục gấp + tranh nét trong khung, **không có khuôn mặt**) ⇒ **0 khuôn mặt lộ**.
- **Chữ lạ / watermark**: soi zoom 1:1 các vùng nghi ngờ (bìa hồ sơ, nhật ký máy, bản đồ, giấy tờ) ⇒ **không có chữ đọc được**; các vạch trên tờ giấy là nét vẽ mờ / khối đen, không thành chữ.
- **Nội dung khớp lời (H3/H19)**: đọc tên nền ra được cảnh cụ thể — `pyxis_station` = tủ thuốc tự động · `pyxis_drawer_ajar` = ngăn kéo thuốc · `ten_hospitals_map` = bản đồ 9 bệnh viện + 1 viện dưỡng lão · `courtroom_bench` = búa công lý · `diner_exterior` = mặt tiền quán đêm · `wire_closeup` = máy ghi âm bí mật · `institutional_bystander` = hành lang bệnh viện vắng tanh.
- **Tràn viền (V7)**: đo mép trên/dưới của cả 23 ảnh ⇒ **không ảnh nào có viền sáng** (sau khi sửa `somerset_courtroom`).

---

## 6. Đổi tên nền trong kịch bản clip: `t4_*` → `tk04_*` (21/11/2026)

**Vấn đề:** cột Nền trong bảng shot (mục 2.1–2.5) và trường `bg` trong `SPEC_AUDIO_CLIP_TAP04.json` trỏ tới `t4_*` — tên ảnh gốc **16:9**. Script dựng video đọc `assets/bg/<nen>.png` ⇒ khi chạy sẽ crash `THIEU NEN assets/bg/t4_*.png` (23/23 ảnh đó nằm ở `assets/bg/_raw/`, không tồn tại trong `assets/bg/`).

**Cách sửa (đúng quy ước Tập 02/Tập 03 — `tk02_*`/`tk03_*` trong clip, `t2_*`/`t3_*` là ảnh gốc):**

| Nơi | Sửa |
|---|---|
| `KE_HOACH_CLIP_TAP04.md` (VN) | 48 dòng bảng shot → `tk04_*` |
| `KE_HOACH_CLIP_TAP04_EN.md` | 48 dòng bảng shot → `tk04_*` |
| `KE_HOACH_CLIP_TAP04_JA.md` | 48 dòng bảng shot → `tk04_*` |
| `SPEC_AUDIO_CLIP_TAP04.json` (VN/EN/JA) | 48 × 3 trường `bg` → `tk04_*` |

**Kiểm chứng sau khi chạy:** cả 3 kế hoạch và cả 3 spec trỏ đúng **23 nền `tk04_*`**; **mọi file được trỏ tới đều tồn tại** trong `assets/bg/`; **0 token `t4_` còn sót**; **0 token ngoài danh sách 23 nền**; caption + mô tả ngắn/dài **không đổi**.

Backup trước khi sửa: `.work/_cu/tk04_bgname_20261121_0852/` (6 file kế hoạch + spec).

> ⚠ **Bẫy khi tự vá tên:** `re.sub(r"\bt4_([a-z0-9_]+)\b", ...)` phải chặn tiền tố `tk`/`tk0` để không ra `tk04_t4_x`. Script dùng `(?<!tk)(?<!tk0)\bt4_(...)\b` + kiểm chứng 2 vòng.

---

## 7. Việc còn lại (người dùng / lần sau)

1. **Nâng 17 nền dự phòng thành AI thật** khi bật credit auto-consumption (xem B1). Ưu tiên theo mức độ "cắt mất chủ thể" / "ảnh chật 16:9": `somerset_exterior` → `icu_night` → `code_blue_aftermath` → `diner_exterior` → `boardroom_empty`.
2. **Dựng 5 clip 9:16** — bước 4 của `KE_HOACH_CLIP_TAP04.md` (cần 48 file WAV theo `SPEC_AUDIO_CLIP_TAP04.json`).
3. **Điền link YouTube Tập 04** vào 5 file caption (đang placeholder) + profile.
4. **Không commit media** (L10): 23 ảnh `assets/bg/tk04_*.png` bị `.gitignore` loại — chỉ commit tài liệu + script.

---

## 8. Script đã tạo (`.work/`)

`_tk_src_t04.py` (23 PAIRS + PROMPT) · `_tk_scan_t04.py` · `_tk_src_montage_t04.py` · `_tk_gen_bg_t04.py` · `_tk_download_imgs_t04.py` · `_tk_postprocess_t04.py` · `_tk_fallback_crop_t04.py` · `_tk_fix_border_t04.py` · `_tk_fix_dark_t04.py` · `_tk_measure_bg_t04.py` · `_tk_qc_coverage_t04.py` · `_tk_patch_bgname_t04.py`
