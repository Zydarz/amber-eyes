# Báo cáo đo giọng mẫu VoxCPM2 — 20261029 (file đóng gói)

Chuẩn: `00_TIEU_CHUAN/QUY_TAC_GIONG_MAU_VOXCPM2.md` · văn bản chuẩn: `voxcpm_refs_manifest.json` · ASR: 2 lượt listen_audio, lấy lượt xấu hơn

## 1. Từng bản

| Vai | File | Tiếng s | Lặng max s | Ồn dB | F0 Hz (mục tiêu) | F0 ±nc | âm tiết/s | LUFS | Đỉnh | CER | Sai thanh | Kết quả |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---|
| H | `H.wav` | 10.02 | 0.64 | -74.0 | 105 (100–106) | 3.9 | 3.79 | -17.6 | -2.0 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 3.9 nc — nghe lại độ trung tính |
| D | `D.wav` | 9.64 | 1.4 | -73.0 | 139 (138–148) | 4.99 | 3.42 | -17.7 | -1.9 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 5.0 nc — nghe lại độ trung tính |
| C | `C.wav` | 9.88 | 0.98 | -58.8 | 213 (202–212) | 3.93 | 3.95 | -18.1 | -2.1 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 3.9 nc — nghe lại độ trung tính |
| W1 | `W1.wav` | 14.2 | 1.0 | -74.8 | 229 (228–242) | 3.27 | 2.96 | -17.8 | -2.3 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 3.3 nc — nghe lại độ trung tính |
| W2 | `W2.wav` | 13.32 | 0.64 | -73.3 | 184 (180–192) | 3.39 | 3.38 | -18.5 | -5.3 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 3.4 nc — nghe lại độ trung tính |
| W3 | `W3.wav` | 12.12 | 0.88 | -168.2 | 155 (162–175) | 3.71 | 3.55 | -17.8 | -4.0 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 3.7 nc — nghe lại độ trung tính |
| W4 | `W4.wav` | 14.16 | 0.82 | -74.6 | 116 (120–128) | 6.26 | 2.82 | -17.1 | -3.0 | 0.0% | 0 | ✅ ⚠ V5 F0 dao động 6.3 nc — nghe lại độ trung tính |

## 2. Bản thắng mỗi vai

| Vai | Bản | F0 | CER |
|---|---|---:|---:|
| H | `H.wav` | 105 | 0.0% |
| D | `D.wav` | 139 | 0.0% |
| C | `C.wav` | 213 | 0.0% |
| W1 | `W1.wav` | 229 | 0.0% |
| W2 | `W2.wav` | 184 | 0.0% |
| W3 | `W3.wav` | 155 | 0.0% |
| W4 | `W4.wav` | 116 | 0.0% |

## 3. G9 giữa các bản thắng (cùng giới)

| Cặp | Cách (nửa cung) | Kết quả |
|---|---:|---|
| H↔D | 4.82 | ĐẠT |
| H↔W3 | 6.73 | ĐẠT |
| H↔W4 | 1.66 | NGHE MÙ BẮT BUỘC |
| D↔W3 | 1.91 | TRƯỢT |
| D↔W4 | 3.16 | NGHE MÙ BẮT BUỘC |
| C↔W1 | 1.2 | TRƯỢT |
| C↔W2 | 2.57 | NGHE MÙ BẮT BUỘC |
| W1↔W2 | 3.77 | TRƯỢT |
| W3↔W4 | 5.07 | ĐẠT |

## 4. Chưa đo được bằng script — người dùng / nghe mù phải điền

| Mục | Vai | Kết quả | Người kiểm · ngày |
|---|---|---|---|
| V5 nghe: trung tính, đúng tuổi/giới, không vọng, không nhạc | mọi vai | | |
| V7 nghe mù xen kẽ H·D·C (Q1) — gán đúng 100% | H D C | | |
| V7 nghe mù H↔W4, D↔W4, W2↔C | | | |
| V8 Higgs clone 20 câu/vai: CER < 2%, G8 1 người | mọi vai | | |
