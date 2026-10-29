#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bổ sung provenance cho ảnh nền Tập 03 sinh ngoài nhánh song song (t3_backyard_garden).
Giữ đúng format entry của .work/gen_images.py (STYLE + prompt + NEG)."""
import json
from datetime import date
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
PROV = ROOT / "provenance.json"
BG = ROOT / "assets" / "bg"

STYLE = ("Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink "
         "linework, deep chiaroscuro lighting, subtle mist and film grain, desaturated muted "
         "palette, ominous quiet tension, highly detailed. ")
NEG = (" Strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, "
       "no watermark, no frame, no letterbox bars, full-bleed image.")

jobs = {j["name"]: j["prompt"]
        for j in json.loads((ROOT / ".work" / "bg_jobs_tap03.json").read_text(encoding="utf-8"))}

prov = json.loads(PROV.read_text(encoding="utf-8"))
added = []
for name in ("t3_backyard_garden", "t3_trapdoor"):
    f = f"assets/bg/{name}.png"
    if any(e.get("file") == f for e in prov):
        print(f"  {name}: da co provenance")
        continue
    raw = BG / "_raw" / f"{name}.png"
    from PIL import Image
    prov.append({
        "file": f,
        "loai": "nền 16:9",
        "cong_cu": "connector__matrix__generate_image (MiniMax qua mcode-tools)",
        "ngay": str(date.today()),
        "prompt": STYLE + jobs[name] + NEG,
        "seed": None,
        "nguon_anh_tham_chieu": None,
        "kich_thuoc_goc": list(Image.open(raw).size),
        "dieu_khoan": "<điều khoản thương mại của MiniMax — cần kiểm tra trước khi đăng>",
        "kiem_tra_thuong_mai": "chưa",
    })
    added.append(name)

PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
print("Da them:", added if added else "(khong co)")
print("Tong so entry provenance:", len(prov))
