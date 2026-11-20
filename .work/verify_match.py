# -*- coding: utf-8 -*-
import json

vn = json.load(open(".work/t32_vn.json", encoding="utf-8"))
en = json.load(open(".work/t32_en.json", encoding="utf-8"))
ja = json.load(open(".work/t32_ja.json", encoding="utf-8"))

vn_lois = [x for x in vn if x.get("kind") == "LOI"]
en_lois = [x for x in en if x.get("kind") == "LOI"]
ja_lois = [x for x in ja if x.get("kind") == "LOI"]

print(f"Total LOI turns: VN={len(vn_lois)}, EN={len(en_lois)}, JA={len(ja_lois)}")
mismatches = 0
for i in range(len(vn_lois)):
    v_sents = len(vn_lois[i]["sentences"])
    e_sents = len(en_lois[i]["sentences"])
    j_sents = len(ja_lois[i]["sentences"])
    if v_sents != e_sents or v_sents != j_sents:
        print(f"Diff at turn {vn_lois[i]['id']}: VN={v_sents}, EN={e_sents}, JA={j_sents}")
        mismatches += 1
if mismatches == 0:
    print("PERFECT 100% MATCH across all turns!")
else:
    print(f"Total mismatches: {mismatches}")
