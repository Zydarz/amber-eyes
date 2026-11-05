#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — soi token của câu trong kichban (nguồn giống hệt QC) cho các mảnh lỗi."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

idx = {}
for el in parse_file(str(ROOT / "01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md")):
    if el["kind"] == "LOI":
        idx[el["id"]] = [(s["id"], s["text"]) for s in el.get("sentences", [])]


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return " ".join(s.split())


def show(eid, a, b, frag):
    print(f"--- {eid} #{a}-{b} | frag: {frag}")
    ctx = " ".join(t for _, t in idx[eid][a - 1:b])
    print("   ctx tokens:", norm(ctx).split())
    print("   frag tokens:", norm(frag).split())


show("1.16", 4, 5, "同時私たちは")
show("1.16", 4, 5, "同時に私たちは")
show("2.06", 4, 6, "Norepinephrine")
show("2.06", 6, 6, "我々の行動分析により彼の凶行は突発的ではなく")
show("2.08", 7, 7, "コード・ブルー")
show("3.02", 4, 6, "彼は不幸な運命に安らかな死をもたらす慈悲の天使の自画像を意図的に描き出そうとしたのです")
show("3.09", 9, 9, "そしてこの巧妙な自己欺瞞こそが一度の真の後悔すら抱かせぬまま")
show("4.04", 1, 3, "CullenのPyxis端末ログを目前に広げた時")
show("4.12", 5, 7, "DigoxinやInsulinを用いてFlorian Gall神父やMichael Strenko")
show("5.05", 1, 3, "経済利益に支配された医療機関の")
