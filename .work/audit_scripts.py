#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, glob, re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(r"D:\TEST\Gax\Audi")

# 1. British vs American English spelling checks
BRITISH_TO_AMERICAN = {
    r'\bbehaviour': 'behavior',
    r'\bcolour': 'color',
    r'\bfavour': 'favor',
    r'\bhonour': 'honor',
    r'\blabour': 'labor',
    r'\bneighbour': 'neighbor',
    r'\brumour': 'rumor',
    r'\bhumour': 'humor',
    r'\bdefence': 'defense',
    r'\boffence': 'offense',
    r'\bpretence': 'pretense',
    r'\bcentre': 'center',
    r'\btheatre': 'theater',
    r'\bfibre': 'fiber',
    r'\blitre': 'liter',
    r'\bmetre': 'meter',
    r'\banalyse': 'analyze',
    r'\bparalyse': 'paralyze',
    r'\bcatalyse': 'catalyze',
    r'\btravelling': 'traveling',
    r'\btravelled': 'traveled',
    r'\bcouncillor': 'councilor',
    r'\bcounsellor': 'counselor',
    r'\bjudgement\b': 'judgment',
    r'\bprogramme\b': 'program',
}

# 2. Sensitive / Gore words under Rule V9 (checking context)
V9_WATCHLIST = [
    r'\bguts\b', r'\bbloodbath\b', r'\bsevered head\b', r'\bmutilated genitals\b',
    r'\bdecapitated head\b', r'\bslit throat\b', r'\bgasoline burn\b'
]

# 3. Typography checks
# - double spaces
# - spaced hyphens instead of em-dash (e.g. " - ")

def audit_episode(ep_num):
    ep_str = f"{ep_num:02d}"
    script_path = ROOT / "01_KICH_BAN" / f"Tap{ep_str}_EN" / f"kichban_tap{ep_str}_EN.md"
    if not script_path.exists():
        return None, [f"File not found: {script_path}"]
    
    text = open(script_path, encoding='utf-8').read()
    lines = text.splitlines()
    issues = []
    
    # Check British spelling
    for pat, us_eq in BRITISH_TO_AMERICAN.items():
        matches = re.findall(pat, text, re.IGNORECASE)
        if matches:
            issues.append(f"British spelling found: '{matches[0]}' -> recommend US '{us_eq}' (count={len(matches)})")
            
    # Check V9 watchlist
    for pat in V9_WATCHLIST:
        m = re.findall(pat, text, re.IGNORECASE)
        if m:
            issues.append(f"V9 sensitive word check: '{m[0]}' (review if needed)")
            
    # Check role formatting
    valid_roles = {'HOST', 'INVESTIGATOR', 'PSYCHOLOGIST', 'ORDINARY PERSON'}
    role_pattern = re.compile(r'^\*\*([^*]+)\*\*(?:\s*\*\([^*]+\)\*)?\s*:')
    for idx, l in enumerate(lines, 1):
        m = role_pattern.match(l.strip())
        if m:
            r = m.group(1).strip()
            if r not in valid_roles:
                issues.append(f"Line {idx}: Unrecognized role '**{r}**'")
                
    # Check spaced hyphens " - " vs em-dash " — "
    spaced_hyphens = len(re.findall(r'(\w)\s+-\s+(\w)', text))
    if spaced_hyphens > 0:
        issues.append(f"Typography: {spaced_hyphens} instances of ' - ' (recommend em-dash ' — ')")
        
    # Check double spaces
    double_spaces = len(re.findall(r'[^\s]\s{2,}[^\s]', text))
    if double_spaces > 0:
        issues.append(f"Typography: {double_spaces} double spaces found")
        
    return len(lines), issues

def run_full_audit():
    print("================ FULL AUDIT OF 29 ENGLISH SCRIPTS ================\n")
    all_clean = True
    report = {}
    for ep in range(1, 30):
        n_lines, issues = audit_episode(ep)
        report[ep] = issues
        status = "✅ CLEAN" if not issues else f"⚠️ {len(issues)} NOTES"
        print(f"Tap {ep:02d} ({n_lines} lines): {status}")
        for iss in issues:
            print(f"    - {iss}")
    return report

if __name__ == '__main__':
    run_full_audit()
