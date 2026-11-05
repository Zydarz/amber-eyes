#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — đo mức thay đổi kịch bản mới (v4) so với âm thanh đã thu + bảng shot.

Với mỗi ngôn ngữ (vi/en/ja):
  1. parse lại kịch bản bằng parse_kichban.py (nguồn sự thật: file .md trong 01_KICH_BAN)
  2. so câu đọc với timeline_s_*.json (âm thanh đã thu) — phủ được bao nhiêu?
  3. so với script_*.json đang dùng (element / câu / nội dung)
  4. báo câu nào TRÙNG chữ, câu nào MỚI, câu nào ĐỔI chữ

Dùng:  py -3 .work/_verify_t04_script.py
"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

LANGS = [
    ("vi", "01_KICH_BAN/Tap04/kichban_tap04_23102026.md", "script_tap04.json",
     "timeline_s_t04.json", "shots_t04.json"),
    ("en", "01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md", "script_tap04_EN.json",
     "timeline_s_EN_t04.json", "shots_EN_t04.json"),
    ("ja", "01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md", "script_tap04_JA.json",
     "timeline_s_JA_t04.json", "shots_JA_t04.json"),
]

TMP = WORK / "_tmp_t04_parse"
TMP.mkdir(exist_ok=True)


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def sents_of(el):
    out = []
    for s in el.get("sentences", []) or []:
        t = (s.get("text") or "").strip()
        if t:
            out.append((s.get("id"), t))
    return out


def flat(els):
    out = []
    for el in els:
        for sid, t in sents_of(el):
            out.append((sid, t))
    return out


def norm(s):
    return " ".join(s.replace("“", '"').replace("”", '"')
                    .replace("‘", "'").replace("’", "'").split())


bad = 0
for lang, kb, script_name, tl_name, shots_name in LANGS:
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
    fn = flat(new)
    sc_ids = [i for i, _ in fn]
    print(f"  element : mới {len(new)} · lượt lời {sum(1 for e in new if e['kind'] == 'LOI')}")
    print(f"  câu     : mới {len(fn)}")

    # ---- 1) script_*.json đang dùng
    sc_path = WORK / script_name
    if sc_path.exists():
        cur = load(sc_path)
        fc = flat(cur)
        print(f"  script_*.json đang dùng: {len(cur)} el · {len(fc)} câu")
        if len(fn) != len(fc):
            print(f"  ⚠ SỐ CÂU KHÁC: mới {len(fn)} vs đang dùng {len(fc)}")
        else:
            diff = [(a[0], a[1], b[1]) for a, b in zip(fn, fc) if a[0] != b[0] or norm(a[1]) != norm(b[1])]
            if diff:
                print(f"  ⚠ {len(diff)} câu lệch so với script_*.json:")
                for sid, a, b in diff[:6]:
                    print(f"     {sid}\n       mới : {a[:110]}\n       cũ  : {b[:110]}")
            else:
                print("  ✔ script_*.json khớp 100%")
    else:
        print(f"  (không có {script_name})")

    # ---- 2) timeline (âm thanh đã thu)
    tl = load(WORK / tl_name)
    items = tl["items"]
    tl_ids = [it["id"] for it in items]
    tl_set = set(tl_ids)
    cov = [i for i in sc_ids if i in tl_set]
    only_sc = [i for i in sc_ids if i not in tl_set]
    only_tl = [i for i in tl_ids if i not in set(sc_ids)]
    print(f"  timeline: {len(tl_ids)} câu · phủ {len(cov)}/{len(sc_ids)} câu kịch bản · total={tl.get('total')}")
    if only_sc:
        print(f"  ⚠ câu trong kịch bản KHÔNG có trong timeline (cần thu lại): {len(only_sc)}")
        print(f"     {only_sc[:12]}")
    if only_tl:
        print(f"  ⚠ câu trong timeline KHÔNG còn trong kịch bản: {len(only_tl)}")
        print(f"     {only_tl[:12]}")

    # so chữ câu nào trùng id có khác chữ không
    tl_txt = {it["id"]: (it.get("text") or "") for it in items}
    mism = []
    for sid, stext in fn:
        if sid in tl_txt and norm(stext) != norm(tl_txt[sid]):
            mism.append((sid, stext, tl_txt[sid]))
    if mism:
        print(f"  ⚠ {len(mism)} câu CÓ TRONG TIMELINE nhưng khác chữ:")
        for sid, a, b in mism[:8]:
            print(f"     {sid}\n       kb : {a[:110]}\n       tl : {b[:110]}")
    else:
        print("  ✔ mọi câu trùng id với timeline đều khớp chữ")

    # ---- 3) bảng shot: câu nào trong bảng shot không còn trong kịch bản
    sh_path = WORK / shots_name
    if sh_path.exists():
        sh = load(sh_path)
        sh_sent = []
        for s in sh["shots"]:
            sh_sent += s.get("sentences", []) or []
        sh_set = set(sh_sent)
        lost = [i for i in sh_sent if i not in set(sc_ids)]
        print(f"  bảng shot: {len(sh['shots'])} shot · {len(sh_sent)} câu · "
              f"câu trong bảng shot KHÔNG còn trong kịch bản: {len(lost)}")
        if lost:
            print(f"     {lost[:12]}")
    else:
        print(f"  (không có {shots_name})")

print("=" * 72)
print("KẾT LUẬN:", "ĐẠT" if bad == 0 else f"CÓ {bad} VẤN ĐỀ")
