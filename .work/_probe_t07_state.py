#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do trang thai du lieu Tap07: script moi (147 cau) vs bang shot cu (164 cau)."""
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

W = Path(r"D:/TEST/Gax/amber-eyes/.work")


def load(name):
    p = W / name
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8-sig"))


script = load("script_tap07.json")
acting = load("acting_tap07.json")
shots = load("shots_t07.json")
timeline = load("timeline_s_t07.json")
sfx = load("sfx_tap07.json")
manifest = load("tts_manifest_t07.json")

print("=" * 70)
print("SCRIPT_TAP07.JSON")
print("=" * 70)
print("type:", type(script).__name__)
if isinstance(script, dict):
    print("keys:", list(script.keys())[:20])
    for k, v in script.items():
        if isinstance(v, list):
            print(f"  {k}: list len={len(v)}")
            if v and isinstance(v[0], dict):
                print("    item0 keys:", list(v[0].keys()))
                print("    item0:", json.dumps(v[0], ensure_ascii=False)[:600])
        elif isinstance(v, dict):
            print(f"  {k}: dict len={len(v)} keys={list(v.keys())[:8]}")
        else:
            print(f"  {k}: {repr(v)[:200]}")
elif isinstance(script, list):
    print("len:", len(script))
    print("item0 keys:", list(script[0].keys()))
    print("item0:", json.dumps(script[0], ensure_ascii=False)[:600])

print()
print("=" * 70)
print("ACTING_TAP07.JSON")
print("=" * 70)
if isinstance(acting, dict):
    print("keys:", list(acting.keys())[:20])
    for k, v in acting.items():
        if isinstance(v, list):
            print(f"  {k}: list len={len(v)}")
            if v and isinstance(v[0], dict):
                print("    item0:", json.dumps(v[0], ensure_ascii=False)[:500])
        elif isinstance(v, dict):
            print(f"  {k}: dict len={len(v)} keys={list(v.keys())[:6]}")

print()
print("=" * 70)
print("SHOTS_TAP07.JSON (cu)")
print("=" * 70)
if isinstance(shots, dict):
    print("keys:", list(shots.keys())[:20])
    for k, v in shots.items():
        if isinstance(v, list):
            print(f"  {k}: list len={len(v)}")
            if v and isinstance(v[0], dict):
                print("    item0:", json.dumps(v[0], ensure_ascii=False)[:700])
        elif isinstance(v, dict):
            print(f"  {k}: dict len={len(v)} keys={list(v.keys())[:6]}")
        else:
            print(f"  {k}: {repr(v)[:200]}")
elif isinstance(shots, list):
    print("len:", len(shots))
    print("item0:", json.dumps(shots[0], ensure_ascii=False)[:700])

print()
print("=" * 70)
print("TIMELINE_S_TAP07.JSON")
print("=" * 70)
if isinstance(timeline, dict):
    print("keys:", list(timeline.keys()))
    for k, v in timeline.items():
        if isinstance(v, list):
            print(f"  {k}: list len={len(v)}")
            if v and isinstance(v[0], dict):
                print("    item0:", json.dumps(v[0], ensure_ascii=False)[:500])
        elif isinstance(v, dict):
            print(f"  {k}: dict len={len(v)} keys={list(v.keys())[:6]}")
        else:
            print(f"  {k}: {repr(v)[:200]}")

print()
print("=" * 70)
print("SFX_TAP07.JSON / MANIFEST")
print("=" * 70)
if isinstance(sfx, dict):
    print("sfx keys:", list(sfx.keys()))
    for k, v in sfx.items():
        if isinstance(v, list):
            print(f"  sfx.{k}: list len={len(v)}")
            if v and isinstance(v[0], dict):
                print("    item0:", json.dumps(v[0], ensure_ascii=False)[:400])
        elif isinstance(v, dict):
            print(f"  sfx.{k}: dict len={len(v)} keys={list(v.keys())[:6]}")
if isinstance(manifest, dict):
    print("manifest keys:", list(manifest.keys())[:20])
    for k, v in manifest.items():
        if isinstance(v, list):
            print(f"  mf.{k}: list len={len(v)}")
        elif isinstance(v, dict):
            print(f"  mf.{k}: dict len={len(v)} keys={list(v.keys())[:6]}")
