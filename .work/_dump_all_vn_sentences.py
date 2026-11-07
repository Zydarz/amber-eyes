# -*- coding: utf-8 -*-
"""Inspect all Vietnamese sentences in Tap 15 for linguistic naturalness and spelling."""
import sys, re
sys.path.insert(0, ".work")
import parse_kichban as PK

parsed = PK.parse_file("01_KICH_BAN/Tap15/kichban_tap15_23102026.md")

with open(".work/vn_sentences_dump_utf8.txt", "w", encoding="utf-8") as f:
    f.write(f"Elements: {len(parsed)}\n")
    for el in parsed:
        if el["kind"] == "LOI":
            role = el.get("role", "")
            act = el.get("act", "")
            f.write(f"\n--- Element {el['id']} (Hồi {act}, Vai: {role}) ---\n")
            for s in el.get("sentences", []):
                f.write(f"  [{s['id']}] {s['text']}\n")

print("Done writing .work/vn_sentences_dump_utf8.txt")
