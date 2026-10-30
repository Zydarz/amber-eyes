import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
vn = json.load(open(ROOT / ".work" / "script_tap02.json", encoding="utf-8"))
en = json.load(open(ROOT / ".work" / "temp_verify_en_t02.json", encoding="utf-8"))

vn_map = {e["id"]: e for e in vn if e["kind"] == "LOI"}
en_map = {e["id"]: e for e in en if e["kind"] == "LOI"}

diff_elements = []
for eid in vn_map:
    vn_s = vn_map[eid]["sentences"]
    en_s = en_map.get(eid, {}).get("sentences", [])
    if len(vn_s) != len(en_s):
        diff_elements.append((eid, vn_map[eid]["role"], len(vn_s), len(en_s)))

print("Elements with different sentence counts:")
for eid, role, vn_c, en_c in diff_elements:
    print(f"  {eid} ({role}): VN has {vn_c}, EN has {en_c}")
