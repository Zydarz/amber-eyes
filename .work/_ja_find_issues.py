#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tìm vị trí lỗi cụ thể trong file JA: ký tự lạ, sót tiếng Việt, số quy ước VN, rác Latin.

    py -3 .work/_ja_find_issues.py 06 09 02
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from ja_token import foreign_scripts, norm_token, token_set  # noqa: E402
import make_ja_scripts as M  # noqa: E402

VN_CHARS = set("ăâđêôơưĂÂĐÊÔƠƯ")
OK_LATIN = {norm_token(x) for x in (set(M.ALLOW_LATIN) | set(M.LOAN_WORDS)) if x}

for ep in sys.argv[1:]:
    ja = HERE.parent / "01_KICH_BAN" / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    vn = M.canonical_vn(ep)
    if not ja.exists():
        print(f"Tap{ep}: chưa có file JA")
        continue
    lines = ja.read_text(encoding="utf-8").splitlines()
    vn_text = vn.read_text(encoding="utf-8")
    vtok = token_set(vn_text)
    vlat = set(vtok)
    print(f"\n############ Tap{ep}")
    for i, ln in enumerate(lines, 1):
        issues = []
        fs = foreign_scripts(ln)
        if fs:
            issues.append(f"ký tự lạ {fs}")
        vn_left = sorted({c for c in ln if c in VN_CHARS})
        if vn_left:
            issues.append(f"sót tiếng Việt {''.join(vn_left)}")
        for m in re.finditer(r"\d{1,3}(?:\.\d{3})+|\d+,\d+", ln):
            issues.append(f"số quy ước VN {m.group(0)}")
        junk = []
        for w in re.findall(r"[A-Za-z][A-Za-z0-9\-'.]{1,}", ln):
            low = norm_token(w)
            if not low or low in vtok or low in OK_LATIN:
                continue
            if re.search(r"[a-z][A-Z]", w) or (len(w) <= 3 and not w.isupper()):
                junk.append(w)
            elif len(w) >= 4 and any(low in v and low != v for v in vlat):
                junk.append(w)
        if junk:
            issues.append(f"rác Latin {sorted(set(junk))}")
        if issues:
            print(f"  dòng {i}: {' | '.join(issues)}")
            print(f"      {ln[:240]}")
