import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
os.environ["AE_EP"] = "05"
import subprocess

r = subprocess.run(["python", ".work/parse_shots.py"], capture_output=True, text=True, encoding="utf-8")
print("STDOUT:\n", r.stdout)
print("STDERR:\n", r.stderr)
print("EXIT CODE:", r.returncode)
