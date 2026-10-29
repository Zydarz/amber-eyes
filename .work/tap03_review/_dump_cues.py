# Dump elements + sentences of Tap03 to locate SFX/BGM cue anchors.
import json, sys, re

p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json"
els = json.load(open(p, encoding="utf-8"))

for e in els:
    if e["kind"] in ("SFX", "BGM"):
        print(f"{e['id']:<6} [{e['kind']}] {e['desc'][:110]}")
    elif e["kind"] == "NGHI":
        print(f"{e['id']:<6} [NGHI {e.get('sec')}s] {e.get('desc','')[:70]}")
    else:
        ss = e["sentences"]
        head = ss[0]["text"][:78] if ss else ""
        tail = ss[-1]["text"][:58] if ss else ""
        print(f"{e['id']:<6} [LOI {e['role']}] n={len(ss):<2} | {head} ... {tail}")
