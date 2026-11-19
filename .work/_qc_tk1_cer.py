#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC CER (G12) cho audio TK1 — dung cach DUNG cho faster-whisper.

BAI HAY CU:
- faster-whisper 1.2.1 KHONG co tham so `sampling_rate`; khi truyen mang numpy,
  no GIA DINH audio da la 16 kHz. Truyen mang 48 kHz => tieng bi chay cham 3 lan,
  cao do hạ, ASR ra văn bảu rác -> CER 70-100% gia (SAI).
- DUNG: cat tung cau ra file WAV 16 kHz mono roi truyen DUONG DAN file.
"""
import json
import pathlib
import subprocess
import sys

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
OUT = HERE / "_qc_tk1_cer_rows.json"
TMP = HERE / "_tk1_seg"
MODEL = "small"
THRESH = 0.02


def cut(src, start, dur, dst):
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", "%.3f" % start, "-t", "%.3f" % dur,
                    "-i", str(src), "-ac", "1", "-ar", "16000", "-f", "wav", str(dst)],
                   check=True, capture_output=True)


def read_16k(p):
    """Doc file WAV 16 kHz mono -> mang float32 (faster-whisper gia dinh 16 kHz)."""
    import wave
    import numpy as np
    with wave.open(str(p), "rb") as wf:
        sr = wf.getframerate()
        ch = wf.getnchannels()
        raw = wf.readframes(wf.getnframes())
    assert sr == 16000, "can 16 kHz, nhan %d" % sr
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    return x


def main():
    TMP.mkdir(parents=True, exist_ok=True)
    tl = json.loads(TL.read_text(encoding="utf-8-sig"))
    model = WhisperModel(MODEL, device="cpu", compute_type="int8", cpu_threads=4)
    print("model loaded: %s" % MODEL, flush=True)

    rows = []
    all_ref, all_hyp = [], []
    for l in tl:
        seg_wav = TMP / ("%s.wav" % l["id"].replace(".", "_").replace("#", "_"))
        cut(WAV, l["start"], l["end"] - l["start"], seg_wav)
        segs, info = model.transcribe(read_16k(seg_wav), language="vi", beam_size=5,
                                       vad_filter=False, condition_on_previous_text=False)
        hyp = " ".join(s.text.strip() for s in segs).strip()
        c = vi_cer.cer_pair(l["text"], hyp)
        c_nn = vi_cer.cer_pair_nonum(l["text"], hyp)
        c_pr = vi_cer.cer_pair_prop(l["text"], hyp)
        rows.append({"id": l["id"], "vai": l["vai"], "ref": l["text"], "hyp": hyp,
                     "cer": c, "cer_nonum": c_nn, "cer_prop": c_pr,
                     "dur": round(l["end"] - l["start"], 2),
                     "lang_detect": info.language, "lang_p": round(info.language_probability, 3)})
        all_ref.append(l["text"])
        all_hyp.append(hyp)
        flag = "DAT" if c < THRESH else "TRUOT"
        print("  %-11s %-3s CER=%6.2f%% (nonum %5.2f%% / prop %5.2f%%) %s"
              % (l["id"], l["vai"], c * 100, c_nn * 100, c_pr * 100, flag), flush=True)
        print("       hyp: %s" % hyp[:130], flush=True)

    ref_all = " ".join(all_ref)
    hyp_all = " ".join(all_hyp)
    c_all = vi_cer.cer_pair(ref_all, hyp_all)
    c_all_nn = vi_cer.cer_pair_nonum(ref_all, hyp_all)
    c_all_pr = vi_cer.cer_pair_prop(ref_all, hyp_all)
    cs = [r["cer"] for r in rows]
    over = [r for r in rows if r["cer"] >= THRESH]
    import numpy as np
    print("\n  TB %.2f%% · trung viet %.2f%% · ca clip %.2f%% (nonum %.2f%% / prop %.2f%%)"
          % (100 * float(np.mean(cs)), 100 * float(np.median(cs)),
             c_all * 100, c_all_nn * 100, c_all_pr * 100))
    print("  So cau CER >= 2%%: %d / %d" % (len(over), len(rows)))
    for r in over:
        print("   ! %s" % r["id"])

    OUT.write_text(json.dumps({"model": MODEL, "method": "16k wav -> file path",
                               "rows": rows, "cer_all": c_all,
                               "cer_all_nonum": c_all_nn, "cer_all_prop": c_all_pr,
                               "mean": float(np.mean(cs)), "median": float(np.median(cs)),
                               "n_over": len(over), "n": len(rows)},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n  -> %s" % OUT)
    print("  KET LUAN G12: %s" % ("DAT (100%% mau < 2%%)" if not over
                                  else "CO %d CAU >= 2%%" % len(over)))


if __name__ == "__main__":
    main()
