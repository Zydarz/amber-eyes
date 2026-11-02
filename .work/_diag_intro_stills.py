#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chan doan 9 shot 1-00..1-08 khong render duoc (vung intro)."""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"

sh = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
print("=== moc thoi gian 9 shot dau ===")
for s in sh[:10]:
    mid = (s["start"] + s["end"]) / 2
    print(f"  {s['id']}: {s['start']:>8.2f} -> {s['end']:>8.2f} · mid={mid:>8.3f} · fi={int(mid*30):>6}")

FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
intro = ROOT / "assets" / "brand" / "intro_kenh_JA_t02.mov"
r = subprocess.run([str(FF), "-i", str(intro)], capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
for line in (r.stderr or "").splitlines():
    if "Duration" in line or "Stream" in line:
        print("  intro:", line.strip())

print("\n=== ffmpeg -ss truc tiep tai cac fi cua shot 1-00..1-08 ===")
for s in sh[:9]:
    mid = (s["start"] + s["end"]) / 2
    fi = int(mid * 30)
    r = subprocess.run([str(FF), "-v", "error", "-ss", f"{fi/30:.3f}", "-i", str(intro),
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                       capture_output=True)
    err = (r.stderr or b"").decode("utf-8", "replace").strip()
    print(f"  {s['id']}: fi={fi} ({fi/30:.3f}s) · byte={len(r.stdout)}"
          + (f" · ERR: {err[:120]}" if err else ""))

print("\n=== render tung shot (stderr -> file) ===")
LOG = W / "_diag_stills_intro.log"
r = subprocess.run([sys.executable, str(W / "build_video3.py"),
                    "--stills", ",".join(s["id"] for s in sh[:9])],
                   cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
LOG.write_text((r.stdout or "") + "\n---STDERR---\n" + (r.stderr or ""), encoding="utf-8")
print(f"  rc={r.returncode}")
print("  stdout:", (r.stdout or "").strip()[:400])
print("  stderr:", (r.stderr or "").strip()[:1500])
sd = W / "video3_JA_t02" / "stills"
for s in sh[:9]:
    p = sd / f"shot_{s['id']}.png"
    print(f"    {p.name}: exists={p.exists()} size={p.stat().st_size if p.exists() else 0}")
