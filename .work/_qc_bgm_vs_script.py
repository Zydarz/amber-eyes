# -*- coding: utf-8 -*-
"""QC: bed BGM của edition.py có khớp mood trong KỊCH BẢN không?

Nguồn sự thật = kịch bản (01_KICH_BAN/TapXX/kichban_tapXX_*.md).
Mỗi `## HỒI N` lấy thẻ [BGM] ĐẦU TIÊN -> mood của nhạc nền hồi đó.
So với "bed" trong .work/edition.py (đúng thứ build_audio3.py dùng).

Chạy:  py -3 .work/_qc_bgm_vs_script.py
"""
import ast
import collections
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

# ------------------------------------------------- mood trong kịch bản -> file đảm nhiệm
# Mỗi mẫu gắn với file + nhóm từ khóa. "Piano ấm áp" khác "Piano tối giản" nên tách.
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
    (r"ambient|Ambient|Dark Ambient|Dark ambient", "bgm_ambient_deep.mp3"),
]


def moods_of(text):
    """Tất cả mood nhạc có trong 1 mô tả [BGM]."""
    out = []
    for pat, f in MOOD:
        if re.search(pat, text, re.IGNORECASE) and f not in out:
            out.append(f)
    # "Piano ấm áp / trang ngọng" và "Piano tối giản" là 2 mood khác nhau:
    # nếu đã khớp piano_warm thì bỏ piano_minimal (tránh khớp kép).
    if "bgm_piano_warm.mp3" in out:
        out = [f for f in out if f != "bgm_piano_minimal.mp3"]
    return out



# ------------------------------------------------- bed trong edition.py
src = (WORK / "edition.py").read_text(encoding="utf-8")
ep_re = re.compile(r'^\s{4}"(\d\d)":\s*\{', re.M)
ep_pos = [(m.group(1), m.start(), m.end()) for m in ep_re.finditer(src)]
beds = {}
for i, (ep, _s, e) in enumerate(ep_pos):
    end = ep_pos[i + 1][1] if i + 1 < len(ep_pos) else len(src)
    chunk = src[e:end]
    b = chunk.find('"bed":')
    if b == -1:
        continue
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

# ------------------------------------------------- mood từng hồi trong kịch bản VN
script_mood = {}
for p in sorted((ROOT / "01_KICH_BAN").glob("Tap*/kichban_tap*.md")):
    if "REVIEW" in p.name:
        continue
    if "_EN" in p.name or "_KO" in p.name or "_JA" in p.name:
        continue
    m = re.search(r"Tap(\d\d)", str(p.parent))
    if not m:
        continue
    ep = m.group(1)
    txt = p.read_text(encoding="utf-8")
    # chia theo heading HỒI
    parts = re.split(r"^##\s*HỒI\s+(\d+)\s*:", txt, flags=re.M)
    for j in range(1, len(parts), 2):
        act = int(parts[j])
        body = parts[j + 1]
        bm = re.search(r"\*\*\[BGM\]:\*\*\s*(.+)", body)
        if not bm:
            continue
        raw = bm.group(1).strip()
        mm = moods_of(raw)
        if mm:
            script_mood.setdefault(ep, {})[act] = (mm, raw[:80])

print("=" * 96)
print("BED TRONG edition.py  vs  MOOD [BGM] TRONG KỊCH BẢN")
print("=" * 96)

rows = []
for ep in sorted(beds):
    for act in range(1, 6):
        v = beds[ep].get(act)
        got = [v] if isinstance(v, str) else list(v or [])
        want, raw = script_mood.get(ep, {}).get(act, ([], ""))
        # music box ở đầu Hồi 1 là intro kênh (build_audio3.py đặt sẵn ở t=0), không phải bed hồi
        intro = (act == 1 and "bgm_music_box.mp3" in want)
        # ambient_deep luôn có sẵn ở lớp sàn -31 dB (build_audio3.py) => không tính là thiếu
        need = [w for w in want if w != "bgm_ambient_deep.mp3"]
        if not need:
            state = "OK"
        elif intro:
            state = "OK"
        elif set(need) <= set(got):
            state = "OK"
        else:
            state = "SAI"
        rows.append((ep, act, state, want, got, raw))

n_ok = sum(1 for r in rows if r[2] == "OK")
n_sai = sum(1 for r in rows if r[2] == "SAI")
n_q = sum(1 for r in rows if r[2] == "?")
print(f"Tổng slot hồi: {len(rows)} | khớp: {n_ok} | SAI: {n_sai} | chưa có mood trong kịch bản: {n_q}")
print()
print(f"{'Tập':<5}{'H':<3}{'KQ':<6}{'Kịch bản đòi':<30}{'edition.py đang dùng'}")
print("-" * 118)
for ep, act, state, want, got, raw in rows:
    if state == "OK":
        continue
    mark = "SAI" if state == "SAI" else "?"
    print(f"T{ep:<4}H{act:<2}{mark:<6}{(', '.join(want) or '(khong ro)'):<42}{', '.join(got)}")
    if state == "SAI":
        print(f"      kịch bản: {raw}")

print()
print("=" * 96)
print("TÓM TẮT THEO TẬP")
print("=" * 96)
per = collections.defaultdict(lambda: [0, 0])
for ep, act, state, want, got, raw in rows:
    if state == "OK":
        per[ep][0] += 1
    elif state == "SAI":
        per[ep][1] += 1
for ep in sorted(per):
    ok, sai = per[ep]
    flag = "" if sai == 0 else "   <-- SAI"
    print(f"  Tập {ep}: khớp {ok}/5, sai {sai}{flag}")
