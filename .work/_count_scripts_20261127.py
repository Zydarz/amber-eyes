#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dem cau thoai / tu / hoi cho Tap 69 va series Bay Tam Ly Va Hanh Vi (140 tap)."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ROLE_RE = re.compile(r"^\*\*([^*]{2,30})\*\*[^:\n]*:\s*$")

def count_md(path):
    txt = path.read_text(encoding="utf-8", errors="replace")
    lines = txt.splitlines()
    n_dialog = 0
    roles = {}
    in_quote = False
    words = 0
    for i, ln in enumerate(lines):
        s = ln.strip()
        m = ROLE_RE.match(s)
        if m:
            n_dialog += 1
            roles[m.group(1)] = roles.get(m.group(1), 0) + 1
        # dong thoai: dong quoted sau role
        if s.startswith('"'):
            body = s.strip('"')
            words += len(body.split())
        if s == '"""':
            in_quote = not in_quote
    hoi = len(re.findall(r"^##+\s*HỒI\s*\d+", txt, re.M | re.I))
    chidau = len(re.findall(r"chỉ dấu", txt, re.I))
    return dict(dialog=n_dialog, roles=roles, words=words, hoi=hoi, chidau=chidau,
                lines=len(lines), bytes=path.stat().st_size)

print("=== TAP 69 ===")
p = ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap69" / "kichban_tap69.md"
if p.exists():
    r = count_md(p)
    print(r)

print()
print("=== SERIES BAY TAM LY VA HANH VI (140 tap) ===")
base = ROOT / "01_KICH_BAN" / "BayTamLyVaHanhVi"
taps = sorted([d for d in base.rglob("Tap*") if d.is_dir()],
              key=lambda d: int(re.search(r"Tap(\d+)", d.name).group(1)))
tot_d = tot_w = 0
n_ok = 0
per = []
for d in taps:
    f = d / ("kichban_tap%s.md" % re.search(r"Tap(\d+)", d.name).group(1))
    if not f.exists():
        cand = list(d.glob("kichban*.md"))
        f = cand[0] if cand else None
    if not f:
        per.append((d.name, None))
        continue
    r = count_md(f)
    tot_d += r["dialog"]
    tot_w += r["words"]
    n_ok += 1
    per.append((d.name, r["dialog"], r["words"], r["hoi"]))
print("so tap co kichban: %d / %d" % (n_ok, len(taps)))
print("TONG cau thoai: %d" % tot_d)
print("TONG tu (uoc): %d" % tot_w)
print("tap khong co kichban:", [x[0] for x in per if x[1] is None])
print()
print("mau 8 tap dau / 8 tap cuoi:")
for x in per[:8] + per[-8:]:
    print("  ", x)

print()
print("=== REVIEW files ===")
rev = list(base.rglob("REVIEW*.md"))
print("so file REVIEW:", len(rev))
