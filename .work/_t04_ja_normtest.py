#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thử nghiệm hành norm() của QC với tiếng Nhật."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return " ".join(s.split())


tests = [
    "2003年秋。",
    "43歳のその男は痩せ型で声は小さく",
    "連続11回の終身刑、最低服役期間397年を言い渡しました。",
    "第1段階：内面崩壊と薬品の不正持ち出し。",
    "アメリカ合衆国ニュージャージー州サマービルのサマセット医療センター（Somerset Medical Center）。",
    "2003年10月。",
]
for t in tests:
    print(repr(t), "->", norm(t).split())
