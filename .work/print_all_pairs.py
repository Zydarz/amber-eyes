import sys
sys.path.append('.work')
from parse_kichban import parse_file

vn = parse_file('01_KICH_BAN/Tap04/kichban_tap04_23102026.md')
en = parse_file('01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md')

print(f"Total elements: {len(vn)}")
for idx, (v, e) in enumerate(zip(vn, en)):
    vs = v.get('sentences', [])
    es = e.get('sentences', [])
    if not vs and not es:
        # Check sfx/bgm
        vr = v.get('raw', '').strip()
        er = e.get('raw', '').strip()
        if vr != er:
            print(f"Elem {idx+1} [Non-dialogue]:\n  VN: {vr}\n  EN: {er}")
    else:
        # Compare dialogue
        print(f"Elem {idx+1} [{v.get('role')}]: VN({len(vs)}) vs EN({len(es)})")
        for i in range(max(len(vs), len(es))):
            v_line = vs[i] if i < len(vs) else "[MISSING IN VN]"
            e_line = es[i] if i < len(es) else "[MISSING IN EN]"
            print(f"  ({i+1}) VN: {v_line}")
            print(f"      EN: {e_line}")
