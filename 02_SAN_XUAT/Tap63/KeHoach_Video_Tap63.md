# HỒ SƠ SẢN XUẤT TẬP 63 · "NGÔ TẠ VŨ" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Tap63/kichban_tap63_22112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap63/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 63: Hồ Sơ Ngô Tạ Vũ — Thảm Án Đại Học Bắc Kinh & Sự Sụp Đổ Của Chiếc Mặt Nạ Hoàn Hảo |
| **Đề tài** | Vụ án nghịch tử sát hại mẹ ruột tại Phúc Châu (Tháng 7/2015) do Ngô Tạ Vũ — cựu sinh viên xuất sắc Đại học Bắc Kinh thực hiện; trốn nã hơn 3 năm đến khi bị bắt năm 2019 |
| **Trọng tâm tâm lý (K10)** | Tâm lý học phát triển & Áp lực kỳ vọng gia đình, Tổn thương ái kỷ bệnh lý (Pathological Narcissism), Cơ chế tự hủy hoại bản ngã và Ảo tưởng cứu rỗi sai lệch. |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Bạn học / Người quen (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung toàn diện vào xung đột tâm lý gia đình, bẫy ái kỷ và bài học giáo dục). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Hình tượng "con nhà người ta" hoàn hảo tại Đại học Bắc Kinh và sự thật sau căn phòng tập thể khóa kín.
* **Hồi 2:** Áp lực kỳ vọng ngột ngạt từ người mẹ, sự nứt vỡ của mặt nạ ái kỷ và ảo tưởng cứu rỗi méo mó.
* **Hồi 3:** Cuộc đời hai mặt tại Trùng Khánh: huấn luyện viên thể hình, nhân viên quán bar và sự bùng phát bản năng tha hóa.
* **Hồi 4:** Vòng vây an ninh nhận diện AI tại sân bay Giang Bắc và cuộc đối chất trí thức tại phòng xử án.
* **Hồi 5:** Bản án tử hình thi hành và 3 bài học cảnh báo đỏ sâu sắc về giáo dục cảm xúc gia đình hiện đại.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Tap63/kichban_tap63_22112026.md`)
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Tap63_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Tap63_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Tap63_KO/`)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
