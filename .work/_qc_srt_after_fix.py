#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra SRT JA Tap02 sau khi sua text: cau truc + khop voi loi noi that."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
n = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t or "")

SRT = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt"
txt = SRT.read_bytes().decode("utf-8-sig").replace("\r\n", "\n")
blocks = [b for b in txt.strip().split("\n\n") if b.strip()]


def sec(ts):
    h, m, s = ts.split(":")
    s, ms = s.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


bad = [i for i, b in enumerate(blocks, 1) if len(b.splitlines()) < 3 or " --> " not in b.splitlines()[1]]
blank = [i for i, b in enumerate(blocks, 1) if any(x.strip() == "" for x in b.splitlines()[2:])]
cues = []
for b in blocks:
    ls = b.splitlines()
    a, z = ls[1].split(" --> ")
    cues.append((sec(a), sec(z), " ".join(ls[2:])))
print(f"cue={len(cues)} · khoi lo={len(bad)} · dong trong={len(blank)}")
print(f"het = {cues[-1][1]:.2f}s")

# khop voi loi noi that
pay = json.loads((W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json").read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in pay["items"] if r.get("id")}
tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it["text"] for it in tl["items"]}
blob = " ".join(sent.values())
hit = sum(1 for _, _, t in cues if n(re.sub(r"^\[[^\]]+\]\s*", "", t)) and n(re.sub(r"^\[[^\]]+\]\s*", "", t)) in n(blob))
print(f"cue co text khop cau noi that: {hit}/{len(cues)}")

# mau 6 cue rai
print("\n--- 6 cue rai ---")
for a, z, t in cues[::max(1, len(cues) // 6)][:6]:
    print(f"  {a:7.2f}->{z:7.2f}  {t[:100]}")
