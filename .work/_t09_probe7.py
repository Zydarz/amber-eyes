import io, json, os, re, glob, subprocess, time

ROOT = r"D:/TEST/Gax/amber-eyes"

# 1) git status for kichban tap09 + untracked
print("=== git status (kichban tap09 + untracked md) ===")
r = subprocess.run(["git","status","--porcelain"], cwd=ROOT, capture_output=True, text=True)
for l in r.stdout.splitlines():
    if "Tap09" in l or "tap09" in l or l.startswith("??"):
        print("  ", l)

print()
print("=== git log for 01_KICH_BAN/Tap09 ===")
r = subprocess.run(["git","log","--oneline","-5","--","01_KICH_BAN/Tap09"], cwd=ROOT, capture_output=True, text=True)
print(r.stdout or "  (none)")

print()
print("=== count sentences in MD using the project's own parser ===")
for lang, p in [("VN","01_KICH_BAN/Tap09/kichban_tap09_23102026.md"),
                 ("EN","01_KICH_BAN/Tap09/kichban_tap09_EN.md"),
                 ("JA","01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md")]:
    fp = os.path.join(ROOT,p)
    t = io.open(fp,encoding="utf-8").read()
    m = re.search(r"^#\s", t, re.M)
    # Vietnamese quotes: opening " (U+201C) closing " (U+201D)
    q_open = t.count("\u201c"); q_close = t.count("\u201d")
    # count lines that are a quoted block
    qblocks = re.findall(r"^\u201c(.*?)\u201d\s*$", t, re.M|re.S)
    print(f"  {lang}: file={os.path.getsize(fp)}B  curly_open={q_open} curly_close={q_close}  qblocks={len(qblocks)}")

print()
print("=== check parse_kichban.py location & usage ===")
for p in glob.glob(os.path.join(ROOT,".work","parse_kichban*.py")):
    print("  ", os.path.relpath(p,ROOT))
r = subprocess.run(["git","status","--porcelain",".work"], cwd=ROOT, capture_output=True, text=True)
print("  .work modified:", [l for l in r.stdout.splitlines() if "parse_kichban" in l or "parse_shots" in l or "build_video3" in l or "edition.py" in l])
