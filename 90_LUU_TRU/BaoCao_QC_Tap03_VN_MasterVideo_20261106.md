# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG (QC) — TẬP 03 (TIẾNG VIỆT) · DỰNG VIDEO MASTER

**Ngày kiểm định:** 06/11/2026 · **Nguồn sự thật:** `02_SAN_XUAT/Tap03/xuat_ban/Tap03_master.mp3`
**Thành phẩm:** `02_SAN_XUAT/Tap03/xuat_ban/Tap03_master.mp4`

---

## 0. LỖI GỐC ĐÃ PHÁT HIỆN VÀ XỬ LÝ (ĐỌC TRƯỚC KHI ĐỌC PHẦN 1)

Khi mở việc, timeline đang có trong repo **không khớp** file audio master:

| Mục | Giá trị cũ (repo) | Giá trị thật của `Tap03_master.mp3` | Lệch |
|---|---|---|---|
| Tổng thời lượng timeline | 1683,720 s | **1664,960 s** | **−18,760 s** |
| Câu cuối cùng kết thúc | 1674,720 s | 1655,960 s (đo bằng ASR: 1655,82 s) | −18,760 s |

Nếu dùng nguyên timeline cũ để dựng, **toàn bộ ảnh sẽ lệch tiếng tới cuối tập** (mỗi câu trôi dần, tổng cộng ~18,8 s ≈ nửa câu lời).

**Cách xử lý:** dựng lại timeline **từ chính file mp3** (không tin file cũ), rồi **kiểm chứng độc lập bằng ASR**:

- `faster-whisper 1.2.1` · mô hình `Systran/faster-whisper-base` (int8, CPU), chạy theo chunk 180 s có checkpoint để chạy lại được.
- Kết quả: **369 đoạn lời**, phủ 22,63 s → 1655,82 s.
- Đối chiếu **218/218 câu** của kịch bản với audio thật: câu nào nằm đúng mốc thời gian trong timeline.
- **Trượt tích luỹ = +0,025 s/câu** (trung bình −0,130 s, trung vị −0,110 s) ⇒ **không có trượt dần**.

> Bản timeline cũ (`1683,72 s`) là bản **ước lượng theo thời lượng TTS dự kiến** của một bản giọng cũ, không phải số đo của master hiện tại. File `build_audio3.py` trộn âm thanh bằng **đúng** công thức đó (`GAP_SENT 0,35` · `GAP_SPEAKER 0,70` · `GAP_ACT 2,0` · `MAX_PAUSE 2,5` · `FIRST_VOICE 23,0` · outro +9,0 s), nên timeline mới (`1664,96 s`) khớp **tuyệt đối** với master.

**Bản sao lưu trước khi ghi đè:** `.work/_cu/t03_20261106_shots_t03.json.bak` · `t03_20261106_timeline_s_t03.json.bak` · `t03_20261106_KeHoach_Video_Tap03.md.bak`

---

## 1. TỔNG QUAN KẾT QUẢ SẢN XUẤT

| Hạng mục | Kết quả | Trạng thái |
|---|---|---|
| Audio nguồn | `Tap03_master.mp3` · 39.960.620 B · 1664,960 s · 48 kHz stereo · 192 kbps | Giữ nguyên, không sửa |
| Timeline | `.work/timeline_s_t03.json` · 1664,960 s · **218 câu** · 5 hồi · 15 mốc (4 ACT + 11 NGHI) | Dựng lại + kiểm chứng ASR |
| Bảng shot | `.work/shots_t03.json` · **110 shot** · ID duy nhất 110/110 | Sinh lại từ timeline mới |
| Stem giọng | `.work/stems_t03/{H,D,C,N1,N2}.wav` (16 kHz) | Dựng lại (đã bị dọn đĩa) |
| Audio cho mux | `.work/audio_master_t03.wav` · 1664,960 s · 48 kHz stereo | Giải mã lại từ mp3 |
| Ảnh tĩnh | `.work/video3_t03/stills/` · **110 PNG** 1920×1080 | Render lại toàn bộ |
| Phụ đề | `02_SAN_XUAT/Tap03/xuat_ban/Tap03.srt` · **428 cue** | Sinh lại |
| Video master | `02_SAN_XUAT/Tap03/xuat_ban/Tap03_master.mp4` | Ghép hình + tiếng |

**Các file cấu hình dùng chung KHÔNG bị sửa** — `edition.py` chỉ bị session song song (đang làm Tập 06) chạm vào khối Tập 05/06; khối `"03"` (dòng 226–323) **nguyên vẹn** (đã đối chiếu bằng `git diff`, mọi hunk đều ≥ dòng 528).

---

## 2. BẢNG THÔNG SỐ ĐO THẬT & ĐỐI CHIẾU TIÊU CHUẨN

### 2.1. Audio → timeline → hình (khớp lời thoại)

| Kiểm | Cách đo | Kết quả | Chuẩn |
|---|---|---|---|
| Câu trong timeline có đúng lời đọc tại đúng mốc | Whisper base, cửa sổ quanh mốc câu | **211/218** khớp trực tiếp; 7 câu còn lại đo lại bằng cách cắt riêng đoạn audio → **7/7 khớp** | 100% |
| **Tổng cộng** | | **218/218 câu** | 100% |
| Trượt thời gian tích luỹ | so mốc ASR với mốc timeline | **+0,025 s/câu** (25% đầu −0,146 s → 25% cuối −0,182 s) | ≈ 0 |
| Khoảng trống giữa các mốc hồi | 15 mốc (4 ACT + 11 NGHI) | mọi mốc **khít** câu kế tiếp (gap = 0,000 s) | không rời |
| Ảnh hiện đúng lúc câu của nó được đọc | giữa shot ↔ câu đang đọc | **110/110 shot** | 100% |

### 2.2. Bảng shot — cổng dùng chung của dự án (`.work/_qc_tap02_shots.py`, AE_EP=03)

| Cổng | Kết quả |
|---|---|
| 218 câu phủ đúng, không câu nào nằm ở 2 shot | ✔ |
| Thứ tự shot khớp thứ tự kịch bản | ✔ |
| Cột vai khớp vai đang đọc | ✔ |
| Nền có file trong `assets/bg/` | ✔ 110/110 |
| **V3** trích dẫn nguyên văn | 0 lỗi |
| **A9.2** mọi số trên hình truy được về câu | 0 lỗi |
| Từ cấm | 0 lỗi |
| Shot dài có beat / neo V2 | ✔ |
| Shot liền nhau không hở / không chồng | ✔ |

Phân bố template: T1 ×59 · T4 ×13 · T9 ×12 · T2 ×7 · T8 ×6 · T10 ×6 · T5 ×4 · T3 ×3.
Phân bố vai: H ×103 · D ×56 · C ×41 · N1 ×9 · N2 ×9.

### 2.3. Ảnh tĩnh — 7 cổng riêng (`.work/_qc_t03_stills_vn.py`)

| Cổng | Tiêu chí | Kết quả |
|---|---|---|
| G1 | đúng 1 ảnh mỗi shot, không thiếu/thừa, ID không trùng | ✔ 110/110 |
| G2 | PNG mở được, 1920×1080, ≥ 20 KB | 0 lỗi |
| G3 | số trên hình + câu trích phải truy được về **câu của shot** | **0 lỗi / 110** |
| G3b | ảnh hiện đúng lúc câu của shot được đọc | **0 lỗi / 110** |
| G4 | thẻ kết có nhãn + tên kênh + khẩu hiệu | ✔ |
| G5 | nền lặp liền quá 4 shot | 0 chuỗi (tối đa 3) |
| G6 | sóng âm trên badge vai phải thật (không phẳng) | ✔ 5/5 vai |

**Kiểm bằng mắt (3 ảnh đại diện):** `shot_1-02` (bàn trực ban + badge HOST có sóng âm biến động thật) · `shot_2-09` (thẻ "HAI NỮ SINH UCSC / Rosalind Thorpe (23 tuổi) & Alice Liu (21 tuổi)") · `shot_5-21` (thẻ kết "HỒ SƠ TẬP 03 · ĐÃ ĐÓNG / AMBER EYES / Phân tích tâm lý tội phạm… / ĐÓN XEM TẬP TIẾP THEO") — không có mặt người, không chữ AI vẽ nhầm trong nền, không tràn/dính chữ, dấu tiếng Việt đúng.

### 2.4. Phụ đề (`.work/_qc_srt_t03_vn.py`)

| Kiểm | Kết quả |
|---|---|
| Cue truy được về câu gốc (không đổi chữ) | **428/428** |
| Có câu đang đọc tại mốc cue | **428/428** |
| Không lùi / không chồng | ✔ 0 lỗi |
| Cue > 2 dòng | 0 |
| Dòng > 42 ký tự | 7 dòng (khoảng 1,6 %, đều do từ dài không cắt đẹp) |

### 2.5. Mô tả YouTube (kiểm khô — chưa ghi file)

| Kiểm | Kết quả |
|---|---|
| Độ dài mô tả | **4.915 ký tự** ≤ 5.000 ✔ |
| Link nguồn trong mô tả | 25 (bảng nguồn có 51, 19 dòng ✅) |
| Có `[PENDING]` / `[CHUA CO]` | không |
| Mã câu trong `summary_vn` / `need` | 0 / 19 mã — đều tồn tại ✔ |
| Mốc chương | lấy từ `act_start_times(TL)` — không hardcode |

### 2.6. Chuỗi limiter khi đóng gói — **đo thử trước, không sửa cấu hình dùng chung**

| Chuỗi | LUFS sau AAC | True peak sau AAC | Lệch A/V | Kết luận |
|---|---|---|---|---|
| **A — chuỗi VN đang khai cho Tập 03** (`limit=0.7943`, không `latency`) | −16,3 | **−1,6 dBFS** | +16,4 ms | **ĐẠT** (A7: ≤ −1,5 dBFS; lệch ≤ 50 ms) |
| B — chuỗi EN/JA (`limit=0.63` + `latency=1`) | — | — | — | không dùng: file mã hoá bị cắt khi hết giờ thử |

⇒ **Giữ nguyên chuỗi A.** Không sửa `edition.py` ⇒ không ảnh hưởng Tập 01/02/04… (không phát sinh nghĩa vụ kiểm hồi Tập 01 theo L9).

---

## 2.7. ĐẦU RA CUỐI — `Tap03_master.mp4` (đo trên chính file thành phẩm)

| Thuộc tính | Giá trị đo được |
|---|---|
| Container | `mov,mp4,m4a,3gp,3g2,mj2` · 577.9 MB · 1664.933 s |
| Video | h264 1920×1080 @ 30/1 fps |
| Audio | aac 48000 Hz · 2 ch · 195 kbps |
| Loudness | **-16.3 LUFS** (chuẩn −16 ± 1) · LRA 3.2 |
| True peak | **-1.6 dBFS** (trần −1,5 dBFS) |
| Lệch A/V | +0.75 (chuẩn ± 50 ms) |

**Kết luận các cổng QC đầu ra: ĐẠT**

| # | Cổng QC đầu ra | Kết quả | Đo được |
|---|---|---|---|
| 1 | G2 H14 hình = tiếng trong ±0,05 s | ✔ | lệch 0.0 ms (video 1664.933s · audio 1664.933s) |
| 2 | G2 H14 hình = timeline.total trong ±0,05 s | ✔ | lệch 26.7 ms (video 1664.933s · timeline 1664.960s) |
| 3 | G3 A7 loudness -16 ±1 LUFS | ✔ | -16.3 LUFS |
| 4 | G3 A7 true peak <= -1,5 dBFS | ✔ | -1.6 dBFS |
| 5 | G4 V4 không im lặng tuyệt đối > 0,3 s @ -60 dB | ✔ | 0 khoảng > 0,3s |
| 6 | G5 giải mã toàn bộ không lỗi | ✔ | 0 dòng lỗi: [] |
| 7 | G7 phụ đề phủ câu | ✔ | 428 cue cho 218 câu |
| 8 | G7 phụ đề bắt đầu sau intro và kết thúc trước hết tập | ✔ | đầu 23.00s · cuối 1651.53s |
| 9 | G8 chuyen hoi 2 @ 361.0s khớp ảnh render | ✔ | MAE 3.78/255 |
| 10 | G8 chuyen hoi 3 @ 690.5s khớp ảnh render | ✔ | MAE 3.79/255 |
| 11 | G8 chuyen hoi 4 @ 1003.0s khớp ảnh render | ✔ | MAE 3.74/255 |
| 12 | G8 chuyen hoi 5 @ 1325.6s khớp ảnh render | ✔ | MAE 3.77/255 |
| 13 | G8 the ket (cuoi video) @ 1663.0s khớp ảnh render | ✔ | MAE 0.14/255 |
| 14 | G8 dau video (intro) @ 10.0s khớp ảnh render | ✔ | MAE 1.15/255 |
| 15 | G9 mốc chương khớp câu đầu mỗi hồi | ✔ | 5 mốc (mm:ss khớp câu đầu hồi, dung sai 2 s) |
| 16 | G10 lệch A/V trong ±50 ms | ✔ | +0.75 ms |

---

## 3. MỐC CHƯƠNG (YOUTUBE CHAPTERS)

Lấy từ **câu đầu tiên của mỗi hồi trong timeline** (không hardcode):

| Hồi | Mốc | Nội dung |
|---|---|---|
| Intro | 00:00 | Intro |
| 1 | 00:23 | Cuộc gọi nửa đêm từ bốt điện thoại Colorado |
| 2 | 06:02 | Hiện trường & chuỗi săn mồi — Nấc thang của sự thay thế |
| 3 | 11:32 | Giải phẫu tâm lý — Bên trong bộ não kẻ thái nhân cách tự phản tỉnh |
| 4 | 16:44 | Đối thoại với FBI — Nền tảng của nghệ thuật lập hồ sơ tội phạm |
| 5 | 22:07 | Phán quyết, bài học cảnh báo đỏ & lời kết |

---

## 4. TÀI NGUYÊN THÀNH PHẨM TẠI `02_SAN_XUAT/Tap03/xuat_ban/`

| File | Vai trò |
|---|---|
| `Tap03_master.mp4` | **Video master** (hình + tiếng đã ghép, faststart) |
| `Tap03_master.mp3` | Audio master (nguồn, không sửa) |
| `Tap03.srt` | Phụ đề (428 cue) |
| `mo_ta.txt` | Mô tả YouTube (dùng để upload) |
| `nguon_tham_khao.md` | Bảng nguồn |
| `thumbnail.png` | Ảnh đại diện |

**Chưa dọn đĩa** (đúng quy tắc §11: chỉ dọn tập đã upload YouTube; Tập 03 VN chưa upload).
