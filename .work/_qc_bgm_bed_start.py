# -*- coding: utf-8 -*-
"""Bed đúng cho mỗi hồi = mood của thẻ [BGM] tại ĐIỂM BẮT ĐẦU bed.

  - Hồi 1: bed bắt đầu tại mốc `act1_cue` của tập (edition.py) -> lấy [BGM] tại mốc đó.
  - Hồi 2..5: bed bắt đầu ở ranh giới hồi -> lấy [BGM] đầu tiên của hồi đó.

Nguồn: .work/script_tapXX.json (đã parse bằng parse_kichban.py).
Chạy:   py -3 .work/_qc_bgm_bed_start.py
"""
import ast
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"

MOOD = [
    (r"guitar", "bgm_guitar_acoustic_60s.mp3"),
    (r"organ", "bgm_church_organ.mp3"),
    (r"hộp nhạc|music box|Music box", "bgm_music_box.mp3"),
    (r"vĩ cầm|violin|Violin", "bgm_violin_heart.mp3"),
    (r"cello|Cello", "bgm_cello_sad.mp3"),
    (r"piano[^.]{0,40}(ấm|trang ngọng|sâu lắng|ấm áp)|ấm áp[^.]{0,40}piano",
     "bgm_piano_warm.mp3"),
    (r"piano|Piano|dương cầm|Dương cầm", "bgm_piano_minimal.mp3"),
    (r"sub-bass|Sub-bass|drone|Drone|Sub-", "bgm_sub_drone.mp3"),
    (r"ambient|Ambient", "bgm_ambient_deep.mp3"),
]
# cello_sad_v2 là biến thể cello -> chấp nhận thay cho cello_sad
EQUIV = {"bgm_cello_sad.mp3": {"bgm_cello_sad.mp3", "bgm_cello_sad_v2.mp3"}}


def moods_of(text):
    out = []
    for pat, f in MOOD:
        if re.search(pat, text, re.IGNORECASE) and f not in out:
            out.append(f)
    if "bgm_piano_warm.mp3" in out:
        out = [f for f in out if f != "bgm_piano_minimal.mp3"]
    return out


# ----------------------------------------------------------------- edition.py
src = (WORK / "edition.py").read_text(encoding="utf-8")
ep_re = re.compile(r'^\s{4}"(\d\d)":\s*\{', re.M)
ep_pos = [(m.group(1), m.start(), m.end()) for m in ep_re.finditer(src)]
beds, cue1 = {}, {}
for i, (ep, _s, e) in enumerate(ep_pos):
    end = ep_pos[i + 1][1] if i + 1 < len(ep_pos) else len(src)
    chunk = src[e:end]
    b = chunk.find('"bed":')
    if b != -1:
        i0 = chunk.index("{", b)
        depth, j = 0, i0
        while j < len(chunk):
            if chunk[j] == "{":
                depth += 1
            elif chunk[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        beds[ep] = ast.literal_eval(chunk[i0:j + 1])
    c = re.search(r'"act1_cue":\s*"([\d.]+)"', chunk)
    if c:
        cue1[ep] = c.group(1)

# ----------------------------------------------------------------- script đã parse
print("=" * 100)
print("BED ĐÚNG THEO ĐIỂM BẮT ĐẦU BED  (Hồi 1 = tại act1_cue · Hồi 2-5 = [BGM] đầu hồi)")
print("=" * 100)
print(f"{'Tập':<5}{'H':<3}{'ĐIỂM BẮT ĐẦU':<12}{'MỐC':<8}{'MOOD KỊCH BẢN':<34}{'BED HIỆN TẠI'}")
print("-" * 118)

need_change = []
for ep in sorted(beds):
    sc = WORK / (f"script_tap{ep}.json" if ep != "01" else "script_v2.json")
    if not sc.exists():
        print(f"T{ep:<4}  (khong co script_tap{ep}.json)")
        continue
    els = json.loads(sc.read_text(encoding="utf-8"))
    bgm_by_act = {}
    for el in els:
        if el.get("kind") == "BGM":
            bgm_by_act.setdefault(el["act"], []).append(el)
    for act in range(1, 6):
        if act == 1:
            cid = cue1.get(ep)
            el = next((e for e in els if e.get("id") == cid), None)
            where = f"act1_cue {cid}"
        else:
            lst = bgm_by_act.get(act, [])
            el = lst[0] if lst else None
            where = f"đầu Hồi {act}"
        v = beds[ep].get(act)
        got = [v] if isinstance(v, str) else list(v or [])
        if el is None:
            print(f"T{ep:<4}H{act:<2}{where:<12}{'':<8}{'(khong co [BGM])':<34}{', '.join(got)}")
            continue
        desc = el.get("desc", "")
        mm = moods_of(desc)
        need = [m for m in mm if m != "bgm_ambient_deep.mp3"]   # ambient có sẵn ở lớp sàn
        ok = all(any(c in EQUIV.get(w, {w}) for c in got) for w in need) if need else True
        mark = "OK " if ok else "SAI"
        if not ok:
            need_change.append((ep, act, need, got, desc, el["id"]))
        print(f"T{ep:<4}H{act:<2}{where:<12}{el['id']:<8}{mark:<5}{', '.join(mm) or '-':<28}"
              f"{', '.join(got)}")

print()
print("=" * 100)
print(f"CẦN SỬA: {len(need_change)} slot")
print("=" * 100)
for ep, act, need, got, desc, eid in need_change:
    print(f"  T{ep} H{act}  ({eid})")
    print(f"      kịch bản : {desc[:110]}")
    print(f"      cần file  : {', '.join(need)}")
    print(f"      đang dùng : {', '.join(got)}")
