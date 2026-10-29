import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/shots_t05.json', 'r', encoding='utf-8') as f:
    shots = json.load(f)['shots']

with open('.work/timeline_s_t05.json', 'r', encoding='utf-8') as f:
    tl = {it.get('cue_id'): it for it in json.load(f)['items']}

print("CÁC SHOT CÓ THỜI LƯỢNG DÀI (> 20s):")
for s in shots:
    dur = s['end'] - s['start']
    if dur > 20.0:
        print(f"\nShot [{s['id']}] dur={dur:.2f}s | BG={s['bg']} | Template={s['template']}")
        print(f"  Sentences ({len(s['sentences'])}): {s['sentences']}")
        for c in s['sentences']:
            it = tl.get(c, {})
            print(f"    - {c} [{it.get('role')}]: {it.get('text')}")
        print("  Segments (Text on screen):")
        for seg in s.get('segments', []):
            at = seg.get('at_sentence')
            elems = seg.get('elems', [])
            print(f"    * at_sentence={at}: {elems}")
