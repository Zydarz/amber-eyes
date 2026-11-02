#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sua text cua timeline JA Tap02 theo LOI NOI THAT (payload Higgs 31/10).

build_audio3.py doc "display" tu tts_manifest_JA_t02.json (25/10, cu) -> phu de lech
154/203 cau. Payload Higgs (31/10) moi la noi that. Script nay:
  1. backup timeline
  2. gan text[it] = payload.display  (GIO nguyen van -> muc thoi gian khong doi)
  3. ghi lai timeline + sinh lai SRT
  4. bao cao anh huong len moc thoi gian beat (build_video3.phrase_time)
"""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"

TL = W / "timeline_s_JA_t02.json"
PAY = W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json"
BK = W / "_cu" / "timeline_s_JA_t02_pre_text_fix.json"
n = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t or "")

tl = json.loads(TL.read_text(encoding="utf-8-sig"))
pay = json.loads(PAY.read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in pay["items"] if r.get("id")}

if not BK.exists():
    shutil.copy2(TL, BK)
    print(f"backup -> {BK.relative_to(ROOT)}")

changed = []
for it in tl["items"]:
    p = pm.get(it["id"])
    if not p:
        continue
    new = p["display"]
    if new != it["text"]:
        changed.append((it["id"], it["text"], new))
        it["text"] = new

TL.write_text(json.dumps(tl, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"da doi text cho {len(changed)} / {len(tl['items'])} cau")
print(f"muc thoi gian: giu nguyen (start/end khong doi)")

print("\n=== TAC DONG len moc thoi gian BEAT (build_video3.phrase_time) ===")
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
old_sent = {it["id"]: it for it in json.loads(BK.read_text(encoding="utf-8-sig"))["items"]}
sent = {it["id"]: it for it in tl["items"]}


def phrase_time(txt, start, end, phrase):
    k = (txt or "").lower().find(phrase.lower())
    if k < 0:
        return None
    return start + (end - start) * k / max(1, len(txt or ""))


moved, lost = [], []
for s in shots:
    for b in s.get("beats") or []:
        for i in s["sentences"]:
            if i not in sent:
                continue
            o = old_sent.get(i)
            if not o:
                continue
            to = phrase_time(o["text"], o["start"], o["end"], b)
            tn = phrase_time(sent[i]["text"], sent[i]["start"], sent[i]["end"], b)
            if to is None and tn is None:
                continue
            if to is None or tn is None:
                lost.append((s["id"], b, "mat khop" if to is not None else "moi them"))
            elif abs(to - tn) > 0.02:
                moved.append((s["id"], b, round(to, 3), round(tn, 3), round(abs(to - tn), 3)))
print(f"  beat doi moc: {len(moved)} · mat khop: {len(lost)}")
for x in moved[:12]:
    print(f"     {x[0]}: {x[1][:30]!r} {x[2]} -> {x[3]} (lech {x[4]}s)")
for x in lost[:10]:
    print(f"     {x[0]}: {x[1][:30]!r} -> {x[2]}")

print("\n=== SINH LAI SRT ===")
r = subprocess.run([sys.executable, str(W / "subtitles.py")], cwd=ROOT,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print("  rc =", r.returncode, (r.stdout or "").strip()[:200])
if r.returncode != 0:
    print((r.stderr or "")[-1200:])
    raise SystemExit(1)

srt = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt"
txt = srt.read_bytes().decode("utf-8-sig").replace("\r\n", "\n")
blocks = [b for b in txt.strip().split("\n\n") if b.strip()]
print(f"  SRT: {len(blocks)} cue")
print("\n  --- 3 cue dau ---")
for b in blocks[:3]:
    print("   ", b.replace("\n", " | ")[:160])
