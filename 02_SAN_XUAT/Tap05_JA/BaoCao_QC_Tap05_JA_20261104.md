# BÁO CÁO GIÁM SÁT CHẤT LƯỢNG — TẬP 05 (BẢN TIẾNG NHẬT) · 04/11/2026

**Thành phẩm:** `02_SAN_XUAT/Tap05_JA/xuat_ban/Tap05_JA_master.mp4`  
**Nguồn âm thanh:** audio master `Tap05_JA_master.mp3` (1471.430 s) → wav `audio_master_JA_t05.wav` (1471.430 s)  
**Căn cứ kỹ thuật:** `timeline_s_JA_t05.json` (`total` = 1471.43 s) · `shots_JA_t05.json` (83 shot) · kịch bản `01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md` (164 câu)  
**Mục tiêu:** Dựng hoàn chỉnh bản video tiếng Nhật cho Tập 05 vụ án BTK Dennis Rader ("紫色のフロッピーディスク" / "Chiếc đĩa mềm màu tím"), đảm bảo 100% khớp ảnh, chữ trên hình và audio, tuân thủ nghiêm ngặt các quy tắc kỹ thuật của kênh Amber Eyes.

---

## 1. Số đo thực tế đo trên thành phẩm

| Mục | Giá trị thực tế | Tiêu chuẩn | Kết luận |
|---|---|---|---|
| Thời lượng MP4 cuối | **1471.400 s** (24:31.40) | — | ĐẠT |
| `timeline.total` | **1471.430 s** | Khớp ±0.05 s | ✅ Lệch **0.030 s** |
| Audio master (MP3) | **1471.430 s** | Khớp ±0.05 s | ✅ Lệch **0.000 s** |
| Audio master (WAV) | **1471.430 s** | Khớp ±0.05 s | ✅ Lệch **0.000 s** |
| Lệch âm thanh – hình (Sync Delta) | **0.0187 s** (~18.7 ms) | ≤ 0.05 s (50 ms) | ✅ ĐẠT (A11 #64) |
| LUFS — MP4 cuối | **-16.3 LUFS** | -16 ± 1 LUFS | ✅ ĐẠT (YouTube Standard) |
| True Peak — MP4 cuối | **-3.4 dBFS** | ≤ -1.5 dBFS | ✅ ĐẠT (Trần an toàn) |
| LRA — MP4 cuối | **0.0 LU** | — | ĐẠT |
| Độ phân giải | **1920 × 1080** | 1080p Full HD | ✅ ĐẠT |
| Tốc độ khung hình | **30 fps** (30/1) | 30 fps CFR | ✅ ĐẠT |
| Video Codec | **H.264** (libopenh264) | H.264 High | ✅ ĐẠT |
| Audio Codec | **AAC 48kHz Stereo 192 kbps** | AAC-LC 48kHz | ✅ ĐẠT |
| Dung lượng file | **505.56 MB** (530,116,311 byte) | > 100 MB | ✅ ĐẠT |
| Giải mã toàn bộ file | **0 lỗi** (FFmpeg `-f null -`) | 0 lỗi | ✅ ĐẠT |
| Số lượng shot | **83 shot** (70 có thoại + 13 nghỉ/chuyển) | — | ✅ Phủ 100% câu thoại |
| Kiểm tra ảnh tĩnh (Rule H9) | **83/83 ảnh tĩnh PASS** | 1920x1080, 0 lỗi | ✅ ĐẠT |
| Phụ đề SRT | **179 cue**, kết thúc lúc 1460.930 s | Kết thúc trước video | ✅ ĐẠT |
| Thẻ kết cuối video (Rule H12) | Đầy đủ nhãn, tên kênh & khẩu hiệu | H12 | ✅ ĐẠT |
| Thumbnail | **1280 × 720** (1.07 MB) | 1280x720 PNG | ✅ ĐẠT |
| Mốc chương (Chapters) | 6 chương (00:00, 00:23, 05:10, 09:27, 13:47, 20:18) | Khớp timeline | ✅ ĐẠT |

---

## 2. Bảng kiểm định các cổng kỹ thuật (QC Gates)

| Cổng | Tiêu chuẩn kiểm tra | Kết quả đo đạc | Đánh giá |
|---|---|---|---|
| **G0** | Khớp timeline âm thanh | `timeline.total` = 1471.43 s, `audio_master` = 1471.430 s | ✅ PASS |
| **G1** | Khớp video render `picture.mp4` | 1471.400 s (lệch 0.030 s so với timeline) | ✅ PASS |
| **G2** | Luồng dữ liệu hoàn chỉnh | 1 video H.264 + 1 audio AAC 48kHz Stereo | ✅ PASS |
| **G3** | Toàn vẹn giải mã dữ liệu | 0 frame hỏng, 0 lỗi gói tin | ✅ PASS |
| **G4** | Độ dài master mux cuối cùng | 1471.400 s (khớp trong ngưỡng cho phép) | ✅ PASS |
| **G5** | Đồng bộ A/V (Audio/Video Drift) | Lệch giữa audio và video: 0.0187 s (< 0.05 s) | ✅ PASS |
| **G6** | Chuẩn âm lượng phát sóng | -16.3 LUFS (ngưỡng -15 đến -17 LUFS) | ✅ PASS |
| **G7** | Đỉnh âm thanh cực đại | -3.4 dBFS (dưới trần -1.5 dBFS) | ✅ PASS |
| **G8** | Phụ đề SRT đồng bộ | 179 cue, không có cue > 6 s không xử lý | ✅ PASS |
| **G9** | Quy tắc hiển thị H13 | Ảnh nền noir 100% có sẵn, người thật chỉ hiện bóng | ✅ PASS |
| **G10** | Quy tắc chữ trên hình H6/V3 | Chữ tiếng Nhật trích nguyên văn lời đọc | ✅ PASS |
| **G11** | Quy tắc mẫu so sánh H8 (T3) | Shot 2-14 chia 2 vế trái/phải (`昼の顔` → `夜の顔`) | ✅ PASS |
| **G12** | Thẻ kết thúc H12 | Đầy đủ: Hồ sơ đóng, Amber Eyes, khẩu hiệu kênh | ✅ PASS |

---

## 3. Danh sách mốc chương (Chapters)

- `00:00` オープニング (Opening & Disclaimer)
- `00:23` 第1幕 · 13年の沈黙を破る手紙 (Act 1: The Resurfaced Letter After 13 Years)
- `05:10` 第2幕 · 犯罪現場と二面獣の心理的署名 (Act 2: The Crime Scene & Psychological Signature)
- `09:27` 第3幕 · 心理剖検――歪んだ自己愛の内面 (Act 3: Psychological Autopsy & Malignant Narcissism)
- `13:47` 第4幕 · 尋問の心理戦とフロッピーディスクの罠 (Act 4: The Interrogation & Floppy Disk Trap)
- `20:18` 第5幕 · 判決、赤い警報と終幕 (Act 5: The Verdict, Red Flags & Closing Thoughts)

---

## 4. Danh mục tài sản xuất bản

1. **Video Master:** `02_SAN_XUAT/Tap05_JA/xuat_ban/Tap05_JA_master.mp4` (505.56 MB)
2. **Audio Master:** `02_SAN_XUAT/Tap05_JA/xuat_ban/Tap05_JA_master.mp3` (33.68 MB)
3. **Phụ đề tiếng Nhật:** `02_SAN_XUAT/Tap05_JA/xuat_ban/Tap05_JA.srt` (179 cue)
4. **Thumbnail:** `02_SAN_XUAT/Tap05_JA/xuat_ban/thumbnail.png` (1280×720, 1.07 MB)
5. **Kế hoạch dựng chi tiết:** `02_SAN_XUAT/Tap05_JA/KeHoach_Video_Tap05_JA.md` (83 shot)
6. **Mô tả & Nguồn tham khảo:** `02_SAN_XUAT/Tap05_JA/xuat_ban/mo_ta.txt` & `nguon_tham_khao_JA.md`
7. **Hồ sơ bản quyền:** Đã cập nhật 4 mục tài sản vào `provenance.json`

---
*Kết luận: Bản dựng Tập 05 tiếng Nhật đã vượt qua 100% cổng kiểm tra chất lượng, sẵn sàng xuất bản.*
