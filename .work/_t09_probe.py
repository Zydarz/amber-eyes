import io, json, os, re, glob

ROOT = r"D:/TEST/Gax/amber-eyes"

SCRIPTS = {
    "VN": "01_KICH_BAN/Tap09/kichban_tap09_23102026.md",
    "EN": "01_KICH_BAN/Tap09/kichban_tap09_EN.md",
    "JA": "01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md",
}

print("=== SCRIPT MD (speaker blocks / quoted lines) ===")
for lang, p in SCRIPTS.items():
    t = io.open(os.path.join(ROOT, p), encoding="utf-8").read()
    sp = re.findall(r"\*\*([A-ZĐĂÂÔƠƯ][A-ZĐĂÂÔƠƯ \.\-]{1,30})\*\*\s*\*\(", t)
    q = re.findall(r'^\s*[""](.+?)[""]\s*$', t, re.M)
    print(lang, "speakerblocks=", len(sp), "quoted_lines=", len(q))

print()
print("=== PARSED script_tap09*.json ===")
for lang, p in [("VN", ".work/script_tap09.json"), ("EN", ".work/script_tap09_EN.json"), ("JA", ".work/script_tap09_JA.json")]:
    fp = os.path.join(ROOT, p)
    if not os.path.exists(fp):
        print(lang, "MISSING", p); continue
    d = json.load(io.open(fp, encoding="utf-8"))
    if isinstance(d, dict):
        print(lang, "dict keys:", list(d.keys())[:12])
        for k, v in d.items():
            if isinstance(v, list):
                print("   ", k, "len=", len(v))
    elif isinstance(d, list):
        print(lang, "list len=", len(d), "sample:", json.dumps(d[0], ensure_ascii=False)[:300])

print()
print("=== acting_tap09*.json ===")
for lang, p in [("VN", ".work/acting_tap09.json"), ("EN", ".work/acting_tap09_EN.json"), ("JA", ".work/acting_tap09_JA.json")]:
    fp = os.path.join(ROOT, p)
    if not os.path.exists(fp):
        print(lang, "MISSING", p); continue
    d = json.load(io.open(fp, encoding="utf-8"))
    items = d if isinstance(d, list) else d.get("items", d)
    print(lang, type(d).__name__, "len=", len(items) if hasattr(items, "__len__") else "?")

print()
print("=== timeline files mentioning t09 ===")
for p in sorted(glob.glob(os.path.join(ROOT, ".work", "timeline*"))):
    n = os.path.basename(p)
    if "09" in n or n in ("timeline_s.json", "timeline_s_EN.json", "timeline_s_JA.json"):
        try:
            d = json.load(io.open(p, encoding="utf-8"))
            tot = d.get("total") if isinstance(d, dict) else None
            print(n, "total=", tot, "mtime=", __import__("time").strftime("%Y-%m-%d %H:%M", __import__("time").localtime(os.path.getmtime(p))))
        except Exception as e:
            print(n, "ERR", e)

print()
print("=== shots files mentioning t09 ===")
for p in sorted(glob.glob(os.path.join(ROOT, ".work", "shots*"))):
    n = os.path.basename(p)
    if "09" in n or n in ("shots.json", "shots_EN.json", "shots_JA.json"):
        try:
            d = json.load(io.open(p, encoding="utf-8"))
            items = d if isinstance(d, list) else d.get("shots", [])
            print(n, "shots=", len(items))
        except Exception as e:
            print(n, "ERR", e)

print()
print("=== assets/bg t09 ===")
for p in sorted(glob.glob(os.path.join(ROOT, "assets", "bg", "t09*"))):
    print(os.path.basename(p), os.path.getsize(p))

print()
print("=== EPISODES['09'] in edition.py ===")
src = io.open(os.path.join(ROOT, ".work", "edition.py"), encoding="utf-8").read()
i = src.find('"09"')
if i < 0:
    i = src.find("'09'")
print(src[max(0, i-200): i+4000] if i >= 0 else "NOT FOUND")
