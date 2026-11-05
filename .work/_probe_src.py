import sys, re
sys.stdout.reconfigure(encoding="utf-8")
p = r"D:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md"
lines = open(p, encoding="utf-8").read().splitlines()
for i, l in enumerate(lines, 1):
    if any(k in l for k in ("know the answers", "boot print", "what to say", "expulsion", "decisive blow")):
        print(i, repr(l))
