#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sánh bảng shot VN / EN / JA: NỀN có dùng chung không, CHỮ TRÊN HÌNH có khác không."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
SB = ROOT / "02_SAN_XUAT"


def rows_of(plan: Path):
    if not plan.exists():
        return None
    txt = plan.read_text(encoding="utf-8")
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", txt, re.M)
    if not m:
        return None
    sec = txt[m.end():]
    t = re.search(r"^\*\*Tổng:", sec, re.M)
    if t:
        sec = sec[: t.start()]
    out = {}
    for line in sec.splitlines():
        if re.match(r"\|\s*\d-\d+", line):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            out[c[0]] = {"bg": c[4], "text": c[5], "tmpl": c[3]}
    return out


VN = rows_of(SB / "Tap03" / "KeHoach_Video_Tap03.md")
EN = rows_of(SB / "Tap03_EN" / "KeHoach_Video_Tap03_EN.md")
JA = rows_of(SB / "Tap03_JA" / "KeHoach_Video_Tap03_JA.md")
KO = rows_of(SB / "Tap03_KO" / "KeHoach_Video_Tap03_KO.md")

print("=" * 78)
print("1) BẢNG SHOT TỒN TẠI?")
for tag, d in (("VN", VN), ("EN", EN), ("JA", JA), ("KO", KO)):
    p = {k: v for k, v in (d or {}).items()}
    print(f"  {tag}: {'CÓ' if d else 'KHÔNG CÓ hồ sơ'}  ({len(p)} dòng shot)")

print("\n" + "=" * 78)
print("2) NỀN (bg) CÓ DÙNG CHUNG KHÔNG?")
for tag, d in (("EN", EN), ("JA", JA)):
    if not d or not VN:
        continue
    common = set(VN) & set(d)
    same_bg = [k for k in common if VN[k]["bg"] == d[k]["bg"]]
    diff_bg = [k for k in common if VN[k]["bg"] != d[k]["bg"]]
    only = set(d) - set(VN)
    print(f"  VN vs {tag}: chung {len(common)} shot · nền GIỐNG {len(same_bg)} · nền KHÁC {len(diff_bg)} · chỉ có ở {tag}: {sorted(only)}")
    for k in diff_bg[:6]:
        print(f"      {k}: VN={VN[k]['bg']}  |  {tag}={d[k]['bg']}")

print("\n" + "=" * 78)
print("3) CHỮ TRÊN HÌNH CÓ GIỐNG KHÔNG?")
for tag, d in (("EN", EN), ("JA", JA)):
    if not d or not VN:
        continue
    common = sorted(set(VN) & set(d))
    same = [k for k in common if VN[k]["text"] == d[k]["text"]]
    print(f"  VN vs {tag}: {len(common)} shot chung · chữ GIỐNG {len(same)} · chữ KHÁC {len(common)-len(same)}")
    for k in common[:4]:
        if VN[k]["text"] != d[k]["text"]:
            print(f"      {k} [{VN[k]['tmpl']}]")
            print(f"        VN : {VN[k]['text'][:105]}")
            print(f"        {tag}: {d[k]['text'][:105]}")

print("\n" + "=" * 78)
print("4) ẢNH TĨNH ĐÃ DỰNG — MỖI BẢN MỘT BỘ RIÊNG?")
for tag, folder in (("VN", "video3_t03"), ("EN", "video3_EN_t03"), ("JA", "video3_JA_t03"), ("KO", "video3_KO_t03")):
    d = ROOT / ".work" / folder / "stills"
    n = len(list(d.glob("shot_*.png"))) if d.exists() else 0
    mtimes = sorted((p.stat().st_mtime for p in d.glob("shot_*.png"))) if d.exists() else []
    last = __import__("datetime").datetime.fromtimestamp(mtimes[-1]).strftime("%d/%m %H:%M") if mtimes else "-"
    print(f"  {tag}: {n:>4} ảnh  ({folder})  render gần nhất: {last}")
