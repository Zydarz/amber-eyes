#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — ảnh nào ĐỔI byte so với bản trước, và ảnh nào GIỮ NGUYÊN."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BK = WORK / "_cu" / "t03_20261105_1800"

before = json.loads((BK / "stills_manifest_before.json").read_text(encoding="utf-8"))
after = json.loads((BK / "stills_manifest_afterB.json").read_text(encoding="utf-8"))

SHOTS = {"vi": "shots_t03.json", "en": "shots_EN_t03.json", "ja": "shots_JA_t03.json"}

for lang, sn in SHOTS.items():
    shots = json.loads((WORK / sn).read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in shots["shots"]}
    same, diff = [], []
    for n, v in before[lang].items():
        (same if after[lang].get(n, {}).get("sha256") == v["sha256"] else diff).append(n)
    print("=" * 78)
    print(f"[{lang}]  GIỮ NGUYÊN {len(same)} · ĐỔI {len(diff)}")
    # phân tích: shot giữ nguyên có role/avatar không?
    for n in same:
        sid = n.replace("shot_", "").replace(".png", "")
        s = by_id.get(sid, {})
        print(f"   giữ: {sid:6} role={s.get('role')!r:8} template={s.get('template')!r:6} "
              f"segments={len(s.get('segments') or [])}")
    # nhóm: shot có role (avatar bán thân) vs không
    with_role = [n for n in diff if by_id.get(n.replace('shot_','').replace('.png',''), {}).get("role")]
    no_role = [n for n in diff if not by_id.get(n.replace('shot_','').replace('.png',''), {}).get("role")]
    print(f"   ĐỔI có role={len(with_role)} · không role={len(no_role)}")
    print(f"   ĐỔI không role: {sorted(n for n in no_role)[:14]}")
