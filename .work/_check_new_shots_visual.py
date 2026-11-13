import json
from pathlib import Path

shots = json.loads(Path('.work/shots_t10.json').read_text(encoding='utf-8'))['shots']
target_sents = [
    '1.02#7', '1.02#8', '1.02#9', '1.02#10',
    '2.04#5', '2.04#6', '2.04#7', '2.04#8',
    '2.06#5', '2.06#6', '2.06#7', '2.06#8',
    '3.07#6', '3.07#7', '3.07#8',
    '3.08#5', '3.08#6', '3.08#7',
    '4.03#4', '4.03#5', '4.03#6',
    '4.04#2',
    '4.05#6', '4.05#7', '4.05#8',
    '4.09#3', '4.09#4', '4.09#5',
    '4.10#5',
    '5.03#4',
    '5.04#4', '5.04#5'
]

print("=== KIEM TRA ANH NEN & CAMERA CUA 32 CAU THOAI MOI ===\n")
matched_shots = []
for s in shots:
    matched = [sid for sid in s.get('sentences', []) if sid in target_sents]
    if matched:
        matched_shots.append(s)
        txt = s['segments'][0]['elems'][0][1] if s['segments'] and s['segments'][0]['elems'] else ''
        dur = s['end'] - s['start']
        print(f"Shot {s['id']} ({s.get('role')} - {dur:.1f}s): {matched}")
        print(f"   Nền: {s['bg']} | Cam: {s['camera']} | Mẫu: {s['template']}")
        print(f"   Chữ: {txt[:75]}...\n")

print(f"Total matched shots: {len(matched_shots)}")
