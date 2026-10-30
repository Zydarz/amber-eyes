import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
vn = json.load(open(ROOT / ".work" / "script_tap02.json", encoding="utf-8"))
vn_map = {e["id"]: e for e in vn if e["kind"] == "LOI"}

target_eids = ["1.07", "2.04", "2.08", "4.05", "4.06", "4.07", "4.10", "4.11", "4.12", "5.06", "5.07", "5.08"]

for eid in target_eids:
    if eid in vn_map:
        e = vn_map[eid]
        print(f"\n=== Element {eid} ({e['role']}) — {len(e['sentences'])} sentences ===")
        for s in e["sentences"]:
            print(f"[{s['id']}] {s['text']}")
