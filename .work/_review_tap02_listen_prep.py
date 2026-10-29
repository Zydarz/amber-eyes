# -*- coding: utf-8 -*-
"""Chuẩn bị bài kiểm tra NGHE MÙ cho Tập 02 — cắt từ chính mp4 thành phẩm.

Tạo:
  role_H.mp3  = 12 câu của vai Host, rải đều trong tập (nghe liền)
  role_D.mp3  = 12 câu của Điều tra viên
  role_C.mp3  = 12 câu của Chuyên gia
  role_HDC.mp3= 9 câu H + 9 câu D + 9 câu C xen kẽ (kiểm tách bạch)
  role_N12.mp3= 4 câu N1 + 3 câu N2
"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
VID = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp4"
OUT = WORK / "_review_tap02_listen"
OUT.mkdir(parents=True, exist_ok=True)

tl = json.loads((WORK / "timeline_s_t02.json").read_text(encoding="utf-8"))
items = tl["items"]


def pick(role, n):
    """Chọn n câu rải đều trong tập cho vai role, loại câu quá ngắn (<1,2 s)."""
    cands = [it for it in items if it["role"] == role and (it["end"] - it["start"]) >= 1.2]
    if not cands:
        return []
    if len(cands) <= n:
        return cands
    step = len(cands) / n
    return [cands[int(i * step)] for i in range(n)]


def cut_and_concat(chosen, out_name, gap=0.7):
    seg_dir = OUT / (out_name + "_seg")
    seg_dir.mkdir(exist_ok=True)
    files = []
    for i, it in enumerate(chosen):
        dur = it["end"] - it["start"]
        p = seg_dir / f"{i:02d}_{it['id'].replace('#', '_').replace('.', '_')}.wav"
        if not p.exists():
            subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{it['start']:.3f}",
                            "-t", f"{dur:.3f}", "-i", str(VID), "-vn",
                            "-af", f"aformat=sample_fmts=s16:channel_layouts=stereo,aresample=48000",
                            str(p)], check=True)
        files.append(p)
    lst = seg_dir / "list.txt"
    lst.write_text("".join(f"file '{f.as_posix()}'\n" for f in files), encoding="utf-8")
    final = OUT / f"{out_name}.mp3"
    # chen 0,7 s im giữa cac doan
    filt = "".join(
        (f"[{i}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[a{i}];"
         for i in range(len(files))))
    chain = "".join(f"[a{i}]" for i in range(len(files)))
    parts = []
    for i in range(len(files)):
        if i:
            parts.append(f"[a{i}]apad=pad_dur={gap}[ap{i}]")
    lab = "".join(f"[ap{i}]" if i else f"[a{i}]" for i in range(len(files)))
    # don gian hon: dung concat demuxer + silence giua bang adelay
    args = [str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst)]
    # them khoang im giua cac doan: tach file va ghep voi silence rieng
    sil = OUT / "_silence.wav"
    if not sil.exists():
        subprocess.run([str(FF), "-y", "-v", "error", "-f", "lavfi",
                        "-i", f"anullsrc=r=48000:cl=stereo:d={gap}", str(sil)], check=True)
    seq = []
    for i, f in enumerate(files):
        seq.append(f)
        if i != len(files) - 1:
            seq.append(sil)
    lst2 = seg_dir / "list2.txt"
    lst2.write_text("".join(f"file '{f.as_posix()}'\n" for f in seq), encoding="utf-8")
    subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst2),
                    "-c:a", "libmp3lame", "-b:a", "128k", str(final)], check=True)
    return final, chosen


def report(name, final, chosen):
    meta = [{"id": c["id"], "role": c["role"], "start": c["start"], "end": c["end"],
             "text": c["text"][:70]} for c in chosen]
    (OUT / f"{name}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2),
                                      encoding="utf-8")
    print(f"{name}: {final.name}  ({len(chosen)} doan)")


jobs = []
jobs.append(("role_H", pick("H", 12)))
jobs.append(("role_D", pick("D", 12)))
jobs.append(("role_C", pick("C", 12)))

# xen ke 3 vai: lay 9 cau cua moi vai, xen theo thu tu thoi gian
h, d, c = pick("H", 9), pick("D", 9), pick("C", 9)
merged = sorted(h + d + c, key=lambda x: x["start"])
jobs.append(("role_HDC", merged))

n1, n2 = pick("N1", 4), pick("N2", 3)
jobs.append(("role_N12", sorted(n1 + n2, key=lambda x: x["start"])))

for name, chosen in jobs:
    if not chosen:
        print(f"{name}: KHONG CO CAU")
        continue
    final, ch = cut_and_concat(chosen, name)
    report(name, final, ch)
print("XONG")
