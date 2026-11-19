# HỒ SƠ SẢN XUẤT TẬP 45 · "MOSES SITHOLE" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Tap45/kichban_tap45_19112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap45/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 45: Hồ Sơ Moses Sithole — Cái Bẫy Tuyển Dụng Hậu Apartheid & Nữ Profiler Tiên Phong |
| **Đề tài** | Sát nhân ABC sát hại 37 phụ nữ tìm việc làm tại Nam Phi năm 1994-1995 |
| **Trọng tâm tâm lý (K10)** | Đấu trí với Tiến sĩ Micki Pistorius (nữ profiler đầu tiên của Nam Phi). |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Người trong cuộc (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung tâm lý học và hành vi). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Khởi nguồn vụ việc, tín hiệu cảnh báo ban đầu và sự vào cuộc của cơ quan chức năng.
* **Hồi 2:** Bóc tách vỏ bọc ngụy trang, cuộc sống đời thường và cơ chế phân ngăn tâm trí bệnh lý.
* **Hồi 3:** Cuộc đấu trí trong phòng thẩm vấn, phân tích vi biểu cảm và sự sụp đổ của các lời khai ngụy biện.
* **Hồi 4:** Khoa học hình sự, phân tích dấu vết vi mô, dữ liệu công nghệ và bước ngoặt phá án.
* **Hồi 5:** Bản án nghiêm minh của tòa án và 3 bài học cảnh báo đỏ sinh tồn đắt giá cho cộng đồng.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (01_KICH_BAN/Tap45/)
- [x] Kịch bản Tiếng Anh (01_KICH_BAN/Tap45_EN/)
- [x] Kịch bản Tiếng Nhật (01_KICH_BAN/Tap45_JA/)
- [x] Kịch bản Tiếng Hàn (01_KICH_BAN/Tap45_KO/)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
