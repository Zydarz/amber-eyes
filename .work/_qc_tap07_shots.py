#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC A9.2 — bảng shot Tập 07 (mục 6 kế hoạch) theo 147 câu.

Cùng bộ cổng với _qc_tap06_shots_v2.py (chuẩn hiện hành) + phát hiện ID câu
cũ (164 câu) còn sót trong bảng.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
BG_DIR = ROOT / "assets" / "bg"
PLAN = ROOT / "02_SAN_XUAT" / "Tap07" / "KeHoach_Video_Tap07.md"

BANNED = ["hiếp dâm", "chặt xác", "cắt cổ", "máu me", "tự tử", "thắt cổ",
          "thi thể", "sát hại", "đòn roi", "trói", "bầm", "đầu độc",
          "diệt cỏ", "bỏ đói", "móc áo"]

script = json.loads((WORK / "script_tap07.json").read_text(encoding="utf-8-sig"))
sent, order = {}, []
for el in script:
    for i, s in enumerate(el.get("sentences") or [], 1):
        sid = f"{el['id']}#{i}"
        sent[sid] = {"role": el.get("role"), "text": s["text"]}
        order.append(sid)
# script gộp hai vai kể chuyện thành "N"; bảng shot tách N1 (mẹ) / N2 (nhân chứng)
N_ELEMENT = {"1.07": "N1", "4.03": "N2"}
ROLE_OF = {sid: N_ELEMENT.get(sid.split("#")[0], d["role"]) for sid, d in sent.items()}

lines = PLAN.read_text(encoding="utf-8-sig").split("\n")
rows = []
for ln in lines:
    if not re.match(r"^\|\s*[1-5]-\d+\s*\|", ln):
        continue
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    c += [""] * (9 - len(c))
    rows.append({"id": c[0], "cau": c[1], "vai": c[2], "mau": c[3], "nen": c[4],
                 "chu": c[5], "beat": c[6], "nv": c[7], "tr": c[8]})

RANGE = re.compile(r"`(\d\.\d+)#(\d+)`\s*[–-]\s*`#(\d+)`")
SINGLE = re.compile(r"`(\d\.\d+)#(\d+)`")
IDONLY = re.compile(r"`(\d\.\d+)`")


def expand(cell):
    out = []
    for m in RANGE.finditer(cell):
        e, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        out.extend(f"{e}#{i}" for i in range(a, b + 1))
    rest = RANGE.sub("", cell)
    for m in SINGLE.finditer(rest):
        out.append(f"{m.group(1)}#{m.group(2)}")
    for m in IDONLY.finditer(rest):
        out.append(m.group(1))
    return out


errors, warns = [], []


def bad(m):
    errors.append(m)


def warn(m):
    warns.append(m)


print(f"Kịch bản: {len(sent)} câu · Bảng shot: {len(rows)} dòng\n")

# ------------------------------------------------------------- 1. phủ câu
covered, dups = [], []
for r in rows:
    for sid in expand(r["cau"]):
        if sid in sent:
            if sid in covered:
                dups.append((sid, r["id"]))
            covered.append(sid)
missing = [s for s in order if s not in covered]
if missing:
    bad(f"1. SÓT {len(missing)} câu chưa có shot: {missing}")
if dups:
    bad(f"1. Trùng câu: {dups}")
print(f"[{'OK  ' if not missing and not dups else 'FAIL'}] 1. Phủ câu: "
      f"{len(set(covered))}/{len(order)} câu, trùng {len(dups)}")

# ------------------------------------------------------------- 1b. ID câu cũ sót
stale = []
for r in rows:
    for sid in expand(r["cau"]):
        if "#" in sid and sid not in sent:
            stale.append((r["id"], sid))
if stale:
    bad(f"1b. ID câu không tồn tại (còn sót từ bảng 164 câu): {stale}")
print(f"[{'OK  ' if not stale else 'FAIL'}] 1b. Không ID câu cũ sót ({len(stale)} lỗi)")

# ------------------------------------------------------------- 2. vai
badvai = []
for r in rows:
    ids = [s for s in expand(r["cau"]) if s in sent]
    if not ids:
        continue
    pv = r["vai"]
    if pv in ("—", "-", ""):
        badvai.append((r["id"], "vai rong"))
        continue
    sv = {ROLE_OF[s] for s in ids}
    if sv != {pv}:
        badvai.append((r["id"], f"bang={pv} script={sv}"))
if badvai:
    bad(f"2. Sai vai: {badvai}")
print(f"[{'OK  ' if not badvai else 'FAIL'}] 2. Cột Vai khớp script ({len(badvai)} sai)")

# ------------------------------------------------------------- 3. handoff
badoff = []
for i, r in enumerate(rows):
    ho = re.findall(r"→([A-Z0-9+]+)", r["nv"])
    ho_last = re.findall(r"→([A-Z0-9+]+)", r["tr"])
    if ho_last:
        badoff.append((r["id"], f"→ dang o cot chuyen tiep: {ho_last}"))
    nxt = rows[i + 1] if i + 1 < len(rows) else None
    exp = []
    if nxt and r["vai"] in ("H", "D", "C", "N1", "N2") and nxt["vai"] in ("H", "D", "C", "N1", "N2") \
            and nxt["vai"] != r["vai"]:
        exp = [nxt["vai"]]
    if ho != exp:
        badoff.append((r["id"], f"handoff={ho} expected={exp}"))
if badoff:
    bad(f"3. Handoff sai: {badoff}")
print(f"[{'OK  ' if not badoff else 'FAIL'}] 3. Handoff = vai dòng kế tiếp ({len(badoff)} sai)")

# ------------------------------------------------------------- 4. nền
bg_files = {p.stem for p in BG_DIR.glob("*.png")}
missbg = []
for r in rows:
    for c in re.findall(r"`(t7_[^`]+)`", r["nen"]):
        if c not in bg_files:
            missbg.append((r["id"], c))
if missbg:
    bad(f"4. Thiếu ảnh nền: {missbg}")
print(f"[{'OK  ' if not missbg else 'FAIL'}] 4. Ảnh nền tồn tại ({len(missbg)} thiếu)")

# ------------------------------------------------------------- 5. số trên hình
UNIT = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy",
        8: "tám", 9: "chín"}
ORD = {1: "thứ nhất", 2: "thứ hai", 3: "thứ ba", 4: "thứ tư"}


def num2vn(n):
    if n < 10:
        return [UNIT[n]]
    if n < 20:
        return ["mười " + ("lăm" if n == 15 else UNIT[n % 10])]
    if n < 100:
        tens = {2: "hai mươi", 3: "ba mươi", 4: "bốn mươi", 5: "năm mươi",
                6: "sáu mươi", 7: "bảy mươi", 8: "tám mươi", 9: "chín mươi"}[n // 10]
        o = n % 10
        if o == 0:
            return [tens]
        variants = []
        if o == 4:
            variants = ["tư", "bốn"]
        elif o == 5:
            variants = ["lăm", "năm"]
        else:
            variants = [UNIT[o]]
        return [tens + " " + v for v in variants]
    return [str(n)]


def has_num(text, n):
    t = text.lower()
    if re.search(r"(?<!\d)" + re.escape(str(n)) + r"(?!\d)", t):
        return True
    if re.search(r"(?<!\d)0" + str(n) + r"(?!\d)", t):
        return True
    if any(v in t for v in num2vn(n)):
        return True
    if n in ORD and ORD[n] in t:
        return True
    return False


badnum = []
for r in rows:
    ids = [s for s in expand(r["cau"]) if s in sent]
    if not ids:
        continue
    txt = " ".join(sent[s]["text"] for s in ids).lower()
    chu = re.sub(r"[*_“”]", "", r["chu"])
    for n in set(int(x) for x in re.findall(r"(?<!\d)\d{1,2}(?!\d)", chu)):
        if n == 0:
            continue
        if not has_num(txt, n):
            badnum.append((r["id"], n, r["chu"][:70]))
if badnum:
    bad(f"5. Số trên hình không có trong câu: {badnum}")
print(f"[{'OK  ' if not badnum else 'FAIL'}] 5. Số trên hình có trong câu ({len(badnum)} sai)")

# ------------------------------------------------------------- 6. trích dẫn
def norm(s):
    s = s.lower().replace("…", " ").replace("...", " ")
    s = re.sub(r"[“”\"'’‘.,;:!?()]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


badq = []
for r in rows:
    ids = [s for s in expand(r["cau"]) if s in sent]
    if not ids:
        continue
    txt = norm(" ".join(sent[s]["text"] for s in ids))
    for q in re.findall(r"“(.+?)”", r["chu"]):
        words = norm(q).split()
        hit = False
        for k in range(0, max(1, len(words) - 3)):
            chunk = " ".join(words[k:k + 4])
            if chunk and chunk in txt:
                hit = True
                break
        if not hit:
            badq.append((r["id"], q[:80]))
if badq:
    bad(f"6. Câu trích không nguyên văn: {badq}")
print(f"[{'OK  ' if not badq else 'FAIL'}] 6. Câu trích nguyên văn ({len(badq)} sai)")

# ------------------------------------------------------------- 7. từ cấm
badw = []
for r in rows:
    low = r["chu"].lower()
    for w in BANNED:
        if w in low:
            badw.append((r["id"], w))
if badw:
    bad(f"7. Từ cấm: {badw}")
print(f"[{'OK  ' if not badw else 'FAIL'}] 7. Không từ cấm ({len(badw)} phát hiện)")

# ------------------------------------------------------------- 8. thẻ kết
last = rows[-1]
ok12 = ("HỒ SƠ TẬP 07 · ĐÃ ĐÓNG" in last["chu"] and "AMBER EYES" in last["chu"])
if not ok12:
    bad(f"8. Thẻ kết cuối không đúng H12: {last['id']} · {last['chu'][:60]}")
print(f"[{'OK  ' if ok12 else 'FAIL'}] 8. Thẻ kết H12 ({last['id']})")

# ------------------------------------------------------------- 9. thứ tự
pos = {s: i for i, s in enumerate(order)}
prev = -1
badorder = []
for r in rows:
    ids = [s for s in expand(r["cau"]) if s in sent]
    if not ids:
        continue
    p = min(pos[s] for s in ids)
    if p < prev:
        badorder.append((r["id"], p, prev))
    prev = p
if badorder:
    bad(f"9. Shot sai thứ tự thời gian: {badorder}")
print(f"[{'OK  ' if not badorder else 'FAIL'}] 9. Thứ tự thời gian ({len(badorder)} sai)")

# ------------------------------------------------------------- 10. id trùng
ids_all = [r["id"] for r in rows]
dupid = sorted({i for i in ids_all if ids_all.count(i) > 1})
if dupid:
    bad(f"10. Shot id trùng: {dupid}")
print(f"[{'OK  ' if not dupid else 'FAIL'}] 10. Shot id duy nhất")

# ------------------------------------------------------------- 11. beat trỏ câu
badbeat = []
for r in rows:
    for m in re.findall(r"`(\d\.\d+#\d+)`", r["beat"]):
        if m not in sent:
            badbeat.append((r["id"], m))
if badbeat:
    warn(f"11. Beat trỏ tới câu không tồn tại: {badbeat}")
print(f"[{'OK  ' if not badbeat else 'WARN'}] 11. Beat trỏ câu hợp lệ ({len(badbeat)} lỗi)")

print("\n" + "=" * 60)
if errors:
    print(f">>> {len(errors)} LỖI:")
    for e in errors:
        print("   -", e)
else:
    print(">>> TẤT CẢ QC A9.2 ĐẠT CHUẨN <<<")
if warns:
    print(f">>> {len(warns)} CẢNH BÁO:")
    for w in warns:
        print("   -", w)
sys.exit(1 if errors else 0)
