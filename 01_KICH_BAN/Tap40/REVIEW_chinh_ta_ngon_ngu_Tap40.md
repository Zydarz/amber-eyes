# BÁO CÁO REVIEW CHÍNH TẢ & NGÔN NGỮ TẬP 40 (3 THỨ TIẾNG: VN – EN – JA)

*Ngày kiểm tra: 20/11/2026.*  
*Đối tượng kiểm tra:*
1. Bản Tiếng Việt: `01_KICH_BAN/Tap40/kichban_tap40_19112026.md`
2. Bản Tiếng Anh: `01_KICH_BAN/Tap40_EN/kichban_tap40_EN.md`
3. Bản Tiếng Nhật: `01_KICH_BAN/Tap40_JA/kichban_tap40_JA.md`

---

## 1. TỔNG HỢP KẾT QUẢ KIỂM TRA CHÍNH TẢ & CẤU TRÚC

| Hạng mục kiểm tra | Bản Tiếng Việt (VN) | Bản Tiếng Anh (EN) | Bản Tiếng Nhật (JA) | Đánh giá |
|---|:---:|:---:|:---:|:---:|
| **Số phần tử (Elements)** | **52** | **52** | **52** | ✅ Khớp 100% |
| **Số câu thoại (Sentences)** | **227** | **227** | **227** | ✅ Khớp 1:1:1 tuyệt đối |
| **Tổng số dòng file** | **372 dòng** | **372 dòng** | **372 dòng** | ✅ Khớp 1:1 cấu trúc dòng |
| **Cân bằng dấu ngoặc đơn `( )`** | 0 lỗi lệch | 0 lỗi lệch | 0 lỗi lệch | ✅ ĐẠT |
| **Cân bằng dấu ngoặc kép `“ ”`** | 0 lỗi lệch | 0 lỗi lệch | 0 lỗi lệch | ✅ ĐẠT |
| **Cân bằng ngoặc vuông tiếng Nhật `「 」`** | Không áp dụng | Không áp dụng | 0 lỗi lệch | ✅ ĐẠT |
| **Dấu kết câu thoại cuối dòng** | 100% có dấu kết câu | 100% có dấu kết câu | 100% có dấu kết câu (`。`, `！`, `？`) | ✅ ĐẠT |
| **Từ lặp âm liên tiếp bất thường** | 0 lỗi (Đã khử "pháp Pháp") | 0 lỗi | 0 lỗi | ✅ ĐẠT |
| **Lỗi viết tắt gây ngắt câu sai** | 0 lỗi (Đã chuẩn hóa `Doctor`) | 0 lỗi | 0 lỗi | ✅ ĐẠT |
| **Từ cấm YouTube Safe (Quy tắc V9)** | 0 lỗi | 0 lỗi | 0 lỗi | ✅ ĐẠT |
| **Dấu ba chấm giữa câu (Quy tắc G1)** | 0 lỗi | 0 lỗi | 0 lỗi | ✅ ĐẠT |

---

## 2. CHI TIẾT HIỆU CHỈNH & TRAU CHUỐT NGÔN NGỮ

### 2.1. Bản Tiếng Việt (`kichban_tap40_19112026.md`)
1. **Khử lặp âm cận kề:**
   - Dòng 278 (câu 4.04#6): Đổi *"lịch sử tư pháp Pháp"* $\rightarrow$ *"lịch sử nền tư pháp nước Pháp"*, tránh lặp âm "pháp Pháp" khi máy TTS đọc.
   - Dòng 356 (câu 5.04#1): Đổi *"nền tư pháp Pháp"* $\rightarrow$ *"nền tư pháp nước Pháp"*, tạo ngữ điệu trang trọng và tự nhiên.
2. **Quy tắc V9 & K4 (An toàn YouTube 100%):** 
   - Kiểm tra toàn bộ danh mục từ cấm bạo lực ghê rợn: hoàn toàn không xuất hiện các mô tả thân xác rùng rợn.
   - Tập trung 100% vào phân tích tâm thần học pháp y: *Ái kỷ ác tính*, *Rối loạn nhân cách chống đối xã hội*, *Cơ chế chia ngăn tâm trí*, *Tội ác di dời hình mẫu người mẹ*, *Hối hận công cụ*, *Đàm phán con tin giải cứu bản thân*.
3. **Quy tắc G1:** Không có dấu ba chấm `...` hay `<#s#>` giữa câu; đảm bảo ngữ lưu đọc liền mạch, nhịp nhàng.

### 2.2. Bản Tiếng Anh (`kichban_tap40_EN.md`)
1. **Loại bỏ viết tắt gây ngắt câu sai:**
   - Chuẩn hóa `Dr. Daniel Zagury` thành `Doctor Daniel Zagury` để tránh tool `parse_kichban.py` tách nhầm dấu chấm sau chữ `Dr.` thành câu riêng, đảm bảo số câu khớp chính xác 227 câu.
2. **Ngữ pháp & Thuật ngữ học thuật Tội phạm học:**
   - Chuẩn hóa các thuật ngữ quốc tế chuyên sâu: *Malignant Narcissism*, *Antisocial Personality Disorder*, *Displaced Matricide*, *Extreme Cognitive Compartmentalization*, *Moral Disengagement*, *Dehumanization*, *Instrumental Regret*, *Tactical Compliance*, *Moral Panic*, *Cognitive Overload Collapse*, *Acute Moral Injury*.
   - Đảm bảo giọng điệu tài liệu điều tra trang trọng (*Narrator-led Documentary*), phân bổ câu từ cân đối cho diễn xuất TTS.

### 2.3. Bản Tiếng Nhật (`kichban_tap40_JA.md`)
1. **Chuẩn hóa ngắt câu theo quy tắc `ja_split`:**
   - Đảm bảo mỗi dòng thoại chứa đúng 1 dấu ngắt câu `。` ở cuối dòng, khử các dấu `。` nằm giữa dòng vốn dễ làm script tách câu thành nhiều câu nhỏ:
     - Câu N1 (1.07#3): Chuẩn hóa câu nói trực giác sinh tồn của Émilie Espès.
     - Câu Chuyên gia (2.06#11): Hợp nhất vế giải thích cơ chế ngắt kết nối lương tri.
     - Câu Chuyên gia (4.09#7 & 4.09#8): Nối mượt vế phân tích hai tầng hối hận của kẻ vu khống.
     - Câu Host (5.05#6): Nối thông điệp chào kết thúc video.
   - Kết quả: Đạt chính xác **227 câu thoại**, khớp 1:1:1 với bản Tiếng Việt và Tiếng Anh.
2. **Chính tả Kana, Kanji & Thuật ngữ tâm lý tiếng Nhật:**
   - Sử dụng chuẩn từ vựng khoa học hành vi của Nhật Bản: 認知的区画化 (Compartmentalization), 代理的母殺し (Displaced Matricide), 道具的後悔 (Instrumental Regret), 道徳的関与の遮断 (Moral Disengagement), 自己愛的な憤怒と崩壊 (Narcissistic Mortification and Rage), 戦術的服従 (Tactical Compliance), モラル・パニック (Moral Panic).

---

## 3. KẾT LUẬN & ĐỀ XUẤT BƯỚC TIẾP THEO

- Cả 3 bản kịch bản Tiếng Việt, Tiếng Anh và Tiếng Nhật của **Tập 40** đã hoàn toàn sạch lỗi chính tả, chuẩn mực về mặt văn phong học thuật tâm lý học tội phạm và đồng bộ tuyệt đối về mặt kỹ thuật (52 elements, 227 câu thoại, khớp nối 1:1:1).
- Đã xuất thành công 3 file parsed JSON: `.work/tap40_vn_parsed.json`, `.work/tap40_en_parsed.json`, `.work/tap40_ja_parsed.json`.
- Sẵn sàng chuyển sang Bước 3: Diễn xuất (`make_acting_tap40.py`) và Bước 4: Đọc giọng TTS theo đúng quy trình sản xuất của kênh Amber Eyes.
