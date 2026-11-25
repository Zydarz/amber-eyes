# HỒ SƠ SẢN XUẤT TẬP 35 · "VỤ ÁN HELLO KITTY" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).  
**Kịch bản gốc:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap35/kichban_tap35_22112026.md`  
**Thành phẩm xuất bản:** `02_SAN_XUAT/Ho_So_Toi_Pham/Tap35/xuat_ban/`

---

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 35: Vụ Án Hello Kitty — Tâm Lý Nhóm Băng Đảng & Bước Thang Phi Nhân Hóa Hồng Kông |
| **Đề tài** | Vụ án giam cầm, tống tiền và sát hại thiếu nữ Phàn Mẫn Nghi tại căn hộ chung cư ở Tiêm Sa Chủy, Hồng Kông (tháng 3–4/1999) do nhóm đòi nợ thuê thuộc phân nhánh Hòa Thắng Hòa gồm Trần Văn Nhạc, Lương Thắng Tổ và Lương Vĩ Luân thực hiện; bị bắt tháng 5/1999 |
| **Trọng tâm tâm lý (K10 / A2c)** | Tâm lý bầy đàn & Hiệu ứng áp lực nhóm (Groupthink / Peer De-individuation), Quá trình leo thang phi nhân hóa nạn nhân (Escalation of Dehumanization), Cơ chế chia ngăn nhận thức (Compartmentalization) và Tâm lý học sang chấn nhân chứng vị thành niên. |
| **Kịch bản** | `01_KICH_BAN/Ho_So_Toi_Pham/Tap35/kichban_tap35_22112026.md` — **Cập nhật 23/11/2026** (238 câu, 5 hồi, chuẩn A2c & Rule V9) |
| **Lượt nói / câu / từ** | 19 lượt nói (34 elements) / **238 câu** / **7.179 từ** — Host 42,4% (101 câu) · Sói (Điều tra viên) 29,4% (70 câu) · Cáo (Chuyên gia tâm lý) 23,1% (55 câu) · Cừu (N1 - Nhân chứng thiếu niên) 5,1% (12 câu) |
| **Thời lượng dự kiến** | 25:00 – 28:00 (~1.600 giây) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (TUYỆT ĐỐI KHÔNG mô tả nhục hình hay bạo lực ghê rợn, tập trung toàn diện vào cơ chế tâm lý bầy đàn, sự tha hóa tập thể và phán quyết tư pháp). |

---

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1 (49 câu / 1.475 từ):** Bóng tối sau ánh đèn Tiêm Sa Chủy, lời thú nhận kinh hoàng của nhân chứng thiếu niên 14 tuổi A Phương và cuộc đột kích của Đội Trọng án Cửu Long tại số 31 đường Granville.
* **Hồi 2 (48 câu / 1.479 từ):** Món nợ nhỏ biến thành cạm bẫy kiểm soát cưỡng chế, chân dung kẻ săn mồi Trần Văn Nhạc và sự lôi kéo đồng phạm Lương Thắng Tổ, Lương Vĩ Luân.
* **Hồi 3 (50 câu / 1.473 từ):** Quá trình leo thang phi nhân hóa nạn nhân (Dehumanization), giải thể nhân cách (De-individuation) dưới tác động của ma túy đá và nghịch lý chia ngăn nhận thức (Compartmentalization).
* **Hồi 4 (48 câu / 1.545 từ):** Phiên tòa lịch sử năm 2000 tại Tòa án Tối cao Hồng Kông, phán quyết tù chung thân đanh thép của Thẩm phán Peter Nguyễn và phiên phúc thẩm năm 2004 của Lương Thắng Tổ.
* **Hồi 5 (43 câu / 1.207 từ):** Dư chấn đô thị, hiệu ứng người ngoài cuộc (Bystander Effect) và Hệ thống 3 bài học cảnh báo sinh tồn thiết thực về cạm bẫy tín dụng đen.

---

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Ho_So_Toi_Pham/Tap35/kichban_tap35_22112026.md`) — **ĐẠT (238 câu, 0 lỗi V9, đủ 10 chỉ dấu K10)**
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Ho_So_Toi_Pham/Tap35_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Ho_So_Toi_Pham/Tap35_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Ho_So_Toi_Pham/Tap35_KO/`)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)

---

## PHỤ LỤC A (Tập 35) — CẤU TRÚC KỊCH BẢN (`parse_kichban.py` trên `kichban_tap35_22112026.md`, 23/11/2026)

Mọi bước kỹ thuật tiếp theo phải sinh ra **đúng bảng này**; khác là dừng và báo.

| Mã | Vai / loại | Câu | Từ | Chỉ dẫn / mô tả |
|---|---|---:|---:|---|
| `1.01` | *BGM* | — | — | Tiếng còi xe ồn ào của khu mua sắm sầm uất Tiêm Sa Chủy, tiếng bước chân trinh sát leo cầu thang chung cư cũ kỹ và âm thanh piano ngột ngạt. |
| `1.02` | Cú · Host | 15 | 481 | giọng trầm ấm, mở đầu với sự nghiêm nghị |
| `1.03` | *SFX* | — | — | Tiếng quạt trần quay kẽo kẹt trong phòng thẩm vấn, tiếng thở dốc ngắt quãng. |
| `1.04` | Cừu · Người bình thường (N1) | 12 | 327 | giọng run rẩy, ám ảnh sâu sắc |
| `1.05` | *SFX* | — | — | Tiếng lật hồ sơ giấy tờ, tiếng bộ đàm rè nhẹ. |
| `1.06` | Cú · Host | 6 | 187 | giọng hạ thấp, chuyển giao lời kể |
| `1.07` | *SFX* | — | — | Tiếng bước chân rầm rập trên cầu thang xi măng cũ, tiếng xích sắt phá khóa cửa kêu chói tai. |
| `1.08` | Sói · Điều tra viên | 16 | 480 | giọng đanh thép, lạnh lùng và chuẩn xác |
| `2.01` | *BGM* | — | — | Tiếng thở dài nặng nề, âm thanh guitar bass chậm rãi biểu thị cạm bẫy xã hội đen đang siết chặt. |
| `2.02` | Cú · Host | 15 | 449 | lật mở nguồn cơn vụ việc |
| `2.03` | *SFX* | — | — | Tiếng đập bàn gỗ chấn động, tiếng thở dốc đe dọa. |
| `2.04` | Sói · Điều tra viên | 12 | 392 | phân tích chân dung đối tượng cầm đầu và thủ đoạn bắt giữ |
| `2.05` | *BGM* | — | — | Âm thanh cello trầm đục, mang đậm màu sắc phân tích tâm lý học tội phạm. |
| `2.06` | Cáo · Chuyên gia tâm lý | 13 | 412 | phân tích cơ chế kiểm soát cưỡng chế và ngòi nổ tâm lý |
| `2.07` | Cú · Host | 8 | 226 | bóc trần bẫy nợ xã hội đen |
| `3.01` | *BGM* | — | — | Tiếng trống điện tử dồn dập, âm thanh kim loại va chạm khô khốc và không gian âm nhạc ngột ngạt đến nghẹt thở. |
| `3.02` | Cú · Host | 5 | 161 | dẫn dắt bước vào giai đoạn leo thang tội ác |
| `3.03` | Cáo · Chuyên gia tâm lý | 14 | 391 | phân tích chuyên sâu về hiện tượng Dehumanization và Groupthink |
| `3.04` | *SFX* | — | — | Tiếng cười rộ lên man rợ rồi tắt lịm, tiếng kim loại va đập khô khốc. |
| `3.05` | Sói · Điều tra viên | 12 | 362 | chỉ rõ sự tha hóa hành vi và vai trò của các đối tượng |
| `3.06` | Cú · Host | 10 | 293 | phân tích nghịch lý chia ngăn nhận thức |
| `3.07` | Sói · Điều tra viên | 9 | 266 | thuật lại thời điểm nạn nhân tử vong |
| `4.01` | *BGM* | — | — | Tiếng búa gõ tòa án vang dội, tiếng xì xào của phòng xử án và giọng đọc cáo trạng đanh thép của thẩm phán. |
| `4.02` | Cú · Host | 10 | 299 | thuật lại cuộc truy quét đồng loạt của lực lượng chức năng |
| `4.03` | *SFX* | — | — | Tiếng giấy tờ sột soạt, tiếng micro rè trong phòng xử án. |
| `4.04` | Sói · Điều tra viên | 14 | 431 | tái hiện cuộc chiến pháp lý căng thẳng tại tòa |
| `4.05` | Cáo · Chuyên gia tâm lý | 9 | 277 | bóc trần phản ứng của các bị cáo trước búa tòa |
| `4.06` | *SFX* | — | — | Ba tiếng gõ búa tòa dứt khoát: Cốp... Cốp... Cốp. |
| `4.07` | Cú · Host | 8 | 291 | tuyên đọc phán quyết lịch sử của thẩm phán |
| `4.08` | Sói · Điều tra viên | 7 | 247 | bổ sung diễn biến phúc thẩm sau đó |
| `5.01` | *BGM* | — | — | Tiếng đàn piano trầm ấm, sâu lắng, khép lại bản án với thông điệp cảnh tỉnh mạnh mẽ cho cộng đồng. |
| `5.02` | Cú · Host | 15 | 460 | tổng kết di chứng xã hội và bài học lịch sử |
| `5.03` | Cáo · Chuyên gia tâm lý | 19 | 508 | đúc kết hệ thống 3 bài học cảnh báo sinh tồn |
| `5.04` | Cú · Host | 9 | 239 | lời kết chương trình, nhấn mạnh thông điệp nhân văn |
