#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dry-run: parse 29 kịch bản VN, kiểm tra đếm câu + render vòng tròn (không gọi LLM)."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

OUT = Path(__file__).parent / "_ja_dry.txt"
lines = []
tot_sent = 0
for i in range(1, 30):
    ep = f"{i:02d}"
    src = M.canonical_vn(ep)
    units = M.parse_units(src)
    for u in units:
        if u["kind"] == "TEXT":
            u["n"] = M.count_sentences_vi(u["vi"])
    dia = [u for u in units if u["kind"] == "TEXT"]
    kinds = {}
    for u in units:
        kinds[u["kind"]] = kinds.get(u["kind"], 0) + 1
    n_sent = sum(u["n"] for u in dia)
    tot_sent += n_sent
    zero = [u["vi"][:70] for u in dia if u["n"] == 0]
    for u in units:
        u["ja"] = u.get("vi", "")
    md = M.render(units)
    n_lines_src = len(src.read_text(encoding="utf-8").splitlines())
    lines.append(f"Tap{ep} | {src.name} | dòng={len(units)}/{n_lines_src} | thoại={len(dia)} | câu={n_sent} | "
                 f"0câu={len(zero)} | {kinds}")
    for z in zero[:2]:
        lines.append(f"      0CÂU: {z}")
    if ep == "01":
        lines.append("--- render mẫu Tap01 (40 dòng đầu) ---")
        lines.extend(md.splitlines()[:40])
        lines.append("--- hết mẫu ---")

lines.append(f"TỔNG câu 29 tập = {tot_sent}")
OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"written {OUT} · tổng câu = {tot_sent}")
