import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/shots_t05.json', 'r', encoding='utf-8') as f:
    shots = json.load(f)['shots']

with open('.work/timeline_s_t05.json', 'r', encoding='utf-8') as f:
    tl = {it.get('id'): it for it in json.load(f)['items']}

print("KIỂM TRA SO KHỚP TỪ VỰNG GIỮA LỜI THOẠI VÀ CHỮ TRÊN HÌNH:")
print("="*80)

def word_overlap(text1, text2):
    w1 = set(w.lower() for w in text1.split() if len(w) > 2)
    w2 = set(w.lower() for w in text2.split() if len(w) > 2)
    overlap = w1.intersection(w2)
    return len(overlap), overlap

for s in shots:
    sid = s['id']
    cues = s['sentences']
    if not cues:
        continue
    screen_texts = []
    for seg in s.get('segments', []):
        for el in seg.get('elems', []):
            if len(el) >= 2:
                screen_texts.append(el[1])
    screen_str = " ".join(screen_texts)
    spoken_str = " ".join([tl.get(c, {}).get('text', '') for c in cues])
    
    count, common = word_overlap(screen_str, spoken_str)
    # If overlap is very small, print it
    if count < 2:
        print(f"\n[CẢNH BÁO KHỚP TỪ THẤP] Shot {sid} (Act {s['act']}) | BG: {s['bg']}")
        print(f"  Cues: {cues}")
        print(f"  Chữ trên hình: {screen_str}")
        print(f"  Lời thoại:     {spoken_str}")
        print(f"  Từ trùng ({count}): {common}")
