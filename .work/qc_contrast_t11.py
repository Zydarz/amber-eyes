#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC do tuong phan chu tren anh tinh Tap 11 (Rule H20)."""
import json
import sys
from pathlib import Path
import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]

ROLE_COLOR = {
    "H": (226, 180, 103), "D": (134, 169, 204), "C": (169, 155, 214),
    "N1": (217, 185, 155), "N2": (110, 140, 160)
}
PALETTE = [
    (226, 180, 103), (242, 239, 233), (156, 152, 143), (134, 169, 204),
    (169, 155, 214), (217, 185, 155), (110, 140, 160), (232, 160, 191)
]

def lum(c):
    def f(v):
        v = v / 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(x) for x in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def scan(folder, shots_file, lang_tag):
    SH = json.loads(Path(shots_file).read_text(encoding="utf-8"))["shots"]
    role_of = {s["id"]: (s.get("role") or "H") for s in SH}
    bad, total = [], 0
    for f in sorted(Path(folder).glob("shot_*.png")):
        total += 1
        sid = f.stem.replace("shot_", "")
        im = np.asarray(Image.open(f).convert("RGB"), dtype=np.float32)
        band = im[700:1010, :, :]
        tc = np.array(ROLE_COLOR.get(role_of.get(sid, "H"), ROLE_COLOR["H"]), dtype=np.float32)
        d = np.sqrt(((band - tc) ** 2).sum(axis=2))
        mask = d < 60
        if mask.sum() < 60:
            best_m = None
            best_n = 0
            for p in PALETTE:
                m = np.sqrt(((band - np.array(p, dtype=np.float32)) ** 2).sum(axis=2)) < 50
                if m.sum() > best_n:
                    best_n = m.sum()
                    best_m = m
            if best_m is not None and best_n >= 60:
                mask = best_m
            else:
                continue
        bg_pixels = band[~mask]
        if len(bg_pixels) == 0:
            continue
        bg_med = np.median(bg_pixels, axis=0)
        fg_med = np.median(band[mask], axis=0)
        r = ratio(fg_med, bg_med)
        dl = abs(lum(fg_med) - lum(bg_med))
        if r < 1.6 or dl < 0.045:
            bad.append((sid, r, dl))
            
    print(f"[{lang_tag}] Quet {total} anh | Loi tuong phan: {len(bad)}")
    if bad:
        for sid, r, dl in bad[:10]:
            print(f"   -> Shot {sid}: ratio={r:.2f}, dl={dl:.3f}")
    return len(bad)

def main():
    print("=== KIEM TRA DO TUONG PHAN CHU (RULE H20) TAP 11 ===")
    errs = 0
    errs += scan(ROOT / ".work/video3_t11/stills", ROOT / ".work/shots_t11.json", "VI")
    errs += scan(ROOT / ".work/video3_EN_t11/stills", ROOT / ".work/shots_EN_t11.json", "EN")
    errs += scan(ROOT / ".work/video3_JA_t11/stills", ROOT / ".work/shots_JA_t11.json", "JA")
    if errs == 0:
        print("\nKET QUA: TAT CA ANH DEU DAT CHUAN TUONG PHAN (0 CHU CHIM)")
    else:
        print(f"\nKET QUA: CO {errs} SHOT CAN XEM XET")
    return 0 if errs == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
