# Trích xuất mọi cue SFX / BGM / NGHI từ kịch bản Tap03..Tap29, kèm mã element chuẩn.
# Dùng đúng logic đếm element của parse_kichban.py để mã cue khớp bảng âm thanh sfx_tapXX.json.
import re, json, os, glob, sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = r'D:\TEST\Gax\Audi'
KB = os.path.join(ROOT, '01_KICH_BAN')
OUT = os.path.join(ROOT, '.work', 'sfx_cues_tap03_29.json')

ROLES = {'HOST':'H','NGƯỜI BÌNH THƯỜNG':'N','ĐIỀU TRA VIÊN':'D','CHUYÊN GIA TÂM LÝ':'C',
         'ORDINARY PERSON':'N','INVESTIGATOR':'D','PSYCHOLOGIST':'C',
         'ĐẶC VỤ FBI':'D','CẢNH SÁT ĐỊA PHƯƠNG':'N'}

def script_path(ep):
    d = os.path.join(KB, f'Tap{ep:02d}')
    cands = [f for f in glob.glob(os.path.join(d, 'kichban_tap*.md'))
             if not re.search(r'ban_goc|truoc_review|REVIEW|_EN', os.path.basename(f))]
    return sorted(cands)[0] if cands else None

def parse(path):
    src = open(path, encoding='utf-8').read().splitlines()
    act = 0; n = 0; els = []; cur = None
    def new(kind, **kw):
        nonlocal n
        n += 1
        e = dict(id=f'{act}.{n:02d}', act=act, kind=kind, **kw)
        els.append(e); return e
    for line in src:
        s = line.strip()
        m = re.match(r'^## (?:HỒI|ACT) (\d)', s)
        if m:
            act = int(m.group(1)); n = 0; cur = None
            els.append(dict(id=f'--H{act}', act=act, kind='HOI', title=s[3:].strip()))
            continue
        if act == 0 or not s or s == '---':
            continue
        m = re.match(r'^\*\*(' + '|'.join(ROLES) + r')\*\*\s*(?:\*\((.*?)\)\*)?\s*:', s)
        if m:
            cur = dict(role=ROLES[m.group(1)], direction=m.group(2) or ''); continue
        m = re.match(r'^\*\*\[(SFX|BGM)\]:\*\*\s*(.*)', s)
        if m:
            new(m.group(1), desc=m.group(2)); continue
        m = re.match(r'^\*\*\[(?:Nghỉ ([\d.]+) giây|Pause ([\d.]+) seconds?)(.*?)\]\*\*', s)
        if m:
            new('NGHI', sec=float(m.group(1) or m.group(2)), desc=(m.group(3) or '').strip(' –-')); continue
        if cur is None: continue
        t = re.sub(r'^\*\s+', '', s); t = re.sub(r'^\d+\.\s+', '', t)
        t = t.replace('**', '').replace('*', '').strip().strip('"“”').strip()
        if not t: continue
        if els and els[-1]['kind'] == 'LOI' and els[-1]['role'] == cur['role'] and els[-1].get('_open'):
            els[-1]['paras'].append(t)
        else:
            e = new('LOI', role=cur['role'], direction=cur['direction'], paras=[t], _open=True)
    for i, e in enumerate(els):
        if e['kind'] != 'LOI' and i > 0 and els[i-1]['kind'] == 'LOI': els[i-1]['_open'] = False
    return els

def merge_cue_continuations(els, raw_lines):
    """Gộp dòng SFX/BGM bị ngắt nối tiếp (dòng sau không phải element mới)."""
    return els

result = {}
for ep in range(3, 30):
    p = script_path(ep)
    if not p:
        print(f'Tap{ep:02d}: KHONG CO KICH BAN'); continue
    raw = open(p, encoding='utf-8').read().splitlines()
    els = parse(p)
    # gộp cue nhiều dòng
    i = 0
    merged = []
    while i < len(els):
        e = els[i]
        if e['kind'] in ('SFX', 'BGM') and e.get('desc', '').endswith(('-', ',', 'và', 'rồi', 'kèm')):
            j = i + 1
            while j < len(els) and els[j]['kind'] in ('SFX', 'BGM'):
                e['desc'] = (e['desc'] + ' ' + els[j].get('desc', '')).strip()
                j += 1
            merged.append(e); i = j; continue
        merged.append(e); i += 1
    els = merged

    title = ''
    for ln in raw:
        m = re.search(r'\*\*Tên tập \(Episode Title\)\*\*\s*\|\s*(.+?)\s*\|', ln)
        if m: title = m.group(1).strip()
    bgm_hint = ''
    for ln in raw:
        m = re.search(r'\*\*Nhạc nền \(BGM\) gợi ý\*\*\s*\|\s*(.+?)\s*\|\s*$', ln)
        if m: bgm_hint = m.group(1).strip()
    acts = [e['title'] for e in els if e['kind'] == 'HOI']
    sfx = [dict(id=e['id'], act=e['act'], desc=e['desc']) for e in els if e['kind'] == 'SFX']
    bgm = [dict(id=e['id'], act=e['act'], desc=e['desc']) for e in els if e['kind'] == 'BGM']
    nghi = [dict(id=e['id'], act=e['act'], sec=e.get('sec'), desc=e.get('desc', '')) for e in els if e['kind'] == 'NGHI']
    nghi_sound = [g for g in nghi if g['desc']]
    result[f'{ep:02d}'] = dict(file=os.path.basename(p), title=title, bgm_hint=bgm_hint,
                               acts=acts, sfx=sfx, bgm=bgm, nghi=nghi_sound,
                               n_loi=sum(1 for e in els if e['kind'] == 'LOI'))
    print(f'Tap{ep:02d}: SFX={len(sfx):2d} BGM={len(bgm):2d} NGHI(có mô tả)={len(nghi_sound):2d} | {title[:70]}')

json.dump(result, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\nGhi:', OUT)
