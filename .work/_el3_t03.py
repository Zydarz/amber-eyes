import json
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
tl = json.loads((W/"timeline_s_t03.json").read_text(encoding="utf-8-sig"))
sent = {i["id"]: i for i in tl["items"]}
for el in ("2.09","4.05"):
    print(f"===== {el} =====")
    for k in sorted([x for x in sent if x.startswith(el+"#")], key=lambda s:int(s.split('#')[1])):
        print(f"  {k} [{sent[k]['role']}] {sent[k]['text']}")
    print()
