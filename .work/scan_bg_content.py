#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quét nội dung prompt ảnh mọi tập: job dài (>75 từ lời), từ V9, từ gợi chữ (H26). Dùng: py -3 .work/scan_bg_content.py [XX ...] [--detail]"""
import json, re, sys, importlib.util
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).parent
spec = importlib.util.spec_from_file_location("q", W / "qc_bg_mapping.py"); q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
V9 = re.compile(r'\b(blood\w*|corpse\w*|dead bod\w*|bod(?:y|ies)|skull\w*|bones?|gun\w*|rifle\w*|pistol\w*|revolver\w*|knife|knives|stab\w*|bullet\w*|noose|gallows|electric chair|syringe\w*|gore|wound\w*|victim\w*|coffin\w*|grave\w*|autopsy|dissect\w*|ashes|urn)\b', re.I)
TX = re.compile(r'\b(text|signs?|signage|labels?|newspapers?|headlines?|posters?|banners?|lettering|inscription\w*|captions?|billboard\w*|plaque\w*|license plates?|numerals?|digits?)\b', re.I)
NEG = re.compile(r'(no|without|blank|unmarked|nothing|never)\s[^,.;]{0,60}(writing|lettering|text|signage|labels?|logos?|numerals?|digits?|readable|inscription\w*|captions?|plates?|banners?|signs?|stamps?)', re.I)
eps = [int(a) for a in sys.argv[1:] if a.isdigit()] or range(25, 69)
print("tập | job | >75 từ | V9? | chữ?")
for n in eps:
    p = W / f"bg_jobs_tap{n:02d}.json"
    if not p.exists(): continue
    j = json.load(open(p, encoding="utf-8"))
    T = {s["id"]: len(s["text"].split()) for e in q.pk.parse_file(q.script_file(n)) for s in (e.get("sentences") or [])}
    long = [x["name"][4:34] for x in j if sum(T.get(c, 0) for c in x["sentences"].split(",") if c) > 75]
    v9 = []; tx = []
    for x in j:
        s = NEG.sub("", x["prompt"])
        a = sorted({m.lower() for m in V9.findall(s)}); b = sorted({m.lower() for m in TX.findall(s)})
        if a: v9.append((x["name"][4:36], a))
        if b: tx.append((x["name"][4:36], b))
    print(n, len(j), len(long), len(v9), len(tx))
    if "--detail" in sys.argv:
        for h in v9: print("   V9", h)
        for h in tx: print("   TX", h)
