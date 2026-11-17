#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VÒNG 4 — 1 nền Tập 11: `control_room_dark_monitors` còn nameplate 4 khối chữ giả
trên viền màn hình (40×8 px gốc) ⇒ yêu cầu viền màn hình TRƠN hoàn toàn.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
JOBS = ROOT / ".work" / "bg_jobs_tap11.json"
OUT = ROOT / ".work" / "bg_jobs_tap11_detext1_r4.json"

PROMPT = (
    "A dim broadcast control room with a wall of switched-off blank dark monitors whose "
    "bezels are completely plain smooth metal with no nameplate, no logo, no badge and no "
    "label of any kind, one small console indicator light, the console buttons are plain "
    "blank unlabeled squares, cold grey light, heavy shadow, no people, "
    "completely blank and unmarked with no writing at all."
)

def main():
    jobs = {j["name"]: j for j in json.loads(JOBS.read_text(encoding="utf-8"))}
    old = jobs["t11_control_room_dark_monitors"]
    out = [{
        "name": "t11_control_room_dark_monitors",
        "act": old.get("act", 1), "sentences": old.get("sentences", ""),
        "desc": old.get("desc", ""), "prompt": PROMPT, "seed": 61001,
        "why": "vong 4: bo nameplate tren vien man hinh (4 khoi chu gia 40x8px)",
    }]
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"ghi {OUT.relative_to(ROOT)} · 1 job vong 4 (seed 61001)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
