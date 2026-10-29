import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/timeline_s_t06.json', 'r', encoding='utf-8') as f:
    tl = json.load(f)

items = tl['items']

def get_sentence_times(prefix):
    res = []
    for it in items:
        cid = it.get('cue_id') or it.get('id', '')
        if cid.startswith(prefix):
            res.append((cid, it['start'], it['end'], it.get('text', '')))
    return res

print("=== TIMELINE CHECK FOR KEY CUES ===")
for prefix in ['1.06', '1.08', '1.09', '2.06', '2.07', '2.11', '3.05', '3.07', '3.09', '3.12']:
    cues = get_sentence_times(prefix)
    for c in cues:
        print(f"[{c[0]}] {c[1]:.2f}s -> {c[2]:.2f}s (dur {c[2]-c[1]:.2f}s): {c[3][:60]}...")
