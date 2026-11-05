# -*- coding: utf-8 -*-
import sys, os, subprocess
sys.stdout.reconfigure(encoding='utf-8')

env = os.environ.copy()
env["AE_EP"] = "06"
env["AE_LANG"] = "en"

test_out = ".work/video3_EN_t06/test_5s.mp4"
cmd = [sys.executable, ".work/build_video3.py", "--from", "20.5", "--to", "25.5", "--workers", "2", "--out", test_out]
print(f"Running test: {' '.join(cmd)}")
res = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding="utf-8")
print("Return code:", res.returncode)
print("STDOUT:\n", res.stdout)
if res.stderr:
    print("STDERR:\n", res.stderr)
