# -*- coding: utf-8 -*-
"""Thêm chữ thẻ kết (H12) vào shot cuối của shots[_JA|_EN]_t25.json — map_shot_anh.py --shots không sinh phần này.
Cấu trúc = Tập 18 (template T2: bold = nhãn đóng hồ sơ, ital = khẩu hiệu). Sao lưu vào .work/_cu/."""
import json, shutil, sys
from pathlib import Path
W = Path(__file__).parent
TXT = {"": ("HỒ SƠ TẬP 25 · ĐÃ ĐÓNG", "AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật"),
       "_EN": ("CASE FILE 25 · CONCLUDED", "AMBER EYES · True Crime Criminal Psychology Analysis"),
       "_JA": ("事件ファイル · 終結", "AMBER EYES · 実録の事件記録から読み解く犯罪心理学")}
for suf, (a, b) in ((k, v) for k, v in TXT.items() if k in (sys.argv[1:] or TXT)):  # vd: py _patch_endcard_t25.py _EN
    p = W / f"shots{suf}_t25.json"
    shutil.copy(p, W / "_cu" / f"shots{suf}_t25_truoc_endcard_20261126.json")
    d = json.load(open(p, encoding="utf-8")); s = d["shots"][-1]
    assert not s["sentences"], "shot cuối phải là thẻ kết"
    s["template"] = "T2"; s["beat_text"] = "—"
    s["segments"] = [{"at_sentence": None, "elems": ([["bold", a], ["ital", b]] if suf != "_JA" else [["ital", a], ["bold", "第25話"], ["ital", b]])}]  # JA: nhãn đỏ + số tập, tránh ngắt "第2|5話"
    json.dump(d, open(p, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print(p.name, s["id"], a)
