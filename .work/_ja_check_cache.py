#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra: với mỗi mục trong cache, hàm check_* có đạt không?

Dùng để tìm các mục 'được chấp nhận' nhưng thực ra sai.
    py -3 .work/_ja_check_cache.py 03
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402
from ja_split import split_dialogue_sentences  # noqa: E402

for ep in sys.argv[1:]:
    src = M.canonical_vn(ep)
    units = M.assign_turn_counts(M.parse_units(src))
    byid = {u["id"]: u for u in units}
    ep_tokens = M.vn_tokens_of(src.read_text(encoding="utf-8"))
    cache = json.loads((HERE / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))
    warns = cache.get("_warn", {})
    errs = cache.get("_err", {})
    print(f"########## tap{ep}: {len(warns)} canh bao, {len(errs)} loi")
    bad = []
    for jid, v in cache.items():
        if not isinstance(jid, str) or jid.startswith("_"):
            continue
        if not isinstance(v, dict):
            continue
        ja = v.get("ja", "")
        if not ja:
            continue
        if "#" in jid:
            uid, _, k = jid.partition("#")
            u = byid.get(uid)
            if u is None:
                continue
            if k == "L":
                ok, reason, kind = M.check_line(ja, u["vi"], u.get("n", 0), ep_tokens)
            else:
                parts = split_dialogue_sentences(u["vi"])
                vi = parts[int(k)] if k.isdigit() and int(k) < len(parts) else u["vi"]
                ok, reason, kind = M.check_sentence(ja, vi, ep_tokens, u["vi"])
        else:
            u = byid.get(jid)
            if u is None:
                continue
            ok, reason, kind = M.check_meta(ja, u["vi"], ep_tokens)
        if not ok:
            bad.append((jid, reason, kind, ja))
    print(f"  -> {len(bad)} muc KHONG dat kiem tra")
    for jid, reason, kind, ja in bad:
        u = byid.get(jid.partition('#')[0])
        print(f"  [{kind}] {jid}: {reason}")
        print(f"      VN: {(u['vi'][:170] if u else '?')}")
        print(f"      JA: {ja[:200]}")
    if warns:
        print("  -- canh bao trong cache:")
        for k, val in list(warns.items())[:10]:
            print(f"     {k}: {str(val)[:120]}")
