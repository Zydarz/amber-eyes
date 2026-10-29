# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"

ja_acting = json.loads((WORK / "acting_tap01_JA.json").read_text(encoding="utf-8"))
ko_script = json.loads((WORK / "script_tap01_KO.json").read_text(encoding="utf-8"))

ko_acting = {
    "_doc": "Diễn xuất từng câu cho bản tiếng Hàn (Tap01_KO). Kế thừa cảm xúc từ bản chuẩn Tap 01; cao độ = 0 (G5); speed clamp G4."
}

# Lấy mọi sentence id từ ko_script
for e in ko_script:
    if e.get("kind") == "LOI":
        for s in e.get("sentences", []):
            sid = s["id"]
            if sid in ja_acting:
                emo, sp, pitch, aside = ja_acting[sid]
                # Pitch luôn = 0 theo G5
                ko_acting[sid] = [emo, sp, 0, None]
            else:
                ko_acting[sid] = ["neutral", 0.0, 0, None]

out_p = WORK / "acting_tap01_KO.json"
out_p.write_text(json.dumps(ko_acting, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Created {out_p.name} with {len(ko_acting)-1} sentences.")
