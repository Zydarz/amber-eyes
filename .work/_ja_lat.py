#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo độ trễ 1 lệnh gọi LLM (để ước lượng throughput của gateway)."""
import sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ja_llm

t0 = time.time()
txt = ja_llm.call("「ok」だけ返してください。", system="日本語で答えてください。",
                  model="MiniMax-M3.1-Flash", max_tokens=200, temperature=0.1, timeout=180)
print(f"latency = {time.time() - t0:.1f}s · resp = {txt[:80]!r}")
