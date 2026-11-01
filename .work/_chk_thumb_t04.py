import sys, pathlib
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work"); sys.path.insert(0, r"D:\TEST\Gax\amber-eyes")
import edition as ED
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
for ep in ("03", "04"):
    d = ED.EPISODES[ep]
    print("EP%s thumb_bg: %s | file ton tai: %s" % (ep, d.get("thumb_bg"), (ROOT/"assets"/"bg"/(d.get("thumb_bg","")+".png")).exists()))
    print("   thumb lines:", d.get("thumb"))
print()
print("EP04 summary ids:", ED.EPISODES["04"]["summary"])
tl = __import__("json").loads((ROOT/".work"/"timeline_s_t04.json").read_text(encoding="utf-8-sig"))
sents = {i["id"]: i["text"] for i in tl["items"]}
for k in ED.EPISODES["04"]["summary"]:
    print("   %-8s %s" % (k, sents.get(k, "THIEU")[:120]))
print()
print("EP04 need (nguon can bo sung):", len(ED.EPISODES["04"]["need"]))
