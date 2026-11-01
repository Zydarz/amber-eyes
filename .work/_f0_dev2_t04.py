"""Tinh lech F0 theo DUNG quy tac check_higgs_f0.py (moc = trung vi YIN cua file NEUTRAL cung vai)."""
import json
import math
import pathlib
import statistics
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent


def nc(a, b):
    return abs(12 * math.log2(a / b))


def report(tag, f0_path, extra_excl=None):
    f0 = json.loads(pathlib.Path(f0_path).read_text(encoding="utf-8-sig"))
    by_role = defaultdict(list)
    for r in f0:
        if r.get("emo") == "neutral":
            by_role[r["role"]].append(r["yin"])
    med = {k: statistics.median(v) for k, v in by_role.items()}
    devs = sorted(((nc(r["yin"], med[r["role"]]), r) for r in f0 if r["role"] in med), key=lambda x: -x[0])
    n = len(devs)
    print("\n== %s == (%d file)" % (tag, n))
    print("  median YIN neutral theo vai:", {k: round(v, 1) for k, v in sorted(med.items())})
    print("  lech: median=%.2f p90=%.2f p99=%.2f max=%.2f | >=4nk: %d (%.1f%%)" % (
        sorted(d for d, _ in devs)[n // 2],
        sorted(d for d, _ in devs)[int(n * .9)],
        sorted(d for d, _ in devs)[int(n * .99)],
        devs[0][0],
        sum(1 for d, _ in devs if d >= 4),
        100 * sum(1 for d, _ in devs if d >= 4) / n))
    return devs, med


d4, m4 = report("T04", HERE / "_f0_t04.json")
p3 = HERE / "_f0_t03.json"
if p3.exists():
    report("T03", p3)

print("\n== T04: 12 file lech lon nhat ==")
for dev, r in d4[:12]:
    print("  %5.2f nk | %-34s | %-8s %-3s %-8s | yin=%6.1f" % (dev, r["file"], r["id"], r["role"], r["emo"], r["yin"]))

TGT = {"2.08#1", "3.02#2", "5.08#5"}
print("\n== 3 cau bi loai toan bo (quy tac dung) ==")
for sid in sorted(TGT):
    print("--- %s ---" % sid)
    for dev, r in sorted([x for x in d4 if x[1]["id"] == sid], key=lambda x: x[0]):
        print("   %5.2f nk | %-34s | %s" % (dev, r["file"], r["emo"]))

excl = set(json.loads((HERE / "higgs_exclude_f0_t04.json").read_text(encoding="utf-8-sig")))
print("\ntong danh sach loai (len file):", len(excl))
# phan bo lech cua cac file trong danh sach loai
bad = [d for d, r in d4 if r["file"] in excl]
good = [d for d, r in d4 if r["file"] not in excl]
print("lech cua file BI LOAI: min=%.2f max=%.2f" % (min(bad), max(bad)))
print("lech cua file KHONG bi loai: max=%.2f | so file > 4nk van duoc giu: %d" % (
    max(good), sum(1 for d in good if d >= 4)))
