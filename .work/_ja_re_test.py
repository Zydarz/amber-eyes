#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import parse_kichban as PK

lines = Path(__file__).resolve().parents[1] / "01_KICH_BAN" / "Tap01_JA" / "kichban_tap01_JA.md".read_text(
    encoding="utf-8").splitlines()
heads = [l for l in lines if l.startswith("## ")]
print("tất cả heading:")
for h in heads:
    print("  ", repr(h[:44]), "act=", bool(re.match(r"^## (?:HỒI|ACT|막|第) (\d)", h.strip())))

pat = re.compile(r"^## (?:HỒI|ACT|막|第) (\d)")
print("mẫu thử:", bool(pat.match(heads[1].strip())))
print("mẫu thử (chỉ 第):", bool(re.match(r"^## (?:第) (\d)", heads[1].strip())))
print("mẫu thử (chỉ 第, không space):", bool(re.match(r"^##\s*第(\d)", heads[1].strip())))
print("mẫu thử (space linh hoat):", bool(re.match(r"^##\s+(?:HỒI|ACT|막|第)\s*(\d)", heads[1].strip())))
