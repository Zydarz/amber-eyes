"""Do lech F0 (nk) cua tung file so voi trung vi vai + phan bo chung T04.

Tinh lai tu .work/_f0_t04.json (list, 382 dong) — cung quy tac voi check_higgs_f0.py:
  lech = |yin - median_yin(cung vai)|  ; loai neu >= 4 nk
"""
import json
import pathlib
import statistics
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
EPN = "04"

f0 = json.loads((HERE / "_f0_t04.json").read_text(encoding="utf-8-sig"))
man_p = HERE / "kaggle_higgs" / ("out_higgs_prod_t%s" % EPN) / ("out_higgs_prod_t%s" % EPN) / "higgs_manifest.json"
man = {r["file"]: r for r in json.loads(man_p.read_text(encoding="utf-8-sig")) if r.get("ok")}

by_role = defaultdict(list)
for r in f0:
    by_role[r["role"]].append(r["yin"])
med_role = {k: statistics.median(v) for k, v in by_role.items()}

rows = []
for r in f0:
    m = med_role.get(r["role"])
    if m is None:
        continue
    dev = abs(r["yin"] - m)
    rows.append((dev, r["file"], r["id"], r["role"], r["yin"], m, r.get("emo")))

rows.sort(reverse=True)
print("median F0 theo vai:", {k: round(v, 1) for k, v in sorted(med_role.items())})
devs = sorted(d[0] for d in rows)
n = len(devs)
print("so file: %d | median lech = %.2f nk | p90 = %.2f | p99 = %.2f | max = %.2f" % (
    n, devs[n // 2], devs[int(n * 0.9)], devs[int(n * 0.99)], devs[-1]))
print("so file lech >= 4 nk: %d" % sum(1 for d in devs if d >= 4))
print("so file lech >= 3 nk: %d" % sum(1 for d in devs if d >= 3))

print("\n== 20 file lech lon nhat ==")
for dev, f, sid, role, yin, m, emo in rows[:20]:
    print("  %5.2f nk | %-34s | %-8s %-3s | yin=%6.1f med=%6.1f | %s" % (dev, f, sid, role, yin, m, emo))

TGT = {"2.08#1", "3.02#2", "5.08#5"}
print("\n== 3 cau bi loai toan bo: lech tung ban ==")
for sid in sorted(TGT):
    print("--- %s ---" % sid)
    for dev, f, s2, role, yin, m, emo in sorted([x for x in rows if x[2] == sid], key=lambda x: x[0]):
        print("   %5.2f nk | %-34s | yin=%6.1f med=%6.1f | %s" % (dev, f, yin, m, emo))

print("\n== so sanh voi tap 03 (neu co _f0_t03.json) ==")
p3 = HERE / "_f0_t03.json"
if p3.exists():
    f3 = json.loads(p3.read_text(encoding="utf-8-sig"))
    br = defaultdict(list)
    for r in f3:
        br[r["role"]].append(r["yin"])
    mr = {k: statistics.median(v) for k, v in br.items()}
    d3 = sorted(abs(r["yin"] - mr[r["role"]]) for r in f3 if r["role"] in mr)
    print("T03: %d file | median lech = %.2f | p90 = %.2f | max = %.2f | >=4nk: %d" % (
        len(d3), d3[len(d3) // 2], d3[int(len(d3) * 0.9)], d3[-1], sum(1 for d in d3 if d >= 4)))
else:
    print("chua co _f0_t03.json")
