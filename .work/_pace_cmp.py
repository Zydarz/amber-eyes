import json, pathlib, statistics
W = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
def stat(p, label):
    if not p.exists():
        print(label, "-> thieu file", p.name); return
    sh = json.loads(p.read_text(encoding="utf-8-sig"))["shots"]
    lens = [s["end"]-s["start"] for s in sh]
    ls = sorted([(round(l,1), s["id"]) for l, s in zip(lens, sh) if l > 16], reverse=True)
    print("%s: %d shot | tb %.1f s | median %.1f | >16s: %d (%.0f%%) | >30s: %d | max %.1f (%s) | min %.1f" % (
        label, len(sh), sum(lens)/len(lens), statistics.median(lens), len(ls), 100*len(ls)/len(sh),
        sum(1 for l in lens if l > 30), max(lens), ls[0][1] if ls else "-", min(lens)))
stat(W/"shots_t04.json", "T04")
stat(W/"shots_t03.json", "T03")
stat(W/"shots_t02.json", "T02")
