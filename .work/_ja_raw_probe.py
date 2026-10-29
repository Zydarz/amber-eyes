#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chẩn đoán: gọi thử đúng 1 lô của Tap28 và in RAW phản hồi gateway."""
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import httpx  # noqa: E402
import ja_llm  # noqa: E402
import make_ja_scripts as M  # noqa: E402

ep = sys.argv[1] if len(sys.argv) > 1 else "28"
src = M.canonical_vn(ep)
units = M.assign_turn_counts(M.parse_units(src))
in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
ep_tokens = M.vn_tokens_of(src.read_text(encoding="utf-8"))

jobs = []
for u in units:
    if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
        parts = M.splittable(u)
        if parts:
            for k, p in enumerate(parts):
                jobs.append({"id": f"{u['id']}#{k}", "vi": p, "ctx": u["vi"], "kind": "dialogue"})
            continue
        jobs.append({"id": f"{u['id']}#L", "vi": u["vi"], "ctx": u["vi"], "kind": "line",
                     "n": u.get("n", 0)})
    elif u["kind"] != "RAW":
        jobs.append({"id": u["id"], "vi": u["vi"], "kind": "meta"})

cache = {}
cp = HERE / "ja_cache" / f"tap{ep}.json"
if cp.exists():
    cache = json.loads(cp.read_text(encoding="utf-8"))
todo = [j for j in jobs if j["id"] not in cache]
print(f"tap{ep}: {len(todo)} mục chưa dịch")
batch = todo[:6]
prompt, sys_p = M.build_prompt(batch, "dialogue")
print(f"prompt {len(prompt)} ký tự · system {len(sys_p)} ký tự")

body = {"model": "MiniMax-M3.1-Flash", "max_tokens": 16000, "temperature": 0.2,
        "messages": [{"role": "user", "content": prompt}], "system": sys_p}
h = {"Content-Type": "application/json",
     "Authorization": f"Bearer {ja_llm._token()}"}
t0 = time.time()
with httpx.Client(timeout=420) as c:
    r = c.post(ja_llm.BASE, headers=h, json=body)
dt = time.time() - t0
print(f"HTTP {r.status_code} sau {dt:.1f}s · {len(r.content)} bytes")
if r.status_code == 200:
    data = r.json()
    print("keys:", list(data.keys()))
    print("stop_reason:", data.get("stop_reason"), "usage:", data.get("usage"))
    for b in data.get("content", []):
        print(f"  block type={b.get('type')} len={len(b.get('text','') or b.get('thinking','') or '')}")
        if b.get("type") == "text":
            print("   TEXT:", b["text"][:300])
        else:
            print("   ", str(b)[:200])
else:
    print(r.text[:400])
