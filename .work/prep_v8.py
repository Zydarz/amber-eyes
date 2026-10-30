"""Dong bo clip TD-PSOLA + bien the TRIM vao refs.json va dataset Kaggle.

Input : assets/voice_ref_voxcpm2_g9/W6_LOW_{TRIM,PS15,PS20,PS25,PS30}.{wav,txt}
        .work/g9_psola_shift.json  (so do)
Output: assets/voice_ref_voxcpm2_g9/refs.json  (them 5 muc)
        .work/kaggle_higgs/dataset_voxcpm2/   (copy wav + txt)
        .work/kaggle_higgs/dataset_voxcpm2/dataset-metadata.json (resources)

Usage: python .work/prep_v8.py
"""
import json
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
G9 = ROOT / "assets" / "voice_ref_voxcpm2_g9"
DS = HERE / "kaggle_higgs" / "dataset_voxcpm2"

shift = json.loads((HERE / "g9_psola_shift.json").read_text(encoding="utf-8-sig"))
meas = {v["name"]: v for v in shift["variants"]}
print("so do tu g9_psola_shift.json:", list(meas))

# CER cua clip (do bang ASR tren clip goc, .work/cer_ref_clips.json)
ASR = {}
pj = HERE / "cer_ref_clips.json"
if pj.exists():
    for r in json.loads(pj.read_text(encoding="utf-8-sig")):
        ASR[r["clip"]] = r

refs_p = G9 / "refs.json"
refs = json.loads(refs_p.read_text(encoding="utf-8-sig"))
base = refs["W6_LOW"]

NEW = [
    ("W6_LOW_TRIM", "trim-only", 0.0, "cat 0.80 s doan im lang giua cau (5.76-6.56 s)"),
    ("W6_LOW_PS15", "psola", -1.5, "TD-PSOLA -1.5 nua cung"),
    ("W6_LOW_PS20", "psola", -2.0, "TD-PSOLA -2.0 nua cung"),
    ("W6_LOW_PS25", "psola", -2.5, "TD-PSOLA -2.5 nua cung"),
    ("W6_LOW_PS30", "psola", -3.0, "TD-PSOLA -3.0 nua cung"),
]

meta_p = DS / "dataset-metadata.json"
meta = json.loads(meta_p.read_text(encoding="utf-8-sig"))
have = {r["path"] for r in meta.get("resources", [])}

for name, kind, st, desc in NEW:
    m = meas.get(name)
    if not m:
        print("!! thieu so do cho", name)
        continue
    a = ASR.get(name, {})
    cer_txt = ""
    if a.get("cer") is not None:
        cer_txt = ("ASR tren clip goc: CER %.2f%% / bo danh tu rieng %.2f%%"
                   % (100 * a["cer"], 100 * (a.get("cer_prop") or 0)))
    e = dict(base)
    e["seconds"] = m["dur"]
    e["f0_median_hz"] = m["f0_ac"]
    e["f0_ac_hz"] = m["f0_ac"]
    e["f0_pp2_hz"] = m["f0_pp2"]
    e["source_file"] = "assets/voice_ref_voxcpm2_g9/%s.wav" % name
    e["reference_file"] = "assets/voice_ref_voxcpm2_g9/%s.wav" % name
    e["variant"] = ("trim-only" if kind == "trim-only" else "psola%+0.1f_st" % st)
    e["processing"] = ("cat im lang giua cau (khong doi cao do)" if kind == "trim-only"
                       else "TD-PSOLA (giai thuoc so) + resample FFT, giu nguyen thoi luong")
    e["derived_from"] = "W6_LOW.wav"
    e["role"] = "N1_CANDIDATE"
    e["why"] = ("Bien the de vai N1 (nu) dat G9 >= 4 nua cung. Kiem clone tren GPU (pilot v8).")
    e["notes"] = [
        desc,
        "F0 do %.1f Hz (AC tho) / %.1f Hz (AC chuan hoa)" % (m["f0_ac"], m["f0_pp2"]),
        cer_txt,
        "Khong dung phase vocoder: pilot v6 cho thay bien the S25-S40 (phase vocoder) "
        "co CER clone 9,5-12,5% trong khi clip goc ASR 0,00%",
    ]
    e.pop("f0_target_hz", None)
    refs[name] = e
    # copy sang dataset
    for ext in (".wav", ".txt"):
        src = G9 / (name + ext)
        if src.exists():
            shutil.copy2(src, DS / (name + ext))
            rp = name + ext
            if rp not in have:
                meta.setdefault("resources", []).append(
                    {"path": rp, "description": "%s - %s, F0 %.1f Hz" % (name, desc, m["f0_ac"])})
                have.add(rp)
    print("  %-14s F0 %6.1f / %6.1f  dur %5.2f  %s" % (name, m["f0_ac"], m["f0_pp2"], m["dur"], cer_txt))

refs_p.write_text(json.dumps(refs, ensure_ascii=False, indent=1), encoding="utf-8")
meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("\n-> %s (%d muc)" % (refs_p, len(refs)))
print("-> %s (%d resources)" % (meta_p, len(meta.get("resources", []))))
