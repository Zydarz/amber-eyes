#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUET VAN DE AUDIO — 15 clip TikTok Tap 04 (VN/EN/JA).

Khong sua gi, chi do va bao cao:
  1. Do dai / LUFS / true peak tren master mp3
  2. Khoang cam > 0.3s (silencedetect -60dB) — vi tri + do dai
  3. Loi noi cuoi cung (ASR) vs do dai file  => duoi cam
  4. Cau bi THIEU (khong match ASR) / match yeu  (tu timeline_tkN.json)
  5. Loi nao dai hon 1.5s (suspicious)
"""
import glob
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
TIK = os.path.join(ROOT, "02_SAN_XUAT", "TIKTOK")
FF = glob.glob(os.path.join(ROOT, ".work", "ffmpeg", "*", "bin", "ffmpeg.exe"))[0]
FP = FF.replace("ffmpeg.exe", "ffprobe.exe")
LANGS = [("VN", "Tap04"), ("EN", "Tap04_EN"), ("JA", "Tap04_JA")]


def sh(args):
    return subprocess.run([str(a) for a in args], capture_output=True, text=True, errors="replace")


def probe(p):
    j = json.loads(sh([FP, "-v", "quiet", "-print_format", "json", "-show_format",
                       "-show_streams", p]).stdout)
    return float(j["format"]["duration"])


def lufs(p):
    r = sh([FF, "-hide_banner", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"])
    m = re.findall(r"I:\s*(-?[\d.]+)\s*LUFS", r.stderr)
    pk = re.findall(r"Peak:\s*(-?[\d.]+)", r.stderr)
    return (float(m[-1]) if m else None, float(pk[-1]) if pk else None)


def silences(p):
    r = sh([FF, "-hide_banner", "-i", p, "-af", "silencedetect=noise=-60dB:d=0.3",
            "-f", "null", "-"])
    out = []
    for m in re.finditer(r"silence_start:\s*(-?[\d.]+).*?silence_duration:\s*([\d.]+)", r.stderr, re.S):
        out.append((float(m.group(1)), float(m.group(2))))
    return out


def asr_speech_end(lang, clip):
    """Diem ket thuc cua loi noi theo cache ASR (neu co)."""
    c = os.path.join(ROOT, ".work", f"_tk_asr_tk04_{clip}_{lang}.json")
    if not os.path.exists(c):
        return None, None
    d = json.load(io.open(c, encoding="utf-8"))
    w = d.get("words") or []
    if not w:
        return None, None
    return float(w[-1]["e"]), float(d.get("duration") or 0)


report = []
for lang, d in LANGS:
    p = os.path.join(TIK, d)
    print("=" * 80)
    print(f"NEN AUDIO — {lang}  ({d})")
    print("=" * 80)
    for n in range(1, 6):
        clip = "TK%d" % n
        mp3 = os.path.join(p, f"TK{n}_master_audio.mp3")
        tl = os.path.join(p, f"timeline_tk{n}.json")
        if not os.path.exists(mp3):
            print(f"  {clip}: THIEU MASTER")
            continue
        dur = probe(mp3)
        I, TP = lufs(mp3)
        sil = silences(mp3)
        end_speech, asr_dur = asr_speech_end(lang, clip)
        rows = json.load(io.open(tl, encoding="utf-8-sig")) if os.path.exists(tl) else []
        missing = [r["id"] for r in rows if r.get("match_ratio", 1) == 0]
        weak = [r["id"] for r in rows if 0 < r.get("match_ratio", 1) < 0.6]
        interp = [r["id"] for r in rows if r.get("interp")]
        tail = (dur - end_speech) if end_speech else None
        gaps = []
        for a, b in zip(rows, rows[1:]):
            g = b["start"] - a["end"]
            if g > 1.5:
                gaps.append((a["id"], b["id"], round(g, 2)))
        issues = []
        if missing:
            issues.append(f"THIEU {len(missing)} CAU: {missing}")
        if tail is not None and tail > 1.0:
            issues.append(f"DUOI CAM {tail:.2f}s")
        if sil:
            issues.append(f"{len(sil)} khoang cam >0.3s, dai nhat {max(s[1] for s in sil):.2f}s")
        if I is None or abs(I + 16) > 1.0:
            issues.append(f"LUFS {I} (can -16+-1)")
        if TP is not None and TP > -1.5:
            issues.append(f"true peak {TP} (> -1.5)")
        if gaps:
            issues.append(f"{len(gaps)} loi gap >1.5s")
        print(f"  {clip}: {dur:6.2f}s  {I} LUFS  TP {TP}  sil={len(sil)}  "
              f"loi noi cuoi={end_speech}  duoi cam={tail if tail is None else round(tail,2)}")
        if weak:
            print(f"        match yeu: {weak}")
        if gaps:
            print(f"        gap >1.5s: {gaps}")
        print(f"        >>> VAN DE: {'; '.join(issues) if issues else 'KHONG CO'}")
        report.append({"lang": lang, "clip": clip, "dur": dur, "lufs": I, "tp": TP,
                       "silences": sil, "missing": missing, "weak": weak,
                       "interp": interp, "tail": tail, "gaps": gaps, "issues": issues})
    print()

print("=" * 80)
print("TONG HOP VAN DE AUDIO")
print("=" * 80)
bad = [r for r in report if r["issues"]]
if not bad:
    print("KHONG CO VAN DE")
for r in bad:
    print(f"  {r['lang']} {r['clip']}: {'; '.join(r['issues'])}")
with io.open(os.path.join(ROOT, ".work", "_audit_audio_tk04.json"), "w", encoding="utf-8") as f:
    f.write(json.dumps(report, ensure_ascii=False, indent=1))
print("\nBao cao: .work/_audit_audio_tk04.json")
