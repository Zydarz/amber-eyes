import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cmd = ["git", "log", "-n", "5", "--oneline", "--", ".work/shots_JA_t02.json"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print(res.stdout)
