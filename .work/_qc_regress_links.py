#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem hoi quy (L9) cho thay doi `verified_links()` trong package.py.

Kiem tra 2 chieu:
  (1) MOI tap EN: link moi sinh == link dang co trong mo_ta.txt tren dia
      (tru Tap03_EN, dang bi [PENDING] do bug).
  (2) So sanh ham CU voi ham MOI tren TAT CA file nguon EN/JA/KO:
      khac biet duy nhat phai la tap bi gap link (khong duoc mat link nao).
"""
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
os.environ.update({"AE_EP": "03", "AE_LANG": "en"})
import package as PK  # noqa: E402


def old_verified_links(src_p: Path) -> list:
    """Ban CU cua verified_links() ( dung y 4 cot, nguyen ban commit )."""
    links = []
    if not src_p.exists():
        return links
    for row in src_p.read_text(encoding="utf-8").splitlines():
        if (row.startswith("| `") or row.startswith("| Mô tả") or row.startswith("| `1.")
                or row.startswith("| `2.") or row.startswith("| `3.")
                or row.startswith("| `4.") or row.startswith("| `5.")):
            cells = [c.strip() for c in row.strip("|").split("|")]
            if len(cells) >= 4 and cells[3].startswith("✅"):
                for u in re.findall(r"https?://\S+", cells[2]):
                    if u not in links:
                        links.append(u)
    return links


def new_verified_links(src_p: Path) -> list:
    links = []
    if not src_p.exists():
        return links
    for row in src_p.read_text(encoding="utf-8").splitlines():
        if not row.startswith("|"):
            continue
        cells = [c.strip() for c in row.strip("|").split("|")]
        urls = []
        if (row.startswith("| `") or row.startswith("| Mô tả")
                or row.startswith("| `1.") or row.startswith("| `2.")
                or row.startswith("| `3.") or row.startswith("| `4.")
                or row.startswith("| `5.")):
            if len(cells) >= 4 and cells[3].startswith("✅"):
                urls = re.findall(r"https?://\S+", cells[2])
        elif len(cells) == 3 and cells[2].startswith("✅") and cells[0].startswith("http"):
            urls = re.findall(r"https?://\S+", cells[0])
        for u in urls:
            if u not in links:
                links.append(u)
    return links


EN = ROOT / "02_SAN_XUAT"
bad = 0
print("=== (1) moi tap EN: link moi == link trong mo_ta.txt tren dia ===")
for d in sorted(EN.glob("Tap*_EN")):
    src = d / "nguon_tham_khao_EN.md"
    mo = d / "xuat_ban" / "mo_ta.txt"
    if not src.exists() or not mo.exists():
        print(f"  {d.name:10} bo qua (thieu file)")
        continue
    new = new_verified_links(src)
    t = mo.read_text(encoding="utf-8")
    # CHI lay khong "SOURCES" (dung den dong trong), bo qua khoi hotlines phia sau
    blk = ""
    if "SOURCES" in t:
        blk = t.split("SOURCES", 1)[1].split("\n\n", 1)[0]
    on_disk = re.findall(r"https?://\S+", blk)
    seen, uniq = set(), []
    for u in on_disk:
        if u not in seen:
            seen.add(u)
            uniq.append(u)
    same = uniq == new
    note = ""
    if not same and len(new) > len(uniq):
        note = "  <-- MOI DUNG them (truoc khi la [PENDING])"
    elif not same:
        note = "  <-- KHAC"
        bad += 1
    print(f"  {d.name:10} moi={len(new):3}  tren dia={len(uniq):3}  "
          f"{'GIONG' if same else 'KHAC'}{note}")

print()
print("=== (2) CU vs MOI tren tat ca file nguon EN/JA/KO ===")
tot_old = tot_new = 0
for d in sorted(EN.glob("Tap*")):
    for suf in ("_EN", "_JA", "_KO", ""):
        src = d / f"nguon_tham_khao{suf}.md"
        if not src.exists():
            continue
        o, n = old_verified_links(src), new_verified_links(src)
        tot_old += len(o)
        tot_new += len(n)
        lost = [u for u in o if u not in n]
        if lost:
            bad += 1
            print(f"  {d.name}{suf}: MAT {len(lost)} link cu")
        if n != o and not lost:
            print(f"  {d.name}{suf}: +{len(n) - len(o)} link moi (khong mat link nao)")
print(f"  tong: CU={tot_old} · MOI={tot_new} · mat={tot_old - tot_new}")

print()
print("KET QUA:", "PASS - khong mat link nao" if bad == 0 else f"LOI - {bad} van de")
sys.exit(0 if bad == 0 else 1)
