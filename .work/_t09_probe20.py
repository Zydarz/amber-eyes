import io, json, os
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
d = json.loads((ROOT/".work/shots_t08.json").read_text(encoding="utf-8"))
sh = d["shots"]
print("total shots:", len(sh))
print()
print("=== 3 shot mẫu đầu (nhiều câu) ===")
for s in sh[:4]:
    print(json.dumps(s, ensure_ascii=False, indent=1)[:1400])
    print("---")
print("=== shot T10 (thẻ hồi) + shot cuối ===")
for s in sh:
    if s.get("template") == "T10":
        print(json.dumps(s, ensure_ascii=False, indent=1)[:900]); break
print(json.dumps(sh[-1], ensure_ascii=False, indent=1)[:900])
print()
print("=== phân bố template / variant ===")
from collections import Counter
print(" template:", Counter(s.get("template") for s in sh))
print(" variant :", Counter(s.get("variant") for s in sh))
print(" camera  :", Counter(s.get("camera") for s in sh))
print(" số câu / shot:", Counter(len(s["sentences"]) for s in sh))
print(" hold:", sum(1 for s in sh if s.get("hold")))
