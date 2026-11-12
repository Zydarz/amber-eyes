import io, json, os, re, glob, subprocess, time

ROOT = r"D:/TEST/Gax/amber-eyes"
FF = os.path.join(ROOT, ".work", "ffmpeg", "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0")
FFPROBE = os.path.join(FF, "bin", "ffprobe.exe")

def probe(mp):
    try:
        out = subprocess.run([FFPROBE,"-v","error","-show_entries","format=duration","-of","csv=p=0",mp],
                             capture_output=True, text=True)
        return out.stdout.strip()
    except Exception as e:
        return "ERR"

print("=== tts_s* dirs : any file mentioning 09 ===")
for d in sorted(glob.glob(os.path.join(ROOT,".work","tts_s*"))):
    if not os.path.isdir(d): continue
    files = os.listdir(d)
    hit = [f for f in files if re.search(r"(^|[_\-.])0?9([_\-]|\d)", f)]
    t9 = [f for f in files if "09" in f]
    print(f"  {os.path.basename(d)}: total={len(files)} '09'-containing={len(t9)}")
    if t9[:3]: print("     e.g.", t9[:3])

print()
print("=== .work/audio_s* dirs ===")
for d in sorted(glob.glob(os.path.join(ROOT,".work","audio_s*"))):
    files = os.listdir(d)
    print(f"  {os.path.basename(d)}: {len(files)} files; sample={files[:2]}")

print()
print("=== any wav/mp3 whose name has 09 anywhere under .work (non voice_ref) ===")
n=0
for p in glob.glob(os.path.join(ROOT,".work","**","*.wav"), recursive=True):
    b = os.path.basename(p)
    if "09" in b and "voice_ref" not in p and "ref_" not in b:
        print("  ", os.path.relpath(p,ROOT), probe(p)); n+=1
        if n>25: break
print("  total shown:", n)

print()
print("=== .work/stems* / audio_mix* t09 ===")
for pat in ["audio_mix_raw*","stems*","cer_sang_loc_giong_nam*"]:
    for p in sorted(glob.glob(os.path.join(ROOT,".work",pat)))[:10]:
        print("  ", os.path.basename(p))

print()
print("=== build_video3.py : CLI / --stills / AE_EP handling ===")
src = io.open(os.path.join(ROOT,".work","build_video3.py"),encoding="utf-8").read()
print("  len:", len(src))
for m in re.finditer(r"^.*(AE_EP|AE_LANG|--stills|def main|argparse|EPISODES\[).*$", src, re.M):
    line = m.group(0).strip()
    if len(line) < 160: print("   ", line)
