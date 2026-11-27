# -*- coding: utf-8 -*-
"""Xem schema provenance + tim dong lien quan Tap03/Tap04 tap."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
print("total", len(prov))
print("--- 2 mau dau ---")
for e in prov[:2]:
    print(json.dumps(e, ensure_ascii=False)[:600])
print("--- 2 mau cuoi ---")
for e in prov[-2:]:
    print(json.dumps(e, ensure_ascii=False)[:600])

keys = set()
for e in prov:
    keys.update(e.keys())
print("ALL KEYS:", sorted(keys))
hits = [e for e in prov if "Tap03" in json.dumps(e, ensure_ascii=False) or "Tap04" in json.dumps(e, ensure_ascii=False)]
print("hits", len(hits))
for e in hits[:6]:
    print(json.dumps(e, ensure_ascii=False)[:400])
print("...")
for e in hits[-6:]:
    print(json.dumps(e, ensure_ascii=False)[:400])
