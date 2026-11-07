import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p14 = PK.parse_file('01_KICH_BAN/Tap14/kichban_tap14_23102026.md')
p17 = PK.parse_file('01_KICH_BAN/Tap17/kichban_tap17_23102026.md')

print("ID   | Kind | Role | T14 | T17 | Title/Start")
for e14, e17 in zip(p14, p17):
    s14 = len(e14.get('sentences', []))
    s17 = len(e17.get('sentences', []))
    print(f"{e14['id']:4s} | {e14['kind']:4s} | {e14.get('role',''):1s}    | {s14:3d} | {s17:3d}")

print(f"Total T14: elements={len(p14)}, sents={sum(len(e.get('sentences',[])) for e in p14)}")
print(f"Total T17: elements={len(p17)}, sents={sum(len(e.get('sentences',[])) for e in p17)}")
