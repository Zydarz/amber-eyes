# -*- coding: utf-8 -*-
"""Kiem CHINH XAC viec cat tu trong phu de: so voi CAU GOC trong timeline.
Neu hai cue lien tiep thuoc cung mot cau, va cau goc co 'cuoi_cue1 cuoi_cue2'
=> cat sai giua tu. Neu cau goc co 'cuoi_cue1 cuoi_cue2' voi dau cach
=> cat dung o ranh gioi tu.
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


def norm(s):
    s = s.lower().replace("–", "-").replace("—", "-")
    s = re.sub(r"\[[^\]]*\]", " ", s)          # bo nhan vai
    s = re.sub(r"[^a-z0-9à-ỹ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# gan cue -> cau (theo moc thoi gian, dung khi cue bat dau trong khoang cau)
assign = {}
for c in cues:
    for it in items:
        if it["start"] - 0.35 <= c["a"] <= it["end"] + 0.35:
            assign[c["i"]] = it
            break

# ---- 1. cue dau tien cua moi cau co bat dau dung tai cau khong? ----
first_cue_of_sentence = {}
for c in cues:
    it = assign.get(c["i"])
    if it and it["id"] not in first_cue_of_sentence:
        cc = dict(c)
        cc["_it"] = it
        first_cue_of_sentence[it["id"]] = cc
d = [round(first_cue_of_sentence[k]["a"] - first_cue_of_sentence[k]["_it"]["start"], 3)
     for k in first_cue_of_sentence]
out = {
    "sentences": len(items),
    "sentences_with_cue": len(first_cue_of_sentence),
    "sentences_without_cue": len(items) - len(first_cue_of_sentence),
    "first_cue_offset_vs_sentence_start": {
        "min": min(d), "max": max(d), "abs_gt_0.1": sum(1 for x in d if abs(x) > 0.1),
        "abs_gt_0.25": sum(1 for x in d if abs(x) > 0.25),
    },
}

# ---- 2. cat sai giua tu GIUA hai cue cung mot cau ----
midword_cue = []
for i in range(1, len(cues)):
    p, c = cues[i - 1], cues[i]
    if abs(c["a"] - p["z"]) > 0.06:
        continue
    itp, itc = assign.get(p["i"]), assign.get(c["i"])
    if not itp or not itc or itp["id"] != itc["id"]:
        continue
    src = norm(itp["text"])
    lw = norm(p["lines"][-1]).split()
    fw = norm(c["lines"][0]).split()
    if not lw or not fw:
        continue
    last_w, first_w = lw[-1], fw[0]
    if last_w == first_w:
        continue
    if f"{last_w} {first_w}" in src:
        continue                       # cat dung o ranh gioi tu
    if f"{last_w}{first_w}" in src:
        midword_cue.append({"id": itp["id"], "cue": p["i"], "next": c["i"],
                            "broken": f"{last_w}|{first_w}",
                            "sentence": itp["text"][:80]})
out["mid_word_cue_splits"] = len(midword_cue)
out["mid_word_cue_sample"] = midword_cue[:12]

# ---- 3. cat sai giua tu GIUA hai dong trong cung mot cue ----
midword_line = []
for c in cues:
    it = assign.get(c["i"])
    if not it or len(c["lines"]) < 2:
        continue
    src = norm(it["text"])
    for k in range(len(c["lines"]) - 1):
        lw = norm(c["lines"][k]).split()
        fw = norm(c["lines"][k + 1]).split()
        if not lw or not fw:
            continue
        last_w, first_w = lw[-1], fw[0]
        if last_w == first_w:
            continue
        if f"{last_w} {first_w}" in src:
            continue
        if f"{last_w}{first_w}" in src:
            midword_line.append({"id": it["id"], "cue": c["i"], "broken": f"{last_w}|{first_w}",
                                 "sentence": it["text"][:80]})
out["mid_word_line_breaks"] = len(midword_line)
out["mid_word_line_sample"] = midword_line[:12]

# ---- 4. dong ket thuc bang dau cham bi "treo" ----
dangling = []
for c in cues:
    last = c["lines"][-1].strip()
    if last.endswith(("-", "–", "—", ",")) and len(last.split()) > 1:
        dangling.append({"cue": c["i"], "ends_with": last[-18:], "text": c["text"][:60]})
out["cues_ending_with_dash_or_comma"] = len(dangling)
out["dangling_sample"] = dangling[:8]

# ---- 5. cue co nhan vai ----
tagged = [c for c in cues if c["text"].startswith("[")]
out["role_tagged_cues"] = len(tagged)
out["role_tag_distribution"] = {}
for c in tagged:
    t = c["text"].split("]")[0] + "]"
    out["role_tag_distribution"][t] = out["role_tag_distribution"].get(t, 0) + 1

print(json.dumps(out, ensure_ascii=False, indent=2))
