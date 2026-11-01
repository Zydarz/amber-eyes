#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In moc thoi gian cuoi hoi 1 (fake timeline, dung thoi luong Higgs that)
de tra loi: shot 1-18 (the 'THIEN THAN TU THAN') dai bao lau — co vuot H10 (3-15 s)?
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FIRST_VOICE, INTRO = 23.0, 22.41
GAP_SENT, GAP_Q, GAP_SPEAKER, GAP_ACT, MAX_PAUSE = 0.35, 0.60, 0.70, 2.0, 2.5

script = json.loads((W / "script_tap04.json").read_text(encoding="utf-8-sig"))
man = {m["id"]: m for m in json.loads((W / "tts_manifest_t04.json").read_text(encoding="utf-8-sig"))}
PAUSE_AFTER = json.loads((W / "acting_tap04.json").read_text(encoding="utf-8-sig")).get("_pause_after", {})
hm = json.loads((W / "kaggle_higgs" / "out_higgs_prod_t04" / "out_higgs_prod_t04"
                 / "higgs_manifest.json").read_text(encoding="utf-8-sig"))
best = {}
for h in hm:
    sid = h["id"]
    if sid not in best or h.get("variant", 0) == 0:
        best[sid] = h
DUR = {k: v["duration_s"] for k, v in best.items()}

t = FIRST_VOICE
items, markers, acts = [], [{"type": "INTRO", "start": 0.0, "end": INTRO}], {}
cur_act = None
pending = None
for e in script:
    act = e["act"]
    if cur_act is not None and act != cur_act:
        markers.append({"type": "ACT", "act": act, "start": round(t, 3), "end": round(t + GAP_ACT, 3)})
        t += GAP_ACT
        pending = None
    if act not in acts:
        acts[act] = [t, t]
    cur_act = act
    if e["kind"] == "NGHI":
        sec = min(e["sec"], MAX_PAUSE)
        markers.append({"type": "NGHI", "id": e["id"], "start": round(t, 3), "end": round(t + sec, 3)})
        t += sec
        pending = None
    elif e["kind"] in ("SFX", "BGM"):
        markers.append({"type": e["kind"], "id": e["id"], "at": round(t, 3)})
    else:
        role = man[e["sentences"][0]["id"]]["role"]
        if pending:
            g = GAP_SPEAKER if pending[0] != role else GAP_SENT
            if pending[1].rstrip("”\" ").endswith("?"):
                g = max(g, GAP_Q)
            t += g
        for k, s in enumerate(e["sentences"]):
            d = DUR.get(s["id"], 3.0)
            items.append({"id": s["id"], "act": act, "role": role,
                          "start": round(t, 3), "end": round(t + d, 3), "dur": d})
            t += d
            t += PAUSE_AFTER.get(s["id"], 0.0)
            if k < len(e["sentences"]) - 1:
                t += GAP_Q if s["text"].rstrip("”\" ").endswith("?") else GAP_SENT
        pending = (role, e["sentences"][-1]["text"])
    acts[act][1] = t

print("=== ACT markers ===")
for m in markers:
    if m["type"] == "ACT":
        print("  ACT %s  %.1f -> %.1f" % (m["act"], m["start"], m["end"]))
print("\n=== cac cau 1.14#5 .. 1.16#3 ===")
for it in items:
    if it["id"].startswith(("1.14#5", "1.14#6", "1.16")):
        print("  %-9s %7.2f -> %7.2f  (%.2fs)" % (it["id"], it["start"], it["end"], it["dur"]))
a2 = next(m for m in markers if m["type"] == "ACT" and m["act"] == 2)
i161 = next(i for i in items if i["id"] == "1.16#1")
print("\nshot 1-18 (1.16#1 -> moc ACT2): %.1f s" % (a2["start"] - (i161["start"] - 0.20)))
print("thoi luong 1.16#1..#3: %s" % [round(i["dur"], 2) for i in items if i["id"].startswith("1.16")])
print("\ntong thoi luong am (fake): %.1f s | gian them: %.1f s"
      % (sum(i["dur"] for i in items), t - FIRST_VOICE - sum(i["dur"] for i in items)))
