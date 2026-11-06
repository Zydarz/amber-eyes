#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — dựng TIMELINE TẠM cho VN/EN/JA (audio master cũ đã bị dọn / kịch bản đã viết lại).

Cách dựng (giữ mốc element cũ đo từ audio thật, chia lại thời lượng câu MỚI):
  1. RATE (ký tự/giây) + khoảng lặng + thời lượng nghỉ: suy từ timeline CŨ của chính bản đó.
     - JA (chưa có timeline t06): suy RATE từ timeline_s_JA_t05.json (audio thật của tập 05 JA).
  2. Mốc element: ghép element CŨ ↔ element MỚI bằng độ tương đồng câu đầu (difflib).
  3. Element không có mốc: tính theo RATE.
  4. Câu trong element: chia thời lượng theo tỉ lệ độ dài câu.
  5. Marker BGM/SFX/NGHI/ACT: đặt lại theo vị trí element MỚI.

Dùng:  py -3 .work/_t06_build_timeline.py vi|en|ja
"""
import difflib
import json
import re
import statistics
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402
import edition as ED  # noqa: E402

N_ELEM = ED.EPISODES["06"].get("n_element") or {}
PAUSE = 0.60      # sau câu cuối hồi, trước thẻ chuyển hồi
ACT_GAP = 2.00    # thẻ chuyển hồi
OUTRO = 10.0      # đuôi tập
G_DEFAULT = 0.75
SIM_MIN = 0.42    # ngưỡng chấp nhận ghép element cũ ↔ mới

CFG = {
    "vi": {"kb": "01_KICH_BAN/Tap06/kichban_tap06_23102026.md",
           "old": "_t06_old_timeline_vi.json", "out": "timeline_s_t06.json"},
    "en": {"kb": "01_KICH_BAN/Tap06_EN/kichban_tap06_EN.md",
           "old": "_t06_old_timeline_en.json", "out": "timeline_s_EN_t06.json"},
    "ja": {"kb": "01_KICH_BAN/Tap06_JA/kichban_tap06_JA.md",
           "old": "timeline_s_JA_t05.json", "out": "timeline_s_JA_t06.json", "anchor": False},
}
lang = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
USE_ANCHOR = CFG[lang].get("anchor", True)
cfg = CFG[lang]
cfg = CFG[lang]


def norm(s):
    s = re.sub(r"[“”\"'‘’()\[\].,;:!?—–\-]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def rate_of(path):
    """(RATE ký tự/giây, khoảng lặng trung vị, dict nghi_dur, dict cue)"""
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


old_path = W / cfg["old"]
old, RATE, G, nghi_dur, cue_desc = rate_of(old_path)
INTRO = old.get("intro") or 22.41

# ---- thống kê element cũ ----------------------------------------------------
old_span, old_chars, old_n, old_first = {}, {}, {}, {}
for it in old["items"]:
    e = it["element"]
    if e not in old_span:
        old_span[e] = [it["start"], it["end"]]
        old_first[e] = it["text"]
    old_span[e][1] = it["end"]
    old_chars[e] = old_chars.get(e, 0) + len(it["text"])
    old_n[e] = old_n.get(e, 0) + 1

new = parse_file(str(ROOT / cfg["kb"]))

# ---- ghép element cũ ↔ mới theo độ tương đồng (ghép toàn cục, greedy) -------
# Mỗi element so bằng CỶ SẮP NHẤT giữa các câu của nó (tránh việc câu đầu
# được viết lại làm hỏng điểm neo).
def el_similarity(e, oe, old_texts):
    a = [norm(s["text"]) for s in e.get("sentences", [])] or [norm(e.get("text", ""))]
    b = [norm(x) for x in old_texts[oe]]
    return max(difflib.SequenceMatcher(None, x, y).ratio() for x in a for y in b)


new_loi = [e for e in new if e.get("kind") == "LOI"]
old_texts = {}
for it in old["items"]:
    old_texts.setdefault(it["element"], []).append(it["text"])

cand = []
if USE_ANCHOR:
    for e in new_loi:
        for oe in old_span:
            cand.append((el_similarity(e, oe, old_texts), e["id"], oe))
cand.sort(reverse=True)

pairs = {e["id"]: [None, 0.0] for e in new_loi}
used_old = set()
for r, nid, oid in cand:
    if r < SIM_MIN:
        break
    if nid in [k for k, v in pairs.items() if v[0]] or oid in used_old:
        continue
    pairs[nid] = [oid, r]
    used_old.add(oid)

print(f"[{lang}] RATE {RATE:.2f} ký tự/s · lặng {G:.2f}s · intro {INTRO}s · "
      f"mốc element dùng lại {sum(1 for v in pairs.values() if v[0])}/{len(pairs)}")
for e in new_loi:
    oid, r = pairs[e["id"]]
    print(f"    {e['id']} <- {oid or '(mới)':<8} sim={r:.2f}")

# ---- dựng timeline mới ------------------------------------------------------
items, markers = [], []
acts = {}
t = INTRO + PAUSE
pending_cues = []
act_no = 1
act_bounds = {1: [t, None]}


def place_cues(at):
    for cid in pending_cues:
        typ, desc = cue_desc.get(cid, ("SFX", ""))
        markers.append({"type": typ, "id": cid, "at": round(at, 2), "desc": desc})
    pending_cues.clear()


anchor = {nid: v[0] for nid, v in pairs.items()}

for e in new:
    eid = e["id"]
    kind = e.get("kind")
    if kind in ("BGM", "SFX"):
        pending_cues.append(eid)
        continue
    if kind == "NGHI":
        place_cues(t)
        d = nghi_dur.get(eid, 1.5)
        markers.append({"type": "NGHI", "id": eid, "start": round(t, 2),
                        "end": round(t + d, 2), "desc": ""})
        t += d
        continue
    # LOI
    if not eid.startswith(str(act_no) + "."):
        act_bounds[act_no][1] = t
        markers.append({"type": "ACT", "act": act_no + 1,
                        "start": round(t + PAUSE, 2), "end": round(t + PAUSE + ACT_GAP, 2)})
        t += PAUSE + ACT_GAP
        act_no += 1
        act_bounds[act_no] = [t, None]
    sents = e.get("sentences", [])
    nchars = [max(1, len(s["text"])) for s in sents]
    oid = anchor.get(eid)
    if oid and oid in old_span:
        o_dur = old_span[oid][1] - old_span[oid][0]
        speech_new = (sum(nchars) / old_chars[oid]) * (o_dur - (old_n[oid] - 1) * G)
    else:
        speech_new = sum(nchars) / RATE
    span = speech_new + (len(sents) - 1) * G
    place_cues(t)
    durs = [speech_new * nc / sum(nchars) for nc in nchars]
    start = t
    role = N_ELEM.get(eid, e.get("role") or "")
    for s, d in zip(sents, durs):
        items.append({"id": s["id"], "element": eid, "act": act_no, "role": role,
                      "start": round(start, 2), "end": round(start + d, 2), "text": s["text"]})
        start += d + G
    t = items[-1]["end"]

act_bounds[act_no][1] = t
place_cues(t)
for a, (s, e_) in act_bounds.items():
    acts[str(a)] = [round(s, 2), round(e_ if e_ is not None else t, 2)]

markers.sort(key=lambda m: (m.get("at", m.get("start", 0)), m["type"]))
markers.insert(0, {"type": "INTRO", "start": 0.0, "end": INTRO})

total = round(t + OUTRO, 2)
out = {"total": total, "intro": INTRO, "items": items, "markers": markers, "acts": acts}
dst = W / cfg["out"]
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

# ---- tự kiểm ----------------------------------------------------------------
errs = []
if len(items) != len({i["id"] for i in items}):
    errs.append("ID câu trùng")
for i in range(len(items) - 1):
    a, b = items[i], items[i + 1]
    if b["start"] < a["end"] - 0.001:
        errs.append(f"câu {a['id']} chồng {b['id']}")
    # hở lớn chỉ được phép ở ranh giới hồi (có thẻ chuyển hồi ở giữa)
    # hoặc do marker NGHI đứng giữa hai element.
    if b["start"] - a["end"] > 2.6 and a["act"] == b["act"]:
        errs.append(f"hở lớn {a['id']}->{b['id']}")
for s in acts.values():
    if s[1] <= s[0]:
        errs.append(f"hồi rỗng {s}")
print(f"  -> {dst.name}: {len(items)} câu · {len(markers)} marker · total {total}s "
      f"({int(total // 60)}:{int(total % 60):02d})")
if errs:
    print("  ✗", len(errs), "lỗi:")
    for e in errs[:10]:
        print("   -", e)
    sys.exit(1)
print("  ✓ tự kiểm đạt")
