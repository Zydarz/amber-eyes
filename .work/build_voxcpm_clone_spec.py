"""Spec cho phep thu VoxCPM2 CHE DO CLONE tren Mac — so cong bang voi Higgs (pilot v10 + san xuat 31/10).

Cung giong mau (H.wav / D3_SH / C2_AB03), cung cau (12 cau/vai, chon nhu prep_v9.pick), 2 ban/cau,
van ban da BO moi the <|...|> (khop quyet dinh 31/10/2026).

Output: .work/voxcpm_clone_spec.json  (Mac doc file nay qua .work/voxcpm_clone_pilot.py)
Usage : python .work/build_voxcpm_clone_spec.py
"""
import hashlib
import json
import pathlib
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent

REFS = {  # vai -> (ten ngan, wav trong repo; .txt cung ten)
    "H": ("H", "assets/voice_ref_voxcpm2/H.wav"),
    "D": ("D3_SH", "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav"),
    "C": ("C2_AB03", "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.wav"),
}
EMO_QUOTA = {"neutral": 8, "sad": 2, "fearful": 1, "surprised": 1}   # giong prep_v9.py
RE_TAG = re.compile(r"<\|[^|]+\|>\s*")

src = json.loads((HERE / "kaggle_higgs" / "higgs_payload_t02.json").read_text(encoding="utf-8-sig"))["items"]


def pick(role):
    pool = sorted([i for i in src if i["role"] == role], key=lambda x: x["id"])
    out = []
    for emo, n in EMO_QUOTA.items():
        c = [i for i in pool if i["emotion"] == emo]
        if not c:
            continue
        step = len(c) / n
        out += [c[int(k * step)] for k in range(min(n, len(c)))]
    while len(out) < 12:
        out.append(next(i for i in pool if i["emotion"] == "neutral" and i not in out))
    return out


items = []
for role, (name, wav) in REFS.items():
    for s in pick(role):
        text = RE_TAG.sub("", s["text"]).strip()
        for v in (0, 1):
            seed = int(hashlib.sha256(f"{s['id']}|{role}|{name}|v{v}".encode()).hexdigest()[:8], 16)
            items.append({
                "key": f"{s['id']}__{role}__{name}__s{v}", "id": s["id"], "role": role,
                "ref_name": name, "ref_wav": wav, "ref_txt": wav.replace(".wav", ".txt"),
                "text": text, "text_plain": s.get("text_plain", text), "emotion": s["emotion"],
                "variant": v, "seed": seed,
                "file": f"{s['id'].replace('#', '_').replace('.', '_')}_{role}_{name}_s{v}.wav",
            })

for _, wav in REFS.values():
    for ext in (".wav", ".txt"):
        assert (HERE.parent / wav.replace(".wav", ext)).exists(), wav
assert not any("<|" in i["text"] for i in items)
spec = {"purpose": "VoxCPM2 clone vs Higgs — cung giong mau, cung cau, 2 ban/cau",
        "created": "2026-10-31", "n_items": len(items), "items": items}
(HERE / "voxcpm_clone_spec.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
print("items:", len(items), dict(Counter(i["role"] for i in items)))
print("cam xuc:", dict(Counter(i["emotion"] for i in items if i["variant"] == 0)))
