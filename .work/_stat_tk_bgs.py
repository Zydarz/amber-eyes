# -*- coding: utf-8 -*-
"""Thong ke shot/nen cua cac bo TK da xuat ban de chuan hoa Tap54."""
import collections
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")

BG_KEYS = ("bg", "nen")
ID_KEYS = ("clip_line_id", "id")


def get_line_bg(l):
    for k in BG_KEYS:
        if k in l:
            return l[k]
    return None


def get_line_id(l):
    for k in ID_KEYS:
        if k in l:
            return l[k]
    return ""


for ep in ["02", "03", "04", "05", "15"]:
    d = ROOT / "02_SAN_XUAT" / "TIKTOK" / ("Tap" + ep)
    sp = d / ("SPEC_AUDIO_CLIP_TAP%s.json" % ep)
    if not sp.exists():
        continue
    spec = json.loads(sp.read_text(encoding="utf-8"))
    clips = spec.get("clips")
    if clips is None:
        continue
    if isinstance(clips, list):
        items = [(c.get("clip", c.get("id", "TK%d" % i)), c) for i, c in enumerate(clips)]
    else:
        items = list(clips.items())

    n_lines = 0
    bgcount = collections.Counter()
    per_clip = {}
    durs = []
    for cid, c in items:
        lines = c.get("lines", [])
        n_lines += len(lines)
        durs.append(c.get("total_est_duration_s", c.get("total_uoc_luong_s", 0)) or 0)
        cc = collections.Counter(get_line_bg(l) for l in lines)
        per_clip[cid] = (len(lines), len(cc), max(cc.values()) if cc else 0)
        for l in lines:
            bgcount[get_line_bg(l)] += 1

    print("Tap%s: clips=%d shots=%d distinct_bg=%d ratio=%.2f dur=%.1f-%.1f s"
          % (ep, len(items), n_lines, len(bgcount), n_lines / max(1, len(bgcount)),
             min(durs), max(durs)))
    for cid, (nl, nb, mx) in per_clip.items():
        print("    %s: lines=%2d bg=%2d max_reuse_in_clip=%d" % (cid, nl, nb, mx))
    print("    bg reused across clips:", sum(1 for v in bgcount.values() if v > 1), "of", len(bgcount))
    print()
