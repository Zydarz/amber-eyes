import sys, re

# Paths
tc_path = r'00_TIEU_CHUAN\TIEU_CHUAN_DUNG_VIDEO.md'
agents_path = r'AGENTS.md'

with open(tc_path, 'r', encoding='utf-8') as f:
    tc_text = f.read()

# Define the full 10-dimension A2c text
a2c_full = '''### A2c. Hệ sinh thái phân tích tâm lý tội phạm — Bộ 10 chỉ dấu chiều sâu kịch bản

Kênh **Amber eyes** định vị là *phân tích tâm lý tội phạm qua những hồ sơ có thật*, **tuyệt đối không phải là bản tin thời sự, phóng sự điều tra hay bản tóm tắt pháp đình thuần túy**. Một kịch bản chỉ kể diễn biến vụ án, quá trình khám nghiệm và kết quả tuyên án là **CHƯA ĐẠT**.

Mọi kịch bản (bản tiếng Việt gốc và các bản dịch ngôn ngữ EN/JA/KO) **BẮT BUỘC** phải vận dụng **Hệ sinh thái 10 chỉ dấu tâm lý & hành vi** được chia thành 2 nhóm:
- **Nhóm I: 5 Trụ cột tâm lý cốt lõi** (Định vị chiều sâu nhân văn, đạo đức và tác động xã hội).
- **Nhóm II: 5 Yếu tố khoa học hành vi bổ trợ** (Giải mã cơ chế phát triển tội ác, dấu ấn tâm thần học và giá trị thức tỉnh thực tiễn).

---

#### 1. Nhóm I: 5 Trụ cột tâm lý cốt lõi

| # | Trụ cột | Bản chất & Chiều sâu cần khai thác | Vị trí khuyến nghị trong 5 hồi |
|---|---|---|---|
| 1 | **Ảnh hưởng xã hội & Sự quan tâm của dư luận** | - **Chấn thương tập thể & hoang tưởng xã hội (Collective Trauma & Paranoia):** Cảm giác an toàn bị phá vỡ; người dân hoảng loạn, mua súng, khóa cửa, nghi kỵ lẫn nhau.<br>- **Cơn sốt truyền thông (Media Frenzy):** Xã hội theo dõi, chia rẽ hoặc phẫn nộ tột cùng trước tội ác.<br>- **Khủng hoảng niềm tin & Cải cách thể chế (Institutional Betrayal & Reform):** Sự rạn nứt uy tín của quân đội, cảnh sát, cơ quan quản lý; những cải cách quy trình, điều luật hoặc tiền lệ tư pháp lịch sử sau vụ án. | **Hồi 1** (thiết lập tầm vóc và sức nặng vụ án) & **Hồi 5** (đúc kết di chứng xã hội). |
| 2 | **Góc nhìn của hung thủ về nạn nhân & Lý do** | - **Vật hóa & Phi nhân hóa (Objectification & Dehumanization):** Nạn nhân không được nhìn nhận như con người có tri giác và gia đình, mà bị giáng cấp thành "đạo cụ" (props), "dự án" (projects), hoặc "công cụ cung cấp sự thỏa mãn ái kỷ" (narcissistic supply).<br>- **Lý do gốc rễ (The Why):** Sự thiếu hụt thấu cảm cảm xúc (Affective Empathy Deficit), khuyết tật Thuyết tâm trí (Theory of Mind), ảo tưởng đặc quyền săn mồi (predatory entitlement). Tiếng khóc van xin không gây trắc ẩn mà kích hoạt sự hưng phấn quyền lực (power arousal). | **Hồi 2** (hành vi hiện trường) & **Hồi 3** (giải phẫu tâm lý). |
| 3 | **Góc nhìn của hung thủ về người thân & Nghịch lý chia ngăn** | - **Cơ chế Chia ngăn nhận thức (Compartmentalization):** Bộ não tội phạm hai mặt khóa chặt "ngăn gia đình bình thường" và "ngăn bóng tối săn mồi" thành hai thế giới riêng biệt không giao thoa.<br>- **Gia đình là "Lá chắn bình thường hóa" (Shield of Normalcy):** Dùng gia đình để tự thuyết phục mình vẫn là người tốt, hoặc coi người thân là tài sản danh dự cần bảo vệ quyền sở hữu.<br>- **Bi kịch của nạn nhân thứ hai:** Người thân (vợ, con, cha mẹ) bị sụp đổ toàn bộ danh tính khi sự thật bại lộ; nỗi sợ mất mặt trước người thân thường lớn hơn nỗi sợ tòa án. | **Hồi 3** (giải phẫu động cơ) & **Hồi 4** (sự sụp đổ phòng thẩm vấn khi đối diện gia đình). |
| 4 | **Thái độ của hung thủ trước bản án nhận được** | - **Hối hận giả tạo vs. Tự thương hại bệnh lý (False Remorse vs. Pathological Self-Pity):** Kẻ ái kỷ/thái nhân cách không khóc vì xót thương nạn nhân, mà khóc vì tiếc thương danh vọng, tự do và đặc quyền của chính mình đã tan vỡ (narcissistic collapse).<br>- **Phản ứng trước sự trừng phạt:** Có kẻ ngoan cố chối tội, coi mình là nạn nhân của tư pháp, thách thức đến phút chót; có kẻ tìm cách tự sát hoặc sụp đổ hoàn toàn khi mất quyền kiểm soát.<br>- **Bản án tâm lý:** Tòa án trừng phạt thể xác, nhưng bản án tâm lý phơi bày sự trơ tráo, trống rỗng tột cùng của nhân cách. | **Hồi 5** (Phán quyết & Lời kết). |
| 5 | **Hệ thống tự bào chữa & Cơ chế trung hòa đạo đức** | - **Kỹ thuật Trung hòa đạo đức (Techniques of Neutralization) & Ngắt kết nối đạo đức (Moral Disengagement):** Cách hung thủ tự lừa dối để vô hiệu hóa lương tri và ngủ ngon mỗi đêm:<br>  + *Đổ lỗi cho nạn nhân (Victim Blaming):* "Cô ta bất cẩn", "Cậu ta vốn muốn chết".<br>  + *Ngoại hóa trách nhiệm (Displacement of Responsibility):* "Do quỷ dữ/Factor X bên trong ép tôi", "Do cấp dưới làm".<br>  + *Giảm thiểu tổn hại (Minimization):* "Tôi chỉ xem trộm thôi", "Tôi chỉ giúp giải thoát".<br>  + *Tự khoác áo thiên thần (Hero Complex):* Đóng vai người mẹ tận tụy, người cứu rỗi.<br>  + *Cưỡng chế hoàn cảnh:* "Cô ta thấy mặt tôi rồi nên ép tôi phải ra tay để tự vệ". | **Hồi 3** (cơ chế nhận thức) & **Hồi 4** (lời khai bào chữa khi đối chất). |

---

#### 2. Nhóm II: 5 Yếu tố khoa học hành vi bổ trợ

| # | Yếu tố hành vi | Bản chất & Chiều sâu cần khai thác | Vị trí khuyến nghị trong 5 hồi |
|---|---|---|---|
| 6 | **Ngòi nổ & Điểm gãy tâm lý (Precipitating Stressor & Tipping Point)** | - **Biến cố kích hoạt (Trigger):** Vì sao tội ác bùng phát vào đúng thời điểm đó? Giọt nước nào làm tràn ly?<br>- Khủng hoảng sự nghiệp, đổ vỡ tình cảm, mất quyền kiểm soát, sự sỉ nhục cái tôi, hoặc áp lực thăng tiến vượt ngưỡng chịu đựng đã đánh sập cơ chế ức chế hành vi. | **Hồi 1** (bối cảnh dẫn nhập) & **Hồi 2** (mốc bắt đầu chuỗi hành vi). |
| 7 | **Dấu ấn tâm lý ("Chữ ký") vs. Thủ đoạn gây án (Signature vs. Modus Operandi)** | - **Thủ đoạn (Modus Operandi - MO):** Cách thức hung thủ làm để gây án và tẩu thoát (găng tay, chọn ban đêm, cắt liên lạc); MO liên tục thay đổi và tiến hóa theo kinh nghiệm.<br>- **Chữ ký tâm lý (Signature):** Hành vi không nhằm phục vụ mục đích trốn thoát, mà để thỏa mãn nhu cầu cảm xúc bệnh lý (chụp ảnh chiến lợi phẩm, các nút thắt dây trói kỳ quặc, trang phục, gửi thư trêu ngươi). Signature là "vân tay linh hồn", không bao giờ thay đổi. | **Hồi 2** (phân tích hiện trường) & **Hồi 3** (giải mã động cơ). |
| 8 | **Chu kỳ ảo tưởng & Quỹ đạo leo thang (Fantasy Addiction & Escalation Cycle)** | - **Cơ chế dung nạp kích thích (Tolerance Buildup):** Tội ác không xuất hiện tức thì mà leo thang như một cơn nghiện. Hành vi ban đầu (nhìn trộm, lấy trộm vặt, nói dối bệnh lý) chỉ thỏa mãn tạm thời.<br>- Khi não bộ quen liều, hung thủ rơi vào "đói ảo tưởng" (fantasy starvation) và buộc phải nâng ngưỡng liều: từ rình mò $\\rightarrow$ đột nhập $\\rightarrow$ khống chế $\\rightarrow$ hủy diệt mạng sống. | **Hồi 2** (diễn biến leo thang) & **Hồi 3** (quy luật tâm lý học). |
| 9 | **Hiệu ứng Hào quang & Điểm mù xã hội (Halo Effect & Collective Blindspots)** | - **Hiệu ứng Hào quang (Halo Effect):** Xã hội đánh đồng "Thành đạt/Lịch thiệp/Đạo mạo = Người tốt". Quân phục đại tá, chức danh chủ tịch nhà thờ, danh xưng chính trị gia hay bộ mặt người mẹ hiền trở thành tấm khiên tàng hình hoàn hảo.<br>- **Thành kiến bình thường hóa (Normalcy Bias):** Người xung quanh vô thức lờ đi các dấu hiệu kỳ quặc vì não bộ từ chối tin vào điều kinh hoàng nhất. | **Hồi 1** (vỏ bọc ban đầu) & **Hồi 4** (sự bàng hoàng khi sự thật phơi bày). |
| 10 | **Nạn nhân học & Tín hiệu cảnh báo đỏ sinh tồn (Victimology & Survival Red Flags)** | - **Nạn nhân học (Victimology):** Phân tích sự bất đối xứng quyền lực và tiêu chí chọn mồi của kẻ săn mồi (sự cô lập xã hội, phụ thuộc cảm xúc, tổn thương tâm lý sẵn có). Tuyệt đối không đổ lỗi nạn nhân; luôn tôn vinh phẩm giá, nỗ lực phản kháng và nhân vị trọn vẹn của nạn nhân.<br>- **Bài học sinh tồn (The Gift of Fear):** Cung cấp giá trị thực tiễn cho người xem: cách lắng nghe trực giác bất an, nhận diện các vi tín hiệu thao túng (phá vỡ ranh giới, làm thân dồn dập, đóng vai nạn nhân, kiểm soát đội lốt chăm sóc). | **Hồi 2** (chân dung nạn nhân) & **Hồi 5** (bài học cảnh giác đời thực). |

---

#### 3. Phân vai thể hiện Hệ sinh thái 10 chỉ dấu
- **Host (Cú - Trầm ấm, sâu sắc):** Nêu bật bối cảnh chấn động xã hội (1), hiệu ứng hào quang đánh lừa dư luận (9), dẫn dắt các nghịch lý đạo đức, và đúc kết bài học cảnh tỉnh sinh tồn/trực giác cho khán giả (10) ở đầu và cuối tập.
- **Điều tra viên (Sói - Lạnh lùng, chuẩn xác):** Phân tích rạch ròi giữa thủ đoạn MO và chữ ký Signature (7), ngòi nổ kích hoạt (6), hồ sơ thẩm vấn, phản ứng thực tế của hung thủ với người thân (3), thái độ trước búa tòa (4) và các phát ngôn tự bào chữa nguyên văn (5).
- **Chuyên gia tâm lý (Cáo - Nhấn mạnh, học thuật):** Bóc trần cơ chế chia ngăn nhận thức (3), quá trình leo thang dung nạp ảo tưởng (8), sự vật hóa và khuyết tật thấu cảm đối với nạn nhân (2), kỹ thuật trung hòa đạo đức (5) và sự sụp đổ của bản ngã ái kỷ (4).

---

#### 4. Cổng kiểm kịch bản (Checklist 10 chỉ dấu trước khi duyệt sản xuất)
Trước khi chuyển sang bước Diễn xuất (Bước 1b), biên kịch và AI **PHẢI** đối soát và trả lời được 10 câu hỏi:
- [ ] 1. **Dư chấn xã hội:** Đã làm rõ vụ án gây chấn động, hoang tưởng tập thể hoặc thúc đẩy cải cách thể chế/luật pháp nào chưa?
- [ ] 2. **Góc nhìn về nạn nhân:** Đã bóc trần hung thủ xem nạn nhân là gì (đạo cụ/dự án) và lý giải gốc rễ thiếu hụt thấu cảm chưa?
- [ ] 3. **Góc nhìn về người thân:** Đã mổ xẻ cơ chế chia ngăn nhận thức và bi kịch sụp đổ danh tính của người thân chưa?
- [ ] 4. **Thái độ trước bản án:** Đã phân biệt đúng sự hối hận giả tạo/tự thương hại bản thân so với sự ăn năn chân chính chưa?
- [ ] 5. **Hệ thống tự bào chữa:** Đã vạch trần các lý lẽ trung hòa đạo đức (đổ lỗi nạn nhân, ngoại hóa trách nhiệm) hung thủ dùng để ru ngủ lương tri chưa?
- [ ] 6. **Ngòi nổ tâm lý:** Đã chỉ ra biến cố kích hoạt (giọt nước tràn ly) khiến tội ác bùng phát vào đúng thời điểm đó chưa?
- [ ] 7. **Chữ ký vs. Thủ đoạn:** Đã tách bạch giữa phương thức tẩu thoát (MO) và dấu ấn thỏa mãn nhu cầu cảm xúc bệnh lý (Signature) chưa?
- [ ] 8. **Quỹ đạo leo thang:** Đã cho thấy chu kỳ phát triển của tội ác từ những hành vi xâm lấn ranh giới nhỏ ban đầu chưa?
- [ ] 9. **Hiệu ứng hào quang:** Đã lý giải tại sao vỏ bọc đạo mạo/thành đạt lại tạo ra điểm mù che mắt cộng đồng suốt thời gian dài chưa?
- [ ] 10. **Nạn nhân học & Bài học sinh tồn:** Đã trả lại nhân phẩm cho nạn nhân và đúc kết những tín hiệu cảnh báo đỏ (Red Flags) thực tiễn cho người xem chưa?

'''

# Replace current A2c in tc_text
a2c_start = tc_text.find('### A2c.')
marker_a3 = '## A3. Quy trình chuẩn — lệnh chạy và thời gian đo được'
a2c_end = tc_text.find(marker_a3)
assert a2c_start != -1 and a2c_end != -1, "A2c boundaries not found"

tc_text = tc_text[:a2c_start] + a2c_full + tc_text[a2c_end:]

# Update entry 118 in A11
entry_118_pattern = r'\| 118 \| \*\*Kịch bản sa đà vào nghiệp vụ phá án thuần túy[^\n]+'
new_entry_118 = r'''| 118 | **Kịch bản sa đà vào nghiệp vụ phá án thuần túy, thiếu chiều sâu tâm lý và dư chấn xã hội** (Nhận xét người dùng 05/11/2026): video kể đủ tình tiết, pháp y và điều tra nhưng không làm sáng tỏ tác động xã hội, thế giới quan của hung thủ về nạn nhân/người thân, thái độ trước bản án, cơ chế tự bào chữa và các yếu tố hành vi (ngòi nổ, chữ ký, leo thang, hào quang, nạn nhân học) ⇒ video biến thành phóng sự phá án thông thường, mất bản sắc "giải phẫu tâm lý" của kênh | **Tuân thủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c) & cổng K10 (AGENTS.md)**: Đối soát đủ 10 câu hỏi cốt lõi trước khi duyệt kịch bản (Nhóm I: 5 trụ cột cốt lõi; Nhóm II: 5 yếu tố khoa học hành vi). Phân vai rõ: Host dẫn dắt dư chấn xã hội/triết lý/cảnh báo sinh tồn; Điều tra viên cung cấp dữ kiện/MO vs Signature/ngòi nổ; Chuyên gia tâm lý mổ xẻ chia ngăn/vật hóa/nghiện ảo tưởng |'''

tc_text = re.sub(entry_118_pattern, new_entry_118, tc_text)

# Validate A11
a11_part = tc_text.split('## A11. Bẫy đã gặp — đừng lặp lại')[1].split('## A12')[0]
matches = re.findall(r'^\|\s*(\d+)\s*\|', a11_part, re.MULTILINE)
nums = [int(m) for m in matches]
assert nums == list(range(1, 119)), f"A11 validation failed! nums: {nums}"
print("TIEU_CHUAN A11 validation passed: 1..118 consecutive, 0 duplicates.")

with open(tc_path, 'w', encoding='utf-8') as f:
    f.write(tc_text)
print("Updated 00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md successfully.")

# Update AGENTS.md
with open(agents_path, 'r', encoding='utf-8') as f:
    agents_text = f.read()

# Step 1 update
agents_target1 = '| 1 | **Duyệt kịch bản** (mục 3) | Mọi dữ kiện về người thật đã đối chiếu nguồn công khai; 0 lỗi V9; đủ 5 trụ cột tâm lý (tiêu chuẩn A2c, K10); người dùng duyệt |'
agents_repl1 = '| 1 | **Duyệt kịch bản** (mục 3) | Mọi dữ kiện về người thật đã đối chiếu nguồn công khai; 0 lỗi V9; đạt đủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (tiêu chuẩn A2c, K10); người dùng duyệt |'

assert agents_target1 in agents_text, "agents_target1 not found"
agents_text = agents_text.replace(agents_target1, agents_repl1)

# Rule K10 update
k10_pattern = r'\| K10 \| \*\*5 trụ cột tâm lý bắt buộc \(tiêu chuẩn A2c\):\*\*[^\n]+'
k10_new = r'| K10 | **Hệ sinh thái 10 chỉ dấu tâm lý bắt buộc (tiêu chuẩn A2c):** Kịch bản PHẢI làm rõ: (1) Ảnh hưởng & sự quan tâm xã hội; (2) Cách hung thủ nhìn nạn nhân & vì sao; (3) Cách hung thủ nhìn người thân & chia ngăn; (4) Thái độ trước bản án; (5) Hệ thống tự bào chữa; (6) Ngòi nổ & điểm gãy tâm lý; (7) Dấu ấn Signature vs. Thủ đoạn MO; (8) Quỹ đạo leo thang ảo tưởng; (9) Hiệu ứng hào quang & điểm mù xã hội; (10) Nạn nhân học & cảnh báo đỏ sinh tồn. Tuyệt đối không biến kịch bản thành phóng sự phá án thuần túy |'

agents_text = re.sub(k10_pattern, k10_new, agents_text)

with open(agents_path, 'w', encoding='utf-8') as f:
    f.write(agents_text)
print("Updated AGENTS.md successfully.")
