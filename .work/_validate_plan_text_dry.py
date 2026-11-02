#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dry-run validator cho bang shot JA Tap02 (khong ghi file).

Kiem tra: beat phai co that trong cau noi · trich dan nguyen van · so tren hinh truy duoc.
Dung nguyen logic _build_plan_tap02_ja.py nhung tu doc shots_text + payload (khong dung
script_tap02_JA.json de check phu de).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ACT_TITLES_JA = {
    1: "第1幕 · 大佐の階級章の裏にある極端なコントラスト",
    2: "第2幕 · 現場と証拠ファイル――深淵への4段階",
    3: "第3幕 · 心理解剖――二重生活の捕食者の内面",
    4: "第4幕 · 取調室――軍人の頭脳を打ち砕く",
    5: "第5幕 · 判決、危険信号、そして結びの考察",
}
KANJI = {"〇": "0", "一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6",
         "七": "7", "八": "8", "九": "9", "十": "10", "百": "100", "千": "1000"}


def digits_of(t):
    """doi so kanji don gian sang arabic de so sanh so tren hinh."""
    for k, v in KANJI.items():
        t = t.replace(k, v)
    return t


txt = json.loads((W / "shots_text_tap02_JA.json").read_text(encoding="utf-8-sig"))
txt = {k: v for k, v in txt.items() if not k.startswith("_")}
pay = json.loads((W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json").read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in pay["items"] if r.get("id")}
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
smap = {s["id"]: s for s in shots}

errors = []
for sid, s in smap.items():
    entry = txt.get(sid)
    if not entry:
        errors.append(f"{sid}: khong co trong shots_text_tap02_JA.json")
        continue
    chu, beats = entry[0], entry[1]
    ctx = " ".join(pm[i]["display"] for i in s["sentences"] if i in pm)
    flat = ctx.replace(" ", "")
    flat_d = digits_of(flat)

    for p in beats or []:
        if p not in ctx:
            errors.append(f"{sid}: BEAT {p!r} khong co trong cau noi")
    for q in re.findall(r"“([^”]+)”", chu):
        for frag in [f.strip() for f in q.split("…") if f.strip()]:
            if frag not in ctx:
                errors.append(f"{sid}: TRICH {frag[:45]!r} khong nguyen van")

    screen = re.sub(r"→\s*`#\d+`:", " ", chu)
    allowed = set(re.findall(r"\d+", flat)) | set(re.findall(r"\d+", flat_d))
    for a in list(allowed):
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    act_num = sid.split("-")[0]
    allowed.add(act_num)
    allowed.add(act_num.zfill(2))
    allowed.add("02")
    for tok in set(re.findall(r"\d[\d,.]*", screen)):
        t = tok.replace(",", "").replace(".", "")
        if tok in allowed or t in allowed or tok in flat or t in flat or tok in flat_d or t in flat_d:
            continue
        if re.search(r"[第幕段階弾]\s*" + re.escape(tok), screen) or re.search(re.escape(tok) + r"\s*[幕段階弾件人話]", screen):
            continue
        if not ctx.strip() and any(re.search(r"\b" + re.escape(t) + r"\b", v) for v in ACT_TITLES_JA.values()):
            continue
        errors.append(f"{sid}: SO {tok!r} khong truy duoc ve cau noi (allowed={sorted(allowed)[:12]})")

print(f"LOI: {len(errors)}")
for e in errors:
    print("  -", e)
