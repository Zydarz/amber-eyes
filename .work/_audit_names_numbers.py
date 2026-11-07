# -*- coding: utf-8 -*-
"""
Audit all proper names, numbers, dates and vocabulary across all 199 sentences in Episode 09.
"""
import sys, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban as PK

p_vn = PK.parse_file(str(ROOT / "01_KICH_BAN/Tap09/kichban_tap09_23102026.md"))
loi_vn = [e for e in p_vn if e["kind"] == "LOI"]

print(f"Loaded {len(loi_vn)} turns.")

# Check all foreign names in VN script
names_to_check = [
    "Charles Manson", "Manson", "Sharon Tate", "Tate", "Roman Polanski", "Polanski",
    "Terry Melcher", "Melcher", "Vincent Bugliosi", "Bugliosi", "Susan Atkins", "Atkins",
    "Patricia Krenwinkel", "Krenwinkel", "Leslie Van Houten", "Van Houten", "Tex Watson", "Watson",
    "Linda Kasabian", "Kasabian", "Bernard Crowe", "Crowe", "Gary Hinman", "Hinman",
    "Jay Sebring", "Sebring", "Abigail Folger", "Folger", "Wojciech Frykowski", "Frykowski",
    "Steven Parent", "Parent", "Leno LaBianca", "Rosemary LaBianca", "LaBianca",
    "Spahn Ranch", "Barker Ranch", "Cielo Drive", "Waverly Drive",
    "Santa Susana", "Death Valley", "Corcoran", "Charles Older", "Kurt Lewin", "Edgar Schein",
    "Gresham Sykes", "David Matza", "Sykes", "Matza", "Gavin de Becker"
]

all_text = " ".join(s["text"] for e in loi_vn for s in e["sentences"])

print("\n--- Proper Names Occurrences in VN ---")
for n in names_to_check:
    cnt = len(re.findall(r'\b' + re.escape(n) + r'\b', all_text, re.IGNORECASE))
    print(f"{n:<25}: {cnt}")

# Check for numbers in words vs digits
print("\n--- Numbers in digits in VN ---")
digits_found = re.findall(r'\b\d+\b', all_text)
print("Digits found in text:", set(digits_found))

# Print sentences containing digits to check Rule K7 (Numbers written in words where possible)
print("\n--- Sentences with digits ---")
for e in loi_vn:
    for s in e["sentences"]:
        if re.search(r'\b\d+\b', s["text"]):
            print(f"[{s['id']}]: {s['text']}")
