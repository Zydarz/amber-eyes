import sys, pathlib
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work"); sys.path.insert(0, r"D:\TEST\Gax\amber-eyes")
import edition as ED
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
print("INTRO_MOV:", ED.INTRO_MOV, "| ton tai:", pathlib.Path(ED.INTRO_MOV).exists())
import subprocess
FF = ED.WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
if pathlib.Path(ED.INTRO_MOV).exists():
    r = subprocess.run([str(FF), "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(ED.INTRO_MOV)],
                       capture_output=True, text=True)
    print("intro duration:", r.stdout.strip(), "| rc", r.returncode)
bgs = sorted(p.name for p in (ROOT/"assets"/"bg").glob("t4_*.png"))
print("nen t4_*:", len(bgs))
for role in ("H","D","C","N1","N2"):
    d = ROOT/"assets"/"cast"/role
    print("cast %s:" % role, sorted(p.name for p in d.glob("*.png")) if d.exists() else "THIEU")
