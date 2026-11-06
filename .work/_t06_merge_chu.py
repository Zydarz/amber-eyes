#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — ghép lớp phủ EN / JA (worker dịch) vào kế hoạch -> _t06_plan_en.json / _t06_plan_ja.json.

Chỉ số của file dịch KHỚP với _t06_plan_vi.json (worklist đã đồng bộ 125 shot).
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

BEAT = {
    "en": {"1.01": "Somber, slow opening strings",
           "1.05": "Cello melody swells",
           "2.13": "A police siren wails across the night",
           "3.09": "A deep, quiet sigh",
           "5.05": "Cello melody swells",
           "5.07": "Music swells then fades out `5.07`"},
    "ja": {"1.01": "重厚な低弦のオープニング",
           "1.05": "チェロの旋律が高ぶる",
           "2.13": "夜を裂く警察のサイレン",
           "3.09": "深く静かな溜息",
           "5.05": "チェロの旋律が高ぶる",
           "5.07": "音楽が静かにフェードアウト `5.07`"},
}

lang = (sys.argv[1] if len(sys.argv) > 1 else "en").lower()
cur = json.loads((W / "_t06_plan_vi.json").read_text(encoding="utf-8"))
chu = json.loads((W / f"_t06_chu_{lang}.json").read_text(encoding="utf-8"))

shots = cur["shots"]
if len(chu) != len(shots):
    print(f"✗ so muc lech: dich {len(chu)} · plan {len(shots)}")
    sys.exit(1)

out, miss = [], []
for i, sh in enumerate(shots):
    s = dict(sh)
    if str(i) in chu:
        s["chu"] = chu[str(i)]
    else:
        miss.append(i)
    s["beat"] = BEAT[lang].get(sh["el"], sh.get("beat", "—"))
    out.append(s)

if miss:
    print(f"✗ thiếu {len(miss)} mục: {miss[:10]}")
    sys.exit(1)

dst = W / f"_t06_plan_{lang}.json"
dst.write_text(json.dumps({"lang": lang, "shots": out}, ensure_ascii=False, indent=1),
               encoding="utf-8")
print(f"-> {dst.name}: {len(out)} shot")
