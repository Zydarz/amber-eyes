#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FIX 4.08#6 — sinh lai 1 cau tren Kaggle cho khop kich ban.

Ly do: acting_tap02_EN.json giu 1 dong `alt` cu ("snowshoe footprint") ghi de chu
trong kich ban ("snow boot impression") -> audio doc sai, phu de lech.

Buoc:
  1. backup + va acting_tap02_EN.json (alt -> chu kich ban)
  2. export_higgs_payload.py  -> payload nguon dung chu moi
  3. ghi SPEC + PAYLOAD 1 cau vao dataset (prod_spec_EN_t02_f1 / higgs_payload_EN_t02_f1)
  4. tao notebook 1 cau tu notebook prod da push (doi ten file + ten OUT)

Chay: AE_LANG=en AE_EP=02 py -3 .work/_fix_4086_t02en.py
"""
import json
import os
import pathlib
import re
import shutil
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
KG = HERE / "kaggle_higgs"
DS = KG / "dataset_voxcpm2_en"
ACTING = HERE / "acting_tap02_EN.json"
NB_SRC = KG / "_push_prod_EN_t02" / "higgs_prod_EN_t02_kaggle.ipynb"
NB_OUT = KG / "_push_fix4086" / "higgs_fix4086_kaggle.ipynb"

OLD = "snowshoe footprint"
NEW = "snow boot impression"
SID = "4.08#6"
SPEC_NAME = "prod_spec_EN_t02_f1.json"
PAYLOAD_NAME = "higgs_payload_EN_t02_f1.json"

os.environ["AE_LANG"] = "en"
os.environ["AE_EP"] = "02"

# ---------------------------------------------------------------- 1. acting
ac = json.loads(ACTING.read_text(encoding="utf-8-sig"))
alt = ac[SID][3]
if NEW in alt:
    print("acting %s da duoc patch truoc do -> bo qua" % SID)
else:
    assert OLD in alt, "alt khong con cum %r: %r" % (OLD, alt)
    bak = HERE / "_cu" / ("acting_tap02_EN_pre_fix4086_%s.json" % time.strftime("%Y%m%d_%H%M%S"))
    shutil.copy2(ACTING, bak)
    ac[SID][3] = alt.replace(OLD, NEW)
    ACTING.write_text(json.dumps(ac, ensure_ascii=False, indent=1), encoding="utf-8")
    print("BACKUP acting ->", bak.name)
    print("PATCH  acting %s: %r -> %r" % (SID, OLD, NEW))

# ---------------------------------------------------------------- 2. payload nguon
import export_higgs_payload as EP  # noqa: E402

new_payload = EP.build()
old_payload = json.loads(EP.OUT.read_text(encoding="utf-8-sig"))
oi = {i["id"]: i for i in old_payload["items"]}
ni = {i["id"]: i for i in new_payload["items"]}
print("\n--- payload moi vs cu ---")
for f in ("role", "text_plain", "text", "emotion", "speed", "display", "ref_wav"):
    diff = [k for k in oi if k in ni and str(oi[k][f]).strip() != str(ni[k][f]).strip()]
    print("  khac %-10s %d  %s" % (f, len(diff), diff[:6]))
assert set(oi) == set(ni), "tap cu khac tap moi"

# ---------------------------------------------------------------- 3. spec + payload 1 cau
item = ni[SID]
src_spec = json.loads((DS / "prod_spec_EN_t02.json").read_text(encoding="utf-8-sig"))
spec = {
    "episode": "02", "mode": "prod",
    "purpose": "FIX 4.08#6: doc 'snow boot impression' cho khop kich ban (thay 'snowshoe footprint')",
    "gen_params": src_spec["gen_params"],
    "variants": src_spec.get("variants", [0, 1]),
    "variants_by_item": {SID: src_spec.get("variants_by_item", {}).get(SID, [0, 1, 2])},
    "items": [SID],
}
# --- ghep clip tham chieu theo role map (giong build_spec.py dong 290-302) ---
import higgs_paths as P  # noqa: E402

_role_raw = json.loads(P.ROLE_MAP.read_text(encoding="utf-8-sig"))
ROLE_MAP = {k: v for k, v in _role_raw.items()
            if not k.startswith("_") and isinstance(v, str) and v.endswith(".wav")}
print("\nrole map EN:", ROLE_MAP)
for _c in ROLE_MAP.values():
    P.check_ref_lang(_c)

item = dict(item)
item["ref_wav"] = ROLE_MAP[item["role"]]
item["ref_txt"] = ROLE_MAP[item["role"]].replace(".wav", ".txt")
assert (DS / item["ref_wav"]).exists(), "thieu clip %s" % item["ref_wav"]
assert (DS / item["ref_txt"]).exists(), "thieu txt %s" % item["ref_txt"]

# giong build_spec.py: bo <|emotion:...|> neu role map tat cam
if _role_raw.get("_emotion_tags") is False:
    item["text"] = re.sub(r"<\|emotion:[^|]+\|>\s*", "", item["text"]).strip()
    item["emotion_tag"] = ""

pay = {
    "episode": "02", "lang": "en", "model": "bosonai/higgs-tts-3-4b",
    "ref_dir": P.REF_DIR,
    "role_ref": {r: {"wav": w, "txt": w.replace(".wav", ".txt")}
                 for r, w in ROLE_MAP.items()},
    "items": [item],
}

# --- cap nhat payload NGUON (higgs_payload_EN_t02.json) cho khop ---
EP.OUT.write_text(json.dumps(new_payload, ensure_ascii=False, indent=1), encoding="utf-8")
print("payload nguon cap nhat ->", EP.OUT.name)
(DS / SPEC_NAME).write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
(DS / PAYLOAD_NAME).write_text(json.dumps(pay, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n=== SPEC 1 cau ===")
print(json.dumps(spec, ensure_ascii=False, indent=1))
print("=== ITEM ===")
print(json.dumps(item, ensure_ascii=False, indent=1))
print("\nghi ->", DS / SPEC_NAME)
print("ghi ->", DS / PAYLOAD_NAME)

# ---------------------------------------------------------------- 4. notebook
nb = json.loads(NB_SRC.read_text(encoding="utf-8-sig"))
src = json.dumps(nb, ensure_ascii=False)
n_before = src.count("prod_spec_EN_t02.json")
src = src.replace("prod_spec_EN_t02.json", SPEC_NAME)
src = src.replace("higgs_payload_EN_t02.json", PAYLOAD_NAME)
src = src.replace("out_higgs_prod_EN_t02", "out_higgs_fix4086")
nb = json.loads(src)
NB_OUT.parent.mkdir(parents=True, exist_ok=True)
NB_OUT.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print("\nnotebook ->", NB_OUT, NB_OUT.stat().st_size, "bytes")
print("  spec tro  %d lan -> %s" % (n_before, SPEC_NAME))
print("  payload  -> %s" % PAYLOAD_NAME)
