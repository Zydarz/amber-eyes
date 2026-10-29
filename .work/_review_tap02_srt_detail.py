# -*- coding: utf-8 -*-
"""Kiem phu de Tập 02: (1) khop cue voi cau trong timeline bang MOC THOI GIAN,
(2) phat hien tu tach giua cue (cat giua tu), (3) tu tach dau dong (wrap giua tu).
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:\TEST\Gax\Audi")
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
    body = L[2:]
    cues.append({"i": L[0], "a": a, "z": z, "lines": body, "text": " ".join(body)})

out = {"cue_count": len(cues)}

# ---------- 1. cue nao thuoc cau nao (theo moc thoi gian) ----------
tl = json.loads((WORK / "timeline_s_t02.json").read_text(encoding="utf-8"))
items = tl["items"]
orphan = []
diffs = []
per_item = {}
for c in cues:
    best = None
    for it in items:
        if it["start"] - 0.35 <= c["a"] <= it["end"] + 0.35:
            best = it
            break
    if best is None:
        orphan.append({"cue": c["i"], "a": c["a"], "text": c["text"][:50]})
        continue
    per_item.setdefault(best["id"], []).append(c)
    diffs.append(round(c["a"] - best["start"], 3))
out["cues_without_timeline_parent"] = len(orphan)
out["orphan_sample"] = orphan[:8]
out["cue_start_vs_sentence_start"] = {
    "min": min(diffs), "max": max(diffs),
    "abs_gt_0.1": sum(1 for d in diffs if abs(d) > 0.1),
    "abs_gt_0.25": sum(1 for d in diffs if abs(d) > 0.25),
    "median": round(sorted(diffs)[len(diffs) // 2], 3),
}

# ---------- 2. cue co cat giua tu (khong phai dau/cuoi cue) ----------
def ends_clean(s):
    s = s.strip()
    return s.endswith((".", "?", "!", ":", '"', "”", "…")) or s.endswith("–") or s.endswith("—")


bad_join = []
for i in range(1, len(cues)):
    prev = cues[i - 1]
    cur = cues[i]
    if abs(cur["a"] - prev["z"]) > 0.05:      # khong lien tiep -> khong xet
        continue
    last = prev["lines"][-1].strip()
    first = cur["lines"][0].strip()
    if ends_clean(last) or not last or not first:
        continue
    # tach giua tu: dau cua cue moi khong bat dau bang chu hoa/dau cham
    if not (first[0].isupper() or first[0].isdigit()):
        bad_join.append({"from_cue": prev["i"], "to_cue": cur["i"],
                         "prev_end": last[-28:], "next_start": first[:28]})
out["mid_word_cue_splits"] = len(bad_join)
out["mid_word_sample"] = bad_join[:14]

# ---------- 3. xuong dong cat giua tu ----------
mid_line = []
for c in cues:
    for k in range(len(c["lines"]) - 1):
        last = c["lines"][k].strip()
        first = c["lines"][k + 1].strip()
        if not last or not first:
            continue
        if last[-1].isalnum() and first[0].isalnum() and not first[0].isupper() and not first[0].isdigit():
            mid_line.append({"cue": c["i"], "line1_end": last[-30:], "line2_start": first[:30]})
        elif last.endswith("-") or (last[-1].isalnum() and first[0].isupper() and last.split()[-1].isalpha() and len(last.split()[-1]) <= 3):
            mid_line.append({"cue": c["i"], "line1_end": last[-30:], "line2_start": first[:30],
                             "note": "nghi vong tach tu"})
out["mid_word_line_breaks"] = len(mid_line)
out["mid_line_sample"] = mid_line[:14]

# ---------- 4. do dai cue + so dong ----------
lens = [c["z"] - c["a"] for c in cues]
out["cue_duration"] = {"min": round(min(lens), 2), "max": round(max(lens), 2),
                       "mean": round(sum(lens) / len(lens), 2),
                       "n_over_7s": sum(1 for x in lens if x > 7.0),
                       "n_over_10s": sum(1 for x in lens if x > 10.0)}
out["lines_per_cue"] = {}
for c in cues:
    k = len(c["lines"])
    out["lines_per_cue"][str(k)] = out["lines_per_cue"].get(str(k), 0) + 1
charlens = [len(l) for c in cues for l in c["lines"]]
out["line_char_len"] = {"min": min(charlens), "max": max(charlens),
                        "mean": round(sum(charlens) / len(charlens), 1),
                        "n_over_45": sum(1 for x in charlens if x > 45),
                        "n_lines": len(charlens)}

# ---------- 5. cue co nhan vai ----------
tag_cues = [c for c in cues if c["text"].startswith("[")]
out["cues_with_role_tag"] = len(tag_cues)
out["role_tag_examples"] = [c["text"][:40] for c in tag_cues[:6]]

# ---------- 6. gap giua cac cue lon (im lang khi co loi) ----------
gaps = [(cues[i]["a"] - cues[i - 1]["z"], cues[i - 1]["i"], cues[i]["i"])
        for i in range(1, len(cues))]
big = sorted([g for g in gaps if g[0] > 1.0], reverse=True)
out["gaps_over_1s"] = len(big)
out["biggest_gaps"] = [{"gap": round(g[0], 2), "between": [g[1], g[2]]} for g in big[:10]]

print(json.dumps(out, ensure_ascii=False, indent=2))
