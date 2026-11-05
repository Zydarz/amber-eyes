# -*- coding: utf-8 -*-
"""Step 1 for JA Tap05: parse_shots -> shots_JA_t05.json, subtitles -> Tap05_JA.srt, QC 3D."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "05"
os.environ["PYTHONIOENCODING"] = "utf-8"
PY = sys.executable

for step, script in (("parse_shots.py", "parse_shots.py"), ("subtitles.py", "subtitles.py")):
    print(f"=== {step} ===")
    r = subprocess.run([PY, str(W / script)], cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    print(r.stdout[-2500:])
    if r.stderr.strip():
        print("STDERR:", r.stderr[-1500:])
    if r.returncode != 0:
        raise SystemExit(f"{step} THAT BAI rc={r.returncode}")

tl = json.loads((W / "timeline_s_JA_t05.json").read_text(encoding="utf-8"))
sh = json.loads((W / "shots_JA_t05.json").read_text(encoding="utf-8"))
shots = sh["shots"]
items = tl["items"]
print(f"\ntimeline total = {tl['total']} s · {len(items)} cau")
print(f"shots total = {sh['total']} s · {len(shots)} shot")

covered = []
for s in shots:
    covered += s["sentences"]
allids = [it["id"] for it in items]
miss = [i for i in allids if i not in covered]
extra = [c for c in covered if c not in allids]
dup = [c for c in set(covered) if covered.count(c) > 1]
print(f"cau bo sot = {len(miss)} {miss[:10]}")
print(f"cau thua   = {len(extra)} {extra[:10]}")
print(f"cau trung  = {len(dup)} {dup[:10]}")

idx = {i: n for n, i in enumerate(allids)}
bad_order = [s["id"] for s in shots if s["sentences"] and idx[s["sentences"][0]] > idx[s["sentences"][-1]]]
print(f"shot thu tu nguoc = {len(bad_order)} {bad_order[:10]}")

gaps = [(a["id"], a["end"], b["id"], b["start"]) for a, b in zip(shots, shots[1:])
        if abs(b["start"] - a["end"]) > 0.05]
print(f"shot khong lien tuc = {len(gaps)} {gaps[:5]}")

bgfiles = {p.stem for p in (ROOT / "assets" / "bg").glob("*.png")}
nobg = sorted({s["bg"] for s in shots if s["bg"]} - bgfiles)
print(f"nen thieu file = {nobg}")

last = shots[-1]
print(f"shot cuoi = {last['id']} · co chu = {bool(last['segments'])}")

too_long = [(s["id"], round(s["end"] - s["start"], 1)) for s in shots if s["end"] - s["start"] > 25]
print(f"shot > 25 s = {len(too_long)} {too_long[:8]}")

srt = (ROOT / "02_SAN_XUAT/Tap05_JA/xuat_ban/Tap05_JA.srt").read_text(encoding="utf-8-sig")
blocks = [b for b in srt.strip().split("\n\n") if b.strip()]

def sec(ts):
    h, m, s = ts.split(":")
    s, ms = s.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

last_end = 0
for b in blocks:
    a, bnd = b.splitlines()[1].split(" --> ")
    last_end = sec(bnd)
print(f"SRT: {len(blocks)} cue · cuoi het {last_end:.2f} s · timeline total {tl['total']:.2f} s")

ok = all(x == 0 for x in [len(miss), len(extra), len(dup), len(bad_order), len(gaps), len(nobg)])
ok = ok and last_end <= tl["total"] + 0.05 and abs(sh["total"] - tl["total"]) <= 0.05
print("\nKET QUA STEP 1:", "PASS" if ok else "FAIL")
