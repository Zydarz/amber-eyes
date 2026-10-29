#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chẩn đoán chi tiết các cờ QC của _qc_ja.py cho 1 tập, kèm ngữ cảnh."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402
from _qc_ja import SIMPLIFIED, VN_CHARS  # noqa: E402

ep = sys.argv[1] if len(sys.argv) > 1 else "01"
ja = M.ROOT / "01_KICH_BAN" / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
vn = M.canonical_vn(ep)
body = re.sub(r"<!--.*?-->", "", ja.read_text(encoding="utf-8"), flags=re.S)
vn_text = vn.read_text(encoding="utf-8")

print(f"===== Tap{ep} =====")
hits = {}
for c in body:
    if c in SIMPLIFIED:
        hits.setdefault(c, 0)
        hits[c] += 1
print("\n-- chữ Hán giả thạch bị gắn cờ --")
for c, n in sorted(hits.items(), key=lambda kv: -kv[1]):
    i = body.find(c)
    print(f"  {c!r} x{n}   ctx: ...{body[max(0,i-30):i+30]!r}...")

print("\n-- ký tự tiếng Việt sót lại --")
vb = sorted({c for c in body if c in VN_CHARS or "1E00" <= f"{ord(c):04X}" <= "1EFF"})
print("  ", vb if vb else "không có")

print("\n-- Latin trong tiếng Nhật (theo regex QC) --")
junk = re.findall(r"[぀-ヿ一-鿿][A-Z]{2,}[぀-ヿ一-鿿]|[一-鿿]-[A-Za-z]{2,}", body)
for j in junk[:20]:
    i = body.find(j)
    print(f"  {j!r}   ctx: ...{body[max(0,i-40):i+40]!r}...")

print("\n-- Latin lạ (KHÔNG có trong file VN) --")
vn_latin = set(re.findall(r"[A-Za-z][A-Za-z0-9\-'.]{1,}", vn_text))
bad_latin = sorted({w for w in re.findall(r"[A-Za-z][A-Za-z0-9\-'.]{1,}", body)
                    if w not in vn_latin and not w.islower()})
print("  ", bad_latin[:40] if bad_latin else "không có")

print("\n-- chữ Hán giả mà Nhật cũng dùng (kiểm tra thủ công) --")
JP_OK = set("点断声术検実両図圧効気対発国学童医")
for c in sorted(hits):
    print(f"  {c}  {'<- Kanji Nhật hợp lệ, bỏ khỏi danh sách' if c in JP_OK else '<- thật'}")
