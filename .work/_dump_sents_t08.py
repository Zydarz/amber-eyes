import json
from pathlib import Path

R = Path(r"D:/TEST/Gax/amber-eyes/.work")
out = []
for n, f in [("VN", "script_tap08.json"), ("EN", "script_tap08_EN.json"), ("JA", "script_tap08_JA.json")]:
    els = json.loads((R / f).read_text(encoding="utf-8"))
    out.append("=" * 30 + " " + n)
    for e in els:
        if e["kind"] != "LOI":
            continue
        out.append("[%s] (%s)" % (e["id"], e["role"]))
        for s in e["sentences"]:
            out.append("  %s: %s" % (s["id"], s["text"]))
Path(R / "_t08_sents.txt").write_text("\n".join(out), encoding="utf-8")
print("lines", len(out))
