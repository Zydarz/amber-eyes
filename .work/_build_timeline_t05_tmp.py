#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 05 — dựng TIMELINE TẠM cho bản dịch khi chưa có audio master mới.

Audio master của Tập 05 đã bị xoá trong đợt dọn đĩa ⇒ không có file WAV để đo.
Cách dựng (giữ mốc element cũ, chia lại thời lượng theo câu MỚI):
  1. Mốc element: lấy từ timeline CŨ (đo từ audio master cũ).
  2. Tốc độ đọc (ký tự/giây): suy từ chính timeline CŨ của bản đó ⇒ đúng nhịp riêng.
  3. Element mới (3.09, 3.10): cộng theo tốc độ đọc chung.
  4. Câu trong element: chia thời lượng theo tỉ lệ độ dài câu.
  5. Marker NGHI/BGM/SFX/ACT: đặt lại theo vị trí element mới.

Dùng:  py -3 .work/_build_timeline_t05_tmp.py vi|en|ja
"""
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

G = 0.75          # khoảng lặng giữa hai câu
PAUSE = 0.60      # sau câu cuối hồi, trước thẻ chuyển hồi
ACT_GAP = 2.00    # thẻ chuyển hồi
INTRO = 22.41     # nhạc mở đầu (đo được, giữ nguyên)

CFG = {
    "vi": ("01_KICH_BAN/Tap05/kichban_tap05_23102026.md", "timeline_s_t05.json"),
    "en": ("01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md", "timeline_s_EN_t05.json"),
    "ja": ("01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md", "timeline_s_JA_t05.json"),
}
lang = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
kb_rel, old_rel = CFG[lang]

old = json.loads((W / old_rel).read_text(encoding="utf-8"))
new = parse_file(str(ROOT / kb_rel))

# ---------------------------------------------------------------- thống kê timeline cũ
old_items = old["items"]
old_span, old_chars, old_n = {}, {}, {}
for it in old_items:
    e = it["element"]
    if e not in old_span:
        old_span[e] = [it["start"], it["end"]]
    old_span[e][1] = it["end"]
    old_chars[e] = old_chars.get(e, 0) + len(it["text"])
    old_n[e] = old_n.get(e, 0) + 1

gaps = [old_items[i + 1]["start"] - old_items[i]["end"]
        for i in range(len(old_items) - 1)
        if old_items[i + 1]["element"] == old_items[i]["element"]]
g = statistics.median(gaps) if gaps else G
speech = sum(it["end"] - it["start"] for it in old_items)
chars = sum(len(it["text"]) for it in old_items)
RATE = chars / speech                                   # ký tự / giây

nghi_dur = {m["id"]: m["end"] - m["start"]
            for m in old["markers"] if m["type"] == "NGHI"}
cue_desc = {m["id"]: (m["type"], m.get("desc", "")) for m in old["markers"]
            if m["type"] in ("BGM", "SFX")}

# Vai thật của từng element lấy từ CỘT VAI của bảng shot (nguồn chuẩn cho badge vai):
# kịch bản chỉ ghi "N" cho vai kể chuyện, còn bảng shot phân N1 (dân Park City) / N2 (Kerri).
ROLE_BY_EL = {}
_sk = W / "_t05_skeleton.json"
if _sk.exists():
    for r in json.loads(_sk.read_text(encoding="utf-8"))["rows"]:
        if r["kind"] != "shot":
            continue
        vai = r["cells"][2].strip()
        if vai and vai != "—":
            ROLE_BY_EL.setdefault(r["spans"][0][0], vai)
if ROLE_BY_EL:
    print("  vai theo bảng shot:",
          {k: v for k, v in sorted(ROLE_BY_EL.items()) if v.startswith("N")})

print(f"[{lang}] tốc độ đọc {RATE:.2f} ký tự/s · khoảng lặn câu {g:.2f}s · "
      f"nghỉ {[f'{k}:{v:.1f}s' for k, v in nghi_dur.items()]}")

# ---------------------------------------------------------------- dựng timeline mới
items, markers = [], []
acts = {}
t = INTRO + PAUSE
pending_cues = []          # cue chờ đặt tại vị trí câu kế tiếp
act_start = None
act_no = 1
act_bounds = {1: [t, None]}


def place_cues(at):
    for cid in pending_cues:
        typ, desc = cue_desc[cid]
        markers.append({"type": typ, "id": cid, "at": round(at, 2), "desc": desc})
    pending_cues.clear()


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
    if eid.startswith(str(act_no) + "."):
        pass
    else:
        # chuyển hồi
        act_bounds[act_no][1] = t
        markers.append({"type": "ACT", "act": act_no + 1,
                        "start": round(t + PAUSE, 2), "end": round(t + PAUSE + ACT_GAP, 2)})
        t += PAUSE + ACT_GAP
        act_no += 1
        act_bounds[act_no] = [t, None]
    sents = e.get("sentences", [])
    nchars = [max(1, len(s["text"])) for s in sents]
    if eid in old_span:
        o_dur = old_span[eid][1] - old_span[eid][0]
        o_ch = old_chars[eid]
        o_ng = old_n[eid]
        speech_new = (sum(nchars) / o_ch) * (o_dur - (o_ng - 1) * g)
    else:
        speech_new = sum(nchars) / RATE
    span = speech_new + (len(sents) - 1) * g
    place_cues(t)
    # chia thời lượng theo độ dài câu
    durs = [speech_new * nc / sum(nchars) for nc in nchars]
    start = t
    for s, d in zip(sents, durs):
        items.append({"id": s["id"], "element": eid, "act": act_no,
                      "role": ROLE_BY_EL.get(eid) or e.get("role") or "",
                      "start": round(start, 2),
                      "end": round(start + d, 2), "text": s["text"]})
        start += d + g
    t = start - g
    # dời t chuyển hồi về sau khi câu cuối
    t = items[-1]["end"]

act_bounds[act_no][1] = t
place_cues(t)
for a, (s, e_) in act_bounds.items():
    acts[str(a)] = [round(s, 2), round(e_ if e_ is not None else t, 2)]

markers.sort(key=lambda m: (m.get("at", m.get("start", 0)), m["type"]))
markers.insert(0, {"type": "INTRO", "start": 0.0, "end": INTRO})

total = round(t + 10.0, 2)     # đuôi tập 10 s
out = {"total": total, "intro": INTRO, "items": items,
       "markers": markers, "acts": acts}
dst = W / f"timeline_s_{'EN_' if lang == 'en' else 'JA_' if lang == 'ja' else ''}t05.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"  -> {dst.name}: {len(items)} câu · {len(markers)} marker · total {total}s")
