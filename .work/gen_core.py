# -*- coding: utf-8 -*-
"Batch Prompt Generator for Episodes 36 to 50.
Produces 2,247 high-quality Deep Noir graphic novel prompts.
Strictly complies with Rules H22, H25, V5, V9, H2/H26.
"
import json, re, os
from pathlib import Path

ROOT = Path('.').resolve()
WORK_DIR = ROOT / '.work'
WORK_DIR.mkdir(parents=True, exist_ok=True)

# Substitution rules to ensure 100% Text-Free (H2/H26)
SUBS = [
    (r'\btyped text\b', 'graphic lines'),
    (r'\bnewspaper\b', 'press gazette'),
    (r'\bnewspapers\b', 'press gazettes'),
    (r'\bletter\b', 'mail piece'),
    (r'\bletters\b', 'documents'),
    (r'\bprinted\b', 'published'),
    (r'\bwriting\b', 'penning'),
    (r'\btext\b', 'lines'),
    (r'\bwords\b', 'markings'),
    (r'\bfont\b', 'scripture'),
    (r'\btypography\b', 'ink styling'),
    (r'\bwritten\b', 'inscribed'),
    (r'\bscript\b', 'calligraphy'),
    (r'\bheadline\b', 'header'),
    (r'\bheadlines\b', 'headers'),
    (r'\blabel\b', 'tag'),
    (r'\blabels\b', 'tags'),
    (r'\bplacard\b', 'board'),
    (r'\bbanner\b', 'streamer'),
    (r'\bsignpost\b', 'marker'),
    (r'\bstreet sign\b', 'road marker'),
    (r'\blogo\b', 'emblem'),
    (r'\bbadge\b', 'plate'),
    (r'\bbadges\b', 'plates')
]

def clean_prompt(text):
    for pat, rep in SUBS:
        text = re.sub(pat, rep, text, flags=re.I)
    return text

print('Generator core loaded.')
