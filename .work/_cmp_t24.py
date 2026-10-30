#!/usr/bin/env python3
"""Side-by-side element comparison for Tap24 VN vs KO."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VN = Path(__file__).resolve().parents[1] / "01_KICH_BAN" / "Tap24" / "kichban_tap24_23102026.md"
KO = Path(__file__).resolve().parents[1] / "01_KICH_BAN" / "Tap24_KO" / "kichban_tap24_KO.md"

vn = PK.parse_lines(VN.read_text(encoding="utf-8").splitlines())
ko = PK.parse_lines(KO.read_text(encoding="utf-8").splitlines())

print(f"VN els={len(vn)}  KO els={len(ko)}")
print(f"VN sents={sum(len(e.get('sentences') or []) for e in vn)}  "
      f"KO sents={sum(len(e.get('sentences') or []) for e in ko)}")
print()

def sig(e):
    k = e.get("kind")
    rid = e.get("role") or ""
    n = len(e.get("sentences", []) or [])
    sec = f" sec={e.get('sec')}" if k == "NGHI" else ""
    return f"kind={k:5s} id={e.get('id')!s:6s} role={rid:6s} sents={n}{sec}"

n = max(len(vn), len(ko))
for i in range(n):
    a = sig(vn[i]) if i < len(vn) else "--- MISSING IN VN ---"
    b = sig(ko[i]) if i < len(ko) else "--- MISSING IN KO ---"
    flag = "  " if a == b else "**"
    print(f"{i+1:3d} {flag} VN: {a}")
    print(f"    {flag} KO: {b}")
    if a != b and i < len(vn) and i < len(ko):
        def st(s):
            if isinstance(s, dict):
                return str(s.get("text", s))[:200]
            return str(s)[:200]
        print(f"      VN sents:")
        for s in (vn[i].get("sentences") or []):
            print(f"        - {st(s)}")
        print(f"      KO sents:")
        for s in (ko[i].get("sentences") or []):
            print(f"        - {st(s)}")
