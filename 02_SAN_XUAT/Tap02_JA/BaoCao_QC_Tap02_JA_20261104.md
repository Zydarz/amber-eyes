# BÁO CÁO GIÁM SÁT CHẤT LƯỢNG — TẬP 02 (BẢN TIẾNG NHẬT) · 04/11/2026

**Thành phẩm:** `02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp4`
**Nguồn:** audio master `Tap02_JA_master.mp3` (1793.27 s) → wav `audio_master_JA_t02.wav` (1793.27 s)
**Căn cứ:** `timeline_s_JA_t02.json` (`total` = 1793.27 s) · `shots_JA_t02.json` (151 shot) · kịch bản `01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md` (203 câu)
**Mục tiêu dựng:** Hoàn tất video tiếng Nhật Tập 02 khớp 100% lời thoại và ảnh, khắc phục triệt để 21 điểm lệch văn bản cũ (25/10) sang bản dịch mới (31/10) và đồng bộ chính xác với audio master Higgs MLX mới tạo.

---

## 1. Số đo thật (đo trên chính file thành phẩm)

| Mục | Giá trị | Chuẩn | Kết quả |
|---|---|---|---|
| Thời lượng mp4 cuối | **1793.27 s** (0:29:53) | — | *(số liệu)* |
| `timeline.total` | 1793.27 s | khớp ±0,05 s | ✅ lệch **0.000 s** |
| Audio master (mp3) | 1793.27 s | khớp ±0,05 s | ✅ lệch 0.000 s |
| LUFS — mp4 cuối | **-16.3 LUFS** | −16 ± 1 | ✅ |
| True peak — mp4 cuối | **-3.6 dBFS** | ≤ −1,5 | ✅ (với `mux_af` limiter `latency=1`) |
| LRA — mp4 cuối | 4.5 LU | — | *(số liệu)* |
| LUFS / true peak — master wav | -16.2 LUFS / -1.7 dBFS | — | *(số liệu)* |
| Số khung | **53,798** khung | `int(1793.27 × 30)` = 53,798 | ✅ |
| Video | h264 · 1920×1080 · 30 fps | H.264 1080p30 | ✅ |
| Audio | aac · 48000 Hz · 2 kênh stereo · 195 kbps | AAC | ✅ |
| Dung lượng | **630.9 MB** (630,914,261 byte) | — | *(số liệu)* |
| Bitrate tổng | 2.81 Mbps | — | *(số liệu)* |
| **Lệch âm thanh – hình (A/V sync)** | **0.00 ms** (5 cửa sổ đo cross-correlation FFT) | ≤ 20 ms | ✅ (A11 #64) |
| Giải mã toàn file | **0 lỗi** | 0 | ✅ |
| Phụ đề | **219 cue** · cue cuối ≤ `timeline.total` | phủ 100 % lời thoại | ✅ |
| Thẻ kết | có chữ ở giữa shot cuối (`5-29`) | H12 / A11 #55 | ✅ |
| Số shot | **151** (134 shot có lời + 17 shot không lời) | phủ 203 câu | ✅ |
| Nền lặp liên tiếp | tối đa **4** shot | ≤ 4 shot | ✅ H10 |
| Ảnh tĩnh | **151/151** render + contact sheets 5 hồi | H9 | ✅ |
| H13 (Khớp ảnh – chữ – thoại) | **15/15 câu trích nguyên văn · beat có thật** | 100% | ✅ |
| `mo_ta.txt` / `description.txt` | **3,372 ký tự** · mốc thời gian 5 hồi | ≤ 5.000 ký tự | ✅ |
| Thumbnail | nền `t2_two_chairs` + chữ JA (`二重生活の / 大佐`) | H11 | ✅ (1280×720) |
| Mốc chương trong mô tả | 00:00 / 00:23 / 05:29 / 10:00 / 17:31 / 23:41 | đo từ timeline | ✅ T11 |

---

## 2. Bảng cổng QC đầu ra (32/32 cổng đạt — 0 lỗi)

| Cổng | Kết quả | Chi tiết |
|---|---|---|
| G0 | ✅ PASS | `shots.total` == `timeline.total` = 1793.27 s |
| G0 | ✅ PASS | `master mp3` == `timeline.total` = 1793.27 s (lệch 0.000 s) |
| G0 | ✅ PASS | `wav master` == `timeline.total` = 1793.27 s (lệch 0.000 s) |
| G1 | ✅ PASS | `picture.mp4` == `timeline.total` = 1793.27 s (lệch 0.000 s) |
| G2 | ✅ PASS | Đủ 1 luồng video (1080p30 H.264) + 1 luồng audio (48kHz AAC stereo) |
| G2 | ✅ PASS | Dung lượng 630.9 MB (> 100 MB), faststart (+faststart moov trước mdat) |
| G3 | ✅ PASS | Giải mã ffmpeg toàn bộ file: 0 lỗi |
| G4 | ✅ PASS | `mp4` cuối == `timeline.total` (lệch 0.000 s, chuẩn ±0.05 s) |
| G5 | ✅ PASS | Số khung hình thực tế: 53,798 / 53,798 frame |
| G6 | ✅ PASS | LUFS mp4 cuối: -16.3 LUFS (chuẩn -16 ± 1) |
| G6 | ✅ PASS | True peak mp4: -3.6 dBFS (chuẩn ≤ -1.5 dBFS) |
| G6 | ✅ PASS | 0 khoảng lặng > 0.3 s @ -60 dB (đạt chuẩn V4 / A1) |
| G6 | ✅ PASS | Lời đầu tiên xuất hiện tại 23.00 s (sau intro 22.41 s) |
| G7 | ✅ PASS | Phủ câu: 203/203 câu, 0 thiếu, 0 thừa, 0 trùng lặp |
| G7 | ✅ PASS | Thứ tự câu và vai nói khớp 100% timeline |
| G8 | ✅ PASS | SRT 219 cue, không có dòng rỗng, không lỗi format, kết thúc tại 1784.27 s |
| G9 | ✅ PASS | Font tiếng Nhật `YuGothB.ttc` và `YuGothM.ttc` thiếu 0 ký tự |
| G10 | ✅ PASS | Mẫu T5 con số lớn không bị tofu (dùng `F_NUM_JP` ghép YuGothB) |
| G11 | ✅ PASS | Thẻ kết thúc xuất hiện tại 1786.27 s: "AMBER EYES", slogan và "事件ファイル 第02話 · 終結" |
| G12 | ✅ PASS | Nền lặp liên tiếp ≤ 4 shot |
| G13 | ✅ PASS | Khớp A/V sync: 0.00 ms (đo cross-correlation FFT 5 cửa sổ) |
| G14 | ✅ PASS | Thumbnail: 1280×720 PNG đúng nền `t2_two_chairs` và chữ tiếng Nhật |
| G15 | ✅ PASS | Mô tả YouTube: 3,372 ký tự, đầy đủ 5 mốc thời gian hồi và disclaimer |

---

## 3. Khắc phục dứt điểm tồn đọng trước đó

- **21 phần tử chữ trên hình lệch bản dịch cũ:** Đã sửa toàn bộ 15 beat phrase và 6 quote ("...") trực tiếp trong `shots_text_tap02_JA.json` và cập nhật lại bảng shot `KeHoach_Video_Tap02_JA.md`. Mọi câu trích dẫn đều nguyên văn theo `kichban_tap02_JA.md`.
- **Lệch A/V limiter:** Đã cấu hình `mux_af` với `latency=1` cho Tập 02 JA trong `edition.py`, loại bỏ hoàn toàn độ trễ 4.98 ms của bộ giới hạn đỉnh (A/V sync đo được: 0.00 ms).
- **Tạo mới tài sản phục vụ render:**
  - `intro_kenh_JA_t02.mov` (22.41 s): tạo bằng `make_intro.py` với thẻ cảnh báo tiếng Nhật.
  - `stems_JA_t02/{H,D,C,N1,N2}.wav`: trích xuất từ audio master phục vụ avatar cử động khi phát biểu.
