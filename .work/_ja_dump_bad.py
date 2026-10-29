#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liệt kê CHÍNH XÁC các mục cache KHÔNG đạt kiểm tra (dùng đúng hàm check của
pipeline), kèm nguồn VN để sửa tay / sửa cơ học.

    py -3 .work/_ja_dump_bad.py            # tất cả
    py -3 .work/_ja_dump_bad.py 25 28      # chỉ Tap25 Tap28
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import make_ja_scripts as M  # noqa: E402

TARGET = [a for a in sys.argv[1:]] or [f"{i:02d}" for i in range(1, 30)]


def jobs_for(ep):
    src = M.canonical_vn(ep)
    units = M.assign_turn_counts(M.parse_units(src))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    out = []
    for u in units:
        if u["kind"] == "RAW":
            continue
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = M.splittable(u)
            if parts:
                for k, p in enumerate(parts):
                    out.append({"id": f"{u['id']}#{k}", "vi": p, "ctx": u["vi"],
                                "kind": "dialogue", "unit": u})
                continue
            out.append({"id": f"{u['id']}#L", "vi": u["vi"], "ctx": u["vi"],
                        "kind": "line", "n": u.get("n", 0), "unit": u})
            continue
        if u["kind"] == "TABLE":
            out.append({"id": u["id"], "vi": u["vi"], "kind": "table",
                        "cells": u["vi"].split("\t"), "unit": u})
            continue
        out.append({"id": u["id"], "vi": u["vi"], "kind": "meta", "unit": u})
    return out, units


def main():
    total = 0
    for ep in TARGET:
        cp = HERE / "ja_cache" / f"tap{ep}.json"
        if not cp.exists():
            continue
        cache = json.loads(cp.read_text(encoding="utf-8"))
        jobs, units = jobs_for(ep)
        ukind = {u["id"]: u["kind"] for u in units}
        src_text = M.canonical_vn(ep).read_text(encoding="utf-8")
        ep_tokens = M.vn_tokens_of(src_text)
        bad = []
        for j in jobs:
            if j["id"] not in cache:
                continue
            if j["kind"] == "meta" and j["unit"]["kind"] in ("ROLE", "PAUSE"):
                continue
            raw = cache[j["id"]].get("ja", "") if isinstance(cache[j["id"]], dict) else ""
            ja = M.repair_ja(raw, j["vi"])
            if j["kind"] == "table" and ("\n" in ja or "\r" in ja):
                ja = ja.replace("\r\n", "<br>").replace("\r", "<br>").replace("\n", "<br>").strip()
            if j["kind"] == "dialogue":
                ok, reason, kind = M.check_sentence(ja, j["vi"], ep_tokens, j.get("ctx", ""))
            elif j["kind"] == "line":
                ok, reason, kind = M.check_line(ja, j["vi"], j.get("n", 0), ep_tokens)
            else:
                ok, reason, kind = M.check_meta(ja, j["vi"], ep_tokens)
            if not ok:
                bad.append((j, ja, reason, kind))
        if not bad:
            continue
        print(f"\n########## Tap{ep}: {len(bad)} mục lỗi ##########")
        for j, ja, reason, kind in bad:
            print(f"\n[{j['id']}] kind={j['kind']} ukind={ukind.get(j['id'])} err={kind}")
            print(f"  VN : {j['vi']}")
            print(f"  JA : {ja}")
            print(f"  WHY: {reason}")
            total += 1
    print(f"\n\nTONG {total} muc that bai")


if __name__ == "__main__":
    main()
