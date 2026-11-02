#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""(A) Plan doc: chu tren hinh + beat co khop WORDS THAT (payload) khong?
(B) Neu sua text cua timeline, co doi moc thoi gian beat khong?"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
n = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t or "")

pay = json.loads((W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json").read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in pay["items"] if r.get("id")}
tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it for it in tl["items"]}
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]

print("=== (A) BEAT + CHU TREN HINH so voi CAU NOI THAT ===")
beat_tot = beat_ok = 0
beat_bad = []
quote_tot = quote_ok = 0
quote_bad = []
bold_tot = bold_ok = 0
bold_bad = []
for s in shots:
    spoken = " ".join(pm[i]["display"] for i in s["sentences"] if i in pm)
    for b in s.get("beats") or []:
        beat_tot += 1
        if n(b) and n(b) in n(spoken):
            beat_ok += 1
        else:
            beat_bad.append((s["id"], b, spoken[:70]))
    for seg in s["segments"]:
        for k, v in seg["elems"]:
            if k == "quote":
                quote_tot += 1
                if n(v.strip("“”\"'")) and n(v.strip("“”\"'")) in n(spoken):
                    quote_ok += 1
                else:
                    quote_bad.append((s["id"], v, spoken[:80]))
            elif k == "bold":
                bold_tot += 1
                if n(v) in n(spoken):
                    bold_ok += 1
                else:
                    bold_bad.append((s["id"], v))

print(f"  BEAT  : {beat_ok}/{beat_tot} khop cau noi")
for x in beat_bad[:8]:
    print(f"     {x[0]}: {x[1][:52]!r}")
print(f"  QUOTE : {quote_ok}/{quote_tot} nguyen van trong cau noi")
for x in quote_bad[:8]:
    print(f"     {x[0]}: {x[1][:60]!r}\n        noi: {x[2]}")
print(f"  BOLD  : {bold_ok}/{bold_tot} nam trong cau noi (chung van tho)")

print("=== (B) TAC DONG khi doi text cua timeline len moc thoi gian beat ===")


def phrase_time(txt, start, end, phrase):
    p = phrase.lower()
    t = txt.lower()
    k = t.find(p)
    if k < 0:
        return None
    return start + (end - start) * k / max(1, len(txt))


moved = []
lost = []
for s in shots:
    for b in s.get("beats") or []:
        for i in s["sentences"]:
            if i not in sent or i not in pm:
                continue
            it = sent[i]
            old_t = phrase_time(it["text"], it["start"], it["end"], b)
            new_t = phrase_time(pm[i]["display"], it["start"], it["end"], b)
            if old_t is None and new_t is None:
                continue
            if old_t is None:
                lost.append((s["id"], b, "KHONG TIM THAY TRONG TEXT MOI"))
            elif new_t is None:
                lost.append((s["id"], b, "KHONG TIM THAY TRONG TEXT MOI"))
            else:
                d = abs(old_t - new_t)
                if d > 0.02:
                    moved.append((s["id"], b, round(old_t, 3), round(new_t, 3), round(d, 3)))
print(f"  beat doi moc thoi gian: {len(moved)} · mat khop: {len(lost)}")
for x in moved[:12]:
    print(f"     {x[0]}: {x[1][:34]!r} {x[2]} -> {x[3]} (lech {x[4]}s)")
for x in lost[:8]:
    print(f"     {x[0]}: {x[1][:34]!r} -> {x[2]}")
