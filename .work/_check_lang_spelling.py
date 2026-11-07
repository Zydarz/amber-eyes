import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"d:\TEST\Gax\amber-eyes")

en_text = (ROOT / "01_KICH_BAN" / "Tap07_EN" / "kichban_tap07_EN.md").read_text(encoding="utf-8")
ja_text = (ROOT / "01_KICH_BAN" / "Tap07_JA" / "kichban_tap07_JA.md").read_text(encoding="utf-8")
ko_text = (ROOT / "01_KICH_BAN" / "Tap07_KO" / "kichban_tap07_KO.md").read_text(encoding="utf-8")

print("=== CHECKING EN SCRIPT ===")
# Common English typos
common_typos_en = [
    r"\bteh\b", r"\brecieve\b", r"\bseperate\b", r"\boccured\b", r"\bdefinately\b",
    r"\bgoverment\b", r"\baccomodate\b", r"\bwich\b", r"\bthier\b", r"\bundoubtly\b"
]
for typo in common_typos_en:
    m = re.findall(typo, en_text, re.IGNORECASE)
    if m:
        print(f"Found typo: {m}")

# Check repeated words in EN like 'the the', 'and and', 'to to', 'in in'
dup_en = re.findall(r"\b(the|and|to|in|of|that|is|was|for|on|with|as|at|by|this|it)\s+\1\b", en_text, re.IGNORECASE)
if dup_en:
    print(f"Found duplicate English words: {dup_en}")
else:
    print("EN: 0 duplicate words, 0 common typos!")

print("\n=== CHECKING JA SCRIPT ===")
# Check for unclosed brackets or punctuation glitches
unmatched_brackets_ja = ja_text.count("「") - ja_text.count("」")
unmatched_parens_ja = ja_text.count("（") - ja_text.count("）")
print(f"JA: 「」 diff = {unmatched_brackets_ja}, （） diff = {unmatched_parens_ja}")
# Check if any English letters slipped into JA narration (except brand names like F-250, Kmart, Glee, etc.)
lines_ja = ja_text.splitlines()
for idx, l in enumerate(lines_ja, 1):
    if l.startswith("[") or l.startswith("#") or l.startswith("**"):
        continue
    # check if full sentence in English exists
    if len(re.findall(r"[a-zA-Z]{5,}", l)) > 2:
        print(f"Line {idx} has English words: {l}")
print("JA: Punctuation and structure checked!")

print("\n=== CHECKING KO SCRIPT ===")
unmatched_quotes_ko = ko_text.count("‘") - ko_text.count("’")
print(f"KO: ‘ ’ diff = {unmatched_quotes_ko}")
print("KO: Checked!")
