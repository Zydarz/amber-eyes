import json, re, subprocess, sys
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
FF = W/"ffmpeg"/"ffmpeg-n9.0-latest-win64-lgpl-shared-9.0"/"bin"/"ffmpeg.exe"
FP = FF.with_name("ffprobe.exe")
wav = W/"audio_master_t03.wav"
mp3 = Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03\xuat_ban\Tap03_master.mp3")
def run(a):
    r = subprocess.run(a, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout, r.stderr
def dur(p):
    o,_ = run([str(FP),"-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",str(p)])
    return float(o.strip())
print("=== THOI LUONG ===")
dw, dm = dur(wav), dur(mp3)
print(f"  wav={dw:.3f}s  mp3={dm:.3f}s  lech={abs(dw-dm):.4f}s")
tl = json.loads((W/"timeline_s_t03.json").read_text(encoding="utf-8-sig"))
print(f"  timeline.total={tl['total']}  intro={tl['intro']}  items={len(tl['items'])}")
print(f"  |wav - timeline| = {abs(dw-tl['total']):.4f}s")
print("=== KHOANG CAM (V4: >0,3 s tai -60 dB) ===")
_,e = run([str(FF),"-i",str(wav),"-af","silencedetect=n=-60dB:d=0.3","-f","null","-"])
s60 = re.findall(r"silence_start:\s*([\d.]+)", e)
dur60 = re.findall(r"silence_duration:\s*([\d.]+)", e)
print(f"  so doan cam: {len(s60)}")
for a,b in list(zip(s60,dur60))[:20]:
    print(f"    tai {a}s  dai {b}s")
print("=== DO LON ===")
_,e2 = run([str(FF),"-i",str(wav),"-af","ebur128=peak=true","-f","null","-"])
tail = [l for l in e2.splitlines() if "I:" in l]
print("  "+ (tail[-1].strip() if tail else "no I:"))
m = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", tail[-1]) if tail else None
lufs = float(m.group(1)) if m else None
pk = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", e2)
print(f"  LUFS={lufs}  Peak={pk[-1] if pk else '?'} dBFS")
print("=== LOI DAU ===")
first = tl["items"][0]["start"]; last = tl["items"][-1]["end"]
print(f"  loi dau {first}s  (can 22,8-23,5)   loi cuoi het {last}s   tong {tl['total']}s")
print("=== GIAI MA ===")
_,err, = run([str(FF),"-v","error","-i",str(wav),"-f","null","-"])
print("  wav decode errors:", len([l for l in err.splitlines() if l.strip()]))
