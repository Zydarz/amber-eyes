#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thử N lệnh gọi LLM song song -> đo throughput thực của gateway."""
import sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ja_llm

N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
payload = (" 다음 문장을 일본어로 번역하세요. " * 120)


def one(i):
    t0 = time.time()
    try:
        ja_llm.call(f"文書{i}: {payload}", system="日本語に翻訳してください。",
                     model="MiniMax-M3.1-Flash", max_tokens=4000, temperature=0.2, timeout=300)
        return time.time() - t0, "ok"
    except Exception as e:
        return time.time() - t0, str(e)[:60]


t0 = time.time()
with ThreadPoolExecutor(max_workers=N) as ex:
    res = list(ex.map(one, range(N)))
dt = time.time() - t0
lat = [r[0] for r in res]
err = [r[1] for r in res if r[1] != "ok"]
print(f"N={N} · tổng {dt:.1f}s · latency min/med/max = "
      f"{min(lat):.1f}/{sorted(lat)[len(lat)//2]:.1f}/{max(lat):.1f}s · lỗi={len(err)}")
for e in err[:3]:
    print("   ", e)
