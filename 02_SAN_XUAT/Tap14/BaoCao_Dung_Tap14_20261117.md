# BÁO CÁO DỰNG TẬP 14 (VI / EN / JA) — 17/11/2026 — DỪNG Ở MỐC SAU BƯỚC 8 (ảnh tĩnh)

## Đã làm và số đo
- Audio: master VI 2206,66 s · EN 1916,54 s · JA 2208,29 s; cả 3 đều −16,2 LUFS; đỉnh −2,2 / −2,6 / −1,6 dBFS; khoảng câm > 0,3 s: 0 / 0 / 1 (JA).
- **Lỗi T20 đã sửa**: `timeline_s_t14.json` (VI) lệch master 7,85 s và `timeline_s_JA_t14.json` lệch 3,76 s (bản ước lượng). Dựng lại từ SRT (SRT khớp ASR tại 3 mốc VI). EN vốn khớp. Sau sửa: total 2206,62 / 1916,52 / 2208,26 so với mp3 ≤ 0,04 s. Bản gốc lưu ở `.work/_cu/t14_pre_build_20261117/`.
- Bảng shot: 215 shot × 3 ngôn ngữ (`.work/_generate_shots_t14.py`, ghi mục 6 của `KeHoach_Video_Tap14.md`). Gán 147 nền ↔ 210 câu bằng tay theo nghĩa (file `_map_t14_a1..a5.txt`). `qc_bg_usage.py` ĐẠT cả 3 ngôn ngữ (147/147 nền dùng, ≤ 3 shot và ≤ 30 s); `qc_bg_shared.py` ĐẠT.
- `bg_jobs_tap14.json` gộp thành 147 job (1 job/1 nền).
- Stems: **xấp xỉ** (cắt từ master, như Tập 13). `qc_wave_gate.py` ĐẠT 5 vai × 3 ngôn ngữ.
- Ảnh tĩnh 215 × 3 = 645 ảnh, 0 lỗi chữ chìm (`qc_contrast_t14.py`).

## Điểm lệch luật / cần quyết định
1. **H1/V5**: nền `t14_c01_dan_linda_wedding_portrait` vẽ rõ mặt hai nạn nhân; `t14_c05_dan_law_firm_partnership_celebration` mặt người rõ nét. Đang gán ở shot 1-35 và 1-36.
2. **H2**: `b2_solitary_diner_booth_night` có biển neon chữ lạ ("FRACA"); `b2_courthouse_facade…` có chữ trên đầu hồi. Mới soi 70 nền mới bằng montage 512 px; 77 nền cũ chưa soi lại.
3. `b2_wedding_cake_topper_discarded` là búp bê nằm trong hộp giống quan tài, nên cân nhắc.
4. **A14 tầng 2 và `build_audio3.py` không chạy được**: không còn audio từng câu. `package.py --mux` cũng sẽ lỗi như Tập 13.
5. Chưa dùng mẫu T8 cho 4 cảnh báo đỏ (mọi shot Hồi 5 là T1).
6. EN/JA chưa có file `KeHoach_Video_Tap14_EN/JA.md` mục 6 (bảng ở `shots_EN/JA_t14.json`, như Tập 13).
7. Intro: chép `intro_kenh_EN.mov` → `_EN_t14`, `intro_kenh_JA_t13.mov` → `_JA_t14`.

## Chưa làm
Dựng hình (~1 giờ/ngôn ngữ), phụ đề, đóng gói/mux, kiểm mp4 cuối.
