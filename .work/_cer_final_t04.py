import json, pathlib, statistics
HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
sel = json.loads((HERE / "higgs_selection_t04.json").read_text(encoding="utf-8-sig"))["selection"]
c = [v["cer"] for v in sel.values() if v["cer"] is not None]
print("chon san xuat: %d cau | CER TB = %.4f%% | >2%%: %d | max %.2f%%" % (
    len(c), 100 * sum(c) / len(c), sum(1 for x in c if x > 0.02), 100 * max(c)))
rows = json.loads((HERE / "higgs_cer_rows_t04.json").read_text(encoding="utf-8-sig"))
best = {}
for r in rows:
    if not r.get("cer_ok"): continue
    i = r["id"]
    if i not in best or r["cer"] < best[i]: best[i] = r["cer"]
b = list(best.values())
print("best theo cau (382 dong): %d cau | CER TB = %.4f%% | >2%%: %d" % (
    len(b), 100 * sum(b) / len(b), sum(1 for x in b if x > 0.02)))
