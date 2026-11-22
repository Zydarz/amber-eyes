# HỒ SƠ SẢN XUẤT TẬP 67 · "VỤ ÁN HELLO KITTY" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Tap67/kichban_tap67_22112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap67/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 67: Vụ Án Hello Kitty — Tâm Lý Nhóm Băng Đảng & Bước Thang Phi Nhân Hóa Hồng Kông |
| **Đề tài** | Vụ án giam cầm, bạo hành và sát hại thiếu nữ Phàn Mẫn Nghi tại căn hộ chung cư ở Tiêm Sa Chủy, Hồng Kông (Tháng 3–4/1999) do nhóm đòi nợ thuê thực hiện; bị bắt tháng 5/1999 |
| **Trọng tâm tâm lý (K10)** | Tâm lý bầy đàn & Hiệu ứng áp lực nhóm (Groupthink / Peer De-individuation), Quá trình leo thang phi nhân hóa nạn nhân (Escalation of Dehumanization) và Tâm lý học sang chấn nhân chứng. |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Nhân chứng thiếu niên (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (TUYỆT ĐỐI KHÔNG mô tả nhục hình hay bạo lực ghê rợn, tập trung toàn diện vào cơ chế tâm lý bầy đàn, sự tha hóa tập thể và phán quyết tư pháp). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Bí mật tại căn hộ số 31 đường Granville khu Tiêm Sa Chủy, lời khai bấn loạn của nhân chứng thiếu niên và cuộc đột kích của cảnh sát.
* **Hồi 2:** Món nợ nhỏ biến thành cạm bẫy kiểm soát cưỡng chế, chân dung kẻ cầm đầu Trần Văn Nhạc và sự lôi kéo đồng phạm.
* **Hồi 3:** Quá trình phi nhân hóa nạn nhân theo bậc thang (Dehumanization) và sự tha hóa đạo đức tập thể dưới tác động của ma túy đá.
* **Hồi 4:** Phiên tòa lịch sử năm 2000 tại Tòa án Tối cao Hồng Kông, phán quyết tù chung thân đanh thép của thẩm phán Peter Nguyễn.
* **Hồi 5:** Tổng kết vụ án và Hệ thống 3 bài học cảnh báo sinh tồn thiết thực về cạm bẫy tín dụng đen và sự cảnh giác trong cộng đồng đô thị.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Tap67/kichban_tap67_22112026.md`)
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Tap67_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Tap67_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Tap67_KO/`)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
