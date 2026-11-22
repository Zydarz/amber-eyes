# -*- coding: utf-8 -*-
"""Sua lai patch ten nen Tap 03 (v3: bo dau ngoac kép thua trong NEN_SRC).

Buoc 1: khoi phuc generator tu backup .work/_cu/tk03_bgname_*/
Buoc 2: patch dung:
  - tuple bg :  ,"t3_x","still"  ->  ,"tk03_x","still"
  - NEN_SRC  :  "t3_x": "t3_x",   ->  "tk03_x": "t3_x",
"""
import glob
import io
import os
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"D:/TEST/Gax/amber-eyes"
WORK = os.path.join(ROOT, ".work")

TUPLE = re.compile(r'"(t3_[a-z0-9_]+)"(\s*,\s*"(?:still|pan|push|pull)")')
MAP = re.compile(r'"(t3_[a-z0-9_]+)"(\s*:\s*")t3_[a-z0-9_]+(")')


def find_backup(name):
    hits = sorted(glob.glob(os.path.join(WORK, "_cu", "tk03_bgname_*", ".work", name)))
    return hits[-1] if hits else None


def main():
    for gen in ("_build_tk_tap03.py", "_build_tk_tap03_multilang.py"):
        p = os.path.join(WORK, gen)
        bak = find_backup(gen)
        if bak:
            shutil.copy2(bak, p)
        s = io.open(p, encoding="utf-8").read()
        s, n1 = TUPLE.subn(lambda m: '"tk03_%s"%s' % (m.group(1)[3:], m.group(2)), s)
        s, n2 = MAP.subn(
            lambda m: '"tk03_%s"%st3_%s%s' % (m.group(1)[3:], m.group(2), m.group(1)[3:], m.group(3)), s)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s)
        print("%-32s tuple=%d  NEN_SRC=%d" % (gen, n1, n2))

    p = os.path.join(WORK, "_build_tk_tap03.py")
    s = io.open(p, encoding="utf-8").read()
    pairs = re.findall(r'"(tk03_[a-z0-9_]+)"\s*:\s*"(t3_[a-z0-9_]+)"', s)
    print("\nNEN_SRC dung: %d" % len(pairs))
    for k, v in pairs[:3]:
        print("   %-26s <- %s" % (k, v))
    bad = re.findall(r'""', s)
    print('dau ngoac kep thua:', len(bad))
    tup = re.findall(r'"(tk03_[a-z0-9_]+)"\s*,\s*"(?:still|pan|push|pull)"', s)
    print("tuple bg: %d · ten duy nhat %d" % (len(tup), len(set(tup))))
    # nen trong NEN_SRC chua co bang 28?
    allkeys = re.findall(r'"(t3_[a-z0-9_]+)"\s*:', s)
    print("key NEN_SRC con la t3_*:", len(allkeys))


if __name__ == "__main__":
    main()
