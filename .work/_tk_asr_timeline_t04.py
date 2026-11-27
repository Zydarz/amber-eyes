#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ASR theo CUA SO (windowed) cho master audio Tap04 - cham duoi file >= 55 s.

Phat hien 27/11/2026 (EN TK2): faster-whisper transcribe ca file 72.34 s chi nhan
den 57.72 s (bo 14.64 s co loi o duoi). Transcribe tung cua so ngan 20.5 s (overlap
1.5 s) thi nhan DUOC tat ca. => dung windowed de sinh word timestamps.

Input : 02_SAN_XUAT/TIKTOK/<Tap04|Tap04_EN|Tap04_JA>/TK{n}_master_audio.mp3
        (uu tien .mp3 vi renderer cung doc .mp3; .wav chi de doi chieu)
Output: <dir>/timeline_tk{n}.json  +  .work/_tk_asr_tk04_<clip>_<lang>.json (cache)
"""
import difflib
import glob
import json
import pathlib
import re
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
WORK = ROOT / ".work"
LANGDIR = {"VN": "Tap04", "EN": "Tap04_EN", "JA": "Tap04_JA"}
LANG_CODE = {"VN": "vi", "EN": "en", "JA": "ja"}
MODE = {"VN": "word", "EN": "word", "JA": "char"}
CLIPS = ["TK1", "TK2", "TK3", "TK4", "TK5"]
MODEL = "small"
WIN_S, OVERLAP_S = 20.5, 4.0
PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
JAPUNCT = re.compile(r"[^\w]", re.UNICODE)


def norm(t, mode="word"):
    if mode == "char":
        return [c for c in JAPUNCT.sub("", t.lower()) if not c.isspace()]
    return [w for w in PUNCT.sub(" ", t.lower()).split() if w]


def decode_mp3(path, sr=16000):
    """Giai ma mp3 -> float32 mono 16 kHz. Dung f32le (s16le lam whisper bo duoi file)."""
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def dur_of(path):
    fp = FF.replace("ffmpeg.exe", "ffprobe.exe")
    try:
        return float(subprocess.check_output(
            [fp, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]
        ).decode().strip())
    except Exception:
        return None


def run_asr(audio, cache_path, lang_code, refresh=False):
    if cache_path.exists() and not refresh:
        return json.loads(cache_path.read_text(encoding="utf-8"))
    from faster_whisper import WhisperModel
    m = WhisperModel(MODEL, device="cpu", compute_type="int8")
    total = len(audio) / 16000.0
    words, segments = [], []
    step = WIN_S - OVERLAP_S
    starts = [0.0]
    while starts[-1] + step + WIN_S < total:
        starts.append(starts[-1] + step)
    # neo cua so cuoi vao cuoi file de bao dam phu duoi (whisper hay bo duoi khi doc file dai)
    last = max(0.0, total - WIN_S)
    if last - starts[-1] > 0.5:
        starts.append(last)
    for si, st in enumerate(starts):
        a = audio[int(st * 16000): int(min(st + WIN_S, total) * 16000)]
        if len(a) < 1600:
            continue
        segs, _ = m.transcribe(a, language=lang_code, beam_size=5, vad_filter=False,
                               condition_on_previous_text=False, word_timestamps=True)
        for s in segs:
            s0, e0 = st + float(s.start), st + float(s.end)
            segments.append({"s": round(s0, 3), "e": round(e0, 3), "t": s.text.strip()})
            for w in (s.words or []):
                if w.start is None:
                    continue
                words.append({"w": w.word.strip(),
                              "s": round(st + float(w.start), 3),
                              "e": round(st + float(w.end), 3)})
    # khu trung vong overlap: giu mot ban cho moi (text, moc thoi gian) cach nhau < 0.6 s
    words.sort(key=lambda x: x["s"])
    kept = []
    for w in words:
        dup = False
        for p in reversed(kept[-12:]):
            if w["s"] - p["s"] > 0.6:
                break
            if p["w"] == w["w"]:
                dup = True
                break
        if not dup:
            kept.append(w)
    words = kept
    words.sort(key=lambda x: x["s"])
    data = {"duration": total, "words": words, "segments": segments, "method": "windowed"}
    cache_path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return data


def expand_word(word_text, s, e, mode):
    toks = norm(word_text, mode)
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


def build_timeline(lang, cid, write=False, refresh=False):
    mode = MODE[lang]
    d = ROOT / "02_SAN_XUAT" / "TIKTOK" / LANGDIR[lang]
    spec = json.loads((d / "SPEC_AUDIO_CLIP_TAP04.json").read_text(encoding="utf-8-sig"))
    lines = spec["clips"][cid]["lines"]
    mp3 = d / f"{cid}_master_audio.mp3"
    wav = d / f"{cid}_master_audio.wav"
    dw, dm = dur_of(wav), dur_of(mp3)
    warn = ""
    if dw and dm and abs(dw - dm) > 0.05:
        warn = (f"  [CANH BAO] wav ({dw:.2f}s) <> mp3 ({dm:.2f}s) LECH PHIEN BAN "
                f"({dw - dm:+.2f}s) - dung mp3")
    audio = decode_mp3(mp3)
    cache = WORK / f"_tk_asr_tk04_{cid}_{lang}.json"
    asr = run_asr(audio, cache, LANG_CODE[lang], refresh=refresh)
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

    print(f"\n=== {lang} {cid}  mode={mode}  mp3={total:.2f}s  lines={len(lines)}  "
          f"asr_tokens={len(asr_tokens)}  asr_words={len(words)}")
    if warn:
        print(warn)
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
    print(f"    audio tail check: asr_end={max((w['e'] for w in words), default=0):.2f} / audio {total:.2f}s")
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
    refresh = "--refresh" in args
    clips = list(CLIPS)
    if "--clip" in args:
        i = args.index("--clip")
        clips = []
        for a in args[i + 1:]:
            if a.startswith("--"):
                break
            clips.append(a.upper())
    total_bad = 0
    for cid in clips:
        total_bad += build_timeline(lang, cid, write=write, refresh=refresh)
    print(f"\nTONG DONG CO VAN DE: {total_bad}")


if __name__ == "__main__":
    main()
