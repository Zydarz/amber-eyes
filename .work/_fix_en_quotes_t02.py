# -*- coding: utf-8 -*-
"""Sửa 2 dòng lớp phủ EN bị lược dấu "…" do lỗi nháy cong trong kịch bản (đã sửa 05/11).

3-20 và 4-18 từng hiện "don…t" / "I don…t" trên hình vì kịch bản dùng dấu nháy kép cong
ở chỗ dấu nháy trong từ. Sau khi sửa kịch bản, trích dẫn đã nguyên văn -> bỏ dấu lược.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
p = Path(r"D:/TEST/Gax/amber-eyes/.work/shots_text_tap02_EN.json")
d = json.loads(p.read_text(encoding="utf-8"))

d["3-20"] = ["“Yes, but I don’t know the answers, and I’m pretty sure the answers don’t matter.”", [], None]
d["4-18"] = ["*His entire world of prestige and honor shattered into dust* → `#6`: “I don’t know what to say.”", [], None]

p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("da sua 3-20, 4-18 ·", len(d), "khoa")
