import io, os, re, json
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
s = (ROOT/".work/edition.py").read_text(encoding="utf-8")
i = s.find('"09": {')
j = s.find('"10": {')
blk = s[i:j]
print("block len", len(blk))
for k in ("text_scrim","intro_card_pos","intro_card_panel","intro_card_hold","summary","roles_line","hashtags","thumb","bg2","combo","inset"):
    print(f"  {k}: {k in blk}")
print()
print("--- tail of 09 block ---")
print(blk[-1200:])
