# -*- coding: utf-8 -*-
"""AUDIT: soát lại bảng SFX Tap03-29.
1) Parity kịch bản VN vs EN (cùng số cue? cùng nội dung?).
2) Mọi âm thanh nằm trong cue [BGM] và [Nghỉ] — có file nào đáp ứng?
3) Marker SFX không đúng chuẩn (bị parser bỏ sót).
"""
import os, re, sys, json, glob
sys.path.insert(0, r'D:\TEST\Gax\Audi\.work')
from _sfx_analysis import DATA, ROOT
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

KB = os.path.join(ROOT, '01_KICH_BAN')

def find_script(ep, en=False):
    d = os.path.join(KB, f'Tap{ep:02d}')
    cands = [f for f in glob.glob(os.path.join(d, '*.md'))
             if not re.search(r'ban_goc|truoc_review|REVIEW', os.path.basename(f))]
    if en:
        c = [f for f in cands if '_EN' in os.path.basename(f)]
    else:
        c = [f for f in cands if '_EN' not in os.path.basename(f)]
    return sorted(c)[0] if c else None

def cues(path):
    out = {'SFX': [], 'BGM': [], 'NGHI': []}
    if not path: return out
    for ln in open(path, encoding='utf-8').read().splitlines():
        s = ln.strip()
        m = re.match(r'^\*\*\[(SFX|BGM)\]:\*\*\s*(.*)', s)
        if m: out[m.group(1)].append(m.group(2)); continue
        m = re.match(r'^\*\*\[(?:Nghỉ ([\d.]+) giây|Pause ([\d.]+) seconds?)(.*?)\]\*\*', s)
        if m:
            d = (m.group(3) or '').strip(' –-')
            if d: out['NGHI'].append(d)
    return out

print('=' * 96)
print('A) PARITY KỊCH BẢN VN vs EN — Tap03..Tap29')
print('=' * 96)
print(f'{"Tập":<6}{"VN SFX":>8}{"EN SFX":>8}{"VN BGM":>8}{"EN BGM":>8}  trạng thái')
mismatch = []
for ep in range(3, 30):
    vn, en = cues(find_script(ep)), cues(find_script(ep, True))
    ok = (len(vn['SFX']) == len(en['SFX']) and len(vn['BGM']) == len(en['BGM']))
    st = 'khớp' if ok else '*** LỆCH ***'
    if not ok: mismatch.append(ep)
    print(f'{ep:<6}{len(vn["SFX"]):>8}{len(en["SFX"]):>8}{len(vn["BGM"]):>8}{len(en["BGM"]):>8}  {st}')
print(f'\nTập lệch: {mismatch if mismatch else "không có — bản EN dùng CHUNG bảng SFX với bản VN"}')

print()
print('=' * 96)
print('B) ÂM THANH NẰM TRONG CUE [BGM] VÀ [Nghỉ] — kiểm tra có file đáp ứng')
print('=' * 96)
assigned = {ep: set(f for r in rows for f in r[3]) for ep, rows in DATA.items()}

# Từ khoá âm thanh môi trường cụ thể (không phải nhạc đơn thuần)
KEY = re.compile(r'gió|mưa|sóng|biển|tiếng tim|tích tắc|đồng hồ|quạt|gió rít|rè rè|tiếng động cơ|'
                 r'côn trùng|chim|tiếng bước chân|thở|tích tắc|chính xác', re.I)
gaps = []
for ep in range(3, 30):
    c = cues(find_script(ep))
    files = assigned.get(ep, set())
    hits = []
    for d in c['BGM']:
        if KEY.search(d): hits.append(('BGM', d))
    for d in c['NGHI']:
        hits.append(('NGHI', d))
    if hits:
        print(f'\n--- Tập {ep:02d} ---')
        print(f'   file đã gán: {", ".join(sorted(files)) or "(không có)"}')
        for kind, d in hits:
            print(f'   [{kind}] {d[:150]}')
            gaps.append((ep, kind, d))
print(f'\nTổng cue BGM/NGHI có âm thanh cụ thể cần đối chiếu: {len(gaps)}')
