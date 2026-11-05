# -*- coding: utf-8 -*-
"""Fix role N -> N1 and N2 in timeline_s_EN_t06.json and script_tap06_EN.json."""
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

# 1. Fix timeline_s_EN_t06.json
tl_path = ".work/timeline_s_EN_t06.json"
tl = json.load(open(tl_path, encoding="utf-8"))
fixed_tl = 0
for it in tl["items"]:
    if it["element"] == "1.09" and it["role"] == "N":
        it["role"] = "N1"
        fixed_tl += 1
    elif it["element"] == "4.04" and it["role"] == "N":
        it["role"] = "N2"
        fixed_tl += 1

with open(tl_path, "w", encoding="utf-8") as f:
    json.dump(tl, f, ensure_ascii=False, indent=2)
print(f"Fixed {fixed_tl} items in {tl_path}")

# 2. Fix script_tap06_EN.json
sc_path = ".work/script_tap06_EN.json"
sc = json.load(open(sc_path, encoding="utf-8"))
fixed_sc = 0
for el in sc:
    if el.get("id") == "1.09" and el.get("role") == "N":
        el["role"] = "N1"
        fixed_sc += 1
    elif el.get("id") == "4.04" and el.get("role") == "N":
        el["role"] = "N2"
        fixed_sc += 1

with open(sc_path, "w", encoding="utf-8") as f:
    json.dump(sc, f, ensure_ascii=False, indent=2)
print(f"Fixed {fixed_sc} elements in {sc_path}")
