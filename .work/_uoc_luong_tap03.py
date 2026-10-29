#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uoc luong thoi luong Tap03 tu mau do chuan hoa tren Tap02 (audio da do that).

Moi hoi -> so giay. Tap03 chua co audio TTS, nen dung he so tu Tap02:
  toc do doc  (tu / giay phan loi)  va  phu luc thoi gian (gap + intro + nen).
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
WORK = Path(r"D:\TEST\Gax\Audi\.work")


def words_of(script_path):
    els = json.loads(Path(script_path).read_text(encoding="utf-8"))
    per_act, per_el = {}, {}
    for e in els:
        if e["kind"] != "LOI":
            continue
        w = sum(s["words"] for s in e["sentences"])
        per_el[e["id"]] = w
        per_act[e["act"]] = per_act.get(e["act"], 0) + w
    return per_act, per_el, els


def timeline_stats(tl_path):
    tl = json.loads(Path(tl_path).read_text(encoding="utf-8"))
    items = tl["items"]
    speech = sum(i["end"] - i["start"] for i in items)
    return tl, items, speech


# ---- 1. hieu chuan tren Tap02 (audio do that) ----
t2_act, t2_el, _ = words_of(WORK / "script_tap02.json")
tl2, items2, speech2 = timeline_stats(WORK / "timeline_s_t02.json")
w2 = sum(t2_act.values())
total2 = tl2["total"]
print("=== TAP02 (mau chuan, audio do that) ===")
print(f"  tu               : {w2}")
print(f"  tong thoi luong  : {total2:.1f}s = {int(total2//60)}:{int(total2%60):02d}")
print(f"  phan loi (audio) : {speech2:.1f}s")
print(f"  phu luc (gap+intro+nen): {total2 - speech2:.1f}s")
print(f"  toc do doc       : {w2/speech2:.3f} tu/giay phan loi")
print(f"  tu / giay tong   : {w2/total2:.3f}")
print()

# ---- 2. ap cho Tap03 ----
t3_act, t3_el, els3 = words_of(WORK / "script_tap03.json")
w3 = sum(t3_act.values())
r_speech = w2 / speech2          # tu/giay phan loi
r_total = w2 / total2            # tu/giay tong

# phu luc Tap03: intro + gap (gap phu thuoc cau truc, khac Tap02)
n_sent3 = sum(len(e["sentences"]) for e in els3 if e["kind"] == "LOI")
n_el3 = sum(1 for e in els3 if e["kind"] == "LOI")
n_act3 = len(set(e["act"] for e in els3 if e["kind"] == "LOI"))
n_q3 = sum(1 for e in els3 if e["kind"] == "LOI"
           for s in e["sentences"] if s["text"].rstrip("”\" ").endswith("?"))

# gap: giua cac cau trong cung luot, giua cac luot khac vai, giua cac hoi
gap_in = (n_sent3 - n_el3) * 0.35
gap_q = n_q3 * 0.60
gap_speaker = 0.70 * 12          # 12 lan doi vai (xem bang vai)
gap_act = (n_act3 - 1) * 2.0
intro = 22.41
overhead = gap_in + gap_q + gap_speaker + gap_act + intro

speech3 = w3 / r_speech
total3 = speech3 + overhead

print("=== TAP03 (uoc luong) ===")
print(f"  tu               : {w3}   (Tap02: {w2} — bang {w3/w2*100:.0f}%)")
print(f"  phan loi (uoc)   : {speech3:.1f}s")
print(f"  phu luc          : {overhead:.1f}s")
print(f"  TONG             : {total3:.1f}s = {int(total3//60)}:{int(total3%60):02d}")
print(f"  brief 25-27 phut : {'DAT' if 1500 <= total3 <= 1620 else 'KHONG DAT'}"
      f"  (thieu {1500-total3:.0f}s .. {1620-total3:.0f}s)")
print()
print("  theo hoi:")
for a in sorted(t3_act):
    tt = t3_act[a] / r_speech
    print(f"    hoi {a}: {t3_act[a]:>5} tu  ~{int(tt//60)}:{int(tt%60):02d} phan loi")
print()
print(f"  (Tap02 de co cross-check: {w2}/{total2:.1f}s = {w2/total2:.3f} tu/giay tong)")
print(f"  -> neu dung he so tong cua Tap02: Tap03 = {w3/r_total:.1f}s = "
      f"{int(w3/r_total//60)}:{int(w3/r_total%60):02d}")
