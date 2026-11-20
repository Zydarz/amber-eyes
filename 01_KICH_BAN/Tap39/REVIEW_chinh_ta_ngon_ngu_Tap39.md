# BÁO CÁO REVIEW CHÍNH TẢ & NGÔN NGỮ TẬP 39 (3 THỨ TIẾNG: VN – EN – JA)

*Ngày kiểm tra: 20/11/2026.*  
*Đối tượng kiểm tra:*
1. Bản Tiếng Việt: `01_KICH_BAN/Tap39/kichban_tap39_19112026.md`
2. Bản Tiếng Anh: `01_KICH_BAN/Tap39_EN/kichban_tap39_EN.md`
3. Bản Tiếng Nhật: `01_KICH_BAN/Tap39_JA/kichban_tap39_JA.md`

---

## 1. TỔNG HỢP KẾT QUẢ KIỂM TRA CHÍNH TẢ & CẤU TRÚC

| Hạng mục kiểm tra | Bản Tiếng Việt (VN) | Bản Tiếng Anh (EN) | Bản Tiếng Nhật (JA) | Đánh giá |
|---|:---:|:---:|:---:|:---:|
| **Số phần tử (Elements)** | **52** | **52** | **52** | ✅ Khớp 100% |
| **Số câu thoại (Sentences)** | **240** | **240** | **240** | ✅ Khớp 100% |
| **Tổng số dòng file** | **383 dòng** | **383 dòng** | **383 dòng** | ✅ Khớp 1:1 dòng |
| **Cân bằng dấu ngoặc đơn `( )`** | 0 lỗi lệch | 0 lỗi lệch | 0 lỗi lệch | ✅ ĐẠT |
| **Cân bằng dấu ngoặc kép `“ ”`** | 0 lỗi lệch | 0 lỗi lệch | 0 lỗi lệch | ✅ ĐẠT |
| **Cân bằng ngoặc vuông tiếng Nhật `「 」`** | Không áp dụng | Không áp dụng | 0 lỗi lệch | ✅ ĐẠT |
| **Dấu kết câu thoại cuối dòng** | 100% có dấu kết câu | 100% có dấu kết câu | 100% có dấu kết câu (`。`, `！`, `？`) | ✅ ĐẠT |
| **Từ lặp liên tiếp bất thường** | 0 lỗi | 0 lỗi | 0 lỗi | ✅ ĐẠT |
| **Lỗi viết tắt gây ngắt câu sai** | 0 lỗi (Đã loại bỏ `Mr.`) | 0 lỗi | 0 lỗi | ✅ ĐẠT |
| **Từ cấm YouTube Safe (Quy tắc V9)** | 0 lỗi | 0 lỗi | 0 lỗi | ✅ ĐẠT |
| **Dấu ba chấm giữa câu (Quy tắc G1)** | 0 lỗi | 0 lỗi | 0 lỗi | ✅ ĐẠT |

---

## 2. CHI TIẾT HIỆU CHỈNH & TRAU CHUỐT NGÔN NGỮ

### 2.1. Bản Tiếng Việt (`kichban_tap39_19112026.md`)
1. **Tinh chỉnh từ trùng lặp lân cận:**
   - Dòng 71: Đổi *"Không lâu sau khi phát hiện hiện trường đầu tiên"* $\rightarrow$ *"Không lâu sau khi tìm thấy hiện trường đầu tiên"* (tránh lặp âm "hiện hiện").
   - Dòng 82: Đổi *"phi tang thi thể thể hiện một sự am hiểu"* $\rightarrow$ *"phi tang thi thể cho thấy một sự am hiểu"* (tránh lặp âm "thể thể").
2. **Quy tắc V9 & K4:** Rà soát và loại bỏ triệt để các từ ngữ nhạy cảm hoặc mô tả bạo lực ghê rợn; thay thế các từ cấm bằng thuật ngữ pháp y/hành vi học chuẩn xác ("tàn độc", "xung động hủy diệt", "tước đoạt sinh mạng").
3. **Quy tắc G1:** Đảm bảo 100% không có dấu ba chấm `...` hay `…` giữa câu, đảm bảo engine TTS đọc liền mạch tự nhiên không bị giật robot.

### 2.2. Bản Tiếng Anh (`kichban_tap39_EN.md`)
1. **Xử lý dấu chấm viết tắt:** Loại bỏ cách viết tắt danh xưng như `Mr.` (dễ khiến tool `parse_kichban.py` tách nhầm thành câu riêng); chuẩn hóa thành tên đầy đủ (`Robin Bereza`, `John Rogers`).
2. **Ngữ pháp & Thuật ngữ học thuật:**
   - Chuẩn hóa các thuật ngữ tội phạm học và tâm lý học hành vi: *Paraphilic Sadomasochism*, *Antisocial Personality Disorder*, *Gender Role Inversion in Predatory Violence*, *Coercive Control*, *Normalcy Bias*, *Escalating Fantasy Trajectory*, *Instrumental Remorse*.
   - Đảm bảo tính cân đối và văn phong tài liệu điều tra trang trọng (*Narrator-led Documentary*).

### 2.3. Bản Tiếng Nhật (`kichban_tap39_JA.md`)
1. **Dấu ngắt câu tiếng Nhật (`。`):** Chuẩn hóa câu văn để mỗi dòng thoại tương ứng chính xác với 1 câu kết thúc bằng `。`, không bị tách đôi ở giữa dòng, đảm bảo parity 240 câu khớp tuyệt đối với bản Tiếng Việt và Tiếng Anh.
2. **Chính tả Kana & Kanji:**
   - 0 ký tự half-width kana lỗi thời.
   - Sử dụng chuẩn ngữ pháp hành vi học Nhật Bản: 認知的区画化 (Compartmentalization), 強迫的コントロール (Coercive Control), 道具的後悔 (Instrumental Remorse), 捕食的暴力における性役割の逆転 (Gender Role Inversion in Predatory Violence).

---

## 3. KẾT LUẬN

Cả 3 bản kịch bản Tiếng Việt, Tiếng Anh và Tiếng Nhật của **Tập 39** đã hoàn toàn sạch lỗi chính tả, chuẩn hóa văn phong học thuật tội phạm học và đạt độ tương thích kỹ thuật 100% với hệ thống dựng phim tự động của kênh Amber Eyes.
