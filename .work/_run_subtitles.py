# -*- coding: utf-8 -*-
import sys, os, subprocess
sys.stdout.reconfigure(encoding='utf-8')

env = os.environ.copy()
env["AE_EP"] = "06"
env["AE_LANG"] = "en"

cmd = [sys.executable, ".work/subtitles.py"]
print(f"Running: {' '.join(cmd)}")
res = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding="utf-8")
print("Return code:", res.returncode)
print("STDOUT:\n", res.stdout)
if res.stderr:
    print("STDERR:\n", res.stderr)
