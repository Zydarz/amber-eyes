#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mo phong 495-560s cua timeline moi T2 EN + dong bo voi ke hoach."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
PLAN = ROOT / "02_SAN_XUAT" / "Tap02_EN" / "KeHoach_Video_Tap02_EN.md"
TL = json.loads((W / "timeline_s_EN_t02.json").read_text(encoding="utf-8-sig"))

print("=== TIMELINE items 490-560s ===")
for it in TL["items"]:
    if 485 <= it["start"] <= 560:
        d = it["end"] - it["start"]
        print(f"  {it['id']:<10} {it['start']:8.2f} -> {it['end']:8.2f}  ({d:5.2f}s) "
              f"[{it['role']}] act{it['act']}  {it['text'][:58]}")

print()
print("=== MARKERS 485-570s ===")
for m in TL["markers"]:
    s = m.get("start", m.get("at", -1))
    if 485 <= s <= 570:
        print(f"  {m.get('type'):<6} {m.get('id') or m.get('act')!s:<8} "
              f"{m.get('start','-')}/{m.get('end','-')}/{m.get('at','-')} {m.get('desc','')[:40]}")

print()
print("=== KE HOACH: dong shot 3-01 .. 3-05 ===")
text = PLAN.read_text(encoding="utf-8-sig")
for line in text.splitlines():
    if re.match(r"\|\s*3-0[1-5]\s*\|", line):
        print("  " + line[:250])

print()
print("=== SCRIPT: element 3.02 / 3.03 ===")
sc = json.loads((W / "script_tap02_EN.json").read_text(encoding="utf-8-sig"))
for e in sc:
    if e["id"] in ("3.02", "3.03", "3.04"):
        print(f"  id={e['id']} kind={e['kind']} act={e['act']} sec={e.get('sec')}")
        print(f"     sentences={[s['id'] for s in e.get('sentences',[])]}")
        print(f"     text={e.get('text','')[:150]}")

print()
print("=== ACTING: _pause_after cho 3.02/3.03 ===")
ac = json.loads((W / "acting_tap02_EN.json").read_text(encoding="utf-8-sig"))
pa = ac.get("_pause_after", {})
for k, v in pa.items():
    if k.startswith("3.02") or k.startswith("3.03") or k.startswith("3.01"):
        print(f"  {k}: {v}")

print()
print("=== TTS MANIFEST: file cho 3.02#1 va cac cau gan ===")
man = {m["id"]: m for m in json.loads((W / "tts_manifest_EN_t02.json").read_text(encoding="utf-8-sig"))}
for k in sorted(man):
    if k.startswith("3.01") or k.startswith("3.02") or k.startswith("3.03"):
        print(f"  {k}: file={man[k].get('file')} role={man[k].get('role')} "
              f"emotion={man[k].get('emotion')} speed={man[k].get('speed')}")
