import io, os, re, json, glob, subprocess, time
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")

def git(*a):
    r = subprocess.run(["git"]+list(a), cwd=str(ROOT), capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.stdout

print("=== git log for Tap09 VN script (with dates) ===")
print(git("log","--format=%h %ad %s","--date=short","--","01_KICH_BAN/Tap09/kichban_tap09_23102026.md"))

print()
print("=== sentence count of Tap09 script AT each commit ===")
for sha in git("log","--format=%h","--","01_KICH_BAN/Tap09/kichban_tap09_23102026.md").split():
    r = subprocess.run(["git","show",f"{sha}:01_KICH_BAN/Tap09/kichban_tap09_23102026.md"],
                       cwd=str(ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode: continue
    txt = r.stdout
    # count quoted blocks
    n = len(re.findall(r'"', txt))
    print(f"  {sha}: quotes={n} lines={len(txt.splitlines())}")

print()
print("=== .gitignore relevant lines ===")
gi = (ROOT/".gitignore").read_text(encoding="utf-8", errors="replace").splitlines()
for l in gi:
    if any(k in l for k in ("mp3","wav","png","jpg","stills","bg")): print("   ", l)

print()
print("=== 02_SAN_XUAT/Tap09_EN + Tap09_JA contents ===")
for d in ["02_SAN_XUAT/Tap09_EN","02_SAN_XUAT/Tap09_JA"]:
    p = ROOT/d
    if not p.is_dir(): print(f"  {d}: MISSING"); continue
    for dp,dn,fn in os.walk(p):
        for f in fn:
            fp = Path(dp)/f
            print(f"   {os.path.relpath(fp,ROOT)}  {fp.stat().st_size}")

print()
print("=== 02_SAN_XUAT/Tap08/xuat_ban listing (reference) ===")
p = ROOT/"02_SAN_XUAT/Tap08/xuat_ban"
if p.is_dir():
    for f in sorted(p.iterdir()):
        print(f"   {f.name}  {f.stat().st_size}")
