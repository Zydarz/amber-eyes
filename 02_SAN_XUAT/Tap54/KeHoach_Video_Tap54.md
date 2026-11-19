# HỒ SƠ SẢN XUẤT TẬP 54 · "THÙNG XI MĂNG TÂN TRANG" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Tap54/kichban_tap54_19112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap54/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 54: Hồ Sơ Thùng Xi Măng Tân Trang — Thù Hận Tích Tụ Dưới Mái Nhà & Ngôi Mộ Trong Phòng Ngủ |
| **Đề tài** | Mâu thuẫn nhà ở thừa kế tại Đài Loan năm 2018, chị dâu sát hại em chồng đắp xi măng |
| **Trọng tâm tâm lý (K10)** | Bùng nổ hung hăng thụ động (Passive-Aggressive), Cơ chế chối bỏ thực tại (Denial). |
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

- [x] Kịch bản Tiếng Việt (01_KICH_BAN/Tap54/)
- [x] Kịch bản Tiếng Anh (01_KICH_BAN/Tap54_EN/)
- [x] Kịch bản Tiếng Nhật (01_KICH_BAN/Tap54_JA/)
- [x] Kịch bản Tiếng Hàn (01_KICH_BAN/Tap54_KO/)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
