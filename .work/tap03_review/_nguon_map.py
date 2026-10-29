#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đối chiếu bảng nguồn Tập 03 với kịch bản đã parse lại: tìm mã câu ĐÚNG cho từng dòng.
Kịch bản đã sửa 21 lỗi fact + bổ sung 1 567 từ ⇒ mã element/câu đã dịch, bảng nguồn cũ sai."""
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
MD = ROOT / "02_SAN_XUAT" / "Tap03" / "xuat_ban" / "nguon_tham_khao.md"
PARSED = json.loads((ROOT / ".work" / "tap03_review" / "parsed_final.json").read_text(encoding="utf-8"))

sents = []
for e in PARSED:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sents.append((s["id"], s["text"]))


def norm(t):
    t = t.replace("“", '"').replace("”", '"').replace("’", "'")
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t


rows = []
for line in MD.read_text(encoding="utf-8").splitlines():
    m = re.match(r"^\|\s*`([\d.]+#\d+)`\s*\|(.*?)\|\s*\|", line)
    if m:
        rows.append((m.group(1), m.group(2).strip()))

print(f"Bang nguon co {len(rows)} dong co ma cau\n")
fixed, unmatched = {}, []
for old, body in rows:
    nb = norm(body)
    hit = None
    for sid, txt in sents:
        nt = norm(txt)
        if nb and (nt.startswith(nb[:60]) or nb.startswith(nt[:60])):
            hit = sid
            break
    if hit is None:
        # doi chieu theo do dai: tim cau nao chua toan bo phan dau cua dong
        for sid, txt in sents:
            nt = norm(txt)
            if len(nb) > 40 and len(nt) > 40 and nb[:40] in nt:
                hit = sid
                break
    if hit is None:
        unmatched.append((old, body[:70]))
    elif hit != old:
        fixed[old] = hit

print("--- MA SAI, can sua ---")
for old, new in fixed.items():
    print(f"  {old:<10} -> {new}")
print(f"\n--- KHONG DOI CHIEU DUOC ({len(unmatched)}) ---")
for old, b in unmatched:
    print(f"  {old:<10} {b}")

out = {"fixed": fixed, "unmatched": unmatched}
(ROOT / ".work" / "tap03_review" / "_nguon_fix.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("\nTong can sua:", len(fixed))
