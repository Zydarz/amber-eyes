# -*- coding: utf-8 -*-
"""Kiem tra provenance (T9) cua cac file BGM trong assets/bgm/ + do dai/dinh dang."""
import json
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8-sig"))
items = data if isinstance(data, list) else data.get("items", [])

bgms = sorted((ROOT / "assets" / "bgm").glob("*.mp3"))
print("=== provenance tung file BGM tren dia ===")
for b in bgms:
    hits = [it for it in items if b.name in str(it.get("file", "")) or b.name in str(it.get("ghi_chu", ""))]
    print(f"\n{b.name}")
    if not hits:
        print("   KHONG co dong provenance nao chua")
    for h in hits[:3]:
        print("   file:", h.get("file"))
        print("   loai:", h.get("loai"))
        print("   nguon:", h.get("nguon_anh_tham_chieu"), "| seed:", h.get("seed"))
        print("   dieu_khoan:", str(h.get("dieu_khoan"))[:300])
        print("   thuong_mai:", str(h.get("kiem_tra_thuong_mai"))[:300])
