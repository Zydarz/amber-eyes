import sys, re

# Read TIEU_CHUAN_DUNG_VIDEO.md
tc_path = r'00_TIEU_CHUAN\TIEU_CHUAN_DUNG_VIDEO.md'
with open(tc_path, 'r', encoding='utf-8') as f:
    tc_text = f.read()

a2c_content = '''### A2c. Năm trụ cột tâm lý & chiều sâu kịch bản (The 5 Psychological Pillars)

Kênh **Amber eyes** định vị là *phân tích tâm lý tội phạm qua những hồ sơ có thật*, **không phải là bản tin thời sự hay phóng sự phá án thuần túy**. Một kịch bản chỉ kể tình tiết vụ án, quá trình điều tra và kết quả tuyên án là **CHƯA ĐẠT**. 

Mọi kịch bản (bản tiếng Việt gốc và các bản dịch ngôn ngữ EN/JA/KO) **BẮT BUỘC** phải làm sáng tỏ **5 trụ cột tâm lý** sau:

| Trụ cột | Bản chất & Chiều sâu cần khai thác | Vị trí khuyến nghị trong 5 hồi |
|---|---|---|
| **1. Ảnh hưởng xã hội & Sự quan tâm của dư luận** | - **Chấn thương tập thể & hoang tưởng xã hội (Collective Trauma & Paranoia):** Cảm giác an toàn bị phá vỡ; người dân hoảng loạn, mua súng, khóa cửa, nghi kỵ lẫn nhau.<br>- **Cơn sốt truyền thông (Media Frenzy):** Xã hội theo dõi, chia rẽ hoặc phẫn nộ tột cùng trước tội ác.<br>- **Khủng hoảng niềm tin & Cải cách thể chế (Institutional Betrayal & Reform):** Sự rạn nứt uy tín của quân đội, cảnh sát, cơ quan quản lý; những cải cách quy trình, điều luật hoặc tiền lệ tư pháp lịch sử sau vụ án. | **Hồi 1** (thiết lập tầm vóc và sức nặng vụ án) & **Hồi 5** (đúc kết di chứng xã hội). |
| **2. Góc nhìn của hung thủ về nạn nhân & Lý do** | - **Vật hóa & Phi nhân hóa (Objectification & Dehumanization):** Nạn nhân không được nhìn nhận như con người có tri giác và gia đình, mà bị giáng cấp thành "đạo cụ" (props), "dự án" (projects), hoặc "công cụ cung cấp sự thỏa mãn ái kỷ" (narcissistic supply).<br>- **Lý do gốc rễ (The Why):** Sự thiếu hụt thấu cảm cảm xúc (Affective Empathy Deficit), khuyết tật Thuyết tâm trí (Theory of Mind), ảo tưởng đặc quyền săn mồi (predatory entitlement). Tiếng khóc van xin không gây trắc ẩn mà kích hoạt sự hưng phấn quyền lực (power arousal). | **Hồi 2** (hành vi hiện trường) & **Hồi 3** (giải phẫu tâm lý). |
| **3. Góc nhìn của hung thủ về người thân & Nghịch lý chia ngăn** | - **Cơ chế Chia ngăn nhận thức (Compartmentalization):** Bộ não tội phạm hai mặt khóa chặt "ngăn gia đình bình thường" và "ngăn bóng tối săn mồi" thành hai thế giới riêng biệt không giao thoa.<br>- **Gia đình là "Lá chắn bình thường hóa" (Shield of Normalcy):** Dùng gia đình để tự thuyết phục mình vẫn là người tốt, hoặc coi người thân là tài sản danh dự cần bảo vệ quyền sở hữu.<br>- **Bi kịch của nạn nhân thứ hai:** Người thân (vợ, con, cha mẹ) bị sụp đổ toàn bộ danh tính khi sự thật bại lộ; nỗi sợ mất mặt trước người thân thường lớn hơn nỗi sợ tòa án. | **Hồi 3** (giải phẫu động cơ) & **Hồi 4** (sự sụp đổ phòng thẩm vấn khi đối diện gia đình). |
| **4. Thái độ của hung thủ trước bản án nhận được** | - **Hối hận giả tạo vs. Tự thương hại bệnh lý (False Remorse vs. Pathological Self-Pity):** Kẻ ái kỷ/thái nhân cách không khóc vì xót thương nạn nhân, mà khóc vì tiếc thương danh vọng, tự do và đặc quyền của chính mình đã tan vỡ (narcissistic collapse).<br>- **Phản ứng trước sự trừng phạt:** Có kẻ ngoan cố chối tội, coi mình là nạn nhân của tư pháp, thách thức đến phút chót; có kẻ tìm cách tự sát hoặc sụp đổ hoàn toàn khi mất quyền kiểm soát.<br>- **Bản án tâm lý:** Tòa án trừng phạt thể xác, nhưng bản án tâm lý phơi bày sự trơ tráo, trống rỗng tột cùng của nhân cách. | **Hồi 5** (Phán quyết & Lời kết). |
| **5. Hệ thống tự bào chữa & Cơ chế trung hòa đạo đức** | - **Kỹ thuật Trung hòa đạo đức (Techniques of Neutralization) & Ngắt kết nối đạo đức (Moral Disengagement):** Cách hung thủ tự lừa dối để vô hiệu hóa lương tri và ngủ ngon mỗi đêm:<br>  + *Đổ lỗi cho nạn nhân (Victim Blaming):* "Cô ta bất cẩn", "Cậu ta vốn muốn chết".<br>  + *Ngoại hóa trách nhiệm (Displacement of Responsibility):* "Do quỷ dữ/Factor X bên trong ép tôi", "Do cấp dưới làm".<br>  + *Giảm thiểu tổn hại (Minimization):* "Tôi chỉ xem trộm thôi", "Tôi chỉ giúp giải thoát".<br>  + *Tự khoác áo thiên thần (Hero Complex):* Đóng vai người mẹ tận tụy, người cứu rỗi.<br>  + *Cưỡng chế hoàn cảnh:* "Cô ta thấy mặt tôi rồi nên ép tôi phải ra tay để tự vệ". | **Hồi 3** (cơ chế nhận thức) & **Hồi 4** (lời khai bào chữa khi đối chất). |

#### Phân công vai thoại làm nổi bật 5 trụ cột
- **Host (Cú):** Nêu bật bối cảnh chấn động xã hội, sự quan tâm của công chúng, dẫn dắt các nghịch lý đạo đức và đúc kết bài học cảnh tỉnh xã hội ở đầu và cuối tập.
- **Điều tra viên (Sói):** Cung cấp các dữ kiện khách quan, hồ sơ thẩm vấn, phản ứng thực tế của hung thủ với người thân, thái độ trước búa tòa và những câu trích tự bào chữa nguyên văn.
- **Chuyên gia tâm lý (Cáo):** Bóc trần các cơ chế vô thức ẩn sâu: cơ chế chia ngăn (compartmentalization), vật hóa nạn nhân (objectification), ngắt kết nối đạo đức (moral disengagement) và sự sụp đổ của bản ngã ái kỷ.

#### Cổng kiểm kịch bản (Checklist trước khi duyệt)
Trước khi chuyển sang bước Diễn xuất (Bước 1b), biên kịch và AI **PHẢI** đối soát và trả lời được 5 câu hỏi:
1. [ ] Đã chỉ ra được vụ án gây chấn động, hoang tưởng hoặc thay đổi thể chế/luật pháp nào chưa?
2. [ ] Đã làm rõ hung thủ xem nạn nhân là gì và tại sao lại có góc nhìn đó chưa?
3. [ ] Đã làm rõ hung thủ nhìn nhận người thân ra sao và nghịch lý chia ngăn gia đình chưa?
4. [ ] Đã mô tả đúng thái độ thật của hung thủ trước bản án (hối hận hay tự thương hại/thách thức) chưa?
5. [ ] Đã bóc trần những lý lẽ tự bào chữa mà hung thủ dùng để lừa dối lương tri chưa?

'''

# Insert A2c before ## A3
marker_a3 = '## A3. Quy trình chuẩn — lệnh chạy và thời gian đo được'
assert marker_a3 in tc_text, "Marker A3 not found"
tc_text = tc_text.replace(marker_a3, a2c_content + marker_a3)

# Add item 118 to A11
a11_part = tc_text.split('## A11. Bẫy đã gặp — đừng lặp lại')[1].split('## A12')[0]
matches = re.findall(r'^\|\s*(\d+)\s*\|', a11_part, re.MULTILINE)
nums = [int(m) for m in matches]
max_num = max(nums)
next_num = max_num + 1
assert next_num == 118, f"Expected next_num 118, got {next_num}"

entry_118 = f'''| {next_num} | **Kịch bản sa đà vào nghiệp vụ phá án thuần túy, thiếu 5 trụ cột tâm lý và dư chấn xã hội** (Nhận xét người dùng 05/11/2026): video kể đủ tình tiết, pháp y và điều tra nhưng không làm sáng tỏ tác động xã hội, thế giới quan của hung thủ về nạn nhân/người thân, thái độ trước bản án và cơ chế tự bào chữa ⇒ video biến thành phóng sự phá án thông thường, mất bản sắc "giải phẫu tâm lý" của kênh | **Tuân thủ khung 5 trụ cột tâm lý (A2c) & cổng K10 (AGENTS.md)**: Đối soát 5 câu hỏi cốt lõi trước khi duyệt kịch bản: (1) chấn thương tập thể & cải cách thể chế; (2) vật hóa nạn nhân & lý do gốc rễ; (3) nghịch lý chia ngăn gia đình; (4) hối hận giả tạo vs tự thương hại bản thân; (5) kỹ thuật trung hòa đạo đức (neutralization). Phân vai rõ: Host dẫn dắt dư chấn xã hội/triết lý; Điều tra viên cung cấp dữ kiện/lời khai tự bào chữa; Chuyên gia tâm lý mổ xẻ cơ chế vô thức |\n'''

# Insert entry_118 right before \n## A12. Cấu hình tập mới
marker_a12 = '## A12. Cấu hình tập mới — một mục trong `.work/edition.py`'
assert marker_a12 in tc_text, "Marker A12 not found"
tc_text = tc_text.replace(marker_a12, entry_118 + '\n' + marker_a12)

# Validate A11 after insertion
a11_part_after = tc_text.split('## A11. Bẫy đã gặp — đừng lặp lại')[1].split('## A12')[0]
matches_after = re.findall(r'^\|\s*(\d+)\s*\|', a11_part_after, re.MULTILINE)
nums_after = [int(m) for m in matches_after]
assert nums_after == list(range(1, 119)), f"Validation failed! nums_after: {nums_after}"
print("A11 validation passed: 1..118 consecutive, 0 duplicates.")

with open(tc_path, 'w', encoding='utf-8') as f:
    f.write(tc_text)
print("Updated 00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md successfully.")
