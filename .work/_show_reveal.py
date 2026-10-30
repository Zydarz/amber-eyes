#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In lich su hien thi cua tung shot: moi doan chu xuat hien luc nao."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).resolve().parents[1] / ".work"
sh = json.loads((W / "shots_t02.json").read_text(encoding="utf-8"))
tl = json.loads((W / "timeline_s_t02.json").read_text(encoding="utf-8"))
SENT = {it["id"]: it for it in tl["items"]}
shots = sh["shots"]


def moments(s):
    sents, segs = s["sentences"], s["segments"]
    starts = [SENT[x]["start"] for x in sents]
    phr = list(s["beats"])
    out = []
    for i, sg in enumerate(segs):
        if i == 0:
            out.append(("bat dau shot", sg))
            continue
        if sg["at_sentence"]:
            tgt = [x for x in sents if x.endswith(f"#{sg['at_sentence']}")]
            out.append((f"cau #{sg['at_sentence']}", sg))
        elif phr:
            out.append((f"cum tu '{phr.pop(0)}'", sg))
        elif i < len(starts):
            out.append((f"cau {sents[i]}", sg))
        else:
            out.append(("giua cau cuoi", sg))
    return out


TARGET = ["1-11", "1-15", "1-18", "1-25", "1-31", "2-05", "5-03", "5-07", "2-14", "2-22", "3-25"]
for s in shots:
    if s["id"] not in TARGET:
        continue
    dur = s["end"] - s["start"]
    print(f"--- {s['id']}  {s['template']}  {dur:.1f}s  ({s['start']:.1f} -> {s['end']:.1f})")
    print(f"    beat: {s['beats'] or '(khong)'}")
    for label, sg in moments(s):
        txt = " | ".join(t for _k, t in sg["elems"])
        print(f"    - [{label}] {txt[:110]}")
