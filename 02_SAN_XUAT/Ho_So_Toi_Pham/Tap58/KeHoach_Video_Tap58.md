# HỒ SƠ SẢN XUẤT TẬP 58 · "THẢM ÁN SNOWTOWN" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap58/kichban_tap58_19112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Ho_So_Toi_Pham/Tap58/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 58: Hồ Sơ Thảm Án Snowtown — Những Chiếc Thùng Axit & Kẻ Thao Túng Lòng Thù Hận |
| **Đề tài** | Vụ án giết người cất giấu thi thể trong hầm ngân hàng bỏ hoang tại Nam Úc (1992–1999) |
| **Trọng tâm tâm lý (K10)** | Thủ lĩnh độc tài thao túng tâm lý, Loạn thần chia sẻ (Folie à plusieurs), Ngụy biện công lý ngầm, Cơ chế chia ngăn tâm trí (Compartmentalization). |
| **Thời lượng dự kiến** | 28:00 – 32:00 (~1.700 – 1.900 giây) |
| **Số câu kịch bản** | **240 câu** (Host: 124 câu, Điều tra viên: 57 câu, Chuyên gia tâm lý: 46 câu, Người bình thường: 13 câu) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Người trong cuộc (N1/N2) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung tâm lý học và hành vi). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1 (50 câu):** Bóng ma trong hầm ngân hàng Snowtown (20/5/1999) và bức màn sương sa mạc. Dư chấn xã hội, phát hiện 6 thùng hóa chất chứa hài cốt 8 nạn nhân, và sự khởi đầu của chuyên án điều tra liên vùng.
* **Hồi 2 (70 câu):** Bóc tách chân dung John Justin Bunting tại ngoại ô Adelaide. Cơ chế thao túng bầy đàn, hội chứng Folie à plusieurs, lôi kéo Robert Wagner & James Vlassakis. Bức tường nhện, sự ngụy biện "thanh trừng tệ nạn" để che giấu lòng tham tài chính (chiếm đoạt trợ cấp xã hội). Chữ ký Signature (ép ghi âm giọng nói) vs Thủ đoạn MO (di chuyển thùng hóa chất).
* **Hồi 3 (48 câu):** Chuyên án Taskforce Chart theo dõi di biến động sau sự mất tích của Elizabeth Haydon. Khám xét khẩn cấp hầm ngân hàng Snowtown và bắt giữ đồng loạt ngày 21/5/1999. Cuộc đấu trí phòng hỏi cung với James Vlassakis, bóc tách tâm lý bầy đàn và bước ngoặt Vlassakis trở thành nhân chứng Hoàng gia.
* **Hồi 4 (41 câu):** Phiên tòa lịch sử năm 2002–2003 tại Tòa án Tối cao Nam Úc do Thẩm phán Brian Martin chủ tọa. Đóng góp của khoa học giám định ADN vi mô và chứng cứ tài chính. Bản án 11 án tù chung thân không ân xá cho John Bunting và 10 án chung thân cho Robert Wagner.
* **Hồi 5 (31 câu):** Bản án lương tri và 3 bài học cảnh báo đỏ sinh tồn đắt giá cho cộng đồng về nhận diện kẻ thao túng độc tài, tránh bẫy đồng lõa và củng cố sự gắn kết gia đình - an ninh khu dân cư.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt 240 câu đạt chuẩn K10/V9 (`01_KICH_BAN/Ho_So_Toi_Pham/Tap58/kichban_tap58_19112026.md`)
- [ ] Cập nhật bản dịch Kịch bản Tiếng Anh (Tap58_EN)
- [ ] Cập nhật bản dịch Kịch bản Tiếng Nhật (Tap58_JA)
- [ ] Cập nhật bản dịch Kịch bản Tiếng Hàn (Tap58_KO)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
