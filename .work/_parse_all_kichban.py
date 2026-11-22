import sys, os, json, re
from pathlib import Path

# Add .work to path
sys.path.insert(0, '.work')
import parse_kichban

results = []

def parse_ep(ep):
    ep_str = f"Tap{ep:02d}"
    kb_dir = f"01_KICH_BAN/{ep_str}"
    if not os.path.exists(kb_dir):
        return None
    
    # Select script file
    files = os.listdir(kb_dir)
    vn_files = [f for f in files if f.endswith('.md') and not any(k in f for k in ['_EN', '_JA', '_KO', 'REVIEW', 'NghienCuu', '_cu', '_ban_goc', '_truoc_review', '_pre_directors_cut'])]
    
    if ep == 1:
        target = "kichban_tap01_22102026_v2.md"
    elif ep == 2:
        target = "kichban_tap02_22102026.md"
    elif ep == 32:
        target = "kichban_tap32_19112026.md"
    elif ep == 49:
        target = "kichban_tap49_19112026.md"
    else:
        target = sorted(vn_files)[-1]
        
    script_path = os.path.join(kb_dir, target)
    
    # Run parse_kichban
    out_json = f".work/_parsed_{ep_str}.json"
    parse_kichban.parse_file(script_path, out_json)
    
    elements = json.load(open(out_json, encoding='utf-8'))
    
    total_sentences = 0
    loi_count = 0
    bgm_count = 0
    sfx_count = 0
    words_count = 0
    
    all_sentences_list = []
    
    for elem in elements:
        kind = elem.get('kind')
        if kind == 'LOI':
            loi_count += 1
            sents = elem.get('sentences', [])
            total_sentences += len(sents)
            all_sentences_list.extend(sents)
            for s in sents:
                words_count += s.get('words', len(s.get('text', '').split()))
        elif kind == 'BGM':
            bgm_count += 1
        elif kind == 'SFX':
            sfx_count += 1
            
    # Read plan file for title / topic / country
    plan_path = f"02_SAN_XUAT/{ep_str}/KeHoach_Video_{ep_str}.md"
    plan_txt = open(plan_path, encoding='utf-8').read() if os.path.exists(plan_path) else ''
    
    # Extract Title / Topic from script content first (first line or heading)
    script_txt = open(script_path, encoding='utf-8').read()
    script_title = ''
    m = re.search(r'#\s*(.+)', script_txt)
    if m:
        script_title = m.group(1).strip()
        
    # Also check KeHoach title
    plan_title = ''
    m_p = re.search(r'# HỒ SƠ SẢN XUẤT TẬP \d+ [·\-] [\"“](.+?)[\"”]', plan_txt)
    if m_p:
        plan_title = m_p.group(1).strip()
    elif re.search(r'\*\*Tên tập\*\*\s*\|\s*([^\|\n]+)', plan_txt):
        plan_title = re.search(r'\*\*Tên tập\*\*\s*\|\s*([^\|\n]+)', plan_txt).group(1).strip()
    elif re.search(r'\|\s*Tên tập\s*\|\s*([^\|\n]+)', plan_txt):
        plan_title = re.search(r'\|\s*Tên tập\s*\|\s*([^\|\n]+)', plan_txt).group(1).strip()
        
    # Extract Topic / Case
    topic = ''
    m_t = re.search(r'\*\*Đề tài\*\*\s*\|\s*([^\|\n]+)', plan_txt)
    if m_t: topic = m_t.group(1).strip()
    elif re.search(r'\|\s*Đề tài\s*\|\s*([^\|\n]+)', plan_txt):
        topic = re.search(r'\|\s*Đề tài\s*\|\s*([^\|\n]+)', plan_txt).group(1).strip()
    elif re.search(r'\|\s*Vụ án\s*\|\s*([^\|\n]+)', plan_txt):
        topic = re.search(r'\|\s*Vụ án\s*\|\s*([^\|\n]+)', plan_txt).group(1).strip()
        
    return {
        'ep': ep,
        'ep_str': ep_str,
        'script_file': target,
        'script_title': script_title,
        'plan_title': plan_title,
        'topic': topic,
        'sentences': total_sentences,
        'dialogue_elements': loi_count,
        'bgm_elements': bgm_count,
        'sfx_elements': sfx_count,
        'words': words_count
    }

for ep in range(1, 69):
    res = parse_ep(ep)
    if res:
        results.append(res)
        print(f"Tap{res['ep']:02d}: sentences={res['sentences']}, elements={res['dialogue_elements']}, title={res['script_title'][:40]}")

open('.work/_accurate_sentences.json', 'w', encoding='utf-8').write(json.dumps(results, ensure_ascii=False, indent=2))
print('Finished parsing all 68 episodes!')
