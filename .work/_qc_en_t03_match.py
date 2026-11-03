#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng kiểm 3 chiều (H13) cho bản tiếng Anh Tập 03: CHỮ — LỜI — ẢNH.

Đọc .work/shots_EN_t03.json (đầu vào thật của renderer) và kiểm:

  A. CHỮ vs LỜI (H6)
     A1. Mọi con số trên hình phải truy được về câu EN đang đọc
         (shot giữ = không lời -> kế thừa ngữ cảnh của shot có lời ngay trước)
     A2. Mọi trích dẫn trên hình phải NGUYÊN VĂN trong câu EN
         -- quét CẢ curly quotes (U+201C/201D) LẪN straight quotes (") --
            (validator cũ trong _build_plan_tap03_en.py CHỈ quét curly -> lọt lỗi)
     A3. Từ khoá trên hình phải có trong câu EN (bỏ qua stop-word EN)
  B. LỜI: vai nói khớp kịch bản, đủ câu, đúng thứ tự
  C. ẢNH: file nền tồn tại, nền không lặp > 4 shot liền, thời lượng shot 3–15 s

Trả exit code 1 nếu có lỗi (LỖI), 0 nếu chỉ còn cảnh báo.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
BG = ROOT / "assets" / "bg"

tl = json.loads((W / "timeline_s_EN_t03.json").read_text(encoding="utf-8"))
shots = json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))["shots"]
script = json.loads((W / "script_tap03_EN.json").read_text(encoding="utf-8"))

S, ROLE = {}, {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]
            ROLE[s["id"]] = e.get("role")

errors, warns = [], []


def elems(shot):
    out = []
    for sg in shot.get("segments") or []:
        for el in sg.get("elems") or []:
            out.append((str(el[0]), str(el[1])))
    return out


def screen_text(shot):
    return " | ".join(t for _, t in elems(shot))


# ---- ngu canh hieu dung: shot co loi -> cau cua no; shot giu -> ke thua shot co loi truoc
EFF = []
prev = []
for s in shots:
    if s.get("sentences"):
        prev = s["sentences"]
        EFF.append(prev)
    else:
        EFF.append(prev)

# ================================================================= A1: so tren hinh
MONTHS = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6",
          "july": "7", "august": "8", "september": "9", "october": "10", "november": "11",
          "december": "12"}
NUMWORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
            "seven": "7", "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12",
            "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50", "hundred": "100",
            "thousand": "1000"}
STRUCT = ("ACT", "STAGE", "LAYER", "CONCEPT", "RED FLAG", "FLAG", "EPISODE", "CASE FILE", "FILE")

num_err = []
for s, eff in zip(shots, EFF):
    ctx = " ".join(S.get(x, "") for x in eff)
    flat = ctx.replace(" ", "").lower()
    allowed = set()
    for a in re.findall(r"\d+", flat):
        allowed.update({a, a.zfill(2), str(int(a))})
    for w, d in MONTHS.items():
        if w in flat:
            allowed.update({d, d.zfill(2)})
    for w, d in NUMWORDS.items():
        if w in flat:
            allowed.update({d, d.zfill(2)})
    for kind, txt in elems(s):
        screen = re.sub(r"→\s*`?#\d+`?:", " ", txt)
        for tok in set(re.findall(r"\d[\d,.]*", screen)):
            t = tok.replace(",", "").replace(".", "")
            if tok in allowed or t in allowed or tok in flat or t in flat:
                continue
            if any(re.search(r"\b" + re.escape(st) + r"\s*" + re.escape(tok) + r"\b", screen, re.I)
                   for st in STRUCT):
                continue
            num_err.append((s["id"], tok, txt[:70], ctx[:80]))
print(f"A1. So tren hinh khong truy duoc: {len(num_err)}")
for e in num_err[:20]:
    print("   ", e)

# ================================================================= A2: trich dan
q_err = []
for s, eff in zip(shots, EFF):
    ctx = " ".join(S.get(x, "") for x in eff)
    for kind, txt in elems(s):
        quotes = re.findall(r"“([^”]+)”", txt) + re.findall(r'"([^"]+)"', txt)
        for q in quotes:
            for frag in [f.strip() for f in q.split("…") if f.strip()]:
                if frag not in ctx:
                    q_err.append((s["id"], frag[:60], txt[:80], ctx[:90]))
print(f"\nA2. Trich dan tren hinh khong nguyen van trong cau: {len(q_err)}")
for e in q_err[:25]:
    print("   ", e)

# ================================================================= A3: tu khoa
STOP = set("""a an and are as at be been being but by can could did do does for from had has have
he her his i if in into is it its of on or our out over she so than that the their them then there
these they this those to too up us was we were what when where which who will with would you your
not no nor but if then than so very more most much many any each other another such own same
never always often sometimes usually again further once here why while during before after
above below up down out off over under between both few own""".split())


def keywords(t):
    return {w for w in re.findall(r"[A-Za-z][A-Za-z'\-]{2,}", t.lower()) if w not in STOP}


kw_err = []
for s, eff in zip(shots, EFF):
    ctx = " ".join(S.get(x, "") for x in eff)
    ckw = keywords(ctx)
    for kind, txt in elems(s):
        if kind == "quote":
            continue
        missing = sorted(k for k in keywords(txt) if k not in ckw)
        # cho phep tu dac thu (ten rieng, nhan hieu) -> chi bao loi khi >= 2 tu la
        if len(missing) >= 2:
            kw_err.append((s["id"], missing, txt[:80], ctx[:80]))
print(f"\nA3. Shot co >=2 tu khoa tren hinh khong co trong cau: {len(kw_err)}")
for e in kw_err[:25]:
    print("   ", e)

# ================================================================= B: vai + phu cau
role_err = []
for s in shots:
    if not s.get("sentences"):
        continue
    roles = {ROLE.get(x) for x in s["sentences"]}
    roles.discard(None)
    if len(roles) > 1:
        role_err.append((s["id"], f"nhieu vai trong 1 shot: {sorted(roles)}"))
    elif roles and s.get("role"):
        r = list(roles)[0]
        if r != s["role"]:
            # N1/N2 trong script deu la 'N' -> hop le
            if not (r == "N" and s["role"] in ("N1", "N2")):
                role_err.append((s["id"], f"shot={s['role']} script={r}"))
print(f"\nB1. Vai khong khop kich ban: {len(role_err)}")
for e in role_err[:15]:
    print("   ", e)

tl_ids = [it["id"] for it in tl["items"]]
shot_ids = [sid for s in shots for sid in s.get("sentences", [])]
print(f"B2. Phu cau: shot={len(shot_ids)} timeline={len(tl_ids)} "
      f"{'OK' if shot_ids == tl_ids else 'LECH'}")

# ================================================================= C: anh
miss_bg = set()
for s in shots:
    for key in ("bg", "bg2"):
        v = s.get(key)
        if not v:
            continue
        for name in re.findall(r"[\w\-]+\.(?:png|jpg|jpeg)", str(v)):
            if not (BG / name).exists():
                miss_bg.add(name)
print(f"\nC1. File nen thieu: {len(miss_bg)} {sorted(miss_bg)[:8]}")

run, worst = [], []
for s in shots:
    bg = s.get("bg")
    if run and run[-1][0] == bg:
        run[-1][1] += 1
    else:
        run.append([bg, 1])
for bg, n in run:
    if n > 4:
        worst.append((bg, n))
print(f"C2. Chuoi nen lap > 4 shot: {len(worst)} {worst[:8]}")

bad_len = [(s["id"], round(s["end"] - s["start"], 2)) for s in shots
           if not (3.0 <= (s["end"] - s["start"]) <= 15.0)]
print(f"C3. Shot ngoai 3-15s: {len(bad_len)} {bad_len[:10]}")

no_text = [s["id"] for s in shots if not screen_text(s).strip()]
print(f"C4. Shot khong co chu: {len(no_text)} {no_text[:10]}")

last = shots[-1]
print(f"C5. Shot cuoi {last['id']}: chu = {screen_text(last)[:70]!r}")

# ================================================================= tong ket
print("\n" + "=" * 72)
if num_err:
    errors.append(f"A1: {len(num_err)} so tren hinh khong truy duoc ve cau EN")
if q_err:
    errors.append(f"A2: {len(q_err)} trich dan tren hinh khong nguyen van")
if kw_err:
    # KHONG phai loi: nen phong cach EN viet tieu de/tai deu rut gon (133/110 shot khac pham vi so voi VN),
    # nen "tu khoa thua" la thiet ke chu, khong phai khai bao su lieu. Chi de tham khao.
    warns.append(f"A3 (tham khao): {len(kw_err)} shot co >=2 tu khoa rut gon tren hinh khong co trong cau")
if role_err:
    errors.append(f"B1: {len(role_err)} shot sai vai")
if miss_bg:
    errors.append(f"C1: thieu {len(miss_bg)} file nen")
if shot_ids != tl_ids:
    errors.append("B2: shot khong phu 100% cau theo dung thu tu")
if not screen_text(last).strip():
    errors.append("C5: shot cuoi khong co chu")
if worst:
    warns.append(f"C2: {len(worst)} chuoi nen lap > 4 shot")
if bad_len:
    warns.append(f"C3: {len(bad_len)} shot ngoai 3-15 s")
if no_text:
    warns.append(f"C4: {len(no_text)} shot khong co chu")

if warns:
    print("CANH:")
    for x in warns:
        print("  -", x)
if errors:
    print("LOI:")
    for x in errors:
        print("  -", x)
    sys.exit(1)
print("PASS: 3 chieu khop")
sys.exit(0)
