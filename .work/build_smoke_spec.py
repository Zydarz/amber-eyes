"""Sinh spec + payload cho SMOKE TEST 2 GPU (12 file).

Dung de chung minh duong chay 2 tien trinh / 2 GPU + merge + catch-up truoc khi
sinh 406 file that cua Tap 02. 6 cau, du ca 5 vai, co 1 cau co the emotion.
"""
import json
import pathlib
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent          # .work/
DS = HERE / "kaggle_higgs" / "dataset_voxcpm2"

ROLE_MAP = {k: v for k, v in json.loads(
    (HERE / "g9_role_map.json").read_text(encoding="utf-8-sig")).items()
    if not k.startswith("_") and isinstance(v, str) and v.endswith(".wav")}

GEN_PARAMS = {
    "temperature": 0.8,
    "temp_by_role": {"H": 0.8, "D": 0.8, "C": 0.8, "N1": 0.8, "N2": 0.8},
    "top_p": 0.95,
    "top_k": 50,
    "max_new_tokens": 1196,
    "sample_rate": 24000,
    "fade_in_ms": 30,
    "seed_scheme": "sha256(id|role|ref|temp|vN) -> int(hex[:8],16)",
}

payload = json.loads((DS / "higgs_payload_t02.json").read_text(encoding="utf-8-sig"))
items = payload["items"]

# 1 cau cho moi vai (uu tien cau co the emotion cho 1 vai) + 1 cau thu
chosen, seen_roles = [], set()
for it in items:
    if it["role"] not in seen_roles:
        chosen.append(it)
        seen_roles.add(it["role"])
    if len(chosen) == 5:
        break
# them 1 cau co the emotion (kiem §5 + the de muc do)
for it in items:
    if it.get("emotion_tag") and it not in chosen:
        chosen.append(it)
        break
# phai du 5 vai
assert seen_roles == {"H", "D", "C", "N1", "N2"}, seen_roles

smoke_items = []
for it in chosen:
    p = dict(it)
    p["ref_wav"] = ROLE_MAP[it["role"]]
    p["ref_txt"] = p["ref_wav"].replace(".wav", ".txt")
    smoke_items.append(p)

spec = {
    "episode": "02",
    "mode": "smoke",
    "purpose": "Kiem duong 2 GPU + merge + catch-up truoc luot san xuat that",
    "gen_params": GEN_PARAMS,
    "variants": [0, 1],
    "items": [it["id"] for it in smoke_items],
}
smoke_payload = {
    "episode": "02",
    "model": payload.get("model", "bosonai/higgs-tts-3-4b"),
    "role_ref": {r: {"wav": w, "txt": w.replace(".wav", ".txt")}
                 for r, w in ROLE_MAP.items()},
    "items": smoke_items,
}

(DS / "prod_spec_smoke.json").write_text(
    json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
(DS / "higgs_payload_smoke.json").write_text(
    json.dumps(smoke_payload, ensure_ascii=False, indent=1), encoding="utf-8")

print("smoke: %d cau x %d ban = %d file" % (
    len(smoke_items), len(spec["variants"]), len(smoke_items) * len(spec["variants"])))
for it in smoke_items:
    print("   %-8s %-3s %-16s %s" % (it["id"], it["role"], it["ref_wav"],
                                     (it.get("emotion_tag") or "-")))
print("theo vai:", dict(Counter(it["role"] for it in smoke_items)))
print("-> ", DS)
