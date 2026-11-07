# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban

parsed = parse_kichban.parse_file(ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_23102026.md")

with open(ROOT / ".work" / "all_sentences_vn.txt", "w", encoding="utf-8") as out:
    total_s = 0
    for el in parsed:
        if el["kind"] == "LOI":
            out.write(f"\n=== {el['id']} [{el['role']}] ({len(el['sentences'])} sentences) ===\n")
            for i, s in enumerate(el["sentences"]):
                total_s += 1
                out.write(f"[{total_s:03d}] {s['id']}: {s['text']}\n")

print(f"Dumped {total_s} sentences to .work/all_sentences_vn.txt")
