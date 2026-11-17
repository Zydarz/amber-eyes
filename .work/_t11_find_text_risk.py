# -*- coding: utf-8 -*-
"""Tìm trong 136 prompt các từ khoá khiến AI hay VẼ CHỮ (H2/H5) — ưu tiên soi mắt."""
import json
import re
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
jobs = json.loads((ROOT / ".work/bg_jobs_tap11_v3.json").read_text(encoding="utf-8"))
old = {j["name"] for j in json.loads((ROOT / ".work/bg_jobs_tap11_v2.json").read_text(encoding="utf-8"))}

KEYS = re.compile(
    r"\b(label|labelled|labeled|labeled|lettering|lettered|writing|wrote|written|inscribed|"
    r"engraved|embossed|printed|title|titled|caption|signed|signature|name[d]? on|"
    r"reading|banner|signboard|street sign|house number|license plate|number plate|"
    r"newspaper|headline|calendar|pages|binder|report|volume|bible|label)\b", re.I)

risky_old, risky_new = [], []
for j in jobs:
    p = j.get("prompt", "")
    hit = sorted({m.group(0).lower() for m in KEYS.finditer(p)})
    if not hit:
        continue
    (risky_old if j["name"] in old else risky_new).append((j["name"], hit))

print(f"=== ẢNH CŨ (66, sinh lại 13/11 — CHƯA có hồ sơ soi mắt) : {len(risky_old)} prompt nhắc chữ ===")
for n, h in risky_old:
    print(f"  {n}  <- {', '.join(h)}")
print(f"\n=== ẢNH MỚI (70, prompt mới) : {len(risky_new)} ===")
for n, h in risky_new:
    print(f"  {n}  <- {', '.join(h)}")

# ghi danh sách để soi bằng montage ô lớn
allr = [n for n, _ in risky_old] + [n for n, _ in risky_new]
(ROOT / ".work/_t11/risky_text_prompts.json").parent.mkdir(parents=True, exist_ok=True)
(ROOT / ".work/_t11/risky_text_prompts.json").write_text(
    json.dumps(allr, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\n-> .work/_t11/risky_text_prompts.json ({len(allr)} mã)")
