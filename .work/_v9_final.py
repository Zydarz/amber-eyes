"""Tong hop cuoi pilot v9: CER theo cau (2 ban, lay ban tot) + G9 tren cau neutral + dem cau cam xuc vot cao do."""
import json, math, sys, pathlib
from collections import defaultdict
import os
import numpy as np
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
R = json.load(open(HERE / f"pilot_{os.environ.get('TAG','v9')}_result.json", encoding="utf-8"))
P = {o["key"]: o["cer_pad"] for o in json.load(open(HERE / f"pilot_{os.environ.get('TAG','v9')}_padtest.json", encoding="utf-8"))}
nc = lambda a, b: abs(12 * math.log2(a / b))
med = lambda v: float(np.median([x for x in v if x])) if any(v) else 0.0

# CER theo cau: min qua 2 ban x moi luot do
sent = defaultdict(list)
for r in R["rows"]:
    cs = [a["cer"] for a in r["asr"] if "cer" in a] + ([P[r["key"]]] if P.get(r["key"]) is not None else [])
    sent[(r["ref"], r["key"].split("__")[2])].append(min(cs) if cs else None)
print("CER THEO CAU (ban tot nhat trong 2 ban, moi luot do):")
cer_ok = {}
for ref in sorted({k[0] for k in sent}):
    best = [min(c for c in v if c is not None) for k, v in sent.items() if k[0] == ref]
    bad = sum(b > 0.02 for b in best)
    cer_ok[ref] = bad
    print(f"  {ref:8} cau dat {len(best)-bad}/{len(best)}  CER tb {100*np.mean(best):.2f}%  max {100*max(best):.1f}%")

# G9 tren cau neutral
rows = R["rows"] + R["base"]
neu = defaultdict(lambda: {"ac": [], "yin": []})
jump = defaultdict(lambda: [0, 0])
for r in rows:
    k = (r["role"], r["ref"])
    if r["emotion"] == "neutral":
        neu[k]["ac"].append(r["f0_ac"]); neu[k]["yin"].append(r["f0_yin"])
for r in rows:
    k = (r["role"], r["ref"])
    if r["emotion"] != "neutral" and neu[k]["yin"]:
        jump[k][1] += 1
        jump[k][0] += nc(r["f0_yin"], med(neu[k]["yin"])) >= 4
F = {k: (med(v["ac"]), med(v["yin"])) for k, v in neu.items() if v["yin"]}
for k, t in R["table"].items():
    kk = tuple(k.split("|"))
    F.setdefault(kk, (t["f0_ac"], t["f0_yin"]))  # vai khong co cau neutral (N2): dung trung vi moi cau
print("\nF0 CAU NEUTRAL (AC / YIN) + cau cam xuc vot >= 4 nc so voi neutral cua chinh no:")
for k in sorted(F):
    print(f"  {k[0]:3} {k[1]:13} {F[k][0]:6.1f} / {F[k][1]:6.1f}   vot: {jump[k][0]}/{jump[k][1]}")
H = ("H", "PROD_H"); N1 = ("N1", "PROD_W6_LOW"); N2 = ("N2", "PROD_W5_HIGH")
d = lambda a, b: min(nc(F[a][0], F[b][0]), nc(F[a][1], F[b][1]))
print("\nG9 (neutral, min 2 thuat toan):")
Ds = sorted(k for k in F if k[0] == "D"); Cs = sorted(k for k in F if k[0] == "C")
for kd in Ds:
    print(f"  {kd[1]:8} D~H {d(kd,H):5.2f}  D~N1 {d(kd,N1):5.2f}  D~N2 {d(kd,N2):5.2f}  D~C(min) {min(d(kd,c) for c in Cs):5.2f}")
for kc in Cs:
    print(f"  {kc[1]:8} C~H {d(kc,H):5.2f}  C~N1 {d(kc,N1):5.2f}  C~N2 {d(kc,N2):5.2f}")
json.dump({"cer_bad_sentences": cer_ok, "f0_neutral": {f"{k[0]}|{k[1]}": v for k, v in F.items()},
           "emotion_jump": {f"{k[0]}|{k[1]}": v for k, v in jump.items()}},
          open(HERE / f"pilot_{os.environ.get('TAG','v9')}_final.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
