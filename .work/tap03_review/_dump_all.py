import json
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
els = json.loads((ROOT / ".work" / "script_tap03.json").read_text(encoding="utf-8"))
out = []
for e in els:
    if e["kind"] != "LOI":
        continue
    out.append(f"--- {e['id']}  vai={e.get('role')} ---")
    for s in e["sentences"]:
        out.append(f"  {s['id']:<9} {s['text']}")
    out.append("")
p = ROOT / ".work" / "tap03_review" / "_sent_all_t3.txt"
p.write_text("\n".join(out), encoding="utf-8")
print("wrote", p, len("\n".join(out)), "chars")
