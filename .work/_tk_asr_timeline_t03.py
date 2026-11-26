#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung timeline_tkN.json cho Tap03 (VN/EN/JA) tu master WAV bang ASR + forced alignment.

Pipeline:
  master WAV -> faster-whisper small (word_timestamps) -> cache .work/_tk_asr_tk03_<clip>_<lang>.json
  spec lines  -> token (word cho EN/VN, KY TU cho JA) -> DP Needleman-Wunsch vs ASR tokens
  -> line start/end -> timeline_tkN.json (Tap03 / Tap03_EN / Tap03_JA)

Tieu chuan (L3):
- Moi dong spec phai match it nhat MOT token ASR.
- Moc thoi gian tang dan, khong chong nhau.
- Doan dau bat dau gan 0s; doan cuoi gan cuoi file.
- Bao cao coverage tung dong de biet dong nao khong chan.

Dung:  py -3 .work/_tk_asr_timeline_t03.py [--lang VN|EN|JA] [--write]
"""
import difflib
import json
import pathlib
import re
import sys
import wave

import numpy as np
from scipy.signal import resample_poly

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
LANGDIR = {"VN": "Tap03", "EN": "Tap03_EN", "JA": "Tap03_JA"}
LANG_CODE = {"VN": "vi", "EN": "en", "JA": "ja"}
MODE = {"VN": "word", "EN": "word", "JA": "char"}
CLIPS = ["TK1", "TK2", "TK3", "TK4", "TK5"]
MODEL = "small"
PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
JAPUNCT = re.compile(r"[^\w]", re.UNICODE)  # bo ca dau cau, gach noi trong JA


def norm(t, mode="word"):
    if mode == "char":
        return [c for c in JAPUNCT.sub("", t.lower()) if not c.isspace()]
    return [w for w in PUNCT.sub(" ", t.lower()).split() if w]


def load16k(path):
    w = wave.open(str(path), "rb")
    n, sr, ch = w.getnframes(), w.getframerate(), w.getnchannels()
    d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    if ch > 1:
        d = d.reshape(-1, ch).mean(axis=1)
    if sr != 16000:
        d = resample_poly(d, 16000, sr).astype(np.float32)
    return d


def run_asr(audio_path, cache_path, lang_code):
    if cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    from faster_whisper import WhisperModel
    m = WhisperModel(MODEL, device="cpu", compute_type="int8")
    audio = load16k(audio_path)
    segs, info = m.transcribe(audio, language=lang_code, beam_size=5, vad_filter=False,
                              word_timestamps=True, condition_on_previous_text=False)
    segs = list(segs)
    words = []
    for s in segs:
        for w in (s.words or []):
            if w.start is None:
                continue
            words.append({"w": w.word.strip(), "s": round(float(w.start), 3), "e": round(float(w.end), 3)})
    data = {"duration": float(info.duration), "words": words,
            "segments": [{"s": round(float(s.start), 3), "e": round(float(s.end), 3), "t": s.text.strip()}
                         for s in segs]}
    cache_path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return data


def expand_word(word_text, s, e, mode):
    """ tach 1 tu ASR thanh nhieu token (word -> chuoi tu; char -> tung ky tu) va noi thoi gian."""
    toks = norm(word_text, mode)
    if not toks:
        return []
    step = (e - s) / len(toks)
    return [(t, s + i * step, s + (i + 1) * step) for i, t in enumerate(toks)]


def align(spec_tokens, asr_tokens, gap=-0.35, min_sim=0.45):
    """Needleman-Wunsch: spec token (theo thu tu) vs ASR token. Tra mapping spec_idx -> asr_idx."""
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


def build_timeline(lang, cid, write=False):
    mode = MODE[lang]
    d = ROOT / "02_SAN_XUAT" / "TIKTOK" / LANGDIR[lang]
    spec = json.loads((d / "SPEC_AUDIO_CLIP_TAP03.json").read_text(encoding="utf-8-sig"))
    lines = spec["clips"][cid]["lines"]
    cache = WORK / f"_tk_asr_tk03_{cid}_{lang}.json"
    asr = run_asr(d / f"{cid}_master_audio.wav", cache, LANG_CODE[lang])
    words = asr["words"]
    total = asr["duration"]

    spec_tokens, owner = [], []
    for li, l in enumerate(lines):
        for t in norm(l["text"], mode):
            spec_tokens.append(t)
            owner.append(li)
    asr_tokens = []
    for w in words:
        asr_tokens.extend(expand_word(w["w"], w["s"], w["e"], mode))
    mapping = align(spec_tokens, asr_tokens)

    per_line = {li: [] for li in range(len(lines))}
    for si, aj in mapping.items():
        per_line[owner[si]].append(aj)

    rows = []
    for li, l in enumerate(lines):
        toks = norm(l["text"], mode)
        idxs = sorted(per_line[li])
        matched = sum(1 for si, aj in mapping.items() if owner[si] == li)
        ratio = matched / max(1, len(toks))
        if idxs:
            start = asr_tokens[idxs[0]][1]
            end = asr_tokens[idxs[-1]][2]
        else:
            start = end = None
        rows.append({"li": li, "line": l, "start": start, "end": end,
                     "ratio": ratio, "nmatch": matched, "ntok": len(toks)})

    known = [r for r in rows if r["start"] is not None]
    for r in rows:
        if r["start"] is not None:
            continue
        before = [k for k in known if k["li"] < r["li"]]
        after = [k for k in known if k["li"] > r["li"]]
        if before and after:
            b, a = before[-1], after[0]
            frac = (r["li"] - b["li"]) / (a["li"] - b["li"])
            r["start"] = b["end"] + frac * (a["start"] - b["end"])
            r["end"] = r["start"]
            r["interp"] = True
        elif before:
            r["start"] = r["end"] = before[-1]["end"]
            r["interp"] = True
        elif after:
            r["start"] = r["end"] = after[0]["start"]
            r["interp"] = True

    prev_end = 0.0
    for r in rows:
        if r["start"] is None:
            r["start"] = r["end"] = prev_end
        r["start"] = round(max(r["start"], prev_end), 3)
        r["end"] = round(max(r["end"], r["start"]), 3)
        prev_end = r["end"]

    print(f"\n=== {lang} {cid}  mode={mode}  dur={total:.2f}s  lines={len(lines)}  "
          f"asr_tokens={len(asr_tokens)}")
    est_sum = sum(l["est_dur_s"] for l in lines)
    meas_sum = sum(r["end"] - r["start"] for r in rows)
    print(f"    measured speech={meas_sum:.2f}s   spec est={est_sum:.2f}s")
    bad = 0
    for r in rows:
        l = r["line"]
        flag = ""
        if r.get("interp"):
            flag = " [NOI SUY]"
            bad += 1
        elif r["ratio"] < 0.6:
            flag = " [MATCH YEU]"
            bad += 1
        print(f"    {l['clip_line_id']:<12} {r['start']:6.2f}-{r['end']:6.2f} "
              f"({r['end'] - r['start']:5.2f}s est={l['est_dur_s']:5.2f}s) "
              f"match={r['nmatch']}/{r['ntok']} bg={l['bg']}{flag}")
    if write:
        tl = []
        for r in rows:
            l = r["line"]
            tl.append({"id": l["clip_line_id"], "vai": l.get("role", "H"),
                       "start": r["start"], "end": r["end"],
                       "pause": round(l.get("pause_after_s", 0.5), 3),
                       "text": l["text"], "bg": l["bg"],
                       "motion": l.get("motion", "still"),
                       "match_ratio": round(r["ratio"], 3),
                       "interp": bool(r.get("interp", False))})
        (d / f"timeline_{cid.lower()}.json").write_text(
            json.dumps(tl, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"    -> wrote {d / f'timeline_{cid.lower()}.json'}  (canh bao {bad} dong)")
    return bad


def main():
    args = sys.argv[1:]
    lang = "VN"
    if "--lang" in args:
        lang = args[args.index("--lang") + 1].upper()
    write = "--write" in args
    total_bad = 0
    for cid in CLIPS:
        total_bad += build_timeline(lang, cid, write=write)
    print(f"\nTONG DONG CO VAN DE: {total_bad}")


if __name__ == "__main__":
    main()
