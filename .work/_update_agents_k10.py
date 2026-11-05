with open('AGENTS.md', 'r', encoding='utf-8') as f:
    text = f.read()

target1 = '| 1 | **Duyệt kịch bản** (mục 3) | Mọi dữ kiện về người thật đã đối chiếu nguồn công khai; 0 lỗi V9; người dùng duyệt |'
repl1 = '| 1 | **Duyệt kịch bản** (mục 3) | Mọi dữ kiện về người thật đã đối chiếu nguồn công khai; 0 lỗi V9; đủ 5 trụ cột tâm lý (tiêu chuẩn A2c, K10); người dùng duyệt |'

target2 = '| K9 | Định dạng kịch bản theo tiêu chuẩn A2. Tên riêng có viết tắt có dấu chấm ("Robert F. Scott") sẽ bị tách câu sai → viết "Robert Scott" |'
repl2 = target2 + '\n| K10 | **5 trụ cột tâm lý bắt buộc (tiêu chuẩn A2c):** Kịch bản PHẢI làm rõ: (1) Ảnh hưởng & sự quan tâm của xã hội; (2) Cách hung thủ nhìn nạn nhân & vì sao; (3) Cách hung thủ nhìn người thân & vì sao; (4) Thái độ hung thủ trước bản án; (5) Hệ thống tự bào chữa (neutralization). Tuyệt đối không biến kịch bản thành phóng sự phá án thuần túy |'

assert target1 in text, 'target1 not found'
assert target2 in text, 'target2 not found'

text = text.replace(target1, repl1)
text = text.replace(target2, repl2)

with open('AGENTS.md', 'w', encoding='utf-8') as f:
    f.write(text)
print('AGENTS.md updated successfully.')
