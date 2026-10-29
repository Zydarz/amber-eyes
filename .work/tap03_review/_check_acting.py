#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra .work/acting_tap03.json theo đúng hợp đồng của tts_sentences.py:
  - đủ 215 câu, đúng mã câu của kịch bản
  - định dạng [cảm xúc, lệch tốc độ, cao độ, lời đọc | None]
  - cảm xúc trong bộ an toàn, cao độ LUÔN = 0, lệch tốc độ trong [-0,06 · 0,02]
  - LỜI ĐỌC RIÊNG chỉ thêm ngắt nghỉ: bỏ hết thẻ <#..#> rồi so với câu gốc phải GIỐNG HỆT
  - không để sót dấu nháy kép trong lời đọc (TTS đọc thành tiếng)
"""
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

W = Path(r"D:\TEST\Gax\Audi\.work")
SCRIPT = json.loads((W / "script_tap03.json").read_text(encoding="utf-8"))
ACT = json.loads((W / "acting_tap03.json").read_text(encoding="utf-8"))

SAFE = {"neutral", "sad", "fearful", "surprised"}
TAG = re.compile(r"<#[\d.]+#>")

sent = {}
for e in SCRIPT:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sent[s["id"]] = s["text"]

err = []
acts = {k: v for k, v in ACT.items() if not k.startswith("_")}

missing = set(sent) - set(acts)
extra = set(acts) - set(sent)
if missing:
    err.append(f"thieu {len(missing)} cau: {sorted(missing)[:8]}")
if extra:
    err.append(f"thua {len(extra)} mau: {sorted(extra)[:8]}")

alt_changed = 0
for sid, v in acts.items():
    if not (isinstance(v, list) and len(v) == 4):
        err.append(f"{sid}: khong phai danh sach 4 phan tu")
        continue
    emo, dsp, pitch, alt = v
    if emo not in SAFE:
        err.append(f"{sid}: cam xuc '{emo}' ngoai bo an toan")
    if pitch != 0:
        err.append(f"{sid}: cao do {pitch} != 0")
    if not (-0.06 <= dsp <= 0.02):
        err.append(f"{sid}: lech toc do {dsp} ngoai [-0.06, 0.02]")
    if alt is not None:
        if not isinstance(alt, str):
            err.append(f"{sid}: loi doc khong phai chuoi")
            continue
        if "“" in alt or "”" in alt or '"' in alt:
            err.append(f"{sid}: con dau nhay trong loi doc")
        base = TAG.sub("", alt)
        base = re.sub(r"\s+", " ", base).strip()
        orig = re.sub(r"\s+", " ", sent[sid].replace("“", "").replace("”", "").replace('"', "")).strip()
        if base != orig:
            alt_changed += 1
            if alt_changed <= 5:
                err.append(f"{sid}: LOI DOC DOI CHUT (sau khi bo the):\n      goc: {orig[:110]}\n      doi: {base[:110]}")

pa = ACT.get("_pause_after", {})
if not isinstance(pa, dict):
    err.append("_pause_after phai la dict")
else:
    for sid, v in pa.items():
        if sid not in acts:
            err.append(f"_pause_after troi mau cau khong ton tai: {sid}")
        if not (0 <= v <= 2.0):
            err.append(f"_pause_after {sid} = {v} ngoai [0, 2]")

n_alt = sum(1 for v in acts.values() if v[3])
print(f"cau: {len(acts)} · loi doc rieng: {n_alt} · nghi them: {len(pa)} ({sum(pa.values()):.1f} s)")
print(f"voi dau nhay con sot: {'co' if alt_changed else 'khong'}")
if alt_changed:
    print(f"  so cau doi chu: {alt_changed}")
print()
if err:
    print(f"{len(err)} LOI:")
    for e in err:
        print("  !!", e)
else:
    print("KET QUA: SACH")
sys.exit(0 if not err else 1)
