# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban as PK

p20 = PK.parse_file(str(ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_23102026.md"))
loi20 = [e for e in p20 if e["kind"] == "LOI"]
print(f"Tap 20: Total sent = {sum(len(x['sentences']) for x in loi20)}")
for e in p20:
    if e["kind"] == "LOI":
        print(f"{e['id']} | {e['role']} | {len(e['sentences'])} sents")
