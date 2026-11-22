# BÁO CÁO ẢNH NỀN DỌC — CLIP TIKTOK TẬP 03

*Ngày: 20/11/2026 · Bộ ảnh: `assets/bg/tk03_*.png` (28 nền dọc 9:16)*
*Kế hoạch: `02_SAN_XUAT/TIKTOK/Tap03/KE_HOACH_CLIP_TAP03.md` · Quy trình chung: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` mục 14*

---

## 1. Tóm tắt

| Hạng mục | Số đo thật |
|---|---|
| Số nền dọc dựng | **28/28** — đủ cho **51 shot** của 5 clip (TK1 10 · TK2 10 · TK3 11 · TK4 11 · TK5 9) |
| Kích thước | **1080×1920 — 28/28 đúng**, sai số 0 |
| Nguồn | **12 nền AI thật** (MiniMax `connector__matrix__generate_image`, 9:16, area 2K, dùng ảnh 16:9 `t3_*` làm ảnh tham chiếu) + **16 nền dự phòng** (cắt 9:16 từ ảnh nền 16:9 gốc — vì hết allowance) |
| Chi phí | **0 đồng** (Kaggle/MiniMax allowance) |
| Shot thiếu nền | **0** · nền sai kích thước: **0** |
| Dòng `provenance.json` | **28** (12 dòng có `prompt` = AI thật · 16 dòng `prompt: null` = dự phòng) |
| Vùng chữ hook (y 270–730, x 120–780) | TB **45,1** (ngưỡng ≤ 58) |
| Vùng chữ phụ đề (y 996–1254, x 120–780) | TB **53,4** (ngưỡng ≤ 72) |
| Vệt sáng ngang trong vùng chữ | **0 ảnh** (ngưỡng 0) |

**So sánh bộ đã xuất bán:** `tk01_*` hook mean 41,6 · `tk02_*` (21 AI + 5 dự phòng) hook mean 30,5. Bộ `tk03_*` tối hơn `tk02_*`, sáng hơn `tk01_*` → chữ trắng vẫn đọc tốt.

---

## 2. Quy trình đã chạy (tái lập được)

| Bước | Lệnh | Kết quả |
|---|---|---|
| 1 | `py -3 .work/_tk_scan_t03.py` | Quét `KE_HOACH_CLIP_TAP03.md` → 51 shot · 28 nền duy nhất → `.work/_tk03_bg_needed.json` |
| 2 | `py -3 .work/_tk_src_montage_t03.py` | Contact sheet 28 ảnh nguồn 16:9 — soi mắt phong cách trước khi sinh |
| 3 | `py -3 .work/_tk_gen_bg_t03.py run` | Upload ref → `generate_image` (9:16, 2K) → receipt `_tk_img_receipt_t03_b1..b3.json` |
| 4 | `py -3 .work/_tk_download_imgs_t03.py` | Tải **12/12** ảnh AI về `.work/tk_img_raw_t03/` |
| 5 | `py -3 .work/_tk_postprocess_t03.py` | LANCZOS 1080×1920 + grade noir (sat 0,65 · contrast 1,15) + vignette 45 % + hạt phim 35mm + tối vùng chữ **strict** |
| 6 | `py -3 .work/_tk_fallback_crop_t03.py` | Dự phòng **16 nền còn thiếu** (0 đồng) |
| 7 | `py -3 .work/_tk_recrop_t03.py` | Crop lại 3 nền bị cắt mất chủ thể (xem mục 4) |
| 8 | `py -3 .work/_tk_measure_bg_t03.py` | Đo 28 ảnh + dựng contact sheet `.work/_tk03_montage.png` |
| 9 | `py -3 .work/_tk_qc_coverage_t03.py` | Phủ 51/51 shot · 28/28 nền · provenance đủ |

---

## 3. Danh sách 28 nền và nguồn

| # | Nền dọc | Ảnh 16:9 gốc | Nguồn | Dùng ở shot |
|---:|---|---|---|---|
| 1 | `tk03_phone_booth` | `t3_phone_booth.jpg` | **AI thật** | TK1 #1 #3 #4 #6 #7 |
| 2 | `tk03_dispatch_desk` | `t3_dispatch_desk.jpg` | **AI thật** | TK1 #2 #5 |
| 3 | `tk03_apartos_house` | `t3_apartos_house.framefix.png` | **AI thật** | TK1 #8 · TK3 #9 |
| 4 | `tk03_brain_mirror` | `t3_brain_mirror.png` | **AI thật** | TK1 #9 · TK2 #9 · TK3 #10 |
| 5 | `tk03_closing_desk` | `t3_closing_desk.png` | **AI thật** | TK1 #10 · TK2 #10 · TK3 #11 · TK4 #11 · TK5 #8 #9 |
| 6 | `tk03_bar_stool_shadow` | `t3_bar_stool_shadow.png` | **AI thật** | TK2 #1 #3 #7 #8 |
| 7 | `tk03_bar_jury_room` | `t3_bar_jury_room.png` | **AI thật** | TK2 #2 #6 |
| 8 | `tk03_galaxie` | `t3_galaxie.framefix.png` | **AI thật** | TK2 #4 |
| 9 | `tk03_hitchhiker` | `t3_hitchhiker.png` | **AI thật** | TK2 #5 · TK3 #8 |
| 10 | `tk03_basement_stairs` | `t3_basement_stairs.png` | **AI thật** | TK3 #1 #5 |
| 11 | `tk03_coal_furnace` | `t3_coal_furnace.png` | **AI thật** | TK3 #2 · TK5 #4 |
| 12 | `tk03_small_bed` | `t3_small_bed.png` | **AI thật** | TK3 #3 |
| 13 | `tk03_trapdoor` | `t3_trapdoor.png` | dự phòng | TK3 #4 |
| 14 | `tk03_mother_shadow` | `t3_mother_shadow.jpg` | dự phòng | TK3 #6 |
| 15 | `tk03_ucsc_campus` | `t3_ucsc_campus.jpg` | dự phòng | TK3 #7 |
| 16 | `tk03_vacaville_1978` | `t3_vacaville_1978.png` | dự phòng | TK4 #1 |
| 17 | `tk03_two_agents` | `t3_two_agents.png` | dự phòng | TK4 #2 |
| 18 | `tk03_giant_doorway` | `t3_giant_doorway.png` | dự phòng | TK4 #3 |
| 19 | `tk03_interview_room` | `t3_interview_room.jpg` | dự phòng | TK4 #4 |
| 20 | `tk03_cassette` | `t3_cassette.png` | dự phòng | TK4 #5 |
| 21 | `tk03_fantasy_spiral` | `t3_fantasy_spiral.png` | dự phòng | TK4 #6 · TK5 #5 |
| 22 | `tk03_trophy_box` | `t3_trophy_box.png` | dự phòng | TK4 #7 |
| 23 | `tk03_organized_split` | `t3_organized_split.png` | dự phòng | TK4 #8 |
| 24 | `tk03_self_observation` | `t3_self_observation.jpg` | dự phòng | TK4 #9 · TK5 #6 |
| 25 | `tk03_case_photos` | `t3_case_photos.png` | dự phòng | TK4 #10 |
| 26 | `tk03_red_flags` | `t3_red_flags.png` | dự phòng | TK5 #1 |
| 27 | `tk03_gift_drowned` | `t3_gift_drowned.png` | dự phòng | TK5 #2 #3 |
| 28 | `tk03_life_sentence` | `t3_life_sentence.png` | dự phòng | TK5 #7 |

**Prompt dùng để sinh (giống hệt bộ `tk01_*`/`tk02_*` đã xuất bán):**
*"A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, cold desaturated grey-blue palette, faded eerie retro colors, decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style… Recompose the scene of Picture 1 as a full-bleed vertical 9:16 illustration… keep the upper third and the lower third as quiet, dark, low-contrast shadow areas… strictly no text, no letters, no numbers, no signs, no logos, no watermark."*

---

## 4. Bẫy gặp được và cách xử lý

| # | Bẫy | Cách xử lý |
|---|---|---|
| **B1** | **Hết allowance MiniMax sau 12 ảnh** (lô 1 + lô 2 = 12/12 thành công, lô 3 trả `402` *"the plan allowance cannot cover this image generation and credit auto-consumption is turned off"*). Thử lại lô 4 ảnh → vẫn `402` | Dừng pipeline AI, dự phòng **16 nền còn lại** bằng crop 9:16 từ ảnh 16:9 gốc (0 đồng). Muốn nâng lên AI thật: bật **Settings → Usage & model → Credits → credit auto-consumption** rồi chạy lại `.work/_tk_gen_bg_extra_t03.py` → `_tk_download_imgs_t03.py` → `_tk_postprocess_t03.py` (script tự ghi đè dòng provenance và backup ảnh cũ vào `.work/_cu/`) |
| **B2** | 1 lần upload ref thất bại âm thầm (`t3_trapdoor.png`) | Script in `UPLOAD FAIL` và bỏ qua mục đó; mục đó vẫn được dự phòng crop ⇒ không mất nền nào |
| **B3** | **Crop 9:16 cắt mất chủ thể**: `two_agents` chỉ còn 1 đặc vụ · `interview_room` chỉ còn chân bàn · `mother_shadow` chỉ còn mép bóng | `.work/_tk_recrop_t03.py` chọn lại cửa sổ 9:16 theo **toạ độ tay** (giữ cả 2 đặc vụ / 1 người + bàn / trọn người), chạy lại đúng pipeline hậu kỳ, backup bản cũ vào `.work/_cu/tk03_recrop_img_*/` |
| **B4** | Ảnh AI 9:16 **không** bảo đảm vùng chữ tối (bài học T35 của Tập 02) | `darken_bands_strict()` chọn `depth` theo 3 điều kiện: mean hook ≤ 58 · mean sub ≤ 72 · **không dòng nào > 70 % pixel vượt ngưỡng 120** ⇒ kết quả **0/28** vượt ngưỡng, 0 vệt ngang |
| **B5** | `mother_shadow` đo được hook mean **58,0** — vừa chạm ngưỡng (sai khác giữa cách đo RGB-average của lúc crop và luminance L lúc đo lại) | `.work/_tk_fix_dark_t03.py` tối thêm một bậc ⇒ hook **54,7** |
| **B6** | URL ảnh tham chiếu `upload_temp_url` **hết hạn sau 1 giờ** | Upload ngay trước mỗi lô, không tái dùng URL cũ |

---

## 5. QC bằng mắt (H2 / H19 / H20 — soi 100 % nền mới)

- **Soi 100 %**: 28/28 nền dọc mới (contact sheet `.work/_tk03_montage.png` + 2 tờ zoom 1:1 `_tk03_zoom.png`, `_tk03_zoom_people.png`).
- **Phong cách**: đúng graphic-novel noir của kênh (nét mực đen, chiaroscuro, palette xám-xanh lạnh, hạt phim 35 mm) — khớp bộ `tk01_*`/`tk02_*` đã đăng và khớp 28 nền 16:9 gốc của Tập 03.
- **Người thật chỉ hiện dạng bóng (H1)**: `bar_stool_shadow` (quay lưng) · `hitchhiker` (quay lưng) · `two_agents` (quay lưng, cả 2) · `giant_doorway` (quay lưng) · `interview_room` (bóng nghiêng, không mặt) · `mother_shadow` (bóng trên tường) · `case_photos` (chỉ có bàn tay đeo găng) ⇒ **0 khuôn mặt lộ**.
- **Chữ lạ / watermark**: soi zoom 1:1 các vùng nghi ngờ (bảng cửa, giấy tờ, bìa hồ sơ, két sắt) ⇒ **không có chữ đọc được**; các vạch trên tờ giấy là nét vẽ mờ, không thành chữ.
- **Nội dung khớp lời (H3/H19)**: đọc tên nền ra được cảnh cụ thể — `brain_mirror` = não + gương nứt · `fantasy_spiral` = cầu thang xoắn ốc · `trophy_box` = thùng gỗ đóng · `trapdoor` = bàn ăn + cửa sập mở · `red_flags` = lồng chim + chìa khóa · `organized_split` = phòng bị chia đôi vệt sáng.

---

## 5b. Sửa tên nền trong kịch bản clip: `t3_*` → `tk03_*` (20/11/2026)

**Vấn đề:** cột Nền trong bảng shot (mục 2.1–2.5) và trường `bg` trong `SPEC_AUDIO_CLIP_TAP03.json` vẫn trỏ tới `t3_*` — tên ảnh gốc **16:9**. Script dựng video đọc `assets/bg/<nen>.png` ⇒ khi chạy sẽ crash `THIEU NEN assets/bg/t3_*.png` (28/28 ảnh đó không tồn tại trong `assets/bg/`, chỉ nằm ở `assets/bg/_raw/`).

**Cách sửa (theo đúng quy ước Tập 02 — `tk02_*` trong clip, `t2_*` là ảnh gốc):**

| Nơi | Sửa |
|---|---|
| `.work/_build_tk_tap03.py` | 51 giá trị `bg` trong tuple → `tk03_*`; `NEN_SRC` 28 mục → `"tk03_x": "t3_x"`; **bổ sung mục thiếu** `tk03_self_observation` (bản gốc chỉ có 27/28 ⇒ QC #8 báo thiếu raw) |
| `.work/_build_tk_tap03_multilang.py` | 102 giá trị `bg` → `tk03_*` |
| `SPEC_AUDIO_CLIP_TAP03.json` (VN/EN/JA) | 51 × 3 trường `bg` → `tk03_*` |
| `KE_HOACH_CLIP_TAP03.md` | 51 dòng bảng shot → `tk03_*` |

**Kiểm chứng sau khi chạy lại generator:** cả 3 spec trỏ đúng 28 nền `tk03_*` và **mọi file được trỏ tới đều tồn tại**; bảng shot VN 51/51 dòng dùng `tk03_*`; caption + mô tả ngắn/dài **không đổi** (so từng file với backup); 12 cổng tự kiểm của generator vẫn **ĐẠT TOÀN BỘ** (kể cả #8 "28/28 nền có file raw").

Backup trước khi sửa: `.work/_cu/tk03_bgname_20261120_2312/` (file kế hoạch + spec) · `.work/_cu/tk03_regen_20261120_2316/` (thư mục sản xuất Tap03 VN/EN/JA).

> ⚠ **Bẫy khi tự vá tên:** `re.sub(r'"tk03_\1"', ...)` trên chuỗi đã chứa `t3_` sẽ ra `tk03_t3_x`; và thay thế trong `NEN_SRC` phải giữ **một** cặp dấu nháy. Đã sửa lại và kiểm bằng `.work/_tk_audit_nensrc.py` (28/28 đúng, 0 lỗi `tk03_t3_`).

---

## 6. Việc còn lại (người dùng / lần sau)

1. **Nâng 16 nền dự phòng thành AI thật** khi bật credit auto-consumption (xem B1). Ưu tiên theo mức độ "cắt mất chủ thể": `two_agents` → `interview_room` → `mother_shadow` (đã crop lại nhưng vẫn là bản cắt) → `gift_drowned` → `life_sentence`.
2. **Dựng 5 clip 9:16** — bước 4 của `KE_HOACH_CLIP_TAP03.md` (cần 51 file WAV theo `SPEC_AUDIO_CLIP_TAP03.json`).
3. **Điền link YouTube Tập 03** vào 5 file caption (đang placeholder) + profile.
4. **Không commit media** (L10): 28 ảnh `assets/bg/tk03_*.png` bị `.gitignore` loại — chỉ commit tài liệu + script.

---

## 7. Script đã tạo (`.work/`)

`_tk_scan_t03.py` · `_tk_src_t03.py` (PAIRS + PROMPT) · `_tk_src_montage_t03.py` · `_tk_gen_bg_t03.py` · `_tk_gen_bg_extra_t03.py` · `_tk_download_imgs_t03.py` · `_tk_postprocess_t03.py` · `_tk_fallback_crop_t03.py` · `_tk_recrop_t03.py` · `_tk_fix_dark_t03.py` · `_tk_measure_bg_t03.py` · `_tk_zoom_t03.py` · `_tk_zoom_people_t03.py` · `_tk_qc_coverage_t03.py`
