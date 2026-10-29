import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/shots_t05.json', 'r', encoding='utf-8') as f:
    shots = json.load(f)['shots']

with open('.work/timeline_s_t05.json', 'r', encoding='utf-8') as f:
    tl = {it.get('id'): it for it in json.load(f)['items']}

# Let's inspect all shots where sentence topics might diverge from image/text
print("KIỂM TRA TẤT CẢ CÁC SHOT TRONG 5 HỒI ĐỂ TÌM BẤT KỲ SỰ LỆCH PHA NÀO KHÁC:")
print("="*80)

for s in shots:
    sid = s['id']
    bg = s['bg']
    cues = s['sentences']
    if not cues:
        continue
    
    # Check text elems
    screen_texts = []
    for seg in s.get('segments', []):
        for el in seg.get('elems', []):
            if len(el) >= 2:
                screen_texts.append(el[1])
                
    spoken_texts = [f"{c}: {tl.get(c, {}).get('text')}" for c in cues]
    
    # Print out shot summary
    print(f"\n[Shot {sid}] BG: {bg}")
    print(f"  Chữ: {' | '.join(screen_texts)}")
    print(f"  Thoại: {' || '.join(spoken_texts)}")
