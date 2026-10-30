"""Make one fixed Higgs reference clip per role from the episode's MiniMax sentences.

Picks neutral, base-speed sentences without digits / Latin words / pause tags, joins them
(0.25 s gap) to 8-15 s, 24 kHz mono WAV at -18 LUFS, plus the exact transcript.
Output: assets/voice_ref_higgs/<role>.wav + <role>.txt + refs.json   (QUY_TAC_AUDIO_HIGGS.md §4)
Usage:  AE_EP=02 py -3 .work/higgs_make_refs.py
"""
import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EP = os.environ.get("AE_EP", "02")
MAN = ROOT / ".work" / f"tts_manifest_t{EP}.json"
AUD = ROOT / ".work" / f"audio_s_t{EP}"
OUT = ROOT / "assets" / "voice_ref_higgs"
LO, HI, GAP = 8.0, 15.0, 0.25
BIN = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin"
FF, FP = str(BIN / "ffmpeg.exe"), str(BIN / "ffprobe.exe")
CER = {}  # sentence id -> measured CER of the MiniMax take (cer_bo_a_tapXX)
LATIN = re.compile(r"\b[a-zA-Z]+\b")


def dur(p):
    r = subprocess.run([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def clean(t):
    return re.sub(r"<#[\d.]+#>", "", t).strip()


def ok(it):
    t = clean(it["text"])
    return (it["emotion"] == "neutral" and "<#" not in it["text"] and not re.search(r"\d", it.get("display") or "")
            and "năm" not in t.split()[:2] and not [w for w in LATIN.findall(t) if not re.search(r"[^\x00-\x7f]", w) and len(w) > 1
                     and w.lower() not in VI_ASCII] and len(t.split()) >= 6)


# Vietnamese words written in plain ASCII (no diacritics) are allowed
VI_ASCII = set("anh ba ban bao bay bon cho chi con cung da dan di do du em gan gia giua hai hay hon khi khong la lam lan len lo luc ma mai minh mot muon nam nay neu nhung noi on qua ra roi sau sao se tai tam the theo thi thu tin toi tren trong va vao vi voi xa xin".split())


def main():
    items = json.loads(MAN.read_text(encoding="utf-8"))
    rows = ROOT / ".work" / f"cer_bo_a_tap{EP}" / "rows_fixed.json"
    CER.update({r["id"]: r["cer"] for r in json.loads(rows.read_text(encoding="utf-8"))} if rows.exists() else {})
    OUT.mkdir(parents=True, exist_ok=True)
    report = {}
    for role in sorted({it["role"] for it in items}):
        cand = [it for it in items if it["role"] == role and ok(it) and (AUD / it["file"]).exists()
                and CER.get(it["id"], 0) <= 0.02]  # never clone a mispronounced line
        cand.sort(key=lambda it: it["id"] not in CER)  # measured-clean lines first
        if not cand:  # small roles (N2) have no neutral line: take the calmest available
            cand = [it for it in items if it["role"] == role and (AUD / it["file"]).exists()]
        pick, tot = [], 0.0
        for it in cand:
            d = dur(AUD / it["file"])
            if tot + d + GAP > HI:
                continue
            pick.append(it)
            tot += d + GAP
            if tot >= LO:
                break
        if tot < LO:
            print(f"!! {role}: chỉ được {tot:.1f} s (< {LO} s)")
        lst = OUT / f"_{role}.txt"
        lst.write_text("".join(f"file '{(AUD / it['file']).as_posix()}'\n" for it in pick), encoding="utf-8")
        wav = OUT / f"{role}.wav"
        flt = (f"apad=pad_dur={GAP},aresample=24000:resampler=soxr,"
               "loudnorm=I=-18:TP=-1.5:LRA=11,silenceremove=start_periods=1:start_threshold=-50dB")
        subprocess.run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-af", flt, "-ac", "1", "-ar", "24000", "-c:a", "pcm_s16le", str(wav)], check=True)
        lst.unlink()
        text = " ".join(clean(it["text"]) for it in pick)
        (OUT / f"{role}.txt").write_text(text, encoding="utf-8")
        report[role] = {"voice_minimax": pick[0]["voice"], "episode": EP, "ids": [it["id"] for it in pick],
                        "seconds": round(dur(wav), 2), "text": text}
        print(f"{role}: {len(pick)} câu · {report[role]['seconds']} s · {pick[0]['voice']}")
    (OUT / "refs.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
