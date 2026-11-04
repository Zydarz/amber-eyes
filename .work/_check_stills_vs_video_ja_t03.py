#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So ảnh TĨNH đã QC với khung hình THẬT trong picture.mp4 của JA Tap03.

Bằng chứng cho H9: ảnh tĩnh đã soi bằng mắt áp dụng được cho video thật.
picture.mp4 là bản ghép cuối (timeline toàn cục) ⇒ seek theo thời gian toàn cục,
không cần trừ offset chunk.

MAE < 15/255 ⇒ chỉ tổn thất nén H.264; > 15 ⇒ lệch nội dung thật.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FPS = 30
shots = json.loads((W / "shots_JA_t03.json").read_text(encoding="utf-8-sig"))["shots"]
STILL = W / "video3_JA_t03" / "stills"
VID = W / "video3_JA_t03" / "picture.mp4"
TMP = W / "_qc_frame_ja_t03"
TMP.mkdir(parents=True, exist_ok=True)

if not VID.exists():
    raise SystemExit(f"khong co {VID}")

rows = []
for s in shots:
    mid = (float(s["start"]) + float(s["end"])) / 2
    fi = int(mid * FPS)
    still = STILL / f"shot_{s['id']}.png"
    if not still.exists():
        rows.append((s["id"], mid, None, "khong co anh tinh"))
        continue
    out = TMP / f"{s['id']}.png"
    subprocess.run([str(FF), "-y", "-v", "error", "-accurate_seek",
                    "-ss", f"{fi / FPS:.6f}", "-i", str(VID),
                    "-frames:v", "1", str(out)], check=True)
    if not out.exists():
        rows.append((s["id"], mid, None, "khong trich duoc khung"))
        continue
    a = np.asarray(Image.open(still).convert("RGB"), dtype=np.int16)
    b = np.asarray(Image.open(out).convert("RGB").resize(a.shape[1::-1]), dtype=np.int16)
    mae = float(np.abs(a - b).mean())
    rows.append((s["id"], mid, mae, ""))

print(f"=== so anh tinh vs picture.mp4 (JA Tap03) — {len(rows)} shot ===")
bad = [r for r in rows if r[2] is None or r[2] > 15]
for sid, mid, mae, err in rows:
    flag = ""
    if mae is None:
        flag = "LOI " + err
    elif mae > 15:
        flag = "  <<< LECH LON"
    print(f"  {sid:6} t={mid:8.2f}s  MAE={mae if mae is None else round(mae, 2)}{flag}")
vals = [r[2] for r in rows if r[2] is not None]
if vals:
    print(f"\nMAE trung binh {sum(vals)/len(vals):.2f} · lon nhat {max(vals):.2f} · "
          f"so vuot 15: {len(bad)}/{len(rows)}")
print("KET QUA:", "PASS - anh tinh QC khop video that" if not bad else f"FAIL - {len(bad)} shot lech")
sys.exit(0 if not bad else 1)
