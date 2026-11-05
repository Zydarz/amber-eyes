import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cmd = ["git", "show", "5e9910b9:.work/edition.py"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
for l in res.stdout.splitlines():
    if "PLAN" in l or "KeHoach" in l or "02" in l:
        print(l)
