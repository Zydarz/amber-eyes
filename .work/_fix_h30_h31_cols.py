# -*- coding: utf-8 -*-
"""Sua H30/H31 trong AGENTS.md: bang luat chuan 3 o (| # | Luat | Bang chung |) - 2 dong moi co 4 o.

Gop o "BẮT BUỘC/Quy trình" vao o Luat, giu o Bang chung. Giu nguyen line-ending.
Dung: py -3 .work/_fix_h30_h31_cols.py
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = pathlib.Path(r"D:/TEST/Gax/amber-eyes/AGENTS.md")
raw = P.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
lines = raw.split(nl)

fixed = 0
for i, l in enumerate(lines):
    if l.startswith("| **H30** |") or l.startswith("| **H31** |"):
        cells = l.split("|")
        # cells: ['', ' **H30** ', ' luat ', ' quy trinh ', ' bang chung ', '']  (6 phan tu)
        if len(cells) == 6:
            cells[2] = cells[2].rstrip() + " " + cells[3].strip()
            del cells[3]
            lines[i] = "|".join(cells)
            fixed += 1
            print(f"dong {i+1}: gop o -> {len(lines[i].split('|'))-1} o")

P.write_text(nl.join(lines), encoding="utf-8", newline="")
print("da sua", fixed, "dong | CRCRLF:", P.read_text(encoding='utf-8').count("\r\r\n"))
