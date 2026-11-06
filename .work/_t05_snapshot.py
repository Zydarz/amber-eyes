#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 05 — chụp lại bảng shot CŨ (trước khi viết lại) vào file JSON ổn định.

Bẫy: writer đọc "bảng cũ" từ chính file nó ghi => chạy 2 lần là dòng dịch chuyển.
Cách đúng: chụp 1 lần từ git HEAD (bản gốc) rồi writer luôn đọc từ snapshot.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

FILES = {
    "vi": "02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md",
    "en": "02_SAN_XUAT/Tap05_EN/KeHoach_Video_Tap05_EN.md",
    "ja": "02_SAN_XUAT/Tap05_JA/KeHoach_Video_Tap05_JA.md",
}


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def rows_from(text):
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
    if not m:
        raise SystemExit("không tìm thấy mục 6")
    sec = text[m.end():]
    mt = re.search(r"^\*\*Tổng:", sec, re.M)
    if mt:
        sec = sec[: mt.start()]
    out = {}
    order = []
    for line in sec.splitlines():
        if re.match(r"\|\s*[1-5]-\d+", line):
            c = cells(line)
            out[c[0]] = c
            order.append(c[0])
    return out, order


for lang, rel in FILES.items():
    dst = W / f"_t05_old_rows_{lang}.json"
    try:
        txt = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT,
                             capture_output=True, text=True, encoding="utf-8",
                             check=True).stdout
        src = "git HEAD"
    except subprocess.CalledProcessError:
        txt = (ROOT / rel).read_text(encoding="utf-8")
        src = "file hiện tại"
    rows, order = rows_from(txt)
    dst.write_text(json.dumps({"src": src, "order": order, "rows": rows},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{lang}: {len(rows)} dòng ← {src} → {dst.name}")
