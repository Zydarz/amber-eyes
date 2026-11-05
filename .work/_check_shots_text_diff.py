import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cmd = ["git", "diff", "5e9910b9..HEAD", "--", ".work/shots_text_tap02_JA.json"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print("Diff in shots_text_tap02_JA.json:")
print(res.stdout[:1000] if res.stdout else "NO DIFF!")
