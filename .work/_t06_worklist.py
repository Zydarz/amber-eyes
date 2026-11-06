#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — sinh worklist dịch lớp phủ chữ trên hình cho EN / JA.

Mỗi shot: chỉ số, element, khoảng câu, nền, mẫu, chữ tiếng Việt (tham chiếu),
và TOÀN BỘ câu của shot trong ngôn ngữ đích (để trích dẫn phải nguyên văn).
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

VN_PLAN = json.loads((W / "_t06_plan_vi.json").read_text(encoding="utf-8"))
KB = {"en": ROOT / "01_KICH_BAN/Tap06_EN/kichban_tap06_EN.md",
      "ja": ROOT / "01_KICH_BAN/Tap06_JA/kichban_tap06_JA.md"}


def sent_list(cell):
    out = []
    for part in str(cell).split(","):
        m = re.match(r"^#(\d+)(?:-#(\d+))?$", part.strip())
        if m:
            a = int(m.group(1))
            out += list(range(a, int(m.group(2) or a) + 1))
    return out


import re  # noqa: E402

for lang in ("en", "ja"):
    els = parse_file(str(KB[lang]))
    script = {}
    for e in els:
        if e.get("kind") == "LOI":
            script[e["id"]] = {s["id"]: s["text"] for s in e.get("sentences", [])}

    lines = [f"# WORKLIST Tap 06 — lớp phủ chữ trên hình ({lang.upper()})", "",
             "QUY TẮC BẮT BUỘC:", ]
    if lang == "en":
        lines += [
            "1. Mỗi shot dùng đúng 2 phần: **TIÊU ĐỀ IN HOA** · *ghi chú nghiêng nhỏ* (dùng dấu `·` làm dấu phân cách).",
            "2. Mỗi phần phải lấy từ CÂU ĐƯỢC ĐỌC của chính shot đó (dòng SENTENCES bên dưới) — KHÔNG bịa thêm dữ kiện.",
            "3. Số trên hình: nếu câu đọc viết số bằng CHỮ (vd 'thirty-three') thì hình cũng viết bằng CHỮ.",
            "   Nếu câu đọc viết số bằng SỐ (vd 'December 11, 1978') thì hình được dùng số.",
            "4. Trích dẫn trong ngoặc kép kép `“...”` phải NGUYÊN VĂN trong câu của shot (không thêm bớt từ).",
            "5. CẤM các từ: blood, corpse, strangle, choke, struggle, raped, rape, underwear,",
            "   sexual intercourse, orgasm, penis, vagina, suffocat, mutilat, dismember, torture.",
            "6. Số ở nhãn cấu trúc được phép: ACT 01, CASE FILE 06, STAGE 2.",
            "7. Nhãn hồi mở đầu: `ACT 01 · ...` ; thẻ kết: `CASE FILE 06 · CLOSED` + `AMBER EYES`.",
            "8. Giữ đúng số phần (2 phần) và độ dài tương đương bản VN để chữ vừa khung.",
        ]
    else:
        lines += [
            "1. 各ショットは 2 要素: **大見出し** · *斜体の補足*（区切りは `·`）。",
            "2. 各要素は必ず同じショットの SENTENCES（読み上げ文）からのみ取り出す。事実を創作しない。",
            "3. 画面上の数字は、読み上げ文が数字で表記（`33件` `1978年` `46歳`）なら数字で書く。",
            "   読み上げ文がひらがな/漢字（例 `三十三`）なら画面も文字で書く。",
            "4. 二重引用符 `“...”` の中身は、そのショットの文に一字一句あること。",
            "5. 禁止語: 血 / 死体 / 絞 / レイプ / 性交渉 / 精通 など描写の直接表現。",
            "6. 構造ラベル内の数字は許可: `第01幕` / `第06話`。",
            "7. 冒頭のラベル: `第01幕 · ...` ; 最終カード: `事件ファイル 第06話 · 終結` + `AMBER EYES`。",
            "8. 要素数（2つ）と長さは VN 版と同程度に保つ。",
        ]
    lines += ["", "=" * 90, ""]

    for i, sh in enumerate(VN_PLAN["shots"]):
        el = sh["el"]
        lines.append(f"### [{i}] el={el} kind={sh.get('kind') or 'shot'} sent={sh.get('sent') or '-'} "
                     f"bg={sh['bg']} tpl={sh.get('tpl') or '-'} nv={sh.get('nv') or '-'}")
        lines.append(f"VN_CHU: {sh.get('chu', '-')}")
        if sh.get("kind") in (None, "shot"):
            ks = sent_list(sh["sent"])
            for k in ks:
                lines.append(f"  {el}#{k}: {script[el].get(f'{el}#{k}', '')}")
        lines.append("")

    out = W / f"_t06_worklist_{lang}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"-> {out.name}: {len(VN_PLAN['shots'])} shot")
