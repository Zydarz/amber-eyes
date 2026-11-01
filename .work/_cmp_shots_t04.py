"""So timeline moi voi shots cu + backup shots cu (L5) truoc khi parse lai."""
import json
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")

tl = json.loads((HERE / "timeline_s_t04.json").read_text(encoding="utf-8-sig"))
sh = json.loads((HERE / "shots_t04.json").read_text(encoding="utf-8-sig"))

print("timeline moi : total=%.2f | items=%d | markers=%d" % (tl["total"], len(tl["items"]), len(tl["markers"])))
print("shots cu     : total=%.2f | shots=%d" % (sh["total"], len(sh["shots"])))
print("=> shots cu build tu timeline CU (lech %.2f s)" % abs(sh["total"] - tl["total"]))

s = sh["shots"]
print("shot dau %s: %.2f-%.2f | shot cuoi %s: %.2f-%.2f" % (
    s[0]["id"], s[0]["start"], s[0]["end"], s[-1]["id"], s[-1]["start"], s[-1]["end"]))
lens = [(round(x["end"] - x["start"], 1), x["id"]) for x in s]
print("dai nhat:", max(lens), "| ngan nhat:", min(lens))

bak = HERE / "_cu" / "shots_t04_truoc_parse_lai_20261031.json"
bak.parent.mkdir(parents=True, exist_ok=True)
if not bak.exists():
    shutil.copy2(HERE / "shots_t04.json", bak)
    print("backup ->", bak)
else:
    print("backup da co:", bak)

# Do lech tung shot giua shots cu va moc cua timeline moi
sent = {it["id"]: it for it in tl["items"]}
worst = []
for x in s:
    if not x.get("sentences"):
        continue
    a = sent.get(x["sentences"][0])
    b = sent.get(x["sentences"][-1])
    if a and b:
        worst.append((round(abs(a["start"] - x["start"]), 2), x["id"]))
worst.sort(reverse=True)
print("shot lech lon nhat so voi moc moi (s):", worst[:8])
