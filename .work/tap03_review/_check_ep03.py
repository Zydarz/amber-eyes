#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra EPISODES['03'] vừa thêm: giá trị dẫn xuất đúng, không hỏng tập khác."""
import importlib
import json
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
sys.path.insert(0, str(ROOT / ".work"))
os.environ["AE_EP"] = "03"

import edition as ED  # noqa: E402

err = []
ep = ED.EP
print("=== EPISODES['03'] ===")
for k in ("script", "dir", "plan", "master", "srt", "acting", "sfx_sheet"):
    print(f"  {k:<12} {ep[k]}")
print(f"  n_element    {ep['n_element']}")
print(f"  act1_cue     {ep['act1_cue']}   silence_cue {ep['silence_cue']}   click_cues {ep['click_cues']}")
print(f"  n1           {ep['n1']}")
print(f"  n2           {ep['n2']}")
print(f"  thumb        {ep['thumb']}   thumb_bg {ep['thumb_bg']}")
print(f"  need         {len(ep['need'])} mau cau")
print(f"  bed          {ep['bed']}")

print("\n=== file tai duoc phai ton tai ===")
for k in ("script", "acting", "sfx_sheet"):
    p = ep[k]
    print(f"  {'OK ' if p.exists() else 'THIEU'} {p}")
    if not p.exists() and k != "acting":
        err.append(f"{k} khong ton tai: {p}")
if not (ROOT / "assets" / "bg" / f"{ep['thumb_bg']}.png").exists():
    err.append(f"thumb_bg khong ton tai: {ep['thumb_bg']}")

print("\n=== file BGM ===")
for act, b in ep["bed"].items():
    fs = b if isinstance(b, tuple) else (b,)
    for f in fs:
        p = ROOT / "assets" / "bgm" / f
        ok = p.exists()
        print(f"  {'OK ' if ok else 'THIEU'} act{act} {f}")
        if not ok:
            err.append(f"BGM thieu: {f}")

print("\n=== ma cau trong script Tap03 ===")
els = json.loads(Path(ep["script"]).read_text(encoding="utf-8"))
sent, mark = {}, {}
for e in els:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sent[s["id"]] = s
    else:
        mark[e["id"]] = e

for i in ep["need"] + list(ep["summary"]):
    if i not in sent:
        err.append(f"ma cau khong ton tai: {i}")
print(f"  need+summary: {len(ep['need'] + list(ep['summary']))} mau, thieu: "
      f"{[i for i in ep['need'] + list(ep['summary']) if i not in sent]}")

print("\n=== kieu cua 3 moc ===")
for key in ("act1_cue", "silence_cue"):
    e = mark.get(ep[key])
    kind = e["kind"] if e else "KHONG CO"
    print(f"  {key:<12} {ep[key]:<6} -> {kind}")
    if kind == "KHONG CO":
        err.append(f"{key} khong phai marker")
for c in ep["click_cues"]:
    e = mark.get(c)
    kind = e["kind"] if e else "KHONG CO"
    print(f"  click_cue    {c:<6} -> {kind}")
    if kind == "KHONG CO":
        err.append(f"click_cue khong phai marker: {c}")

print("\n=== n_element co khop vai trong script khong ===")
for eid, role in ep["n_element"].items():
    e = els[[x["id"] for x in els].index(eid)] if eid in mark else None
    e = next((x for x in els if x["id"] == eid), None)
    print(f"  {eid} -> {role}  (kind={e['kind'] if e else '?'}, vai={e.get('role','?')})")

print("\n=== KHONG HONG TAP KHAC ===")
for other in ("01", "02", "04", "05"):
    if other not in ED.EPISODES:
        continue
    o = ED.EPISODES[other]
    ok = o["script"].exists() and (ROOT / "assets" / "bgm" / (o["bed"][1] if isinstance(o["bed"][1], tuple) else o["bed"][1])).exists()
    print(f"  Tap{other}: script={'OK' if o['script'].exists() else 'THIEU'}  n_element={o['n_element']}")
    if not o["script"].exists():
        err.append(f"Tap{other} script khong ton tai")

print("\nKET QUA:", "SACH" if not err else f"{len(err)} LOI")
for e in err:
    print("  !!", e)
sys.exit(0 if not err else 1)
