#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra anh TINH (da QC) co khop voi khung hinh THAT trong video da render hay khong.

Voi moi shot trong khoang da render: trich 1 khung tu mp4 tai dung frame giua shot,
so voi anh tinh cua shot do. Do lech trung binh (MAE) phai NHO (nhieu < 6/255);
lon > 15 => noi dung lech (sai nen / sai chu / sai mau).

Vay la bang chung cho H9: anh tinh QC duoc ap dung cho video that.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
import numpy as np  # noqa: E402
from PIL import Image  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FPS = 30
shots = json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))["shots"]
STILL = W / "video3_EN_t03" / "stills"
TMP = W / "_ab_frame_check"
TMP.mkdir(exist_ok=True)

CHUNK = sys.argv[1] if len(sys.argv) > 1 else "A"
VID = {"A": W / "video3_EN_t03_cA" / "chunkA.mp4",
       "B": W / "video3_EN_t03_cB" / "chunkB.mp4",
       "C": W / "video3_EN_t03_cC" / "chunkC.mp4"}[CHUNK]
if not VID.exists():
    raise SystemExit(f"khong co {VID}")

rng = {"A": (0, 549.0), "B": (549.0, 1098.0), "C": (1098.0, 1646.62)}[CHUNK]
lo, hi = rng
# MOI CHUNK bat dau o frame CUC BO 0 => phai tru offset khi seek trong file chunk
OFF = int(round(lo * FPS))          # A:0 · B:16470 · C:32940

rows = []
for s in shots:
    mid = (s["start"] + s["end"]) / 2
    if not (lo <= mid < hi):
        continue
    fi = int(mid * FPS)
    lfi = fi - OFF                   # frame cuc bo trong file chunk
    still = STILL / f"shot_{s['id']}.png"
    if not still.exists():
        continue
    out = TMP / f"{s['id']}.png"
    # -ss TRUOC -i (fast seek) + accurate_seek mac dinh => dung frame canh bang
    subprocess.run([str(FF), "-y", "-v", "error", "-accurate_seek",
                    "-ss", f"{lfi / FPS:.6f}", "-i", str(VID),
                    "-frames:v", "1", str(out)],
                   check=True)
    if not out.exists():
        rows.append((s["id"], mid, None, "khong trich duoc khung"))
        continue
    a = np.asarray(Image.open(still).convert("RGB"), dtype=np.int16)
    b = np.asarray(Image.open(out).convert("RGB").resize(a.shape[1::-1]), dtype=np.int16)
    mae = float(np.abs(a - b).mean())
    rows.append((s["id"], mid, mae, ""))

print(f"=== so san anh tinh vs video chunk {CHUNK} ({len(rows)} shot) ===")
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
    print(f"\nMAE trung binh {sum(vals) / len(vals):.2f} · lon nhat {max(vals):.2f} · "
          f"so vuot 15: {len(bad)}/{len(rows)}")
print("KET QUA:", "PASS - anh tinh QC khop video" if not bad else f"FAIL - {len(bad)} shot lech")
sys.exit(0 if not bad else 1)
