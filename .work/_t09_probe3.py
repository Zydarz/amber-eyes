import io, json, os, re, glob, subprocess, time

ROOT = r"D:/TEST/Gax/amber-eyes"

def probe(mp):
    try:
        out = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",mp],
                             capture_output=True, text=True)
        return out.stdout.strip()
    except Exception as e:
        return "ERR "+str(e)

print("=== ALL timeline_s* files (name, total, mtime) ===")
for p in sorted(glob.glob(os.path.join(ROOT,".work","timeline_s*.json"))):
    try:
        d = json.load(io.open(p,encoding="utf-8"))
        tot = d.get("total") if isinstance(d,dict) else None
        print(f"  {os.path.basename(p):28s} total={tot}  mtime={time.strftime('%m-%d %H:%M', time.localtime(os.path.getmtime(p)))}")
    except Exception as e:
        print(" ", os.path.basename(p), "ERR", e)

print()
print("=== ALL shots*.json ===")
for p in sorted(glob.glob(os.path.join(ROOT,".work","shots*.json"))):
    try:
        d = json.load(io.open(p,encoding="utf-8"))
        items = d if isinstance(d,list) else d.get("shots",[])
        print(f"  {os.path.basename(p):28s} shots={len(items)}  mtime={time.strftime('%m-%d %H:%M', time.localtime(os.path.getmtime(p)))}")
    except Exception as e:
        print(" ", os.path.basename(p), "ERR", e)

print()
print("=== t9 backgrounds ===")
bgdir = os.path.join(ROOT,"assets","bg")
t9 = sorted(f for f in os.listdir(bgdir) if f.startswith("t9"))
for f in t9: print("  ", f, os.path.getsize(os.path.join(bgdir,f)))
print("  count:", len(t9))

print()
print("=== t8 backgrounds (reference) ===")
t8 = sorted(f for f in os.listdir(bgdir) if f.startswith("t8"))
print("  count:", len(t8), " sample:", t8[:3])

print()
print("=== audio masters in .work root ===")
for p in sorted(glob.glob(os.path.join(ROOT,".work","audio_master*"))):
    print("  ", os.path.basename(p), probe(p))

print()
print("=== tts manifests t09 ===")
for p in glob.glob(os.path.join(ROOT,".work","tts_manifest_t09*")):
    d = json.load(io.open(p,encoding="utf-8"))
    items = d if isinstance(d,list) else d.get("items",d)
    print("  ", os.path.basename(p), "n=", len(items) if hasattr(items,'__len__') else "?")

print()
print("=== tts sentence audio dirs for t09 ===")
for d in sorted(glob.glob(os.path.join(ROOT,".work","tts_s*"))):
    name = os.path.basename(d)
    files = os.listdir(d)
    t9f = [f for f in files if "09" in f]
    print(f"  {name}: total={len(files)} with09={len(t9f)}")
