import glob, json, os, re

def get_country(text):
    text_lower = text.lower()
    if any(k in text_lower for k in ['hoa kỳ', 'mỹ', 'california', 'texas', 'florida', 'colorado', 'ohio', 'new york', 'massachusetts', 'illinois', 'kansas', 'missouri', 'oregon', 'washington', 'connecticut', 'georgia', 'indiana', 'alaska', 'nebraska', 'utah', 'fbi']):
        return 'Mỹ'
    if any(k in text_lower for k in ['nhật bản', 'tokyo', 'kyoto', 'osaka', 'kobe', 'saitama', 'aum shinrikyo']):
        return 'Nhật Bản'
    if any(k in text_lower for k in ['hàn quốc', 'seoul', 'hwaseong', 'busan']):
        return 'Hàn Quốc'
    if any(k in text_lower for k in ['hồng kông', 'hong kong']):
        return 'Hồng Kông'
    if any(k in text_lower for k in ['trung quốc', 'bắc kinh', 'thượng hải', 'quảng đông', 'bạch ngân']):
        return 'Trung Quốc'
    if any(k in text_lower for k in ['anh quốc', 'nước anh', 'london', 'manchester', 'leeds']):
        return 'Anh'
    if any(k in text_lower for k in ['canada', 'ontario', 'toronto', 'trenton', 'belleville']):
        return 'Canada'
    if any(k in text_lower for k in ['úc', 'australia', 'sydney', 'melbourne', 'adelaide']):
        return 'Úc'
    if any(k in text_lower for k in ['pháp', 'paris']):
        return 'Pháp'
    if any(k in text_lower for k in ['đức', 'berlin']):
        return 'Đức'
    if any(k in text_lower for k in ['nga', 'moscow', 'liên xô']):
        return 'Nga'
    if any(k in text_lower for k in ['áo', 'austria', 'vienna']):
        return 'Áo'
    return 'Chưa rõ'

# Check all bg files in assets/bg and _raw
bg_files = set(os.listdir('assets/bg') if os.path.exists('assets/bg') else [])
raw_files = set(os.listdir('assets/bg/_raw') if os.path.exists('assets/bg/_raw') else [])
all_bg = bg_files | raw_files

def get_generated_images_count(ep):
    if ep == 1:
        return 44
    prefix1 = f"t{ep}_"
    prefix2 = f"t{ep:02d}_"
    prefix3 = f"tap{ep:02d}_"
    imgs = [f for f in all_bg if f.lower().startswith(prefix1) or f.lower().startswith(prefix2) or f.lower().startswith(prefix3)]
    return len(imgs)

def get_shots_rule_count(ep, plan_text):
    # 1. From shots_tXX.json or shots.json
    fn = '.work/shots.json' if ep == 1 else f'.work/shots_t{ep:02d}.json'
    if os.path.exists(fn):
        try:
            d = json.load(open(fn, encoding='utf-8'))
            shots = d.get('shots', [])
            if len(shots) > 0:
                return len(shots)
        except:
            pass
            
    # 2. From plan_text shot table lines
    shot_lines = [l for l in plan_text.splitlines() if re.match(r'^\|\s*`?\d+[\.\d]*', l)]
    if len(shot_lines) > 0:
        return len(shot_lines)
        
    # 3. From text mentions: "(\d+) shot" or "(\d+) dòng"
    m = re.search(r'(\d+)\s+shot', plan_text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r'Bảng shot\s*\|\s*\*\*?(\d+)\s+dòng', plan_text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return 0

def get_sentences_count(ep, plan_text):
    # Try plan text first
    m = re.search(r'(\d+)\s+câu', plan_text)
    # Check if there is sentence count in script file
    kb_dir = f'01_KICH_BAN/Tap{ep:02d}'
    script_file = None
    if os.path.exists(kb_dir):
        files = [f for f in os.listdir(kb_dir) if f.endswith('.md')]
        vn_files = [f for f in files if 'kichban_' in f and not any(k in f for k in ['_EN', '_JA', '_KO', 'REVIEW'])]
        if vn_files:
            script_file = os.path.join(kb_dir, sorted(vn_files)[-1])
        elif files:
            script_file = os.path.join(kb_dir, sorted(files)[0])
            
    script_sentences = 0
    if script_file:
        c = open(script_file, encoding='utf-8').read()
        # count dialogue items
        # AMBER EYES scripts have lines like `1.01`, `1.02` or `**HOST**:`
        # In parse_kichban.py, each turn is split into sentences
        dialogue_turns = re.findall(r'(?:\*\*(?:HOST|ĐIỀU TRA VIÊN|CHUYÊN GIA TÂM LÝ|[^\*]+)\*\*|`\d+\.\d+`):?\s*([^\n]+)', c)
        # Or count lines starting with character names
        dialogue_lines = [l for l in c.splitlines() if any(l.strip().startswith(role) for role in ['**HOST', '**ĐIỀU TRA', '**CHUYÊN GIA', '**CÚ', '**SÓI', '**CÁO', '**N1', '**N2', '**NGƯỜI'])]
        
        # Also check if plan has explicit count:
        m_plan = re.search(r'\|\s*(?:Lượt nói\s*/\s*)?câu(?:\s*/\s*từ)?\s*\|\s*.*?(\d+)\s+câu', plan_text)
        if not m_plan:
            m_plan = re.search(r'\*\*(\d+)\s+câu(?:\s+thoại)?\*\*', plan_text)
        if not m_plan:
            m_plan = re.search(r'(\d+)\s+câu thoại', plan_text)
            
        if m_plan:
            return int(m_plan.group(1))
        elif dialogue_lines:
            # roughly dialogue turns or lines
            return len(dialogue_lines)
            
    if m:
        return int(m.group(1))
    return 0

results = []
for ep in range(1, 69):
    ep_str = f'Tap{ep:02d}'
    p = f'02_SAN_XUAT/{ep_str}/KeHoach_Video_{ep_str}.md'
    txt = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    
    # Title
    t = ''
    m = re.search(r'# HỒ SƠ SẢN XUẤT TẬP \d+ [·\-] [\"“](.+?)[\"”]', txt)
    if m: t = m.group(1).strip()
    if not t:
        m = re.search(r'# HỒ SƠ SẢN XUẤT TẬP \d+ [·\-] ([^\n\(\)]+)', txt)
        if m: t = m.group(1).strip()
    if not t:
        m = re.search(r'\*\*Tên tập\*\*\s*\|\s*([^\|\n]+)', txt)
        if m: t = m.group(1).strip()
    if not t:
        m = re.search(r'\|\s*Tên tập\s*\|\s*([^\|\n]+)', txt)
        if m: t = m.group(1).strip()
    if not t:
        m = re.search(r'#\s*TẬP\s*\d+[:\s\-\–]+([^\n]+)', txt)
        if m: t = m.group(1).strip()
        
    # Topic
    v = ''
    m = re.search(r'\*\*Đề tài\*\*\s*\|\s*([^\|\n]+)', txt)
    if m: v = m.group(1).strip()
    if not v:
        m = re.search(r'\|\s*Đề tài\s*\|\s*([^\|\n]+)', txt)
        if m: v = m.group(1).strip()
    if not v:
        m = re.search(r'\|\s*Vụ án\s*\|\s*([^\|\n]+)', txt)
        if m: v = m.group(1).strip()
    if not v:
        m = re.search(r'\*\*Vụ án\*\*\s*\|\s*([^\|\n]+)', txt)
        if m: v = m.group(1).strip()
        
    country = get_country(t + ' ' + v + ' ' + txt[:2000])
    sents = get_sentences_count(ep, txt)
    imgs = get_generated_images_count(ep)
    shots = get_shots_rule_count(ep, txt)
    
    results.append({
        'ep': ep,
        'title': t,
        'topic': v,
        'country': country,
        'sentences': sents,
        'images': imgs,
        'shots': shots
    })

open('.work/_episodes_data.json', 'w', encoding='utf-8').write(json.dumps(results, ensure_ascii=False, indent=2))
print(f'Done processing {len(results)} episodes!')
