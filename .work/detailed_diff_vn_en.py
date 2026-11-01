import sys
sys.path.append('.work')
from parse_kichban import parse_file

vn = parse_file('01_KICH_BAN/Tap04/kichban_tap04_23102026.md')
en = parse_file('01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md')

with open('.work/all_elements_vn_en.txt', 'w', encoding='utf-8') as out:
    out.write(f"Elements: VN {len(vn)}, EN {len(en)}\n")

    for i in range(max(len(vn), len(en))):
        v = vn[i] if i < len(vn) else {}
        e = en[i] if i < len(en) else {}
        
        v_id = v.get('element_id', str(i+1))
        e_id = e.get('element_id', str(i+1))
        
        v_s = v.get('sentences', [])
        e_s = e.get('sentences', [])
        
        v_role = v.get('role')
        e_role = e.get('role')
        
        out.write(f"\n==========================================\n")
        out.write(f"ELEMENT {i+1} | ID: VN {v_id} / EN {e_id} | Role: VN {v_role} / EN {e_role}\n")
        out.write(f"VN sentences ({len(v_s)}):\n")
        for s_idx, s in enumerate(v_s):
            out.write(f"  [VN {s_idx+1}] {s}\n")
        out.write(f"EN sentences ({len(e_s)}):\n")
        for s_idx, s in enumerate(e_s):
            out.write(f"  [EN {s_idx+1}] {s}\n")
print("Done writing to .work/all_elements_vn_en.txt")
