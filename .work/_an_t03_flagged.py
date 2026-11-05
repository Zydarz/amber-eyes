#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A4 — soi từng shot bị QC báo lỗi: chữ trên hình vs câu đang đọc."""
import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path("D:/TEST/Gax/amber-eyes")
os.environ.setdefault("AE_EP", "03")
sys.path.insert(0, str(ROOT / ".work"))
import edition as ED  # noqa: E402

TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))
SENT = {it["id"]: it for it in TL["items"]}
SHOTS = {s["id"]: s for s in SH["shots"]}

TARGET = ["3-12", "4-11", "5-04", "1-05", "1-06", "2-10", "3-13", "3-18"]
for sid in TARGET:
    s = SHOTS[sid]
    print("=" * 78)
    print(f"SHOT {sid} · vai={s['role']} · mẫu={s['template']}/{s.get('variant')} · nền={s['bg']} · "
          f"{round(s['end']-s['start'],1)}s")
    print(f"  câu: {s['sentences']}")
    for x in s["sentences"]:
        print(f"    {x} :: {SENT[x]['text']}")
    for seg in s["segments"]:
        at = seg["at_sentence"]
        print(f"  SEG at={at}:")
        for kind, t in seg["elems"]:
            print(f"     [{kind}] {t!r}")
    print(f"  beat_text: {s.get('beat_text')!r}")
    print(f"  flags: {s['flags']}")
