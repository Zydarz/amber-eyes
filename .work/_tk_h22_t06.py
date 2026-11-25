# -*- coding: utf-8 -*-
"""Do H22 cho bang shot TikTok Tap 06 (VI/EN/JA) — dung est_duration_s trong spec.

H22(c): mot nen toi da 3 shot VA 30 s (theo clip: moi clip la 1 video).
Ke ca so nen >= 4 shot trong ca tap (de canh bao nen dung lam motif lap lai).
"""
import collections
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = pathlib.Path("D:/TEST/Gax/amber-eyes/02_SAN_XUAT/TIKTOK")

CLIPS = {}
for d in ("Tap06", "Tap06_EN", "Tap06_JA"):
    p = BASE / d / "SPEC_AUDIO_CLIP_TAP06.json"
    CLIPS[d] = json.loads(p.read_text(encoding="utf-8"))

viol = 0
for d, spec in CLIPS.items():
    print("=" * 12, d)
    for ck, c in spec["clips"].items():
        per = collections.defaultdict(list)
        for ln in c["lines"]:
            per[ln["bg"]].append((ln["clip_line_id"], float(ln.get("est_duration_s") or 0)))
        for bg, rows in per.items():
            n = len(rows)
            secs = sum(s for _, s in rows)
            if n > 3 or secs > 30:
                viol += 1
                print("  VI PHAM %-40s %2d shot %6.1f s  %s"
                      % (bg, n, secs, " ".join(x[0] for x in rows)))
    per = collections.defaultdict(list)
    for ck, c in spec["clips"].items():
        for ln in c["lines"]:
            per[ln["bg"]].append((ck, ln["clip_line_id"], float(ln.get("est_duration_s") or 0)))
    over = [(bg, len(v), round(sum(s for _, _, s in v), 1)) for bg, v in per.items() if len(v) > 3]
    print("  -- nen >=4 shot ca tap:", over if over else "khong co")
    print("  -- so nen duy nhat ca tap:", len(per))

print("\nTONG VI PHAM (theo clip):", viol)
