#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vá package.py (nhánh tiếng Việt) để đọc nguồn đã kiểm chứng từ file thật.

- Thêm hàm sources_vn(): đọc 02_SAN_XUAT/<Tập>/nguon_mo_ta.txt (khối chèn vào mô tả)
  và 02_SAN_XUAT/<Tập>/nguon_tham_khao.md (bảng đối chiếu từng câu).
- description(): thay placeholder "[CHƯA CÓ — ...]" bằng {src_block}.
- description(): nếu có bảng nguồn thật thì copy sang xuat_ban/nguon_tham_khao.md,
  nếu không thì giữ nguyên hành vi cũ (sinh khung rỗng).

Giu nguyên hệ xuống dòng gốc (file có \r\n lẫn \r\r\n).
"""
import pathlib
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
P = ROOT / ".work" / "package.py"

BK = ROOT / ".work" / "_cu"
BK.mkdir(parents=True, exist_ok=True)
stamp = time.strftime("%Y%m%d_%H%M%S")
shutil.copy2(P, BK / f"package.py.bak_{stamp}")
print("backup ->", BK / f"package.py.bak_{stamp}")

raw = P.read_bytes().decode("utf-8")
orig_len = len(raw)


def eol_before(text, pos):
    """Kieu ket thuc dong ngay truoc pos (giu nguyen \r\n / \r\r\n / \n)."""
    i = text.rfind("\n", 0, pos)
    if i < 0:
        return "\n"
    seg = text[max(0, i - 2):i + 1]
    if seg.endswith("\r\r\n"):
        return "\r\r\n"
    if seg.endswith("\r\n"):
        return "\r\n"
    return "\n"


FUNC_LINES = [
    "def sources_vn():",
    '    """Nguon da kiem chung cho ban tieng Viet.',
    "",
    "    Doc `02_SAN_XUAT/<Tap>/nguon_mo_ta.txt` (khoi chen vao muc NGUON THAM KHAO)",
    "    va `02_SAN_XUAT/<Tap>/nguon_tham_khao.md` (bang doi chieu tung cau).",
    "    Khong co file => tra ve khung rong nhu truoc. KHONG bia nguon.",
    '    """',
    '    blk_p = ED.EP_DIR / "nguon_mo_ta.txt"',
    '    tbl_p = ED.EP_DIR / "nguon_tham_khao.md"',
    '    block = blk_p.read_text(encoding="utf-8").strip() if blk_p.exists() else ""',
    '    table = tbl_p.read_text(encoding="utf-8").strip() if tbl_p.exists() else ""',
    "    if not block:",
    '        block = ("[CHUA CO - phai bo sung nguon cong khai da kiem chung truoc khi dang, "',
    '                 "xem nguon_tham_khao.md]")',
    '    return block, (table + "\\n") if table else ""',
    "",
    "",
]

# --- 1. chen ham truoc def description(): -------------------------------------
m = re.search(r"^def description\(\):", raw, flags=re.M)
assert m, "khong tim thay def description()"
eol = eol_before(raw, m.start())
raw = raw[:m.start()] + eol.join(FUNC_LINES) + eol + raw[m.start():]
print(f"1) chen ham sources_vn()  [eol={eol!r}]")

# --- 2. gan src_block trong description() ------------------------------------
ANCHOR = "        return description_en()"
assert raw.count(ANCHOR) == 1, f"so lan anchor = {raw.count(ANCHOR)}"
eol2 = eol_before(raw, raw.index(ANCHOR))
raw = raw.replace(ANCHOR, ANCHOR + eol2 + "    src_block, src_table = sources_vn()")
print("2) gan src_block, src_table")

# --- 3. thay placeholder bang {src_block} ------------------------------------
PH = "[CHƯA CÓ — phải bổ sung nguồn công khai đã kiểm chứng trước khi đăng, xem nguon_tham_khao.md]"
assert raw.count(PH) == 1, f"so lan placeholder = {raw.count(PH)}"
raw = raw.replace(PH, "{src_block}")
print("3) thay placeholder -> {src_block}")

# --- 4. nguon_tham_khao.md: copy bang that neu co ---------------------------
OLD_WRITE = '    (OUT_DIR / "nguon_tham_khao.md").write_text("\\n".join(md) + "\\n", encoding="utf-8")'
assert raw.count(OLD_WRITE) == 1, f"so lan write = {raw.count(OLD_WRITE)}"
eol4 = eol_before(raw, raw.index(OLD_WRITE))
NEW_WRITE = eol4.join([
    "    if src_table:",
    '        (OUT_DIR / "nguon_tham_khao.md").write_text(src_table, encoding="utf-8")',
    "    else:",
    '        (OUT_DIR / "nguon_tham_khao.md").write_text("\\n".join(md) + "\\n", encoding="utf-8")',
])
raw = raw.replace(OLD_WRITE, NEW_WRITE)
print("4) nguon xuat ban/nguon_tham_khao.md")

P.write_bytes(raw.encode("utf-8"))
print(f"package.py: {orig_len} -> {len(raw)} byte")
print("OK")
