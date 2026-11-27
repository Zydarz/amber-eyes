#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra noi dung master mp3 moi cua EN TK2 (khong dung file wav cu).

Giải mã mp3 bang ffmpeg -> numpy -> faster-whisper -> can Needleman-Wunsch
voi 11 cau trong SPEC_AUDIO_CLIP_TAP04.json.
"""
import difflib
import json
import pathlib
import re
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")
FF = sorted(str(p) for p in (ROOT / ".work" / "ffmpeg").glob("*/bin/ffmpeg.exe"))[0]
SPEC = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN" / "SPEC_AUDIO_CLIP_TAP04.json"
PUNCT = re.compile(r"[^\w\s]", re.UNICODE)


def decode(path, sr=16000):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                           "-f", "s16le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0


def norm(t):
    return [w for w in PUNCT.sub(" ", t.lower()).split() if w]


def expand(word_text, s, e):
    toks = norm(word_text)
    if not toks:
        return []
    step = (e - s) / len(toks)
    return [(t, s + i * step, s + (i + 1) * step) for i, t in enumerate(toks)]


def align(spec_tokens, asr_tokens, gap=-0.35, min_sim=0.45):
    n, m = len(spec_tokens), len(asr_tokens)
    rat = {}
    for i, a in enumerate(spec_tokens):
        for j, (b, _, _) in enumerate(asr_tokens):
            if not b:
                continue
            rat[(i, j)] = 1.0 if a == b else difflib.SequenceMatcher(None, a, b).ratio()
    NEG = -1e9
    sc = np.full((n + 1, m + 1), NEG, dtype=np.float32)
    bt = np.zeros((n + 1, m + 1), dtype=np.int8)
    sc[0, 0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            best, op = NEG, 0
            if i > 0 and j > 0 and sc[i - 1, j - 1] > NEG:
                v = sc[i - 1, j - 1] + rat.get((i - 1, j - 1), 0.0)
                if v > best:
                    best, op = v, 1
            if i > 0 and sc[i - 1, j] > NEG:
                v = sc[i - 1, j] + gap
                if v > best:
                    best, op = v, 2
            if j > 0 and sc[i, j - 1] > NEG:
                v = sc[i, j - 1] + gap
                if v > best:
                    best, op = v, 3
            sc[i, j] = best
            bt[i, j] = op
    i, j = n, m
    mapping = {}
    while i > 0 or j > 0:
        op = bt[i, j]
        if op == 1 and i > 0 and j > 0:
            if rat.get((i - 1, j - 1), 0.0) >= min_sim:
                mapping[i - 1] = j - 1
            i -= 1
            j -= 1
        elif op == 2 and i > 0:
            i -= 1
        elif op == 3 and j > 0:
            j -= 1
        else:
            break
    return mapping


def main():
    src = pathlib.Path(sys.argv[1])
    spec = json.loads(SPEC.read_text(encoding="utf-8-sig"))
    lines = spec["clips"]["TK2"]["lines"]
    audio = decode(src)
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, info = m.transcribe(audio, language="en", beam_size=5, vad_filter=False,
                              condition_on_previous_text=False, word_timestamps=True)
    words = []
    for s in segs:
        for w in (s.words or []):
            if w.start is None:
                continue
            words.append((w.word.strip(), float(w.start), float(w.end)))
    asr_tokens = []
    for w, s, e in words:
        asr_tokens.extend(expand(w, s, e))
    spec_tokens, owner = [], []
    for li, l in enumerate(lines):
        for t in norm(l["text"]):
            spec_tokens.append(t)
            owner.append(li)
    mapping = align(spec_tokens, asr_tokens)
    per = {li: [] for li in range(len(lines))}
    for si, aj in mapping.items():
        per[owner[si]].append(aj)
    print(f"Nguon: {src.name}  ({len(audio)/16000:.2f}s)")
    print(f"cau trong spec: {len(lines)} | asr tokens: {len(asr_tokens)}\n")
    bad = 0
    for li, l in enumerate(lines):
        idxs = sorted(per[li])
        matched = sum(1 for si, aj in mapping.items() if owner[si] == li)
        toks = norm(l["text"])
        ratio = matched / max(1, len(toks))
        if idxs:
            st, en = asr_tokens[idxs[0]][1], asr_tokens[idxs[-1]][2]
        else:
            st = en = None
        flag = ""
        if st is None:
            flag = "  <<< THIEU"
            bad += 1
        elif ratio < 0.6:
            flag = "  <<< MATCH YEU"
        print(f"  {l['clip_line_id']:<12} {'' if st is None else '%6.2f-%6.2f' % (st, en)} "
              f"match={matched}/{len(toks)} ({ratio:.0%}) {flag}")
    print(f"\nCAU THIEU: {bad}")
    print("\n--- ASR tail (8s cuoi) ---")
    for w, s, e in words[-14:]:
        print(f"  {s:6.2f}-{e:6.2f} {w}")


if __name__ == "__main__":
    main()
