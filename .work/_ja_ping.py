#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thử gọi gateway 1 lần xem có phản hồi không (đo độ trễ)."""
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import ja_llm  # noqa: E402

t0 = time.time()
try:
    txt = ja_llm.call("「こんにちは」とだけ返してください。JSON配列は不要です。",
                      "あなたは日本語訳者です。", model="MiniMax-M3.1-Flash",
                      max_tokens=200, temperature=0.1, timeout=120)
    print(f"OK {time.time()-t0:.1f}s -> {txt[:120]!r}")
except Exception as e:
    print(f"LỖI sau {time.time()-t0:.1f}s: {str(e)[:300]}")
