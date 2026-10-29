import sys, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

VN = "01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md"
KO = "01_KICH_BAN/Tap01_KO/kichban_tap01_KO.md"
vn = PK.parse_lines(open(VN, encoding="utf-8").read().splitlines())
ko = PK.parse_lines(open(KO, encoding="utf-8").read().splitlines())

print("### per-turn sentence count diff")
for a, b in zip(vn, ko):
    if a["kind"] == "LOI":
        na, nb = len(a["sentences"]), len(b["sentences"])
        if na != nb:
            print(f"{a['id']}: VN {na} vs KO {nb}")
            for s in a["sentences"]:
                print(f"    VN> {s['text'][:120]}")
            for s in b["sentences"]:
                print(f"    KO> {s['text'][:120]}")

print()
print("### quotes in VN raw")
vnraw = open(VN, encoding="utf-8").read()
for m in re.finditer(r"'([^']{4,})'", vnraw):
    print("  VN:", repr(m.group(1)))
print("### quotes in KO raw")
koraw = open(KO, encoding="utf-8").read()
for m in re.finditer(r"‘([^’]{2,})’", koraw):
    print("  KO:", repr(m.group(1)))
print("### ascii-quoted in KO raw")
for m in re.finditer(r"'([^']{2,})'", koraw):
    print("  KO-ascii:", repr(m.group(1)))

print()
print("### leftover diacritics / hanja in KO narration")
kotxt = " ".join(e.get("text", "") for e in ko if e["kind"] == "LOI")
for i, c in enumerate(kotxt):
    if c in "àáảãạằắẳẵặầấẩẫậẫắèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵđĐ":
        print("  diacritic:", repr(c), "ctx:", repr(kotxt[max(0,i-45):i+45]))
for i, c in enumerate(kotxt):
    if "一" <= c <= "鿿" or "豈" <= c <= "﫿":
        print("  hanja:", repr(c), "ctx:", repr(kotxt[max(0,i-45):i+45]))
