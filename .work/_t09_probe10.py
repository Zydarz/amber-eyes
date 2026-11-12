import io, os, re, glob, time, subprocess
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")

print("=== files modified in last 3 days anywhere under D:/TEST/Gax (all types) ===")
cut = time.time() - 3*86400
hits = []
for base in [r"D:/TEST/Gax"]:
    for dp, dn, fn in os.walk(base):
        if any(x in dp for x in ("\\.git", "node_modules", "__pycache__")): continue
        for f in fn:
            fp = os.path.join(dp,f)
            try:
                mt = os.path.getmtime(fp)
            except OSError: continue
            if mt > cut:
                hits.append((mt, fp, os.path.getsize(fp)))
hits.sort(reverse=True)
for mt, fp, sz in hits[:60]:
    print("  ", time.strftime("%m-%d %H:%M", time.localtime(mt)), f"{sz:>10}", os.path.relpath(fp, ROOT) if fp.startswith(str(ROOT)) else fp)
print("  TOTAL:", len(hits))

print()
print("=== user profile dirs: recent md/json mentioning Manson ===")
for d in [Path.home()/"Desktop", Path.home()/"Downloads", Path.home()/"Documents"]:
    if not d.exists(): continue
    for p in d.rglob("*"):
        if p.is_file() and p.suffix.lower() in (".md",".txt",".json",".docx"):
            try: mt = p.stat().st_mtime
            except OSError: continue
            if mt > cut and "manson" in p.name.lower():
                print("  ", time.strftime("%m-%d %H:%M", time.localtime(mt)), p)
