import io, json, os, re, glob, subprocess, time
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")

def git(*a):
    r = subprocess.run(["git"]+list(a), cwd=str(ROOT), capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.stdout

print("=== git stash / branch ===")
print(git("stash","list") or "  (no stash)")
print(git("branch","-a"))

print()
print("=== quoted LINES (reading lines) count in Tap09 MD ===")
for lang,p in [("VN","01_KICH_BAN/Tap09/kichban_tap09_23102026.md"),
                ("EN","01_KICH_BAN/Tap09/kichban_tap09_EN.md"),
                ("JA","01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md")]:
    t = (ROOT/p).read_text(encoding="utf-8")
    lines = t.split("\n")
    in_q = False; qlines = 0
    for L in lines:
        s = L.strip()
        if not s: continue
        if re.match(r"^\*\*(HOST|NGƯỜI BÌNH THƯỜNG|ĐIỀU TRA VIÊN|CHUYÊN GIA TÂM LÝ|HOST|INVESTIGATOR|PSYCHOLOGIST|ORDINARY PERSON|ホスト|捜査官|心理学者|一般人)\*\*", s):
            in_q = True; continue
        if s.startswith("**[") or s.startswith("## "):
            in_q = False; continue
        if in_q and not s.startswith("**") and not s.startswith("|"):
            qlines += 1
    print(f"  {lang}: quoted_reading_lines≈{qlines}")

print()
print("=== git log 02_SAN_XUAT/Tap09 ===")
print(git("log","--oneline","-6","--","02_SAN_XUAT/Tap09") or "  (none)")

print()
print("=== is master mp3 gitignored? ===")
print(git("check-ignore","-v","02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.mp3") or "  (not ignored / not exist)")

print()
print("=== search whole repo for t09 audio wav/mp3 (name has 1_02_01 / s1_02_01 style) ===")
hits = []
for p in glob.glob(str(ROOT/".work"/"**","*.wav"), recursive=True):
    if "09" in p and "voice_ref" not in p:
        hits.append(os.path.relpath(p, str(ROOT)))
print("  count:", len(hits))
for h in hits[:10]: print("   ", h)

print()
print("=== audio_s_higgs* dirs ===")
for d in sorted(glob.glob(str(ROOT/".work"/"audio_s*"))):
    print("  ", os.path.basename(d), len(os.listdir(d)))

print()
print("=== how was timeline_s_t09.json produced? grep .work for 'timeline_s_t09' ===")
for p in glob.glob(str(ROOT/".work"/"*.py")):
    try: s = io.open(p,encoding="utf-8",errors="replace").read()
    except Exception: continue
    if "timeline_s_t09" in s:
        print("  ", os.path.basename(p))
