#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Khôi phục file mp3 TTS từ node_id đã lưu trong .work/tts_s_EN_t02/res_*.json.

Dùng khi gói TTS hết số dư (402) nhưng file đã sinh trước đó vẫn còn trên drive:
node_id -> get_asset_url -> tải lại mp3.
python .work/_restore_from_nodes.py <sid> [<sid> ...]
"""
import json
import sys
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"D:\TEST\Gax\Audi\.work")
import tts_sentences as TS  # noqa: E402

W = Path(r"D:\TEST\Gax\Audi\.work")
TTS = W / "tts_s_EN_t02"
OUT = W / "audio_s_EN_t02"

want = sys.argv[1:]
nodes = {}
for f in sorted(TTS.glob("res_*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    if d.get("code") not in (0, None):
        continue
    for x in d.get("success_items") or []:
        stem = x.get("file_name", "").rsplit(".", 1)[0]
        p = stem.lstrip("s").split("_")
        if len(p) != 3:
            continue
        sid = f"{p[0]}.{p[1]}#{int(p[2])}"
        nodes.setdefault(sid, []).append((f.name, x.get("node_id")))

for sid in want:
    if sid not in nodes:
        print(f"!! {sid}: không có node_id")
        continue
    src, node = nodes[sid][-1]
    url = TS.mcode(["get_asset_url", node], 120)["download_url"]
    ma, num = sid.split("#")
    p = OUT / f"s{ma.replace('.', '_')}_{int(num):02d}.mp3"
    urllib.request.urlretrieve(url, p)
    print(f"{sid:>9}  <- {src} node={node}  -> {p.name} ({p.stat().st_size} byte)")
