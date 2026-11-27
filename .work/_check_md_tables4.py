# -*- coding: utf-8 -*-
"""Kiem tra so o cua cac bang markdown trong 1 file (T25): moi dong phai khop header."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def cells(line):
    """Dem o bang bo qua dau | da escape (\\|) va dau | trong code span."""
    s = re.sub(r"\\\|", "\x00", line)
    s = re.sub(r"`[^`]*`", lambda m: m.group(0).replace("|", "\x00"), s)
    return s.count("|") - 1


def check(path):
    raw = path.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(nl)
    bad = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1].strip()):
            ncol = cells(l)
            sep = cells(lines[i + 1])
            if sep != ncol:
                bad.append((i + 1, ncol, sep, lines[i + 1].strip()[:40]))
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                c = cells(lines[j])
                if c != ncol:
                    bad.append((j + 1, ncol, c, lines[j].strip()[:70]))
                j += 1
            i = j
        else:
            i += 1
    print(f"{path.name}: {len(bad)} dong sai so o")
    for ln, exp, got, txt in bad:
        print(f"   dong {ln}: header {exp} o, dong nay {got} o | {txt}")
    return len(bad)


if __name__ == "__main__":
    total = 0
    for p in sys.argv[1:]:
        total += check(pathlib.Path(p))
    print("TONG:", total)
