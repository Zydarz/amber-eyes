import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/shots_t05.json', 'r', encoding='utf-8') as f:
    shots = json.load(f)['shots']

with open('.work/timeline_s_t05.json', 'r', encoding='utf-8') as f:
    tl = {it.get('id'): it for it in json.load(f)['items']}

print("KIỂM TRA TỪNG HỒI:")

with open('.work/_audit_by_act.txt', 'w', encoding='utf-8') as out:
    def audit_act(act_num):
        out.write(f"\n==================== HỒI {act_num} ====================\n")
        act_shots = [s for s in shots if s['act'] == act_num and s['sentences']]
        for s in act_shots:
            sid = s['id']
            bg = s['bg']
            screen = []
            for seg in s.get('segments', []):
                for el in seg.get('elems', []):
                    if len(el) >= 2:
                        screen.append(el[1])
            cues = s['sentences']
            spoken = [f"[{c}] {tl.get(c, {}).get('text')}" for c in cues]
            out.write(f"\n[{sid}] BG: {bg} | Sentences: {cues}\n")
            out.write(f"  CHỮ: {' // '.join(screen)}\n")
            for sp in spoken:
                out.write(f"  THOẠI: {sp}\n")

    for a in range(1, 6):
        audit_act(a)

