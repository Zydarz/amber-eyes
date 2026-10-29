#!/usr/bin/env python3
"""Align VN vs KO elements with difflib and report every mismatch in kind/role/sentence count."""
import difflib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

vn_path = Path(sys.argv[1])
ko_path = Path(sys.argv[2])

vn = PK.parse_lines(vn_path.read_text(encoding="utf-8").splitlines())
ko = PK.parse_lines(ko_path.read_text(encoding="utf-8").splitlines())


def st(s):
    if isinstance(s, dict):
        return str(s.get("text", s))
    return str(s)


def sig(e):
    return (e.get("kind"), e.get("role") or "", len(e.get("sentences") or []))


sv = [sig(e) for e in vn]
sk = [sig(e) for e in ko]

sm = difflib.SequenceMatcher(a=sv, b=sk, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        continue
    print(f"### {tag.upper()}  vn[{i1}:{i2}]  ko[{j1}:{j2}]")
    for k in range(i1, i2):
        e = vn[k]
        print(f"  - VN  {e.get('kind'):5s} {e.get('id')!s:6s} role={e.get('role') or '':6s} "
              f"sents={len(e.get('sentences') or [])}")
        for s in (e.get("sentences") or []):
            print(f"      V| {st(s)[:150]}")
    for k in range(j1, j2):
        e = ko[k]
        print(f"  + KO  {e.get('kind'):5s} {e.get('id')!s:6s} role={e.get('role') or '':6s} "
              f"sents={len(e.get('sentences') or [])}")
        for s in (e.get("sentences") or []):
            print(f"      K| {st(s)[:150]}")
    print()
