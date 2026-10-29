#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B8 — <tập>.srt from the measured timeline (plan v9 section 7.3).

Cue: <= 2 lines x 42 chars, <= 6 s. Long sentences split at the comma nearest
the middle (time split by character ratio inside the sentence only).
The first cue of every turn carries the speaker tag, e.g. [ĐIỀU TRA VIÊN].
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402  (AE_LANG=en -> English edition)

ROOT = Path(r"D:\TEST\Gax\Audi")
OUT_DIR = ED.OUT_DIR
TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
TAG = ED.SUB_TAG
MAXC, MAXT = 84, 6.0


def split_text(t, maxc=MAXC):
    t = t.strip()
    if len(t) <= maxc:
        return [t]
    mid = len(t) / 2
    pattern = r"[,;:–—―…、。』」）\)]\s*" if ED.JA else r"[,;:–—]\s*"
    cuts = [m.end() for m in re.finditer(pattern, t) if 0 < m.end() < len(t)]
    if not cuts:
        cuts = [m.start() for m in re.finditer(r"\s", t) if 0 < m.start() < len(t)]
    if not cuts:
        cuts = [int(mid)]
    c = min(cuts, key=lambda k: abs(k - mid))
    left = t[:c].strip()
    right = t[c:].strip()
    if not left:
        return split_text(right, maxc)
    if not right:
        return split_text(left, maxc)
    return split_text(left, maxc) + split_text(right, maxc)


def two_lines(t):
    max_line = 24 if ED.JA else (32 if ED.KO else 42)
    if len(t) <= max_line:
        return t
    if ED.JA:
        mid = len(t) // 2
        cuts = [m.end() for m in re.finditer(r"[、。――…」）)\]]", t)]
        k = min(cuts, key=lambda i: abs(i - mid)) if cuts else mid
        return t[:k].strip() + "\n" + t[k:].strip()
    words = t.split()
    # break where the longer of the two lines is shortest
    k = min(range(1, len(words)), key=lambda i: max(len(" ".join(words[:i])), len(" ".join(words[i:]))))
    return " ".join(words[:k]) + "\n" + " ".join(words[k:])


def ts(x):
    h, r = divmod(x, 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"


def main():
    cues, prev_el = [], None
    for it in TL["items"]:
        parts = split_text(it["text"])
        if it["element"] != prev_el:            # the speaker tag shares the first cue's length budget
            parts = split_text(parts[0], MAXC - len(TAG[it["role"]]) - 3) + parts[1:]
        total = sum(len(p) for p in parts)
        t = it["start"]
        dur = it["end"] - it["start"]
        for k, p in enumerate(parts):
            d = dur * len(p) / total
            txt = p
            if k == 0 and it["element"] != prev_el:
                txt = f"[{TAG[it['role']]}] {p}"
            cues.append((t, t + d, two_lines(txt)))
            t += d
        prev_el = it["element"]
    out = []
    for i, (a, b, txt) in enumerate(cues, 1):
        out.append(f"{i}\n{ts(a)} --> {ts(min(b, a + MAXT))}\n{txt}\n")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / ED.SRT).write_text("\n".join(out), encoding="utf-8")
    long_ = sum(1 for a, b, _ in cues if b - a > MAXT)
    print(f"{len(cues)} cue · cue > 6 s bị cắt bớt thời gian hiển thị: {long_}")


if __name__ == "__main__":
    main()
