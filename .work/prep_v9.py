"""PILOT v9 — do clone Higgs cho giong mau MOI cua vai D (khan tram) va C (trong sac).

Input : assets/voice_ref_voxcpm2_dc/, assets/voice_ref_voxcpm2_dc2/ (VoxCPM2, 30/10/2026)
        .work/kaggle_higgs/higgs_payload_t02.json (cau that Tap 02)
Output: .work/kaggle_higgs/dataset_voxcpm2/  <TEN>.wav/.txt (8 clip) + pilot_spec_v9.json + pilot_payload_v9.json

Moi clip x 12 cau CUA DUNG VAI (8 neutral + sad/fearful/surprised -> kiem G8) x 2 ban.
Ten clip ngan vi dc/ va dc2/ trung ten file.

Usage: python .work/prep_v9.py [--mode v9|v10]

v10 (30/10/2026): vong 3 giong D (seed 7, 88-90 Hz) + C2_AB03 lam doi chung D~C.
"""
import argparse
import json
import pathlib
import shutil
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
DS = HERE / "kaggle_higgs" / "dataset_voxcpm2"

CLIPS_V9 = [  # (ten tren Kaggle, vai, file nguon, ly do)
    ("D1_VG", "D", "voice_ref_voxcpm2_dc/D_NEW_vlow-gravel_t01", "D vong 1 vlow-gravel seed 42, F0 97.6/90.0"),
    ("D1_DS", "D", "voice_ref_voxcpm2_dc/D_NEW_deep-smoker_t01", "D vong 1 deep-smoker seed 42, F0 96.4/98.7"),
    ("D2_VG", "D", "voice_ref_voxcpm2_dc2/D_NEW_vlow-gravel_t01", "D vong 2 vlow-gravel seed 7, F0 89.4/90.6"),
    ("D2_DS", "D", "voice_ref_voxcpm2_dc2/D_NEW_deep-smoker_t01", "D vong 2 deep-smoker seed 7, F0 97.0/98.7"),
    ("C2_AB05", "C", "voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t05", "C alto-brisk seed 256, F0 200/199, 4.14 am/s"),
    ("C2_LE03", "C", "voice_ref_voxcpm2_dc2/C_NEW_lecture_t03", "C lecture seed 77, F0 216/215, 4.40 am/s"),
    ("C2_AB03", "C", "voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03", "C alto-brisk seed 77, F0 208/210, 4.15 am/s"),
    ("C2_LE02", "C", "voice_ref_voxcpm2_dc2/C_NEW_lecture_t02", "C lecture seed 13, F0 213/213, 4.01 am/s"),
]
CLIPS_V10 = [
    ("D3_SH", "D", "voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02", "D vong 3 subbass-husky seed 7, F0 88.4/89.1"),
    ("D3_BG", "D", "voice_ref_voxcpm2_dc3/D_NEW_bass-gravel_t02", "D vong 3 bass-gravel seed 7, F0 89.4/89.4"),
    ("D3_LG", "D", "voice_ref_voxcpm2_dc3/D_NEW_low-growl_t02", "D vong 3 low-growl seed 7, F0 90.4/90.7"),
    ("C2_AB03", "C", "voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03", "C da chon (pilot v9) - doi chung D~C"),
]
ap = argparse.ArgumentParser()
ap.add_argument("--mode", default="v9", choices=["v9", "v10"])
MODE = ap.parse_args().mode
CLIPS = {"v9": CLIPS_V9, "v10": CLIPS_V10}[MODE]
TAG = {"v9": "P9", "v10": "P10"}[MODE]
EMO_QUOTA = {"neutral": 8, "sad": 2, "fearful": 1, "surprised": 1}

items_src = json.loads((HERE / "kaggle_higgs" / "higgs_payload_t02.json")
                       .read_text(encoding="utf-8-sig"))["items"]


def pick(role):
    pool = sorted([i for i in items_src if i["role"] == role], key=lambda x: x["id"])
    out = []
    for emo, n in EMO_QUOTA.items():
        c = [i for i in pool if i["emotion"] == emo]
        if not c:
            continue
        step = len(c) / n
        out += [c[int(k * step)] for k in range(min(n, len(c)))]
    while len(out) < 12:                       # bu bang neutral neu thieu cam xuc
        out.append(next(i for i in pool if i["emotion"] == "neutral" and i not in out))
    return out


sent = {r: pick(r) for r in sorted({c[1] for c in CLIPS}, reverse=True)}
for r, L in sent.items():
    print(r, len(L), dict(Counter(i["emotion"] for i in L)))

items = []
for name, role, src, why in CLIPS:
    for ext in (".wav", ".txt"):
        shutil.copy2(ROOT / "assets" / (src + ext), DS / (name + ext))
    for j, s in enumerate(sent[role]):
        items.append({
            "id": "%s_%s__%s__%d" % (TAG, role, name, j),
            "role": role, "ref_wav": name + ".wav", "ref_txt": name + ".txt",
            "text_plain": s["text_plain"], "text": s["text"],
            "emotion": s["emotion"], "emotion_tag": s.get("emotion_tag", ""),
            "src_id": s["id"], "why": why,
        })

GEN = json.loads((DS / "pilot_spec_v8.json").read_text(encoding="utf-8"))["gen_params"]
spec = {"episode": "02", "mode": "pilot_" + MODE,
        "purpose": "F0 clone + CER + G8 cho giong mau moi D (khan tram) / C (trong sac)",
        "gen_params": GEN, "variants": [0, 1], "items": [i["id"] for i in items]}
payload = {"episode": "02", "model": "bosonai/higgs-tts-3-4b", "items": items,
           "role_ref": {}}
(DS / f"pilot_spec_{MODE}.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
(DS / f"pilot_payload_{MODE}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"pilot {MODE}: " + "%d item x 2 ban = %d file" % (len(items), 2 * len(items)))
print("theo clip:", dict(Counter(i["ref_wav"] for i in items)))
