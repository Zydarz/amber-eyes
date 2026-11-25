# BÁO CÁO REVIEW CHÍNH TẢ & NGÔN NGỮ TẬP 51 (BẢN SẢN XUẤT)

*Ngày lập: 24/11/2026.*  
*Đối tượng kiểm tra:* `01_KICH_BAN/Ho_So_Toi_Pham/Tap51/kichban_tap51_22112026.md`  
*Quy chuẩn đối chiếu:* `AGENTS.md` (Luật K1–K10, G1–G13, V1–V9) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Mục A2, A2c, A9.2).

---

## 1. TỔNG HỢP KẾT QUẢ KIỂM TRA KỸ THUẬT & CHÍNH TẢ

| Hạng mục kiểm tra | Tiêu chuẩn kỹ thuật | Đo lường thực tế | Kết luận |
|---|---|:---:|:---:|
| **Tổng số phần tử (Elements)** | Cấu trúc 5 Hồi chuẩn A2 / Tập 10 / Tập 50 | **52 Elements** | ✅ ĐẠT |
| **Lượt lời thoại (LOI)** | 36 lượt phân vai chuẩn podcast H-D-C-N | **36 Lượt** | ✅ ĐẠT |
| **Tổng số câu thoại (Sentences)** | Đảm bảo đúng 240 câu theo yêu cầu | **240 Câu** | ✅ ĐẠT |
| **Độ an toàn YouTube (Rule V9)** | 0 từ cấm A9.2 (máu, thi thể, sát hại, đập, trói...) | **0 Lỗi vi phạm** | ✅ ĐẠT |
| **Quy tắc đọc liền mạch (Rule G1)** | 0 dấu ba chấm `...` hay `…` giữa câu | **0 Lỗi vi phạm** | ✅ ĐẠT |
| **Cân bằng dấu ngoặc đơn `( )`** | Khớp 1:1, không mở ngoặc sót | **100% Khớp** | ✅ ĐẠT |
| **Cân bằng dấu ngoặc vuông `[ ]`** | Khớp các thẻ BGM/SFX/NGHI | **100% Khớp** | ✅ ĐẠT |
| **Cân bằng dấu trích dẫn `“ ”`** | Khớp cặp mở/đóng toàn kịch bản | **100% Khớp** | ✅ ĐẠT |
| **Ký tự ngoại lai (Chữ Hán / rác encode)** | Không tồn tại ký tự lạ ngoài bảng chữ cái tiếng Việt | **0 Lỗi** (Đã khử sạch chữ Hán sót) | ✅ ĐẠT |
| **Từ lặp bất thường lân cận** | Không lặp âm vấp váp gây khó cho engine TTS | **Đã xử lý sạch** | ✅ ĐẠT |

---

## 2. CHI TIẾT HIỆU CHỈNH & TRAU CHUỐT NGÔN TỪ

1. **Chuẩn hóa an toàn YouTube (Rule V9 / A9.2):**
   - Đã rà soát và thay thế toàn bộ các từ ngữ có thể kích hoạt thuật toán hạn chế quảng cáo:
     * *"sát nhân máu lạnh"* $\rightarrow$ *"tội phạm nguy hiểm"*.
     * *"bảo quản thi thể bằng"* $\rightarrow$ *"phong tỏa căn phòng bằng"*.
     * *"sát hại mẹ ruột"* $\rightarrow$ *"tước đoạt sinh mạng mẹ ruột"*.
     * *"đập tan hoàn toàn"* $\rightarrow$ *"bác bỏ hoàn toàn"*.
   - Đảm bảo lời văn mang tính học thuật phân tích tâm lý tội phạm và khoa học pháp y khách quan.

2. **Khử ký tự Hán và lỗi gõ phím:**
   - Phát hiện và sửa lỗi ký tự Hán lẫn trong văn bản: *"lừa đảo親 nhân"* $\rightarrow$ *"lừa đảo người thân"*.
   - Khắc phục các cụm từ lặp âm: *"tuyệt đối, đối tượng"* $\rightarrow$ *"tuyệt đối, kẻ thủ ác"*; *"tình yêu thương thương cảm"* $\rightarrow$ *"tình yêu thương sâu sắc"*.

3. **Chuẩn hóa chữ viết cho giọng đọc (Rule G11 & K7):**
   - Chuẩn hóa cách viết chữ thường cho tên tháng trong ngữ cảnh thời gian tiếng Việt (*"tháng bảy"*, *"tháng hai"*, *"tháng tư"*, *"tháng tám"*, *"tháng mười hai"*, *"tháng một"*, *"tháng năm năm 2023"* thay vì viết hoa tùy tiện).
   - Số tiền, số ngày, mốc thời gian đều được viết bằng chữ hoặc số chuẩn mực để pipeline `tts_sentences.py` tự động chuyển đổi phiên âm mượt mà.

4. **Chuẩn hóa chỉ dẫn diễn xuất (Stage Directions):**
   - Loại bỏ các nhãn chỉ dẫn mang tính sao chép từ tập khác (như *"bóc tách tâm lý đồng phạm Gary Stretch"*, *"phác họa sự đảo ngược vai trò giới"*, *"Hereford"*).
   - Thay thế bằng các nhãn chỉ dẫn chuẩn xác 100% với hồ sơ Ngô Tạ Vũ:
     * `HOST *(phân tích sự phân liệt nhân cách của Ngô Tạ Vũ)*:`
     * `HOST *(phân tích áp lực tâm lý học đường)*:`
     * `CHUYÊN GIA TÂM LÝ *(phân tích cơ chế ái kỷ bệnh lý và ảo tưởng cứu rỗi)*:`
     * `CHUYÊN GIA TÂM LÝ *(giải phẫu sự tha hóa nhân cách và phản ứng bù trừ cực đoan)*:`
     * `CHUYÊN GIA TÂM LÝ *(bóc tách cơ chế chia ngăn nhận thức và sự sụp đổ phòng vệ)*:`
     * `HOST *(vạch trần thủ đoạn lừa đảo thân nhân)*:`

---

## 3. KẾT LUẬN

Kịch bản sản xuất Tập 51 (`kichban_tap51_22112026.md`) đã hoàn toàn sạch lỗi chính tả, đạt chuẩn an toàn quảng cáo YouTube (V9), cấu trúc 240 câu thoại tuyệt đối chuẩn mực và sẵn sàng đưa vào các bước sản xuất âm thanh, diễn xuất (TTS) và dựng video tiếp theo.
