#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng bảng shot Tập 02 bản tiếng Nhật từ bảng VN + shots_text_tap02_JA.json.

Tự kiểm tra (trả về exit code khác 0 nếu lỗi):
  1. mọi shot trong bảng VN đều có bản JA
  2. cụm beat JA phải có thật trong câu JA của shot
  3. mọi con số trên hình phải truy được về câu JA (hoặc tên hồi)
  4. trích dẫn trong ngoặc kép phải nguyên văn trong câu JA
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

ja_table = json.loads((W / "shots_text_tap02_JA.json").read_text(encoding="utf-8"))
ja_table = {k: v for k, v in ja_table.items() if not k.startswith("_")}
script = json.loads((W / "script_tap02_JA.json").read_text(encoding="utf-8"))
S = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]

vn_lines = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn_lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_lines) if i > i0 and l.startswith("**Tổng:"))

ACT_TITLES_JA = {
    1: "第1幕 · 大佐の階級章の裏にある極端なコントラスト",
    2: "第2幕 · 現場と証拠ファイル――深淵への4段階",
    3: "第3幕 · 心理解剖――二重生活の捕食者の内面",
    4: "第4幕 · 取調室――軍人の頭脳を打ち砕く",
    5: "第5幕 · 判決、危険信号、そして結びの考察",
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

for l in vn_lines[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        out_lines.append(l)
        continue
    sid = m.group(1)
    c = l.strip().strip("|").split("|")
    if sid not in ja_table:
        if c[5].strip() != "—":
            errors.append(f"{sid}: thiếu bản JA")
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

    # --- kiểm cụm beat JA có thật trong câu JA
    if ctx.strip():
        for p in re.findall(r'ở "([^"]+)"', beat):
            if p not in ctx:
                errors.append(f"{sid}: cụm beat \"{p}\" không có trong câu JA: \"{ctx[:40]}...\"")

    # --- kiểm trích dẫn nguyên văn
    for q in re.findall(r"“([^”]+)”", chu):
        for frag in [f.strip() for f in q.split("…") if f.strip()]:
            if frag not in ctx:
                errors.append(f"{sid}: trích dẫn “{frag[:45]}…” không nguyên văn trong câu JA")

    # --- kiểm số trên hình
    screen = re.sub(r"→\s*`#\d+`:", " ", chu)
    allowed = set(re.findall(r"\d+", flat))
    for a in list(allowed):
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    act_num = sid.split("-")[0]
    allowed.add(act_num)
    allowed.add(act_num.zfill(2))
    allowed.add("02")  # episode number

    for tok in set(re.findall(r"\d[\d,.]*", screen)):
        t = tok.replace(",", "").replace(".", "")
        if tok in allowed or t in allowed or tok in flat or t in flat:
            continue
        # allow standard structural labels
        if re.search(r"[第幕段階弾]\s*" + re.escape(tok), screen) or re.search(re.escape(tok) + r"\s*[幕段階弾件人話]", screen):
            continue
        if not ctx.strip() and any(re.search(r"\b" + re.escape(t) + r"\b", v) for v in ACT_TITLES_JA.values()):
            continue
        errors.append(f"{sid}: số “{tok}” không truy được về câu JA (allowed: {allowed})")

    c[5] = " " + chu + " "
    c[6] = " " + beat.strip() + " "
    out_lines.append("|" + "|".join(c) + "|")

for k in ja_table:
    if k not in used:
        errors.append(f"{k}: có bản JA nhưng không có dòng VN")

print("\n".join(errors) if errors else "OK", f"· dòng JA: {len(used)}")
if warnings:
    print("CANH:", "; ".join(warnings))
if errors:
    sys.exit(1)

# Ghi file kế hoạch JA
plan_path = ROOT / "02_SAN_XUAT" / "Tap02_JA" / "KeHoach_Video_Tap02_JA.md"

# Build header from Tap01_JA style
header = """# HỒ SƠ SẢN XUẤT TẬP 02 · BẢN TIẾNG NHẬT · 「二重生活の大佐」 (PHẦN B)

> **TRẠNG THÁI: HOÀN THÀNH DỰNG VIDEO**

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản:** `01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md` · **Chữ cố định:** `00_TIEU_CHUAN/CHU_CO_DINH_JA.md` · **Thành phẩm:** `02_SAN_XUAT/Tap02_JA/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md`. Bảng shot giữ nguyên các cột Câu, Vai, Mẫu, Nền, Nhân vật và mô tả beat; chỉ thay:
- cột **Chữ** sang tiếng Nhật chuẩn phát thanh tài liệu (Pillow vẽ chữ với `YuGothB.ttc` / `YuGothM.ttc`);
- các cụm `ở "…"` trong cột **Beat** sang cụm tiếng Nhật **có thật** trong câu JA tương ứng.

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`, 203 câu, 36 lượt nói, Director's Cut) |
| Lượt nói / câu | 36 / **203**. Host 50% · Chuyên gia 25% · Điều tra viên 20% · Người bình thường 5%. Mã câu trùng 100% bản VN (`script_tap02_JA.json`) |
| N1 / N2 | `1.07` トレントン基地関係者 (Cừu) / `4.06` ツイード住民 (Mèo) |
| Bảng shot | 151 dòng = 135 shot có lời + 16 dòng không lời |
| Nền dùng | `assets/bg/` (dùng lại 100% của bản VN/EN) |
| Giọng | H `Japanese_GentleButler` 0.95 · D `Japanese_SeriousCommander` 0.97 · C `Japanese_DependableWoman` 0.95 · N1 `Japanese_KindLady` 0.95 · N2 `Japanese_DecisivePrincess` 0.95 |

## B3. Ánh xạ riêng (trong `parse_shots.py`)

Giống hệt bản VN (`COMBO`, `BG2`, `INSET`), vì số hiệu shot và nền không đổi.

<!--TABLE-->
"""

tail = "\n**Tổng:** 151 shot phủ 100% kịch bản.\n"
body = "\n".join(out_lines)
out = header + body + tail
plan_path.write_text(out, encoding="utf-8")
print(f"Đã ghi {plan_path}")
sys.exit(0)
