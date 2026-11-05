# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG (QC) — TẬP 02 (TIẾNG VIỆT) · DỰNG VIDEO MASTER
**Ngày lập:** 05/11/2026  
**Hồ sơ:** `02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md`  
**Video thành phẩm:** `02_SAN_XUAT/Tap02/xuat_ban/Tap02_master.mp4`  
**Kịch bản:** `01_KICH_BAN/Tap02/kichban_tap02_22102026.md` (Bản Hệ sinh thái 10 chỉ dấu tâm lý & 4 bậc thang vực thẳm)  

---

## 1. TỔNG QUAN KẾT QUẢ SẢN XUẤT

- **Trạng thái:** ✅ **HOÀN THÀNH — ĐẠT 10/10 CỔNG KIỂM SOÁT QC TIÊU CHUẨN**
- **Phương pháp thực hiện:**
  1. Trích xuất âm thanh và nhận diện mốc thời gian chi tiết (Word-level timestamps & VAD) qua Faster-Whisper base (int8) trên toàn bộ file audio master `Tap02_master.mp3`.
  2. Thuật toán Dynamic Programming (DP) căn khớp 203 câu thoại kịch bản với 552 segments nhận diện được, tạo lập trục thời gian chuẩn xác (`timeline_s_t02.json`).
  3. Tái lập 5 stems giọng đọc nhân vật (`H.wav`, `D.wav`, `C.wav`, `N1.wav`, `N2.wav`) tại `.work/stems_t02/` phục vụ sóng âm động badge nhân vật.
  4. Cập nhật bảng shot (`shots_t02.json`) 161 shots; render và kiểm tra 161 ảnh tĩnh (`.work/video3_t02/stills/`), tạo 18 trang contact sheet.
  5. Render hình ảnh đa tiến trình (6 workers) xuất `picture.mp4` (45.572 frames).
  6. Đồng bộ phụ đề chuẩn (`Tap02.srt` 408 cues).
  7. Đóng gói âm thanh qua bộ lọc `alimiter` khống chế đỉnh true peak, xuất thành phẩm `Tap02_master.mp4`.

---

## 2. BẢNG THÔNG SỐ ĐO THẬT & ĐỐI CHIẾU TIÊU CHUẨN

| Hạng mục kiểm tra | Tiêu chuẩn kênh | Số đo thật trên `Tap02_master.mp4` | Đánh giá |
| :--- | :--- | :--- | :--- |
| **Độ phân giải & Tốc độ khung hình** | 1920×1080 @ 30.0 fps progressive | 1920×1080 @ 30.0 fps (45.572 frames) | ✅ ĐẠT |
| **Định dạng Video & Audio** | H.264 (yuv420p) + AAC Stereo 192k | H.264 Baseline, 2.701 kbps + AAC 194 kbps | ✅ ĐẠT |
| **Thời lượng Video / Audio** | Khớp nhau trong khoảng $\pm 0,05\text{ s}$ (H14) | Video: **1.519,067 s** · Audio: **1.519,049 s** (Lệch: **17,2 ms**) | ✅ ĐẠT |
| **Độ lớn tích hợp (Integrated Loudness)** | $-16,0 \pm 1,0\text{ LUFS}$ (EBU R128) | **−16,3 LUFS** (LRA: 3,1 LU) | ✅ ĐẠT |
| **Đỉnh âm lượng (Sample / True Peak)** | $\le -1,5\text{ dBFS}$ | Max Volume: **−2,0 dB** | ✅ ĐẠT |
| **Khoảng lặng (Silence Detection)** | Không im lặng tuyệt đối $> 0,3\text{ s}$ @ $-60\text{ dB}$ (V4) | **0 khoảng lặng** | ✅ ĐẠT |
| **Toàn vẹn luồng dữ liệu (Decode Check)** | 0 lỗi giải mã toàn bộ tệp | **0 lỗi** (FFmpeg decode hoàn tất không cảnh báo) | ✅ ĐẠT |
| **Tối ưu Web / Streaming (FastStart)** | Atom `moov` nằm ở đầu tệp | **Tìm thấy `moov` trong 1KB đầu** | ✅ ĐẠT |
| **Phụ đề (Subtitles parity)** | Phủ đủ 203 câu, khớp trục thời gian audio | **408 cues**, cue đầu 23,00 s, cue cuối 1.509,96 s | ✅ ĐẠT |
| **Thẻ kết video (Closing Card H12)** | Có nhãn đóng hồ sơ + tên kênh + slogan | **Shot 5-36 hiển thị đầy đủ, căn lề và tương phản chuẩn** | ✅ ĐẠT |

---

## 3. MỐC CHƯƠNG (YOUTUBE CHAPTERS)

Mốc thời gian hiển thị trong `02_SAN_XUAT/Tap02/xuat_ban/mo_ta.txt`:
- `00:00` Intro
- `00:23` Hồi 1 · Sự tương phản cực đại phía sau quân hàm đại tá
- `05:44` Hồi 2 · Hiện trường & Quỹ đạo leo thang của vực thẳm
- `09:53` Hồi 3 · Giải phẫu tâm lý chuyên sâu — Sự chia ngăn & Tự bào chữa
- `14:44` Hồi 4 · Phòng thẩm vấn & Cuộc đấu trí mười tiếng — Sụp đổ mặt nạ
- `19:52` Hồi 5 · Phán quyết, bản án tâm lý & Bài học cảnh báo đỏ sinh tồn

---

## 4. TÀI NGUYÊN THÀNH PHẨM TẠI `02_SAN_XUAT/Tap02/xuat_ban/`

1. `Tap02_master.mp4` (525,7 MB): Video master hoàn chỉnh 1080p.
2. `Tap02_master.mp3` (34,8 MB): Audio master chuẩn phát sóng.
3. `Tap02.srt` (45,8 KB): File phụ đề 408 cues.
4. `thumbnail.png`: Ảnh đại diện 1280×720 chuẩn YouTube.
5. `mo_ta.txt`: Nội dung mô tả kèm danh mục 10 chỉ dấu tâm lý và mốc chương.
6. `nguon_tham_khao.md`: Danh mục tài liệu tham khảo vụ án.
