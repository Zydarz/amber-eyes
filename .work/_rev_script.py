import json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

print("=== 1. KIỂM TRA KỊCH BẢN & PARSER ===")
sys.path.insert(0, '.work')
import parse_kichban

script_file = "01_KICH_BAN/Tap05/kichban_tap05_23102026.md"
els = parse_kichban.parse_lines(open(script_file, encoding='utf-8').read().splitlines())
print(f"Tổng số phần tử parsed: {len(els)}")

lois = [e for e in els if e['kind'] == 'LOI']
sents = [s for e in lois for s in e['sentences']]
words = sum(s['words'] for s in sents)
print(f"Số lượt thoại: {len(lois)} | Số câu thoại: {len(sents)} | Tổng số từ: {words}")

roles = {}
for e in lois:
    r = e['role']
    roles[r] = roles.get(r, 0) + len(e['sentences'])
print("Phân bổ câu theo vai:", roles)

# Check pause elements
pauses = [e for e in els if e['kind'] == 'NGHI']
print(f"Số đoạn nghỉ (NGHI): {len(pauses)}")
for p in pauses:
    print(f"  {p['id']} ({p['sec']}s): {p.get('desc')}")

# Check BGM & SFX elements
cues = [e for e in els if e['kind'] in ('BGM', 'SFX')]
print(f"Số cue BGM/SFX trong kịch bản: {len(cues)}")
for c in cues:
    print(f"  {c['id']} [{c['kind']}]: {c.get('desc')[:60]}...")
