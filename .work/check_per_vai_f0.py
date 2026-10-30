"""Do F0 tung file DEMO_vai_*.mp3 de chung minh moi file chua dung 1 vai."""
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from g9_decide import f0_p2, fix_octave  # noqa: E402
from check_reel_f0 import ac_of  # noqa: E402

FF = HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
OUT = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban"
EXPECT = {"H": (130.4, "nam"), "D": (198.3, "nam"), "C": (214.3, "nu"),
          "N1": (184.6, "nu"), "N2": (285.7, "nu")}

print("%-6s %8s %8s  %-6s %-10s %s" % ("vai", "ac", "pp2", "gioi", "F0 ky vong", "ket luận"))
for role, (e, gioi) in EXPECT.items():
    p = OUT / f"DEMO_vai_{role}.mp3"
    if not p.exists():
        print("!! thieu", p.name)
        continue
    r = subprocess.run([str(FF), "-v", "error", "-i", str(p), "-ac", "1", "-ar", "24000",
                        "-f", "f32le", "-"], capture_output=True, check=True)
    x = np.frombuffer(r.stdout, np.float32).copy()
    ac = ac_of(x, 24000)
    p2 = f0_p2(x, 24000)
    p2f, tag = fix_octave(ac, p2)
    # gioi tính theo nguong 165 Hz
    thuc = "nam" if ac < 165 else "nu"
    ok = "DUNG" if thuc == gioi else "SAI GIOI"
    print("%-6s %8.1f %8.1f  %-6s %-10s %s" % (role, ac, p2f, thuc, "%.1f Hz" % e, ok))
