# -*- coding: utf-8 -*-
"""Kiem bang markdown: ERROR = o thua (bi GFM bo mat), WARN = o thieu (GFM them o rong)."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding="utf-8")

SPLIT = re.compile(r"(?<!\\)\|")

def cells(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip() for c in SPLIT.split(s)]

total_err = 0
for rel in ["AGENTS.md", "00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md", "README.md"]:
    p = ROOT / rel
    raw = p.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    crcrlf = raw.count(b"\r\r\n")
    lines = raw.decode("utf-8").split("\r\n")
    print(f"\n=== {rel} | BOM={bom} CRCRLF={crcrlf} | dong={len(lines)} ===")
    i = 0
    err = warn = 0
    ntab = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1]):
            ncol = len(cells(ln))
            j = i + 2
            rows = 0
            while j < len(lines) and lines[j].startswith("|"):
                nc = len(cells(lines[j]))
                if nc > ncol:
                    print(f"  ERROR dòng {j+1}: {nc} ô > {ncol} cột (ô thừa bị mất) -> {lines[j][:70]}")
                    err += 1
                elif nc < ncol:
                    print(f"  WARN  dòng {j+1}: {nc} ô < {ncol} cột (GFM thêm ô rỗng) -> {lines[j][:60]}")
                    warn += 1
                rows += 1
                j += 1
            ntab += 1
            i = j
        else:
            i += 1
    total_err += err
    print(f"  => {ntab} bảng | ERROR {err} | WARN {warn}")

print(f"\nTỔNG ERROR (mất nội dung): {total_err}")
