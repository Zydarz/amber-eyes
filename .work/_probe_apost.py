import sys, re
sys.stdout.reconfigure(encoding="utf-8")
files = {
 "EN": r"D:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md",
 "JA": r"D:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md",
 "KO": r"D:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap02_KO/kichban_tap02_KO.md",
 "VN": r"D:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap02/kichban_tap02_22102026.md",
}
for tag, p in files.items():
    lines = open(p, encoding="utf-8").read().splitlines()
    hits = []
    for i, l in enumerate(lines, 1):
        n = l.count("'")
        if n:
            hits.append((i, n))
    print(f"=== {tag}: {len(hits)} dong co dau nhay ASCII '")
    for i, n in hits[:14]:
        print(f"   {i} ({n}): {lines[i-1][:110]}")
    if len(hits) > 14: print(f"   ... +{len(hits)-14} dong")
