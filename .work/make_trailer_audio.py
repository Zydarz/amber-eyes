#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ÂM THANH + ĐÓNG GÓI trailer Concept A.

Dùng: py -3 .work/make_trailer_audio.py
Input : .work/trailer_a/vo/*.mp3 · assets/bgm/*.mp3 · assets/sfx/*.wav · picture.mp4
Output: .work/trailer_a/trailer_master.mp4

Chuẩn hoá (A7): loudnorm 2 lượt I=-16 TP=-1,5 LRA=11 → alimiter (latency=1) → AAC 192k.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work" / "trailer_a"
VO = WORK / "vo"
BGM = ROOT / "assets" / "bgm"
SFX = ROOT / "assets" / "sfx"
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFPROBE = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

DUR = 50.0
LANG = os.environ.get("AE_LANG", "vi").strip().lower()
SUF = "" if LANG == "vi" else "_" + LANG
VO_DIR = WORK / ("vo" if LANG == "vi" else "vo_" + LANG)


def run(cmd):
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit(f"ffmpeg failed:\n{r.stderr[-1500:]}")
    return r.stdout


def dur(p):
    return float(run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).strip())


def main():
    man = json.loads((WORK / "vo_manifest.json").read_text(encoding="utf-8"))
    items = [it for it in man["items"] if it.get("lang", "vi") == LANG]

    # ---- 1. các lớp
    cmd = [FF, "-y", "-v", "error"]
    for it in items:
        cmd += ["-i", str(VO_DIR / f"{it['id']}.mp3")]
    cmd += ["-stream_loop", "-1", "-i", str(BGM / "bgm_music_box.mp3")]
    cmd += ["-stream_loop", "-1", "-i", str(BGM / "bgm_sub_drone.mp3")]
    sfx_plan = [("folder_close.wav", 4.5, 0.30), ("card_flip.wav", 10.5, 0.22),
                ("card_flip.wav", 16.5, 0.22), ("card_flip.wav", 22.5, 0.22)]
    for fn, at, vol in sfx_plan:
        cmd += ["-i", str(SFX / fn)]
    n_items = len(items)
    i_box = n_items
    i_drone = n_items + 1
    i_sfx0 = n_items + 2

    chains = []
    for i, it in enumerate(items):
        chains.append(f"[{i}:a]adelay={int(it['at'] * 1000)}|{int(it['at'] * 1000)}[v{i}]")
    chains.append(f"[{i_box}:a]volume=0.20,afade=t=in:st=0:d=1.2,afade=t=out:st={DUR - 3}:d=3[box]")
    chains.append(f"[{i_drone}:a]volume=0.13,afade=t=in:st=0:d=3,afade=t=out:st={DUR - 5}:d=5[drone]")
    sfx_labels = []
    for k, (fn, at, vol) in enumerate(sfx_plan):
        lbl = f"s{k}"
        chains.append(f"[{i_sfx0 + k}:a]volume={vol},adelay={int(at * 1000)}|{int(at * 1000)},"
                      f"atrim=0:{min(1.6, dur(SFX / fn))}[{lbl}]")
        sfx_labels.append(f"[{lbl}]")
    # ---- 2. trộn: VO + nhạc + drone + SFX
    mix_in = "".join(f"[v{i}]" for i in range(n_items)) + "[box][drone]" + "".join(sfx_labels)
    chains.append(f"{mix_in}amix=inputs={n_items + 2 + len(sfx_plan)}:normalize=0:dropout_transition=0,"
                  f"atrim=0:{DUR},apad=pad_dur={DUR}[mix]")
    chains.append("[mix]alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1[lim]")
    cmd += ["-filter_complex", ";".join(chains), "-map", "[lim]",
            "-t", str(DUR), "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", str(WORK / f"mix_raw{SUF}.wav")]

    print("=== trộn thô ===", flush=True)
    run(cmd)

    # ---- 3. loudnorm 2 lượt (A7)
    print("=== loudnorm lượt 1 (đo) ===", flush=True)
    # loudnorm in JSON ra STDERR, không phải stdout
    r1 = subprocess.run([str(FF), "-i", str(WORK / f"mix_raw{SUF}.wav"), "-af",
                         "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                        capture_output=True, text=True, encoding="utf-8", errors="replace")
    blob = r1.stderr + r1.stdout
    j = blob[blob.rfind("{"):blob.rfind("}") + 1]
    m = json.loads(j)
    li = m["input_i"]
    tp = float(m["input_tp"])
    lra = float(m["input_lra"])
    thresh = float(m["input_thresh"])
    offset = float(m.get("target_offset", 0.0))
    print(f"  đo vào: I={li} LUFS · TP={tp} dBFS · LRA={lra} · thresh={thresh} · offset={offset}")

    print("=== loudnorm lượt 2 (áp dụng) ===", flush=True)
    run([FF, "-y", "-v", "error", "-i", str(WORK / f"mix_raw{SUF}.wav"), "-af",
         f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={li}:measured_TP={tp}:measured_LRA={lra}:"
         f"measured_thresh={thresh}:offset={offset}:linear=true:print_format=summary",
         "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", str(WORK / f"audio_master{SUF}.wav")])

    # ---- 4. đóng gói
    print("=== đóng gói ===", flush=True)
    run([FF, "-y", "-v", "error", "-i", str(WORK / f"picture{SUF}.mp4"), "-i", str(WORK / f"audio_master{SUF}.wav"),
         "-map", "0:v", "-map", "1:a", "-c:v", "copy",
         "-af", "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1",
         "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart",
         str(WORK / f"trailer_master{SUF}.mp4")])

    d = dur(WORK / f"trailer_master{SUF}.mp4")
    size = (WORK / f"trailer_master{SUF}.mp4").stat().st_size
    print(f"done -> {WORK / f'trailer_master{SUF}.mp4'}  {d:.2f}s  {size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
