import json

report = json.load(open('.work/_accurate_final_report.json', encoding='utf-8'))
pool = {r['ep']: r for r in report[28:]}

# Principle of shuffling:
# We want to interweave:
# A: Mỹ & Phương Tây giật gân (Dahmer, Chris Watts, Unabomber...)
# B: Châu Á cận cảnh / Việt Nam (Nguyễn Đức Nghĩa, Trương Tử Cường, Hello Kitty, Lao Vinh Chi...)
# C: Châu Âu / Nam Phi bí ẩn (Quái vật Florence, Marc Dutroux, Natascha Kampusch...)
# D: Tâm lý gia đình / Ái kỷ / Giáo phái độc hại (Turpin, Garanhuns, Richthofen...)

# Let's design a curated sequence from 29 to 68
curated_order = [
    # Giai đoạn 1: Mở màn hấp dẫn sau tập 28 (Lê Văn Luyện)
    29, # Jeffrey Dahmer (Mỹ - Sát nhân tâm lý hàng đầu)
    34, # Nguyễn Đức Nghĩa (Việt Nam - Vụ án rúng động tâm lý sinh viên)
    30, # Chris Watts (Mỹ - Án mạng gia đình & mặt nạ hoàn hảo)
    68, # Trương Tử Cường (Hồng Kông - Tướng cướp thế kỷ & tâm lý con bạc)
    38, # Natascha Kampusch (Áo - 3.096 ngày giam cầm tâm lý)
    31, # Ted Kaczynski - Unabomber (Mỹ - Thiên tài chống văn minh)
    67, # Vụ Án Hello Kitty (Hồng Kông - Ám ảnh tâm lý tội phạm đô thị)
    41, # Quái Vật Florence (Ý - Bí ẩn đôi tình nhân nước Ý)
    35, # Nguyễn Đức Anh (Việt Nam - Tâm lý tội ác giấu xác)
    33, # Aileen Wuornos (Mỹ - Quái vật nữ xa lộ & thù hận)
    
    # Giai đoạn 2: Đan xen Á - Âu - Mỹ và các hội chứng tâm lý đa dạng
    62, # Lao Vinh Chi & Pháp Tử Anh (Trung Quốc - Cặp đôi sát nhân lồng sắt)
    32, # Rodney Alcala - Dating Game (Mỹ - Ống kính tử thần)
    37, # Dr. Harold Shipman (Anh - Bác sĩ tử thần & bẫy lòng tin)
    53, # Tsutomu Miyazaki (Nhật Bản - Sát nhân Otaku & ảo giác)
    48, # Suzane von Richthofen (Brazil - Thảm án con cái vì tình)
    36, # Kip Kinkel (Mỹ - Xả súng trường học & tiếng nói hoang tưởng)
    65, # Lâm Quá Vân - Đồ Tể Đêm Mưa (Hồng Kông - Hũ thủy tinh kinh dị)
    42, # Marc Dutroux (Bỉ - Quái vật Marcinelle & bê bối tư pháp)
    54, # Thùng Xi Măng Tân Trang (Đài Loan - Nấm mồ bê tông mẹ kế)
    59, # David Parker Ray - Toy Box Killer (Mỹ - Căn phòng tra tấn)

    # Giai đoạn 3: Tội phạm xuyên quốc gia & giáo phái dị biệt
    57, # Charles Sobhraj - Con Rắn Độc Bikini (Pháp / Ấn Độ / Nepal)
    39, # Joanna Dennehy (Anh - Nữ sát nhân tâm thần phân liệt)
    63, # Ngô Tạ Vũ (Trung Quốc - Bi kịch thiên tài ĐH Bắc Kinh giết mẹ)
    52, # Gia Đình Turpin (Mỹ - Ngôi nhà giam cầm 13 đứa con)
    46, # Rosemary Ndlovu (Nam Phi - Nữ cảnh sát trục lợi bảo hiểm bằng máu)
    61, # Điêu Ái Thanh (Trung Quốc - Kỳ án 2.000 mảnh ĐH Nam Kinh)
    43, # Peter Kürten (Đức - Ma cà rồng Düsseldorf)
    50, # Bộ Ba Garanhuns (Brazil - Giáo phái ăn thịt đồng loại)
    40, # Patrice Alègre (Pháp - Kẻ săn đêm vùng Toulouse)
    58, # Thảm Án Gia Đình Miyazawa (Nhật Bản - Bí ẩn Setagaya)

    # Giai đoạn 4: Đỉnh điểm hồ sơ hóc búa & chặng cuối
    49, # Pedro López (Colombia/Ecuador - Quái vật Andes)
    60, # Sát Nhân Bạch Ngân - Cao Thừa Dũng (Trung Quốc - 28 năm truy tìm ADN)
    44, # Bóng Ma Heilbronn (Đức - Sai lầm thế kỷ về dấu vết ADN)
    55, # Adrian Lim (Singapore - Gã thầy pháp toa rập tà giáo)
    45, # Moses Sithole (Nam Phi - Sát nhân xa lộ)
    64, # Chu Khắc Hoa (Trung Quốc - Tay súng bắn tỉa nguy hiểm nhất)
    51, # Juana Barraza (Mexico - Nữ đô vật sát hại người già)
    56, # Mona Fandey (Malaysia - Nữ phù thủy đoạt mạng chính khách)
    47, # Cedric Maake (Nam Phi - Sát nhân búa Wemmer Pan)
    66  # Chu Khải Bình (Hồng Kông - Bi kịch con trai bất hiếu)
]

print("Length of curated order:", len(curated_order))
print("Is permutation of 29..68:", sorted(curated_order) == list(range(29, 69)))

out_mapping = []
for new_ep, old_ep in enumerate(curated_order, start=29):
    item = pool[old_ep]
    out_mapping.append({
        'new_ep': new_ep,
        'old_ep': old_ep,
        'title': item['title'],
        'country': item['country'],
        'images': item['images'],
        'sentences': item['sentences']
    })

open('.work/_proposed_shuffle.json', 'w', encoding='utf-8').write(json.dumps(out_mapping, ensure_ascii=False, indent=2))
print("Proposed shuffle generated successfully!")
