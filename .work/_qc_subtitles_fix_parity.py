#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L9: sua subtitles.py -> phai kiem hoi quy Tap 01 (va Tap 02 VN/EN).

So sanh byte SRT tru/sau cho moi cap (lang, ep) co san timeline.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
BK = W / "_cu" / "subtitles_fix_20261102"
BK.mkdir(parents=True, exist_ok=True)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
PY = sys.executable

# (lang, ep) -> duong dan SRT dich
CASES = [
    ("vi", "01", "02_SAN_XUAT/Tap01/xuat_ban/Tap01.srt"),
    ("ja", "01", "02_SAN_XUAT/Tap01_JA/xuat_ban/Tap01_JA.srt"),
    ("vi", "02", "02_SAN_XUAT/Tap02/xuat_ban/Tap02.srt"),
    ("ja", "02", "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt"),
    ("en", "02", "02_SAN_XUAT/Tap02_EN/xuat_ban/Tap02_EN.srt"),
]

print("=== 1. LUU BAN CU (baseline) ===")
for lang, ep, rel in CASES:
    p = ROOT / rel
    if p.exists():
        dst = BK / f"{lang}_{ep}_{p.name}"
        shutil.copy2(p, dst)
        print(f"  {lang}{ep}: {rel} ({p.stat().st_size} byte)")
    else:
        print(f"  {lang}{ep}: KHONG CO {rel}")

print("\n=== 2. SINH LAI ===")
for lang, ep, rel in CASES:
    env = dict(os.environ)
    env["AE_LANG"] = lang
    env["AE_EP"] = ep
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([PY, str(W / "subtitles.py")], cwd=ROOT, env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(f"  {lang}{ep}: rc={r.returncode} {r.stdout.strip()[:90]}")
    if r.returncode != 0:
        print("     ", (r.stderr or "")[-600:])

print("\n=== 3. SO SANH ===")
allok = True
for lang, ep, rel in CASES:
    p = ROOT / rel
    base = BK / f"{lang}_{ep}_{p.name}"
    if not base.exists() or not p.exists():
        print(f"  {lang}{ep}: bo qua (khong co baseline)")
        continue
    b = base.read_bytes()
    a = p.read_bytes()
    same = b == a
    if not same:
        allok = False
        bt = b.decode("utf-8-sig", errors="replace").replace("\r\n", "\n")
        at = a.decode("utf-8-sig", errors="replace").replace("\r\n", "\n")
        bb = bt.strip().split("\n\n")
        ab = at.strip().split("\n\n")
        print(f"  {lang}{ep}: KHAC ({len(bb)} -> {len(ab)} khoi)")
        n = 0
        for i, (x, y) in enumerate(zip(bb, ab), 1):
            if x != y:
                n += 1
                if n <= 4:
                    print(f"     khoi {i}:\n       CU : {x!r}\n       MOI: {y!r}")
        if len(bb) != len(ab):
            print(f"     len khac: {len(bb)} vs {len(ab)}")
    else:
        print(f"  {lang}{ep}: y NGUYEN byte ({len(a)} byte)")

print("\n=== 4. KIEM BLOCK LO (moi phai 0) ===")
for lang, ep, rel in CASES:
    p = ROOT / rel
    if not p.exists():
        continue
    txt = p.read_bytes().decode("utf-8-sig", errors="replace").replace("\r\n", "\n")
    bl = [x for x in txt.strip().split("\n\n") if x.strip()]
    bad = [i for i, x in enumerate(bl, 1) if len(x.splitlines()) < 3 or " --> " not in x.splitlines()[1]]
    blank = [i for i, x in enumerate(bl, 1) if any(ln.strip() == "" for ln in x.splitlines()[2:])]
    print(f"  {lang}{ep}: {len(bl)} khoi · lo={len(bad)} {bad[:5]} · dong trong={len(blank)} {blank[:5]}")
    if bad or blank:
        allok = False

print("\nKET QUA:", "PASS" if allok else "CO THAY DOI - can review")
