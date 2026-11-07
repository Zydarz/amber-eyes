#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 08 — dựng LẠI timeline cho VN/EN/JA từ kịch bản ĐÃ VIẾT LẠI (06/11/2026).

Cách dựng (theo đúng cách `.work/_t07/_t07_build_timeline.py` của Tập 07):
  1. RATE (ký tự/giây) + khoảng lặng + thời lượng nghỉ: suy từ timeline CŨ ĐO ĐƯỢC.
     - VN/EN: timeline CŨ của CHÍNH tập 08 (đo từ audio thật) → neo theo element ID.
     - JA   : chưa có timeline t08 ⇒ lấy RATE từ timeline JA t07 (audio thật tập 07).
  2. Neo element: element CŨ ↔ element MỚI theo ID (27/32 element LOI của Tập 08
     giữ nguyên ID); element không có trong bản cũ thì dùng RATE.
  3. Câu trong element: chia thời lượng đo được của element CŨ theo tỉ lệ độ dài câu MỚI.
  4. Marker BGM/SFX/NGHI/ACT/INTRO: đặt lại theo vị trí element MỚI.

Bố trí trong hồi (đúng công thức build_audio3.py):
  FIRST_VOICE 23,0 · GAP_SENT 0,35 · GAP_Q 0,60 · GAP_SPEAKER 0,70 · GAP_ACT 2,0.

Mốc dùng để hiển thị: timeline ƯỚC LƯỢNG — audio master Tập 08 đã bị dọn sau khi đăng
(AGENTS.md §11), không còn file TTS từng câu nên không đo được thời lượng thật.
Khi có audio mới phải chạy lại build_audio3.py (sẽ ghi đè đúng file này).

Dùng:  py -3 .work/_build_timeline_t08.py vi|en|ja
"""
import json
import statistics
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
import edition as ED  # noqa: E402

N_ELEM = ED.EPISODES["08"].get("n_element") or {}
INTRO, FIRST_VOICE = 22.41, 23.0
GAP_SENT, GAP_Q, GAP_SPEAKER, GAP_ACT, MAX_PAUSE = 0.35, 0.60, 0.70, 2.0, 2.5
OUTRO = 10.0
G_DEFAULT = 0.75

CFG = {
    "vi": {"old": "_cu/timeline_s_t08_before_rebuild_20261106.json",
           "out": "timeline_s_t08.json", "anchor": True},
    "en": {"old": "_cu/timeline_s_EN_t08_before_rebuild_20261106.json",
           "out": "timeline_s_EN_t08.json", "anchor": True},
    "ja": {"old": "timeline_s_JA_t07.json",
           "out": "timeline_s_JA_t08.json", "anchor": False},
}
lang = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
cfg = CFG[lang]
USE_ANCHOR = cfg["anchor"]


def rate_of(path):
    d = json.loads(path.read_text(encoding="utf-8"))
    items = d["items"]
    gaps = [items[i + 1]["start"] - items[i]["end"]
            for i in range(len(items) - 1)
            if items[i + 1]["element"] == items[i]["element"]]
    g = statistics.median(gaps) if gaps else G_DEFAULT
    speech = sum(it["end"] - it["start"] for it in items)
    chars = sum(len(it["text"]) for it in items)
    rate = chars / speech if speech else 14.0
    nghi = {m["id"]: m["end"] - m["start"] for m in d["markers"] if m["type"] == "NGHI"}
    cue = {m["id"]: (m["type"], m.get("desc", "")) for m in d["markers"]
           if m["type"] in ("BGM", "SFX")}
    return d, rate, g, nghi, cue


old, RATE, G, nghi_dur, cue_desc = rate_of(W / cfg["old"])
INTRO = old.get("intro") or INTRO

# ---- thống kê element CŨ ----------------------------------------------------
old_span, old_chars, old_n, old_speech = {}, {}, {}, {}
for it in old["items"]:
    e = it["element"]
    if e not in old_span:
        old_span[e] = [it["start"], it["end"]]
    old_span[e][1] = it["end"]
    old_chars[e] = old_chars.get(e, 0) + len(it["text"])
    old_n[e] = old_n.get(e, 0) + 1
    old_speech[e] = old_speech.get(e, 0) + (it["end"] - it["start"])

new = json.loads(ED.SCRIPT_JSON.read_text(encoding="utf-8"))
print(f"[{lang}] RATE {RATE:.2f} ky tu/s · lang {G:.2f}s · intro {INTRO}s · neo: {USE_ANCHOR}")

items, markers = [], []
acts = {}
t = FIRST_VOICE
pending_cues = []
act_no = 1
act_bounds = {1: [t, None]}
n_anchor = 0


def place_cues(at):
    for cid in pending_cues:
        typ, desc = cue_desc.get(cid, ("SFX", ""))
        markers.append({"type": typ, "id": cid, "at": round(at, 2), "desc": desc})
    pending_cues.clear()


for e in new:
    eid, kind = e["id"], e.get("kind")
    if kind in ("BGM", "SFX"):
        pending_cues.append(eid)
        continue
    if kind == "NGHI":
        place_cues(t)
        d = min(e.get("sec", 1.5), MAX_PAUSE)
        markers.append({"type": "NGHI", "id": eid, "start": round(t, 2),
                        "end": round(t + d, 2), "desc": e.get("desc", "")})
        t += d
        continue
    # ---- LOI
    if not eid.startswith(str(act_no) + "."):
        act_bounds[act_no][1] = t
        markers.append({"type": "ACT", "act": act_no + 1,
                        "start": round(t, 3), "end": round(t + GAP_ACT, 3)})
        t += GAP_ACT
        act_no += 1
        act_bounds[act_no] = [t, None]
    sents = e.get("sentences", [])
    if not sents:
        continue
    role = N_ELEM.get(eid, e.get("role") or "")
    if USE_ANCHOR and eid in old_span:
        speech_new = old_speech[eid] * (sum(len(s["text"]) for s in sents) / old_chars[eid])
        n_anchor += 1
    else:
        speech_new = sum(len(s["text"]) for s in sents) / RATE
    nchars = [max(1, len(s["text"])) for s in sents]
    durs = [speech_new * nc / sum(nchars) for nc in nchars]
    place_cues(t)
    start = t
    for i, (s, d) in enumerate(zip(sents, durs)):
        items.append({"id": s["id"], "element": eid, "act": act_no, "role": role,
                      "start": round(start, 3), "end": round(start + d, 3), "text": s["text"]})
        start += d
        if i < len(sents) - 1:
            start += GAP_Q if s["text"].rstrip("”\" ").endswith("?") else GAP_SENT
        elif i == len(sents) - 1:
            # ngat giua cac lượt: 0,70 s nếu đổi vai, 0,35 s nếu cùng vai
            pass
    t = items[-1]["end"]
    # khoang lach giua hai lượt (cung vai / doi vai)
    prev_role = items[-1]["role"]
    nxt = next((x for x in new[new.index(e) + 1:] if x.get("kind") == "LOI"), None)
    if nxt is not None:
        nrole = N_ELEM.get(nxt["id"], nxt.get("role") or "")
        t += GAP_SPEAKER if nrole != prev_role else GAP_SENT

act_bounds[act_no][1] = t
place_cues(t)
for a, (s, e_) in act_bounds.items():
    acts[str(a)] = [round(s, 3), round(e_ if e_ is not None else t, 3)]

markers.sort(key=lambda m: (m.get("at", m.get("start", 0)), m["type"]))
markers.insert(0, {"type": "INTRO", "start": 0.0, "end": INTRO})

total = round(t + OUTRO, 3)
out = {"total": total, "intro": INTRO, "items": items, "markers": markers, "acts": acts,
       "_estimated": {"ref": cfg["old"], "rate_chars_per_s": round(RATE, 3),
                      "anchor_elements": n_anchor, "anchor": USE_ANCHOR,
                      "note": "thoi luong uoc luong - audio master Tap 08 da bi don; dung cho anh tinh, khong dung de dung video"}}
dst = W / cfg["out"]
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

# ---- tu kiem ----------------------------------------------------------------
errs = []
if len(items) != len({i["id"] for i in items}):
    errs.append("ID cau trung")
for i in range(len(items) - 1):
    a, b = items[i], items[i + 1]
    if b["start"] < a["end"] - 0.001:
        errs.append(f"cau {a['id']} chong {b['id']}")
for s in acts.values():
    if s[1] <= s[0]:
        errs.append(f"hoi rong {s}")
print(f"  -> {dst.name}: {len(items)} cau · {len(markers)} marker · neo {n_anchor} element · "
      f"total {total}s ({int(total // 60)}:{int(total % 60):02d})")
if errs:
    print("  ✗", len(errs), "loi:")
    for e in errs[:10]:
        print("   -", e)
    sys.exit(1)
print("  ✓ tu kiem dat")
