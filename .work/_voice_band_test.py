#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thử dải tốc độ cho một giọng EN — đo bằng chính model nghe (audios_understand).

Mục đích: G10 (A4.2) đòi "mỗi vai = 1 người". `English_Deep-VoicedGentleman` bị nghe
thành 3 người khi tốc độ đọc trải rộng (0,91 → 0,99). Thí nghiệm: đọc CÙNG một câu ở
nhiều tốc độ, ghép lại, hỏi model "mấy người?".

python .work/_voice_band_test.py English_Deep-VoicedGentleman
"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
sys.path.insert(0, str(W))
import tts_sentences as TS  # noqa: E402

VOICE = sys.argv[1] if len(sys.argv) > 1 else "English_Deep-VoicedGentleman"
TEXT = "The first stage: Voyeurism. He prowled quiet residential neighborhoods at night."
OUT = W / "voice_band_test"
OUT.mkdir(exist_ok=True)


def make(speed, emo, tag):
    af = OUT / f"args_{tag}.json"
    af.write_text(json.dumps({"requests": [{"text": TEXT, "voice_id": VOICE, "emotion": emo,
                                            "speed": speed, "pitch": 0, "volume": 1.0,
                                            "output_file": f"band_{tag}"}]}, ensure_ascii=False),
                  encoding="utf-8")
    res = TS.mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)], 600)
    it = res["success_items"][0]
    url = TS.mcode(["get_asset_url", it["node_id"]], 120)["download_url"]
    import urllib.request
    p = OUT / f"band_{tag}.mp3"
    urllib.request.urlretrieve(url, p)
    return p


def join(paths, out):
    args = [str(FF), "-y", "-v", "error"]
    for p in paths:
        args += ["-i", str(p)]
    n = len(paths)
    parts = "".join(f"[{i}:a]aresample=32000,aformat=channel_layouts=mono,apad=pad_dur=1.0[a{i}];" for i in range(n))
    parts += "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[o]"
    subprocess.run(args + ["-filter_complex", parts, "-map", "[o]", "-c:a", "libmp3lame", "-b:a", "128k", str(out)], check=True)


def ask(path, prompt):
    url = TS.mcode(["upload-temp-url", str(path)], 300)["temp_url"]
    af = OUT / "_q.json"
    af.write_text(json.dumps({"audio_info": [{"url": url, "mime_type": "audio/mpeg", "prompt": prompt}]},
                              ensure_ascii=False), encoding="utf-8")
    r = TS.mcode(["connector", "call", "connector__matrix__audios_understand", "--args-file", str(af)])
    return (r.get("results") or [{}])[0].get("description", json.dumps(r)[:400])


CASES = [
    ("wide", [(0.91, "neutral"), (0.93, "neutral"), (0.95, "neutral"), (0.97, "neutral"), (0.99, "neutral")]),
    ("mid", [(0.93, "neutral"), (0.95, "neutral"), (0.97, "neutral"), (0.99, "neutral")]),
    ("tight", [(0.95, "neutral"), (0.97, "neutral"), (0.99, "neutral")]),
    ("emo", [(0.95, "neutral"), (0.95, "sad"), (0.95, "fearful"), (0.95, "surprised")]),
]

for tag, combo in CASES:
    files = [make(s, e, f"{tag}_{i}") for i, (s, e) in enumerate(combo)]
    out = OUT / f"band_{tag}.mp3"
    join(files, out)
    ans = ask(out, f"This file has {len(combo)} English readings separated by ~1 s silence, "
                   "all supposedly by ONE narrator reading the SAME sentence. Ignore the words; judge only "
                   "VOICE IDENTITY (timbre, register, accent). First line exactly: 'SPEAKERS: <number>'. "
                   "Then say which readings sound like a different person and why (one line each).")
    print(f"=== {tag}: {combo}")
    print(ans)
    print()
