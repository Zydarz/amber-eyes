# HỒ SƠ SẢN XUẤT TẬP 41 · "DR. HAROLD SHIPMAN" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap41/kichban_tap41_19112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Ho_So_Toi_Pham/Tap41/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 41: Hồ Sơ Dr. Harold Shipman — Thiên Thần Tử Thần & Phức Cảm Thượng Đế Y Khoa |
| **Đề tài** | Bác sĩ gia đình uy tín tại Anh sát hại hơn 215 bệnh nhân lớn tuổi suốt 24 năm |
| **Trọng tâm tâm lý (K10)** | Phức cảm Thượng đế (God Complex), Lạm dụng lòng tin áo trắng, Kiểm toán hồ sơ bệnh án. |
| **Thời lượng dự kiến** | 28:00 – 32:00 (~1.800 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Người trong cuộc (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung tâm lý học và hành vi). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Khởi nguồn vụ việc, tín hiệu cảnh báo ban đầu và sự vào cuộc của cơ quan chức năng.
* **Hồi 2:** Bóc tách vỏ bọc ngụy trang, cuộc sống đời thường và cơ chế phân ngăn tâm trí bệnh lý.
* **Hồi 3:** Cuộc đấu trí trong phòng thẩm vấn, phân tích vi biểu cảm và sự sụp đổ của các lời khai ngụy biện.
* **Hồi 4:** Khoa học hình sự, phân tích dấu vết vi mô, dữ liệu công nghệ và bước ngoặt phá án.
* **Hồi 5:** Bản án nghiêm minh của tòa án và 3 bài học cảnh báo đỏ sinh tồn đắt giá cho cộng đồng.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (01_KICH_BAN/Ho_So_Toi_Pham/Tap41/)
- [x] Kịch bản Tiếng Anh (01_KICH_BAN/Ho_So_Toi_Pham/Tap41_EN/)
- [x] Kịch bản Tiếng Nhật (01_KICH_BAN/Ho_So_Toi_Pham/Tap41_JA/)
- [x] Kịch bản Tiếng Hàn (01_KICH_BAN/Ho_So_Toi_Pham/Tap41_KO/)
- [x] Tách câu (`parse_kichban.py`) -> Đã sinh `script_tap41.json` (227 câu), `script_tap41_EN.json` (251 câu), `script_tap41_JA.json` (242 câu)
- [x] Diễn xuất kịch bản (`make_acting_tap41.py`) -> Đã sinh `acting_tap41.json` (227 câu, nhịp nghỉ trung vị 0.65s đạt chuẩn A13)
- [x] Khai báo cấu hình sản xuất `EPISODES['37']` trong `.work/edition.py` & bảng âm thanh `.work/sfx_tap41.json`
- [ ] Sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
