# -*- coding: utf-8 -*-
"""Phu de Tập 02 — kiểm tra trung thực văn bản + đồng bộ thời gian (bản chính xác).

1) Ghép lại phụ đề của TỪNG câu (các cue + các dòng nối bằng 1 dấu cách)
   rồi so với câu gốc trong timeline → phát hiện mất dấu cách (cắt giữa từ),
   thêm/bớt chữ, hoặc sai thứ tự.
2) Gán cue theo TRUNG ĐIỂM thời gian → kiểm cue đầu tiên của câu có bắt đầu
   đúng lúc câu bắt đầu nói không.
3) Kiểm phủ: câu nào không có phụ đề, vai nào không có nhãn.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
SRT = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02.srt"

raw = SRT.read_text(encoding="utf-8")
blocks = [b for b in re.split(r"\n\s*\n", raw.strip()) if b.strip()]
cues = []
for b in blocks:
    L = b.splitlines()
    if len(L) < 3:
        continue
    ts = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", L[1])
    if len(ts) < 2:
        continue
    a = int(ts[0][0]) * 3600 + int(ts[0][1]) * 60 + int(ts[0][2]) + int(ts[0][3]) / 1000
    z = int(ts[1][0]) * 3600 + int(ts[1][1]) * 60 + int(ts[1][2]) + int(ts[1][3]) / 1000
    cues.append({"i": L[0], "a": a, "z": z, "lines": [x.rstrip() for x in L[2:]],
                 "text": " ".join(x.strip() for x in L[2:])})

tl = json.loads((WORK / "timeline_s_t02.json").read_text(encoding="utf-8"))
items = tl["items"]


def norm(s, strip_tag=True):
    s = s.lower().replace("–", "-").replace("—", "-")
    if strip_tag:
        s = re.sub(r"\[[^\]]*\]", " ", s)
    s = re.sub(r"[^a-z0-9à-ỹ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


out = {}

# ---------- 1. gan cue theo trung diem ----------
by_sent = {}
for c in cues:
    mid = (c["a"] + c["z"]) / 2
    hit = None
    for it in items:
        if it["start"] - 0.05 <= mid <= it["end"] + 0.05:
            hit = it
            break
    if hit is None:
        # trung diem nam giua 2 cau -> gan vao cau chua ket thuc gan nhat
        cands = [it for it in items if it["start"] <= mid <= it["end"] + 0.6]
        hit = cands[-1] if cands else None
    if hit is not None:
        by_sent.setdefault(hit["id"], []).append(c)
out["sentences_total"] = len(items)
out["sentences_with_cues"] = len(by_sent)
out["sentences_without_cues"] = len(items) - len(by_sent)
noc = [it["id"] for it in items if it["id"] not in by_sent]
out["sentences_without_cues_ids"] = noc[:15]
out["roles_without_cues"] = sorted({it["role"] for it in items if it["id"] in set(noc)})

# ---------- 2. trung thuc van ban ----------
bad_text = []
for it in items:
    cs = sorted(by_sent.get(it["id"], []), key=lambda c: c["a"])
    if not cs:
        continue
    built = " ".join(" ".join(l.strip() for l in c["lines"]) for c in cs)
    src = it["text"]
    nb, ns = norm(built), norm(src)
    if nb != ns:
        # tim vi tri lech
        k = 0
        while k < min(len(nb), len(ns)) and nb[k] == ns[k]:
            k += 1
        bad_text.append({
            "id": it["id"], "role": it["role"],
            "cues": [c["i"] for c in cs],
            "len_sub": len(nb), "len_src": len(ns),
            "first_diff_at": k,
            "sub_around": nb[max(0, k - 25):k + 25],
            "src_around": ns[max(0, k - 25):k + 25],
        })
out["sentences_with_text_mismatch"] = len(bad_text)
out["mismatch_sample"] = bad_text[:10]

# ---------- 3. dong bo: cue dau tien cua moi cau ----------
offs = []
for it in items:
    cs = sorted(by_sent.get(it["id"], []), key=lambda c: c["a"])
    if not cs:
        continue
    offs.append({"id": it["id"], "role": it["role"],
                 "cue_start": cs[0]["a"], "sent_start": it["start"],
                 "diff": round(cs[0]["a"] - it["start"], 3)})
d = [o["diff"] for o in offs]
out["first_cue_offset"] = {
    "min": min(d), "max": max(d),
    "abs_gt_0.1": sum(1 for x in d if abs(x) > 0.1),
    "abs_gt_0.25": sum(1 for x in d if abs(x) > 0.25),
    "abs_gt_0.5": sum(1 for x in d if abs(x) > 0.5),
    "late_by_0.5": sorted([o for o in offs if o["diff"] > 0.5], key=lambda o: -o["diff"])[:8],
    "early_by_0.5": sorted([o for o in offs if o["diff"] < -0.5], key=lambda o: o["diff"])[:8],
}

# ---------- 4. phu de co theo doi duong luyen van khong ----------
covered = 0
for it in items:
    cs = by_sent.get(it["id"], [])
    if not cs:
        continue
    src_dur = it["end"] - it["start"]
    sub_dur = sum(c["z"] - c["a"] for c in cs)
    covered += min(src_dur, sub_dur)
out["speech_covered_by_subtitle_pct"] = round(100 * covered /
                                               sum(it["end"] - it["start"] for it in items), 2)

# ---------- 5. nhan vai theo vai trong kich ban ----------
role_of_cue = {}
for sid, cs in by_sent.items():
    for c in cs:
        role_of_cue[c["i"]] = next(it["role"] for it in items if it["id"] == sid)
tag_cues = [c for c in cues if c["text"].startswith("[")]
out["tagged_cues"] = len(tag_cues)
tag_by_role = {}
for c in tag_cues:
    r = role_of_cue.get(c["i"], "?")
    tag_by_role.setdefault(r, []).append(c["text"].split("]")[0] + "]")
out["tags_by_role"] = {k: {"count": len(v), "labels": sorted(set(v))}
                       for k, v in tag_by_role.items()}
# vai nao co cau nhung khong duoc gan nhan
roles_no_tag = sorted({r for r in role_of_cue.values()
                        if not any(role_of_cue.get(c["i"]) == r for c in tag_cues)})
out["roles_never_tagged"] = roles_no_tag

print(json.dumps(out, ensure_ascii=False, indent=2))
