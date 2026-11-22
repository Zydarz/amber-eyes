import json, re, os

# Load previously gathered data
data = json.load(open('.work/_episodes_data_cleaned.json', encoding='utf-8'))

# Manual overrides / fine tuning for accurate reporting
for row in data:
    ep = row['ep']
    ep_str = f"Tap{ep:02d}"
    
    # Tap 26
    if ep == 26:
        row['title'] = "Nữ Hộ Sinh Kotobuki & Tội Ác Dưới Lớp Vỏ Bọc Từ Thiện (Hồ Sơ Miyuki Ishikawa)"
        row['topic'] = "Vụ án phòng bảo sanh Kotobuki, Tokyo"
        row['country'] = "Nhật Bản"
        row['clean_title'] = "Nữ Hộ Sinh Kotobuki (Miyuki Ishikawa)"
    # Tap 29
    elif ep == 29:
        row['title'] = "Sát Nhân Từ Nỗi Sợ Bị Bỏ Rơi Bệnh Lý (Hồ Sơ Jeffrey Dahmer)"
        row['topic'] = "Hồ sơ Jeffrey Dahmer, Milwaukee, Wisconsin"
        row['country'] = "Mỹ"
        row['clean_title'] = "Jeffrey Dahmer — Kẻ Ăn Thịt Người Vùng Milwaukee"
    elif ep == 27:
        row['country'] = "Việt Nam"
    elif ep == 28:
        row['country'] = "Việt Nam"
        
    # Check exact sentences count from parse_kichban logic or script file
    kb_dir = f"01_KICH_BAN/{ep_str}"
    if os.path.exists(kb_dir):
        files = [f for f in os.listdir(kb_dir) if f.endswith('.md')]
        vn_files = [f for f in files if 'kichban_' in f and not any(k in f for k in ['_EN', '_JA', '_KO', 'REVIEW'])]
        target = os.path.join(kb_dir, sorted(vn_files)[-1]) if vn_files else (os.path.join(kb_dir, sorted(files)[0]) if files else None)
        if target:
            c = open(target, encoding='utf-8').read()
            # Find dialogue blocks
            # Match element lines like `1.01`, `1.02` with dialogue
            # Or regex count of all sentences
            # Count elements that have dialogues
            turns = re.findall(r'(?:\*\*(?:HOST|ĐIỀU TRA VIÊN|CHUYÊN GIA TÂM LÝ|CÚ|SÓI|CÁO|N1|N2|[^\*]+)\*\*|`\d+\.\d+`):?\s*([^\n]+)', c)
            # If the current sentences count is 0 or dubious, update it
            if row['sentences'] == 0 and turns:
                row['sentences'] = len(turns)

    # Clean up topic & title display
    # Remove markdown formatting like **
    row['clean_title'] = re.sub(r'[\*\"“”]', '', row['clean_title']).strip()
    row['topic'] = re.sub(r'[\*\"“”]', '', row['topic']).strip()
    
    # If shots count is 0, what is the shot rule count?
    # In AMBER EYES standard, when shot table is not generated yet, rule:
    # 1 shot corresponds to 1 sentence (or dialogue beat), plus intro, 4 act transitions, and 1 ending card.
    # So expected shot count = sentences + ~5 (intro/cards) or roughly 1:1 with sentences.
    # If shots > 0 (already generated in shots.json or plan table), we keep that exact number.
    row['shots_status'] = 'Đã lập bảng shot' if row['shots'] > 0 else 'Chưa lập bảng shot'
    row['expected_shots'] = row['shots'] if row['shots'] > 0 else (f"~{row['sentences'] + 5}" if row['sentences'] > 0 else "Chưa chốt")

open('.work/_episodes_data_final.json', 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=2))
print('Final data ready!')
