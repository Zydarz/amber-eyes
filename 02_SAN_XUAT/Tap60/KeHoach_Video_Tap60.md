# HỒ SƠ SẢN XUẤT TẬP 60 · "SÁT NHÂN BẠCH NGÂN" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Tap60/kichban_tap60_22112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap60/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 60: Hồ Sơ Sát Nhân Bạch Ngân — Bóng Ma 28 Năm & Bước Ngoặt Phả Hệ ADN |
| **Đề tài** | Vụ án sát nhân liên hoàn Bạch Ngân (Bạch Ngân, Cam Túc & Bao Đầu, Nội Mông, Trung Quốc, 1988–2002) do Cao Thừa Dũng thực hiện, phá án tháng 8/2016 |
| **Trọng tâm tâm lý (K10)** | Phân liệt hai mặt (Dual Identity), Sự nhẫn nại bệnh lý (Pathological Patience), Ảo tưởng kiểm soát và Phá án bằng phả hệ ADN dòng Y (Y-STR Chromosome Profiling). |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Người trong cuộc (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Tuyệt đối không mô tả bạo lực ghê rợn hay thương tích; tập trung 100% vào phân tích tâm lý học hành vi và khoa học pháp y). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Ám ảnh đô thị công nghiệp, nỗi sợ hãi bao trùm Bạch Ngân và thách thức điều tra kéo dài nhiều thập kỷ.
* **Hồi 2:** Bóc tách mặt nạ đời thường, cơ chế phân ngăn tâm trí bệnh lý và sự nhẫn nại đáng sợ của kẻ thủ ác.
* **Hồi 3:** Bức tường bế tắc trong công tác truy tìm và bước đột phá mang tính cách mạng của công nghệ phả hệ ADN dòng Y (Y-STR).
* **Hồi 4:** Khoảnh khắc còng số tám tra vào tay, phản ứng đóng băng cảm xúc tại phòng thẩm vấn và sự sụp đổ của ảo tưởng an toàn.
* **Hồi 5:** Bản án nghiêm khắc của pháp luật và Hệ sinh thái 3 cảnh báo đỏ sinh tồn đắt giá cho cộng đồng.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Tap60/kichban_tap60_22112026.md`)
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Tap60_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Tap60_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Tap60_KO/`)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
