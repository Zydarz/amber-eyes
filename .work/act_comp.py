import sys
sys.path.append('.work')
from parse_kichban import parse_file

vn = parse_file('01_KICH_BAN/Tap04/kichban_tap04_23102026.md')
en = parse_file('01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md')

# Read raw files to get headers and act divisions
with open('01_KICH_BAN/Tap04/kichban_tap04_23102026.md', encoding='utf-8') as f:
    vn_text = f.read()

with open('01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md', encoding='utf-8') as f:
    en_text = f.read()

# Let's inspect differences element by element
out_lines = []
for idx, (v, e) in enumerate(zip(vn, en)):
    vs = v.get('sentences', [])
    es = e.get('sentences', [])
    vr = v.get('role')
    er = e.get('role')
    
    out_lines.append(f"\n=======================================================")
    out_lines.append(f"ELEMENT {idx+1} [Role: VN={vr}, EN={er}] (VN={len(vs)} sentences, EN={len(es)} sentences)")
    
    if not vs and not es:
        v_raw = v.get('raw', '').strip()
        e_raw = e.get('raw', '').strip()
        out_lines.append(f"  [VN-RAW]: {v_raw}")
        out_lines.append(f"  [EN-RAW]: {e_raw}")
    else:
        for i in range(max(len(vs), len(es))):
            v_line = vs[i] if i < len(vs) else "[TRỐNG TRONG VN]"
            e_line = es[i] if i < len(es) else "[TRỐNG TRONG EN]"
            out_lines.append(f"  [{i+1}]")
            out_lines.append(f"    VN: {v_line}")
            out_lines.append(f"    EN: {e_line}")

with open('.work/act_comparison.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))

print("Dumped comparison to .work/act_comparison.txt")
