import subprocess
from pathlib import Path

ff = Path(".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe")
for p in Path("assets/sfx/t05").glob("*.wav"):
    r = subprocess.run([str(ff), "-v", "error", "-show_entries", "format=duration,size", "-of", "default=noprint_wrappers=1", str(p)], capture_output=True, text=True)
    print(p.name, r.stdout.strip())
