# BÁO CÁO SINH ẢNH NỀN TẬP 31 + TẬP 32 (Cloudflare FLUX) — 27/11/2026

## 1. Phạm vi

| Mục | Tập 31 | Tập 32 | Tổng |
|---|---:|---:|---:|
| Shot (theo bảng mapping) | 165 | 143 | 308 |
| Ảnh nền sinh được (có file) | **159** | **0** | **159** |
| Còn thiếu | 6 | 143 | **149** |

Nguồn prompt: `.work/bg_jobs_tap31.json` (165 job) · `.work/bg_jobs_tap32.json` (143 job).
Công cụ: Cloudflare Workers AI `@cf/black-forest-labs/flux-1-schnell`, steps=4, out 2112×1188 PNG,
hậu kỳ Deep Noir H21/H25/H26 (crop 16:9 + Lanczos, bão hoà ×0,65, tương phản ×1,15, vignette 4 góc, hạt phim 35 mm).

## 2. Việc đã làm trước khi sinh

### 2.1 Rà rủi ro chữ (bài học T37–39, 26/11/2026)

Với FLUX.1-schnell, thêm câu "no text" **không** có tác dụng — còn kích hoạt chữ. Phải **bỏ hẳn cơ hội vẽ chữ**.
Script rà: `.work/_audit_prompts_t31_32.py` (bỏ negation trước, rồi chấm theo vật mang chữ).

Kết quả rà ban đầu (trước khi viết lại): **T31 44/165** và **T32 51/143** prompt có rủi ro.

### 2.2 Viết lại 99 prompt

Script: `.work/_rewrite_prompts_t31_32.py` → ghi **44** prompt t31 + **55** prompt t32.
Bản gốc lưu ở `.work/_cu/bg_jobs_tap31_20261127_1525_before_rewrite.json` và bản t32 tương ứng (L5).

4 bước áp dụng cho mỗi prompt:
1. Gỡ mọi từ kích hoạt chữ (sign, shop, notice, map, calendar, ledger, screen, plate, neon, roulette…).
2. Thay bằng vật thể cụ thể + bề mặt trơn: *blank / unmarked / plain / bare / featureless*.
3. Đưa vật mang chữ ra khỏi khung: *tight framing*, *crop*, *so the facade stays out of picture*.
4. Bỏ negation trong core prompt (giữ nguyên hằng số `STYLE_SUFFIX` của `flux_client.py` — đã được kiểm chứng ở T39 135/135).

Ví dụ: `t32_a1_05_herbal_tea_shop_yau_ma_tei` (biển cửa hàng + chữ Hán) → quay vào trong, `tight framing on the shelves so the street front stays out of picture`.

## 3. Kết quả chạy sinh ảnh

Lệnh: `py -3 .work/gen_images_cf_tap3739.py 31 32` (nền) — 13,9 phút, 0 lỗi kỹ thuật.

T31 sinh được 159/165 (ảnh ~4,1–5,0 MB, 2,1–23 s/ảnh). **Dừng tại ảnh 160/165** (`t31_a5_17_night_city_skyline_connections`) vì pool Cloudflare cạn quota:

```
HTTP 429 · code 4006
"AiError: you have used up your daily free allocation of 10,000 neurons,
 please upgrade to Cloudflare's Workers Paid plan if you would like to continue usage."
```

Đã probe trực tiếp cả 7 account trong `.work/.cloudflare_accounts` → **cả 7 đều trả 429 code 4006** ⇒ hết quota ngày thật,
không phải rate-limit tạm thời. Quota reset 00:00 UTC = **07:00 VN 28/11/2026**.

T32 chưa kịp sinh ảnh nào (script dừng ngay khi pool cạn).

**Không tự chuyển sang Kaggle** (user đã chốt 25/11/2026: chỉ dùng Cloudflare).

## 4. Ảnh còn thiếu

- Tập 31 (6, đều thuộc hồi 5): `t31_a5_17_night_city_skyline_connections`, `t31_a5_18_fallen_mask_sunrise_floor`,
  `t31_a5_18b_empty_chair_sunrise_window`, `t31_a5_19_calm_path_amber_light`, `t31_a5_20_amber_eyes_study_closing`,
  `t31_a5_21_end_card_amber_horizon` (thẻ kết).
- Tập 32: toàn bộ 143.

## 5. Lịch chạy lại

Đã tạo lịch 1 lần: **07:05 VN 28/11/2026** (cron `a20684fe-c1f5-4202-8d3d-2100b0822640`, gắn vào chính cuộc trò chuyện này).
Lịch sẽ chạy `gen_images_cf_tap3739.py 31 32` (tự bỏ qua 159 ảnh đã có), gộp `provenance.json`,
cập nhật `Bang_Shot_Anh_TapXX.md`, rồi chạy cổng `map_shot_anh.py --check 31 32`.

## 6. Hồ sơ & bảng mapping

- `provenance.json`: **+159 dòng** (tổng 7252 dòng), ghi đủ công cụ / prompt / ngày / điều khoản / đã kiểm thương mại (L7).
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap31/Bang_Shot_Anh_Tap31.md`: cột "Có file" → **159/165**.
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap32/Bang_Shot_Anh_Tap32.md`: **0/143**.
- Lỗi mapping: **0** (T31) và **0** (T32) — không lặp ảnh, không ảnh nào không shot nào dùng.

## 7. Việc còn lại của người dùng

1. **QC hình ảnh** (AI đã được yêu cầu bỏ QC đúng/sai): soi 159 ảnh Tập 31 trong `assets/bg/t31_*.png`,
   đánh dấu ảnh có chữ lạ / lệch nghĩa. Danh sách 99 prompt đã viết lại nằm trong `.work/bg_jobs_tap3{1,2}.json`
   — nếu ảnh nào vẫn ra chữ, sửa prompt theo vòng 3 (bỏ cơ hội vẽ chữ) rồi sinh lại.
2. Sau khi lịch 07:05 VN 28/11 chạy xong: kiểm tra T32, QC ảnh T32.
3. Chưa commit gì (media bị `.gitignore` loại — L10).
