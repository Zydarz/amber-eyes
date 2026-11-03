#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DRY-RUN: do do dai mo ta moi sinh cho tung tap EN (KHONG ghi file)."""
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))


def pick_block(tpl: str) -> str:
    """Sao chep logic pick_block cua package.py (khoi co CHAPTERS)."""
    best = None
    for m in re.finditer(r"```(?:text)?\n(.*?)```", tpl, re.S):
        if "CHAPTERS" in m.group(1):
            best = m.group(1)
    if best is None:
        raise SystemExit("khong tim thay khoi CHAPTERS trong template")
    return best


def links_from(src_p: Path):
    links = []
    if not src_p.exists():
        return links
    for row in src_p.read_text(encoding="utf-8").splitlines():
        if not row.startswith("|"):
            continue
        cells = [c.strip() for c in row.strip("|").split("|")]
        urls = []
        if len(cells) == 3 and cells[2].startswith("✅") and cells[0].startswith("http"):
            urls = re.findall(r"https?://\S+", cells[0])
        elif len(cells) >= 4 and cells[3].startswith("✅"):
            urls = re.findall(r"https?://\S+", cells[2])
        for u in urls:
            if u not in links:
                links.append(u)
    return links


EN = ROOT / "02_SAN_XUAT"
print(f"{'tap':10} {'template':>9} {'link':>5} {'do dai mo ta':>14}  trong 5000?")
for d in sorted(EN.glob("Tap*_EN")):
    tpls = list(d.glob("CHU_CO_DINH_EN.md"))
    src = d / "nguon_tham_khao_EN.md"
    if not tpls:
        print(f"{d.name:10} {'KHONG':>9} {'':>5} {'-':>14}  (khong co template)")
        continue
    body = pick_block(tpls[0].read_text(encoding="utf-8"))
    links = links_from(src)
    src_block = "📚 SOURCES\n" + ("\n".join(links) if links else "[PENDING]") + "\n\n"
    if "📚 SOURCES" in body:
        body = re.sub(r"📚 SOURCES\n(?:.*\n)*?(?=\n)", src_block, body, count=1)
    else:
        body = body + "\n" + src_block
    print(f"{d.name:10} {tpls[0].stat().st_size:9} {len(links):5} {len(body):14}  "
          f"{'OK' if len(body) <= 5000 else 'VUOT ' + str(len(body) - 5000)}")
