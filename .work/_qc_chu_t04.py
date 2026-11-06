#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — QC cột "Chữ" (H6/V3) cho một ngôn ngữ.

Kiểm mỗi shot:
  * `#N` phải nằm trong khoảng câu của shot (N = số thứ tự câu trong ELEMENT)
  * mỗi mảnh chữ (bold/italic/quote) phải là chuỗi từ LIÊN TÚC có trong câu đang đọc
    (với khối sau `→ #N`, chỉ được dùng từ câu #N trở đi)
  * mọi con số trên hình phải có trong câu
  * câu trích dẫn phải nguyên văn (đã bao gồm ở kiểm trên)

Dùng:  py -3 .work/_qc_chu_t04.py [vi|en|ja]
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

W = ROOT / ".work"
LANG = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
KB = {"vi": "01_KICH_BAN/Tap04/kichban_tap04_23102026.md",
      "en": "01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md",
      "ja": "01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md"}[LANG]

idx = {}
for el in parse_file(str(ROOT / KB)):
    if el["kind"] == "LOI":
        idx[el["id"]] = [(s["id"], s["text"]) for s in el.get("sentences", [])]

sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
CHU = json.loads((W / f"_t04_chu_{LANG}.json").read_text(encoding="utf-8"))


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return " ".join(s.split())


def contains(frag, ctx):
    f, c = norm(frag), norm(ctx)
    if not f:
        return True
    fw, cw = f.split(), c.split()
    for i in range(len(cw) - len(fw) + 1):
        if cw[i:i + len(fw)] == fw:
            return True
    return False


errs = []
for r in sk["rows"]:
    if r["kind"] != "shot":
        continue
    sid = r["sid"]
    chu = CHU.get(sid)
    if chu is None:
        errs.append((sid, "THIẾU CHỮ"))
        continue
    eid, a, b = r["spans"][0]
    sents = idx[eid]
    # tách khối
    parts = re.split(r"\s+→\s+", chu)
    cur_from = a
    for part in parts:
        m = re.match(r"(?:ở\s+)?`#(\d+)`:?\s*(.*)", part, re.S)
        if m:
            n = int(m.group(1))
            if not (a <= n <= b):
                errs.append((sid, f"`#{n}` nằm ngoài khoảng câu {a}-{b} của {eid}"))
            cur_from = max(cur_from, n)
            part = m.group(2)
        ctx = " ".join(t for _, t in sents[cur_from - 1:b])
        for frag in re.findall(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", part):
            txt = frag[0] or frag[1] or frag[2]
            if not contains(txt, ctx):
                errs.append((sid, f"mảnh không có trong câu (từ #{cur_from}): «{txt}»"))
        # Số trên hình phải có trong câu. Bản Nhật không có khoảng trắng
        # ("43歳" là MỘT token) nên so theo RUN (bỏ khoảng trắng) — đúng quy tắc
        # của cổng dự án _qc_tap02_shots.py. Trước đây dùng contains() theo
        # token ⇒ mọi số JA đều FAIL ⇒ buộc phải bỏ số khỏi ảnh JA.
        flat_ctx = ctx.replace(" ", "")
        allowed_nums = set(re.findall(r"\d+", flat_ctx))
        allowed_nums |= {a.zfill(2) for a in list(allowed_nums)}
        for num in re.findall(r"\d[\d.,]*", part):
            tok = num.replace(".", "")
            if not tok.strip(","):
                continue
            if num in flat_ctx or tok in allowed_nums:
                continue
            errs.append((sid, f"số không có trong câu: «{num}»"))

print(f"[{LANG}] shot kiểm: {sum(1 for r in sk['rows'] if r['kind'] == 'shot')} · lỗi: {len(errs)}")
for sid, msg in errs:
    print(f"  ✗ {sid}: {msg}")
print("KẾT QUẢ:", "PASS" if not errs else "FAIL")
