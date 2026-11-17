#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VÒNG 3 — 1 nền Tập 11: gỡ triệt để huy hiệu khỏi prompt.

Sau vòng 2, `haunted_new_identity_shadow` ĐÃ bỏ được trang định danh nhưng AI lại
điền chữ vô nghĩa vào BÊ TRONG huy hiệu — vì từ "crest / emblem" trong prompt gợi
mở "huy hiệu gia đình có khẩu hiệu". ⇒ BỎ HẲN emblem, để bìa sau trơn hoàn toàn.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
JOBS = ROOT / ".work" / "bg_jobs_tap11.json"
OUT = ROOT / ".work" / "bg_jobs_tap11_detext1_r3.json"

PROMPT = (
    "Still life of a plain closed passport booklet lying face-down on wet winter pavement, "
    "the back cover is a completely smooth blank surface with no emblem, no crest, no shield, "
    "no symbol, no badge and no mark of any kind, permanent looming shadows of past crimes "
    "falling across it, eternal moral exile and social ostracism, "
    "completely blank and unmarked with no writing at all."
)

def main():
    jobs = {j["name"]: j for j in json.loads(JOBS.read_text(encoding="utf-8"))}
    old = jobs["t11_haunted_new_identity_shadow"]
    out = [{
        "name": "t11_haunted_new_identity_shadow",
        "act": old.get("act", 1), "sentences": old.get("sentences", ""),
        "desc": old.get("desc", ""), "prompt": PROMPT, "seed": 51001,
        "why": "vong 3: bo han emblem (AI dien chu vao huyen hiệu)",
    }]
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"ghi {OUT.relative_to(ROOT)} · 1 job vong 3 (seed 51001)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
