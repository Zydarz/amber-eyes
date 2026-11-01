import json, pathlib
sh = json.loads(pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\shots_t04.json").read_text(encoding="utf-8-sig"))["shots"]
ls = [(round(s["end"]-s["start"],1), s["id"]) for s in sh if s["end"]-s["start"] > 16]
print("shot > 16 s (gate B se CANH BAO):", sorted(ls, reverse=True))
print("tb/shot: %.1f s | dai nhat: %.1f | ngan nhat: %.1f" % (
    sum(s["end"]-s["start"] for s in sh)/len(sh),
    max(s["end"]-s["start"] for s in sh), min(s["end"]-s["start"] for s in sh)))
