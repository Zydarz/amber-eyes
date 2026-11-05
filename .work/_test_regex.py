# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def extract_sentence_ids(cstr):
    clean = cstr.replace('`', '')
    res = []
    # splits segments like "3.07#2–#3, 3.09#1–#2"
    for seg in clean.split(','):
        seg = seg.strip()
        m = re.match(r'(\d+\.\d+)#(\d+)(?:[–—\-]+#?(\d+))?', seg)
        if m:
            prefix, s_start, s_end = m.groups()
            st = int(s_start)
            en = int(s_end) if s_end else st
            for i in range(st, en + 1):
                res.append(f"{prefix}#{i}")
    return res

test_cases = [
    "`1.02#1`",
    "`1.02#2`–`#3`",
    "`1.06#8`, `1.08#1`",
    "`1.09#3`–`#6`",
    "`3.07#2`–`#3`, `3.09#1`–`#2`",
    "`5.06#13`–`#15`",
]

for tc in test_cases:
    print(f"{tc} -> {extract_sentence_ids(tc)}")
