# HỒ SƠ SẢN XUẤT TẬP 36 · "KIP KINKEL" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).  
**Kịch bản gốc:** `01_KICH_BAN/Tap36/kichban_tap36_19112026.md`  
**Kịch bản Tiếng Anh:** `01_KICH_BAN/Tap36_EN/kichban_tap36_EN.md`  
**Kịch bản Tiếng Nhật:** `01_KICH_BAN/Tap36_JA/kichban_tap36_JA.md`  
**Tài liệu nghiên cứu chuyên sâu:** `01_KICH_BAN/Tap36/NghienCuu_TamLy_BoSung_KichBan_Tap36.md`  
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap36/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 36: Tiếng Nói Trong Tâm Trí — Khởi Phát Tâm Thần Phân Liệt & Cơn Địa Chấn Thurston High (Hồ Sơ Kip Kinkel) |
| **Đề tài** | Thiếu niên 15 tuổi sát hại cha mẹ rồi xả súng tại trường trung học Thurston, Springfield, Oregon năm 1998 |
| **Trọng tâm tâm lý (K10)** | Khởi phát tâm thần phân liệt sớm, Ảo giác thính giác mệnh lệnh, Điểm mù gia đình giáo viên, Tổn thương ái kỷ & Bản chất sự hối hận sau 23 năm. |
| **Tổng số câu thoại** | **240 câu** (Khớp tuyệt đối 1:1 cả 3 ngôn ngữ: Việt, Anh, Nhật; 36 khối LOI elements). |
| **Thời lượng dự kiến** | 28:00 – 32:00 (~1.700 – 1.900 giây) |
| **Giọng đọc phân bổ** | Host (~51.2% - 123 câu) · Điều tra viên (~21.2% - 51 câu) · Chuyên gia tâm lý (~22.1% - 53 câu) · Người trong cuộc (~5.4% - 13 câu: N1 bạn học, N2 trần tình Kip Kinkel). |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung tâm lý học và hành vi). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1: Cơn Địa Chấn Thurston High & Ảo Tưởng Bình Yên Thôn Dã (47 câu):** Bối cảnh thị trấn ngoại ô Springfield, ảo tưởng bình yên, thảm kịch căn tin sáng 21/05/1998, sự dũng cảm của Jake Ryker quật ngã hung thủ, lời thú nhận ban đầu.
* **Hồi 2: Điểm Mù Gia Đình Giáo Viên & Quỹ Đạo Leo Thang Ảo Giác (57 câu):** Hiện trường căn nhà gỗ phủ vải trắng, chân dung cha mẹ giáo viên danh giá, căn bệnh tâm thần phân liệt khởi phát từ năm 12 tuổi, ảo giác thính giác mệnh lệnh và sự thỏa hiệp mua súng sai lầm của người cha.
* **Hồi 3: Ngòi Nổ Điểm Gãy 20/05/1998 & Cơn Ác Mộng Căn Tin (52 câu):** Vụ trộm súng từ bạn học Korey Ewert, bị còng tay đình chỉ học, cuộc điện thoại định mệnh của cha, điểm gãy tổn thương ái kỷ, thảm kịch gia đình và đêm kinh hoàng trước vụ xả súng.
* **Hồi 4: Phòng Hỏi Cung, Ảo Thanh Mệnh Lệnh & Bản Chất Sự Hối Hận (48 câu):** Cuộc hỏi cung nghẹt thở của Thám tử Al Warthen, phân tích sự sụp đổ hoảng loạn 1998 VS. sự ăn năn bản thể sau 23 năm (phỏng vấn 2021), tác động của thuốc chống loạn thần và sự hoàn thiện vỏ não trước trán.
* **Hồi 5: Bản Án 111 Năm, Sự Thức Tỉnh Sau 23 Năm & Bài Học Sinh Tồn (36 câu):** Bản án không ân xá, di sản an ninh học đường (Đánh giá nguy cơ đe dọa), 3 nguyên tắc nhận diện khủng hoảng tâm thần học đường và bảo vệ vũ khí gia đình.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt 240 câu (`01_KICH_BAN/Tap36/kichban_tap36_19112026.md`)
- [x] Kịch bản Tiếng Anh 240 câu (`01_KICH_BAN/Tap36_EN/kichban_tap36_EN.md`)
- [x] Kịch bản Tiếng Nhật 240 câu (`01_KICH_BAN/Tap36_JA/kichban_tap36_JA.md`)
- [x] Tách câu & xuất JSON sản xuất (`parse_kichban.py` -> `.work/script_tap36.json`, `script_tap36_EN.json`, `script_tap36_JA.json`)
- [x] File diễn xuất & nhịp nghỉ sản xuất (`make_acting_tap36.py` -> `.work/acting_tap36.json` - 240/240 câu có pause_after)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
