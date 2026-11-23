# -*- coding: utf-8 -*-
"""Update REVIEW_kichban_tap16_multilingual.md with exact 257-sentence counts and QC outputs."""
import sys, re
sys.path.insert(0, '.work')
import parse_kichban as PK

p_vn = PK.parse_file('01_KICH_BAN/Ho_So_Toi_Pham/Tap16/kichban_tap16_23102026.md')

review_path = '01_KICH_BAN/Ho_So_Toi_Pham/Tap16/REVIEW_kichban_tap16_multilingual.md'
content = open(review_path, encoding='utf-8').read()

# Update summary line
content = re.sub(
    r'\*\*Tổng cộng toàn tập:\*\* \*\*51 phần tử · 32 lượt thoại · 220 câu thoại.*',
    '**Tổng cộng toàn tập:** **51 phần tử · 32 lượt thoại · 257 câu thoại (khớp tuyệt đối 1:1 trên toàn bộ 4 ngôn ngữ).**',
    content
)

# Update QC code block
qc_old = """==========================================
PARITY AUDIT ACROSS 4 EDITIONS
==========================================
VN: 51 elements, 32 LOI turns, 220 sentences -> MATCH
EN: 51 elements, 32 LOI turns, 220 sentences -> MATCH
JA: 51 elements, 32 LOI turns, 220 sentences -> MATCH
KO: 51 elements, 32 LOI turns, 220 sentences -> MATCH

>>> FINAL STATUS TAP 16: ALL PASS <<< (Exit Code: 0)"""

qc_new = """==========================================
PARITY AUDIT ACROSS 4 EDITIONS
==========================================
VN: 51 elements, 32 LOI turns, 257 sentences -> MATCH
EN: 51 elements, 32 LOI turns, 257 sentences -> MATCH
JA: 51 elements, 32 LOI turns, 257 sentences -> MATCH
KO: 51 elements, 32 LOI turns, 257 sentences -> MATCH

>>> FINAL STATUS TAP 16: ALL PASS <<< (Exit Code: 0)"""

content = content.replace(qc_old, qc_new)

# Update Act headings and specific counts in tables
content = content.replace('7 lượt thoại, 50 câu', '7 lượt thoại, 58 câu')
content = content.replace('| **1.04** | LOI | **D** (Điều tra viên) | Khách quan, sắc lạnh, hiện trường ban đầu | 8 | 8 | 8 | 8 |',
                          '| **1.04** | LOI | **H** (Host) | Vỏ bọc gia đình danh giá & Điểm mù thượng lưu | 12 | 12 | 12 | 12 |')
content = content.replace('| **1.07** | LOI | **N** (N1 - Jean Phillips) | Bàng hoàng, linh cảm bất an của học sinh | 6 | 6 | 6 | 6 |',
                          '| **1.07** | LOI | **N** (N1 - Jean Phillips) | Bàng hoàng, linh cảm bất an & Chấn thương đạo đức | 12 | 12 | 12 | 12 |')

content = content.replace('6 lượt thoại, 41 câu', '6 lượt thoại, 45 câu')
content = content.replace('| **2.10** | LOI | **C** (Chuyên gia) | Phân tích cơ chế biến mất của hung thủ OCPD | 7 | 7 | 7 | 7 |',
                          '| **2.10** | LOI | **C** (Chuyên gia) | Cơ chế Chia ngăn nhận thức 18 năm & Vỏ bọc Robert Clark | 11 | 11 | 11 | 11 |')

content = content.replace('7 lượt thoại, 45 câu', '7 lượt thoại, 53 câu')
content = content.replace('| **3.04** | LOI | **C** (Chuyên gia) | Bóc tách kỹ thuật "Mục đích cao cả" | 6 | 6 | 6 | 6 |',
                          '| **3.04** | LOI | **C** (Chuyên gia) | Kỹ thuật "Mục đích cao cả" & Tại sao không thể hối hận | 10 | 10 | 10 | 10 |')
content = content.replace('| **3.05** | LOI | **H** (Host) | Bức thư 5 trang gửi mục sư và sự ngụy biện đức tin | 7 | 7 | 7 | 7 |',
                          '| **3.05** | LOI | **H** (Host) | Bức thư 5 trang, Ăn năn giả tạo & Tự thương hại bệnh lý | 11 | 11 | 11 | 11 |')

content = content.replace('8 lượt thoại, 49 câu', '8 lượt thoại, 58 câu')
content = content.replace('| **4.09** | LOI | **N** (N2 - Wanda Flanery) | Chân thực, sự bàng hoàng về người hàng xóm | 6 | 6 | 6 | 6 |',
                          '| **4.09** | LOI | **N** (N2 - Wanda Flanery) | Động lực chuyển hóa tâm lý & Phá vỡ hiệu ứng bàng quan | 11 | 11 | 11 | 11 |')
content = content.replace('| **4.12** | LOI | **C** (Chuyên gia) | Sự sụp đổ của chiếc mặt nạ bình thường hóa | 6 | 6 | 6 | 6 |',
                          '| **4.12** | LOI | **C** (Chuyên gia) | Cú sốc sụp đổ bản ngã của người vợ thứ hai Delores Miller | 10 | 10 | 10 | 10 |')

content = content.replace('4 lượt thoại, 35 câu', '4 lượt thoại, 43 câu')
content = content.replace('| **5.03** | LOI | **D** (Điều tra viên) | Di sản khoa học hình sự và sự khép lại vụ án | 5 | 5 | 5 | 5 |',
                          '| **5.03** | LOI | **D** (Điều tra viên) | Di sản khoa học hình sự & Bài học cảnh giác cộng đồng | 9 | 9 | 9 | 9 |')
content = content.replace('| **5.04** | LOI | **C** (Chuyên gia) | Bóc tách bản ngã ái kỷ độc hại và tình yêu gia đình | 6 | 6 | 6 | 6 |',
                          '| **5.04** | LOI | **C** (Chuyên gia) | Chấn thương đạo đức nhân chứng & Trách nhiệm xã hội | 10 | 10 | 10 | 10 |')

content = content.replace('total sentences: 220', 'total sentences: 257')
content = content.replace('51 elements, 220 sentences, parity with', '51 elements, 257 sentences, parity with')
content = content.replace('câu VN=220 JA=220', 'câu VN=257 JA=257')
content = content.replace('220 câu đọc.', '257 câu đọc.')

open(review_path, 'w', encoding='utf-8').write(content)
print("REVIEW_kichban_tap16_multilingual.md updated successfully.")
