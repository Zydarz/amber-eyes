# -*- coding: utf-8 -*-
"""Review orthography, vocabulary, numbers, and quotation marks across VN, EN, JA scripts."""
import re
import sys
sys.path.insert(0, '.work')
import parse_kichban

def check_vn():
    print("=== REVIEWING VIETNAMESE SCRIPT ===")
    els = parse_kichban.parse_lines(open('01_KICH_BAN/Ho_So_Toi_Pham/Tap41/kichban_tap41_19112026.md', encoding='utf-8').read().splitlines())
    digits_found = []
    quotes_found = []
    typos = []
    
    # Common VN typos or misused terms
    typo_patterns = [
        (r'\breo rắc\b', 'gieo rắc'),
        (r'\bngăn nắp\b', ''),
        (r'\bsơ suất\b', ''),
        (r'\bxuất xứ\b', ''),
        (r'\bchẩn đoán\b', ''),
    ]
    
    for e in els:
        if e['kind'] == 'LOI':
            for s in e['sentences']:
                t = s['text']
                # check digits
                d = re.findall(r'\b\d+\b', t)
                if d:
                    digits_found.append((s['id'], d, t))
                if "'" in t or '"' in t:
                    quotes_found.append((s['id'], t))
                for pat, corr in typo_patterns:
                    if re.search(pat, t, re.I):
                        typos.append((s['id'], pat, corr, t))
                        
    print(f"Digits in text: {len(digits_found)}")
    for sid, d, t in digits_found:
        print(f"  {sid}: digits {d} -> '{t}'")
        
    print(f"Typos/Orthography alerts: {len(typos)}")
    for sid, pat, corr, t in typos:
        print(f"  {sid}: found {pat} (suggest: {corr}) -> '{t}'")

def check_en():
    print("\n=== REVIEWING ENGLISH SCRIPT ===")
    els = parse_kichban.parse_lines(open('01_KICH_BAN/Ho_So_Toi_Pham/Tap41_EN/kichban_tap41_EN.md', encoding='utf-8').read().splitlines())
    digits_found = []
    for e in els:
        if e['kind'] == 'LOI':
            for s in e['sentences']:
                t = s['text']
                d = re.findall(r'\b\d+\b', t)
                if d:
                    digits_found.append((s['id'], d, t))
    print(f"Digits in EN text: {len(digits_found)}")
    for sid, d, t in digits_found:
        print(f"  {sid}: digits {d} -> '{t}'")

def check_ja():
    print("\n=== REVIEWING JAPANESE SCRIPT ===")
    els = parse_kichban.parse_lines(open('01_KICH_BAN/Ho_So_Toi_Pham/Tap41_JA/kichban_tap41_JA.md', encoding='utf-8').read().splitlines())
    digits_found = []
    for e in els:
        if e['kind'] == 'LOI':
            for s in e['sentences']:
                t = s['text']
                d = re.findall(r'\d+', t)
                if d:
                    digits_found.append((s['id'], d, t))
    print(f"Digits in JA text: {len(digits_found)}")
    for sid, d, t in digits_found:
        print(f"  {sid}: digits {d} -> '{t}'")

if __name__ == '__main__':
    check_vn()
    check_en()
    check_ja()
