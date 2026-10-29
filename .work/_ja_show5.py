#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import make_ja_scripts as M  # noqa: E402

for ep, k in [("18", "u0273"), ("20", "u0277"), ("21", "u0122"),
              ("22", "u0122"), ("24", "u0122")]:
    d = json.loads((HERE / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))
    v = d.get(k, {})
    print(f"--- Tap{ep} {k} kind={v.get('kind')}")
    print(repr(v.get("ja"))[:500])
    jobs = None
    print()
