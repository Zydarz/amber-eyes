import sys
sys.path.append('.work')
from parse_kichban import parse_file

vn = parse_file('01_KICH_BAN/Tap04/kichban_tap04_23102026.md')
en = parse_file('01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md')

with open('.work/script_diff_analysis.txt', 'w', encoding='utf-8') as out:
    for i in range(len(vn)):
        v = vn[i]
        e = en[i]
        v_s = v.get('sentences', [])
        e_s = e.get('sentences', [])
        v_role = v.get('role')
        e_role = e.get('role')
        v_raw = v.get('raw', '')
        e_raw = e.get('raw', '')
        
        # Compare
        diff_flag = False
        reasons = []
        if len(v_s) != len(e_s):
            diff_flag = True
            reasons.append(f"Sentence count mismatch: VN {len(v_s)} vs EN {len(e_s)}")
        if v_role != e_role:
            diff_flag = True
            reasons.append(f"Role mismatch: VN {v_role} vs EN {e_role}")
            
        out.write(f"--- Element {i+1} (VN sentences: {len(v_s)}, EN: {len(e_s)}) ---\n")
        out.write(f"Role: VN={v_role}, EN={e_role}\n")
        if reasons:
            out.write("MISMATCH: " + "; ".join(reasons) + "\n")
        out.write("VN:\n")
        for s in v_s:
            out.write(f"  - {s}\n")
        out.write("EN:\n")
        for s in e_s:
            out.write(f"  - {s}\n")
        out.write("\n")
print("Analysis written to .work/script_diff_analysis.txt")
