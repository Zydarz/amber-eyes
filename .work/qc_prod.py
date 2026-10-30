"""QC lượt sản xuất Tập 02 (Higgs Audio v3) — theo §8 QUY_TAC_AUDIO_HIGGS.md.

Mỗi file âm thanh phải qua 6 kiểm:
  1. giải mã được, WAV PCM 16-bit
  2. đúng 24 kHz, mono
  3. 0,5 s < thời lượng < 47 s
  4. tỉ lệ giây/âm tiết trong ±35% so với trung vị cùng vai
  5. không có đoạn lặng > 0,3 s ở −60 dBFS **bên trong** câu
  6. không có đuôi tạp âm (100 ms cuối lặng/không có năng lượng nói)

Input : .work/kaggle_higgs/out_higgs_prod/out_higgs_prod/  (higgs_manifest.json)
Output: .work/qc_prod.txt + .work/qc_prod.json

Usage: python .work/qc_prod.py
"""
import json
import pathlib
import re
import sys
import wave
from collections import defaultdict

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
WAVDIR = HERE / "kaggle_higgs" / "out_higgs_prod" / "out_higgs_prod"
OUT_T = HERE / "qc_prod.txt"
OUT_J = HERE / "qc_prod.json"

SR_EXPECT = 24000
DUR_MIN, DUR_MAX = 0.5, 47.0
SIL_DB = -60.0
SIL_MAX = 0.30          # giây, bên trong câu
SYL_TOL = 0.35          # ±35% so với trung vị vai
TAIL_S = 0.10

# ------------------------------------------------------------------ đọc wav
def read_wav(p):
    with wave.open(str(p), "rb") as w:
        sr, nch, sw, n = w.getframerate(), w.getnchannels(), w.getsampwidth(), w.getnframes()
        raw = w.readframes(n)
    if sw != 2:
        raise ValueError("sau 16-bit (sampwidth=%d)" % sw)
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    if nch > 1:
        a = a.reshape(-1, nch).mean(axis=1)
    return a, sr, nch, sw


def max_internal_silence(a, sr, thr_db=-60.0):
    """Do dai (s) cua doan im lang dai nhat 'ben trong' — bo 100 ms dau/cuoi."""
    if a.size == 0:
        return 0.0
    thr = 10 ** (thr_db / 20)
    win = max(1, int(0.010 * sr))
    nb = len(a) // win
    if nb < 3:
        return 0.0
    fr = a[:nb * win].reshape(nb, win)
    rms = np.sqrt((fr ** 2).mean(axis=1))
    q = rms < thr
    # bo 100 ms dau + cuoi
    k = int(0.10 * sr / win)
    if k * 2 < nb:
        q[:k] = False
        q[-k:] = False
    best = cur = 0
    for v in q:
        cur = cur + 1 if v else 0
        if cur > best:
            best = cur
    return best * win / sr


def tail_noise(a, sr, tail_s=TAIL_S):
    """RMS duoi 100 ms cuoi / RMS toan bo — cao la duoi nhieu."""
    if a.size < int(sr * tail_s) * 2:
        return 0.0
    t = a[-int(sr * tail_s):]
    body = a[:-int(sr * tail_s)]
    rb = float(np.sqrt((body ** 2).mean())) if body.size else 0.0
    rt = float(np.sqrt((t ** 2).mean()))
    return (rt / rb) if rb > 1e-6 else (1.0 if rt > 1e-6 else 0.0)


def main():
    man_p = WAVDIR / "higgs_manifest.json"
    if not man_p.exists():
        cands = sorted((HERE / "kaggle_higgs" / "out_higgs_prod").rglob("higgs_manifest.json"))
        if not cands:
            raise SystemExit("khong tim thay manifest san xuat")
        man_p = cands[0]
    rows = [r for r in json.loads(man_p.read_text(encoding="utf-8-sig")) if r.get("ok")]
    print("manifest:", man_p, "| OK:", len(rows))

    recs = []
    for r in rows:
        p = WAVDIR / r["file"]
        if not p.exists():
            cands = list((HERE / "kaggle_higgs" / "out_higgs_prod").rglob(r["file"]))
            if not cands:
                continue
            p = cands[0]
        rec = {"id": r["id"], "role": r["role"], "ref_wav": r["ref_wav"],
               "variant": r.get("variant"), "file": r["file"], "bad": []}
        # so tu (bo the Higgs tag) — cung tieu chuan voi measure_cer_prod.py
        txt = re.sub(r"<\|[^|]*\|>", " ", r.get("text_plain") or r.get("text_sent") or "")
        txt = re.sub(r"<#.*?#>", " ", txt)
        rec["nwords"] = len(txt.split())
        try:
            a, sr, nch, sw = read_wav(p)
        except Exception as e:
            rec["bad"].append("KHONG GIAI MA: %s" % e)
            recs.append(rec)
            continue
        dur = len(a) / sr
        rec.update(sr=sr, nch=nch, sw=sw, dur=round(dur, 2),
                   peak=round(float(np.abs(a).max()), 4))
        if sr != SR_EXPECT:
            rec["bad"].append("SR %d != %d" % (sr, SR_EXPECT))
        if nch != 1:
            rec["bad"].append("khong mono (%d kenh)" % nch)
        if not (DUR_MIN < dur < DUR_MAX):
            rec["bad"].append("thoi luong %.2f s ngoai (%.1f, %.1f)" % (dur, DUR_MIN, DUR_MAX))
        sil = max_internal_silence(a, sr)
        rec["silence_s"] = round(sil, 3)
        if sil > SIL_MAX:
            rec["bad"].append("im lang noi %.3f s > %.2f s" % (sil, SIL_MAX))
        tn = tail_noise(a, sr)
        rec["tail_ratio"] = round(tn, 3)
        if tn > 0.30:
            rec["bad"].append("duoi tap am (ratio %.2f)" % tn)
        recs.append(rec)

    # ---- tỉ lệ giây/âm tiết so với trung vị vai (dùng text_norm nếu có) ----
    by_role = defaultdict(list)
    for rec in recs:
        if rec.get("dur"):
            nw = rec.get("nwords")
            if nw:
                by_role[rec["role"]].append(rec)
    med = {}
    for role, v in by_role.items():
        rates = [x["nwords"] / x["dur"] for x in v]
        med[role] = float(np.median(rates))
    for rec in recs:
        if rec["role"] in med and rec.get("nwords") and rec.get("dur"):
            rate = rec["nwords"] / rec["dur"]
            rec["syl_rate"] = round(rate, 3)
            rec["rate_ratio"] = round(rate / med[rec["role"]], 3)
            if abs(rate / med[rec["role"]] - 1) > SYL_TOL:
                rec["bad"].append("nhip am tiem %.3f/s = %.0f%% trung vi vai (ngoai +-%.0f%%)"
                                  % (rate, 100 * rate / med[rec["role"]], 100 * SYL_TOL))

    bad = [r for r in recs if r["bad"]]
    L = []
    L.append("=" * 100)
    L.append("QC LUOT SAN XUAT TAP 02 — Higgs Audio v3 (§8)")
    L.append("=" * 100)
    L.append("file kiem: %d | dat: %d | LOI: %d" % (len(recs), len(recs) - len(bad), len(bad)))
    L.append("")
    L.append("Nhip am tiem trung vi theo vai (am/s): " + ", ".join(
        "%s=%.3f" % (k, v) for k, v in sorted(med.items())))
    L.append("")
    if bad:
        L.append("FILE LOI (%d):" % len(bad))
        L.append("%-12s %-4s %-5s %-8s %-9s %s" % ("id", "vai", "var", "dur", "im lang", "ly do"))
        for r in sorted(bad, key=lambda x: x["id"]):
            L.append("%-12s %-4s %-5s %-8s %-9s %s" % (
                r["id"], r["role"], r.get("variant"), r.get("dur"), r.get("silence_s"),
                "; ".join(r["bad"])))
    else:
        L.append("KHONG CO FILE LOI — tat ca %d file qua het 6 kiem." % len(recs))
    L.append("")
    L.append("Theo vai:")
    g = defaultdict(list)
    for r in recs:
        g[r["role"]].append(r)
    L.append("%-6s %-6s %-16s %-9s %-10s %-10s %-9s" % (
        "Vai", "n", "clip", "dur tb", "im lang max", "duoi max", "nhip/s"))
    for role, v in sorted(g.items()):
        L.append("%-6s %-6d %-16s %-9.2f %-10.3f %-10.2f %-9.3f" % (
            role, len(v), v[0]["ref_wav"],
            float(np.median([x["dur"] for x in v if x.get("dur")])),
            max((x.get("silence_s") or 0) for x in v),
            max((x.get("tail_ratio") or 0) for x in v),
            med.get(role, 0)))

    txt = "\n".join(L)
    OUT_T.write_text(txt, encoding="utf-8")
    OUT_J.write_text(json.dumps({"n": len(recs), "n_bad": len(bad),
                                 "median_syl_rate": med, "records": recs},
                                ensure_ascii=False, indent=1), encoding="utf-8")
    print(txt)
    print("\n->", OUT_T)
    print("->", OUT_J)


if __name__ == "__main__":
    main()
