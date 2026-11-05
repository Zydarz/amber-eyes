# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def sent_range(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:[–—\-]+`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out

# Check original parse_shots regex
def original_sent_range(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out

test_cases = [
    "`1.02#1`",
    "`1.02#2`–`#3`",
    "`1.06#8`, `1.08#1`",
    "`1.09#3`–`#6`",
    "`3.07#2`–`#3`, `3.09#1`–`#2`",
]

for tc in test_cases:
    print(tc, "-> orig:", original_sent_range(tc))
