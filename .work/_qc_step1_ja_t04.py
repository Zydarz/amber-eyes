#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC Step 1 (H14/H13/H6) cho JA Tap04: parse_shots -> shots_JA_t04.json, subtitles -> Tap04_JA.srt."""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

tl = json.loads((W / "timeline_s_JA_t04.json").read_text(encoding="utf-8-sig"))
sh = json.loads((W / "shots_JA_t04.json").read_text(encoding="utf-8-sig"))
shots = sh["shots"]
items = tl["items"]

print(f"timeline total = {tl['total']} s · {len(items)} câu")
print(f"shots total    = {sh['total']} s · {len(shots)} shot")

covered = []
for s in shots:
    covered += s["sentences"]
allids = [it["id"] for it in items]
miss = [i for i in allids if i not in covered]
extra = [c for c in covered if c not in allids]
dup = [c for c in set(covered) if covered.count(c) > 1]
print(f"câu bỏ sót = {len(miss)} {miss[:10]}")
print(f"câu thừa   = {len(extra)} {extra[:10]}")
print(f"câu trùng  = {len(dup)} {dup[:10]}")

idx = {i: n for n, i in enumerate(allids)}
bad_order = [s["id"] for s in shots if s["sentences"] and idx[s["sentences"][0]] > idx[s["sentences"][-1]]]
print(f"shot thứ tự ngược = {len(bad_order)} {bad_order[:10]}")

sent = {it["id"]: it for it in items}
drift = []
for s in shots:
    if not s["sentences"]:
        continue
    want = round(sent[s["sentences"][0]]["start"] - 0.20, 3)
    if abs(s["start"] - want) > 0.02:
        drift.append((s["id"], s["start"], want))
print(f"shot lệch mốc đầu = {len(drift)} {drift[:5]}")

gaps = [(a["id"], a["end"], b["id"], b["start"]) for a, b in zip(shots, shots[1:])
        if abs(b["start"] - a["end"]) > 0.02]
print(f"shot không liên tục = {len(gaps)} {gaps[:5]}")

bgfiles = {p.stem for p in (ROOT / "assets" / "bg").glob("*.png")}
nobg = sorted({s["bg"] for s in shots if s["bg"]} - bgfiles)
print(f"nền thiếu file = {nobg}")

last = shots[-1]
print(f"shot cuối = {last['id']} · có chữ = {bool(last['segments'])}")
for el in last["segments"]:
    print("    ", el)

# chữ trên hình phải là tiếng Nhật (không còn tiếng Việt sót)
susp = []
for s in shots:
    for seg in s["segments"]:
        for el in seg.get("elems", []):
            t = el[1] if len(el) > 1 else ""
            if re.search(r"[ăâđêôơưĂÂĐÊÔƠƯạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]", t or ""):
                susp.append((s["id"], t[:60]))
print(f"chữ trên hình còn tiếng Việt = {len(susp)} {susp[:5]}")

# SRT subtitle check
srt_path = ROOT / "02_SAN_XUAT/Tap04_JA/xuat_ban/Tap04_JA.srt"
srt = srt_path.read_text(encoding="utf-8-sig")
blocks = [b for b in srt.strip().split("\n\n") if b.strip()]

def sec(ts):
    h, m, s = ts.split(":")
    s, ms = s.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

last_end = 0
for b in blocks:
    a, bnd = b.splitlines()[1].split(" --> ")
    last_end = sec(bnd)
print(f"SRT: {len(blocks)} cue · cuối hết {last_end:.2f} s · timeline total {tl['total']:.2f} s")

ok = all(x == 0 for x in [len(miss), len(extra), len(dup), len(bad_order), len(drift), len(gaps), len(nobg), len(susp)])
ok = ok and last_end <= tl["total"] + 0.05 and abs(sh["total"] - tl["total"]) <= 0.05
print("\nKẾT QUẢ QC STEP 1:", "PASS" if ok else "FAIL")
