#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — kiểm chứng kịch bản mới (v4) khớp lời đọc đã thu.

Với mỗi ngôn ngữ (vi/en/ja):
  1. parse lại kịch bản bằng parse_kichban.py (nguồn sự thật: file .md trong 01_KICH_BAN)
  2. so với script_*.json đang dùng (element / câu / nội dung)
  3. so câu đọc với timeline_s_*.json (âm thanh đã thu) — phải phủ 100%

Dùng:  py -3 .work/_verify_t03_script.py
"""
import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

LANGS = [
    ("vi", "01_KICH_BAN/Tap03/kichban_tap03_22102026.md", "script_tap03.json", "timeline_s_t03.json"),
    ("en", "01_KICH_BAN/Tap03_EN/kichban_tap03_EN.md", "script_tap03_EN.json", "timeline_s_EN_t03.json"),
    ("ja", "01_KICH_BAN/Tap03_JA/kichban_tap03_JA.md", "script_tap03_JA.json", "timeline_s_JA_t03.json"),
]

TMP = WORK / "_tmp_t03_parse"
TMP.mkdir(exist_ok=True)


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def sents_of(el):
    """Danh sách câu đọc của 1 element (bỏ qua kind != speech)."""
    out = []
    for s in el.get("sentences", []) or []:
        t = (s.get("text") or "").strip()
        if t:
            out.append(t)
    return out


def flat(els):
    """(id, câu) theo thứ tự đọc."""
    out = []
    for el in els:
        for i, t in enumerate(sents_of(el), 1):
            out.append((f"{el['id']}#{i}", t))
    return out


bad = 0
for lang, kb, script_name, tl_name in LANGS:
    print("=" * 72)
    print(f"[{lang}] {kb}")
    kb_path = ROOT / kb
    out = TMP / f"parse_{lang}.json"
    r = subprocess.run([sys.executable, str(WORK / "parse_kichban.py"), str(kb_path), str(out)],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print("  PARSE LỖI:", (r.stdout or "")[-800:], (r.stderr or "")[-800:])
        bad += 1
        continue

    new = load(out)
    cur = load(WORK / script_name)
    fn, fc = flat(new), flat(cur)

    print(f"  element : mới {len(new)} · đang dùng {len(cur)}")
    print(f"  câu     : mới {len(fn)} · đang dùng {len(fc)}")

    # 1) so câu đọc
    diff = []
    if len(fn) != len(fc):
        diff.append(f"SAI SỐ CÂU ({len(fn)} vs {len(fc)})")
    for i in range(min(len(fn), len(fc))):
        if fn[i][0] != fc[i][0]:
            diff.append(f"id lệch @{i}: {fn[i][0]} vs {fc[i][0]}")
            break
        if fn[i][1] != fc[i][1]:
            diff.append(f"chữ lệch @{fn[i][0]}:\n      mới : {fn[i][1][:120]}\n      cũ  : {fc[i][1][:120]}")
    if diff:
        bad += 1
        print("  ⚠ SAI LỆCH LỜI ĐỌC:")
        for d in diff[:12]:
            print("     -", d)
    else:
        print("  ✔ lời đọc khớp 100% với bản đang dùng")

    # 2) so với timeline (âm thanh đã thu)
    tl = load(WORK / tl_name)
    items = tl["items"]
    tl_ids = [it["id"] for it in items]
    tl_txt = {it["id"]: (it.get("text") or "").strip() for it in items}
    sc_ids = [i for i, _ in fn]

    only_script = [i for i in sc_ids if i not in tl_ids]
    only_tl = [i for i in tl_ids if i not in sc_ids]
    print(f"  timeline: {len(tl_ids)} câu · phủ {len(set(sc_ids) & set(tl_ids))}/{len(set(tl_ids))}")
    if only_script:
        print(f"  ⚠ câu trong kịch bản KHÔNG có trong timeline: {only_script[:8]} ({len(only_script)})")
        bad += 1
    if only_tl:
        print(f"  ⚠ câu trong timeline KHÔNG có trong kịch bản: {only_tl[:8]} ({len(only_tl)})")
        bad += 1

    # 3) so chữ từng câu kịch bản vs timeline (bỏ dấu nháy/khoảng trắng)
    def norm(s):
        return " ".join(s.replace("“", '"').replace("”", '"')
                        .replace("‘", "'").replace("’", "'").split())

    mism = []
    for i in sc_ids:
        if i in tl_txt:
            a, b = norm(tl_txt[i]), norm(dict(fn)[i] if isinstance(fn, dict) else "")
    # so từng cặp theo thứ tự
    for (sid, stext), it in zip(fn, items):
        if sid != it["id"]:
            break
        if norm(stext) != norm((it.get("text") or "")):
            mism.append((sid, stext, (it.get("text") or "")))
    if mism:
        print(f"  ⚠ {len(mism)} câu lệch chữ so với timeline:")
        for sid, a, b in mism[:6]:
            print(f"     {sid}\n       kb : {a[:110]}\n       tl : {b[:110]}")
    else:
        print("  ✔ mọi câu khớp chữ với timeline (đã chuẩn hoá dấu nháy)")

print("=" * 72)
print("KẾT LUẬN:", "ĐẠT — kịch bản khớp lời đọc đã thu" if bad == 0 else f"CÓ {bad} VẤN ĐỀ")
sys.exit(0 if bad == 0 else 1)
