#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do lai toan bo kho anh + kich ban + san xuat cho bao cao 27/11/2026."""
import json, os, re, sys, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BG = ROOT / "assets" / "bg"
KB = ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham"
SX = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham"
WORK = ROOT / ".work"

# --- 1. Anh nen theo tap ---
img_by_tap = {}
root_png = list(BG.glob("*.png"))
root_all = [p for p in BG.iterdir() if p.is_file() and p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")]
for p in root_all:
    m = re.match(r"^t(\d+)_", p.name)
    if m:
        t = int(m.group(1))
        img_by_tap.setdefault(t, []).append(p.name)
other = len(root_all) - sum(len(v) for v in img_by_tap.values())

# --- 2. bg_jobs ---
jobs = {}
for jf in WORK.glob("bg_jobs_tap*.json"):
    m = re.match(r"^bg_jobs_tap(\d+)\.json$", jf.name)
    if not m:
        continue
    try:
        data = json.loads(jf.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"!! doc loi {jf.name}: {e}", file=sys.stderr)
        continue
    items = data if isinstance(data, list) else data.get("jobs", data.get("items", []))
    jobs[int(m.group(1))] = len(items)

# --- 3. Kich ban: so cau + so shot ---
def count_dialogues(md_text):
    # dong thoai: "- **H**: ..." hoac "**H**: ..." hoac "- **Câu ...**:"
    n = 0
    for line in md_text.splitlines():
        s = line.strip()
        if not s.startswith("-"):
            continue
        if re.match(r"^-\s*\*\*[^*]{1,40}\*\*\s*:", s) or re.match(r"^-\s*\*\*[^*]{1,40}\*\*\s+", s):
            n += 1
    return n

scripts = {}
for d in sorted(KB.iterdir()):
    if not d.is_dir():
        continue
    m = re.match(r"^Tap(\d+)$", d.name)
    if not m:
        continue
    t = int(m.group(1))
    md = list(d.glob("kichban*.md"))
    if not md:
        continue
    md.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    txt = md[0].read_text(encoding="utf-8", errors="replace")
    scripts[t] = {
        "file": md[0].name,
        "dialogues": count_dialogues(txt),
        "bytes": md[0].stat().st_size,
        "mtime": md[0].stat().st_mtime,
    }

# --- 4. Shot map ---
shots = {}
for sm in WORK.glob("shot_map_tap*.json"):
    m = re.match(r"^shot_map_tap(\d+)\.json$", sm.name)
    if m:
        try:
            d = json.loads(sm.read_text(encoding="utf-8"))
            shots[int(m.group(1))] = len(d) if isinstance(d, list) else len(d.get("shots", d.get("rows", [])))
        except Exception:
            pass

# --- 5. Bang Shot Anh ---
bangs = {}
for b in SX.glob("Tap*/Bang_Shot_Anh_Tap*.md"):
    m = re.match(r"^Tap(\d+)$", b.parent.name)
    if m:
        bangs[int(m.group(1))] = b.stat().st_mtime

# --- 6. San xuat ---
prod = {}
for d in SX.iterdir():
    if not d.is_dir():
        continue
    m = re.match(r"^Tap(\d+)$", d.name)
    if not m:
        continue
    t = int(m.group(1))
    xb = d / "xuat_ban"
    masters = []
    if xb.exists():
        for f in xb.iterdir():
            if f.is_file() and f.suffix.lower() in (".mp4", ".mp3", ".wav"):
                masters.append(f.name)
    prod[t] = {"masters": sorted(masters), "xb": xb.exists()}

# --- 7. Tap moi trong kich ban ---
print("=== TAP TRONG KICH BAN (Ho_So_Toi_Pham) ===")
print("so thu muc Tap: %d" % len(scripts))
print()
print("tap\tcau\tshot\tjob\tanh\tbang\tmaster")
tot_job = tot_img = 0
need = []
for t in sorted(set(list(scripts.keys()) + list(jobs.keys()) + list(img_by_tap.keys()))):
    s = scripts.get(t, {})
    nj = jobs.get(t)
    ni = len(img_by_tap.get(t, []))
    tot_job += nj or 0
    tot_img += ni
    if nj is not None and ni < nj:
        need.append((t, nj, ni, nj - ni))
    print("%d\t%s\t%s\t%s\t%s\t%s\t%s" % (
        t, s.get("dialogues", "-"), shots.get(t, "-"), nj if nj is not None else "-", ni,
        "Y" if t in bangs else "-",
        ",".join(prod.get(t, {}).get("masters", [])) or "-"))
print()
print("TONG job (taps co bg_jobs): %d" % tot_job)
print("TONG anh nen theo tien to tap: %d" % tot_img)
print("Anh nen goc khong theo tap: %d" % other)
print("TONG file goc assets/bg: %d" % len(root_all))
print("Tong tap can sinh anh: %d tap / %d anh" % (len(need), sum(x[3] for x in need)))
for t, nj, ni, d in need:
    print("   tap %d: %d/%d thieu %d" % (t, ni, nj, d))
print()
print("=== TAP CO DU 100% ANH ===")
full = sorted([t for t in img_by_tap if jobs.get(t) and len(img_by_tap[t]) >= jobs[t]])
print(", ".join(str(t) for t in full), "=> %d tap" % len(full))
print()
print("=== TAP DANG DUNG / MOI ===")
for t in sorted(set(list(jobs.keys()) + list(img_by_tap.keys()))):
    if t > 60:
        print("  tap", t, "job=", jobs.get(t), "anh=", len(img_by_tap.get(t, [])))
