#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tao thu muc push cho kernel FIX 4.08#6 (EN Tap 02)."""
import json
import pathlib

d = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\kaggle_higgs\_push_fix4086")
d.mkdir(parents=True, exist_ok=True)

readme = """# Amber Eyes - Higgs v3, FIX 1 cau 4.08#6 (EN Tap 02)

Sinh lai rieng cau 4.08#6 (vai D) voi chu kich ban:
`the snow boot impression` (thay `the snowshoe footprint`).

Cung clip tham chieu D_EN.wav, cung emotion (neutral) / speed (0.99),
cung seed scheme sha256(id|role|ref|temp|vN) -> so sanh 1:1 voi ban cu.
3 ban (variant 0/1/2).
"""

meta = {
    "id": "chiduong2026/amber-eyes-higgs-fix-4086-en-t02-kaggle-gpu",
    "title": "Amber Eyes Higgs fix 4.08#6 EN T02 Kaggle GPU",
    "code_file": "higgs_fix4086_kaggle.ipynb",
    "language": "python",
    "kernel_type": "notebook",
    "is_private": True,
    "enable_gpu": True,
    "enable_tpu": False,
    "enable_internet": True,
    "keywords": ["tts", "higgs-audio-v3", "english", "fix"],
    "dataset_sources": ["chiduong2026/amber-eyes-voice-ref-voxcpm2-en"],
    "competition_sources": [],
    "model_sources": [],
}

(d / "README.md").write_text(readme, encoding="utf-8")
(d / "kernel-metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

print("OK ->", d)
for f in sorted(d.iterdir()):
    print("   %-38s %8d" % (f.name, f.stat().st_size))
