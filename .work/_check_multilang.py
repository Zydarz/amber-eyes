import json, sys
sys.path.insert(0, '.work')
from parse_kichban import parse_file

en = parse_file('01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md')
ja = parse_file('01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md')
ko = parse_file('01_KICH_BAN/Tap05_KO/kichban_tap05_KO.md')
print(f"EN: {len(en)} elements | JA: {len(ja)} elements | KO: {len(ko)} elements")
