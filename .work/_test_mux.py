import subprocess, sys, os
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
FF = W/"ffmpeg"/"ffmpeg-n9.0-latest-win64-lgpl-shared-9.0"/"bin"/"ffmpeg.exe"
FP = FF.with_name("ffprobe.exe")
bak = W/"_cu"/"picture_t03.CU_BAN.bak_20261102_113801.mp4"
tmp = W/"_cu"/"test60.mp4"
# cat 60s tu file picture CU BAN (thoi luong 1911s) de thu pipeline mux
r = subprocess.run([str(FF),"-y","-v","error","-i",str(bak),"-t","60","-c","copy",str(tmp)],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print("cat 60s:", r.returncode, r.stderr[:300])
out = W/"_cu"/"test60_mux.mp4"
mux_af = "alimiter=limit=0.7943:attack=5:release=50:level=disabled"
cmd = [str(FF),"-y","-v","error","-i",str(tmp),"-i",str(W/"audio_master_t03.wav"),
       "-map","0:v","-map","1:a","-c:v","copy","-af",mux_af,"-c:a","aac","-b:a","192k",
       "-shortest","-movflags","+faststart",str(out)]
r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
print("mux:", r.returncode, r.stderr[:400])
if out.exists():
    o = subprocess.run([str(FP),"-v","error","-show_entries","format=duration,size","-of","default=nw=1",str(out)],
                       capture_output=True, text=True)
    print("ket qua:\n"+o.stdout)
    # kiem tra loudness tren mp4 (A11 #38)
    r2 = subprocess.run([str(FF),"-i",str(out),"-af","ebur128=peak=true","-f","null","-"],
                        capture_output=True, text=True, encoding="utf-8", errors="replace")
    tail = [l for l in r2.stderr.splitlines() if "I:" in l]
    print("ebur128:", tail[-1].strip() if tail else "?")
    pk = [l for l in r2.stderr.splitlines() if "Peak:" in l]
    print("peak   :", pk[-1].strip() if pk else "?")
