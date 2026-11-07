# -*- coding: utf-8 -*-
"""Comprehensive spellcheck and grammar audit for EN, JA, KO scripts."""

import sys, re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban

# 1. EN Audit
en_parsed = parse_kichban.parse_file(ROOT / "01_KICH_BAN" / "Tap20_EN" / "kichban_tap20_EN.md")
en_sentences = []
for el in en_parsed:
    if el["kind"] == "LOI":
        for s in el["sentences"]:
            en_sentences.append((s["id"], s["text"]))

print(f"EN: Parsed {len(en_sentences)} sentences.")

# Common English typos & checks
en_typos = []
for sid, txt in en_sentences:
    # Check repeated words
    rep = re.findall(r'\b([a-zA-Z]{2,})\s+\1\b', txt, re.IGNORECASE)
    if rep:
        en_typos.append((sid, f"Repeated word: {rep}", txt))
    # Check space before punctuation
    if re.search(r'\s+[,.;:!?]', txt):
        en_typos.append((sid, "Space before punctuation", txt))
    # Check double punctuation
    if re.search(r'[,;!?]{2,}', txt) or re.search(r'\.{2,}', txt):
        en_typos.append((sid, "Double punctuation", txt))
    # Check lower case start of sentence
    if txt and txt[0].islower():
        en_typos.append((sid, "Starts with lowercase", txt))
    # Check unclosed quotes
    if txt.count('"') % 2 != 0 or txt.count('“') != txt.count('”'):
        en_typos.append((sid, "Unbalanced quotes", txt))

print(f"EN Typo check results: {len(en_typos)} issues found.")
for t in en_typos:
    print(" ", t)

# 2. JA Audit
ja_parsed = parse_kichban.parse_file(ROOT / "01_KICH_BAN" / "Tap20_JA" / "kichban_tap20_JA.md")
ja_sentences = []
for el in ja_parsed:
    if el["kind"] == "LOI":
        for s in el["sentences"]:
            ja_sentences.append((s["id"], s["text"]))

print(f"\nJA: Parsed {len(ja_sentences)} sentences.")

ja_typos = []
for sid, txt in ja_sentences:
    # Check for internal full stop 。 (should only be at the end)
    if txt[:-1].count("。") > 0:
        ja_typos.append((sid, "Internal 。 detected", txt))
    # Check for half-width characters
    if re.search(r'[\uff61-\uff9f]', txt):
        ja_typos.append((sid, "Half-width katakana", txt))
    # Check for unmatched brackets 「 」 or （ ）
    if txt.count("「") != txt.count("」"):
        ja_typos.append((sid, "Unmatched 「」", txt))
    if txt.count("（") != txt.count("）"):
        ja_typos.append((sid, "Unmatched （）", txt))

print(f"JA Typo check results: {len(ja_typos)} issues found.")
for t in ja_typos:
    print(" ", t)

# 3. KO Audit
ko_parsed = parse_kichban.parse_file(ROOT / "01_KICH_BAN" / "Tap20_KO" / "kichban_tap20_KO.md")
ko_sentences = []
for el in ko_parsed:
    if el["kind"] == "LOI":
        for s in el["sentences"]:
            ko_sentences.append((s["id"], s["text"]))

print(f"\nKO: Parsed {len(ko_sentences)} sentences.")

ko_typos = []
for sid, txt in ko_sentences:
    # Check repeated words
    rep = re.findall(r'\b([가-힣]{2,})\s+\1\b', txt)
    if rep:
        ko_typos.append((sid, f"Repeated word: {rep}", txt))
    # Check space before punctuation
    if re.search(r'\s+[,.;:!?]', txt):
        ko_typos.append((sid, "Space before punctuation", txt))
    # Check unmatched parens
    if txt.count("(") != txt.count(")"):
        ko_typos.append((sid, "Unmatched ()", txt))

print(f"KO Typo check results: {len(ko_typos)} issues found.")
for t in ko_typos:
    print(" ", t)
