import io, json, os, re, sys
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT/".work"))
from parse_kichban import parse_file

# Nội dung từng element lời của Tập 09 (VN) — cần để gán nền khớp (H3)
els = parse_file(str(ROOT/"01_KICH_BAN/Tap09/kichban_tap09_23102026.md"))
print("=== TẬP 09: nội dung từng element lời ===")
for e in els:
    if e["kind"] != "LOI": continue
    txt = " ".join(s["text"] for s in e["sentences"])
    print(f"\n{e['id']} (act {e['act']}, role {e['role']}, {len(e['sentences'])} câu):")
    print("   ", txt[:300].replace("\n"," "))
