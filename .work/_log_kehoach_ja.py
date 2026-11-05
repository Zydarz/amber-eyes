import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cmd = ["git", "log", "-n", "5", "--oneline", "--", "02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print(res.stdout)
