#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra glossary: giá trị JA có lẫn Latin/kana lạ không, và mục trùng."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
from ja_glossary import TERMS, ROLES_JA  # noqa: E402

OK_LATIN = re.compile(r"^[A-Z0-9\-.' ]+$")

print("-- giá trị JA có chữ Latin (kiểm tra tay) --")
for vi, ja in TERMS.items():
    lat = re.findall(r"[A-Za-z]+", ja)
    if lat and not OK_LATIN.match(ja):
        print(f"  {vi!r} -> {ja!r}   Latin: {lat}")

print("\n-- giá trị JA có kana lẫn ký tự Latin trong 1 từ (rác kiểu 'ムンハusen') --")
for vi, ja in TERMS.items():
    for w in re.findall(r"[ぁ-んァ-ヶ一-鿿]+[A-Za-z]+[ぁ-んァ-ヶ一-鿿]*", ja):
        print(f"  {vi!r} -> {ja!r}   từ rác: {w!r}")

print("\n-- giá trị JA rỗng / không có kanji-kana --")
for vi, ja in TERMS.items():
    if not ja.strip():
        print(f"  RỖNG: {vi!r}")

print("\n-- khoá trùng giá trị (có thể nhầm) --")
from collections import defaultdict  # noqa: E402
rev = defaultdict(list)
for vi, ja in TERMS.items():
    rev[ja].append(vi)
for ja, vis in rev.items():
    if len(vis) > 1:
        print(f"  {ja!r} <- {vis}")

print(f"\nTỔNG: {len(TERMS)} mục · {len(ROLES_JA)} vai")
