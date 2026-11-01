import sys
sys.path.append('.work')
from parse_kichban import parse_file

vn = parse_file('01_KICH_BAN/Tap04/kichban_tap04_23102026.md')
en = parse_file('01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md')

with open('.work/compare_vn_en_tap04.txt', 'w', encoding='utf-8') as f:
    for i, (v, e) in enumerate(zip(vn, en)):
        v_s = v.get('sentences', [])
        e_s = e.get('sentences', [])
        r_v = v.get('role')
        r_e = e.get('role')
        f.write(f"=== Element {i+1} [Role: {r_v} / {r_e}] (VN: {len(v_s)}, EN: {len(e_s)}) ===\n")
        f.write("--- VN ---\n")
        for idx, s in enumerate(v_s):
            f.write(f"  [{idx+1}] {s}\n")
        f.write("--- EN ---\n")
        for idx, s in enumerate(e_s):
            f.write(f"  [{idx+1}] {s}\n")
        f.write("\n")
print("Done dumping")
