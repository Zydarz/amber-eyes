"""Đối chiếu khung hình THẬT trong video với ảnh tĩnh đã QC.

Ảnh tĩnh = render(fi) đúng pixel (trước khi mã hoá). Video = H.264 3000k ⇒
có sai số mã hoá. Nên so bằng sai số trung bình + 99% phân vị, KHÔNG so byte.

Cổng chặn: MAE < 8/255 và p99 < 30 ⇒ khung hình khớp ảnh tĩnh.
"""
import os
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("AE_EP", "06")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import numpy as np  # noqa: E402
from PIL import Image  # noqa: E402

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
STILLS = WORK / "video3_t06" / "stills"
PICTURE = WORK / "video3_t06" / "picture.mp4"
TMP = WORK / "_qc_frames_t06_v2"
TMP.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402
import json  # noqa: E402

SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))["shots"]

# các shot đã SOI MẮT (chữ trên hình đổi) + 2 shot đối chiếu
CHECK = ["1-05", "2-06", "2-08", "2-14", "2-15", "3-03", "3-04", "3-08",
         "5-01", "5-07", "5-08", "1-00", "6-00", "4-00"]

MAE_MAX = 8.0
P99_MAX = 30.0


def grab(t, dst):
    r = subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(PICTURE),
                        "-frames:v", "1", "-f", "image2", str(dst)],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0 or not dst.exists():
        raise SystemExit(f"CHẶN - không trích được khung t={t}: {r.stderr.strip()}")


def main():
    if not PICTURE.exists():
        raise SystemExit("CHẶN - chưa có picture.mp4")
    by_id = {s["id"]: s for s in SH}
    rows, bad = [], 0
    for sid in CHECK:
        png = STILLS / f"shot_{sid}.png"
        if sid not in by_id or not png.exists():
            print(f"  {sid}: bỏ qua (không có shot hoặc không có ảnh tĩnh)")
            continue
        t = (by_id[sid]["start"] + by_id[sid]["end"]) / 2
        jpg = TMP / f"f_{sid}.png"
        grab(t, jpg)
        a = np.asarray(Image.open(png).convert("RGB"), dtype=np.int16)
        b = np.asarray(Image.open(jpg).convert("RGB"), dtype=np.int16)
        if a.shape != b.shape:
            print(f"  {sid}: KÍCH THƯỚC KHÁC {a.shape} vs {b.shape}")
            bad += 1
            continue
        d = np.abs(a - b)
        mae = float(d.mean())
        p99 = float(np.percentile(d, 99))
        ok = mae < MAE_MAX and p99 < P99_MAX
        if not ok:
            bad += 1
        print(f"  {sid}  t={t:7.2f}s  MAE={mae:5.2f}  p99={p99:5.1f}  {'OK' if ok else 'NGOAI'}")
        rows.append((sid, t, mae, p99, ok))

    print(f"\n  {len(rows) - bad}/{len(rows)} khung hình khớp ảnh tĩnh (MAE < {MAE_MAX}, p99 < {P99_MAX})")
    if bad:
        raise SystemExit(f"CHẶN - {bad} khung hình lệch quá ngưỡng")
    print("OK  khung hình video khớp ảnh tĩnh đã QC")


if __name__ == "__main__":
    main()
