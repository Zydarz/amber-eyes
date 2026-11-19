#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xac nhan lai CER (G12) cho TK1: 2 lượt ASR doc lap (A4.1b yeu cau >= 2 luot
truoc khi ket luan ve 1 cau).

Luot 1: faster-whisper small (da chay, xem _qc_tk1_cer_rows.json)
Luot 2: faster-whisper small lan 2 (beam 5, co seed khac via temperature)
Luot 3: faster-whisper base (model khac hoan toan)
Chay tren 12 cau, in ca 3 luot de so sanh.
"""
import json
import pathlib
import subprocess
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = ROOT / ".work"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

import vi_cer  # noqa: E402
from faster_whisper import WhisperModel  # noqa: E402

FF = HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"
WAV = D / "TK1_master_audio.wav"
TL = D / "timeline_tk1.json"
OUT = HERE / "_qc_tk1_cer_multiround.json"
TMP = HERE / "_tk1_seg"
THRESH = 0.02


def cut(start, dur, dst):
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", "%.3f" % start, "-t", "%.3f" % dur,
                    "-i", str(WAV), "-ac", "1", "-ar", "16000", "-f", "wav", str(dst)],
                   check=True, capture_output=True)


def read_16k(p):
    with wave.open(str(p), "rb") as wf:
        sr = wf.getframerate()
        ch = wf.getnchannels()
        raw = wf.readframes(wf.getnframes())
    assert sr == 16000
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    return x


def main():
    TMP.mkdir(parents=True, exist_ok=True)
    tl = json.loads(TL.read_text(encoding="utf-8-sig"))
    segs = []
    for l in tl:
        p = TMP / ("%s.wav" % l["id"].replace(".", "_").replace("#", "_"))
        cut(l["start"], l["end"] - l["start"], p)
        segs.append((l, read_16k(p)))

    rounds = []
    for mname, temp in [("small", 0.0), ("small", 0.4), ("base", 0.0)]:
        model = WhisperModel(mname, device="cpu", compute_type="int8", cpu_threads=4)
        rows = []
        for l, audio in segs:
            out, _ = model.transcribe(audio, language="vi", beam_size=5,
                                      temperature=temp, vad_filter=False,
                                      condition_on_previous_text=False)
            hyp = " ".join(s.text.strip() for s in out).strip()
            c = vi_cer.cer_pair(l["text"], hyp)
            rows.append({"id": l["id"], "vai": l["vai"], "cer": c, "hyp": hyp})
        rounds.append({"model": mname, "temperature": temp, "rows": rows})
        print("\n=== LUOT %s (temp=%.1f) ===" % (mname, temp), flush=True)
        for r in rows:
            print("  %-11s CER=%6.2f%%  %s" % (r["id"], r["cer"] * 100, r["hyp"][:100]), flush=True)

    # tong hop
    ids = [l["id"] for l in tl]
    print("\n=== TONG HOP 3 LUOT ===")
    print("  %-11s %-4s %8s %8s %8s   %s" % ("cau", "vai", "L1", "L2", "L3", "chenh"))
    summary = []
    for i, sid in enumerate(ids):
        vals = [rd["rows"][i]["cer"] for rd in rounds]
        mean = float(np.mean(vals))
        maxv = max(vals)
        summary.append({"id": sid, "vai": tl[i]["vai"], "cers": vals, "mean": mean, "max": maxv})
        print("  %-11s %-4s %7.2f%% %7.2f%% %7.2f%%   %s"
              % (sid, tl[i]["vai"], vals[0] * 100, vals[1] * 100, vals[2] * 100,
                 "CHAC" if (maxv - min(vals)) < 0.03 else "LECH"))
    means = [s["mean"] for s in summary]
    stable_fail = [s for s in summary if s["max"] >= THRESH]
    print("\n  TB (3 luot): %.2f%% · trung viet %.2f%%" % (100 * float(np.mean(means)),
                                                           100 * float(np.median(means))))
    print("  Cau trung binh >= 2%% (ca 3 luot deu vuot): %d / %d"
          % (len(stable_fail), len(ids)))
    for s in stable_fail:
        print("   ! %s  trung binh %.2f%%" % (s["id"], s["mean"] * 100))

    OUT.write_text(json.dumps({"rounds": rounds, "summary": summary,
                               "mean": float(np.mean(means)),
                               "median": float(np.median(means)),
                               "n_stable_fail": len(stable_fail), "n": len(ids)},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n  -> %s" % OUT)


if __name__ == "__main__":
    main()
