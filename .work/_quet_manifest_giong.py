# -*- coding: utf-8 -*-
"""D: Quet TAT CA manifest (VN/EN/JA/KO) -> vai nao dung voice_id nao, voi nhan giong."""
import json
from collections import defaultdict
from pathlib import Path

WORK = Path(__file__).resolve().parents[1] / ".work"
live = json.loads((WORK / "_voice_list_live_20261027.json").read_text(encoding="utf-8-sig"))
names = {v["voice_id"]: v["voice_name"] for v in live["available_voices"]}

# nhan giong suy tu ten giong trong catalog (ten deu la tieng Anh)
def gender(vid):
    n = names.get(vid, "")
    low = (vid + " " + n).lower()
    male = ("man", "boy", "male", "gentleman", "guy", "qingse", "book_female_1" if False else "zzz")
    fem = ("woman", "girl", "female", "lady", "queen", "sir", "hostess")
    if any(k in low for k in ("man", "boy", "male", "gentleman")):
        return "NAM"
    if any(k in low for k in ("woman", "girl", "female", "lady", "queen")):
        return "NU"
    return "?"

ROLE_VN = {"H": "Host", "D": "D.trai", "C": "C.gia", "N1": "N1", "N2": "N2"}
GROUPS = {
    "VN": ["tts_manifest.json", "tts_manifest_t02.json", "tts_manifest_t03.json",
           "tts_manifest_t04.json", "tts_manifest_t05.json", "tts_manifest_t06.json",
           "tts_manifest_t07.json"],
    "EN": ["tts_manifest_EN.json", "tts_manifest_EN_t02.json", "tts_manifest_EN_t03.json",
           "tts_manifest_EN_t04.json", "tts_manifest_EN_t05.json"],
    "JA": ["tts_manifest_JA.json", "tts_manifest_JA_t02.json"],
    "KO": ["tts_manifest_KO.json"],
}

for lang, files in GROUPS.items():
    print(f"########## BAN {lang} ##########")
    for fn in files:
        p = WORK / fn
        if not p.exists():
            continue
        items = json.loads(p.read_text(encoding="utf-8"))
        per = defaultdict(lambda: defaultdict(int))
        for it in items:
            per[it["role"]][it["voice"]] += 1
        ep = fn.replace("tts_manifest_", "").replace(".json", "")
        print(f"-- {ep} ({len(items)} cau)")
        for role in sorted(per):
            for vid, n in sorted(per[role].items(), key=lambda x: -x[1]):
                nm = names.get(vid, "khong trong catalog live")
                print(f"   {ROLE_VN.get(role, role):8s} {vid:32s} {gender(vid):3s} ({nm}) {n:4d} cau")
        # dem so NAM trong 3 vai chinh
        main = [r for r in ("H", "D", "C") if r in per]
        n_main = len(main)
        n_male = 0
        for r in main:
            top = max(per[r].items(), key=lambda x: x[1])[0]
            if gender(top) == "NAM":
                n_male += 1
        print(f"   => 3 vai chinh: {n_main} vai, {n_male} gioi NAM")
        print()
