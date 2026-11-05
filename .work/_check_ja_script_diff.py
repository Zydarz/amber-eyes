import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cmd = ["git", "log", "-n", "5", "--oneline", "--", "01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md", ".work/script_tap02_JA.json"]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Git log for JA script:")
print(res.stdout)

cmd_diff = ["git", "diff", "5e9910b9..HEAD", "--", "01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md", ".work/script_tap02_JA.json"]
res_diff = subprocess.run(cmd_diff, capture_output=True, text=True)
print("Diff since 5e9910b9 (Nov 4):")
print(res_diff.stdout if res_diff.stdout else "NO DIFF!")
