import io, json, os, re, sys, hashlib
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban as PK

PAIRS = [
    ("VN", "01_KICH_BAN/Tap09/kichban_tap09_23102026.md", ".work/script_tap09.json"),
    ("EN", "01_KICH_BAN/Tap09/kichban_tap09_EN.md", ".work/script_tap09_EN.json"),
    ("JA", "01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md", ".work/script_tap09_JA.json"),
]

for lang, md, js in PAIRS:
    mdp = ROOT / md
    src = mdp.read_text(encoding="utf-8").splitlines()
    els = PK.parse_lines(src)
    loi = [e for e in els if e["kind"] == "LOI"]
    n_sent = sum(len(e["sentences"]) for e in loi)
    stored = json.loads((ROOT / js).read_text(encoding="utf-8"))
    s_loi = [e for e in stored if e["kind"] == "LOI"]
    s_sent = sum(len(e.get("sentences", [])) for e in s_loi)
    print(f"{lang}: MD->elements={len(els)} LOI_elements={len(loi)} sentences={n_sent} | stored elements={len(stored)} LOI={len(s_loi)} sentences={s_sent} | SAME={n_sent==s_sent and len(els)==len(stored)}")

print()
print("=== EN copies identical? ===")
a = (ROOT/"01_KICH_BAN/Tap09/kichban_tap09_EN.md").read_bytes()
b = (ROOT/"01_KICH_BAN/Tap09_EN/kichban_tap09_EN.md").read_bytes()
print("  Tap09/kichban_tap09_EN.md  md5:", hashlib.md5(a).hexdigest())
print("  Tap09_EN/kichban_tap09_EN.md md5:", hashlib.md5(b).hexdigest())
print("  identical:", a == b)

print()
print("=== KO script present? ===")
kp = ROOT/"01_KICH_BAN/Tap09_KO/kichban_tap09_KO.md"
print("  exists:", kp.exists(), kp.stat().st_size if kp.exists() else "")

print()
print("=== element breakdown VN ===")
els = PK.parse_lines((ROOT/PAIRS[0][1]).read_text(encoding="utf-8").splitlines())
from collections import Counter
print(" ", Counter(e["kind"] for e in els))
print("  LOI per act:", {a: sum(len(e['sentences']) for e in els if e['kind']=='LOI' and e['act']==a) for a in range(1,6)})
