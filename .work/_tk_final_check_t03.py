# -*- coding: utf-8 -*-
"""Kiem tra cuoi: nen doc Tap 03 + spec + plan + provenance."""
import io
import json
import os
import re
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
BG = os.path.join(ROOT, "assets", "bg")
TK = os.path.join(ROOT, "02_SAN_XUAT", "TIKTOK")

names = sorted(n[:-4] for n in os.listdir(BG) if n.startswith("tk03_") and n.endswith(".png"))
print("1) nen doc assets/bg/tk03_*.png : %d" % len(names))

bad = []
for n in names:
    with Image.open(os.path.join(BG, n + ".png")) as im:
        if im.size != (1080, 1920):
            bad.append((n, im.size))
print("   sai kich thuoc (khong phai 1080x1920):", bad or "khong co")

prov = json.loads(io.open(os.path.join(ROOT, "provenance.json"), encoding="utf-8-sig").read())
items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
rows = [it for it in items if str(it.get("file", "")).startswith("assets/bg/tk03_")]
ai = [r for r in rows if r.get("prompt")]
fb = [r for r in rows if not r.get("prompt")]
print("2) provenance.json : %d dong tk03_* (%d AI that · %d du phong)"
      % (len(rows), len(ai), len(fb)))
print("   dong thieu trong provenance:",
      [n for n in names if ("assets/bg/%s.png" % n) not in {r.get("file") for r in rows}] or "khong co")

for d in ("Tap03", "Tap03_EN", "Tap03_JA"):
    spec_p = os.path.join(TK, d, "SPEC_AUDIO_CLIP_TAP03.json")
    s = io.open(spec_p, encoding="utf-8-sig").read()
    bgs = set(re.findall(r'"(?:bg|nen|background)"\s*:\s*"([a-z0-9_]+)"', s))
    miss = [b for b in bgs if not os.path.exists(os.path.join(BG, b + ".png"))]
    shots = len(re.findall(r'"(?:bg|nen|background)"\s*:\s*"', s))
    print("3) %-10s spec : %d shot · %d nen duy nhat · thieu file: %s"
          % (d, shots, len(bgs), miss or "khong co"))

plan = os.path.join(TK, "Tap03", "KE_HOACH_CLIP_TAP03.md")
t = io.open(plan, encoding="utf-8").read()
rows_t = re.findall(r"\|\s*`TK\d\.01#\d+`\s*\|\s*`([a-z0-9_]+)`", t)
print("4) plan VN : %d dong shot · nen khong phai tk03_: %s"
      % (len(rows_t), [r for r in rows_t if not r.startswith("tk03_")] or "khong co"))
print("   co muc 5 (anh nen doc):", "## 5. Ảnh nền dọc" in t)
rep = os.path.join(TK, "Tap03", "BAO_CAO_ANH_NEN_DOC_TAP03.md")
print("5) bao cao :", "co" if os.path.exists(rep) else "THIEU", rep)
print("   co muc 5b (doi ten nen):", "5b. Sửa tên nền" in io.open(rep, encoding="utf-8").read())
