# HỒ SƠ SẢN XUẤT TẬP 66 · "CHU KHẢI LƯỢNG" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Tap66/kichban_tap66_22112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap66/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 66: Hồ Sơ Chu Khải Lượng — Màn Kịch Tìm Cha Mẹ Trước Ống Kính & Tổn Thương Ái Kỷ Hồng Kông |
| **Đề tài** | Vụ án nghịch tử Chu Khải Lượng (Henry Chau) cùng đồng phạm sát hại cha mẹ ruột tại Đại Giác Tả, Hồng Kông (Tháng 3/2013), sau đó lên truyền hình khóc lóc nhờ tìm kiếm |
| **Trọng tâm tâm lý (K10)** | Rối loạn nhân cách ái kỷ (NPD) & Phản xã hội (ASPD), Cơ chế diễn kịch trước truyền hình (Media Deception), Tâm lý đổ lỗi cho gia đình (Externalizing Blame) và Thao túng đồng phạm. |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Phóng viên / Nhân chứng (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung toàn diện vào phân tích vi biểu cảm, xung đột ái kỷ và bài học gia đình). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Nước mắt cá sấu trên truyền hình Hồng Kông, câu chuyện người con hiếu thảo và những điểm bất thường trong hồ sơ xuất nhập cảnh.
* **Hồi 2:** Bóc tách vi biểu cảm dối trá, cuộc đột kích căn hộ tại Đại Giác Tả và sự sụp đổ của màn kịch truyền thông.
* **Hồi 3:** Quá khứ bất mãn của nghịch tử từng du học Anh, tổn thương ái kỷ bệnh lý và sự thao túng đồng phạm thiểu năng.
* **Hồi 4:** Đại chiến pháp đình năm 2015, thái độ cợt nhả trước vành móng ngựa và phán quyết tù chung thân đích đáng.
* **Hồi 5:** Tổng kết vụ án và Hệ thống 3 bài học cảnh báo sâu sắc về áp lực kỳ vọng độc hại và nhận diện lệch lạc nhân cách trong gia đình.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Tap66/kichban_tap66_22112026.md`)
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Tap66_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Tap66_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Tap66_KO/`)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
