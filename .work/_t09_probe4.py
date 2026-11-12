import io, json, os, re, glob, subprocess, time, shutil

ROOT = r"D:/TEST/Gax/amber-eyes"
FF = os.path.join(ROOT, ".work", "ffmpeg", "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0")
FFPROBE = os.path.join(FF, "bin", "ffprobe.exe")
print("ffprobe exists:", os.path.exists(FFPROBE))

def probe(mp):
    if not os.path.exists(FFPROBE): return "NO_FFPROBE"
    try:
        out = subprocess.run([FFPROBE,"-v","error","-show_entries","format=duration","-of","csv=p=0",mp],
                             capture_output=True, text=True)
        return out.stdout.strip() or out.stderr.strip()[:80]
    except Exception as e:
        return "ERR "+str(e)

print()
print("=== masters under 02_SAN_XUAT (any mp3/wav), t08+t09 ===")
for p in sorted(glob.glob(os.path.join(ROOT,"02_SAN_XUAT","**","*.mp3"), recursive=True)):
    rel = os.path.relpath(p, ROOT)
    if any(k in rel for k in ("Tap08","Tap09","Tap07")):
        print(f"  {rel}  dur={probe(p)}  {os.path.getsize(p)}")

print()
print("=== .work/audio_master* ===")
for p in sorted(glob.glob(os.path.join(ROOT,".work","audio_master*"))):
    print("  ", os.path.basename(p), probe(p), os.path.getsize(p))

print()
print("=== timeline_s_t09.json content summary ===")
d = json.load(io.open(os.path.join(ROOT,".work","timeline_s_t09.json"),encoding="utf-8"))
print("  keys:", list(d.keys()))
for k,v in d.items():
    if isinstance(v,list):
        print("  ",k,"len=",len(v))
        if v: print("     first:", json.dumps(v[0],ensure_ascii=False)[:250]); print("     last:", json.dumps(v[-1],ensure_ascii=False)[:250])
    else:
        print("  ",k,"=",v)

print()
print("=== acting_tap09.json structure ===")
a = json.load(io.open(os.path.join(ROOT,".work","acting_tap09.json"),encoding="utf-8"))
print("  type:", type(a).__name__, "len:", len(a))
if isinstance(a,list):
    print("  first:", json.dumps(a[0],ensure_ascii=False)[:400])
    print("  last :", json.dumps(a[-1],ensure_ascii=False)[:400])
    ids = [x.get("id") for x in a]
    print("  ids first10:", ids[:10], "... last10:", ids[-10:])
