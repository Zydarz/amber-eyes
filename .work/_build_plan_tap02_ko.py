#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng bảng shot Tập 02 bản TIẾNG HÀN từ bảng VN + shots_text_tap02_KO.json.

Sao yên bảng VN ở cột Câu, Vai, Mẫu, Nền, Nhân vật, chuyển cảnh; chỉ thay:
  - cột Chữ -> tiếng Hàn (chữ hiện trên màn hình)
  - cụm `ở "…"` trong cột Beat -> cụm tiếng Hàn CÓ THẬT trong câu KO

Tự kiểm (exit code khác 0 nếu lỗi):
  1. mọi shot có chữ trong bảng VN đều có bản KO
  2. cụm beat KO phải có thật trong câu KO của shot
  3. mọi con số trên hình phải truy được về câu KO
  4. trích dẫn trong ngoặc kép phải nguyên văn trong câu KO

python .work/_build_plan_tap02_ko.py
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

ko_table = json.loads((W / "shots_text_tap02_KO.json").read_text(encoding="utf-8"))
ko_table = {k: v for k, v in ko_table.items() if not k.startswith("_")}
script = json.loads((W / "script_tap02_KO.json").read_text(encoding="utf-8"))
S = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]

vn_lines = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn_lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_lines) if i > i0 and l.startswith("**Tổng:"))

ACT_TITLES_KO = {
    1: "제1막 · 대령의 계급장 뒤에 숨겨진 극단적 대비",
    2: "제2막 · 현장 & 범죄 프로파일 – 심연의 에스컬레이션 궤적",
    3: "제3막 · 심층 심리 해부 – 심리적 구획화와 자기 합리화",
    4: "제4막 · 취조실 안의 심리전 – 10시간의 가면의 붕괴",
    5: "제5막 · 판결, 심리적 종말 & 생존의 경고",
}


def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


errors = []
out_lines = []
used = set()

for l in vn_lines[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        out_lines.append(l)
        continue
    sid = m.group(1)
    c = l.strip().strip("|").split("|")
    if sid not in ko_table:
        if c[5].strip() != "—":
            errors.append(f"{sid}: thiếu bản KO")
        out_lines.append(l)
        continue
    used.add(sid)
    chu, phrases = ko_table[sid][0], ko_table[sid][1]
    override = ko_table[sid][2] if len(ko_table[sid]) > 2 else None
    ids = sents(c[1])
    ctx = " ".join(S.get(x, "") for x in ids)
    flat = ctx.replace(" ", "")

    # --- beat: thay cụm `ở "…"` bằng cụm KO
    if override is not None:
        beat = override
    else:
        vn_ph = re.findall(r'ở "([^"]+)"', c[6])
        if len(vn_ph) != len(phrases):
            errors.append(f"{sid}: {len(vn_ph)} cụm beat VN ≠ {len(phrases)} cụm KO ({vn_ph} vs {phrases})")
            beat = c[6]
        else:
            it = iter(phrases)
            beat = re.sub(r'ở "([^"]+)"', lambda _: 'ở "' + next(it) + '"', c[6])

    # --- cụm beat KO phải có thật trong câu KO
    if ctx.strip():
        for p in re.findall(r'ở "([^"]+)"', beat):
            if p not in ctx:
                errors.append(f"{sid}: cụm beat \"{p}\" không có trong câu KO: \"{ctx[:50]}...\"")

    # --- trích dẫn nguyên văn
    for q in re.findall(r"“([^”]+)”", chu):
        for frag in [f.strip() for f in q.split("…") if f.strip()]:
            if frag not in ctx:
                errors.append(f"{sid}: trích dẫn “{frag[:45]}…” không nguyên văn trong câu KO")

    # --- số trên hình
    screen = re.sub(r"→\s*`#\d+`:", " ", chu)
    allowed = set(re.findall(r"\d+", flat))
    for a in list(allowed):
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    act_num = sid.split("-")[0]
    allowed.add(act_num)
    allowed.add(act_num.zfill(2))
    allowed.add("02")  # số tập

    for tok in set(re.findall(r"\d[\d,.]*", screen)):
        t = tok.replace(",", "").replace(".", "")
        if tok in allowed or t in allowed or tok in flat or t in flat:
            continue
        if re.search(r"(제|막|단계|화|편)\s*" + re.escape(tok), screen) or re.search(re.escape(tok) + r"\s*(막|단계|편|화)", screen):
            continue
        if not ctx.strip() and any(re.search(r"\b" + re.escape(t) + r"\b", v) for v in ACT_TITLES_KO.values()):
            continue
        errors.append(f"{sid}: số “{tok}” không truy được về câu KO (allowed: {sorted(allowed)})")

    c[5] = " " + chu + " "
    c[6] = " " + beat.strip() + " "
    out_lines.append("|" + "|".join(c) + "|")

for k in ko_table:
    if k not in used:
        errors.append(f"{k}: có bản KO nhưng không có dòng VN")

print("\n".join(errors) if errors else "OK", f"· dòng KO: {len(used)}")
if errors:
    sys.exit(1)

# ---------------------------------------------------------------- ghi hồ sơ KO
plan_path = ROOT / "02_SAN_XUAT" / "Tap02_KO" / "KeHoach_Video_Tap02_KO.md"
plan_path.parent.mkdir(parents=True, exist_ok=True)

header = """# HỒ SƠ SẢN XUẤT TẬP 02 · BẢN TIẾNG HÀN · 「두 얼굴의 대령」 (PHẦN B)

> **TRẠNG THÁI: BẢN DỰNG ẢNH TĨNH — CHỜ TTS LẠI**

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản:** `01_KICH_BAN/Tap02_KO/kichban_tap02_KO.md` · **Chữ cố định:** `00_TIEU_CHUAN/CHU_CO_DINH_KO.md` · **Thành phẩm:** `02_SAN_XUAT/Tap02_KO/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md`. Bảng shot giữ nguyên các cột Câu, Vai, Mẫu, Nền, Nhân vật và mô tả beat; chỉ thay:
- cột **Chữ** sang tiếng Hàn chuẩn phát thanh tài liệu (Pillow vẽ chữ với `malgunbd.ttf` / `malgun.ttf`);
- các cụm `ở "…"` trong cột **Beat** sang cụm tiếng Hàn **có thật** trong câu KO tương ứng.

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap02_KO/kichban_tap02_KO.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_KO.md`, 203 câu, 36 lượt nói, Director's Cut) |
| Lượt nói / câu | 36 / **203**. Mã câu trùng 100% bản VN (`script_tap02_KO.json`) |
| N1 / N2 | `1.07` 트렌턴 기지 관계자 (양) / `4.06` 트위드 주민 (고양이) |
| Bảng shot | 161 dòng = 144 shot có lời + 17 dòng không lời |
| Nền dùng | `assets/bg/` (dùng lại 100% của bản VN/EN/JA) |
| Giọng | **CHƯA CÓ** — cần đọc lại TTS sau khi duyệt bảng shot này |

## B3. Ánh sáng riêng (trong `parse_shots.py`)

Giống hệt bản VN (`COMBO`, `BG2`, `INSET`), vì số hiệu shot và nền không đổi.

<!--TABLE-->
"""

tail = ("\n> ⚠ **Timeline tạm (05/11/2026):** `.work/timeline_s_KO_t02.json` dựng lại theo kịch bản KO mới "
        "(203 câu, 1.953,97 s) — dùng khung nhịp của timeline VN (đo thật) và tốc độ đọc ước tính theo tiếng Nhật "
        "(hệ âm tiết CJK). **Chưa có audio master KO** ⇒ sau khi đọc lại TTS phải dựng lại timeline bằng Whisper rồi dựng lại ảnh.\n")
body = "\n".join(out_lines)
plan_path.write_text(header + body + tail, encoding="utf-8")
print(f"Đã ghi {plan_path}")
sys.exit(0)
