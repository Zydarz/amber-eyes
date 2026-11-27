# -*- coding: utf-8 -*-
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
for e in prov:
    if e.get("file") == "02_SAN_XUAT/TIKTOK/Tap01/Caption_TK1.txt":
        print(json.dumps(e, ensure_ascii=False, indent=1))
for e in prov:
    if e.get("file") == "02_SAN_XUAT/TIKTOK/Tap01/MoTa_Dai_TK1.txt":
        print(json.dumps(e, ensure_ascii=False, indent=1))
for e in prov:
    if e.get("file") == "02_SAN_XUAT/TIKTOK/Tap04/TK1_video.mp4":
        print(json.dumps(e, ensure_ascii=False, indent=1))
