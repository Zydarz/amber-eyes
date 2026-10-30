"""Cap nhat assets/voice_ref_voxcpm2_g9/refs.json — ghi F0 THAT cua 4 clip moi
+ 5 bien the hao cao do, kem ghi chu trung thuc (khong ghi "muc tieu" nhu da dat).

Nguyen tac: refs.json la HOA SO TON TAI — chi ghi so do. Neu F0 do khong dung
dai muc tieu thi ghi ro trong `notes`, KHONG ghi con so uoc luong.
"""
import json
import pathlib
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from voice_audition import f0_median as f0_ac  # noqa: E402

G9 = ROOT / "assets" / "voice_ref_voxcpm2_g9"
REFS_P = G9 / "refs.json"
DS = HERE / "kaggle_higgs" / "dataset_voxcpm2"


def f0_p2(x, sr, fmin=70.0, fmax=400.0):
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


def measure(name):
    p = G9 / (name + ".wav")
    a, sr = read_wav(p)
    dur = len(a) / sr
    peak = float(np.max(np.abs(a)))
    return {"seconds": round(dur, 2), "sample_rate": sr, "channels": 1,
            "f0_ac": round(f0_ac(a, sr), 1), "f0_pp2": round(f0_p2(a, sr), 1),
            "peak_dbfs": round(20 * np.log10(peak + 1e-12), 2)}


refs = json.loads(REFS_P.read_text(encoding="utf-8-sig"))

# ---- 1) cap nhat 4 clip goc voi so do that ------------------------------
TARGETS = {
    "M_LOW": (70, 86),
    "M_HIGH": (168, 182),
    "W6_LOW": (148, 162),
    "W5_HIGH": (258, 276),
}
for name, (lo, hi) in TARGETS.items():
    m = measure(name)
    e = refs.get(name)
    if not e:
        print("!! thieu entry", name)
        continue
    # loay cac ghi chu CU ve F0/thoi luong (se ghi lai bang so do that)
    notes = [n for n in (e.get("notes") or [])
             if not (n.upper().startswith("F0")
                     or "THOI LUONG" in n.upper()
                     or "THOI_LUONG" in n.upper())]
    # giu duy nhat, theo thu tu
    seen_n = set()
    notes = [n for n in notes if not (n in seen_n or seen_n.add(n))]
    if not (lo <= m["f0_ac"] <= hi):
        notes.append("F0 do %.1f Hz (AC tho) ngoai dai muc tieu %d-%d Hz" % (
            m["f0_ac"], lo, hi))
    if not (16.0 <= m["seconds"] <= 28.0):
        notes.append("THOI_LUONG %.2fs ngoai [16,28]s" % m["seconds"])
    e["seconds"] = m["seconds"]
    e["sample_rate"] = m["sample_rate"]
    e["channels"] = m["channels"]
    e["f0_median_hz"] = m["f0_ac"]
    e["f0_ac_hz"] = m["f0_ac"]
    e["f0_pp2_hz"] = m["f0_pp2"]
    e["peak_dbfs"] = m["peak_dbfs"]
    e["f0_target_hz"] = [lo, hi]
    e["notes"] = notes
    print("%-9s dur=%6.2f  F0_ac=%6.1f  F0_pp2=%6.1f  peak=%6.1f dBFS  notes=%s" % (
        name, m["seconds"], m["f0_ac"], m["f0_pp2"], m["peak_dbfs"], notes or ["-"]))

# ---- 2) them 5 bien the hao cao do ---------------------------------------
shift_info = json.loads((HERE / "g9_shift_clip.json").read_text(encoding="utf-8-sig"))
base = refs["W6_LOW"]
for v in shift_info["variants"]:
    name = v["name"]
    m = measure(name)
    e = dict(base)
    e["role"] = "N1_CANDIDATE"
    e["variant"] = "shift-%0.1f_st" % v["semitones"]
    e["seconds"] = m["seconds"]
    e["sample_rate"] = m["sample_rate"]
    e["channels"] = m["channels"]
    e["f0_median_hz"] = m["f0_ac"]
    e["f0_ac_hz"] = m["f0_ac"]
    e["f0_pp2_hz"] = m["f0_pp2"]
    e["peak_dbfs"] = m["peak_dbfs"]
    e["f0_target_hz"] = [140, 165]
    e["derived_from"] = "W6_LOW.wav"
    e["processing"] = "phase vocoder (time-stretch + resample), giu nguyen thoi luong"
    e["reference_file"] = str((G9 / (name + ".wav")).relative_to(ROOT)).replace("\\", "/")
    e["why"] = ("Bien the hao cao do cua W6_LOW de vai N1 (nu) dat G9 >= 4 nua cung "
                "voi ca C (205.1 Hz) va N2 (275.9 Hz). Clone N1 phai <= 162.8 Hz (AC tho).")
    e["notes"] = [
        "Hao %0.1f nua cung so voi W6_LOW (x%0.4f) bang phase vocoder" % (
            abs(v["semitones"]), v["factor"]),
        "F0 do %0.1f Hz (AC tho) / %0.1f Hz (AC chuan hoa)" % (m["f0_ac"], m["f0_pp2"]),
        "Clone du doan %0.1f-%0.1f Hz (AC tho) theo ti le drift 0.95-1.10" % (
            v["pred_clone_ac"][0], v["pred_clone_ac"][1]),
        "Da cat 0.80s doan im lang de thoi luong <= 28s (khong mat chu)",
    ]
    refs[name] = e
    print("%-13s dur=%6.2f  F0_ac=%6.1f  F0_pp2=%6.1f  peak=%6.1f dBFS  (-%.1f st)" % (
        name, m["seconds"], m["f0_ac"], m["f0_pp2"], m["peak_dbfs"], abs(v["semitones"])))

REFS_P.write_text(json.dumps(refs, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n-> %s (%d muc)" % (REFS_P, len(refs)))

# ---- 3) dong bo sang dataset Kaggle -------------------------------------
DS.mkdir(parents=True, exist_ok=True)
for name in list(TARGETS) + [v["name"] for v in shift_info["variants"]]:
    for ext in (".wav", ".txt"):
        src = G9 / (name + ext)
        dst = DS / (name + ext)
        dst.write_bytes(src.read_bytes())
print("-> dataset: %d file clip da dong bo" % (
    2 * (len(TARGETS) + len(shift_info["variants"]))))
(DS / "refs.json").write_bytes(REFS_P.read_bytes())
print("-> dataset: refs.json da dong bo")
