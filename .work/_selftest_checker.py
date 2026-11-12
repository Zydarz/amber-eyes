# -*- coding: utf-8 -*-
"""Tu kiem: checker co that su bat dong 'thua o' khong? (tren ban sao tam)"""
import re
import shutil
import sys
import tempfile
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

def scan(path):
    lines = Path(path).read_bytes().decode("utf-8").split("\r\n")
    i = 0
    err = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1]):
            ncol = len(cells(ln))
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                nc = len(cells(lines[j]))
                if nc > ncol:
                    err += 1
                    print(f"    ERROR dòng {j+1}: {nc} ô > {ncol}")
                j += 1
            i = j
        else:
            i += 1
    return err

tmp = Path(tempfile.mkdtemp())
src = ROOT / "00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md"
dst = tmp / "TIEU_CHUAN_DUNG_VIDEO.md"
shutil.copyfile(src, dst)
text = dst.read_bytes().decode("utf-8")
# inject 1 dong thua o (6 o) ngay sau dong A11 #138
bad = "| 138 | **Dung nghen** | A | B | C | D |"
assert text.count("| 138 |") == 1
text = text.replace("| 138 |", bad, 1)
with open(dst, "w", encoding="utf-8", newline="") as f:
    f.write(text)

print("ban sao tam co 1 dong thua o:")
err = scan(dst)
print(f"  => checker bat {err} loi (mong doi >= 1)")
print(f"  => file goc: {scan(src)} loi (mong doi 0)")
shutil.rmtree(tmp, ignore_errors=True)
assert err >= 1, "CHECKER KHONG BAT LOI -> khong tin duoc ket qua xanh"
print("SELFTEST OK")
