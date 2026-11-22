# HỒ SƠ SẢN XUẤT TẬP 61 · "KỲ ÁN ĐIÊU ÁI THANH" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Tap61/kichban_tap61_22112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap61/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 61: Kỳ Án Điêu Ái Thanh — Bí Ẩn Đại Học Nam Kinh & Tâm Lý Hủy Hoại Chứng Cứ Cực Đoan |
| **Đề tài** | Vụ mất tích và án mạng của nữ sinh viên Điêu Ái Thanh tại Đại học Nam Kinh, Giang Tô, Trung Quốc (Tháng 1/1996) |
| **Trọng tâm tâm lý (K10)** | Tâm lý kiểm soát & hủy hoại chứng cứ cực đoan (Extreme Destruction), Dấu ấn Signature vs. Thủ đoạn MO, Điểm mù xã hội và Áp lực đô thị hóa. |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Bạn học / Nhân chứng (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả chi tiết rùng rợn, tập trung toàn diện vào khoa học hành vi, bối cảnh tâm lý xã hội và pháp y). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Buổi tối mùa đông năm 1996 tại Đại học Nam Kinh, bóng dáng cô nữ sinh và sự biến mất đầy u uẩn.
* **Hồi 2:** Phân tích dấu ấn hành vi chuyên nghiệp, sự bình tĩnh đáng sợ và không gian tội ác khép kín.
* **Hồi 3:** Điểm mù đô thị thời kỳ đầu mở cửa, sự thiếu hụt công nghệ giám sát và những bế tắc điều tra.
* **Hồi 4:** Quyết định không áp dụng thời hiệu miễn trừ, nỗ lực phân tích ADN thế hệ mới và bản án tâm lý đối với kẻ thủ ác.
* **Hồi 5:** Nỗi đau khắc khoải của gia đình và 3 nguyên tắc sinh tồn đô thị quý giá cho sinh viên xa nhà.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Tap61/kichban_tap61_22112026.md`)
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Tap61_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Tap61_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Tap61_KO/`)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
