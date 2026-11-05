#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — công cụ xem cấu trúc dữ liệu đầu vào (chỉ đọc)."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(__file__).resolve().parent

sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
rows = sk["rows"]
shots = [r for r in rows if r["kind"] == "shot"]
meta = [r for r in rows if r["kind"] != "shot"]
print("skeleton: rows=%d shots=%d meta=%d" % (len(rows), len(shots), len(meta)))
print("idmap sample:", list(sk["idmap"].items())[:6])
print()
print("=== first 2 shot rows ===")
for r in shots[:2]:
    print(json.dumps(r, ensure_ascii=False, indent=1))
print("=== meta rows ===")
for r in meta:
    print(r["sid"], r["kind"], r["cells"])

sent = json.loads((W / "_t04_sentences.json").read_text(encoding="utf-8"))
print()
print("sentences langs:", list(sent.keys()))
ja = sent["ja"]
print("ja elements:", len(ja))
k = list(ja.keys())[:3]
for kk in k:
    print(kk, json.dumps(ja[kk], ensure_ascii=False)[:500])

chu = json.loads((W / "_t04_chu_vn.json").read_text(encoding="utf-8"))
print()
print("chu_vn entries:", len(chu))
for kk in list(chu)[:6]:
    print(repr(kk), "=>", repr(chu[kk]))

bv = json.loads((W / "_t04_beat_vi.json").read_text(encoding="utf-8"))
print()
print("beat_vi entries:", len(bv))
for kk in list(bv)[:8]:
    print(repr(kk), "=>", repr(bv[kk]))
