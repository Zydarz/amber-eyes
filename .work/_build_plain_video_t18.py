# Video "nen tho" Tap18 theo yeu cau nguoi dung (20/11/2026): intro kenh + anh nen NGUYEN BAN (khong chen chu/badge/the) + master audio.
# Thumbnail van co chu (package.thumbnail). Moc shot lay tu shots_*_t18.json; the chuyen hoi (nen 'void') giu nen shot truoc.
import json, subprocess, sys, os, shutil
from pathlib import Path
W = Path(__file__).parent; R = W.parent
FF = r"C:\Users\ADMIN\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
CFG = {"VI": ("", "Tap18", "Tap18_master", "intro_kenh.mov"), "EN": ("_EN", "Tap18_EN", "Tap18_EN_master", "intro_kenh_EN_t18.mov"),
       "JA": ("_JA", "Tap18_JA", "Tap18_JA_master", "intro_kenh_JA_t18.mov")}
AF = "alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1"
def run(c): subprocess.run([FF, "-y", "-v", "error"] + c, check=True)
for L in (sys.argv[1:] or CFG):
    suf, d, m, intro = CFG[L]
    sh = json.load(open(W/f"shots{suf}_t18.json", encoding="utf-8")); tot = sh["total"]; S = sh["shots"]
    work = W/f"plain_t18{suf}"; work.mkdir(exist_ok=True)
    INTRO = 22.40
    segs = []; prev = None
    for i, s in enumerate(S):
        bg = s["bg"] if s["bg"] != "void" else prev
        a = INTRO if i == 0 else s["start"]; b = S[i+1]["start"] if i+1 < len(S) else tot
        segs.append((bg, a, b)); prev = bg
    # frame-exact: tinh theo khung
    lst = []; t0 = 0
    for k, (bg, a, b) in enumerate(segs):
        lst.append(f"file '{(R/'assets/bg'/(bg+'.png')).as_posix()}'\nduration {b-a:.4f}")
    lst.append(f"file '{(R/'assets/bg'/(segs[-1][0]+'.png')).as_posix()}'")
    (work/"list.txt").write_text("\n".join(lst), encoding="utf-8")
    enc = ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-profile:v", "high", "-r", "30", "-g", "60"]
    run(["-i", str(R/"assets/brand"/intro), "-t", str(INTRO), "-vf", "scale=1920:1080,fps=30", *enc, str(work/"intro.mp4")])
    run(["-f", "concat", "-safe", "0", "-i", str(work/"list.txt"), "-vf", "scale=1920:1080:flags=lanczos,fps=30,format=yuv420p", *enc, str(work/"body.mp4")])
    (work/"cat.txt").write_text(f"file '{(work/'intro.mp4').as_posix()}'\nfile '{(work/'body.mp4').as_posix()}'\n", encoding="utf-8")
    run(["-f", "concat", "-safe", "0", "-i", str(work/"cat.txt"), "-c", "copy", str(work/"picture.mp4")])
    out = R/"02_SAN_XUAT"/d/"xuat_ban"/(m+".mp4")
    run(["-i", str(work/"picture.mp4"), "-i", str(R/"02_SAN_XUAT"/d/"xuat_ban"/(m+".wav")), "-map", "0:v", "-map", "1:a", "-c:v", "copy",
         "-af", AF, "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)])
    print(L, "ok", out, flush=True)
