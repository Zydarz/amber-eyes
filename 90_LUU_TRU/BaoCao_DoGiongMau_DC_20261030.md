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

---

# Vòng 2 — 32 take (`assets/voice_ref_voxcpm2_dc2/`, commit e24c8fc), seed 7,13,77,123,256,512,1234,4321

Số thô: `.work/voxcpm_do/do_dc2_32take.json`, `.work/voxcpm_do/do_dc2_8take_asr.json`.

- **D: 2/16 qua F0**, vẫn thấp: 89,4 và 97,0 Hz. 14 take còn lại 108–138 Hz (vùng Higgs kéo về Host).
- **C: 9/16 qua F0**, và lần này **nhanh** (3,9–4,4 âm/s): câu mô tả "alto" đã ghim được cao độ khi nói nhanh.
- 8 take qua F0 chạy ASR 2 lượt: **CER 0,0%, 0 lỗi thanh điệu, 0 lỗi khác** (đã đọc bản chép, đủ chữ, không bị chặn).

| Take | F0 AC / YIN | Âm/s | CER | Ghi chú |
|---|---|---:|---:|---|
| D_NEW_vlow-gravel_t01 (dc2) | 89,4 / 90,6 | 3,62 | 0% | **thấp nhất, giữa dải** |
| D_NEW_deep-smoker_t01 (dc2) | 97,0 / 98,7 | 3,39 | 0% | mép trên |
| C_NEW_alto-brisk_t05 | 200,0 / 198,6 | 4,14 | 0% | **duy nhất không cảnh báo nào** (F0 dao động 3,0 nc) |
| C_NEW_lecture_t03 | 216,2 / 215,0 | 4,40 | 0% | nhanh nhất |
| C_NEW_alto-brisk_t03 | 207,8 / 209,6 | 4,15 | 0% | |
| C_NEW_lecture_t02 | 213,3 / 213,2 | 4,01 | 0% | |
| C_NEW_alto-brisk_t08 | 202,5 / 204,6 | 3,94 | 0% | |
| C_NEW_lecture_t08 | 202,5 / 202,1 | 3,97 | 0% | |

## Phát hiện: seed quyết định cao độ, không phải câu mô tả
Cùng một seed cho cao độ gần nhau dù câu mô tả khác: seed 7 → D 89/97 Hz; seed 256 → C 200/193; seed 123 → C 262/281.
Mọi take D đạt ở cả 2 vòng đều là seed **42** hoặc **7**. Seed ngẫu nhiên chỉ ~13% ra D < 100 Hz.
⇒ Muốn thêm ứng viên D thì giữ seed 42/7 và đổi câu mô tả, không tăng số seed.

## Chưa đạt thiết kế
- D nói 3,4–3,6 âm/s, **không chậm hơn Host** (3,4) như thiết kế 2,9–3,2.
- Độ khàn: chưa có số đo, cần người nghe.
- F0 sau Higgs clone: chưa đo (cổng quyết định).

---

# Pilot v9 trên Kaggle — bản Higgs clone (30/10/2026)

Kernel `chiduong2026/amber-eyes-higgs-v9-voice-dc-kaggle-gpu`: 8 giọng mẫu × 12 câu thật đúng vai × 2 bản = 192 file, 0 lỗi.
Đo: `.work/analyze_pilot_v9.py --cer`, `.work/_v9_padtest.py`, `.work/_v9_final.py`, `.work/_v9_blind.py`.
Số thô: `.work/pilot_v9_result.{txt,json}`, `.work/pilot_v9_final.json`, `.work/pilot_v9_padtest.json`.
Mốc so sánh: Host/N1/N2 lấy từ 416 file sản xuất, đo cùng thuật toán.

| Giọng mẫu | F0 clone neutral (AC/YIN) | CER: câu đạt (bản tốt / 2 bản) | Âm/s | D↔H | D↔C / C↔H | Câu cảm xúc vọt ≥ 4 nc |
|---|---|---:|---:|---:|---:|---:|
| D1_DS (dc deep-smoker seed 42) | 96,0 / 100,8 | **12/12** (tb 0,13%) | 3,56 | 3,88 ❌ | ≥ 11,3 ✅ | **1/8** |
| D1_VG (dc vlow-gravel seed 42) | 99,5 / 94,2 | **12/12** (0,11%) | 3,54 | 3,64 ❌ | ≥ 11,5 ✅ | 2/8 |
| D2_DS (dc2 deep-smoker seed 7) | 97,9 / 99,4 | 11/12 | 3,58 | 3,92 ❌ | ≥ 11,5 ✅ | 3/8 |
| D2_VG (dc2 vlow-gravel seed 7) | 91,1 / 91,3 | ❌ 8/12 | 4,08 | **5,17 ✅** | ≥ 13 ✅ | 3/8 |
| **C2_AB03** (alto-brisk seed 77) | 208,7 / 210,6 | **12/12** (0,12%) | 4,07 | — | C↔H 8,87 ✅ | 0/6 |
| C2_AB05 (alto-brisk seed 256) | 193,5 / 193,4 | 12/12 (0,12%) | 4,00 | — | 7,39 ✅ | 0/6 |
| C2_LE02 | 207,4 / 205,6 | 12/12 | 3,96 | — | 8,45 ✅ | 0/6 |
| C2_LE03 | 211,9 / 209,3 | 11/12 | 4,32 | — | 8,76 ✅ | 0/6 |
| *Host sản xuất (H.wav)* | 122,8 / 126,2 | — | 3,55 | | | **6/15** |

- So với bản sản xuất: **D↔C từ 1,03 nc lên ≥ 11 nc** — lỗi "D nghe như C" đã hết.
- **D↔H còn 3,6–3,9 nc** với các giọng D đọc đúng chữ (ngưỡng G9 = 4). Riêng D2_VG đạt 5,17 nc nhưng trượt CER 4/12 câu.
- C↔N1 1,4–2,8 nc (trượt) — giống `C.wav` cũ (2,58); N1 chỉ ở cảnh 1.07 và 4.06, không liền kề C.
- CER: 46 file trượt ở lượt đầu, phần lớn do ASR bỏ chữ đầu câu; chèn 0,5 s lặng cứu 14/46; ASR dao động mạnh (1 câu 2,3% → 266,7%) ⇒ tiêu chí cuối: mỗi câu có ≥ 1 trong 2 bản đạt ≤ 2%.
- Nghe mù (`listen_audio`, H/D/C xen kẽ 9 đoạn): lượt 1 D1_DS và D1_VG đúng 3 người, 9/9 đoạn; lượt 2 sai và mâu thuẫn ⇒ theo Q4 **không dùng làm bằng chứng**.
- **Phát hiện phụ (ảnh hưởng bản sản xuất hiện tại):** thẻ `<|emotion:sadness|>` làm Host ra 203–228 Hz ở 5/8 câu buồn → nghe như giọng nữ. Ghi A11 #53.

---

# Vòng 3 (Mac) + Pilot v10 trên Kaggle — 30/10/2026

**Mac vòng 3** (`assets/voice_ref_voxcpm2_dc3/`, commit 1d100fa): 16 take D, 4 câu mô tả × seed 42/7/2718/9001.
Không take nào < 88 Hz (mục tiêu 78–88). Seed 7 ra 88–90 Hz ở cả 4 câu mô tả ⇒ đây là sàn của VoxCPM2.
3 take thấp nhất (seed 7) + `smoker-bass_t01` (seed 42, 95 Hz): ASR 2 lượt CER 0,0%, 0 lỗi thanh điệu.
Số thô: `.work/voxcpm_do/do_dc3_16take.json`, `.work/voxcpm_do/do_dc3_3take_asr.json`.

**Pilot v10** (`chiduong2026/amber-eyes-higgs-v10-voice-d3-kaggle-gpu`): D3_SH / D3_BG / D3_LG + C2_AB03 × 12 câu × 2 bản = 96 file, 0 lỗi.
Đo: `.work/analyze_pilot_v9.py --tag v10 --cer`, `TAG=v10 .work/_v9_padtest.py`, `TAG=v10 .work/_v9_final.py`.

| Giọng | F0 clone neutral (AC/YIN) | D↔H | D↔C | CER câu đạt | Âm/s | Câu cảm xúc vọt ≥ 4 nc |
|---|---|---:|---:|---:|---:|---:|
| **D3_SH** (subbass-husky seed 7) | 87,6 / 85,9 | **5,85 ✅** | 15,1 ✅ | 11/12 | 4,04 | 3/8 |
| D3_BG (bass-gravel seed 7) | 88,9 / 89,0 | 5,59 ✅ | 14,9 ✅ | 11/12 | 4,02 | 5/8 |
| D3_LG (low-growl seed 7) | 91,4 / 91,8 | 5,10 ✅ | 14,4 ✅ | 11/12 | 3,99 | 3/8 |
| C2_AB03 (đối chứng) | 209,6 / 211,6 | — | — | 11/12 | 4,03 | 0/6 |

- **Lần đầu D đạt G9 với Host** (5,1–5,9 nc, cả 2 thuật toán) **và** giữ CER.
- Câu trượt CER của **cả 3 giọng D là cùng một câu**, chỉ mất chữ đầu "Thứ" ("Thứ dẫn cảnh sát tới gần hắn…", 14 từ → 1 lỗi = 6,5%); pilot v9 cũng trượt câu này ⇒ lỗi theo câu, không theo giọng. C2_AB03: "Bởi vậy" → "với vậy".
- D3 nói **4,0 âm/s, nhanh hơn Host (3,55)** — ngược thiết kế "chậm, cụt".
- Câu `sad`/`surprised` vẫn vọt (D3_SH surprised 172 Hz) — cùng lỗi thẻ cảm xúc của Host (A11 #53).
- Nghe: `02_SAN_XUAT/Tap02/thu_giong_v10/`.
