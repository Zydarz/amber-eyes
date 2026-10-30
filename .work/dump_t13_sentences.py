import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

data = json.loads((WORK / "script_tap13.json").read_text(encoding="utf-8"))

out = []
for item in data:
    if item.get("kind") == "LOI":
        act = item.get("act")
        tid = item.get("id")
        role = item.get("role")
        for s in item.get("sentences", []):
            out.append(f"Act {act} | {tid} ({role}) | {s['id']}: {s['text']}")

(WORK / "sentences_tap13.txt").write_text("\n".join(out), encoding="utf-8")
print(f"Dumped {len(out)} sentences to sentences_tap13.txt")
