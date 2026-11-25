# HỒ SƠ SẢN XUẤT TẬP 39 · "LAO VINH CHI & PHÁP TỬ ANH" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap39/kichban_tap39_22112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Ho_So_Toi_Pham/Tap39/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 39: Hồ Sơ Lao Vinh Chi & Pháp Tử Anh — Tâm Lý Đồng Phạm & Mặt Nạ Nạn Nhân Suốt 20 Năm |
| **Đề tài** | Chuỗi vụ án bắt cóc, cướp tài sản và sát hại nhiều người do cặp đôi Pháp Tử Anh và Lao Vinh Chi thực hiện (1996–1999); Lao Vinh Chi trốn nã 20 năm đến khi sa lưới năm 2019 |
| **Trọng tâm tâm lý (K10)** | Tâm lý đồng phạm (Folie à deux), Thao túng tâm lý và Hội chứng phụ thuộc, Cơ chế tự bào chữa & Phản xạ đóng vai nạn nhân (Victim Playing). |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Người quen / Nhân chứng (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung toàn diện vào cơ chế tâm lý đồng phạm, vi biểu cảm và đấu trí pháp đình). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Cô giáo tiểu học và gã giang hồ bất hảo, nguồn gốc của liên minh tội ác độc hại.
* **Hồi 2:** Trận đấu súng nghẹt thở tại Hợp Phì năm 1999 và cuộc đào tẩu hai mươi năm dưới lớp vỏ bọc thanh lịch.
* **Hồi 3:** Khoảnh khắc nhận diện bằng AI tại Hạ Môn và nụ cười thách thức kỳ dị trước ống kính máy quay.
* **Hồi 4:** Màn kịch nước mắt tại phiên tòa, chiến thuật đóng vai nạn nhân và sự sụp đổ trước chứng cứ thực nghiệm.
* **Hồi 5:** Bản án tử hình được thi hành và Hệ thống 3 bài học cảnh báo nhận diện bẫy thao túng đồng phạm.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Ho_So_Toi_Pham/Tap39/kichban_tap39_22112026.md`) — Đã duyệt chính tả & 240 câu chuẩn
- [x] Phụ lục A Bảng câu thoại (`02_SAN_XUAT/Ho_So_Toi_Pham/Tap39/PhuLucA_BangCau_Tap39.md`) — 240/240 câu
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Ho_So_Toi_Pham/Tap39_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Ho_So_Toi_Pham/Tap39_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Ho_So_Toi_Pham/Tap39_KO/`)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
