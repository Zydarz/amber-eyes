#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Experiment: how much pitch movement do emotion / pitch / pause tags add? (English edition)

Each test sentence is read in variants; we measure the F0 range (semitones, 5–95 %),
speech rate and check with ASR that no tag is read aloud.
Output: 02_SAN_XUAT/Tap01_EN/thu_giong/bieu_cam/report.md + so_sanh_bieu_cam.mp3
"""
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402
import tts_sentences as TS  # noqa: E402
from voice_audition import pcm, cer, FF  # noqa: E402

OUT = ED.EP_DIR / "thu_giong" / "bieu_cam"
CAST = ED.CAST
# (role, label, text, emotion, speed, pitch)
T = [
    ("H", "A neutral", "But when police entered that cold, silent house that night, they found the mother – Dee Dee Blanchard – dead in her bedroom.", "neutral", 0.95, 0),
    ("H", "B tags", "But when police entered that cold, silent house that night... <#0.4#> they found the mother – Dee Dee Blanchard – <#0.3#> dead in her bedroom.", "neutral", 0.95, 0),
    ("H", "C fearful+tags", "But when police entered that cold, silent house that night... <#0.4#> they found the mother – Dee Dee Blanchard – <#0.3#> dead in her bedroom.", "fearful", 0.93, 0),
    ("H", "D sad+tags", "But when police entered that cold, silent house that night... <#0.4#> they found the mother – Dee Dee Blanchard – <#0.3#> dead in her bedroom.", "sad", 0.92, -1),
    ("H", "A neutral", "And Gypsy Rose was gone.", "neutral", 0.95, 0),
    ("H", "C surprised", "And Gypsy Rose... <#0.3#> was gone.", "surprised", 0.92, 0),
    ("D", "A neutral", "And the person behind the plan that led to the death of that saintly mother... was none other than her own little girl.", "neutral", 0.99, 0),
    ("D", "C angry+tags", "And the person behind the plan that led to the death of that saintly mother... <#0.5#> was none other than her own little girl.", "angry", 0.95, -1),
    ("C", "A neutral", "How do you keep a human being by your side forever?", "neutral", 0.95, 0),
    ("C", "C surprised", "How do you keep a human being by your side... forever?", "surprised", 0.93, 1),
    ("N2", "A neutral", "So why, in all those years, in front of hundreds of doctors, police officers and crowds, did Gypsy never once stand up from that wheelchair and expose her mother?", "neutral", 0.95, 0),
    ("N2", "C surprised", "So why, in all those years, <#0.2#> in front of hundreds of doctors, police officers and crowds, <#0.2#> did Gypsy never once stand up from that wheelchair... and expose her mother?", "surprised", 0.97, 1),
    ("H", "A neutral", "Welcome to the criminal psychology case files.", "neutral", 0.95, 0),
    ("H", "C happy", "Welcome... <#0.3#> to the criminal psychology case files.", "happy", 0.95, 1),
]


def f0_track(x, sr):
    win, hop, out = int(0.04 * sr), int(0.01 * sr), []
    for s in range(0, len(x) - win, hop):
        f = x[s:s + win]
        if np.sqrt((f ** 2).mean()) < 0.02:
            continue
        f = f - f.mean()
        ac = np.correlate(f, f, "full")[win - 1:]
        lo, hi = int(sr / 400), int(sr / 65)
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.35 * ac[0]:
            out.append(sr / k)
    return np.array(out)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    reqs = [{"text": t, "voice_id": CAST[r][0], "emotion": e, "speed": sp, "pitch": pi, "volume": 1.0,
             "output_file": f"x{i:02d}"} for i, (r, lab, t, e, sp, pi) in enumerate(T)]
    files = {}
    for b in range(0, len(reqs), 10):
        af = OUT / f"args_{b // 10}.json"
        af.write_text(json.dumps({"requests": reqs[b:b + 10]}, ensure_ascii=False), encoding="utf-8")
        res = TS.mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)])
        for f in res.get("failed_items", []):
            print("!! failed", b + f["index"], f.get("error_msg"))
        for it in res.get("success_items", []):
            stem = it["file_name"].rsplit(".", 1)[0]
            url = TS.mcode(["get_asset_url", it["node_id"]], 120)["download_url"]
            local = OUT / (stem + ".mp3")
            urllib.request.urlretrieve(url, local)
            files[int(stem[1:])] = (local, url)
    md = ["| # | Vai | Biến thể | cảm xúc · tốc độ · cao độ | Dải cao độ (5–95 %) | Độ lệch | Thời lượng | ASR có đọc thẻ? |",
          "|---|---|---|---|---:|---:|---:|---|"]
    for i, (r, lab, t, e, sp, pi) in enumerate(T):
        if i not in files:
            continue
        local, url = files[i]
        x, sr = pcm(local)
        f0 = f0_track(x, sr)
        st = 12 * np.log2(f0 / np.median(f0))
        rng = np.percentile(st, 95) - np.percentile(st, 5)
        af = OUT / f"asr_{i:02d}.json"
        af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg",
                                                 "prompt": "Transcribe verbatim in English."}}), encoding="utf-8")
        hyp = TS.mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600).get("transcription", "")
        leak = "CÓ" if ("#" in hyp or "<" in hyp) else "không"
        md.append(f"| {i:02d} | {r} | {lab} | {e} · {sp} · {pi:+d} | {rng:.1f} st | {st.std():.2f} st | {len(x) / sr:.1f} s | {leak} — {hyp[:70]} |")
    (OUT / "report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    lst = OUT / "list.txt"
    lst.write_text("".join(f"file '{files[i][0].as_posix()}'\n" for i in sorted(files)), encoding="utf-8")
    subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-af", "apad=pad_dur=0.8", "-c:a", "libmp3lame", "-b:a", "160k", str(OUT / "so_sanh_bieu_cam.mp3")])
    print("\n".join(md))


if __name__ == "__main__":
    main()
