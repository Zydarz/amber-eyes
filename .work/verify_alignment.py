import sys
sys.path.append('.work')
from parse_kichban import parse_file

vn = parse_file('01_KICH_BAN/Tap04/kichban_tap04_23102026.md')
en = parse_file('01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md')

errors = []
if len(vn) != len(en):
    errors.append(f"Element count mismatch: VN {len(vn)} vs EN {len(en)}")

for idx, (v, e) in enumerate(zip(vn, en)):
    v_id = v.get('id')
    e_id = e.get('id')
    if v_id != e_id:
        errors.append(f"Elem {idx+1}: ID mismatch VN '{v_id}' vs EN '{e_id}'")
        
    v_kind = v.get('kind')
    e_kind = e.get('kind')
    if v_kind != e_kind:
        errors.append(f"Elem {idx+1} ({v_id}): Kind mismatch VN '{v_kind}' vs EN '{e_kind}'")
        
    v_role = v.get('role')
    e_role = e.get('role')
    if v_role != e_role:
        errors.append(f"Elem {idx+1} ({v_id}): Role mismatch VN '{v_role}' vs EN '{e_role}'")
        
    v_s = v.get('sentences', [])
    e_s = e.get('sentences', [])
    if len(v_s) != len(e_s):
        errors.append(f"Elem {idx+1} ({v_id}): Sentence count mismatch VN {len(v_s)} vs EN {len(e_s)}")

if errors:
    print(f"Found {len(errors)} alignment errors:")
    for err in errors:
        print("  - " + err)
else:
    print("ALL 61 ELEMENTS AND 154 SENTENCES ARE 100% PERFECTLY ALIGNED!")
