#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chẩn đoán: vì sao các mục bị loại? Gọi LLM rồi in lý do check_unit."""
import sys, json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M
import ja_llm

ep = sys.argv[1] if len(sys.argv) > 1 else "02"
n = int(sys.argv[2]) if len(sys.argv) > 2 else 6

units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
cache = json.loads((M.CACHE_DIR / f"tap{ep}.json").read_text(encoding="utf-8"))
by_id = {u["id"]: u for u in units}
in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
ep_tokens = M.vn_tokens_of(M.canonical_vn(ep).read_text(encoding="utf-8"))

bad = []
for uid, rec in cache.items():
    u = by_id.get(uid)
    if u is None or u["kind"] in ("ROLE", "RAW"):
        continue
    ja = rec.get("ja", "")
    kind = "dialogue" if uid in in_turn else "meta"
    ok, why = M.check_unit(u, ja, kind, ep_tokens)
    if not ok:
        bad.append((u, ja, why))
print(f"Tap{ep}: {len(bad)} mục trong cache KHÔNG đạt kiểm tra\n")
for u, ja, why in bad[:n]:
    print("=" * 72)
    print(u["id"], u["kind"], "n =", u.get("n"))
    print("VI :", u["vi"][:260])
    print("JA :", ja[:260])
    print("LÝ DO:", why)
    hard, soft = M.quality_flags(ja, M.vn_tokens_of(u["vi"]), u["vi"], ep_tokens)
    print("hard:", hard, "| soft:", soft)

# thử dịch lại mục đầu tiên để xem lỗi còn lại không
if bad:
    u, ja, why = bad[0]
    print("\n--- thử dịch lại", u["id"], "---")
    txt = ja_llm.call(M.build_prompt([u], "dialogue" if u["id"] in in_turn else "meta"),
                      M.STYLE, model=M.MODEL, max_tokens=4000, temperature=0.15, timeout=240)
    try:
        rows = M.parse_json_array(txt)
        new = rows[0]["ja"]
        print("JA mới:", new[:400])
        ok2, why2 = M.check_unit(u, new, "dialogue" if u["id"] in in_turn else "meta", ep_tokens)
        print("check:", "OK" if ok2 else "FAIL - " + why2)
    except Exception as e:
        print("parse lỗi:", e, "| raw:", txt[:300])
