#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, glob, re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]

def inspect_all():
    print("Checking punctuation and quote styling across all 29 scripts...")
    for ep in range(1, 30):
        p = ROOT / "01_KICH_BAN" / f"Tap{ep:02d}_EN" / f"kichban_tap{ep:02d}_EN.md"
        text = open(p, encoding='utf-8').read()
        
        # Check punctuation outside closing double quotes (British style e.g. ”.)
        punct_outside = re.findall(r'“[^”\n]+”[.,]', text)
        
        # Check for unclosed quotes
        open_quotes = len(re.findall(r'“', text))
        close_quotes = len(re.findall(r'”', text))
        
        # Check for ASCII straight double quotes inside dialogue
        dialogue_lines = [l for l in text.splitlines() if not l.startswith('#') and not l.startswith('|') and not l.startswith('**[')]
        dialogue_text = "\n".join(dialogue_lines)
        ascii_quotes = len(re.findall(r'"', dialogue_text))
        
        notes = []
        if punct_outside:
            notes.append(f"{len(punct_outside)} quotes with punctuation outside (e.g. {repr(punct_outside[0])})")
        if open_quotes != close_quotes:
            notes.append(f"Unmatched curly quotes: {open_quotes} open vs {close_quotes} close")
            
        if notes:
            print(f"Tap {ep:02d}: {', '.join(notes)}")
        else:
            print(f"Tap {ep:02d}: OK")

if __name__ == '__main__':
    inspect_all()
