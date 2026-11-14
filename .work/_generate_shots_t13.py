import json
from pathlib import Path

# Load scripts and bg jobs
sc_vi = json.load(open('.work/script_tap13.json', encoding='utf-8'))
sc_en = json.load(open('.work/script_tap13_EN.json', encoding='utf-8'))
sc_ja = json.load(open('.work/script_tap13_JA.json', encoding='utf-8'))
old_jobs = json.load(open('.work/bg_jobs_tap13.json', encoding='utf-8'))

from collections import defaultdict
elem_to_jobs = defaultdict(list)
for j in old_jobs:
    elem = j['sentences'].split('#')[0]
    elem_to_jobs[elem].append(j)

# Build sentence to background mapping
sent_to_bg = {}
for e in sc_vi:
    if 'sentences' not in e or not e['sentences']:
        continue
    eid = e['id']
    sents = [s['id'] for s in e['sentences']]
    jobs = elem_to_jobs[eid]
    n_s = len(sents)
    n_j = len(jobs)
    
    idx = 0
    for i in range(n_j):
        sz = n_s // n_j + (1 if i < (n_s % n_j) else 0)
        chunk = sents[idx : idx + sz]
        idx += sz
        for sid in chunk:
            sent_to_bg[sid] = jobs[i]['name']

print(f"Total mapped sentences: {len(sent_to_bg)}")

# Load timelines
tl_vi = json.load(open('.work/timeline_s_t13.json', encoding='utf-8'))
tl_en = json.load(open('.work/timeline_s_EN_t13.json', encoding='utf-8'))
tl_ja = json.load(open('.work/timeline_s_JA_t13.json', encoding='utf-8'))

# Act titles for T10
ACT_TITLES_VI = {
    2: ("HỒI 02", "ĐÊM KINH HOÀNG TẠI ĐẠI LỘ HELEN VÀ CUỘC GỌI 911"),
    3: ("HỒI 03", "GIẢI MÃ TÂM LÝ: TỪ 'CHA MẸ HỔ' ĐẾN HỘI CHỨNG NÓI DỐI BỆNH LÝ"),
    4: ("HỒI 04", "ĐẤU TRÍ PHÒNG THẨM VẤN & SỰ THỨC TỈNH CỦA NGƯỜI CHA"),
    5: ("HỒI 05", "BẢN ÁN LƯƠNG TÂM & LỜI CẢNH TỈNH")
}

ACT_TITLES_EN = {
    2: ("ACT 02", "HORROR ON HELEN AVENUE AND THE 911 CALL"),
    3: ("ACT 03", "PSYCHOLOGICAL DECODING: FROM TIGER PARENTING TO PATHOLOGICAL LYING"),
    4: ("ACT 04", "THE INTERROGATION CHESS MATCH & A FATHER'S AWAKENING"),
    5: ("ACT 05", "VERDICT OF CONSCIENCE & SURVIVAL RED FLAGS")
}

ACT_TITLES_JA = {
    2: ("第02幕", "ヘレン通りの惨劇と911通報の真相"),
    3: ("第03幕", "心理解剖：タイガー・マザーの呪縛と虚言癖の罠"),
    4: ("第04幕", "取調室の攻防と奇跡的に目覚めた父親の告発"),
    5: ("第05幕", "良心の審判と生存のための赤い警告")
}

CAMERAS = ['pan', 'pull', 'still', 'push']

def generate_shots(lang):
    if lang == 'vi':
        tl = tl_vi
        sc = sc_vi
        act_titles = ACT_TITLES_VI
        t2_title = "HỒ SƠ TẬP 13 · ĐÃ ĐÓNG"
        t2_sub = "AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật"
    elif lang == 'en':
        tl = tl_en
        sc = sc_en
        act_titles = ACT_TITLES_EN
        t2_title = "EPISODE 13 DOSSIER · CLOSED"
        t2_sub = "AMBER EYES · Criminal Psychology Through True Case Files"
    else:
        tl = tl_ja
        sc = sc_ja
        act_titles = ACT_TITLES_JA
        t2_title = "第13話 事件記録 · 終結"
        t2_sub = "AMBER EYES · 実際の事件記録から読み解く犯罪心理学"
        
    sent_dict = {it['id']: it for it in tl['items']}
    
    shots = []
    cam_idx = 0
    
    # Process by act
    for act_num in range(1, 6):
        act_items = [it for it in tl['items'] if it['act'] == act_num]
        
        for idx_in_act, it in enumerate(act_items, 1):
            sid = it['id']
            eid = it['element']
            role = it['role']
            text = it['text']
            
            # Shot id
            shot_id = f"{act_num}-{idx_in_act:02d}"
            
            # Start and end
            # Rule: shot 1-01 starts at 22.8s
            if shot_id == "1-01":
                s_start = 22.8
            else:
                s_start = it['start'] - 0.2
                
            # If next item in same act
            if idx_in_act < len(act_items):
                next_it = act_items[idx_in_act]
                s_end = next_it['start'] - 0.2
            else:
                # Last item in act ends at act boundary or item end
                s_end = it['end']
                
            # Background
            bg_name = sent_to_bg[sid]
            
            # Template & variant
            template = 'T1'
            variant = ''
            elem_kind = 'ital'
            
            if eid in ('1.07', '4.06'):
                template = 'T4'
                variant = 'testimony'
            elif sid in ('5.05#2', '5.05#6', '5.05#10', '5.05#14'):
                template = 'T8'
                variant = 'flags'
                
            # Segments
            if template == 'T8':
                flag_num_str = {
                    '5.05#2': '01',
                    '5.05#6': '02',
                    '5.05#10': '03',
                    '5.05#14': '04'
                }[sid]
                segments = [{'at_sentence': None, 'elems': [['ital', flag_num_str], ['bold', text.upper()]]}]
            else:
                segments = [{'at_sentence': None, 'elems': [[elem_kind, text]]}]
                
            cam = CAMERAS[cam_idx % len(CAMERAS)]
            cam_idx += 1
            
            shot_obj = {
                'id': shot_id,
                'act': act_num,
                'start': round(s_start, 3),
                'end': round(s_end, 3),
                'role': role,
                'sentences': [sid],
                'template': template,
                'variant': variant,
                'bg': bg_name,
                'bg2': None,
                'inset': None,
                'camera': cam,
                'segments': segments,
                'beats': [],
                'beat_text': '—',
                'flags': {
                    'bust': False,
                    'nobust': False,
                    'intro': (shot_id == '1-01'),
                    'handoff': [],
                    'dual': False,
                    'guests': False,
                    'p2': False
                },
                'hold': False,
                'transition': 'dissolve'
            }
            shots.append(shot_obj)
            
        # Add T10 if act < 5
        if act_num < 5:
            t10_id = f"{act_num}-{len(act_items)+1:02d}"
            # ACT marker
            act_m = [m for m in tl['markers'] if m['type'] == 'ACT' and m.get('act') == act_num + 1][0]
            t10_start = act_m['start']
            t10_end = act_m['end']
            
            # Segments for T10
            t10_act_str, t10_title_str = act_titles[act_num + 1]
            t10_segs = [{'at_sentence': None, 'elems': [['ital', t10_act_str], ['bold', t10_title_str]]}]
            
            t10_shot = {
                'id': t10_id,
                'act': act_num,
                'start': round(t10_start, 3),
                'end': round(t10_end, 3),
                'role': None,
                'sentences': [],
                'template': 'T10',
                'variant': '',
                'bg': 'void',
                'bg2': None,
                'inset': None,
                'camera': 'still',
                'segments': t10_segs,
                'beats': [],
                'beat_text': '—',
                'flags': {
                    'bust': False,
                    'nobust': True,
                    'intro': False,
                    'handoff': [],
                    'dual': False,
                    'guests': False,
                    'p2': False
                },
                'hold': False,
                'transition': 'dip'
            }
            shots.append(t10_shot)
            
    # Add T2 at the very end
    last_act_items = [it for it in tl['items'] if it['act'] == 5]
    t2_id = f"5-{len(last_act_items)+1:02d}"
    last_shot = shots[-1]
    t2_start = last_shot['end']
    t2_end = tl['total']
    
    t2_segs = [{'at_sentence': None, 'elems': [['bold', t2_title], ['ital', t2_sub]]}]
    t2_shot = {
        'id': t2_id,
        'act': 5,
        'start': round(t2_start, 3),
        'end': round(t2_end, 3),
        'role': None,
        'sentences': [],
        'template': 'T2',
        'variant': '',
        'bg': 't13_amber_eyes_closing_dossier_jennifer',
        'bg2': None,
        'inset': None,
        'camera': 'still',
        'segments': t2_segs,
        'beats': [],
        'beat_text': '—',
        'flags': {
            'bust': False,
            'nobust': True,
            'intro': False,
            'handoff': [],
            'dual': False,
            'guests': False,
            'p2': False
        },
        'hold': False,
        'transition': 'dip'
    }
    shots.append(t2_shot)
    
    # Continuity fix: ensure each shot start exactly matches previous shot end
    for i in range(len(shots) - 1):
        shots[i]['end'] = shots[i+1]['start']
        
    return {
        'total': tl['total'],
        'shots': shots
    }

for lang in ('vi', 'en', 'ja'):
    res = generate_shots(lang)
    if lang == 'vi':
        out_name = '.work/shots_t13.json'
    elif lang == 'en':
        out_name = '.work/shots_EN_t13.json'
    else:
        out_name = '.work/shots_JA_t13.json'
    with open(out_name, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print(f"Saved {out_name}: shots={len(res['shots'])}, total={res['total']}")
