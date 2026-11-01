#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vá qc_tap04.py: so `alt` cua acting voi cau o dang lời ĐỌC đã chuẩn hoá.

Ly do: script giu dau nhay (cho chu tren hinh), lời doc bo dau nhay (G1) va
them the nhip <#0.35#> -> <|prosody:pause|>. So tho => 2 can bao sai.
Sua: chuan hoa hai ve (bo the nhip, bo dau nhay, ghep khoang trang) roi so.
"""
import pathlib
import py_compile
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
p = ROOT / ".work" / "qc_tap04.py"
s = p.read_text(encoding="utf-8", newline="")
E = "\r\r\n" if "\r\r\n" in s else ("\r\n" if "\r\n" in s else "\n")
print("line ending:", repr(E))

old = (E.join([
    '        if alt and re.sub(r"<\\|[^|]*\\|>", "", str(alt)).strip() != sent[k][0].strip():',
]))
new = (E.join([
    '        if alt and _spoken(str(alt)) != _spoken(sent[k][0]):',
]))
if s.count(old) != 1:
    sys.exit("!! khong tim thay anchor so alt (%d)" % s.count(old))
s = s.replace(old, new)

helper = (E.join([
    "def _spoken(t):",
    '    """Chuẩn hoá lời đọc: bỏ thẻ nhịp (MiniMax <#0.35#> / Higgs <|prosody:pause|>),',
    "",
    "    bỏ dấu nháy kép, gộp khoảng trắng. Script giữ nháy (chữ trên hình),",
    "    lời đọc thì không (G1) — nên phải so ở dạng đã chuẩn hoá.",
    '    """',
    '    t = re.sub(r"<#[^#]*#>|<\\|[^|]*\\|>", " ", str(t))',
    '    t = t.replace("“", "").replace("”", "").replace(chr(34), "")',
    '    return re.sub(r"\\s+", " ", t).strip()',
    "",
    "",
]))
anchor = "def script_sentences(script):"
if s.count(anchor) != 1:
    sys.exit("!! khong tim thay anchor script_sentences")
s = s.replace(anchor, helper + anchor)

p.write_text(s, encoding="utf-8", newline="")
py_compile.compile(str(p), doraise=True)
print("py_compile OK")
