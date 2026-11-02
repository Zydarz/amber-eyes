#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bước 1 (H14): audio JA Tap02 đã đổi (Higgs 01/11) -> phải dựng lại shots + SRT.

- Sao lưu shots/SRT cũ (L5) vào .work/_cu/ja_t02_20261102/
- Chạy parse_shots.py (AE_LANG=ja, AE_EP=02) -> shots_JA_t02.json
- Chạy subtitles.py -> Tap02_JA.srt
- QC: shots phủ 100% câu, đúng thứ tự, có nền, thời lượng khớp timeline.
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"
PY = sys.executable

BK = W / "_cu" / "ja_t02_20261102"
BK.mkdir(parents=True, exist_ok=True)

print("=== 0. SAO LUU (L5) ===")
for rel in [".work/shots_JA_t02.json",
            "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt",
            ".work/shots_text_tap02_JA.json"]:
    src = ROOT / rel
    if src.exists():
        dst = BK / src.name
        shutil.copy2(src, dst)
        print(f"  sao luu {rel} -> {dst.relative_to(ROOT)}")
    else:
        print(f"  BO QUA (khong ton tai) {rel}")

print("\n=== 1. parse_shots.py ===")
r = subprocess.run([PY, str(W / "parse_shots.py")], cwd=ROOT,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print(r.stdout)
if r.stderr.strip():
    print("STDERR:", r.stderr[-3000:])
if r.returncode != 0:
    raise SystemExit(f"parse_shots THAT BAI rc={r.returncode}")

print("=== 2. subtitles.py ===")
r = subprocess.run([PY, str(W / "subtitles.py")], cwd=ROOT,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print(r.stdout)
if r.stderr.strip():
    print("STDERR:", r.stderr[-2000:])
if r.returncode != 0:
    raise SystemExit(f"subtitles THAT BAI rc={r.returncode}")

print("=== 3. QC khop 3 chieu (H13) ===")
tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sh = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))
shots = sh["shots"]
items = tl["items"]

print(f"  timeline total = {tl['total']} s · {len(items)} cau")
print(f"  shots  total = {sh['total']} s · {len(shots)} shot")

# a) phu 100% cau, dung thu tu
covered = []
for s in shots:
    covered += s["sentences"]
allids = [it["id"] for it in items]
miss = [i for i in allids if i not in covered]
extra = [c for c in covered if c not in allids]
dup = [c for c in set(covered) if covered.count(c) > 1]
print(f"  cau bi bo sot = {len(miss)} {miss[:10]}")
print(f"  cau thua      = {len(extra)} {extra[:10]}")
print(f"  cau trung     = {len(dup)} {dup[:10]}")

# b) thu tu: moi shot phai bat dau truoc / dung sau cau cua no
idx = {i: n for n, i in enumerate(allids)}
bad_order = []
for s in shots:
    if not s["sentences"]:
        continue
    first, last = s["sentences"][0], s["sentences"][-1]
    if idx[first] > idx[last]:
        bad_order.append(s["id"])
print(f"  shot co thu tu nguoc = {len(bad_order)} {bad_order[:10]}")

# c) moc thoi gian shot phai khop timeline
sent = {it["id"]: it for it in items}
drift = []
for s in shots:
    if not s["sentences"]:
        continue
    want_start = round(sent[s["sentences"][0]]["start"] - 0.20, 3)
    if abs(s["start"] - want_start) > 0.02:
        drift.append((s["id"], s["start"], want_start))
print(f"  shot lech moc dau = {len(drift)} {drift[:5]}")

# d) shot lien tuc khong gap / khong de
gaps = []
for a, b in zip(shots, shots[1:]):
    if abs(b["start"] - a["end"]) > 0.02:
        gaps.append((a["id"], a["end"], b["id"], b["start"]))
print(f"  shot khong lien tuc = {len(gaps)} {gaps[:5]}")

# e) nền co file that
bgdir = ROOT / "assets" / "bg"
bgfiles = {p.stem for p in bgdir.glob("*.png")}
nobg = sorted({s["bg"] for s in shots if s["bg"]} - bgfiles)
print(f"  nen thieu file = {nobg}")

# f) shot cuoi phai co chu (H12)
last = shots[-1]
print(f"  shot cuoi = {last['id']} · co chu = {bool(last['segments'])}")
for el in last["segments"]:
    print("     ", el)

# g) do dai shot ngoai 3-15 s (H10)
too_long = [(s["id"], round(s["end"] - s["start"], 1)) for s in shots if s["end"] - s["start"] > 15]
too_short = [(s["id"], round(s["end"] - s["start"], 1)) for s in shots if s["end"] - s["start"] < 1.0]
print(f"  shot > 15 s = {len(too_long)} {too_long[:8]}")
print(f"  shot < 1 s  = {len(too_short)} {too_short[:8]}")

# h) nen lap qua 4 shot lien tiep (H10)
run, prev, maxrun, where = 1, None, 1, ""
for s in shots:
    if s["bg"] == prev:
        run += 1
    else:
        run, prev = 1, s["bg"]
    if run > maxrun:
        maxrun, where = run, s["id"]
print(f"  nen lap toi da = {maxrun} shot lien tiep (tai {where})")

# i) SRT
srt = (ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt").read_text(encoding="utf-8-sig")
blocks = [b for b in srt.strip().split("\n\n") if b.strip()]


def sec(ts):
    h, m, s = ts.split(":")
    s, ms = s.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


last_end = 0
for b in blocks:
    a, bnd = b.splitlines()[1].split(" --> ")
    last_end = sec(bnd)
print(f"  SRT: {len(blocks)} cue · cuoi het {last_end:.2f} s · timeline total {tl['total']:.2f} s")
ok = all(x <= 0 for x in [
    len(miss), len(extra), len(dup), len(bad_order), len(drift), len(gaps), len(nobg)])
print("\nKET QUA:", "PASS" if ok and last_end <= tl["total"] + 0.05 else "FAIL")
