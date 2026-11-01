# Báo cáo đo giọng mẫu JA/KO theo seed bộ VN (ja2, ko2) — 01/11/2026

Nguồn: `assets/voice_ref_voxcpm2_ja2/`, `_ko2/` (26 take mỗi bộ; Mac commit `a1e6736`, `2f965c6`; log `.work/voxcpm_ja2_run.log`, `_ko2_run.log`: 26 dòng, 0 lỗi).
Đo trên Windows: `voxcpm_do_mau.measure(final=True)` (V2, V5, V6) và YIN (`voxcpm_yin_f0.py`). Dải F0 lấy từ manifest, sai số ±6%. **Chưa đo CER**: chưa có ASR/chuẩn hoá cho tiếng Nhật/Hàn.
Script đo: scratchpad `do_jk.py`; số đầy đủ: `do_jk.json` (không lưu vào repo).

Dải mục tiêu: H 100–118 · D 78–88 · C 200–218 · N2 (W5) 258–292 · N1 (W6) 148–182 Hz.

## Kết quả theo vai

| Vai | JA (ja2) | KO (ko2) |
|---|---|---|
| H | ✅ `H_vnctrl_ja_t02` AC 106,7 / YIN 103,7 · `H_jactrl_t02` 117,6 / 113,9 (`H_vnctrl_ja_t01` 102 Hz nhưng sàn ồn −36 dB → loại) | ✅ `H_koctrl_t01` 121,2 / 124,5 (sát mép trên) |
| D | ❌ không take nào < 98 Hz. Thấp nhất `D_vnctrl_ja_t01` 101,9 Hz, trùng H (≈0 nc). 2 take ~99 Hz có sàn ồn −47 dB | ❌ thấp nhất `D_vnctrl_ko_t01` 114/117 Hz, cách H ≈ 1 nc |
| C | ⚠ chỉ `C_jactrl_t01` 207,8 / 213,6 nhưng **dài 29,2 s > 28 s**. 3 take còn lại 258–272 Hz, sát N2 (< 1 nc) | ❌ 242–275 Hz, không take nào trong dải |
| N2 | ✅ cả 4 take. Tốt nhất `W5_HIGH_vnctrl_ja_t02` 280,7 / 287,6 (25,2 s) | ✅ `W5_HIGH_vnctrl_ko_t02` 275,9 / 287,5 · `W5_HIGH_koctrl_t02` 266,7 / 272,3 |
| N1 | ❌ 213–269 Hz, không take nào trong dải | ⚠ `W6_LOW_vnctrl_ko_t01` 195,1 / 197,0 (vượt mép trên +6%); cách C ~4 nc |

Chuẩn file: hầu hết đạt −18 ± 1 LUFS, đỉnh ≤ −2 dBFS. Lỗi chuẩn: JA `C_vnctrl_ja_t01` −19,2 LUFS, `D_*_t02` sàn ồn −46/−48 dB, `H_vnctrl_ja_t01` sàn ồn −36 dB; KO `C_vnctrl_ko_t01` −19,5 LUFS. Sàn ồn −180 dB = số 0 tuyệt đối giữa câu, không phải lỗi.

## Kết luận
- **Cả hai bộ chưa dùng được.** Đạt: H và N2 (cả JA và KO). Trượt: **D, C, N1** ở cả hai ngôn ngữ.
- Cùng seed + câu mô tả, VoxCPM2 đọc tiếng Nhật/Hàn **cao hơn** bản Việt: nữ +4…+7 nc (C, N1), nam D không xuống dưới 98 Hz. Giống en2: seed không giữ danh tính.
- Cặp H~D là điểm nghẽn: D chưa có take nào cách H ≥ 4 nc theo hướng trầm hơn.
- Bước tiếp: vòng riêng cho D, C, N1 mỗi ngôn ngữ (như dc3: 4 câu mô tả mạnh hơn × 4 seed), lời đọc C tiếng Nhật rút ngắn để < 28 s. Chưa chạy Higgs trước khi có đủ 5 vai.
