import json, re, os

data = json.load(open('.work/_episodes_data.json', encoding='utf-8'))

# Let's inspect country determination and clean up titles / cases
for row in data:
    ep = row['ep']
    ep_str = f"Tap{ep:02d}"
    plan_path = f"02_SAN_XUAT/{ep_str}/KeHoach_Video_{ep_str}.md"
    txt = open(plan_path, encoding='utf-8').read() if os.path.exists(plan_path) else ''
    
    # Refine Country
    c_text = (row['title'] + " " + row['topic'] + " " + txt[:3000]).lower()
    
    country = 'Chưa rõ'
    if any(k in c_text for k in ['hàn quốc', 'seoul', 'hwaseong', 'busan', 'cho seung-hui', 'lee chun-jae']):
        country = 'Hàn Quốc'
    elif any(k in c_text for k in ['nhật bản', 'tokyo', 'kyoto', 'osaka', 'kobe', 'saitama', 'aum shinrikyo', 'tsutomu miyazaki', 'akihabara']):
        country = 'Nhật Bản'
    elif any(k in c_text for k in ['hồng kông', 'hong kong', 'trương tử cường', 'lâm quá vân', 'lý gia thành']):
        country = 'Hồng Kông'
    elif any(k in c_text for k in ['trung quốc', 'quảng đông', 'bạch ngân', 'thượng hải', 'bắc kinh', 'lao vinh chi', 'pháp tử anh']):
        country = 'Trung Quốc'
    elif any(k in c_text for k in ['canada', 'ontario', 'toronto', 'trenton', 'belleville', 'russell williams', 'paul bernardo', 'karla homolka']):
        country = 'Canada'
    elif any(k in c_text for k in ['anh quốc', 'nước anh', 'vương quốc anh', 'london', 'manchester', 'leeds', 'harold shipman', 'jack the ripper']):
        country = 'Anh'
    elif any(k in c_text for k in ['áo', 'austria', 'vienna', 'josef fritzl', 'amstetten']):
        country = 'Áo'
    elif any(k in c_text for k in ['đức', 'germany', 'berlin']):
        country = 'Đức'
    elif any(k in c_text for k in ['pháp', 'france', 'paris']):
        country = 'Pháp'
    elif any(k in c_text for k in ['úc', 'australia', 'snowtown', 'martin bryant', 'port arthur']):
        country = 'Úc'
    elif any(k in c_text for k in ['hoa kỳ', 'mỹ', 'fbi', 'california', 'texas', 'florida', 'colorado', 'ohio', 'new york', 'massachusetts', 'illinois', 'kansas', 'missouri', 'oregon', 'washington', 'connecticut', 'georgia', 'indiana', 'alaska', 'nebraska', 'utah', 'tennessee', 'louisiana', 'michigan', 'wisconsin', 'maryland', 'pennsylvania', 'minnesota', 'arizona', 'nevada', 'iowa']):
        country = 'Mỹ'
    elif any(k in c_text for k in ['nga', 'moscow', 'liên xô', 'alexander pichushkin', 'chikatilo']):
        country = 'Nga'
    
    row['country'] = country
    
    # Accurate sentences count
    # Check script file directly using regex on dialogue turns
    kb_dir = f"01_KICH_BAN/{ep_str}"
    if os.path.exists(kb_dir):
        files = [f for f in os.listdir(kb_dir) if f.endswith('.md')]
        vn_files = [f for f in files if 'kichban_' in f and not any(k in f for k in ['_EN', '_JA', '_KO', 'REVIEW'])]
        target = os.path.join(kb_dir, sorted(vn_files)[-1]) if vn_files else (os.path.join(kb_dir, sorted(files)[0]) if files else None)
        if target:
            lines = open(target, encoding='utf-8').readlines()
            # In AMBER EYES, dialogue lines are marked by bold character headers, e.g. **HOST**:, **ĐIỀU TRA VIÊN**:
            # or lines with `1.01`, etc.
            # But let's check if the plan has the exact canonical count:
            m_c = re.search(r'\|\s*Lượt nói\s*/\s*câu\s*/\s*từ\s*\|\s*[^\|]*?/\s*\*\*?(\d+)\*\*?', txt)
            if not m_c:
                m_c = re.search(r'\|\s*(?:Lượt nói\s*/\s*)?câu(?:\s*/\s*từ)?\s*\|\s*.*?(\d+)\s+câu', txt)
            if not m_c:
                m_c = re.search(r'\*\*(\d+)\s+câu(?:\s+thoại)?\*\*', txt)
            if not m_c:
                m_c = re.search(r'(\d+)\s+câu thoại', txt)
            if not m_c:
                # count from script: count paragraphs that are spoken dialogue
                # let's count dialogue blocks
                dlg = 0
                for l in lines:
                    l_s = l.strip()
                    if any(l_s.startswith(r) for r in ['**HOST', '**ĐIỀU TRA', '**CHUYÊN GIA', '**CÚ', '**SÓI', '**CÁO', '**N1', '**N2', '**NGƯỜI']):
                        dlg += 1
                row['sentences'] = dlg if dlg > 0 else row['sentences']
            else:
                row['sentences'] = int(m_c.group(1))

    # Clean Title / Case Name
    title_clean = row['title']
    title_clean = re.sub(r'\(PHẦN B\)', '', title_clean).strip()
    title_clean = re.sub(r'^Tập\s*\d+[:\s\-\–]*', '', title_clean).strip()
    row['clean_title'] = title_clean

open('.work/_episodes_data_cleaned.json', 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=2))

# Print summary of countries
unresolved = [r for r in data if r['country'] == 'Chưa rõ']
print(f'Unresolved countries: {len(unresolved)}')
for u in unresolved:
    print(f"Tap{u['ep']:02d}: {u['title']} | {u['topic']}")
