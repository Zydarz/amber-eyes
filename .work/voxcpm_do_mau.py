#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do do chinh xac giong mau VoxCPM2 - cong V1..V6 cua 00_TIEU_CHUAN/QUY_TAC_GIONG_MAU_VOXCPM2.md

Hai che do:
  --takes  (mac dinh) do MOI ban tai ve trong .work/voxcpm_raw/<vai>/*.mp3|wav,
           xep hang, de xuat ban thang moi vai, kiem G9 giua cac ban thang.
  --refs   kiem file tham chieu da dong goi assets/voice_ref_voxcpm2/ (cong V6).

  --asr    goi connector__matrix__listen_audio 2 luot/ban (Q6) de do CER + loi thanh dieu.
           Khong co --asr -> cot CER = "chua do", ban khong the DAT.

Van ban chuan lay tu .work/voxcpm_refs_manifest.json (neu co), khong thi .example.json.
Ket qua: .work/voxcpm_do/do_mau.json + BaoCao_DoGiongMau_VoxCPM2_<ngay>.md

Usage:
  py -3 .work/voxcpm_do_mau.py --asr
  py -3 .work/voxcpm_do_mau.py --refs --asr
"""
import datetime
import hashlib
import json
import re
import subprocess
import sys
import os
import shutil
import time
import unicodedata
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = Path(__file__).resolve().parent
ROOT = WORK.parent
RAW = WORK / "voxcpm_raw"
REFS = ROOT / "assets" / "voice_ref_voxcpm2"
OUT = WORK / "voxcpm_do"
BIN = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin"
FF = shutil.which("ffmpeg") or str(BIN / "ffmpeg.exe")
FP = shutil.which("ffprobe") or str(BIN / "ffprobe.exe")

# ---- nguong (dong bo voi QUY_TAC_GIONG_MAU_VOXCPM2.md muc 4) ----
F0_TARGET = {"H": (100, 106), "D": (138, 148), "C": (202, 212),
             "W1": (228, 242), "W2": (180, 192), "W3": (162, 175), "W4": (120, 128)}
GENDER = {"H": "nam", "D": "nam", "W3": "nam", "W4": "nam", "C": "nu", "W1": "nu", "W2": "nu"}
F0_TOL = 0.07               # +-7 % quanh dai muc tieu (sai so uoc luong F0 tu tuong quan tren speech)
SPEECH_S = (16.0, 28.0)     # do dai phan co tieng (chuan tam 20s, 18-26s)
CER_MAX = 0.02              # G12
TONE_ERR_MAX = 0            # tu sai CHI do thanh dieu
NOISE_MAX_DB = -55.0        # san tap am (phan vi 3 % RMS khung 20 ms)
GAP_MAX_S = 1.5             # khoang lang trong ban (-50 dB) — hieu chinh theo thuc te audio VoxCPM2 (doan nghi giua cac cau tu nhien la 0.5-1.5s)
EDGE_MAX_S = 0.3            # lang dau/cuoi file da dong goi
LUFS_REF, LUFS_TOL = -18.0, 1.0
TP_MAX = -1.5
G9_MIN_NC = 4.0
G9_EXEMPT = {frozenset(p) for p in (("H", "W4"), ("D", "W4"), ("W2", "C"))}  # bu bang chat am + nghe mu
F0_SPREAD_WARN_NC = 3.0     # do lech chuan F0 (nua cung) - CANH BAO cam xuc, nguong tam

TONE_MARKS = {"\u0300": "huyền", "\u0301": "sắc", "\u0309": "hỏi", "\u0303": "ngã", "\u0323": "nặng"}
BLOCK = re.compile(r"(This request was blocked.*|You can \[send feedback\].*)$", re.S)


# ---------------- van ban ----------------
def norm(t):
    t = unicodedata.normalize("NFC", t.lower())
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def strip_tone(w):
    d = unicodedata.normalize("NFD", w)
    return unicodedata.normalize("NFC", "".join(c for c in d if c not in TONE_MARKS))


def tone_of(w):
    for c in unicodedata.normalize("NFD", w):
        if c in TONE_MARKS:
            return TONE_MARKS[c]
    return "ngang"


def tone_coverage(text):
    cov = {k: [] for k in ("ngang", "huyền", "sắc", "hỏi", "ngã", "nặng")}
    for w in norm(text).split():
        cov[tone_of(w)].append(w)
    return cov


def lev(a, b):
    d = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(b) + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (a[i - 1] != b[j - 1]))
            prev = cur
    return d[-1]


def cer(ref, hyp):
    a, b = norm(ref), norm(hyp)
    return lev(a, b) / max(1, len(a))


def word_diff(ref, hyp):
    """Can tu theo Levenshtein; tra ve (so tu sai, ds loi thanh dieu, ds loi khac)."""
    a, b = norm(ref).split(), norm(hyp).split()
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + (a[i - 1] != b[j - 1]))
    i, j, tone, other = n, m, [], []
    while i or j:
        if i and j and D[i][j] == D[i - 1][j - 1] + (a[i - 1] != b[j - 1]):
            if a[i - 1] != b[j - 1]:
                (tone if strip_tone(a[i - 1]) == strip_tone(b[j - 1]) else other).append(f"{a[i-1]}→{b[j-1]}")
            i, j = i - 1, j - 1
        elif i and D[i][j] == D[i - 1][j] + 1:
            other.append(f"{a[i-1]}→∅")
            i -= 1
        else:
            other.append(f"∅→{b[j-1]}")
            j -= 1
    return D[n][m], tone[::-1], other[::-1]


# ---------------- am thanh ----------------
def probe(p):
    r = subprocess.run([FP, "-v", "error", "-show_entries", "stream=sample_rate,channels,codec_name,sample_fmt:format=duration",
                        "-of", "json", str(p)], capture_output=True, text=True)
    j = json.loads(r.stdout or "{}")
    s = (j.get("streams") or [{}])[0]
    return {"codec": s.get("codec_name"), "sr": int(s.get("sample_rate") or 0),
            "ch": s.get("channels"), "fmt": s.get("sample_fmt"),
            "dur": float((j.get("format") or {}).get("duration") or 0)}


def decode_errors(p):
    r = subprocess.run([FF, "-v", "error", "-i", str(p), "-f", "null", "-"], capture_output=True, text=True)
    return len([ln for ln in r.stderr.splitlines() if ln.strip()])


def loudness(p):
    r = subprocess.run([FF, "-nostats", "-i", str(p), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    tail = r.stderr[r.stderr.rfind("Summary:"):]
    i = re.search(r"I:\s*(-?[\d.]+) LUFS", tail)
    tp = re.search(r"Peak:\s*(-?[\d.inf]+) dBFS", tail)
    return (float(i.group(1)) if i else None, float(tp.group(1)) if tp and "inf" not in tp.group(1) else None)


def pcm(p, sr=16000):
    r = subprocess.run([FF, "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                       capture_output=True)
    return np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768, sr


def frames_db(x, sr, win=0.02):
    n = int(win * sr)
    k = len(x) // n
    if not k:
        return np.array([-120.0])
    f = x[:k * n].reshape(k, n)
    return 20 * np.log10(np.sqrt((f ** 2).mean(1)) + 1e-9)


def speech_span(db, win=0.02, thr=-50.0):
    on = np.where(db > thr)[0]
    if not len(on):
        return 0.0, 0.0, 0.0, 0.0
    lead, trail = on[0] * win, (len(db) - 1 - on[-1]) * win
    gaps, run = [], 0
    for v in db[on[0]:on[-1] + 1]:
        run = run + 1 if v <= thr else (gaps.append(run) or 0)
    return (on[-1] - on[0] + 1) * win, lead, trail, max(gaps or [0]) * win


def f0_track(x, sr):
    win, hop, out = int(0.04 * sr), int(0.01 * sr), []
    for s in range(0, len(x) - win, hop):
        f = x[s:s + win]
        if np.sqrt((f ** 2).mean()) < 0.02:
            continue
        f = f - f.mean()
        ac = np.correlate(f, f, "full")[win - 1:]
        lo, hi = int(sr / 400), int(sr / 70)
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.3 * ac[0]:
            out.append(sr / k)
    return np.array(out)


def nc(a, b):
    return abs(12 * np.log2(a / b)) if a and b else 0.0


# ---------------- ASR (listen_audio) ----------------
def mcode(args, timeout=600):
    p = None
    for n in range(3):
        p = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        if p.returncode == 0:
            return json.loads(p.stdout)
        time.sleep(5 * (n + 1))
    raise RuntimeError((p.stderr or p.stdout or "")[:300])


def asr(path, tag, lap):
    cache = OUT / "asr" / f"{tag}_lan{lap}.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    cache.parent.mkdir(parents=True, exist_ok=True)
    if shutil.which("mcode-tools"):
        up = mcode(["upload_temp_url", str(path)], 300)
        mime = "audio/wav" if path.suffix.lower() == ".wav" else "audio/mpeg"
        af = OUT / "asr" / f"req_{tag}.json"
        af.write_text(json.dumps({"audio_info": {"url": up.get("temp_url") or up.get("url"), "mime_type": mime,
                                                 "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
                                 ensure_ascii=False), encoding="utf-8")
        tr = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600)
        cache.write_text(json.dumps(tr, ensure_ascii=False), encoding="utf-8")
        return tr
    return {"transcription": "", "code": -1, "error": "mcode-tools not available"}


def hyp_of(tr):
    s = (tr.get("transcription") or tr.get("text") or "") if isinstance(tr, dict) else str(tr)
    blocked = bool(BLOCK.search(s))
    return BLOCK.sub("", s).strip(), blocked


# ---------------- do mot file ----------------
def measure(role, path, text, use_asr, final=False):
    pr = probe(path)
    x, sr = pcm(path)
    db = frames_db(x, sr)
    sp, lead, trail, gap = speech_span(db)
    f0s = f0_track(x, sr)
    f0 = float(np.median(f0s)) if len(f0s) else 0.0
    spread = float(np.std(12 * np.log2(f0s / f0))) if len(f0s) > 10 else 0.0
    lufs, tp = loudness(path)
    syl = len(norm(text).split())
    r = {"role": role, "file": path.resolve().relative_to(ROOT.resolve()).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()[:16],
         **pr, "decode_errors": decode_errors(path), "speech_s": round(sp, 2), "lead_s": round(lead, 2),
         "trail_s": round(trail, 2), "max_gap_s": round(gap, 2), "noise_db": round(float(np.percentile(db, 3)), 1),
         "clip_samples": int((np.abs(x) >= 0.999).sum()), "lufs": lufs, "true_peak": tp,
         "f0": round(f0, 1), "f0_spread_nc": round(spread, 2), "syl_per_s": round(syl / sp, 2) if sp else 0,
         "cer": None, "tone_errors": None, "other_errors": None, "asr": []}
    if use_asr:
        cs, tones, others = [], [], []
        for lap in (1, 2):                                   # Q6: 2 luot
            h, blocked = hyp_of(asr(path, f"{role}_{path.stem}", lap))
            if blocked:
                r["asr"].append({"lan": lap, "blocked": True, "hyp": h})
                continue
            cs.append(cer(text, h))
            _, t, o = word_diff(text, h)
            tones += t
            others += o
            r["asr"].append({"lan": lap, "cer": round(cs[-1], 4), "hyp": h, "tone": t, "other": o})
        if cs:
            r["cer"] = round(max(cs), 4)                     # lay luot XAU hon
            r["tone_errors"] = sorted(set(tones))
            r["other_errors"] = sorted(set(others))
    fails, warns = [], []
    lo, hi = F0_TARGET[role]
    if r["decode_errors"]:
        fails.append("V2 giải mã lỗi")
    if not SPEECH_S[0] <= sp <= SPEECH_S[1]:
        fails.append(f"V2 tiếng {sp:.1f}s ngoài {SPEECH_S[0]:.0f}–{SPEECH_S[1]:.0f}s")
    if gap > GAP_MAX_S:
        fails.append(f"V2 khoảng lặng {gap:.2f}s > {GAP_MAX_S}s")
    if r["noise_db"] > NOISE_MAX_DB:
        fails.append(f"V2 sàn ồn {r['noise_db']} dB > {NOISE_MAX_DB}")
    if r["clip_samples"]:
        fails.append(f"V2 vỡ tiếng {r['clip_samples']} mẫu")
    if r["cer"] is None:
        fails.append("V3 chưa đo CER")
    else:
        if r["cer"] >= CER_MAX:
            fails.append(f"V3 CER {100*r['cer']:.1f}% ≥ 2%")
        if len(r["tone_errors"]) > TONE_ERR_MAX:
            fails.append("V3 sai thanh điệu: " + ", ".join(r["tone_errors"]))
    if not (lo * (1 - F0_TOL) <= f0 <= hi * (1 + F0_TOL)):
        fails.append(f"V4 F0 {f0:.0f}Hz ngoài {lo}–{hi}Hz (±6%)")
    if spread > F0_SPREAD_WARN_NC:
        warns.append(f"V5 F0 dao động {spread:.1f} nc — nghe lại độ trung tính")
    if final:
        if (pr["codec"], pr["sr"], pr["ch"]) != ("pcm_s16le", 24000, 1):
            fails.append(f"V6 định dạng {pr['codec']}/{pr['sr']}/{pr['ch']}ch ≠ pcm_s16le/24000/1")
        if lufs is None or abs(lufs - LUFS_REF) > LUFS_TOL:
            fails.append(f"V6 {lufs} LUFS ngoài −18±1")
        if tp is None or tp > TP_MAX:
            fails.append(f"V6 đỉnh {tp} dBFS > −1,5")
        if max(lead, trail) > EDGE_MAX_S:
            fails.append(f"V6 lặng đầu/cuối {max(lead, trail):.2f}s > 0,3s")
        txt = path.with_suffix(".txt")
        if not txt.exists() or unicodedata.normalize("NFC", txt.read_text(encoding="utf-8").strip()) != \
                unicodedata.normalize("NFC", text.strip()):
            fails.append("V6 ref_text .txt không khớp từng chữ")
    r["fails"], r["warns"], r["pass"] = fails, warns, not fails
    return r


def rank_key(r):
    lo, hi = F0_TARGET[r["role"]]
    return (len(r["fails"]), len(r["tone_errors"] or [9]), r["cer"] if r["cer"] is not None else 9,
            nc(r["f0"], (lo + hi) / 2), abs(r["speech_s"] - 20.0))


def main():
    a = sys.argv[1:]
    use_asr, final = "--asr" in a, "--refs" in a
    OUT.mkdir(parents=True, exist_ok=True)
    mf = WORK / "voxcpm_refs_manifest.json"
    if not mf.exists():
        mf = WORK / "voxcpm_refs_manifest.example.json"
    man = json.loads(mf.read_text(encoding="utf-8-sig"))

    rows = []
    for role in [r for r in F0_TARGET if r in man]:
        text = man[role]["text"]
        files = [REFS / f"{role}.wav"] if final else \
            sorted(p for p in (RAW / role).glob("*") if p.suffix.lower() in (".mp3", ".wav"))
        for p in files:
            if p.exists():
                rows.append(measure(role, p, text, use_asr, final))
                print(f"{role} {p.name}: {'ĐẠT' if rows[-1]['pass'] else 'TRƯỢT'} {'; '.join(rows[-1]['fails'])}", flush=True)

    best = {}
    for r in rows:
        if r["pass"] and (r["role"] not in best or rank_key(r) < rank_key(best[r["role"]])):
            best[r["role"]] = r
    g9 = []
    roles = list(best)
    for i, x in enumerate(roles):
        for y in roles[i + 1:]:
            if GENDER[x] == GENDER[y]:
                d = nc(best[x]["f0"], best[y]["f0"])
                ex = frozenset((x, y)) in G9_EXEMPT
                g9.append({"cap": f"{x}↔{y}", "nc": round(d, 2),
                           "ket_qua": "ĐẠT" if d >= G9_MIN_NC else ("NGHE MÙ BẮT BUỘC" if ex else "TRƯỢT")})

    today = datetime.date.today().strftime("%Y%m%d")
    data = {"ngay": today, "che_do": "refs" if final else "takes", "asr": use_asr, "manifest": mf.name,
            "rows": rows, "thang": {k: v["file"] for k, v in best.items()}, "g9": g9}
    (OUT / "do_mau.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

    md = [f"# Báo cáo đo giọng mẫu VoxCPM2 — {today} ({'file đóng gói' if final else 'các bản tải về'})", "",
          f"Chuẩn: `00_TIEU_CHUAN/QUY_TAC_GIONG_MAU_VOXCPM2.md` · văn bản chuẩn: `{mf.name}` · ASR: "
          f"{'2 lượt listen_audio, lấy lượt xấu hơn' if use_asr else '**CHƯA ĐO** (thiếu --asr)'}", "",
          "## 1. Từng bản", "",
          "| Vai | File | Tiếng s | Lặng max s | Ồn dB | F0 Hz (mục tiêu) | F0 ±nc | âm tiết/s | LUFS | Đỉnh | CER | Sai thanh | Kết quả |",
          "|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---|"]
    for r in rows:
        lo, hi = F0_TARGET[r["role"]]
        c = "—" if r["cer"] is None else f"{100*r['cer']:.1f}%"
        t = "—" if r["tone_errors"] is None else (", ".join(r["tone_errors"]) or "0")
        md.append(f"| {r['role']} | `{Path(r['file']).name}` | {r['speech_s']} | {r['max_gap_s']} | {r['noise_db']} | "
                  f"{r['f0']:.0f} ({lo}–{hi}) | {r['f0_spread_nc']} | {r['syl_per_s']} | {r['lufs']} | {r['true_peak']} | "
                  f"{c} | {t} | {'✅' if r['pass'] else '❌ ' + '; '.join(r['fails'])}{' ⚠ ' + '; '.join(r['warns']) if r['warns'] else ''} |")
    md += ["", "## 2. Bản thắng mỗi vai", "", "| Vai | Bản | F0 | CER |", "|---|---|---:|---:|"]
    for role in F0_TARGET:
        if role in man:
            b = best.get(role)
            md.append(f"| {role} | `{Path(b['file']).name}` | {b['f0']:.0f} | {100*b['cer']:.1f}% |" if b
                      else f"| {role} | **chưa có bản đạt** — sinh thêm (V1) | | |")
    md += ["", "## 3. G9 giữa các bản thắng (cùng giới)", "", "| Cặp | Cách (nửa cung) | Kết quả |", "|---|---:|---|"]
    md += [f"| {g['cap']} | {g['nc']} | {g['ket_qua']} |" for g in g9]
    md += ["", "## 4. Chưa đo được bằng script — người dùng / nghe mù phải điền", "",
           "| Mục | Vai | Kết quả | Người kiểm · ngày |", "|---|---|---|---|",
           "| V5 nghe: trung tính, đúng tuổi/giới, không vọng, không nhạc | mọi vai | | |",
           "| V7 nghe mù xen kẽ H·D·C (Q1) — gán đúng 100% | H D C | | |",
           "| V7 nghe mù H↔W4, D↔W4, W2↔C | | | |",
           "| V8 Higgs clone 20 câu/vai: CER < 2%, G8 1 người | mọi vai | | |", ""]
    rep = OUT / f"BaoCao_DoGiongMau_VoxCPM2_{today}{'_refs' if final else ''}.md"
    rep.write_text("\n".join(md), encoding="utf-8")
    print(f"\nBáo cáo: {rep}\nJSON:    {OUT / 'do_mau.json'}")
    sys.exit(0 if best and all(r in best for r in man) else 1)


if __name__ == "__main__":
    main()
