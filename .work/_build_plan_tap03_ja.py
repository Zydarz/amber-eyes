#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng bảng shot Tập 03 bản tiếng Nhật từ bảng VN + shots_text_tap03_JA.json.

Tự kiểm (exit code khác 0 nếu lỗi):
  1. mọi shot có chữ trong bảng VN đều có bản JA
  2. cụm beat JA phải có thật trong câu JA của shot
  3. mọi con số trên hình phải truy được về câu JA (hoặc tiêu đề hồi)
  4. trích dẫn trong ngoặc kép phải nguyên văn trong câu JA
  5. shot nào không có câu JA thì không được có số trên hình
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

ja_table = json.loads((W / "shots_text_tap03_JA.json").read_text(encoding="utf-8-sig"))
ja_table = {k: v for k, v in ja_table.items() if not k.startswith("_")}
script = json.loads((W / "script_tap03_JA.json").read_text(encoding="utf-8-sig"))
S = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]

vn_path = ROOT / "02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md"
vn_lines = vn_path.read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn_lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_lines) if i > i0 and l.startswith("**Tổng:"))

ACT_TITLES_JA = {
    1: "第1幕 · コロラドの電話ボックスから届く深夜の通話",
    2: "第2幕 · 現場と狩りの連鎖――代替の階段",
    3: "第3幕 · 心理剖検――内省型サイコパスの脳の内側",
    4: "第4幕 · FBIとの対話――犯罪プロファイリング技術の基礎",
    5: "第5幕 · 判決、赤い警鐘の教訓＆終幕",
}


def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


errors = []
warnings = []
out_lines = []
used = set()
n_rows = 0

for l in vn_lines[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        out_lines.append(l)
        continue
    n_rows += 1
    sid = m.group(1)
    c = l.strip().strip("|").split("|")
    if sid not in ja_table:
        if c[5].strip() != "—":
            errors.append(f"{sid}: thiếu bản JA (chu_vn = {c[5].strip()[:60]!r})")
        out_lines.append(l)
        continue
    used.add(sid)
    chu, phrases = ja_table[sid][0], ja_table[sid][1]
    override = ja_table[sid][2] if len(ja_table[sid]) > 2 else None
    ids = sents(c[1])
    ctx = " ".join(S.get(x, "") for x in ids)
    flat = ctx.replace(" ", "")

    # --- beat: thay cụm `ở "…"` bằng cụm JA
    if override is not None:
        beat = override
    else:
        vn_ph = re.findall(r'ở "([^"]+)"', c[6])
        if len(vn_ph) != len(phrases):
            errors.append(f"{sid}: {len(vn_ph)} cụm beat VN ≠ {len(phrases)} cụm JA ({vn_ph} vs {phrases})")
            beat = c[6]
        else:
            it = iter(phrases)
            beat = re.sub(r'ở "([^"]+)"', lambda _: 'ở "' + next(it) + '"', c[6])

    # --- cụm beat JA có thật trong câu JA (phrase_time() tìm trong text câu)
    for p in re.findall(r'ở "([^"]+)"', beat):
        if p not in ctx:
            errors.append(f"{sid}: cụm beat \"{p}\" không có trong câu JA: \"{ctx[:50]}...\"")

    # --- trích dẫn nguyên văn
    for q in re.findall(r"“([^”]+)”", chu):
        for frag in [f.strip() for f in q.split("…") if f.strip()]:
            if frag not in ctx:
                errors.append(f"{sid}: trích dẫn “{frag[:50]}…” không nguyên văn trong câu JA")

    # --- số trên hình
    screen = re.sub(r"→\s*`#\d+`:", " ", chu)
    KANJI_NUM = {"〇": "0", "一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6",
                 "七": "7", "八": "8", "九": "9", "十": "10", "百": "100", "千": "1000"}
    flat_arabic = "".join(KANJI_NUM.get(ch, ch) for ch in flat)
    allowed = set(re.findall(r"\d+", flat)) | set(re.findall(r"\d+", flat_arabic))
    for a in list(allowed):
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    act_num = sid.split("-")[0]
    allowed.add(act_num)
    allowed.add(act_num.zfill(2))
    allowed.add("03")           # số tập

    for tok in set(re.findall(r"\d[\d,.]*", screen)):
        t = tok.replace(",", "").replace(".", "")
        if tok in allowed or t in allowed or tok in flat or t in flat:
            continue
        if re.search(r"[第幕段階弾兆候概念層]\s*" + re.escape(tok), screen) or \
           re.search(re.escape(tok) + r"\s*[幕段階弾件人話回目]", screen):
            continue
        if not ctx.strip() and any(re.search(r"\b" + re.escape(t) + r"\b", v) for v in ACT_TITLES_JA.values()):
            continue
        errors.append(f"{sid}: số “{tok}” không truy được về câu JA (ctx rỗng = {not ctx.strip()})")

    c[5] = " " + chu + " "
    c[6] = " " + beat.strip() + " "
    out_lines.append("|" + "|".join(c) + "|")

for k in ja_table:
    if k not in used:
        errors.append(f"{k}: có bản JA nhưng không có dòng VN")

print("\n".join(errors) if errors else "OK", f"· dòng JA: {len(used)}/{n_rows}")
if warnings:
    print("CANH:", "; ".join(warnings))
if errors:
    sys.exit(1)

# ---------------------------------------------------------------- ghi plan JA
plan_path = ROOT / "02_SAN_XUAT/Tap03_JA/KeHoach_Video_Tap03_JA.md"
old = plan_path.read_text(encoding="utf-8").splitlines()
cut = next(i for i, l in enumerate(old) if l.startswith("## 6. DANH SÁCH SHOT")) if any(
    l.startswith("## 6. DANH SÁCH SHOT") for l in old) else len(old)

header = """
---

## 6. DANH SÁCH SHOT — TẬP 03 (JA)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

**Bản JA:** cột *Chữ* dùng tiếng Nhật chuẩn phát thanh tài liệu (Pillow vẽ chữ với `YuGothB.ttc` / `YuGothM.ttc`); các cụm `ở "…"` trong cột *Beat* là cụm tiếng Nhật **có thật** trong câu JA của shot đó (`phrase_time()` dò trong text câu để đặt thời điểm).

**Intro:** đặt `assets/brand/intro_kenh_JA_t03.mov` ở 0,00 s (sinh bằng `py -3 .work/make_intro.py` với `AE_LANG=ja AE_EP=03` — thẻ cảnh báo tiếng Nhật). Không câu thoại nào thuộc intro.
Renderer hiện ảnh intro ở 0,00–20,50 s; shot `1-00` (20,50 s → lời đầu 23,0 s) mở dần từ đuôi đen của intro.

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
"""

body = "\n".join(out_lines[2:])          # bỏ dòng tiêu đề + dòng kẻ của bảng VN
tail = "\n**Tổng:** 110 shot — 93 shot có lời + 17 khoảng nghỉ / chuyển cảnh (bản JA giữ nguyên cột Câu, Vai, Mẫu, Nền, Nhân vật; chỉ thay cột *Chữ* và cụm `ở \"…\"` trong cột *Beat*).\n"
out = "\n".join(old[:cut]).rstrip() + "\n" + header + body + tail
plan_path.write_text(out, encoding="utf-8")
print(f"Đã ghi {plan_path} · {len(out_lines)} dòng bảng")
sys.exit(0)
