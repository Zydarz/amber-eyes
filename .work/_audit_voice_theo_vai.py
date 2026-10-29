# -*- coding: utf-8 -*-
"""A: Vai -> voice_id that actually produced each VN episode, cross-referenced with the live catalog."""
import json
from collections import defaultdict
from pathlib import Path

WORK = Path(r"D:\TEST\Gax\Audi\.work")
live = json.loads((WORK / "_voice_list_live_20261027.json").read_text(encoding="utf-8-sig"))
names = {v["voice_id"]: v["voice_name"] for v in live["available_voices"]}

ROLE_VN = {"H": "Host", "D": "Dieu tra vien", "C": "Chuyen gia", "N1": "N1", "N2": "N2"}

mans = {
    "Tap01": "tts_manifest.json",
    "Tap02": "tts_manifest_t02.json",
    "Tap03": "tts_manifest_t03.json",
    "Tap04": "tts_manifest_t04.json",
    "Tap05": "tts_manifest_t05.json",
    "Tap06": "tts_manifest_t06.json",
    "Tap07": "tts_manifest_t07.json",
}

for ep, fn in mans.items():
    p = WORK / fn
    if not p.exists():
        print(f"--- {ep}: KHONG co {fn}")
        continue
    items = json.loads(p.read_text(encoding="utf-8"))
    per = defaultdict(lambda: defaultdict(int))
    for it in items:
        per[it["role"]][it["voice"]] += 1
    print(f"--- {ep} ({fn}) · {len(items)} cau")
    for role in sorted(per):
        for vid, n in per[role].items():
            nm = names.get(vid, "<<KHONG CO TRONG CATALOG LIVE>>")
            lang = vid.split("_")[0]
            print(f"   {ROLE_VN.get(role, role):15s} {vid:34s} ({nm})  lang-trong-id={lang:22s} {n:4d} cau")
    print()
