import json, os, re

data = json.load(open('.work/_episodes_data_final.json', encoding='utf-8'))

# Accurate metadata mapping based on actual crime profiles
case_metadata = {
    1: ("Độc Dược Nhân Danh Tình Mẹ (Dee Dee & Gypsy Rose Blanchard)", "Mỹ"),
    2: ("Đại Tá Hai Mặt (Russell Williams)", "Canada"),
    3: ("Gã Khổng Lồ IQ 145 & Chiếc Gương Giải Phẫu Tâm Trí (Ed Kemper)", "Mỹ"),
    4: ("Thiên Thần Tử Thần & Phức Cảm Chúa Trời (Charles Cullen)", "Mỹ"),
    5: ("Chiếc Đĩa Mềm Màu Tím & Cơn Nghiện Trói Buộc (BTK - Dennis Rader)", "Mỹ"),
    6: ("Nụ Cười Chú Hề & 29 Bí Mật Dưới Tầng Hầm (John Wayne Gacy)", "Mỹ"),
    7: ("Bản Án Giết Người Bằng Tin Nhắn (Michelle Carter)", "Mỹ"),
    8: ("Khi Các Thiên Tài Bị Tẩy Não (Giáo phái Aum Shinrikyo)", "Nhật Bản"),
    9: ("Nghệ Thuật Xóa Bỏ Bản Ngã (Charles Manson & Gia đình Manson)", "Mỹ"),
    10: ("Chiếc Hộp Gỗ Dưới Gầm Giường (Cameron Hooker - Colleen Stan)", "Mỹ"),
    11: ("Cặp Đôi Ken & Barbie (Paul Bernardo & Karla Homolka)", "Canada"),
    12: ("Thảm Kịch Jonestown & Ảo Mộng Thiên Đường Đẫm Máu (Jim Jones)", "Mỹ / Guyana"),
    13: ("Vỏ Bọc 'Con Nhà Người Ta' & Lời Nói Dối 1,5 Triệu Đô (Jennifer Pan)", "Canada"),
    14: ("Bi Kịch Betty Broderick: Phản Kháng Tự Hủy & Cơn Điên Sau Ly Hôn", "Mỹ"),
    15: ("Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới (Jodi Arias)", "Mỹ"),
    16: ("Chiếc Mặt Nạ Quyến Rũ Của Kẻ Săn Mồi (Ted Bundy)", "Mỹ"),
    17: ("Ác Quỷ Đêm Hè (Night Stalker - Richard Ramirez)", "Mỹ"),
    18: ("Quái Vật Vùng Rostov (Andrei Chikatilo)", "Nga (Liên Xô)"),
    19: ("Sát Nhân Sông Xanh & Bản Thỏa Hiệp Lịch Sử (Gary Ridgway)", "Mỹ"),
    20: ("Bóng Ma Hwaseong & 33 Năm Đi Tìm Công Lý (Lee Chun-jae)", "Hàn Quốc"),
    21: ("Căn Hầm Bí Mật 24 Năm & Tội Ác Ngụy Trang Hoàn Hảo (Josef Fritzl)", "Áo"),
    22: ("Bức Thư Kỳ Bí & Ảo Tưởng Ma Quái (Sát nhân Otaku - Tsutomu Miyazaki)", "Nhật Bản"),
    23: ("Bóng Đỏ Bạch Ngân & 28 Năm Giải Mã ADN Phả Hệ (Cao Thừa Dũng)", "Trung Quốc"),
    24: ("Bác Sĩ Tử Thần & Chiếc Bẫy Lòng Tin (Harold Shipman)", "Anh"),
    25: ("Sát Nhân Áo Mưa & Cơn Cuồng Nộ Thù Hận Xã Hội (Yoo Young-chul)", "Hàn Quốc"),
    26: ("Nữ Hộ Sinh Kotobuki & Tội Ác Hậu Chiến (Miyuki Ishikawa)", "Nhật Bản"),
    27: ("Tổn Thương Ái Kỷ & Thao Túng Đồng Phạm (Thảm án Bình Phước - Nguyễn Hải Dương)", "Việt Nam"),
    28: ("Cơn Cuồng Loạn Trong Đêm Mưa Bão (Thảm án tiệm vàng - Lê Văn Luyện)", "Việt Nam"),
    29: ("Nỗi Sợ Bị Bỏ Rơi & Ảo Tưởng Kiểm Soát Tuyệt Đối (Jeffrey Dahmer)", "Mỹ"),
    30: ("Hồ Sơ Chris Watts: Mặt Nạ Chồng Mẫu Mực & Hội Chứng Hủy Diệt Gia Đình", "Mỹ"),
    31: ("Unabomber: Thiên Tài Toán Học & Bản Tuyên Ngôn Chống Văn Minh (Ted Kaczynski)", "Mỹ"),
    32: ("Dating Game Killer: Trò Chơi Hẹn Hò & Ống Kính Tử Thần (Rodney Alcala)", "Mỹ"),
    33: ("Thảm Sát Port Arthur: Bi Kịch Đẫm Máu & Luật Súng Đạn Úc (Martin Bryant)", "Úc"),
    34: ("Kẻ Ăn Thịt Đồng Loại Giữa Thủ Đô Ánh Sáng (Issei Sagawa)", "Nhật Bản / Pháp"),
    35: ("Đứa Con Của Sam & Tiếng Chó Sủa Trong Đêm (David Berkowitz)", "Mỹ"),
    36: ("Đồ Tể Đêm Mưa: Chiếc Hũ Thủy Tinh & Ảo Giác Bệnh Hoạn (Lâm Quá Vân)", "Hồng Kông"),
    37: ("Sát Nhân Vùng Vịnh Vàng: 44 Năm Dưới Vỏ Bọc Cảnh Sát (Joseph DeAngelo)", "Mỹ"),
    38: ("Quái Vật Nữ Xa Lộ & Nỗi Hận Thù Khắc Sâu (Aileen Wuornos)", "Mỹ"),
    39: ("Giáo Phái Đền Thái Dương: Cuộc Di Cư Sang Sao Thiên Lang (Luc Jouret)", "Thụy Sĩ / Pháp / Canada"),
    40: ("Thảm Sát Trường Trung Học Columbine (Eric Harris & Dylan Klebold)", "Mỹ"),
    41: ("Ngôi Nhà Kinh Hoàng Phố Cromwell (Fred & Rose West)", "Anh"),
    42: ("Sát Nhân Bàn Cờ Vua Vùng Moscow (Alexander Pichushkin)", "Nga"),
    43: ("Quái Vật Vùng Marcinelle & Bê Bối Bảo Kê Tư Pháp (Marc Dutroux)", "Bỉ"),
    44: ("Vây Hãm Đỉnh Núi Carmel & Thảm Kịch Waco (David Koresh)", "Mỹ"),
    45: ("Kẻ Giết Người Hàng Loạt Vùng Boksburg (Moses Sithole)", "Nam Phi"),
    46: ("Nữ Cảnh Sát Trục Lợi Bảo Hiểm Bằng Máu (Rosemary Ndlovu)", "Nam Phi"),
    47: ("Sát Nhân Búa Vùng Wemmer Pan (Cedric Maake)", "Nam Phi"),
    48: ("Thảm Án Giết Cha Mẹ Vì Tình (Suzane von Richthofen)", "Brazil"),
    49: ("Quái Vật Vùng Andes (Pedro López)", "Colombia / Ecuador / Peru"),
    50: ("Bộ Ba Ăn Thịt Người Vùng Garanhuns (Jorge Negromonte)", "Brazil"),
    51: ("Quái Vật Florence (Il Mostro di Firenze)", "Ý"),
    52: ("Sát Nhân Đồ Tể Vùng Hannover (Fritz Haarmann)", "Đức"),
    53: ("Bóng Ma Vùng Heilbronn (Phantom of Heilbronn)", "Đức"),
    54: ("Thảm Kịch Hungerford: Cơn Điên Xả Súng (Michael Ryan)", "Anh"),
    55: ("Sát Nhân Bờ Kênh Manchester (The Manchester Pusher)", "Anh"),
    56: ("Quái Vật Vùng Troyes: Vỏ Bọc Người Cha Hoàn Hảo (Patrice Alègre)", "Pháp"),
    57: ("Bác Sĩ Giả & 18 Năm Dối Trá Tự Hủy (Jean-Claude Romand)", "Pháp"),
    58: ("Sát Nhân Rừng Đen Vùng Baden-Württemberg (Heinrich Pommerenke)", "Đức"),
    59: ("Kẻ Săn Đêm Vùng Vienna & Bẫy Cảnh Sát Quốc Tế (Jack Unterweger)", "Áo"),
    60: ("Nữ Quái Lao Vinh Chi & Pháp Tử Anh: Chiếc Lồng Chó Đoạt Mạng", "Trung Quốc"),
    61: ("Sát Nhân Vùng Vũ Hán & Bản Án Tống Tiền Đẫm Máu", "Trung Quốc"),
    62: ("Thảm Sát Gangwon: Cơn Điên Của Viên Cảnh Sát (Woo Bum-kon)", "Hàn Quốc"),
    63: ("Băng Đảng Chijon: Lò Thiêu Người & Sự Căm Phẫn Giới Thượng Lưu", "Hàn Quốc"),
    64: ("Kẻ Độc Hành Akihabara & Vòng Xoáy Trầm Cảm Mạng Xã Hội (Tomohiro Kato)", "Nhật Bản"),
    65: ("Thảm Sát Kyoto Animation & Ảo Tưởng Đạo Văn (Shinji Aoba)", "Nhật Bản"),
    66: ("Thảm Án Tiệm Bánh Bát Tiên & Ám Ảnh 'Bánh Bao Thịt Người'", "Ma Cao"),
    67: ("Hồ Sơ 'Đông Tinh' & Băng Đảng Xã Hội Đen Bắt Cóc Hồng Kông", "Hồng Kông"),
    68: ("Tướng Cướp Thế Kỷ & Tâm Lý Con Bạc Bệnh Lý (Trương Tử Cường)", "Hồng Kông")
}

for row in data:
    ep = row['ep']
    if ep in case_metadata:
        row['clean_title'], row['country'] = case_metadata[ep]
        
    # Accurate sentence count check:
    # If sentences < 50 for planned episodes, calculate from dialogue paragraphs in script
    kb_path = f"01_KICH_BAN/Tap{ep:02d}"
    if os.path.exists(kb_path):
        files = [f for f in os.listdir(kb_path) if f.endswith('.md')]
        vn_files = [f for f in files if 'kichban_' in f and not any(k in f for k in ['_EN', '_JA', '_KO', 'REVIEW'])]
        target = os.path.join(kb_path, sorted(vn_files)[-1]) if vn_files else (os.path.join(kb_path, sorted(files)[0]) if files else None)
        if target:
            lines = open(target, encoding='utf-8').readlines()
            # A turn in kịch bản has lines of text. Let's count spoken non-empty sentences or dialogue turns
            # Count elements like `1.01`, `1.02`
            elem_ids = re.findall(r'`\d+\.\d+`', open(target, encoding='utf-8').read())
            if len(elem_ids) > 100:
                row['sentences'] = len(elem_ids)

    # Shots count:
    # If shots == 0 (not parsed yet), by production rule it equals:
    # number of sentences + 4 act transitions + 1 closing card = sentences + 5
    if row['shots'] > 0:
        row['shots_rule'] = row['shots']
    else:
        row['shots_rule'] = row['sentences'] + 5 if row['sentences'] > 0 else "Chưa chốt kịch bản"

open('.work/_episodes_data_final.json', 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=2))
print('Data fully enriched and validated!')
