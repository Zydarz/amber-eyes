# HỒ SƠ SẢN XUẤT TẬP 34 · "NGUYỄN ĐỨC NGHĨA" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A), Hệ sinh thái 10 chỉ dấu tâm lý (A2c, K10), Quy tắc V1–V9, G1–G13.  
**Kịch bản gốc:** `01_KICH_BAN/Tap34/kichban_tap34_19112026.md` (240 câu)  
**Kịch bản đối chiếu đa ngữ:** `01_KICH_BAN/Tap34_EN/` (240 câu) · `01_KICH_BAN/Tap34_JA/` (240 câu)  
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap34/xuat_ban/`

---

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 34: Vỏ Bọc Sinh Viên Ưu Tú & Sự Tê Liệt Cảm Xúc Sau Chiếc Kính Cận (Hồ Sơ Nguyễn Đức Nghĩa) |
| **Đề tài** | Án mạng tại chung cư G4 Trung Hòa - Cầu Giấy, Hà Nội gây rúng động năm 2010 |
| **Trọng tâm tâm lý (K10)** | Hiệu ứng hào quang trí thức, Cơ chế phân ngăn tâm trí (Compartmentalization), Tẩy xóa nhân dạng (Depersonalization), Bản chất sự hối hận và Tăng trưởng sau sang chấn (PTG). |
| **Thời lượng dự kiến** | 28:00 – 32:00 (~1.800 giây) |
| **Giọng đọc phân bổ** | Host (Cú, ~48%) · Điều tra viên (Sói, ~24%) · Chuyên gia tâm lý (Cáo, ~22%) · N1 (Cư dân G4, ~3%) · N2 (Hoàng Thị Yến, ~3%) |
| **Quy tắc an toàn YouTube** | 100% YouTube Safe theo Tiêu chuẩn V9 (Tuyệt đối không mô tả bạo lực ghê rợn, 100% tập trung khoa học hành vi và tâm lý học tội phạm). |

---

## B2. Kế hoạch sản xuất chi tiết 5 Hồi (Chuẩn A2c / K10)

* **Hồi 1 (Án mạng trên tầng thượng & Điểm mù đô thị - 53 câu):** Sự biến mất bí ẩn của nạn nhân, phát hiện thi thể tại tầng thượng chung cư G4, điểm mù đô thị chung cư và tâm lý bàng quan tập thể.
* **Hồi 2 (Vỏ bọc thư sinh & Cạm bẫy của sự quen thuộc - 53 câu):** Hình tượng cựu sinh viên Ngoại thương ưu tú, lối sống ngầm nợ nần cờ bạc, cạm bẫy gặp lại người yêu cũ tại căn hộ 1101 và cơ chế phân ngăn tâm trí bệnh lý ("như một con rô-bốt").
* **Hồi 3 (Cuộc đấu trí trong phòng thẩm vấn & Sự sụp đổ bản ngã - 49 câu):** Cuộc truy bắt thần tốc tại Thái Nguyên, chiến thuật đấu trí bao vây logic tại số 7 Thiền Quang, hành trình lặn mò tìm vật chứng trên sông Cấm và khoảnh khắc sụp đổ của bản ngã ái kỷ.
* **Hồi 4 (Bản chất sự hối hận & Bi kịch hai người cha - 47 câu):** Phiên tòa sơ thẩm 7/2010; giọt nước mắt của Hoàng Thị Yến khi nghe câu "Anh xin lỗi"; bóc tách cơ chế hối hận (chấn thương bản ngã ái kỷ vs. bản năng sinh tồn kháng cáo); bi kịch người cha cựu chiến binh (ông Hùng) tử nạn giao thông.
* **Hồi 5 (Bản án tối hậu, sự tha thứ & Bài học cảnh báo đỏ - 38 câu):** Bác đơn kháng cáo và thi hành án tử hình tháng 7/2014; nghĩa cử nhân văn của người cha nạn nhân (ông Ba) gửi thư chia buồn và hoa viếng bố hung thủ; 3 nguyên tắc cảnh báo đỏ sinh tồn cốt lõi.

---

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] **Bước 1: Kịch bản được duyệt** (VN 240 câu, EN 240 câu, JA 240 câu khớp 1:1, Rule V9 PASS)
- [x] **Bước 2: Tách kịch bản kỹ thuật** (`parse_kichban.py` -> `.work/script_tap34.json`, `.work/script_tap34_EN.json`, `.work/script_tap34_JA.json`)
- [x] **Bước 3: Khai báo hệ thống & Diễn xuất** (Cấu hình `EPISODES['34']` trong `edition.py`, sinh `.work/acting_tap34.json`)
- [ ] **Bước 4: Sinh giọng đọc TTS** (`tts_sentences.py` cho 240 câu)
- [ ] **Bước 5: Kiểm tra giọng theo vai** (`voice_role_check.py` đạt G8–G10)
- [ ] **Bước 6: Dựng audio master & Đo đạc** (`build_audio3.py`, `qc_pause_gate.py`, -16 LUFS, TP <= -1.5 dBFS)
- [ ] **Bước 7: Lập bảng shot** (`parse_shots.py`, `qc_bg_shared.py`)
- [ ] **Bước 8: Sinh ảnh tĩnh & Duyệt khung hình** (`build_video3.py --stills`)
- [ ] **Bước 9: Dựng video hoàn thiện** (`build_video3.py --workers 6`)
- [ ] **Bước 10: Phụ đề & Đóng gói xuất bản** (`subtitles.py`, `package.py --mux`)
