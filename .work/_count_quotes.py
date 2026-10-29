"""Báo cáo số dấu nháy và số gạch đầu dòng của file VN (để KO khớp chính xác)."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
LIST = re.compile(r"^\s*(?:\*\s{2,}|\d+\.\s{1,})\S")

for f in sys.argv[1:]:
    raw = Path(f).read_text(encoding="utf-8")
    straight = re.findall(r"'([^']{2,})'", raw)
    curly = re.findall("\u2018([^\u2019]{2,})\u2019", raw)
    dbl = re.findall(r'"([^"]{2,})"', raw)
    cdbl = re.findall("\u201c([^\u201d]{2,})\u201d", raw)
    items = [l for l in raw.splitlines() if LIST.match(l)]
    print(f"=== {f}")
    print(f"  straight ' : {len(straight)}  {straight}")
    print(f"  curly '\u2018' : {len(curly)}  {curly}")
    print(f"  double \"  : {len(dbl)}  {dbl}")
    print(f"  curly \"    : {len(cdbl)}  {cdbl}")
    print(f"  list items : {len(items)}")
    for l in items:
        print(f"      {l[:110]}")
    print()
