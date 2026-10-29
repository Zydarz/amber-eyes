# Báo cáo đo giọng mẫu VoxCPM2 — 20261029 (file đóng gói)

Chuẩn: `00_TIEU_CHUAN/QUY_TAC_GIONG_MAU_VOXCPM2.md` · văn bản chuẩn: `voxcpm_refs_manifest.json` · ASR: 2 lượt listen_audio, lấy lượt xấu hơn

## 1. Từng bản

| Vai | File | Tiếng s | Lặng max s | Ồn dB | F0 Hz (mục tiêu) | F0 ±nc | âm tiết/s | LUFS | Đỉnh | CER | Sai thanh | Kết quả |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---|
| H | `H.wav` | 22.54 | 0.86 | -77.0 | 107 (100–106) | 4.78 | 3.5 | -17.3 | -2.0 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 4.8 nc — nghe lại độ trung tính |
| D | `D.wav` | 22.26 | 0.68 | -71.1 | 152 (138–148) | 4.34 | 3.82 | -17.6 | -2.2 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 4.3 nc — nghe lại độ trung tính |
| C | `C.wav` | 23.44 | 0.76 | -85.8 | 208 (202–212) | 3.72 | 3.92 | -18.0 | -4.1 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 3.7 nc — nghe lại độ trung tính |
| W1 | `W1.wav` | 23.52 | 0.54 | -65.5 | 250 (228–242) | 3.99 | 3.74 | -17.0 | -2.0 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 4.0 nc — nghe lại độ trung tính |
| W2 | `W2.wav` | 26.64 | 1.1 | -80.8 | 200 (180–192) | 3.39 | 3.42 | -17.6 | -2.8 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 3.4 nc — nghe lại độ trung tính |
| W3 | `W3.wav` | 24.58 | 0.58 | -76.3 | 162 (162–175) | 3.58 | 3.62 | -17.3 | -4.0 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 3.6 nc — nghe lại độ trung tính |
| W4 | `W4.wav` | 26.14 | 0.82 | -180.0 | 137 (120–128) | 4.24 | 3.6 | -17.6 | -2.0 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 4.2 nc — nghe lại độ trung tính |

## 2. Bản thắng mỗi vai

| Vai | Bản | F0 | CER |
|---|---|---:|---:|
| H | `H.wav` | 107 | 0.0% |
| D | `D.wav` | 152 | 0.0% |
| C | `C.wav` | 208 | 0.0% |
| W1 | `W1.wav` | 250 | 0.0% |
| W2 | `W2.wav` | 200 | 0.0% |
| W3 | `W3.wav` | 162 | 0.0% |
| W4 | `W4.wav` | 137 | 0.0% |

## 3. G9 giữa các bản thắng (cùng giới)

| Cặp | Cách (nửa cung) | Kết quả |
|---|---:|---|
| H↔D | 6.06 | ĐẠT |
| H↔W3 | 7.07 | ĐẠT |
| H↔W4 | 4.19 | ĐẠT |
| D↔W3 | 1.01 | TRƯỢT |
| D↔W4 | 1.87 | NGHE MÙ BẮT BUỘC |
| C↔W1 | 3.2 | TRƯỢT |
| C↔W2 | 0.66 | NGHE MÙ BẮT BUỘC |
| W1↔W2 | 3.86 | TRƯỢT |
| W3↔W4 | 2.88 | TRƯỢT |

## 4. Chưa đo được bằng script — người dùng / nghe mù phải điền

| Mục | Vai | Kết quả | Người kiểm · ngày |
|---|---|---|---|
| V5 nghe: trung tính, đúng tuổi/giới, không vọng, không nhạc | mọi vai | | |
| V7 nghe mù xen kẽ H·D·C (Q1) — gán đúng 100% | H D C | | |
| V7 nghe mù H↔W4, D↔W4, W2↔C | | | |
| V8 Higgs clone 20 câu/vai: CER < 2%, G8 1 người | mọi vai | | |
