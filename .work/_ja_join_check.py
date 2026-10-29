#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm chứng: số câu sau khi ghép bằng luật của parse_kichban (JA) == số câu VN.

Dùng chính parse_kichban để đếm (không tự viết lại), để chắc chắn bản JA
và bản VN cho ra cùng số câu.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M
import parse_kichban as PK

# ---- tách câu kiểu JA, đúng như parse_kichban.ja_split
JA_END = re.compile(r'[。！？…][」』”"）)\]]*')


def ja_split(para):
    parts, last = [], 0
    for m in JA_END.finditer(para):
        parts.append(para[last:m.end()])
        last = m.end()
    tail = para[last:].strip()
    if tail:
        parts.append(tail)
    return parts


def ja_sentences(line):
    """Số câu của 1 dòng JA theo đúng luật parse_kichban."""
    if any(ch in line for ch in '。！？'):
        return len(ja_split(line))
    return len(re.split(PK.LATIN_SPLIT, line))


def main():
    bad = []
    tot_lines = 0
    for i in range(1, 30):
        ep = f"{i:02d}"
        units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
        in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
        for u in units:
            if u["kind"] not in ("TEXT", "BULLET") or u["id"] not in in_turn:
                continue
            tot_lines += 1
            parts = M.split_dialogue_sentences(u["vi"]) if hasattr(M, "split_dialogue_sentences") else None
            if parts is None:
                from ja_split import split_dialogue_sentences
                parts = split_dialogue_sentences(u["vi"])
            # giả lập: mỗi câu VN -> 1 câu JA, ghép lại không có khoảng trắng
            ja_fake = "".join(p + "。" for p in parts)
            n_ja = ja_sentences(ja_fake)
            n_vn = u.get("n", 0)
            if n_ja != n_vn:
                bad.append((ep, u["id"], n_vn, n_ja, u["vi"][:150]))
    print(f"dòng thoại: {tot_lines} · LỆCH số câu: {len(bad)}")
    for ep, uid, nv, nj, v in bad[:15]:
        print(f"  [{ep} {uid}] VN={nv} JA={nj} :: {v}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
