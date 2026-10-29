import json
import re

import sys
sys.path.insert(0, ".work")
import parse_kichban as PK

src_vi = open("01_KICH_BAN/Tap04/kichban_tap04_23102026.md", encoding="utf-8").readlines()
src_en = open("01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md", encoding="utf-8").readlines()

els_vi = PK.parse_lines(src_vi)
els_en = PK.parse_lines(src_en)

print(f"Elements: VI = {len(els_vi)}, EN = {len(els_en)}")

s_vi = [s for e in els_vi if e["kind"] == "LOI" for s in e["sentences"]]
s_en = [s for e in els_en if e["kind"] == "LOI" for s in e["sentences"]]
print(f"Sentences: VI = {len(s_vi)}, EN = {len(s_en)}")

# So sánh từng element
for i in range(max(len(els_vi), len(els_en))):
    e_v = els_vi[i] if i < len(els_vi) else None
    e_e = els_en[i] if i < len(els_en) else None
    id_v = e_v["id"] if e_v else "N/A"
    id_e = e_e["id"] if e_e else "N/A"
    kind_v = e_v["kind"] if e_v else "N/A"
    kind_e = e_e["kind"] if e_e else "N/A"
    role_v = e_v.get("role") if e_v else "N/A"
    role_e = e_e.get("role") if e_e else "N/A"
    cnt_v = len(e_v.get("sentences", [])) if e_v else 0
    cnt_e = len(e_e.get("sentences", [])) if e_e else 0

    if id_v != id_e or kind_v != kind_e or role_v != role_e or cnt_v != cnt_e:
        print(f"Diff at index {i}: VI({id_v}, {kind_v}, {role_v}, {cnt_v} sents) vs EN({id_e}, {kind_e}, {role_e}, {cnt_e} sents)")
