import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from PIL import Image

ROOT = Path("D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"

sd = W / "video3_JA_t02" / "stills"
if sd.exists():
    shutil.rmtree(sd)
sd.mkdir(parents=True, exist_ok=True)
print(f"Cleared stills directory: {sd}")

LOG = W / "_stills_ja_t02.log"
t0 = time.time()
with open(LOG, "w", encoding="utf-8") as fh:
    r = subprocess.run([sys.executable, str(W / "build_video3.py"), "--stills", "all"],
                       cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT)
dt = time.time() - t0
print(f"build_video3 --stills all: rc={r.returncode} · {dt:.1f} s · log={LOG.name}")

shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
ids = [s["id"] for s in shots]
missing, zero, badsize = [], [], []
for sid in ids:
    p = sd / f"shot_{sid}.png"
    if not p.exists():
        missing.append(sid)
        continue
    if p.stat().st_size == 0:
        zero.append(sid)
        continue
    with Image.open(p) as im:
        if im.size != (1920, 1080):
            badsize.append((sid, im.size))

print(f"\n=== KIEM TRA {len(ids)} STILLS ===")
print(f"  Tong so shot: {len(ids)}")
print(f"  Thieu file:   {len(missing)} {missing[:10]}")
print(f"  0 byte:       {len(zero)} {zero[:10]}")
print(f"  Sai size:     {len(badsize)} {badsize[:6]}")
passed = (len(missing) == 0 and len(zero) == 0 and len(badsize) == 0)
print(f"\nKET QUA STILLS: {'PASS' if passed else 'FAIL'}")
if not passed:
    raise SystemExit("Stills validation failed!")
