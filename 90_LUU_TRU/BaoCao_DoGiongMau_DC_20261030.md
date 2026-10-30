# Đo 18 giọng mẫu ứng viên D_NEW + C_NEW (VoxCPM2) — 30/10/2026

Nguồn: `assets/voice_ref_voxcpm2_dc/` (commit 4428cb5). Đo: `.work/voxcpm_do_dc.py` (dùng `measure()` của
`voxcpm_do_mau.py`, cổng V2–V6) + `.work/voxcpm_yin_f0.py` (F0 thuật toán 2, YIN). ASR: listen_audio 2 lượt (Q6).
Số thô: `.work/voxcpm_do/do_dc_18take.json`, `.work/voxcpm_do/do_dc_6take_asr.json`.

## Kết quả
- **D_NEW: 2/9 take qua F0** (mục tiêu clip 82–95 Hz, ±6%). Seed quyết định cao độ mạnh hơn câu mô tả:
  cùng một câu mô tả ra 90–195 Hz.
- **C_NEW: 4/9 take qua F0** (200–218 Hz). Take nói nhanh (4,2–4,6 âm/s) đều bị đẩy cao (235–254 Hz).
  Chỉ 1 take vừa đúng cao độ vừa nhanh (`bright-auth_t03`), nhưng sàn ồn −53,6 dB (cần ≤ −55).

| Take | F0 AC / YIN (Hz) | Tiếng (s) | Âm/s | CER (2 lượt) | Thanh điệu sai | Ghi chú |
|---|---|---:|---:|---:|---:|---|
| D_NEW_vlow-gravel_t01 | 97,6 / 90,0 | 25,7 | 3,31 | 0,0% | 0 | F0 dao động 6,3 nc |
| D_NEW_deep-smoker_t01 | 96,4 / 98,7 | 25,8 | 3,30 | 0,0% | 0 | khoảng lặng 1,48 s (sát ngưỡng 1,5) |
| C_NEW_crisp_t02 | 200,0 / 206,5 | 26,1 | 3,52 | 0,0% | 0 | |
| C_NEW_bright-auth_t02 | 200,0 / 202,7 | 24,7 | 3,73 | 0,0% | 0 | |
| C_NEW_lecture_t02 | 207,8 / 214,0 | 24,3 | 3,78 | 0,0% | 0 | |
| C_NEW_bright-auth_t03 | 210,5 / 215,9 | 21,9 | 4,21 | 0,0% | 0 | ❌ V2 sàn ồn −53,6 dB |

Định dạng (V6): cả 18 take đạt PCM 16-bit 24 kHz mono, −17,1…−18,8 LUFS, đỉnh ≤ −1,8 dBFS, `.txt` khớp.

## Chưa kiểm được
- **Độ khàn / chất giọng**: không có số đo, cần người nghe.
- **F0 sau khi Higgs clone**: đây mới là cổng quyết định (H.wav 108 → 130 Hz). Phải chạy thử trên Kaggle.
- Tốc độ chưa đạt thiết kế: D 3,3 âm/s (thiết kế 2,9–3,2), C 3,5–3,8 (thiết kế 3,9–4,3).
