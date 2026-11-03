#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng kiểm đầu vào cho bản tiếng Anh Tập 03 — trước khi dựng hình.

Kiểm:
  1. Tap03_EN_master.mp3 có dài khớp timeline_s_EN_t03.json["total"] (±0,05 s)
  2. WAV audio_master_EN_t03.wav khớp mp3 (±0,05 s)
  3. shots_EN_t03.json phủ 100% câu của timeline, đúng thứ tự, không thừa không thiếu
  4. Mọi shot có bg (file nền tồn tại trong assets/bg)
  5. Shot cuối có chữ (thẻ kết) — H12
  6. Mỗi shot 3–15 s — H10
  7. Shot ID đúng định dạng, liên tục, không trùng
  8. Chữ trên hình: mọi con số phải truy được về câu EN đang đọc (H6)

Trả exit code 1 nếu có lỗi.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FFP = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

errors = []
warns = []


def dur(p: Path) -> float:
    out = subprocess.run(
        [str(FFP), "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(p)],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    return float(out.stdout.strip())


tl = json.loads((W / "timeline_s_EN_t03.json").read_text(encoding="utf-8"))
sh = json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))
script = json.loads((W / "script_tap03_EN.json").read_text(encoding="utf-8"))

TOTAL = tl["total"]
shots = sh["shots"]

print(f"timeline.total = {TOTAL:.3f} s   items = {len(tl['items'])}   shots = {len(shots)}")

# ---------------------------------------------------------------- 1 & 2: audio
master = ROOT / "02_SAN_XUAT" / "Tap03_EN" / "xuat_ban" / "Tap03_EN_master.mp3"
if not master.exists():
    errors.append(f"khong co file master: {master}")
else:
    d = dur(master)
    print(f"master mp3      = {d:.3f} s   ({master.stat().st_size} bytes)")
    if abs(d - TOTAL) > 0.05:
        errors.append(f"H14: master mp3 {d:.3f}s lech timeline.total {TOTAL:.3f}s "
                      f"(lech {d - TOTAL:+.3f}s) -> phai tai parse_shots + dung lai hinh")
    else:
        print("  OK: khớp timeline.total ±0,05 s")

wav = W / "audio_master_EN_t03.wav"
if wav.exists():
    dw = dur(wav)
    print(f"master wav      = {dw:.3f} s")
    if abs(dw - TOTAL) > 0.05:
        errors.append(f"master wav {dw:.3f}s lech timeline.total {TOTAL:.3f}s")
    if abs(dw - d) > 0.05:
        errors.append(f"wav {dw:.3f}s lech mp3 {d:.3f}s")
else:
    warns.append("khong co audio_master_EN_t03.wav (khong bat buoc)")

# ---------------------------------------------------------------- 3: shots phu cau
tl_ids = [it["id"] for it in tl["items"]]
shot_ids = []
for s in shots:
    for sid in s.get("sentences", []):
        shot_ids.append(sid)

if shot_ids != tl_ids:
    only_shot = [x for x in shot_ids if x not in set(tl_ids)]
    only_tl = [x for x in tl_ids if x not in set(shot_ids)]
    errors.append(
        f"shots phu cau khong dung timeline: shot={len(shot_ids)} tl={len(tl_ids)}"
        f" | chi trong shot={only_shot[:8]} | chi trong timeline={only_tl[:8]}")
    if sorted(shot_ids) == sorted(tl_ids):
        errors.append("  -> thu tu SAI (cung tap roi khac thu tu)")
else:
    print(f"  OK: {len(shot_ids)} cau, phu 100% va dung thu tu")

# ---------------------------------------------------------------- 4: nen
BG = ROOT / "assets" / "bg"
missing_bg = set()
for s in shots:
    for key in ("bg", "bg2"):
        v = s.get(key)
        if not v:
            continue
        for name in re.findall(r"[\w\-]+\.(?:png|jpg|jpeg)", str(v)):
            if not (BG / name).exists():
                missing_bg.add(name)
if missing_bg:
    errors.append(f"thieu file nen: {sorted(missing_bg)[:12]} (n={len(missing_bg)})")
else:
    print("  OK: moi file nen ton tai")

# ---------------------------------------------------------------- 5: shot cuoi co chu
last = shots[-1]
if not str(last.get("beat_text", "")).strip() and not str(last.get("text", "")).strip():
    errors.append(f"H12: shot cuoi {last['id']} khong co chu (the ket)")
else:
    print(f"  OK: shot cuoi {last['id']} co chu")

# ---------------------------------------------------------------- 6: thoi luong shot 3-15s
bad_len = [(s["id"], round(s["end"] - s["start"], 2)) for s in shots
           if not (3.0 <= (s["end"] - s["start"]) <= 15.0)]
if bad_len:
    warns.append(f"H10: {len(bad_len)} shot ngoai 3-15s: {bad_len[:10]}")

# ---------------------------------------------------------------- 7: dinh dang ID
ids = [s["id"] for s in shots]
if len(set(ids)) != len(ids):
    errors.append("trung shot id")
pat = re.compile(r"^[1-5]-\d{2}$")
badid = [i for i in ids if not pat.match(i)]
if badid:
    errors.append(f"shot id sai dinh dang {pat.pattern}: {badid[:10]}")

# shot lien tuc theo thu tu: start/end chay lien
gaps = []
for a, b in zip(shots, shots[1:]):
    if abs(b["start"] - a["end"]) > 0.02:
        gaps.append((a["id"], a["end"], b["id"], b["start"]))
if gaps:
    warns.append(f"{len(gaps)} khe gap giua cac shot: {gaps[:6]}")

# moc thoi gian shot phai nam trong timeline
oob = [(s["id"], s["start"], s["end"]) for s in shots
       if s["start"] < -0.001 or s["end"] > TOTAL + 0.001]
if oob:
    errors.append(f"shot vuot bien timeline: {oob[:6]}")

# ---------------------------------------------------------------- 8: so tren hinh
S = {}
ROLE_OF = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]
            ROLE_OF[s["id"]] = e.get("vai") or e.get("role")


def screen_text(shot) -> str:
    """Chu that tren hinh = segments[*].elems[*][1] (khong phai beat_text — do la ghi chu doi tap)."""
    out = []
    for sg in shot.get("segments") or []:
        for el in sg.get("elems") or []:
            out.append(str(el[1]))
    return " | ".join(out)

MONTHS = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6",
          "july": "7", "august": "8", "september": "9", "october": "10", "november": "11",
          "december": "12"}
NUMWORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
            "seven": "7", "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12",
            "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50", "hundred": "100",
            "thousand": "1000"}
STRUCT = ("ACT", "STAGE", "LAYER", "CONCEPT", "RED FLAG", "FLAG", "EPISODE", "CASE FILE", "FILE")
num_err = []
_eff, _prev = [], []
for _s in shots:
    if _s.get("sentences"):
        _prev = _s["sentences"]
    _eff.append(_prev)
for s, eff in zip(shots, _eff):
    ctx = " ".join(S.get(x, "") for x in eff)
    flat = ctx.replace(" ", "").lower()
    screen = screen_text(s)
    screen = re.sub(r"→\s*`?#\d+`?:", " ", screen)
    allowed = set()
    for a in re.findall(r"\d+", flat):
        allowed.update({a, a.zfill(2), str(int(a))})
    for w, d in MONTHS.items():
        if w in flat:
            allowed.update({d, d.zfill(2)})
    for w, d in NUMWORDS.items():
        if w in flat:
            allowed.update({d, d.zfill(2)})
    for tok in set(re.findall(r"\d[\d,.]*", screen)):
        t = tok.replace(",", "").replace(".", "")
        if tok in allowed or t in allowed or tok in flat or t in flat:
            continue
        if any(re.search(r"\b" + re.escape(st) + r"\s*" + re.escape(tok) + r"\b", screen, re.I)
               for st in STRUCT):
            continue
        num_err.append((s["id"], tok, ctx[:70]))
if num_err:
    for e in num_err[:15]:
        print("  [SO] ", e)
    errors.append(f"H6: {len(num_err)} so tren hinh khong truy duoc ve cau EN")
else:
    print("  OK: moi so tren hinh deu truy duoc ve cau EN")

# ---------------------------------------------------------------- 9: trich dan nguyen van
q_err = []
_eff2, _prev2 = [], []
for _s in shots:
    if _s.get("sentences"):
        _prev2 = _s["sentences"]
    _eff2.append(_prev2)
for s, eff in zip(shots, _eff2):
    ctx = " ".join(S.get(x, "") for x in eff)
    screen = screen_text(s)
    for q in re.findall(r"[\"“]([^\"”]+)[\"”]", screen):
        for frag in [f.strip() for f in q.split("…") if f.strip()]:
            if frag not in ctx:
                q_err.append((s["id"], frag[:50]))
if q_err:
    for e in q_err[:10]:
        print("  [QUOTE] ", e)
    warns.append(f"{len(q_err)} trich dan tren hinh khong nguyen van trong cau")

# ---------------------------------------------------------------- 10: vai noi khop kich ban
role_err = []
for s in shots:
    if not s.get("sentences"):
        continue
    roles = {ROLE_OF.get(x) for x in s["sentences"]}
    roles.discard(None)
    if len(roles) > 1:
        role_err.append((s["id"], sorted(roles)))
    elif roles and s.get("role") and list(roles)[0] != s.get("role"):
        # script ghi N1/N2 chung lai la 'N' -> hop le
        if not (list(roles)[0] == "N" and s.get("role") in ("N1", "N2")):
            role_err.append((s["id"], f"shot={s.get('role')} script={list(roles)[0]}"))
if role_err:
    for e in role_err[:10]:
        print("  [ROLE] ", e)
    errors.append(f"H13: {len(role_err)} shot co vai khong khop kich ban")
else:
    print("  OK: vai noi khop kich ban o moi shot")

# ---------------------------------------------------------------- 11: moi shot deu co chu
no_text = [s["id"] for s in shots if not screen_text(s).strip()]
if no_text:
    warns.append(f"{len(no_text)} shot khong co chu tren hinh: {no_text[:12]}")

# ---------------------------------------------------------------- 12: nen lap lai qua 4 shot
run = []
worst = []
for s in shots:
    bg = s.get("bg")
    if run and run[-1][0] == bg:
        run[-1][1] += 1
    else:
        run.append([bg, 1])
for bg, n in run:
    if n > 4:
        worst.append((bg, n))
if worst:
    warns.append(f"H10: {len(worst)} chuoi nen lap > 4 shot: {worst[:8]}")

# ---------------------------------------------------------------- ket qua
print()
if warns:
    print("CANH:")
    for x in warns:
        print("  -", x)
if errors:
    print("LOI:")
    for x in errors:
        print("  -", x)
    sys.exit(1)
print("PASS: dau vao EN Tap03 hop le")
sys.exit(0)
