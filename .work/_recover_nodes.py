import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).resolve().parents[1] / ".work"
TTS = W / "tts_s_EN_t02"
man = json.loads((W / "tts_manifest_EN_t02.json").read_text(encoding="utf-8"))
order = [m["id"] for m in man]
pos = {sid: i for i, sid in enumerate(order)}
MISS = ["4.08#9"] + [f"4.10#{k}" for k in range(1, 11)] + [f"5.08#{k}" for k in range(1, 8)]
print("vị trí trong manifest (batch gốc = pos//10):")
for s in MISS:
    print(f"   {s:>9}  pos={pos[s]:>3}  batch gốc={pos[s]//10:>2}")

print("\nres_*.json hiện có:")
for f in sorted(TTS.glob("res_*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    code = d.get("code")
    si = d.get("success_items") or []
    ids = [x.get("file_name", "") for x in si[:3]]
    print(f"   {f.name}  code={code}  success={len(si)}  {ids}")

# node_id còn sống cho các câu bị thiếu?
print("\ntìm node_id cho 18 câu thiếu trong res_*:")
found = {}
for f in sorted(TTS.glob("res_*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    for x in d.get("success_items") or []:
        stem = x.get("file_name", "").rsplit(".", 1)[0]
        parts = stem.lstrip("s").split("_")
        sid = f"{parts[0]}.{parts[1]}#{int(parts[2])}" if len(parts) == 3 else stem
        if sid in MISS:
            found[sid] = (f.name, x.get("node_id"))
for s in MISS:
    print(f"   {s:>9}  {found.get(s, 'KHÔNG CÒN trong res_*')}")
