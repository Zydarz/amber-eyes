#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Subagent Batch Prompt Generator for Episode 07.
Formats the exact prompts and target paths for the Antigravity image-generator subagent
once Google Gemini image quota resets (~19:37:12 UTC+7).
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
BG_DIR = ROOT / "assets" / "bg"

STYLE_PREFIX = (
    "Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink linework, "
    "deep chiaroscuro lighting, subtle mist and film grain, desaturated muted palette, ominous quiet tension, highly detailed. "
)
STYLE_SUFFIX = (
    " Strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, "
    "no watermark, no frame, no letterbox bars, full-bleed image."
)

jobs = json.loads((WORK / "bg_jobs_tap07.json").read_text(encoding="utf-8"))

batch_prompts = []
for j in jobs:
    name = j["name"]
    full_prompt = f"{STYLE_PREFIX}{j['prompt']}{STYLE_SUFFIX}"
    batch_prompts.append({
        "name": name,
        "target_file": f"assets/bg/{name}.png",
        "aspect_ratio": "16:9",
        "prompt": full_prompt
    })

out_json = WORK / "gemini_image_prompts_tap07.json"
out_json.write_text(json.dumps(batch_prompts, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Đã xuất {len(batch_prompts)} prompt hoàn chỉnh sang {out_json}")
