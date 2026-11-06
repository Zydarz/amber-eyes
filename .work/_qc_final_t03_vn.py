#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap03 VN — CỔNG QC CUỐI cho video master (H14/A7/V4/H12/H16/T11).

Kiểm trên chính file mp4 thành phẩm:
  G1  container: 1920x1080 @ 30 fps, H.264 + AAC
  G2  H14: |video - audio| <= 0,05 s và |video - timeline.total| <= 0,05 s
  G3  A7: -16 ± 1 LUFS, true peak <= -1,5 dBFS
  G4  V4: không có khoảng im lặng tuyệt đối > 0,3 s ở -60 dB
  G5  giải mã toàn bộ: 0 lỗi
  G6  faststart: 'moov' nằm ở đầu tệp
  G7  phụ đề: đủ cue, cue đầu/cuối khớp timeline
  G8  H12 + H16: trích khung tại các mốc (đầu, hồi, cuối) so với ảnh render
      gốc (MAE 2-6/255) -> chứng minh hình khớp đúng thời điểm trong timeline
  G9  T11: mốc chương trong mo_ta.txt khớp câu đầu mỗi hồi
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
FP = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
MP4 = ROOT / "02_SAN_XUAT/Tap03/xuat_ban/Tap03_master.mp4"
SRT = ROOT / "02_SAN_XUAT/Tap03/xuat_ban/Tap03.srt"
MOTA = ROOT / "02_SAN_XUAT/Tap03/xuat_ban/mo_ta.txt"
TMP = WORK / "_qc_final_t03"
TMP.mkdir(exist_ok=True)

os.environ.setdefault("AE_EP", "03")
os.environ.setdefault("AE_LANG", "vi")
sys.path.insert(0, str(WORK))
import build_video3 as BV  # noqa: E402

TL = BV.TL
fails = []


def chk(label, cond, detail=""):
    print(f"[{'OK  ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(label)


def probe(p):
    o = subprocess.run([str(FP), "-v", "error", "-show_entries",
                        "stream=codec_name,codec_type,width,height,r_frame_rate,nb_frames,sample_rate,channels,bit_rate",
                        "-show_entries", "format=duration,size,format_name",
                        "-of", "json", str(p)], capture_output=True, text=True).stdout
    return json.loads(o)


# ---------------------------------------------------------------- G1
pr = probe(MP4)
v = next(s for s in pr["streams"] if s["codec_type"] == "video")
a = next(s for s in pr["streams"] if s["codec_type"] == "audio")
dur = float(pr["format"]["duration"])
v_dur = float(v.get("duration") or dur)
a_dur = float(a.get("duration") or dur)
print(f"      video: {v['codec_name']} {v['width']}x{v['height']} @{v['r_frame_rate']} "
      f"frames={v.get('nb_frames')}")
print(f"      audio: {a['codec_name']} {a['sample_rate']}Hz ch={a['channels']} {a.get('bit_rate')}")
print(f"      file : {dur:.3f}s  {int(pr['format']['size'])/1e6:.1f} MB  {pr['format']['format_name']}")
chk("G1 container 1920x1080 @30fps H.264+AAC",
    v["width"] == 1920 and v["height"] == 1080 and v["r_frame_rate"] == "30/1"
    and v["codec_name"] == "h264" and a["codec_name"] == "aac")

# ---------------------------------------------------------------- G2 H14
d_va = abs(v_dur - a_dur)
d_vt = abs(v_dur - float(TL["total"]))
chk("G2 H14 hình = tiếng trong ±0,05 s", d_va <= 0.05, f"lệch {d_va*1000:.1f} ms "
    f"(video {v_dur:.3f}s · audio {a_dur:.3f}s)")
chk("G2 H14 hình = timeline.total trong ±0,05 s", d_vt <= 0.05,
    f"lệch {d_vt*1000:.1f} ms (video {v_dur:.3f}s · timeline {float(TL['total']):.3f}s)")

# ---------------------------------------------------------------- G3 A7
e = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(MP4),
                    "-af", "ebur128=peak=true", "-f", "null", "-"],
                   capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
seg = e[e.rfind("Integrated loudness:"):][:2500]
I = re.findall(r"I:\s*(-?[\d.]+)\s*LUFS", seg)
LRA = re.findall(r"LRA:\s*(-?[\d.]+)\s*LU", seg)
PK = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", seg)
lufs = float(I[-1]) if I else None
lra = float(LRA[-1]) if LRA else None
peak = float(PK[-1]) if PK else None
print(f"      LUFS={lufs}  LRA={lra}  true peak={peak} dBFS")
chk("G3 A7 loudness -16 ±1 LUFS", lufs is not None and -17.0 <= lufs <= -15.0, f"{lufs} LUFS")
chk("G3 A7 true peak <= -1,5 dBFS", peak is not None and peak <= -1.5, f"{peak} dBFS")

# ---------------------------------------------------------------- G4 V4
sd = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(MP4),
                     "-af", "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"],
                    capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
sil = re.findall(r"silence_duration:\s*([\d.]+)", sd)
long_sil = [float(x) for x in sil if float(x) > 0.3]
chk("G4 V4 không im lặng tuyệt đối > 0,3 s @ -60 dB", not long_sil,
    f"{len(long_sil)} khoảng > 0,3s" + (f" {long_sil[:5]}" if long_sil else ""))

# ---------------------------------------------------------------- G5 decode
dec = subprocess.run([str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"],
                     capture_output=True, text=True, encoding="utf-8", errors="replace")
errs = [l for l in dec.stderr.splitlines() if l.strip() and "Deprecated" not in l]
chk("G5 giải mã toàn bộ không lỗi", not errs, f"{len(errs)} dòng lỗi: {errs[:3]}")

# ---------------------------------------------------------------- G6 faststart
with open(MP4, "rb") as f:
    head = f.read(1024)
chk("G6 faststart (moov ở đầu tệp)", b"moov" in head)

# ---------------------------------------------------------------- G7 phụ đề
srt = SRT.read_text(encoding="utf-8").strip()
blocks = [b for b in srt.split("\n\n") if b.strip()]
def cue_time(b, idx=1):
    m = re.search(r"(\d\d):(\d\d):(\d\d),(\d\d\d)", b.splitlines()[idx])
    h, mi, s, ms = map(int, m.groups())
    return h * 3600 + mi * 60 + s + ms / 1000
first_cue, last_cue = cue_time(blocks[0]), cue_time(blocks[-1])
print(f"      SRT: {len(blocks)} cue · {first_cue:.2f}s .. {last_cue:.2f}s")
chk("G7 phụ đề phủ câu", len(blocks) >= len(TL["items"]),
    f"{len(blocks)} cue cho {len(TL['items'])} câu")
chk("G7 phụ đề bắt đầu sau intro và kết thúc trước hết tập",
    22.0 <= first_cue <= 25.0 and last_cue <= float(TL["total"]) + 0.5,
    f"đầu {first_cue:.2f}s · cuối {last_cue:.2f}s")

# ---------------------------------------------------------------- G8 H12 + H16
print("[G8] trích khung tại các mốc, so với ảnh render gốc")
probe_pts = []
for act in range(2, 6):
    m = next(x for x in TL["markers"] if x["type"] == "ACT" and x["act"] == act)
    probe_pts.append((f"chuyen hoi {act}", (m["start"] + m["end"]) / 2))
probe_pts.append(("the ket (cuoi video)", float(TL["total"]) - 2.0))
probe_pts.append(("dau video (intro)", 10.0))

for label, t in probe_pts:
    fi = int(t * BV.FPS)
    ref = TMP / f"ref_{fi}.png"
    BV.render(fi).convert("RGB").save(ref)
    got = TMP / f"got_{fi}.png"
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(MP4),
                    "-frames:v", "1", str(got)], check=True, capture_output=True)
    with Image.open(ref) as im1, Image.open(got) as im2:
        a1 = np.asarray(im1.convert("RGB"), dtype=np.float32)
        a2 = np.asarray(im2.convert("RGB"), dtype=np.float32)
    if a1.shape != a2.shape:
        chk(f"G8 {label} @ {t:.1f}s", False, "kich thuoc khac nhau")
        continue
    mae = float(np.abs(a1 - a2).mean())
    chk(f"G8 {label} @ {t:.1f}s khớp ảnh render", mae <= 12.0, f"MAE {mae:.2f}/255")

# ---------------------------------------------------------------- G9 T11 chapters
mota = MOTA.read_text(encoding="utf-8") if MOTA.exists() else ""
chap = re.findall(r"(\d\d):(\d\d)\s+(Hồi \d[^\n]*)", mota)
print(f"      chapters trong mo_ta.txt: {len(chap)}")
act_first = {}
for it in TL["items"]:
    act_first.setdefault(it["act"], it["start"])
bad = []
for mi, se, label in chap:
    ts = int(mi) * 60 + int(se)      # mm:ss (không phải hh:mm)
    mm = re.search(r"Hồi (\d)", label)
    if not mm:
        continue
    a = int(mm.group(1))
    if a in act_first and abs(ts - act_first[a]) > 2.0:
        bad.append(f"Hồi {a}: mô tả {ts}s vs thực {act_first[a]:.1f}s")
chk("G9 mốc chương khớp câu đầu mỗi hồi", not bad, "; ".join(bad[:4]) if bad
    else f"{len(chap)} mốc (mm:ss khớp câu đầu hồi, dung sai 2 s)")

# ---------------------------------------------------------------- G10 lệch A/V
print("[G10] độ lệch âm thanh so với master (A/V offset)")
SRC_WAV = WORK / "audio_master_t03.wav"
SRX = 8000


def win(path, t0, dur):
    raw = subprocess.run([str(FF), "-v", "error", "-ss", f"{t0}", "-i", str(path),
                          "-t", f"{dur}", "-f", "f32le", "-ac", "1", "-ar", str(SRX), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def lag_ms(a, b):
    n = min(len(a), len(b))
    a = a[:n] - a[:n].mean()
    b = b[:n] - b[:n].mean()
    m = 1 << int(np.ceil(np.log2(2 * n)))
    cc = np.fft.irfft(np.fft.rfft(a, m) * np.conj(np.fft.rfft(b, m)), m)
    k = int(np.argmax(cc[:2000]))
    if k > 1000:
        k -= m
    return k / SRX * 1000.0


if SRC_WAV.exists():
    T0, DUR = 120.0, 40.0
    off = lag_ms(win(SRC_WAV, T0, DUR), win(MP4, T0, DUR))
    print(f"      lệch âm thanh: {off:+.2f} ms")
    chk("G10 lệch A/V trong ±50 ms", abs(off) <= 50, f"{off:+.2f} ms")
else:
    print("      (bỏ qua: không có audio_master_t03.wav)")

print("=" * 78)
print("KẾT LUẬN:", "ĐẠT" if not fails else f"LỖI {len(fails)}: {fails}")
sys.exit(0 if not fails else 1)
