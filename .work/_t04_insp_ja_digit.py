#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — thử nghiệm: QC chấp nhận số tiếng Nhật thế nào?"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(__file__).resolve().parent
sent = json.loads((W / "_t04_sentences.json").read_text(encoding="utf-8"))
ja = sent["ja"]


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return " ".join(s.split())


def contains(frag, ctx):
    f, c = norm(frag), norm(ctx)
    if not f:
        return True
    fw, cw = f.split(), c.split()
    for i in range(len(cw) - len(fw) + 1):
        if cw[i:i + len(fw)] == fw:
            return True
    return False


ctx103 = " ".join(s["text"] for s in ja["1.03"][0:3])
print("ctx 1.03#1-#3 tokens:", norm(ctx103).split())
print()
for frag in ["2003年秋", "2003", "43歳のその男", "歳", "アメリカ合衆国ニュージャージー州サマービルのサマセット医療センター",
             "サマセット医療センター", "（Somerset Medical Center）", "Somerset", "Somerset Medical Center"]:
    print(f"  contains({frag!r}) = {contains(frag, ctx103)}")

print()
ctx14 = " ".join(s["text"] for s in ja["1.14"][2:5])
print("ctx 1.14#3-#5 tokens:", norm(ctx14).split())
for frag in ["16年間にわたり", "16", "9つの病院と1つの養護施設", "9", "ニュージャージー州とペンシルベニア州"]:
    print(f"  contains({frag!r}) = {contains(frag, ctx14)}")

print()
print("--- câu JA có số đứng riêng? ---")
for eid, ss in ja.items():
    for s in ss:
        toks = norm(s["text"]).split()
        for t in toks:
            if re.fullmatch(r"\d+", t):
                print("  ", s["id"], repr(t))
print("(hết)")
