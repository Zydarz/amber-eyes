"""Ghep 12 part (A.part_00..05 + B.part_00..05) thanh 1 picture.mp4 bang concat -c copy.

Kiem tra truoc khi ghep:
  - moi part co frame > 0, cung kich thuoc 1920x1080, cung fps
  - tong frame == int(timeline.total * FPS)
Kiem tra sau khi ghep:
  - ffprobe: so frame, duration, DTS don dieu (khong lui), khong loi giai ma
"""
import json
import os
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("AE_EP", "06")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

VD = WORK / "video3_t06"
A = WORK / "video3_t06_A"
B = WORK / "video3_t06_B"


def probe(p):
    r = subprocess.run(
        [str(FP), "-v", "error", "-select_streams", "v:0", "-count_frames",
         "-show_entries", "stream=nb_read_frames,width,height,r_frame_rate,duration",
         "-of", "json", str(p)],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit(f"ffprobe that bai {p.name}: {r.stderr.strip()}")
    st = json.loads(r.stdout)["streams"][0]
    return {"frames": int(st.get("nb_read_frames") or 0), "w": int(st["width"]), "h": int(st["height"]),
            "fps": st["r_frame_rate"], "dur": float(st.get("duration") or 0)}


def main():
    parts = [A / f"part_{k:02d}.mp4" for k in range(6)] + [B / f"part_{k:02d}.mp4" for k in range(6)]
    missing = [p.name for p in parts if not p.exists()]
    if missing:
        raise SystemExit(f"CHẶN - thieu part: {missing}")

    total_expected = int(json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))["total"] * 30)
    info = []
    for p in parts:
        s = probe(p)
        info.append((p, s))
        print(f"  {p.parent.name}/{p.name}: {s['frames']} frame  {s['w']}x{s['h']}  "
              f"{s['fps']}  {s['dur']:.3f}s")
        if s["frames"] <= 0:
            raise SystemExit(f"CHẶN - {p.name} khong co frame")
        if (s["w"], s["h"]) != (1920, 1080):
            raise SystemExit(f"CHẶN - {p.name} sai kich thuoc {s['w']}x{s['h']}")

    tot = sum(s["frames"] for _, s in info)
    print(f"\ntong frame = {tot} (ky vong {total_expected})")
    if tot != total_expected:
        raise SystemExit(f"CHẶN - tong frame {tot} != {total_expected}")

    lst = VD / "parts12.txt"
    lst.write_text("".join(f"file '{p.as_posix()}'\n" for p, _ in info), encoding="utf-8")

    out = VD / "picture.mp4"
    r = subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c", "copy", str(out)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit(f"CHẶN - concat that bai: {r.stderr.strip()}")
    if r.stderr.strip():
        print("ffmpeg stderr:", r.stderr.strip()[:600])

    s = probe(out)
    print(f"\npicture.mp4: {s['frames']} frame  {s['w']}x{s['h']}  {s['fps']}  {s['dur']:.3f}s")
    if s["frames"] != total_expected:
        raise SystemExit(f"CHẶN - picture.mp4 co {s['frames']} frame, ky vong {total_expected}")

    # DTS phai don dieu
    r2 = subprocess.run([str(FF), "-v", "error", "-i", str(out), "-vf", "showinfo", "-f", "null", "-"],
                        capture_output=True, text=True, encoding="utf-8", errors="replace")
    bad = [L for L in r2.stderr.splitlines() if "DTS" in L and ("N/A" in L or "nan" in L.lower())]
    if bad:
        raise SystemExit(f"CHẶN - {len(bad)} dong DTS khong hop le")
    print("OK  DTS hop le (khong N/A)")
    print(f"OK  picture.mp4 -> {out}  ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
