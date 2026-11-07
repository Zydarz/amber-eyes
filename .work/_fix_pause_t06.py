#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap06 — khôi phục/bổ sung `_pause_after` (AGENTS A13, A11 #135).

1. VN: chuyển 93 khoảng nghỉ của bản cũ (154 câu, git 0e9bd7c) sang mã câu mới THEO NỘI DUNG.
2. Bổ sung 0,3/0,4 s cho các ranh giới cùng vai đến khi dự đoán đạt cổng A13
   (trung vị nghỉ ≥ 0,6 s và ≤ 25% chỗ < 0,4 s) — dự đoán từ timeline hiện tại.
3. JA: dùng cùng bảng nghỉ VN (cùng mã câu, cùng nội dung). EN: giữ 113 mục, bổ sung như bước 2.
Chạy lại an toàn (idempotent): luôn dựng từ bản cũ + file hiện có.
"""
import json, subprocess, difflib, statistics as st, re
from pathlib import Path
W = Path(__file__).parent
OLD = W / "_cu/t06_higgs_redo_20261106/acting_tap06.json"

def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def norm(s): return re.sub(r"[\W_]+", "", s.lower())

def sents(script):
    out = []
    for e in script:
        for s in e.get("sentences", []): out.append((s["id"], s["text"], e["id"]))
    return out

def predict(tl, pause, base_pause):
    it = tl["items"]; g = []
    for a, b in zip(it, it[1:]):
        if a["act"] != b["act"]: continue
        g.append(b["start"] - a["end"] - base_pause.get(a["id"], 0) + pause.get(a["id"], 0))
    return g

def gate(g): return st.median(g), sum(x < 0.4 for x in g) / len(g)

def fill(tl, pause, base):
    it = tl["items"]
    cand = [(a, b) for a, b in zip(it, it[1:]) if a["act"] == b["act"] and a["element"] == b["element"]
            and a["id"] not in pause]
    cand.sort(key=lambda ab: -len(ab[0]["text"]))       # câu dài trước: cần chỗ thở hơn
    for a, _ in cand:
        m, r = gate(predict(tl, pause, base))
        if m >= 0.6 and r <= 0.20: break               # đặt biên 0,20 để còn dư so với ngưỡng 0,25
        pause[a["id"]] = 0.4 if len(a["text"]) >= 120 else 0.3
    return pause

old_sc = json.loads(subprocess.run(["git", "show", "0e9bd7c:.work/script_tap06.json"], capture_output=True,
                                   cwd=W.parent, check=True).stdout.decode("utf-8"))
old_txt = {i: t for i, t, _ in sents(old_sc)}
old_p = load(OLD)["_pause_after"]
new_s = sents(load(W / "script_tap06.json"))

# 1. chuyển theo nội dung
vn = {}
lost = []
for oid, v in old_p.items():
    t = old_txt.get(oid)
    best = max(new_s, key=lambda x: difflib.SequenceMatcher(None, norm(t), norm(x[1])).ratio()) if t else None
    r = difflib.SequenceMatcher(None, norm(t), norm(best[1])).ratio() if t else 0
    if r >= 0.85: vn[best[0]] = max(vn.get(best[0], 0), v)
    else: lost.append((oid, round(r, 2)))
cur = load(W / "acting_tap06.json")
for k, v in cur["_pause_after"].items(): vn.setdefault(k, v)   # giữ mục đang có
print(f"VN: cũ {len(old_p)} · chuyển được {len(old_p)-len(lost)} · không khớp {lost} · sau gộp {len(vn)}")

res = {}
for lang, sfx, acting in (("vi", "", "acting_tap06.json"), ("ja", "_JA", "acting_tap06_JA.json"),
                          ("en", "_EN", "acting_tap06_EN.json")):
    tl = load(W / f"timeline_s{sfx}_t06.json")
    p_acting = W / acting
    data = load(p_acting) if p_acting.exists() else {"_doc": "", "_pause_after": {}}
    base = data["_pause_after"] if lang != "ja" else {}            # JA hiện chạy với 0 khoảng nghỉ
    before = gate(predict(tl, base, base))
    pause = dict(vn) if lang in ("vi", "ja") else dict(base)
    pause = fill(tl, pause, base)
    after = gate(predict(tl, pause, base))
    data["_pause_after"] = dict(sorted(pause.items(), key=lambda kv: [int(x) for x in re.split(r"[.#]", kv[0])]))
    if lang == "ja":
        data["_doc"] = ("Bảng diễn xuất Tập 06 JA — chỉ `_pause_after` (cùng mã câu, cùng bảng nghỉ VN). "
                        "Sinh bởi _fix_pause_t06.py 07/11/2026 (AGENTS A13).")
    else:
        data["_doc"] = data.get("_doc", "") + " | 07/11/2026: _pause_after khôi phục/bổ sung bởi _fix_pause_t06.py (AGENTS A13)"
    with open(p_acting, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=1); f.write("\n")
    tot = sum(pause.values()) - sum(base.values())
    print(f"{lang}: mục {len(base)}→{len(pause)} · trung vị {before[0]:.2f}→{after[0]:.2f} s · "
          f"<0,4 s {before[1]:.0%}→{after[1]:.0%} · master dài thêm ≈{tot:.0f} s")
