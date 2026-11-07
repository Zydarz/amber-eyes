#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh .work/acting_tap09_JA.json cho bản tiếng Nhật Tập 09 (Charles Manson).
Kế thừa cảm xúc, tốc độ và khoảng lặng _pause_after từ acting_tap09.json chuẩn; pitch luôn = 0 (G5).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

vn_acting = json.loads((WORK / "acting_tap09.json").read_text(encoding="utf-8"))
ja_script = json.loads((WORK / "script_tap09_JA.json").read_text(encoding="utf-8"))

ja_acting = {
    "_doc": "Diễn xuất từng câu cho bản tiếng Nhật (Tap09_JA). Kế thừa cảm xúc từ bản chuẩn Tap 09; pitch = 0 (G5); speed clamp G4.",
    "_pause_after": vn_acting.get("_pause_after", {})
}

sent_count = 0
for e in ja_script:
    if e.get("kind") == "LOI":
        for s in e.get("sentences", []):
            sid = s["id"]
            sent_count += 1
            if sid in vn_acting:
                emo, sp, pitch, aside = vn_acting[sid]
                ja_acting[sid] = [emo, sp, 0, None]
            else:
                ja_acting[sid] = ["neutral", 0.0, 0, None]

if sent_count != 199:
    print(f"CẢNH BÁO: Số câu tiếng Nhật ({sent_count}) != 199", file=sys.stderr)
    sys.exit(1)

out_p = WORK / "acting_tap09_JA.json"
out_p.write_text(json.dumps(ja_acting, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Created {out_p.name} with {sent_count} sentences and {len(ja_acting.get('_pause_after', {}))} pauses.")
