import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/shots_t06.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
shots = data['shots']

with open('.work/timeline_s_t06.json', 'r', encoding='utf-8') as f:
    tl = json.load(f)

items_by_id = {}
for it in tl['items']:
    cid = it.get('cue_id') or it.get('id', '')
    if cid:
        items_by_id[cid] = it

print(f"Total parsed shots: {len(shots)}")

key_shots = ['1-10', '1-11', '1-12', '1-13', '1-14', '1-15', '1-16', 
             '2-06', '2-07', '2-08', '2-09', '2-13', '2-14', '2-15',
             '3-03', '3-04', '3-05', '3-06', '3-07']

for s in shots:
    sid = s.get('id')
    if sid in key_shots:
        start = s.get('start', 0)
        end = s.get('end', 0)
        dur = end - start
        bg = s.get('bg')
        cues = s.get('sentences', [])
        print(f"\n[{sid}] ({start:.2f}s -> {end:.2f}s, dur {dur:.2f}s)")
        print(f"  BG: {bg}")
        print(f"  Cues: {cues}")
        spoken_parts = []
        for c in cues:
            if c in items_by_id:
                spoken_parts.append(f"[{c}] {items_by_id[c]['text']}")
        for sp in spoken_parts:
            print(f"    * {sp}")
