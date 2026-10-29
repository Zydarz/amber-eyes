#!/usr/bin/env python3
"""QC parity cho toàn bộ bản tiếng Hàn (Tập 01 – 29).

    usage: py -3 .work/_qc_ko_all.py

Chạy _qc_ko_parity.py cho từng tập có file KO, in bảng tổng kết.
Exit 0 = tất cả PASS.
"""
import io
import os
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:\TEST\Gax\Audi")
KB = ROOT / "01_KICH_BAN"
QC = ROOT / ".work" / "_qc_ko_parity.py"

# tập -> file nguồn tiếng Việt (bản đang dùng)
SRC = {
    "01": "Tap01/kichban_tap01_22102026_v2.md",
    "02": "Tap02/kichban_tap02_22102026.md",
    "03": "Tap03/kichban_tap03_22102026.md",
}
for n in range(4, 30):
    SRC[f"{n:02d}"] = f"Tap{n:02d}/kichban_tap{n:02d}_23102026.md"

rows = []
for ep in sorted(SRC):
    src = KB / SRC[ep]
    ko = KB / f"Tap{ep}_KO" / f"kichban_tap{ep}_KO.md"
    if not src.exists():
        rows.append((ep, "SOURCE-MISSING", "", ""))
        continue
    if not ko.exists():
        rows.append((ep, "NO-KO-FILE", "", ""))
        continue
    p = subprocess.run([sys.executable, str(QC), str(src), str(ko), "--quiet"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = p.stdout or ""
    m = re.search(r"PASS\s+\S+\s+—\s+(\d+) elements,\s+(\d+) sentences", out)
    fails = re.findall(r"^FAIL\s+(.*)$", out, re.M)
    warns = re.findall(r"^WARN\s+(.*)$", out, re.M)
    status = "PASS" if p.returncode == 0 else "FAIL"
    rows.append((ep, status, f"{m.group(1)} el / {m.group(2)} câu" if m else "",
                 " · ".join(f[:70] for f in fails[:2])))

w = max(len(r[0]) for r in rows)
print(f"{'Tập':<{w}}  {'KQ':<6}  {'Phần tử / câu':<20} Ghi chú")
print("-" * (w + 62))
npass = 0
for ep, st, cnt, note in rows:
    if st == "PASS":
        npass += 1
    print(f"{ep:<{w}}  {st:<6}  {cnt:<20} {note}")
print("-" * (w + 62))
print(f"PASS {npass}/{len(rows)}")
sys.exit(0 if npass == len(rows) else 1)
