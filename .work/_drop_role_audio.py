#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xoá file mp3 của một vai trong .work/audio_s_<suf>/ (để đọc lại bằng giọng khác).

python .work/_drop_role_audio.py D
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
role = sys.argv[1]
man = json.loads((W / "tts_manifest_EN_t02.json").read_text(encoding="utf-8"))
out = W / "audio_s_EN_t02"
n = 0
for m in man:
    if m["role"] == role:
        p = out / m["file"]
        if p.exists():
            p.unlink()
            n += 1
print(f"đã xoá {n} file của vai {role} trong {out.name}")
