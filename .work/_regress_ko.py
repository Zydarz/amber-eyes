#!/usr/bin/env python3
"""Regression parser: parse lại 4 nguồn VN/EN và so byte với fixture gốc.

Fixture (baseline đã lưu sẵn):
    .work/script_v2.json     <- Tap01 VN
    .work/script_EN.json     <- Tap01 EN
    .work/script_tap19.json  <- Tap19 VN
    .work/script_tap29.json  <- Tap29 VN

Exit 0 = tất cả khớp byte-for-byte.
"""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, '.work')
import parse_kichban as pk

ROOT = Path('.')
CASES = [
    ('Tap01 VN', '01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md', '.work/script_v2.json'),
    ('Tap01 EN', '01_KICH_BAN/Tap01_EN/kichban_tap01_EN.md', '.work/script_EN.json'),
    ('Tap19 VN', '01_KICH_BAN/Tap19/kichban_tap19_23102026.md', '.work/script_tap19.json'),
    ('Tap29 VN', '01_KICH_BAN/Tap29/kichban_tap29_23102026.md', '.work/script_tap29.json'),
]

ok = True
for label, src, fix in CASES:
    sp = ROOT / src
    fp = ROOT / fix
    if not sp.exists():
        print('SKIP  %-9s source missing: %s' % (label, src))
        continue
    if not fp.exists():
        print('SKIP  %-9s fixture missing: %s' % (label, fix))
        continue
    els = pk.parse_file(str(sp))
    got = json.dumps(els, ensure_ascii=False, indent=1)
    want = fp.read_text(encoding='utf-8')
    same = got == want
    ok = ok and same
    print('%-5s %-9s %s' % ('MATCH' if same else 'DIFF', label, src))
    if not same:
        print('   fixture %s  md5=%s' % (fix, hashlib.md5(want.encode()).hexdigest()))
        print('   fresh                    md5=%s' % hashlib.md5(got.encode()).hexdigest())
        g = json.loads(got)
        w = json.loads(want)
        print('   elements: fixture=%d fresh=%d' % (len(w), len(g)))
        for i, (a, b) in enumerate(zip(w, g)):
            if a != b:
                print('   first diff at element %d (%s)' % (i, a.get('id')))
                for k in sorted(set(a) | set(b)):
                    if a.get(k) != b.get(k):
                        print('      key %r: fixture=%r' % (k, str(a.get(k))[:160]))
                        print('      key %r: fresh  =%r' % (k, str(b.get(k))[:160]))
                break

print()
print('REGRESSION', 'PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
