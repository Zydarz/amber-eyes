import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cmd = ["git", "diff", "--stat", "02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print(res.stdout)

cmd2 = ["git", "diff", "02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md"]
res2 = subprocess.run(cmd2, capture_output=True, text=True, encoding="utf-8")
print(res2.stdout[:1500])
