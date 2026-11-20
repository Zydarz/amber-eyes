# BÁO CÁO REVIEW CHÍNH TẢ, NGÔN NGỮ & ĐỒNG BỘ KỊCH BẢN TẬP 32
## HỒ SƠ TED BUNDY (3 NGÔN NGỮ: TIẾNG VIỆT, TIẾNG ANH, TIẾNG NHẬT)

*Thời gian thực hiện:* 20/11/2026  
*Phạm vi kiểm tra:* Toàn bộ 238 câu thoại, 32 lượt thoại (LOI), 48 elements trên 3 bản kịch bản sản xuất.

---

### 1. BẢNG TỔNG HỢP KIỂM TRA CHÍNH TẢ & ĐỊNH DẠNG (LỖI ĐÃ KHẮC PHỤC)

| Ngôn ngữ | Vấn đề phát hiện | Giải pháp xử lý | Kết quả kiểm định |
| :--- | :--- | :--- | :---: |
| **Tiếng Việt (VN)** | - Xuất hiện dấu ngoặc kép cong `“` bị mất ở đầu dòng câu 2.08#6 do hàm strip của parser.<br>- Rà soát các từ dễ nhầm lẫn chính tả (*dằn vặt*, *ngụy tạo*, *xung động*, *chia ngăn*). | - Viết lại thành cấu trúc chuẩn: *"Chính hiệu ứng hào quang đã một lần nữa làm mờ mắt các nhà điều tra giàu kinh nghiệm nhất."*<br>- Kiểm tra 100% ngữ pháp, văn phong podcast tài liệu điều tra trang trọng. | **100% CLEAN (0 lỗi)** |
| **Tiếng Anh (EN)** | - Dấu nháy đơn mở/đóng `‘…’` trong trích dẫn lời Thẩm phán Cowart và từ `‘polite’` gây nhiễu nhận diện dấu sở hữu cách `’s`.<br>- Tách câu do viết tắt `Dr.` | - Chuyển sang dấu ngoặc kép chuẩn `“…”` theo quy chuẩn quốc tế.<br>- Viết thành `Doctor Robert Hare`, `Doctor Al Carlisle`, `Doctor Dorothy Lewis` để parser tách câu chuẩn xác. | **100% CLEAN (0 lỗi)** |
| **Tiếng Nhật (JA)** | - Sót từ mượn tiếng Anh `disguise` ở Hồi 3.<br>- Dấu ngắt câu `。` trong lời trích dẫn dài gây lệch số câu so với bản VN/EN. | - Thay thế `disguise` bằng từ thuần Nhật chuẩn xác: `偽装` (ngụy trang).<br>- Đồng bộ cấu trúc dấu câu tiếng Nhật để đảm bảo khớp 100% từng câu thoại với bản gốc. | **100% CLEAN (0 lỗi)** |

---

### 2. BẢNG ĐỐI CHIẾU SỐ ĐO KỸ THUẬT CUỐI CÙNG

- **Tiếng Việt (VN):** 48 elements | 32 lượt thoại | **CHÍNH XÁC 238 CÂU THOẠI**
- **Tiếng Anh (EN):** 48 elements | 32 lượt thoại | **CHÍNH XÁC 238 CÂU THOẠI**
- **Tiếng Nhật (JA):** 48 elements | 32 lượt thoại | **CHÍNH XÁC 238 CÂU THOẠI**
- **Khớp nối xuyên ngôn ngữ:** **Khớp chính xác 100% từng câu thoại và từng Turn (PERFECT 100% MATCH).**

---

### 3. ĐƯỜNG DẪN TỆP ĐÃ HIỆU CHỈNH HOÀN CHỈNH

- Bản Tiếng Việt: [kichban_tap32_19112026.md](file:///d:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap32/kichban_tap32_19112026.md)
- Bản Tiếng Anh: [kichban_tap32_EN.md](file:///d:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap32_EN/kichban_tap32_EN.md)
- Bản Tiếng Nhật: [kichban_tap32_JA.md](file:///d:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap32_JA/kichban_tap32_JA.md)
