import sys

with open('01_KICH_BAN/Tap04/REVIEW_kichban_tap04.md', 'r', encoding='utf-8') as f:
    content = f.read()

target = "- ⚠ `script_tap04.json`, `acting_tap04.json`, audio, bảng shot đều CŨ. Bản `kichban_tap04_EN.md` chưa sửa."

replacement = """- ⚠ `script_tap04.json`, `acting_tap04.json`, audio, bảng shot đều CŨ.

## Đồng bộ và đối chiếu kịch bản Tiếng Việt — Tiếng Anh (31/10/2026)
Sao lưu: `.work/_cu/tap04_truoc_dongbo_en_vn_20261031/`
1. **Phát hiện & sửa lỗi logic nội bộ (K8) trong bản tiếng Việt:**
   - Tại `5.02#4`: Bản vá trước viết *"tòa án quận Lehigh, bang Pennsylvania, tuyên thêm 6 bản án chung thân, nâng tổng số lên 18"* → vi phạm K8 (11 án NJ + 6 án PA = 17 ≠ 18).
   - Đã sửa thành: *"Ít ngày sau, các tòa án tại bang Pennsylvania tuyên thêm 7 bản án chung thân, nâng tổng số lên 18."* (chính xác theo lịch sử: 6 án tại Lehigh và 1 án tại Northampton, tổng 11 + 7 = 18).
2. **Đồng bộ toàn diện bản tiếng Anh (`kichban_tap04_EN.md`):**
   - Đã cập nhật và đồng bộ cả 2 đường dẫn: `01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md` và `01_KICH_BAN/Tap04/kichban_tap04_EN.md` (cùng hash SHA256).
   - Loại bỏ toàn bộ các chi tiết cũ chưa kiểm chứng / hư cấu từ phim ảnh ở bản EN:
     * `1.05#3` & `1.07#3`: Loại bỏ chi tiết hư cấu lén lấy thuốc giảm đau của N1; dẫn lời N1 theo đúng chuẩn K3 ("imagine the perspective").
     * `1.08#3`: Bỏ chi tiết không nguồn linh mục Gall "sắp xuất viện".
     * `1.10#3`: Bỏ mô tả cách thức truyền thuốc liều cao (K4).
     * `1.14#5` & `#6`: Chuẩn hóa số nạn nhân: tự nhận 40, tòa xác nhận 29, ước tính có thể hàng trăm (bỏ con số ước đoán 300-400).
     * `2.02#3`: Bỏ liệt kê tên thuốc cụ thể (K4).
     * `2.06`: Rút từ 11 câu xuống 8 câu, loại bỏ quy trình từng bước lách máy Pyxis và bơm thuốc vào túi dịch (K4); sửa mâu thuẫn logic: máy vẫn lưu lệnh hủy và nhật ký tra cứu (K8).
     * `2.08#2` & `#6`: Chuẩn hóa kết quả xét nghiệm (bỏ "blood work" per V9) và bổ sung nạn nhân 38 tuổi Chris Hardgrove.
     * `2.11#4` & `#7`: Nêu rõ tên cụ bà Helen Dean (91 tuổi); sửa St. Luke thỏa thuận tự nguyện thôi việc thay vì sa thải.
     * `3.02#3`: Chuyển lời trích dẫn không nguồn của Cullen thành lời gián tiếp (K2).
     * `3.04`: Rút từ 6 câu xuống 5 câu, bỏ chi tiết bị bắt nạt/tự hại lúc 9 tuổi và bệnh viện tự hỏa táng mẹ (cần nguồn).
     * `3.07#4`: Bỏ nhắc ống tiêm (K4).
     * `3.09#6`: Bổ sung tên nạn nhân sinh viên Michael Strenko (21 tuổi).
     * `4.04`: Rút từ 6 câu xuống 5 câu, bỏ quy trình Vecuronium (K4) và câu trích cảm thán hư cấu của Amy (K2).
     * `4.06`: Rút từ 5 câu xuống 4 câu, bỏ các câu thoại hư cấu mang màu sắc kịch bản phim của N2.
     * `4.08` & `4.11`: Bắt giữ tại nhà hàng ở Bridgewater ngày 12/12/2003, bỏ cảnh rượt đuổi; bỏ "tim đập" (V9).
     * `4.12`: Rút từ 10 câu xuống 8 câu, bỏ cảnh phòng thẩm vấn hư cấu (áo len, nắm tay, 4 câu trích dẫn từ phim The Good Nurse); giữ lại diễn biến cốt lõi: Amy thuyết phục Cullen như một người bạn cũ và Cullen khai nhận.
     * `5.02#4`: 11 án chung thân tại NJ + 7 án tại PA = 18 án chung thân liên tiếp (397 năm tù không ân xá).
     * `5.04#2` & `#5`: Thể chế phớt lờ người lên tiếng; Đạo luật Cullen bắt buộc báo cáo và bảo vệ bệnh viện khi thông tin trung thực.
     * `5.08#3` & `#6`: "có thể đã cướp đi" và bỏ dấu "..." giữa câu (G1).
3. **Kết quả kiểm định tự động (Automated QC):**
   - Cả 2 bản đều đạt **61 phần tử** · **154 câu** khớp nhau 1-to-1 (`Sentence count mismatch: 0`).
   - Kiểm tra V9 / A9.2 (từ cấm): **0 lỗi** trên cả VN và EN.
   - Kiểm tra G1 (dấu "..." giữa câu): **0 lỗi**.
   - Kiểm tra cân bằng ngoặc kép / đơn: **0 lỗi** (`Unbalanced quote hits: 0`)."""

if target in content:
    new_content = content.replace(target, replacement)
    with open('01_KICH_BAN/Tap04/REVIEW_kichban_tap04.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated REVIEW_kichban_tap04.md successfully!")
else:
    print("Target not found!")
