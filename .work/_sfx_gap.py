# -*- coding: utf-8 -*-
"""
Trich danh sach "dai nen moi" CON THIEU trong assets/sfx/ tu muc 5.2 cua
02_SAN_XUAT/Danh_Sach_SFX_Tap03-29.md.

Muc 5.2 liet ke, theo tung tap, cac file nen moi phai tao.
Tao file JSON: .work/sfx_gap.json
  [{ "code": "amb_hospital_ventilator", "tap": ["04"], "mo_ta": "..." }, ...]
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "02_SAN_XUAT" / "Danh_Sach_SFX_Tap03-29.md"
SFX_DIR = ROOT / "assets" / "sfx"
OUT = ROOT / ".work" / "sfx_gap.json"

CODE_RE = re.compile(r"`([a-z0-9_]+\.wav)`")


def existing_codes() -> set[str]:
    """Tat ca file .wav dang co trong assets/sfx/ (goc + tXX/)."""
    found: set[str] = set()
    for p in SFX_DIR.rglob("*.wav"):
        found.add(p.stem)
    return found


def parse() -> list[dict]:
    text = DOC.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Chi lay phan muc 5.2
    try:
        i0 = next(i for i, l in enumerate(lines) if l.startswith("### 5.2"))
    except StopIteration:
        return []
    try:
        i1 = next(i for i, l in enumerate(lines) if i > i0 and l.startswith("## 6."))
    except StopIteration:
        i1 = len(lines)

    have = existing_codes()
    gap: dict[str, dict] = {}

    for line in lines[i0:i1]:
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 3:
            continue
        tap = cols[0]
        if not tap.isdigit():
            continue
        last = cols[-1]
        # Cot cuoi chua "Dai nen moi phai tao" -> tach theo dau phay
        for raw in last.split(","):
            m = CODE_RE.search(raw)
            if not m:
                continue
            fname = m.group(1)
            code = fname[:-4]
            note = raw.replace(f"`{fname}`", "").strip(" .")
            if code in have:
                continue
            entry = gap.setdefault(
                code, {"code": code, "tap": [], "ghi_chu": note}
            )
            if tap not in entry["tap"]:
                entry["tap"].append(tap)

    out = sorted(gap.values(), key=lambda x: x["code"])
    for e in out:
        e["tap"] = sorted(e["tap"], key=int)
    return out


if __name__ == "__main__":
    rows = parse()
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Thieu {len(rows)} file nen moi -> {OUT}")
    for r in rows:
        print(f"  {r['code']:<38} tap {','.join(r['tap']):<14} {r['ghi_chu'][:44]}")
