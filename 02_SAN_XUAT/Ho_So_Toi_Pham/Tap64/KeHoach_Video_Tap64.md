# HỒ SƠ SẢN XUẤT TẬP 64 · "CHU KHẮC HOA" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap64/kichban_tap64_22112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Ho_So_Toi_Pham/Tap64/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 64: Hồ Sơ Chu Khắc Hoa — Sát Nhân Cướp Bóng Ma & Tâm Lý Sói Đơn Độc Cực Đoan |
| **Đề tài** | Chuỗi vụ án dùng súng cướp ngân hàng và sát hại người vô tội liên tỉnh suốt 8 năm (2004–2012) tại Trùng Khánh, Trường Sa, Nam Kinh do Chu Khắc Hoa thực hiện; bị tiêu diệt tháng 8/2012 |
| **Trọng tâm tâm lý (K10)** | Tâm lý "Sói đơn độc" (Lone Wolf), Rối loạn nhân cách chống đối xã hội (ASPD), Sự cô lập cảm xúc tuyệt đối và Kỹ năng sinh tồn quân sự hóa phục vụ tội ác. |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Nhân chứng / Cán bộ tuần tra (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung phân tích tâm lý hành vi, chiến thuật vây bắt và bài học phòng ngừa tội phạm vũ trang). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Bóng ma cửa ngân hàng, chuỗi án mạng liên tỉnh 8 năm và nỗi sợ hãi bao trùm các đô thị ven sông Trường Giang.
* **Hồi 2:** Chân dung con sói đơn độc Chu Khắc Hoa, sự cô lập cảm xúc tuyệt đối và kỹ năng sinh tồn dã ngoại đáng sợ.
* **Hồi 3:** Cuộc vây bắt quy mô lịch sử với vạn cán bộ chiến sĩ tại núi Ca Lạc dưới cái nóng 40 độ C.
* **Hồi 4:** Màn đấu súng chớp nhoáng tại ngõ hẻm Đồng Thoại Phường và khoảnh khắc bóng ma gục ngã trước công lý.
* **Hồi 5:** Tổng kết chuyên án và Hệ thống 3 bài học cảnh báo đỏ phòng ngừa tội phạm cướp ngân hàng có vũ trang.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Ho_So_Toi_Pham/Tap64/kichban_tap64_22112026.md`)
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Ho_So_Toi_Pham/Tap64_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Ho_So_Toi_Pham/Tap64_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Ho_So_Toi_Pham/Tap64_KO/`)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
