#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — dựng TIMELINE TẠM cho 3 ngôn ngữ (chưa có audio master mới).

Kịch bản v4 có 212 câu mỗi ngôn ngữ, trong khi âm thanh đã thu chỉ có 154/161/166 câu
với chữ cũ. Timeline này là MỐC ƯỚC LƯỢNG để `parse_shots.py` sinh bảng shot — KHÔNG phải
audio thật. Khi thu lại audio phải chạy lại build_audio3.py rồi parse_shots.py (H14).

Nguyên tắc (đã kiểm chứng cho Tập 02/03):
  1. Thứ tự element lấy theo MÃ element (hồi, số) — không suy từ mốc thời gian cũ.
  2. Thời lượng câu: hồi quy dur ≈ a + b·len(text), hệ số a,b hồi quy TỪ timeline gốc
     (giữ đúng nhịp đọc + khoảng lặng giữa câu của từng ngôn ngữ).
  3. Marker ACT tính LẠI từ mốc câu mới; khoảng lặng chuyển hồi lấy đúng số giây
     trong kịch bản mới (2 s) — giữ mốc cũ sẽ ra shot "chuyển hồi" 90–160 s.
  4. Marker NGHI: đặt tại vị trí element tương ứng, thời lượng = số giây trong kịch bản mới.
  5. Marker BGM/SFX: đặt tại thời điểm tới element tương ứng (đơn điệu với thứ tự element).
  6. INTRO giữ nguyên; outro = total − end(câu cuối) của timeline gốc (10 s).
  7. Vai: role trong kịch bản; "N" → N1/N2 theo EPISODES["04"]["n_element"].

Dùng:  py -3 .work/_build_timeline_t04_tmp.py
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

CFG = [
    ("vi", "01_KICH_BAN/Tap04/kichban_tap04_23102026.md",
     "timeline_s_t04.json", "script_tap04.json"),
    ("en", "01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md",
     "timeline_s_EN_t04.json", "script_tap04_EN.json"),
    ("ja", "01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md",
     "timeline_s_JA_t04.json", "script_tap04_JA.json"),
]
N_ELEMENT = {"1.07": "N1", "4.06": "N2"}          # EPISODES["04"]["n_element"]


def elkey(eid):
    a, b = eid.split(".")
    return (int(a), int(b))


def fit(durs, lens):
    """Hồi quy dur ≈ a + b·len (ít nhất bình phương, không cần numpy)."""
    n = len(durs)
    sx = sum(lens)
    sy = sum(durs)
    sxx = sum(x * x for x in lens)
    sxy = sum(x * y for x, y in zip(lens, durs))
    den = n * sxx - sx * sx
    if den == 0:
        return sy / n, 0.0
    b = (n * sxy - sx * sy) / den
    a = (sy - b * sx) / n
    return a, b


def r3(x):
    return round(x, 3)


report = []
for lang, kb, tl_name, script_name in CFG:
    tl_path = W / tl_name
    old = json.loads(tl_path.read_text(encoding="utf-8"))
    els = parse_file(str(ROOT / kb))

    # ---- hệ số nhịp từ timeline gốc
    old_items = old["items"]
    a, b = fit([it["end"] - it["start"] for it in old_items],
               [len(it["text"]) for it in old_items])

    # ---- ngân sách thời lượng câu mới
    def dur_of(txt):
        return max(1.2, a + b * len(txt))

    # ---- dựng tuần tự
    intro = old["intro"]
    first_start = old_items[0]["start"]          # 23.0 cho cả 3 bản
    outro = r3(old["total"] - old_items[-1]["end"])

    items, markers = [], []
    t = first_start
    act_lo, act_hi = {}, {}
    prev_act = None
    for el in els:
        eid = el["id"]
        act = int(eid.split(".")[0])
        kind = el["kind"]
        if prev_act is not None and act != prev_act:
            # khoảng lặng chuyển hồi 2 s (đúng "nghỉ chuyển hồi (2 s)" trong bảng shot)
            markers.append({"type": "ACT", "act": act,
                            "start": r3(t), "end": r3(t + 2.0)})
            t += 2.0
        prev_act = act
        if kind == "LOI":
            role = el["role"]
            if role == "N":
                role = N_ELEMENT.get(eid, "N1")
            for s in el.get("sentences", []):
                d = dur_of(s["text"])
                items.append({
                    "id": s["id"], "element": eid, "act": act, "role": role,
                    "start": r3(t), "end": r3(t + d), "text": s["text"],
                })
                act_lo.setdefault(act, t)
                act_hi[act] = t + d
                t += d
        elif kind == "NGHI":
            sec = float(el.get("sec") or 0)
            markers.append({"type": "NGHI", "id": eid, "start": r3(t),
                            "end": r3(t + sec), "desc": el.get("desc") or ""})
            t += sec
        else:                                     # BGM / SFX
            markers.append({"type": kind, "id": eid, "at": r3(t),
                            "desc": el.get("desc") or ""})

    # ---- marker ACT: khoảng lặng giữa hồi N và hồi N+1 (đã thêm ở vòng lặp)
    acts = {}
    for act in sorted(act_lo):
        acts[str(act)] = [r3(act_lo[act]), r3(act_hi[act])]

    markers.insert(0, {"type": "INTRO", "start": 0.0, "end": r3(intro)})
    total = r3(items[-1]["end"] + outro)

    # ---- ghi file (sao lưu bản gốc)
    bak = W / (tl_name.replace(".json", "") + ".bak")
    if not bak.exists():
        bak.write_text(tl_path.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
    tl_path.write_text(json.dumps(
        {"total": total, "intro": r3(intro), "items": items, "markers": markers,
         "acts": acts}, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

    # ---- kiểm tra tự thân
    ids = [it["id"] for it in items]
    dup = len(ids) != len(set(ids))
    mono = all(items[i]["start"] < items[i]["end"] for i in range(len(items)))
    ordered = all(items[i]["end"] <= items[i + 1]["start"] + 1e-9
                  for i in range(len(items) - 1))
    act_ok = True
    for act in sorted(act_lo):
        if act + 1 in act_lo:
            m = next(x for x in markers if x.get("type") == "ACT" and x.get("act") == act + 1)
            if not (m["end"] - m["start"] > 0):
                act_ok = False
    total_ok = total >= items[-1]["end"]
    voice = items[-1]["end"] - items[0]["start"]

    report.append((lang, len(items), total, voice, round(a, 4), round(b, 5),
                   dup, mono, ordered, act_ok, total_ok))

    # ---- đồng bộ script_*.json (nguồn cho build_video3)
    spath = W / script_name
    if spath.exists():
        sc = json.loads(spath.read_text(encoding="utf-8"))
        by = {}
        for it in items:
            by[it["id"]] = it["text"]
        ch = 0
        for el in sc:
            if el.get("kind") != "LOI":
                continue
            for s in el.get("sentences", []):
                if s["id"] in by:
                    if s.get("text") != by[s["id"]]:
                        s["text"] = by[s["id"]]
                        ch += 1
        spath.write_text(json.dumps(sc, ensure_ascii=False, indent=1),
                         encoding="utf-8", newline="\n")
        print(f"[{lang}] script_*.json: cập nhật {ch} câu")

print()
print(f"{'lang':5s} {'câu':>5s} {'total(s)':>10s} {'voice(s)':>10s} {'a':>8s} {'b':>9s} "
      f"{'trùng':>6s} {'start<end':>9s} {'khớp':>6s} {'ACT':>5s} {'total':>6s}")
for row in report:
    lang, n, total, voice, a, b, dup, mono, ordered, act_ok, total_ok = row
    print(f"{lang:5s} {n:5d} {total:10.2f} {voice:10.2f} {a:8.4f} {b:9.5f} "
          f"{'LOI' if dup else 'OK':>6s} {'OK' if mono else 'LOI':>9s} "
          f"{'OK' if ordered else 'LOI':>6s} {'OK' if act_ok else 'LOI':>5s} "
          f"{'OK' if total_ok else 'LOI':>6s}")
allok = all(not r[6] and r[7] and r[8] and r[9] and r[10] for r in report)
print("\nKẾT QUẢ:", "PASS" if allok else "FAIL")
