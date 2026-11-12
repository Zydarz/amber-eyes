import io, json, os, re, glob, subprocess, time

ROOT = r"D:/TEST/Gax/amber-eyes"
W = os.path.join(ROOT, ".work")

def git(*args):
    r = subprocess.run(["git"]+list(args), cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.stdout

print("=== git status for 01_KICH_BAN/Tap09 ===")
out = git("status","--porcelain","01_KICH_BAN/Tap09","01_KICH_BAN/Tap09_EN","01_KICH_BAN/Tap09_JA")
print(out or "  (clean - no uncommitted change)")

print()
print("=== git log for those paths ===")
print(git("log","--oneline","-5","--","01_KICH_BAN/Tap09") or "  (none)")

print()
print("=== .md files modified in last 4 days anywhere (excl .work) ===")
cut = time.time() - 4*86400
for p in glob.glob(os.path.join(ROOT,"**","*.md"), recursive=True):
    if ".work" in p or "\\.git" in p: continue
    try:
        mt = os.path.getmtime(p)
    except OSError: continue
    if mt > cut:
        print("  ", time.strftime("%m-%d %H:%M", time.localtime(mt)), os.path.relpath(p,ROOT))

print()
print("=== .json in .work modified in last 2 days (excl probe) ===")
cut2 = time.time() - 2*86400
for p in glob.glob(os.path.join(W,"*.json")):
    mt = os.path.getmtime(p)
    if mt > cut2:
        print("  ", time.strftime("%m-%d %H:%M", time.localtime(mt)), os.path.basename(p))

print()
print("=== MD sentence counting (per-element quoted blocks) ===")
def count_md(path):
    t = io.open(path, encoding="utf-8").read()
    lines = t.split("\n")
    n_blocks = 0; n_lines = 0; in_q = False
    for L in lines:
        s = L.strip()
        if not s: continue
        if s.startswith("\u201c"):
            n_blocks += 1
            # count sentences inside by splitting on . ! ? followed by capital
            inner = s.strip("\u201c\u201d")
            n_lines += len([x for x in re.split(r"(?<=[.!?])\s+", inner) if x.strip()])
            if not s.endswith("\u201d"): in_q = True
            continue
        if in_q:
            n_lines += len([x for x in re.split(r"(?<=[.!?])\s+", s.strip("\u201c\u201d")) if x.strip()])
            if s.endswith("\u201d"): in_q = False
    return n_blocks, n_lines

for lang, p in [("VN","01_KICH_BAN/Tap09/kichban_tap09_23102026.md"),
                 ("EN","01_KICH_BAN/Tap09/kichban_tap09_EN.md"),
                 ("JA","01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md")]:
    b, l = count_md(os.path.join(ROOT,p))
    print(f"  {lang}: quoted_blocks={b}  sentences_inside≈{l}")
