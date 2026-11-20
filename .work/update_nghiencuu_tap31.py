# -*- coding: utf-8 -*-
with open('01_KICH_BAN/Tap31/NghienCuu_TamLy_BoSung_KichBan_Tap31.md', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('140 câu thoại', '210 câu thoại')
text = text.replace('240 câu thoại', '210 câu thoại')

historical_additions = """
### 1.3. CÁC CỨ LIỆU LỊCH SỬ THỰC TẾ BỔ SUNG TỪ INTERNET & HỒ SƠ TƯ PHÁP
1. **Thí nghiệm tâm lý của Giáo sư Henry Murray tại Harvard (1959–1962):**
   - Henry Murray (cựu lãnh đạo thẩm tra tâm lý của OSS - tiền thân CIA) điều hành dự án nghiên cứu giới hạn chịu đựng tâm lý, nhận tài trợ liên quan đến các chương trình nghiên cứu hành vi Chiến tranh Lạnh (MKUltra-adjacent).
   - Chàng sinh viên 16 tuổi Ted Kaczynski đã trải qua hơn 200 giờ chịu đựng các buổi thẩm vấn áp bức tâm lý cực độ: bị gắn điện cực đo phản ứng sinh lý và bị thẩm vấn viên miệt thị, xé nát các tiểu luận triết học cá nhân dưới ánh đèn chói lóa.
2. **Nạn nhân Percy Wood & Vụ chuyến bay United Airlines 444:**
   - Tháng 11/1979: Chuyến bay United Airlines 444 mang 80 hành khách thoát chết trong gang tấc khi cơ chế kích nổ đo khí áp bị lỗi kỹ thuật.
   - Ngày 10/6/1980: Percy Wood (Chủ tịch kiêm Giám đốc điều hành United Airlines) bị thương nặng khi mở gói bưu kiện ngụy trang dưới dạng cuốn tiểu thuyết *Ice Brothers* của Sloan Wilson.
3. **Nạn nhân tử vong Hugh Scrutton (1985) & Vụ nổ Salt Lake City (1987):**
   - Ngày 11/12/1985: Hugh Scrutton (chủ tiệm cho thuê máy tính RenTech tại Sacramento, California) trở thành nạn nhân tử vong đầu tiên khi nhặt bưu kiện gỗ chứa đầy mảnh kim loại ở bãi đỗ xe phía sau.
   - Ngày 20/2/1987 tại Salt Lake City: Gary Wright (chủ tiệm máy tính) bị trọng thương sau khi chạm vào bẫy nổ tại bãi đỗ xe; đây là hiện trường duy nhất có nhân chứng nhìn thấy gã đàn ông mặc áo nỉ trùm đầu và đeo kính râm phi công, dẫn đến bức phác thảo truy nã huyền thoại của FBI.
4. **Hai vụ sát hại đẫm máu thập niên 1990:**
   - Ngày 10/12/1994: Thomas Mosser (chuyên gia quảng cáo Burson-Marsteller) bị sát hại ngay tại nhà bếp trước mặt vợ con. Lời trần tình đanh thép của bà Susan Mosser tại tòa đã vạch trần sự hèn nhát của kẻ thủ ác.
   - Ngày 24/4/1995: Gilbert Murray (Chủ tịch Hiệp hội Lâm nghiệp California) thiệt mạng khi mở kiện hàng tại văn phòng.
5. **Chữ ký ngôn ngữ học pháp y "You can't eat your cake and have it too":**
   - Đặc vụ FBI James R Fitzgerald phát hiện câu tục ngữ đảo ngữ cổ xưa từ thế kỷ 16 trong bản Tuyên ngôn 35.000 từ, đối chiếu khớp 100% với các bức thư lưu trữ thập niên 1970 của Ted trên gác xép tại Schenectady, New York do người em trai David Kaczynski cung cấp.
6. **Tình bạn hàn gắn vĩ đại giữa David Kaczynski và nạn nhân Gary Wright:**
   - Sau bản án, David trao phần lớn tiền thưởng 1 triệu USD cho các nạn nhân; nạn nhân Gary Wright đã chủ động tìm đến ôm David và cả hai trở thành những người anh em thân thiết cùng đi diễn thuyết về sự tha thứ và chữa lành vết thương khắp nước Mỹ.
"""

if '### 1.3. CÁC CỨ LIỆU LỊCH SỬ THỰC TẾ' not in text:
    text = text.replace('---', '---\n' + historical_additions + '\n---', 1)

with open('01_KICH_BAN/Tap31/NghienCuu_TamLy_BoSung_KichBan_Tap31.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated NghienCuu Tap 31 successfully.')
