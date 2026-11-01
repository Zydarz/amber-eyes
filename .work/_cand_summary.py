import json, pathlib
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
tl = json.loads((ROOT/".work"/"timeline_s_t04.json").read_text(encoding="utf-8-sig"))
sents = {i["id"]: i["text"] for i in tl["items"]}
for k in ("1.03#1","1.03#2","1.05#3","1.08#1","1.08#3","2.10#1","2.10#2","3.02#1","3.02#2","5.08#1","5.08#2"):
    print("%-8s %s" % (k, sents.get(k, "THIEU")))
