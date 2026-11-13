# -*- coding: utf-8 -*-
import subprocess, sys
sys.path.insert(0, '.work')
import parse_kichban as PK

# Read original JA script
txt = subprocess.check_output(['git', 'show', 'HEAD:01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md'], encoding='utf-8')
ja_orig = PK.parse_lines(txt.splitlines())

print("Loaded ja_orig with elements:", len(ja_orig))
