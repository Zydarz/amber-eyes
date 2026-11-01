import sys, json, pathlib
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work"); sys.path.insert(0, r"D:\TEST\Gax\amber-eyes")
import edition as ED
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
tl = {}
for ep in ("03", "04"):
    for cand in (ROOT/".work"/("timeline_s_t%s.json" % ep), ROOT/".work"/"timeline_s_t03.json"):
        if cand.exists():
            tl[ep] = json.loads(cand.read_text(encoding="utf-8-sig")); break
for ep in ("03", "04"):
    d = ED.EPISODES[ep]
    sents = {i["id"]: i["text"] for i in tl[ep]["items"]}
    print("== EP%s summary %s ==" % (ep, d["summary"]))
    for k in d["summary"]:
        print("   %-8s %s" % (k, sents.get(k, "THIEU CAU")[:170]))
    print()
items = tl["04"]["items"]
print("== 10 cau dau T04 ==")
for it in items[:10]:
    print("   %-9s %-3s %-8s %s" % (it["id"], it["role"], it.get("emotion",""), it["text"][:130]))
print("== cac cau role H (HOST) ==")
for it in items:
    if it["role"] == "H":
        print("   %-9s %s" % (it["id"], it["text"][:130]))
