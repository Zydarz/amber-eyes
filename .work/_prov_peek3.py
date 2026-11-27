# -*- coding: utf-8 -*-
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
for kw in ("Caption", "mo_ta", "checklist", "MoTa", "KE_HOACH_TIKTOK"):
    hits = [e for e in prov if kw in json.dumps(e, ensure_ascii=False)]
    print(kw, len(hits))
    for e in hits[:3]:
        print("   ", json.dumps(e, ensure_ascii=False)[:300])
