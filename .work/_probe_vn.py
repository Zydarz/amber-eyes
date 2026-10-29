#!/usr/bin/env python3
"""Probe a VN script: quote pairs, element text scope, proper names per turn."""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

raw = Path(sys.argv[1]).read_text(encoding="utf-8")
q = re.findall(r"'([^']{2,})'", raw)
print(f"VN single-quote pairs: {len(q)}")
for x in q:
    print("   ", x[:100])

els = PK.parse_lines(raw.splitlines())
print("\nelements:", len(els))
for e in els:
    if e.get("kind") != "LOI":
        continue
    names = re.findall(r"(?<![A-Za-z])[A-Z][A-Za-z'\-]{2,}(?:\s+[A-Z][A-Za-z'\-]{2,})*(?![A-Za-z])",
                       e.get("text", ""))
    multi = [n for n in names if " " in n]
    nums = sorted(set(re.sub(r"[.,]", "", m) for m in re.findall(r"\d+(?:[.,]\d+)*", e.get("text", ""))))
    print(f"  {e['id']:5s} role={e.get('role')} sents={len(e['sentences']):2d} "
          f"nums={nums} multi={multi}")
    print(f"        keys={sorted(e.keys())}")
    break

print("\n-- all LOI: multiword proper names + digits --")
for e in els:
    if e.get("kind") != "LOI":
        continue
    names = re.findall(r"(?<![A-Za-z])[A-Z][A-Za-z'\-]{2,}(?:\s+[A-Z][A-Za-z'\-]{2,})*(?![A-Za-z])",
                       e.get("text", ""))
    multi = [n for n in names if " " in n]
    nums = sorted(set(re.sub(r"[.,]", "", m) for m in re.findall(r"\d+(?:[.,]\d+)*", e.get("text", ""))))
    if multi or nums:
        print(f"  {e['id']:5s} sents={len(e['sentences']):2d} nums={nums} multi={multi}")

print("\n-- first LOI element raw fields --")
for e in els:
    if e.get("kind") == "LOI":
        for k, v in e.items():
            if k in ("sentences",):
                continue
            print(f"   {k} = {str(v)[:200]!r}")
        break
