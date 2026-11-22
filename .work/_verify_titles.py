import json, os, re

accurate = json.load(open('.work/_accurate_sentences.json', encoding='utf-8'))

for item in accurate:
    ep = item['ep']
    ep_str = item['ep_str']
    script_path = os.path.join(f"01_KICH_BAN/{ep_str}", item['script_file'])
    txt = open(script_path, encoding='utf-8').read()
    
    # Extract the main title from Markdown header
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    header_lines = [l for l in lines if l.startswith('#')]
    
    title_line = ''
    if len(header_lines) > 0:
        # Often line 1 is '# KỊCH BẢN CHI TIẾT TẬP XX: HỒ SƠ ...'
        # or line 2 has '## HỒ SƠ ...'
        for hl in header_lines:
            if any(k in hl for k in ['HỒ SƠ', 'VỤ ÁN', 'THẢM ÁN', 'BẢN ÁN', 'KỲ ÁN', 'ĐẠI TÁ', 'ĐỘC DƯỢC', 'GÃ KHỔNG LỒ', 'THIÊN THẦN', 'CHIẾC ĐĨA MỀM', 'NỤ CƯỜI CHÚ HỀ', 'KHI CÁC THIÊN TÀI', 'NGHỆ THUẬT', 'CHIẾC HỘP GỖ', 'CẶP ĐÔI', 'THẢM KỊCH', 'VỎ BỌC', 'BI KỊCH', 'CƠN CUỒNG GHEN', 'CHIẾC MẶT NẠ', 'ÁC QUỶ', 'QUÁI VẬT', 'SÁT NHÂN', 'BÓNG MA', 'CĂN HẦM', 'BỨC THƯ', 'BÓNG ĐỎ', 'BÁC SĨ']):
                title_line = hl
                break
        if not title_line:
            title_line = header_lines[0]
            
    # Clean up title line
    title_clean = re.sub(r'^#+\s*', '', title_line)
    title_clean = re.sub(r'^KỊCH BẢN (?:CHI TIẾT |AUDIO\s*/\s*PODCAST\s*TÂM LÝ HỌC TỘI PHẠM\s*[-–—]\s*)?TẬP\s*\d+[:\s\-\–—]*', '', title_clean, flags=re.IGNORECASE)
    title_clean = re.sub(r'\(PHẦN [AB]\)', '', title_clean, flags=re.IGNORECASE).strip()
    
    # Topic from plan or script
    topic = item.get('topic', '')
    
    # Detect country accurately from content
    full_sample = (title_clean + " " + topic + " " + txt[:2500]).lower()
    
    country = "Mỹ" # default
    if any(k in full_sample for k in ['bình phước', 'bắc giang', 'nguyễn hải dương', 'lê văn luyện', 'nguyễn đức nghĩa', 'nguyễn đức anh', 'việt nam']):
        country = "Việt Nam"
    elif any(k in full_sample for k in ['hàn quốc', 'korea', 'seoul', 'hwaseong', 'lee choon-jae', 'yoo young-chul', 'woo bum-kon', 'chijon']):
        country = "Hàn Quốc"
    elif any(k in full_sample for k in ['nhật bản', 'japan', 'tokyo', 'aum shinrikyo', 'miyuki ishikawa', 'tsutomu miyazaki', 'akihabara', 'kyoto animation', 'tomohiro kato', 'shinji aoba']):
        country = "Nhật Bản"
    elif any(k in full_sample for k in ['hồng kông', 'hong kong', 'lâm quá vân', 'trương tử cường', 'hello kitty', 'đông tinh']):
        country = "Hồng Kông"
    elif any(k in full_sample for k in ['ma cao', 'macau', 'bát tiên']):
        country = "Ma Cao"
    elif any(k in full_sample for k in ['trung quốc', 'china', 'bạch ngân', 'cao thừa dũng', 'lao vinh chi', 'pháp tử anh', 'ngô tạ vũ', 'chu khắc hoa', 'điêu ái thanh']):
        country = "Trung Quốc"
    elif any(k in full_sample for k in ['canada', 'ontario', 'russell williams', 'paul bernardo', 'karla homolka', 'jennifer pan']):
        country = "Canada"
    elif any(k in full_sample for k in ['anh quốc', 'vương quốc anh', 'nước anh', 'england', 'uk', 'london', 'harold shipman', 'fred & rose west', 'fred west', 'hungerford', 'manchester']):
        country = "Anh"
    elif any(k in full_sample for k in ['áo', 'austria', 'amstetten', 'josef fritzl', 'vienna', 'jack unterweger']):
        country = "Áo"
    elif any(k in full_sample for k in ['úc', 'australia', 'tasmania', 'port arthur', 'martin bryant']):
        country = "Úc"
    elif any(k in full_sample for k in ['pháp', 'france', 'paris', 'issei sagawa', 'patrice alègre', 'jean-claude romand']):
        country = "Pháp"
    elif any(k in full_sample for k in ['đức', 'germany', 'hannover', 'heilbronn', 'baden-württemberg', 'fritz haarmann', 'heinrich pommerenke']):
        country = "Đức"
    elif any(k in full_sample for k in ['bỉ', 'belgium', 'marcinelle', 'marc dutroux']):
        country = "Bỉ"
    elif any(k in full_sample for k in ['nga', 'russia', 'rostov', 'moscow', 'andrei chikatilo', 'alexander pichushkin']):
        country = "Nga"
    elif any(k in full_sample for k in ['brazil', 'richthofen', 'garanhuns']):
        country = "Brazil"
    elif any(k in full_sample for k in ['nam phi', 'south africa', 'moses sithole', 'rosemary ndlovu', 'cedric maake']):
        country = "Nam Phi"
    elif any(k in full_sample for k in ['ý', 'italy', 'florence']):
        country = "Ý"
    elif any(k in full_sample for k in ['mexico', 'juana barraza']):
        country = "Mexico"
    elif any(k in full_sample for k in ['colombia', 'ecuador', 'peru', 'pedro lópez']):
        country = "Colombia / Ecuador"
    elif any(k in full_sample for k in ['đài loan', 'taiwan']):
        country = "Đài Loan"
    elif any(k in full_sample for k in ['guyana', 'jonestown']):
        country = "Mỹ / Guyana"
        
    item['actual_title'] = title_clean
    item['actual_country'] = country

open('.work/_accurate_metadata.json', 'w', encoding='utf-8').write(json.dumps(accurate, ensure_ascii=False, indent=2))
print('Metadata successfully mapped!')
