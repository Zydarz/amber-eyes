import subprocess, pathlib, re
FF = r"D:\TEST\Gax\amber-eyes\.work\ffmpeg\ffmpeg-n9.0-latest-win64-lgpl-shared-9.0\bin\ffmpeg.exe"
for name in (r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03\xuat_ban\Tap03_master.mp4",
             r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03_EN\xuat_ban\Tap03_EN_master.mp4"):
    p = pathlib.Path(name)
    if not p.exists():
        print(p.name, "KHONG CO"); continue
    r = subprocess.run([FF, "-i", str(p), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    s = r.stderr.split("Summary:")[-1]
    iu = re.findall(r"I:\s*(-?[\d.]+)\s*LUFS", s)
    pk = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", s)
    lra = re.findall(r"LRA:\s*(-?[\d.]+)\s*LU", s)
    print(f"{p.name}: LUFS={iu[-1] if iu else '?'} · true peak={pk[-1] if pk else '?'} dBFS · LRA={lra[-1] if lra else '?'}")
