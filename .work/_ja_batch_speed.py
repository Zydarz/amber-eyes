#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo thời gian thật của 1 lô thoại (payload giống hệt pipeline)."""
import sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M

ep = sys.argv[1] if len(sys.argv) > 1 else "02"
size = int(sys.argv[2]) if len(sys.argv) > 2 else 8
N = int(sys.argv[3]) if len(sys.argv) > 3 else 6

units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
dia = [u for u in units if u["id"] in in_turn and u["kind"] == "TEXT"][:size * N]
batches = [dia[i * size:(i + 1) * size] for i in range(N)]
ep_tokens = M.vn_tokens_of(M.canonical_vn(ep).read_text(encoding="utf-8"))

t0 = time.time()
with ThreadPoolExecutor(max_workers=N) as ex:
    res = list(ex.map(lambda b: M.call_batch(b, "dialogue", 1, ep_tokens), batches))
dt = time.time() - t0
ok = sum(len(r) for r in res)
print(f"size={size} N={N} · {dt:.1f}s · đạt {ok}/{size * N} · "
      f"{ok / dt * 60:.1f} mục/phút")
