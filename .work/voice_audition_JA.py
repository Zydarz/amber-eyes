#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B0a (Japanese edition) — audition 2 Japanese voices per character for Tap01_JA.
Copy of voice_audition_EN.py adapted for Japanese language and Japanese voices.

Each candidate reads the character's own line from the JA script. Then:
  * listen_audio transcribes it  -> character error rate vs. the script (CER)
  * characters / second
  * median F0 (autocorrelation)
Output: 02_SAN_XUAT/Tap01_JA/thu_giong/report.md + so_sanh_giong_JA.mp3
"""
import json
import re
import subprocess
import sys
import unicodedata
import urllib.request
from pathlib import Path

import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "02_SAN_XUAT" / "Tap01_JA" / "thu_giong"
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
SCRIPT = json.loads((ROOT / ".work" / "script_tap01_JA.json").read_text(encoding="utf-8"))
SENT = {s["id"]: s["text"] for e in SCRIPT if e["kind"] == "LOI" for s in e["sentences"]}

CANDS = [  # role, voice_id, sentence, emotion, speed  (Japanese edition, 2 candidates per role)
    ("H", "Japanese_GentleButler", "2.04#2", "neutral", 0.95),
    ("H", "Japanese_IntellectualSenior", "2.04#2", "neutral", 0.95),
    ("D", "Japanese_SeriousCommander", "1.11#3", "neutral", 0.97),
    ("D", "Japanese_DominantMan", "1.11#3", "neutral", 0.97),
    ("C", "Japanese_DependableWoman", "3.08#2", "neutral", 0.95),
    ("C", "Japanese_CalmLady", "3.08#2", "neutral", 0.95),
    ("N1", "Japanese_KindLady", "1.07#1", "sad", 0.95),
    ("N1", "Japanese_GracefulMaiden", "1.07#1", "sad", 0.95),
    ("N2", "Japanese_OptimisticYouth", "4.03#1", "neutral", 0.95),
    ("N2", "Japanese_DecisivePrincess", "4.03#1", "neutral", 0.95),
]


def mcode(args, timeout=600):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[:500] or r.stdout[:500])
    return json.loads(r.stdout)


def tts_text(t):
    return t.replace("“", "").replace("”", "").replace('"', "").replace("「", "").replace("」", "")


def norm(t):
    t = unicodedata.normalize("NFKC", t)
    t = re.sub(r"[^\w]", "", t)
    return t.strip()


def cer(ref, hyp):
    a, b = norm(ref), norm(hyp)
    d = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(b) + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (a[i - 1] != b[j - 1]))
            prev = cur
    return d[-1] / max(1, len(a))


def pcm(path, sr=16000):
    r = subprocess.run([str(FF), "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr),
                        "-f", "s16le", "-"], capture_output=True)
    return np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768, sr


def f0_median(x, sr):
    win, hop, out = int(0.04 * sr), int(0.01 * sr), []
    for s in range(0, len(x) - win, hop):
        f = x[s:s + win]
        if np.sqrt((f ** 2).mean()) < 0.02:
            continue
        f = f - f.mean()
        ac = np.correlate(f, f, "full")[win - 1:]
        lo, hi = int(sr / 400), int(sr / 70)
        if lo >= hi or len(ac) <= hi:
            continue
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.3 * ac[0]:
            out.append(sr / k)
    return float(np.median(out)) if out else 0.0


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    reqs = [{"text": tts_text(SENT[s]), "voice_id": v, "emotion": e, "speed": sp,
             "pitch": 0, "volume": 1.0, "output_file": f"{i:02d}_{r}_{v}"}
            for i, (r, v, s, e, sp) in enumerate(CANDS)]
    (OUT / "args.json").write_text(json.dumps({"requests": reqs}, ensure_ascii=False), encoding="utf-8")
    if (OUT / "res.json").exists():                       # reuse audio already made
        res = json.loads((OUT / "res.json").read_text(encoding="utf-8"))
    else:
        print("Đang gửi yêu cầu TTS thử giọng...")
        res = mcode(["connector", "call", "connector__matrix__batch_text_to_audio",
                     "--args-file", str(OUT / "args.json")], 900)
        (OUT / "res.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    for f in res.get("failed_items", []):
        print("!! TTS failed", CANDS[f["index"]][1], f.get("error_msg"))
    rows, files = [], []
    for it in res.get("success_items", []):
        fn = it["file_name"]
        i = int(fn[:2])
        role, vid, sid, _, _ = CANDS[i]
        url = mcode(["get_asset_url", it["node_id"]], 120)["download_url"]
        local = OUT / fn
        if not local.exists():
            urllib.request.urlretrieve(url, local)
        files.append(local)
        x, sr = pcm(local)
        dur = len(x) / sr
        chars = len(norm(SENT[sid]))
        cached = OUT / f"asr_{i:02d}_res.json"
        try:
            if cached.exists():
                tr = json.loads(cached.read_text(encoding="utf-8"))
                hyp = tr.get("transcription", "") or tr.get("text", "")
                raise StopIteration
            af = OUT / f"asr_{i:02d}.json"
            af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg",
                                                     "prompt": "Transcribe verbatim in Japanese. Do not add or omit anything."}},
                                     ensure_ascii=False), encoding="utf-8")
            tr = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600)
            (OUT / f"asr_{i:02d}_res.json").write_text(json.dumps(tr, ensure_ascii=False), encoding="utf-8")
            hyp = tr.get("transcription") or tr.get("text") or ""
        except StopIteration:
            pass
        except Exception as e:  # noqa: BLE001
            hyp = f"(lỗi nhận dạng: {e})"
        c = cer(SENT[sid], hyp)
        rows.append((role, vid, dur, chars / dur, f0_median(x, sr), c, hyp))
    rows.sort(key=lambda r: (r[0], r[5]))
    md = ["# BÁO CÁO THỬ GIỌNG TIẾNG NHẬT — TẬP 01", "",
          "| Vai | voice_id | Thời lượng | Ký tự/s | F0 | CER | Nghe lại được |",
          "|---|---|---:|---:|---:|---:|---|"]
    for r in rows:
        md.append(f"| {r[0]} | `{r[1]}` | {r[2]:.1f} s | {r[3]:.2f} | {r[4]:.0f} Hz | {100 * r[5]:.1f}% | {r[6][:120]} |")
    (OUT / "report.md").write_text("\n".join(md), encoding="utf-8")
    lst = OUT / "list.txt"
    lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in sorted(files)), encoding="utf-8")
    subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c:a", "libmp3lame", "-b:a", "160k", str(OUT / "so_sanh_giong_JA.mp3")])
    print("\n".join(md))


if __name__ == "__main__":
    main()
