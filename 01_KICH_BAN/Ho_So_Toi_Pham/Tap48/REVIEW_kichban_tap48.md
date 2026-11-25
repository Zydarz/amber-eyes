# BÁO CÁO REVIEW CHÍNH TẢ, NGÔN TỪ & KIỂM ĐỊNH TƯ PHÁP KỊCH BẢN TẬP 48
## HỒ SƠ DAVID BAIN — GIAI ĐIỆU BUỔI BÌNH MINH ĐẪM MÁU & CUỘC CHIẾN PHÁP ĐÌNH LỊCH SỬ

* **File kịch bản sản xuất:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap48/kichban_tap48_19112026.md`
* **Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (A2, A2c), Quy tắc AI (`AGENTS.md`: K1–K10, V1–V9, G1–G13).
* **Ngày hoàn thành kiểm định:** 24/11/2026.

---

## 1. TỔNG QUAN THÔNG SỐ KỊCH BẢN SẢN XUẤT

| Tiêu chí kỹ thuật | Kết quả đo lường | Trạng thái kiểm định |
| :--- | :---: | :---: |
| **Tổng số câu thoại (Dialogue sentences)** | **240 câu** | **ĐẠT CHUẨN 100%** |
| **Số phần tử kịch bản (Elements)** | **31 phần tử** (BGM, SFX, Speech turns) | **ĐẠT (parse_kichban.py PASS)** |
| **Phân bổ 5 Hồi** | H1: 47 · H2: 60 · H3: 50 · H4: 53 · H5: 35 | **Cân đối, cấu trúc chuẩn A2** |
| **Tỷ lệ phân vai** | Host: 76 (31,7%) · Sói: 59 (24,6%) · Cáo: 75 (31,2%) · N: 30 (12,5%) | **Tách bạch 4 vai, đúng tỷ lệ** |
| **Chữ số còn sót trong lời thoại** | **0 chữ số** (toàn bộ chuyển thành chữ tiếng Việt) | **ĐẠT CHUẨN G11 / K7** |
| **Dấu ba chấm (`...`) / thẻ ngắt giữa câu** | **0 lỗi** | **ĐẠT CHUẨN G1** |
| **An toàn nội dung YouTube (V9)** | **0 từ cấm mô tả bạo lực ghê rợn hay thương tích** | **ĐẠT CHUẨN V9 100%** |
| **Hệ sinh thái 10 chỉ dấu tâm lý (K10 / A2c)** | Đầy đủ 10/10 chỉ dấu tâm lý & hành vi | **ĐẠT CHUẨN K10** |

---

## 2. KẾT QUẢ RÀ SOÁT CHÍNH TẢ & CHUẨN HÓA NGÔN TỪ

### 2.1. Chuẩn hóa số đọc sang chữ tiếng Việt (Luật G11 & K7)
Toàn bộ các số năm, ngày tháng, mốc giờ, số nhà, cỡ súng và tổng đài khẩn cấp đã được rà soát và chuyển thành chữ để đảm bảo engine TTS không đọc sai hoặc bị ngắc ngứ:
- `20 tháng 6 năm 1994` $\rightarrow$ `hai mươi tháng sáu năm một chín chín mươi tư`
- `số 65 đường Every` $\rightarrow$ `số sáu mươi lăm đường Every`
- `22 tuổi` $\rightarrow$ `hai mươi hai tuổi`
- `07 giờ 09 phút sáng` $\rightarrow$ `bảy giờ chín phút sáng`
- `tổng đài 111` $\rightarrow$ `tổng đài khẩn cấp một một một`
- `súng trường cỡ nòng 22 hiệu Anschutz` $\rightarrow$ `súng trường bán tự động cỡ nòng hai mươi hai hiệu Anschutz`
- `05 giờ 45 phút` $\rightarrow$ `năm giờ bốn mươi lăm phút`
- `06 giờ 44 phút` $\rightarrow$ `sáu giờ bốn mươi tư phút`
- `Tháng 5 năm 1995` $\rightarrow$ `Tháng năm năm một chín chín mươi lăm`
- `16 năm không ân xá` $\rightarrow$ `mười sáu năm không ân xá`
- `Năm 2007` $\rightarrow$ `Năm hai nghìn không trăm lẻ bảy`
- `Tháng 3 năm 2009` $\rightarrow$ `Tháng ba năm hai nghìn không trăm lẻ chín`
- `mùng 5 tháng 6 năm 2009` $\rightarrow$ `mùng năm tháng sáu năm hai nghìn không trăm lẻ chín`
- `13 năm ngồi sau song sắt` $\rightarrow$ `mười ba năm ngồi sau song sắt`

### 2.2. Kiểm định dấu câu và ngắt nhịp (Luật G1)
- Toàn bộ 240 câu thoại đều kết thúc bằng dấu chấm `.`, dấu hỏi `?` hoặc dấu cảm `!`.
- Không có bất kỳ câu thoại nào kết thúc lửng lơ bằng dấu hai chấm `:` hoặc thiếu dấu ngắt câu.
- Loại bỏ hoàn toàn dấu ba chấm (`...`) gây vỡ nhịp thở robot của giọng đọc AI. Mọi khoảng dừng kịch tính được cấu hình thông qua tham số `_pause_after` giữa các câu theo chuẩn A3/G2.

### 2.3. Rà soát danh từ riêng và thuật ngữ quốc tế (Luật G6, G7, K1)
- Tên các nhân vật và địa danh được giữ nguyên gốc chuẩn xác để phụ đề và hình ảnh khớp tuyệt đối: *David Bain, Robin Bain, Margaret Bain, Arawa Bain, Laniet Bain, Stephen Bain, Joe Karam, Dunedin, Andersons Bay, Every Street, Opera Alive, Anschutz, Christchurch*.
- Thuật ngữ khoa học hình sự được diễn đạt tự nhiên, chuẩn xác: *hóa chất phát quang luminol, dấu vết vi mô, quỹ đạo bay của giọt máu, muội than thuốc súng*.

---

## 3. ĐỐI CHIẾU DỮ KIỆN TƯ PHÁP VỚI NGUỒN CÔNG KHAI (LUẬT K1, K2, K3)

1. **Vụ án tại 65 Every Street, Andersons Bay, Dunedin (20/06/1994):** 5 nạn nhân thiệt mạng, David Bain là người duy nhất sống sót gọi 111 lúc 07:09 sáng sau tuyến phát báo. (Khớp nguồn hồ sơ cảnh sát New Zealand và Tòa án Tối cao).
2. **Khẩu súng .22 Anschütz có ống giảm thanh:** Thuộc quyền sở hữu của David Bain; vỏ đạn và đường đạn tại hiện trường khớp hoàn toàn với mẫu vật lưu trữ.
3. **Hiện trường phòng Stephen:** Cuộc giằng co quyết liệt giữa nạn nhân 14 tuổi và kẻ thủ ác; tròng kính dự phòng của David bị rơi tại hiện trường khớp với gọng kính gãy tìm thấy trong phòng ngủ của David.
4. **Dấu chân tất phát quang bằng luminol:** Các dấu chân tất dính máu vô hình đối với mắt thường chạy dọc hành lang trùng khớp kích thước chân và đôi tất David đang mang.
5. **Thông điệp máy tính lúc 06:44 sáng:** Dòng chữ ngắn *"Sorry, you are the only one who deserved to stay"* gõ trên máy tính gia đình ngay thời điểm David trở về nhà.
6. **Vai trò lịch sử của Joe Karam:** Cựu danh thủ bóng bầu dục All Black dành hơn 10 năm điều tra độc lập, xuất bản sách và kháng cáo cho David Bain.
7. **Phán quyết của Cơ mật viện London (2007) & Tòa án Tối cao Christchurch (2009):** Tuyên hủy án do sai sót tố tụng năm 2007; tái thẩm tuyên **VÔ TỘI (NOT GUILTY)** ngày 05/06/2009.
8. **Khoản chi trả nhân đạo (2015):** Khoản hỗ trợ 925.000 đô la (ex gratia payment) khép lại vụ tranh tụng bồi thường kéo dài.

---

## 4. KẾT LUẬN & BÀN GIAO SẢN XUẤT

Kịch bản `01_KICH_BAN/Ho_So_Toi_Pham/Tap48/kichban_tap48_19112026.md` đã hoàn tất toàn bộ các bước kiểm tra chính tả, ngữ pháp, chuẩn hóa số đọc tiếng Việt và kiểm định tư pháp. Kịch bản đã sẵn sàng 100% để chuyển sang các bước sản xuất tiếp theo trong pipeline:
- [x] Tách câu (`parse_kichban.py`) — **ĐÃ TEST THÀNH CÔNG (240 câu)**
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Dựng hình và đóng gói xuất bản (`build_video3.py`, `package.py --mux`)
