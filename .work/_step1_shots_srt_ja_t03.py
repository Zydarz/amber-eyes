#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bước 1 (H14) cho JA Tap03: parse_shots -> shots_JA_t03.json, subtitles -> Tap03_JA.srt, QC 3 chiều."""
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
os.environ["AE_EP"] = "03"
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

tl = json.loads((W / "timeline_s_JA_t03.json").read_text(encoding="utf-8-sig"))
sh = json.loads((W / "shots_JA_t03.json").read_text(encoding="utf-8-sig"))
shots = sh["shots"]
items = tl["items"]
print(f"\ntimeline total = {tl['total']} s · {len(items)} cau")
print(f"shots  total = {sh['total']} s · {len(shots)} shot")

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

sent = {it["id"]: it for it in items}
drift = []
for s in shots:
    if not s["sentences"]:
        continue
    want = round(sent[s["sentences"][0]]["start"] - 0.20, 3)
    if abs(s["start"] - want) > 0.02:
        drift.append((s["id"], s["start"], want))
print(f"shot lech moc dau = {len(drift)} {drift[:5]}")

gaps = [(a["id"], a["end"], b["id"], b["start"]) for a, b in zip(shots, shots[1:])
        if abs(b["start"] - a["end"]) > 0.02]
print(f"shot khong lien tuc = {len(gaps)} {gaps[:5]}")

bgfiles = {p.stem for p in (ROOT / "assets" / "bg").glob("*.png")}
nobg = sorted({s["bg"] for s in shots if s["bg"]} - bgfiles)
print(f"nen thieu file = {nobg}")

last = shots[-1]
print(f"shot cuoi = {last['id']} · co chu = {bool(last['segments'])}")
for el in last["segments"]:
    print("    ", el)

too_long = [(s["id"], round(s["end"] - s["start"], 1)) for s in shots if s["end"] - s["start"] > 15]
too_short = [(s["id"], round(s["end"] - s["start"], 1)) for s in shots if s["end"] - s["start"] < 1.0]
print(f"shot > 15 s = {len(too_long)} {too_long[:8]}")
print(f"shot < 1 s  = {len(too_short)} {too_short[:8]}")

run, prev, maxrun, where = 1, None, 1, ""
for s in shots:
    run = run + 1 if s["bg"] == prev else 1
    prev = s["bg"]
    if run > maxrun:
        maxrun, where = run, s["id"]
print(f"nen lap toi da = {maxrun} shot lien tiep (tai {where})")

# chữ trên hình phải là tiếng Nhật (không còn tiếng Việt sót)
susp = []
for s in shots:
    for seg in s["segments"]:
        t = seg.get("text", "") if isinstance(seg, dict) else ""
        if re.search(r"[ăâđêôơưĂÂĐÊÔƠƯạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]", t or ""):
            susp.append((s["id"], t[:60]))
print(f"chu tren hinh con tieng Viet = {len(susp)} {susp[:5]}")

srt = (ROOT / "02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA.srt").read_text(encoding="utf-8-sig")
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

ok = all(x == 0 for x in [len(miss), len(extra), len(dup), len(bad_order), len(drift), len(gaps), len(nobg), len(susp)])
ok = ok and last_end <= tl["total"] + 0.05 and abs(sh["total"] - tl["total"]) <= 0.05
print("\nKET QUA:", "PASS" if ok else "FAIL")

# ---- đối chiếu shot với bản VN (cùng số hiệu, cùng câu) ----
vn_path = W / "shots_t03.json"
if vn_path.exists():
    vn = json.loads(vn_path.read_text(encoding="utf-8-sig"))
    vm = {s["id"]: s for s in vn["shots"]}
    diffs = []
    for s in shots:
        v = vm.get(s["id"])
        if not v:
            diffs.append((s["id"], "KHONG CO O BAN VN"))
            continue
        if v["sentences"] != s["sentences"]:
            diffs.append((s["id"], f"cau khac: VN {v['sentences']} vs JA {s['sentences']}"))
        if abs((v["end"] - v["start"]) - (s["end"] - s["start"])) > 0.05:
            diffs.append((s["id"], f"dai lech {v['end']-v['start']:.2f} vs {s['end']-s['start']:.2f}"))
        if v.get("bg") != s.get("bg"):
            diffs.append((s["id"], f"nen khac: {v.get('bg')} vs {s.get('bg')}"))
    print(f"\nsoi shot JA voi VN: {len(diffs)} khac biet")
    for d in diffs[:12]:
        print("   ", d)
else:
    print("\n(chua co shots_t03.json de doi chieu)")

