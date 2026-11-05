# -*- coding: utf-8 -*-
import sys, os, subprocess
sys.stdout.reconfigure(encoding='utf-8')

env = os.environ.copy()
env["AE_EP"] = "06"
env["AE_LANG"] = "en"

cmd = [sys.executable, ".work/build_video3.py", "--workers", "6"]
print(f"Launching full render: {' '.join(cmd)}")
res = subprocess.run(cmd, env=env)
print("Render process exited with code:", res.returncode)
if res.returncode != 0:
    sys.exit(res.returncode)

# Probe picture.mp4
out_mp4 = ".work/video3_EN_t06/picture.mp4"
probe_cmd = [
    "ffprobe", "-v", "error", "-show_entries",
    "format=duration:stream=nb_frames,width,height",
    "-of", "json", out_mp4
]
p_res = subprocess.run(probe_cmd, capture_output=True, text=True, encoding="utf-8")
print("Probe output:\n", p_res.stdout)
