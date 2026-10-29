import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/shots_t05.json', 'r', encoding='utf-8') as f:
    shots = json.load(f)['shots']

with open('.work/timeline_s_t05.json', 'r', encoding='utf-8') as f:
    tl = {it.get('id'): it for it in json.load(f)['items']}

with open('.work/_alignment_dump_t05.txt', 'w', encoding='utf-8') as out_f:
    out_f.write(f"KIỂM TRA CHI TIẾT 83 SHOT (KHỚP 3 CHIỀU: ẢNH - CHỮ - LỜI THOẠI):\n")
    for i, s in enumerate(shots):
        sid = s['id']
        dur = s['end'] - s['start']
        bg = s['bg']
        tpl = s['template']
        cues = s['sentences']
        role = s['role']
        
        # Collect spoken text
        spoken = []
        for c in cues:
            it = tl.get(c)
            if it:
                spoken.append(f"[{c} {it.get('role')}]: {it.get('text')}")
            else:
                spoken.append(f"[{c}]: (pause/sfx)")
                
        # Collect screen text
        screen = []
        for seg in s.get('segments', []):
            for el in seg.get('elems', []):
                if len(el) >= 2:
                    screen.append(f"<{el[0]}>{el[1]}</{el[0]}>")
                    
        out_f.write(f"\n--- Shot {sid} ({s['start']:.1f}s -> {s['end']:.1f}s, dur {dur:.1f}s) | BG: {bg} | Tpl: {tpl} | Role: {role} ---\n")
        out_f.write(f"  CHỮ TRÊN HÌNH: {' // '.join(screen) if screen else '(không có chữ)'}\n")
        out_f.write(f"  LỜI THOẠI ĐỌC:\n")
        if spoken:
            for sp in spoken:
                out_f.write(f"    * {sp}\n")
        else:
            out_f.write(f"    * (Đoạn đệm / pause / transition)\n")

