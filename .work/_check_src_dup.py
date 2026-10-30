#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rà 2 mã SFX khác nhau nhưng dùng CHUNG 1 track nguồn YouTube (2 file sẽ
trùng tiếng trong bản trộn)."""
import io
import sys
from collections import defaultdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / ".work" / "yt_map.tsv"
TICK = chr(96)

ACCEPT = {frozenset(["fx_lav_mic_breathing", "fx_breathing_tense_close"])}

man = {}
for raw in io.open(MAP, encoding="utf-8-sig").read().splitlines():
    p = raw.split("\t")
    if len(p) >= 2 and p[1].strip():
        man[p[1].strip()] = p[0].strip()

by_track = defaultdict(list)
for ma, track in man.items():
    by_track[track].append(ma)

dups = {t: sorted(ms) for t, ms in by_track.items() if len(ms) > 1}
print("ma trong manifest:", len(man), "| track dung chung:", len(dups))
for t, ms in sorted(dups.items(), key=lambda kv: kv[1][0]):
    tag = "ACCEPT" if any(frozenset(x) == frozenset(ms) for x in ACCEPT) else "!! CANH BAO"
    print("  %-10s %-46s %s" % (tag, t, ", ".join(ms)))
