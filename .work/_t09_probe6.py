import io, json, os, re, glob, subprocess, time

ROOT = r"D:/TEST/Gax/amber-eyes"
W = os.path.join(ROOT, ".work")

print("=== dirs named *t09* under .work ===")
for p in sorted(glob.glob(os.path.join(W,"*t09*"))) + sorted(glob.glob(os.path.join(W,"*tap09*"))):
    if os.path.isdir(p):
        print("  DIR ", os.path.relpath(p,ROOT), len(os.listdir(p)), "files")
    else:
        print("  FILE", os.path.relpath(p,ROOT), os.path.getsize(p))

print()
print("=== tts_manifest_t09.json ===")
p = os.path.join(W,"tts_manifest_t09.json")
if os.path.exists(p):
    d = json.load(io.open(p,encoding="utf-8"))
    print("  type:",type(d).__name__,"len:",len(d))
    if isinstance(d,list) and d:
        print("  first:",json.dumps(d[0],ensure_ascii=False)[:400])
        print("  last :",json.dumps(d[-1],ensure_ascii=False)[:300])
        print("  ids sample:",[x.get("id") for x in d[:5]],"...",[x.get("id") for x in d[-3:]])

print()
print("=== tts manifests for t08 (reference naming) ===")
for p in sorted(glob.glob(os.path.join(W,"tts_manifest*t08*"))):
    d = json.load(io.open(p,encoding="utf-8"))
    print("  ", os.path.basename(p), "len=", len(d))

print()
print("=== script_tap09*.json sentence counts ===")
for lang,p in [("VN","script_tap09.json"),("EN","script_tap09_EN.json"),("JA","script_tap09_JA.json")]:
    fp = os.path.join(W,p)
    if not os.path.exists(fp): print(lang,"MISSING"); continue
    d = json.load(io.open(fp,encoding="utf-8"))
    n = sum(len(e.get("sentences",[])) for e in d if e.get("kind")=="LOI")
    ids = [s["id"] for e in d if e.get("kind")=="LOI" for s in e.get("sentences",[])]
    print(f"  {lang}: elements={len(d)} LOI_sentences={n} first={ids[:3]} last={ids[-3:]}")

print()
print("=== acting_tap09*: keys + _pause_after ===")
for lang,p in [("VN","acting_tap09.json"),("EN","acting_tap09_EN.json"),("JA","acting_tap09_JA.json")]:
    fp = os.path.join(W,p)
    if not os.path.exists(fp): print(lang,"MISSING"); continue
    d = json.load(io.open(fp,encoding="utf-8"))
    print(f"  {lang}: type={type(d).__name__} len={len(d)} keys5={list(d.keys())[:5]}")

print()
print("=== kaggle_higgs out dirs for t09 ===")
for p in sorted(glob.glob(os.path.join(W,"kaggle_higgs","*"))):
    if "t09" in p or "09" in os.path.basename(p):
        print("  ", os.path.relpath(p,ROOT), (len(os.listdir(p)) if os.path.isdir(p) else os.path.getsize(p)))
