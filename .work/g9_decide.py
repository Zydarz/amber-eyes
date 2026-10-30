"""CHOT phan bo vai Tap 02 (Higgs Audio v3) — do lai TOAN BO clip SACH da clone,
tinh G9 day du theo gioi tinh + cap ke thuc te cua Tap 02.

Input :
  .work/kaggle_higgs/out_higgs_v6/out_higgs_v6/higgs_manifest.json  (pilot v6, dung san)
  .work/kaggle_higgs/out_higgs_v7/out_higgs_v7/higgs_manifest.json  (do lai)
  .work/kaggle_higgs/out_higgs_v8/out_higgs_v8/higgs_manifest.json  (do lai)
  .work/script_tap02.json                                            (co-occurrence that)
  assets/voice_ref_voxcpm2*/ *.wav                                  (F0 clip goc)

Output:
  .work/g9_decide.json + .work/g9_decide.txt

Quy tac G9 (AGENTS.md dong 111):
  "Cac vai phai khac hanh nhau: hai giong cung gioi cach nhau >= 4 nua cung"
  => chi ap cho HOP CUNG GIOI. Verdict dung: min(nc_ac, nc_pp2) >= 4 => DAT.
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
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))
from voice_audition import f0_median as f0_ac  # noqa: E402

KG = HERE / "kaggle_higgs"
NC_MIN = 4.0

# GIOI TINH clip tham chieu (tu DAT_SPEC_G9.md + mo ta VoxCPM2)
CLIP_GENDER = {
    "H.wav": "nam", "D.wav": "nam", "W3.wav": "nam", "W4.wav": "nam",
    "M_LOW.wav": "nam", "M_HIGH.wav": "nam",
    "C.wav": "nu", "W1.wav": "nu", "W2.wav": "nu",
    "W5_HIGH.wav": "nu", "W6_LOW.wav": "nu",
}
# Vai -> gioi tinh nhan vat (tu CAST trong edition.py)
ROLE_GENDER = {"H": "nam", "D": "nam", "C": "nu", "N1": "nu", "N2": "nu"}
# Clip SACH (khong qua xu ly tan so) — phai ton tai trong assets/voice_ref_voxcpm2_g9/
CLEAN_CLIPS = ["H.wav", "D.wav", "C.wav", "W1.wav", "W2.wav", "W3.wav", "W4.wav",
               "M_LOW.wav", "M_HIGH.wav", "W5_HIGH.wav", "W6_LOW.wav"]


def read_wav(p):
    with wave.open(str(p), "rb") as w:
        sr, nch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        raw = w.readframes(w.getnframes())
    if sw == 2:
        a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    elif sw == 4:
        a = np.frombuffer(raw, np.int32).astype(np.float32) / 2147483648
    else:
        a = np.frombuffer(raw, np.uint8).astype(np.float32) / 128 - 1
    if nch > 1:
        a = a.reshape(-1, nch).mean(axis=1)
    return a, sr


def f0_p2(x, sr, fmin=70.0, fmax=400.0):
    """AC chuan hoa + parabolic + sua octave — cung thuat toan voi analyze_pilot_v6.py."""
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
    return float(np.median(out)) if out else 0.0


def med(v):
    v = sorted(x for x in v if x)
    return v[len(v) // 2] if v else 0.0


def nc(a, b):
    if not a or not b or a <= 0 or b <= 0:
        return 0.0
    return abs(12 * math.log2(a / b))


def fix_octave(ac, p2):
    if not ac or not p2:
        return p2 or 0.0, ""
    if abs(p2 * 2 - ac) / ac < 0.05:
        return round(p2 * 2, 1), "x2"
    if abs(p2 / 2 - ac) / ac < 0.05:
        return round(p2 * 2, 1), "nhan2"
    return round(p2, 1), ""


def measure_dir(d):
    """Do F0 clone theo (role, ref_wav) cho 1 thu muc output pilot."""
    d = pathlib.Path(d)
    man_p = d / "higgs_manifest.json"
    if not man_p.exists():
        cands = sorted(d.rglob("higgs_manifest.json"))
        if not cands:
            return {}
        man_p = cands[0]
    man = json.loads(man_p.read_text(encoding="utf-8-sig"))
    rows = [r for r in man if r.get("ok")]
    cells = defaultdict(list)
    for r in rows:
        p = d / r["file"]
        if not p.exists():
            continue
        a, sr = read_wav(p)
        ac = round(f0_ac(a, sr), 1)
        p2raw = round(f0_p2(a, sr), 1)
        p2, _ = fix_octave(ac, p2raw)
        cells[(r["role"], r["ref_wav"])].append((ac, p2))
    out = {}
    for k, v in cells.items():
        out[k] = {"role": k[0], "ref_wav": k[1], "n": len(v),
                  "f0_ac": med([x[0] for x in v]),
                  "f0_p2": med([x[1] for x in v])}
    print("  %-58s -> %d o" % (man_p.parent.name, len(out)))
    return out


# ------------------------------------------------------------------ 1. F0 clone
print("== do F0 clone ==")
CLONE = {}
for tag in ("v6", "v7", "v8"):
    d = KG / ("out_higgs_%s" % tag) / ("out_higgs_%s" % tag)
    if d.exists():
        for k, v in measure_dir(d).items():
            CLONE[k] = v

# ------------------------------------------------------------------ 2. F0 clip goc
REF_F0 = {}
for d in (ROOT / "assets" / "voice_ref_voxcpm2_g9", ROOT / "assets" / "voice_ref_voxcpm2"):
    if not d.exists():
        continue
    for w in sorted(d.glob("*.wav")):
        a, sr = read_wav(w)
        ac = round(f0_ac(a, sr), 1)
        p2raw = round(f0_p2(a, sr), 1)
        p2, _ = fix_octave(ac, p2raw)
        REF_F0.setdefault(w.name, {"f0_ac": ac, "f0_p2": p2,
                                   "dur": round(len(a) / sr, 2)})

# ------------------------------------------------------------------ 3. ke lien ke that
script = json.loads((HERE / "script_tap02.json").read_text(encoding="utf-8-sig"))
loi = [x for x in script if x.get("kind") == "LOI"]


def role_of(block):
    """Script goi vai nung 'N'; tach N1 (canh 1.07) va N2 (canh 4.06) nhu payload."""
    r = block["role"]
    if r != "N":
        return r
    return "N1" if block["id"].startswith("1.07") else "N2"


roles_seq = [role_of(x) for x in loi]
adj_pairs = defaultdict(int)
for a, b in zip(roles_seq, roles_seq[1:]):
    adj_pairs[tuple(sorted((a, b)))] += 1
role_count = defaultdict(int)
for r in roles_seq:
    role_count[r] += 1

# ------------------------------------------------------------------ 4. bang G9
def cell(role, ref):
    return CLONE.get((role, ref))


def pair_nc(c1, c2):
    """Tra ve (min, ac, pp2) — quy tac: ca 2 thuat toan deu >= 4 moi DAT."""
    x = nc(c1["f0_ac"], c2["f0_ac"])
    y = nc(c1["f0_p2"], c2["f0_p2"])
    return min(x, y), round(x, 2), round(y, 2)


L = []
L.append("=" * 104)
L.append("G9 DECIDE — Tap 02 (Higgs Audio v3).  Verdict: min(nc_ac, nc_pp2) >= 4 nc")
L.append("=" * 104)
L.append("")
L.append("[1] F0 CLONE THAT (do lai tu 3 pilot)")
L.append("    %-6s %-16s %-4s %-9s %-9s | %-9s %-9s %-8s %s" % (
    "Vai", "Clip", "n", "F0_ac", "F0_pp2", "clip_ac", "clip_pp2", "drift_ac", "gioi"))
for k in sorted(CLONE):
    c = CLONE[k]
    r = REF_F0.get(k[1], {})
    dr = "%+.1f%%" % (100 * (c["f0_ac"] / r["f0_ac"] - 1)) if r.get("f0_ac") else ""
    L.append("    %-6s %-16s %-4d %-9.1f %-9.1f | %-9s %-9s %-8s %s" % (
        k[0], k[1], c["n"], c["f0_ac"], c["f0_p2"],
        r.get("f0_ac", ""), r.get("f0_pp2", ""), dr,
        CLIP_GENDER.get(k[1], "?")))
L.append("")

L.append("[2] KE LIEN KE THAT cua Tap 02 (36 phan loi)")
for r in sorted(role_count):
    L.append("    %-3s %d phan" % (r, role_count[r]))
L.append("    Cap ke lien ke:")
for p, n in sorted(adj_pairs.items()):
    same = "cung gioi" if ROLE_GENDER[p[0]] == ROLE_GENDER[p[1]] else "KHAC gioi"
    L.append("      %-8s x%-3d  %s" % ("%s-%s" % p, n, same))
L.append("")

# ---- cac phuong an gan vai: chi dung clip SACH, dung gioi tinh vai
def candidates(role):
    g = ROLE_GENDER[role]
    out = []
    for ref in CLEAN_CLIPS:
        if CLIP_GENDER.get(ref) != g:
            continue
        c = cell(role, ref)
        if not c:
            continue
        out.append((ref, c))
    return out


H_C = candidates("H")
D_C = candidates("D")
C_C = candidates("C")
N1_C = candidates("N1")
N2_C = candidates("N2")

L.append("[3] UNG VIEN THEO GIOI TINH (chi clip SACH, da clone that)")
for name, lst in (("H (nam)", H_C), ("D (nam)", D_C), ("C (nu)", C_C),
                   ("N1 (nu)", N1_C), ("N2 (nu)", N2_C)):
    L.append("    %-9s %s" % (name, ", ".join(
        "%s(%.0f/%.0f)" % (r.replace(".wav", ""), c["f0_ac"], c["f0_p2"])
        for r, c in lst) or "—"))
L.append("")

full = []
for hr, h in H_C:
    for dr, d in D_C:
        for cr, c in C_C:
            for n1r, n1 in N1_C:
                for n2r, n2 in N2_C:
                    hd = pair_nc(h, d)
                    cn1 = pair_nc(c, n1)
                    cn2 = pair_nc(c, n2)
                    nn = pair_nc(n1, n2)
                    # G9 CHI ap cap CUNG GIOI
                    same_gender = [("H-D", hd)]
                    for nm, pair in (("C-N1", cn1), ("C-N2", cn2), ("N1-N2", nn)):
                        same_gender.append((nm, pair))
                    worst = min(p[1][0] for p in same_gender)
                    # cap ke lien ke that (chi cap cung gioi)
                    adj_same = [(("%s-%s" % p), adj_pairs[p]) for p in adj_pairs
                                if ROLE_GENDER[p[0]] == ROLE_GENDER[p[1]]]
                    full.append({
                        "H": hr, "D": dr, "C": cr, "N1": n1r, "N2": n2r,
                        "H_D": hd, "C_N1": cn1, "C_N2": cn2, "N1_N2": nn,
                        "margin": round(worst, 2),
                        "verdict": "DAT" if worst >= NC_MIN else "TRUOT",
                        "adj_same": adj_same,
                    })
full.sort(key=lambda r: -r["margin"])

L.append("[4] PHOI DAY DU — xep theo bien nho nhat (G9 ap cho CAP CUNG GIOI)")
L.append("    %-9s %-9s %-6s %-9s %-9s %-9s %-8s %s" % (
    "H", "D", "C", "H-D", "C-N1", "C-N2", "N1-N2", "Ket"))
for r in full[:15]:
    L.append("    %-9s %-9s %-6s %-9.2f %-9.2f %-9.2f %-8.2f %s" % (
        r["H"].replace(".wav", ""), r["D"].replace(".wav", ""), r["C"].replace(".wav", ""),
        r["H_D"][0], r["C_N1"][0], r["C_N2"][0], r["N1_N2"][0], r["verdict"]))
n_dat = len([r for r in full if r["verdict"] == "DAT"])
L.append("    => %d/%d phoi DAT" % (n_dat, len(full)))
L.append("")

# ---- phan tich rieng: cap nao dang ky ket
L.append("[5] PHAN TICH CAP KY KET — phoi nao that bai vi cap nao?")
fail_cnt = defaultdict(int)
for r in full:
    for nm in ("H_D", "C_N1", "C_N2", "N1_N2"):
        if r[nm][0] < NC_MIN:
            fail_cnt[nm] += 1
for nm in ("H_D", "C_N1", "C_N2", "N1_N2"):
    L.append("    %-8s that bai o %d/%d phoi" % (nm, fail_cnt[nm], len(full)))
L.append("")

# ---- phuong an gan vai du dung bo clip SACH + clip nao khong ton tai
L.append("[6] PHUONG AN (chi clip SACH, G9 ap cho cap cung gioi + cap ke lien ke that)")
L.append("    Chi danhgia cap CUNG GIOI. Cap lien ke that: %s" % ", ".join(
    "%s x%d" % ("%s-%s" % p, n) for p, n in sorted(adj_pairs.items())))
L.append("")
cand_rows = []
for hr, h in H_C:
    for dr, d in D_C:
        hd = pair_nc(h, d)
        for cr, c in C_C:
            for n1r, n1 in N1_C:
                cn1 = pair_nc(c, n1)
                for n2r, n2 in N2_C:
                    cn2 = pair_nc(c, n2)
                    nn = pair_nc(n1, n2)
                    marg = min(hd[0], cn1[0], cn2[0], nn[0])
                    cand_rows.append((marg, hr, dr, cr, n1r, n2r,
                                      hd, cn1, cn2, nn))
cand_rows.sort(key=lambda x: -x[0])
seen = set()
shown = 0
for m, hr, dr, cr, n1r, n2r, hd, cn1, cn2, nn in cand_rows:
    key = (hr, dr, cr, n1r, n2r)
    if key in seen:
        continue
    seen.add(key)
    L.append("    %-8s %-8s %-5s %-8s %-8s | H-D %5.2f | C-N1 %5.2f | C-N2 %5.2f | N1-N2 %5.2f | %s" % (
        hr.replace(".wav", ""), dr.replace(".wav", ""), cr.replace(".wav", ""),
        n1r.replace(".wav", ""), n2r.replace(".wav", ""),
        hd[0], cn1[0], cn2[0], nn[0],
        "DAT" if m >= NC_MIN else "TRUOT"))
    shown += 1
    if shown >= 16:
        break

out_txt = "\n".join(L)
(HERE / "g9_decide.txt").write_text(out_txt, encoding="utf-8")
(HERE / "g9_decide.json").write_text(json.dumps({
    "clone_f0": {"%s|%s" % k: v for k, v in CLONE.items()},
    "ref_f0": REF_F0,
    "adjacent_pairs": {"%s-%s" % k: v for k, v in adj_pairs.items()},
    "role_counts": dict(role_count),
    "full": full, "n_full": len(full), "n_full_dat": n_dat,
}, ensure_ascii=False, indent=1), encoding="utf-8")
print(out_txt)
print("\n-> .work/g9_decide.txt / .work/g9_decide.json")
