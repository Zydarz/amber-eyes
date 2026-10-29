import subprocess
from pathlib import Path

ff = Path(".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe")
p = Path("assets/sfx/fx_sigh_emotional.wav")
r = subprocess.run([str(ff), "-v", "error", "-show_entries", "format=duration,size", "-of", "default=noprint_wrappers=1", str(p)], capture_output=True, text=True)
print(p.name, r.stdout.strip())
