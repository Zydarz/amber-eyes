#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cau 3.08#10: text o dau? script JSON vs timeline vs tts_manifest vs acting."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def find(obj, target, path=""):
    hits = []
    if isinstance(obj, dict):
        if obj.get("id") == target:
            hits.append((path, obj))
        for k, v in obj.items():
            hits += find(v, target, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += find(v, target, f"{path}[{i}]")
    return hits


for tag, file in [("script_tap02_JA.json", W / "script_tap02_JA.json"),
                  ("tts_manifest_JA_t02.json", W / "tts_manifest_JA_t02.json"),
                  ("acting_tap02_JA.json", W / "acting_tap02_JA.json"),
                  ("timeline_s_JA_t02.json", W / "timeline_s_JA_t02.json")]:
    if not file.exists():
        print(f"{tag}: KHONG CO")
        continue
    d = json.loads(file.read_text(encoding="utf-8-sig"))
    hits = find(d, "3.08#10")
    print("=" * 70)
    print(f"{tag}  ({len(hits)} noi co id 3.08#10)")
    for path, h in hits[:3]:
        keep = {k: v for k, v in h.items() if k in ("id", "text", "read", "loi_doc", "reading",
                                                    "spoken", "content", "voice", "speed")}
        print(f"  {path}: {json.dumps(keep, ensure_ascii=False)[:300]}")
