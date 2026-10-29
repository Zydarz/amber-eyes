import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

W = Path(r"D:\TEST\Gax\Audi\.work")
for ep in ("02", "03"):
    d = json.loads((W / f"acting_tap{ep}.json").read_text(encoding="utf-8"))
    acts = {k: v for k, v in d.items() if not k.startswith("_")}
    import collections
    c = collections.Counter(v[1] for v in acts.values())
    n = len(acts)
    print(f"Tap{ep} ({n} cau) — lech toc do:")
    for k in sorted(c):
        print(f"   {k:+.2f} : {c[k]:>3}  ({c[k]/n*100:4.1f}%)")
    print()
