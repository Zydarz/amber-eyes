import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(r"D:\TEST\Gax\Audi\.work")
TTS = W / "tts_s_EN_t02"
man = json.loads((W / "tts_manifest_EN_t02.json").read_text(encoding="utf-8"))
D = [m["id"] for m in man if m["role"] == "D"]
pos = {m["id"]: i for i, m in enumerate(man)}

nodes = {}
for f in sorted(TTS.glob("res_*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    if d.get("code") not in (0, None):
        continue
    for x in d.get("success_items") or []:
        stem = x.get("file_name", "").rsplit(".", 1)[0]
        p = stem.lstrip("s").split("_")
        if len(p) != 3:
            continue
        sid = f"{p[0]}.{p[1]}#{int(p[2])}"
        nodes.setdefault(sid, []).append((f.name, x.get("node_id")))

have = [s for s in D if s in nodes]
print(f"vai D: {len(D)} câu · có node_id trong res_*: {len(have)} · thiếu: {len(D) - len(have)}")
for s in D:
    mark = "OK " if s in nodes else "-- "
    print(f"  {mark}{s:>9}  pos={pos[s]:>3}  {nodes.get(s, [('-','-')])[0][0]}")
