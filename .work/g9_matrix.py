"""G9 — bang khoang cach nua cung cho MOI cap cung gioi (Tap 02 / Higgs Audio v3).

Van de G9 (AGENTS.md dong 111):
  "Cac vai phai khac hanh nhau: hai giong cung gioi cach nhau >= 4 nua cung,
   khac ro chat giong; xen ke 3 vai -> nghe mu gan dung 100%"

Tap 02 co 5 vai: H (nam) · D (nam) · C (nu) · N1 (nu) · N2 (nu)
=> cap cung gioi phai kiem: H<->D · C<->N1 · C<->N2 · N1<->N2

Script nay:
  1. do lai F0 (2 thuat toan) cho TAT CA audio clone cua pilot v3 + pilot v4
  2. gop theo (vai, clip tham chieu, temperature) -> median + khoang
  3. in bang G9 day du + duyet tat ca phan bo (N1_clip, N2_clip) co the
  4. tinh khoang F0 moi can tao cho clip tham chieu moi

Khong goi ASR, khong goi model. Chi doc WAV local.
"""
import json
import math
import pathlib
import sys
import wave
from collections import defaultdict

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent                                    # repo goc
sys.path.insert(0, str(ROOT))
from voice_audition import f0_median as f0_ac  # noqa: E402

KAGGLE = HERE / "kaggle_higgs"                  # noi luu audio pilot v3 + v4
REF_DIR = ROOT / "assets" / "voice_ref_voxcpm2"
OUT = HERE / "g9_matrix.json"


def read_wav(p):
    with wave.open(str(p), "rb") as w:
        sr, nch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        raw = w.readframes(w.getnframes())
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    if nch > 1:
        a = a.reshape(-1, nch).mean(axis=1)
    return a, sr


def f0_p2(x, sr, fmin=70.0, fmax=400.0):
    """AC chuan hoa + parabolic + sua octave (pp2) — giong _v4_f0.py."""
    win = int(0.045 * sr)
    hop = int(0.010 * sr)
    lo, hi = int(sr / fmax), int(sr / fmin)
    out, prev = [], None
    for s in range(0, len(x) - win, hop):
        f = x[s:s + win]
        if np.sqrt((f ** 2).mean()) < 0.01:
            continue
        f = f - f.mean()
        peak = np.max(np.abs(f))
        if peak > 0:
            f = np.clip(f, -0.5 * peak, 0.5 * peak)
        n = len(f)
        nfft = 1 << int(np.ceil(np.log2(2 * n)))
        F = np.fft.rfft(f, nfft)
        ac = np.fft.irfft(F * np.conj(F), nfft)[:n]
        if ac[0] <= 0:
            continue
        acn = ac / ac[0]
        k = lo + int(np.argmax(acn[lo:hi]))
        if acn[k] < 0.25:
            continue
        shift = 0.0
        if 0 < k < n - 1:
            a0, a1, a2 = acn[k - 1], acn[k], acn[k + 1]
            d = a0 - 2 * a1 + a2
            if d != 0:
                shift = 0.5 * (a0 - a2) / d
        f0 = sr / (k + shift)
        if prev is not None:
            if 0.5 * prev < f0 < prev:
                k2 = int(round(k / 2))
                if k2 >= lo and acn[k2] > 0.8 * acn[k]:
                    f0 = sr / (k2 + shift)
            elif prev < f0 < 2 * prev:
                k2 = int(round(k * 2))
                if k2 < len(acn) and acn[k2] > 0.8 * acn[k]:
                    f0 = sr / (k2 + shift)
        out.append(f0)
        prev = f0
    return out


def nc(a, b):
    """Khoang cach nua cung giua 2 F0."""
    if not a or not b or a <= 0 or b <= 0:
        return 0.0
    return abs(12 * math.log2(a / b))


def med(vals):
    v = sorted(x for x in vals if x)
    return v[len(v) // 2] if v else 0.0


# ---------------------------------------------------------------- 1. do F0 clone
rows_all = []
for tag, sub in (("v3", "out_higgs_v3"), ("v4", "out_higgs_v4")):
    man_cands = sorted((KAGGLE / sub).rglob("higgs_manifest.json"))
    if not man_cands:
        print(f"!! khong tim thay manifest cho {tag}")
        continue
    man_p = man_cands[0]
    root = man_p.parent
    man = json.loads(man_p.read_text(encoding="utf-8-sig"))
    n_ok = 0
    for r in man:
        if not r.get("ok"):
            continue
        p = root / r["file"]
        if not p.exists():
            cands = list((KAGGLE / sub).rglob(r["file"]))
            if not cands:
                continue
            p = cands[0]
        a, sr = read_wav(p)
        fr = f0_p2(a, sr)
        rows_all.append({
            "pilot": tag,
            "role": r["role"],
            "ref_wav": r["ref_wav"],
            "temp": r["temp"],
            "id": r.get("id"),
            "f0_ac": round(f0_ac(a, sr), 1),
            "f0_p2": round(float(np.median(fr)), 1) if fr else 0.0,
            "dur": round(len(a) / sr, 2),
        })
        n_ok += 1
    print(f"{tag}: {n_ok}/{len(man)} audio do F0 xong")

# ------------------------------------------------------- 2. gop theo vai/clip/temp
g = defaultdict(list)
for r in rows_all:
    g[(r["role"], r["ref_wav"], r["temp"])].append(r)

table = {}
for k, v in g.items():
    table["|".join([k[0], k[1], str(k[2])])] = {
        "role": k[0], "ref_wav": k[1], "temp": k[2], "n": len(v),
        "f0_ac": med([x["f0_ac"] for x in v]),
        "f0_p2": med([x["f0_p2"] for x in v]),
        "f0_ac_min": min(x["f0_ac"] for x in v),
        "f0_ac_max": max(x["f0_ac"] for x in v),
        "f0_p2_min": min(x["f0_p2"] for x in v),
        "f0_p2_max": max(x["f0_p2"] for x in v),
    }

print()
print("=" * 104)
print("F0 THUC cua audio clone (gop ca 2 bo pilot v3 + v4)")
print("=" * 104)
print("%-4s %-9s %-5s %-4s %-9s %-9s %-18s %-18s" % (
    "Vai", "Clip", "Temp", "n", "F0_ac", "F0_pp2", "F0_ac min-max", "F0_pp2 min-max"))
for k in sorted(table):
    t = table[k]
    print("%-4s %-9s %-5s %-4d %-9.1f %-9.1f %-18s %-18s" % (
        t["role"], t["ref_wav"], t["temp"], t["n"], t["f0_ac"], t["f0_p2"],
        "%.1f - %.1f" % (t["f0_ac_min"], t["f0_ac_max"]),
        "%.1f - %.1f" % (t["f0_p2_min"], t["f0_p2_max"])))

# ------------------------------------------------------------- 3. F0 clip goc
ref_f0 = {}
for p in sorted(REF_DIR.glob("*.wav")):
    a, sr = read_wav(p)
    fr = f0_p2(a, sr)
    ref_f0[p.stem] = {
        "f0_ac": round(f0_ac(a, sr), 1),
        "f0_p2": round(float(np.median(fr)), 1) if fr else 0.0,
        "dur": round(len(a) / sr, 2),
    }

print()
print("=" * 104)
print("F0 cua CLIP THAM CHIEU goc (assets/voice_ref_voxcpm2)")
print("=" * 104)
for k in sorted(ref_f0):
    print("  %-4s F0_ac=%6.1f  F0_pp2=%6.1f  %5.1f s" % (
        k, ref_f0[k]["f0_ac"], ref_f0[k]["f0_p2"], ref_f0[k]["dur"]))

# --------------------------------------------------------------- 4. bang G9
print()
print("=" * 104)
print("G9 — MOI cap cung gioi (nguong >= 4 nua cung)")
print("=" * 104)


def pick(role, ref, temp):
    return table.get("|".join([role, ref, str(temp)]))


H = pick("H", "H.wav", 0.8)
D = pick("D", "D.wav", 0.8)
C = pick("C", "C.wav", 0.8)

pairs = []
if H and D:
    pairs.append(("H", "D", H["f0_ac"], D["f0_ac"], H["f0_p2"], D["f0_p2"],
                  "H<-H.wav", "D<-D.wav"))
for n1ref in ("W1.wav", "W2.wav", "W3.wav", "W4.wav"):
    for n2ref in ("W1.wav", "W2.wav", "W3.wav", "W4.wav"):
        n1 = pick("N1", n1ref, 0.7)
        n2 = pick("N2", n2ref, 0.7)
        if n1 and n2 and C:
            pairs.append(("C", "N1", C["f0_ac"], n1["f0_ac"], C["f0_p2"], n1["f0_p2"],
                          "C<-C.wav", "N1<-%s" % n1ref))
            pairs.append(("C", "N2", C["f0_ac"], n2["f0_ac"], C["f0_p2"], n2["f0_p2"],
                          "C<-C.wav", "N2<-%s" % n2ref))
            pairs.append(("N1", "N2", n1["f0_ac"], n2["f0_ac"], n1["f0_p2"], n2["f0_p2"],
                          "N1<-%s" % n1ref, "N2<-%s" % n2ref))

print("%-5s %-5s %-13s %-13s %-8s %-8s %s" % (
    "VaiA", "VaiB", "A", "B", "nc_ac", "nc_pp2", "Ket"))
g9_rows = []
for a, b, fa, fb, pa, pb, da, db in pairs:
    d_ac, d_p2 = nc(fa, fb), nc(pa, pb)
    ok = min(d_ac, d_p2) >= 4
    warn = (not ok) and max(d_ac, d_p2) >= 4
    verdict = "DAT" if ok else ("CANH BAO" if warn else "TRUOT")
    print("%-5s %-5s %-13s %-13s %-8.2f %-8.2f %s" % (
        a, b, da, db, d_ac, d_p2, verdict))
    g9_rows.append({"a": a, "b": b, "a_detail": da, "b_detail": db,
                    "f0_ac_a": fa, "f0_ac_b": fb, "nc_ac": round(d_ac, 2),
                    "nc_pp2": round(d_p2, 2), "verdict": verdict})

# ------------------------------------------------- 5. duyet phan bo N1/N2
print()
print("=" * 104)
print("DUYET phan bo (N1_clip, N2_clip) — ca 3 cap nua (C<->N1, C<->N2, N1<->N2) deu >= 4 nc")
print("=" * 104)
print("%-10s %-10s %-9s %-9s %-9s %s" % (
    "N1 clip", "N2 clip", "C<->N1", "C<->N2", "N1<->N2", "Ket"))
combos = []
for n1ref in ("W1.wav", "W2.wav", "W3.wav", "W4.wav"):
    for n2ref in ("W1.wav", "W2.wav", "W3.wav", "W4.wav"):
        n1 = pick("N1", n1ref, 0.7)
        n2 = pick("N2", n2ref, 0.7)
        if not (n1 and n2 and C):
            continue
        a1 = min(nc(C["f0_ac"], n1["f0_ac"]), nc(C["f0_p2"], n1["f0_p2"]))
        a2 = min(nc(C["f0_ac"], n2["f0_ac"]), nc(C["f0_p2"], n2["f0_p2"]))
        a3 = min(nc(n1["f0_ac"], n2["f0_ac"]), nc(n1["f0_p2"], n2["f0_p2"]))
        ok = min(a1, a2, a3) >= 4
        warn = (not ok) and max(a1, a2, a3) >= 4
        verdict = "DAT" if ok else ("CANH BAO" if warn else "TRUOT")
        print("%-10s %-10s %-9.2f %-9.2f %-9.2f %s" % (
            n1ref, n2ref, a1, a2, a3, verdict))
        combos.append({"n1_ref": n1ref, "n2_ref": n2ref,
                       "c_n1": round(a1, 2), "c_n2": round(a2, 2),
                       "n1_n2": round(a3, 2), "verdict": verdict})

# ------------------------------------- 6. khoang F0 moi can tao cho clip moi
print()
print("=" * 104)
print("KHOANG F0 can co cho CLIP THAM CHIEU MOI (de clone dat G9)")
print("=" * 104)
h_ac = H["f0_ac"] if H else 124.3
d_ac = D["f0_ac"] if D else 123.7
c_ac = C["f0_ac"] if C else 208.7
n2_ac = pick("N2", "W1.wav", 0.7)
n2_ac = n2_ac["f0_ac"] if n2_ac else 275.9

req = {
    "H (de cach D >= 4 nc)": {
        "can_clone_f0_max": round(d_ac / (2 ** (4 / 12)), 1),
        "clip_tham_chieu_rough_hz": [70, 100],
    },
    "D (de cach H >= 4 nc)": {
        "can_clone_f0_min": round(h_ac * (2 ** (4 / 12)), 1),
        "clip_tham_chieu_rough_hz": [150, 190],
    },
    "N1 (nu, de cach C va N2 deu >= 4 nc)": {
        "can_clone_f0_max": round(min(c_ac, n2_ac) / (2 ** (4 / 12)), 1),
        "can_clone_f0_min": round(c_ac * (2 ** (4 / 12)), 1),
        "note": ("nen <= %.0f Hz va >= %.0f Hz -> khoang < %.0f Hz; "
                 "khong the > %.0f Hz (se sat N2)" % (
                     min(c_ac, n2_ac) / (2 ** (4 / 12)), c_ac * (2 ** (4 / 12)),
                     min(c_ac, n2_ac) / (2 ** (4 / 12)),
                     n2_ac * (2 ** (4 / 12)))),
        "clip_tham_chieu_rough_hz": [140, 175],
    },
}
for k, v in req.items():
    print("  %s" % k)
    for kk, vv in v.items():
        print("      %-28s %s" % (kk, vv))

OUT.write_text(json.dumps({
    "clone_f0_table": table,
    "ref_f0": ref_f0,
    "g9_pairs": g9_rows,
    "n1_n2_combos": combos,
    "required_new_clips": req,
}, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n->", OUT)
