import io, json, os, re, glob, subprocess, time

ROOT = r"D:/TEST/Gax/amber-eyes"

def probe(mp):
    try:
        out = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",mp],
                             capture_output=True, text=True)
        return out.stdout.strip()
    except Exception as e:
        return "ERR "+str(e)

print("=== MASTER AUDIO for Tap09 ===")
for d in ["02_SAN_XUAT/Tap09","02_SAN_XUAT/Tap09_EN","02_SAN_XUAT/Tap09_JA"]:
    p = os.path.join(ROOT,d)
    if not os.path.isdir(p):
        print(d, "MISSING DIR"); continue
    for f in sorted(os.listdir(p)):
        if f.lower().endswith((".mp3",".wav",".m4a")):
            fp = os.path.join(p,f)
            print(f"{d}/{f}  dur={probe(fp)}  size={os.path.getsize(fp)}")

print()
print("=== any Tap09 master anywhere ===")
for pat in ["**/*ap09*master*.mp3","**/*ap09*.mp3"]:
    for p in glob.glob(os.path.join(ROOT,pat), recursive=True):
        try:
            print(os.path.relpath(p,ROOT), probe(p), os.path.getsize(p))
        except Exception as e:
            print(p, "ERR")

print()
print("=== assets/bg count per episode ===")
bgdir = os.path.join(ROOT,"assets","bg")
if os.path.isdir(bgdir):
    files = os.listdir(bgdir)
    import collections
    c = collections.Counter()
    for f in files:
        m = re.match(r"^(t\d+)", f)
        c[m.group(1) if m else "OTHER:"+f[:12]] += 1
    for k,v in sorted(c.items()):
        print(k, v)
else:
    print("assets/bg MISSING")

print()
print("=== acting_tap09 sentence ids vs script ===")
for lang,p in [("VN",".work/acting_tap09.json"),("EN",".work/acting_tap09_EN.json"),("JA",".work/acting_tap09_JA.json")]:
    d = json.load(io.open(os.path.join(ROOT,p),encoding="utf-8"))
    items = d if isinstance(d,list) else d.get("items",d)
    print(lang, "n=",len(items))
    if isinstance(items, list):
        print("   first id:", items[0].get("id"), "| last id:", items[-1].get("id"))
        print("   sample:", json.dumps(items[0], ensure_ascii=False)[:400])
