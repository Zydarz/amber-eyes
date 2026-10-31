# Báo cáo đo giọng mẫu EN theo seed bộ VN (en2) — 31/10/2026

Nguồn: `assets/voice_ref_voxcpm2_en2/` (22 take, Mac commit `63a3658`, log `.work/voxcpm_en2_run.log`). Manifest `.work/voxcpm_refs_manifest_en2.json`.
Đo trên Windows: AC + chuẩn file (`voxcpm_do_mau.measure`, V2–V6) và YIN (`voxcpm_yin_f0.py`). **Chưa đo CER**: `vi_cer`/ASR chỉ có cho tiếng Việt.
Bước 1 của brief (seed thật từ `takes.json`) **không có trong log** — seed H 42, W5 2024, W6 (2.5, 999) vẫn là suy ra.

| Vai | F0 giọng VN đã chốt | Take EN | Seed | AC | YIN | Chuẩn file | Đánh giá |
|---|---:|---|---:|---:|---:|---|---|
| H | 107 | `H_vnctrl_t01` | 42 | 116,8 | 119,1 | OK | ứng viên |
| H | | `H_enctrl_t01` | 42 | 117,6 | 119,5 | OK | ứng viên |
| H | | `H_vnctrl_t02` | 101 | 103,9 | 105,4 | OK | ứng viên (gần VN nhất) |
| D | 88 | `D_vnctrl_t01` | 7 | **145,5** | **85,0** | OK | **2 thuật toán lệch** (YIN chỉ 155 khung có thanh) → phải nghe |
| D | | `D_vnctrl_t02` | 42 | 127,0 | 149,3 | OK | trượt |
| D | | `D_enctrl_t01` | 7 | 105,3 | 97,7 | OK | trượt (Higgs dồn 105–130 Hz về ~125 = trùng Host) |
| D | | `D_enctrl_t02` | 42 | 111,1 | 101,8 | OK | trượt |
| C | 208 | `C_enctrl_t01` | 77 | 197,5 | 200,5 | OK | ứng viên |
| C | | `C_enctrl_t02` | 42 | 200,0 | 211,7 | OK | ứng viên |
| C | | `C_vnctrl_t02` | 42 | 202,5 | 225,5 | OK | dự phòng |
| N2 (W5) | 289 | `W5_HIGH_enctrl_t01` | 2024 | 262,3 | 266,7 | OK (16,3 s) | ứng viên |
| N1 (W6) | 179 | `W6_LOW_vnctrl_t01` | 999 | 183,9 | 186,6 | OK | ứng viên (gần VN nhất) |
| N1 (W6) | | `W6_LOW_enctrl_t01` | 999 | 190,5 | 192,4 | sàn ồn −50,6 dB | dự phòng |

Các take còn lại trượt F0 hoặc thời lượng (xem log). Mọi take có cảnh báo V5 (F0 dao động 3–10 nc) — cần nghe độ trung tính.

## Kết luận
- **Cùng seed + cùng câu mô tả, khác lời đọc ⇒ KHÔNG ra cùng giọng.** D seed 7: VN 88 Hz → EN 85/145 Hz (vnctrl), 105/98 Hz (enctrl). Seed chỉ là điểm xuất phát, không giữ danh tính. Danh tính VN↔EN phải do **tai người dùng** xác nhận.
- H, C, N1, N2: có ứng viên trong dải. **D chưa có**: cần nghe `D_vnctrl_t01`; nếu không đạt → vòng D riêng (nhiều seed, như dc3: 4 câu mô tả × 4 seed).
- Sau khi chọn: chạy thử Higgs đọc tiếng Anh (R3) — đo F0/G9 trên bản đọc, vì Higgs kéo giọng nam 105–130 Hz.
