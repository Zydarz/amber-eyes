import os
import sys
import subprocess
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"

env = os.environ.copy()
env["AE_EP"] = "02"

cmd = ["python", str(WORK / "build_video3.py"), "--workers", "6"]
print(f"Starting build_video3.py with 6 workers at {time.strftime('%Y-%m-%d %H:%M:%S')}...")
t0 = time.time()
r = subprocess.run(cmd, env=env)
print(f"Finished build_video3.py in {time.time() - t0:.2f}s with return code {r.returncode}")
if r.returncode != 0:
    sys.exit(r.returncode)
