#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit: (a) tiêu đề hồi có ngoặc không phải mốc thời gian, (b) mục cache nào
không còn đạt kiểm tra (sẽ bị bỏ nếu bật tự kiểm lại cache).

    py -3 .work/_ja_cache_audit.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

CACHE = HERE / "ja_cache"
TIME_RE = re.compile(r"\d{1,2}\s*[:：]\s*\d{2}")

n_bad_act = 0
n_stale = 0
per_ep = []

for i in range(1, 30):
    ep = f"{i:02d}"
    src = M.canonical_vn(ep)
    units = M.assign_turn_counts(M.parse_units(src))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    ep_tokens = M.vn_tokens_of(src.read_text(encoding="utf-8"))

    # (a) tiêu đề hồi: ngoặc cuối không phải mốc thời gian -> để nguyên tiếng Việt
    for u in units:
        if u["kind"] == "ACT":
            rng = u.get("rng", "")
            if rng and not TIME_RE.search(rng):
                n_bad_act += 1
                print(f"Tap{ep} {u['id']} ACT rng KHÔNG phải mốc thời gian: {rng!r}")
                print(f"        tiêu đề: {u['vi'][:120]}")

    # (b) mục cache không đạt kiểm tra
    cp = CACHE / f"tap{ep}.json"
    if not cp.exists():
        continue
    cache = json.loads(cp.read_text(encoding="utf-8"))
    bad = []
    for u in units:
        if u["kind"] in ("RAW", "ROLE", "PAUSE"):
            continue
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = M.splittable(u)
            if parts:
                for k, p in enumerate(parts):
                    jid = f"{u['id']}#{k}"
                    if jid in cache:
                        ok, reason, kk = M.check_sentence(
                            M.repair_ja(cache[jid].get("ja", ""), p), p, ep_tokens, u["vi"])
                        if not ok:
                            bad.append((jid, reason))
                continue
            jid = f"{u['id']}#L"
            if jid in cache:
                ok, reason, kk = M.check_line(
                    M.repair_ja(cache[jid].get("ja", ""), u["vi"]), u["vi"], u.get("n", 0), ep_tokens)
                if not ok:
                    bad.append((jid, reason))
            continue
        if u["id"] in cache:
            ok, reason, kk = M.check_meta(
                M.repair_ja(cache[u["id"]].get("ja", ""), u["vi"]), u["vi"], ep_tokens)
            if not ok:
                bad.append((u["id"], reason))
    if bad:
        n_stale += len(bad)
        per_ep.append((ep, len(bad)))
        print(f"\nTap{ep}: {len(bad)} mục cache không đạt")
        for jid, reason in bad[:14]:
            print(f"    {jid}: {reason[:120]}")

print(f"\n==> ACT rng sai: {n_bad_act} · mục cache cần dịch lại: {n_stale}")
print(f"    theo tập: {per_ep}")
