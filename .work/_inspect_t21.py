# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban as PK

p = PK.parse_file(str(ROOT / "01_KICH_BAN" / "Tap21" / "kichban_tap21_23102026.md"))
print(f"Total elements: {len(p)}")
loi = [e for e in p if e["kind"] == "LOI"]
print(f"LOI turns: {len(loi)}")
print(f"Total sentences: {sum(len(x.get('sentences', [])) for x in loi)}")
for e in p:
    num_s = len(e.get("sentences", []))
    print(f"{e['id']} | {e['kind']} | role={e.get('role', '')} | sents={num_s}")
