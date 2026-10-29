"""Lint ban KO: bat cac tu Latin khong co trong file VN (rac tieng, chinh ta,
so lieu bi chieu) + Hanja + dau cham sai.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

vn_path, ko_path = Path(sys.argv[1]), Path(sys.argv[2])


def narration(path):
    els = PK.parse_lines(path.read_text(encoding="utf-8").splitlines())
    return " ".join(e.get("text", "") for e in els if e["kind"] == "LOI")


vn_raw = vn_path.read_text(encoding="utf-8")
ko_raw = ko_path.read_text(encoding="utf-8")
vn_txt = narration(vn_path)
ko_txt = narration(ko_path)

# Latin tokens: letter+ letter (apostrophes ok). Numbers with units too.
TOK = re.compile(r"[A-Za-z][A-Za-z'’\-]+")
# a Latin token glued to Hangul with no space => suspicious
GLUED = re.compile(r"[가-힣][A-Za-z]{2,}[가-힣]")

vn_tokens = {t.lower() for t in TOK.findall(vn_raw)}
ko_tokens = TOK.findall(ko_txt)

# allowlist: latin that legitimately appears only in KO (technical terms / glosses)
ALLOW = {
    "first", "lady", "Chicago", "sign", "stair", "massacre", "monster", "called", "they", "me",
    "tag", "x", "n", "s", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "o", "p", "q", "r", "t", "u", "v", "w", "y", "z", "kiss", "ass", "ceo", "api", "ok",
    "www", "http", "https", "com", "org", "net", "mr", "mrs", "dr", "st",
    # thuat ngu chuyen mon giu tieng Anh (theo glossary)
    "white", "trauma", "bonding", "album", "beatles", "system", "machiavellianism",
    "extreme", "sensory", "deprivation", "syndrome", "learned", "helplessness",
}

unknown = {}
for t in ko_tokens:
    if t.lower() in vn_tokens or t.lower() in ALLOW:
        continue
    unknown[t] = unknown.get(t, 0) + 1

print("--- Latin token trong KO khong co trong VN ---")
if unknown:
    for t, c in sorted(unknown.items(), key=lambda x: -x[1]):
        print(f"  {c:>3}x  {t}")
else:
    print("  (none)")

print("\n--- Hanja / chu Han trong KO narration ---")
HANJA = re.compile("[" + chr(0x4E00) + "-" + chr(0x9FFF)
                   + chr(0xF900) + "-" + chr(0xFAFF) + "]")
h = sorted(set(HANJA.findall(ko_txt)))
print("  " + ("".join(h) if h else "(none)"))

print("\n--- Hanja / chu Han trong TOAN BO file KO (ke ca metadata) ---")
h2 = sorted(set(HANJA.findall(ko_raw)))
print("  " + ("".join(h2) if h2 else "(none)"))

print("\n--- Latin token dinh tien do chu Hangul (dinh dang) ---")
g = sorted(set(GLUED.findall(ko_txt)))
print("  " + (", ".join(g) if g else "(none)"))

print("\n--- Dau cham tieng Viet con lai ---")
VN_STRICT = set("ằắẳẵặầấẩẫậềếểễệỉịồốổỗộớởỡợứửữựỳỷỹỵđĐạảãẵ")
print("  " + "".join(sorted({c for c in ko_txt if c in VN_STRICT})))

print("\n--- Ky tu la (rac / chu Han) trong TOAN BO file KO ---")
ALLOWED = re.compile(
    "[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9\\s.,;:!?‘’“”\"'()\\[\\]\\-*/#&%=~@$"
    "…–—°©♥àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿłµ"
    "`_| +<>·※→←↑↓■□▲△●○◆◇★☆№§¶†‡•]"
)
bad = {}
for i, ch in enumerate(ko_raw):
    if not ALLOWED.match(ch):
        bad.setdefault(ch, []).append(i)
if bad:
    for ch, pos in bad.items():
        print(f"  {ch!r} x{len(pos)}  -> {ko_raw[max(0,pos[0]-45):pos[0]+25]!r}")
else:
    print("  (none)")

print("\n--- Cau bat dau bang chu so (se khong tach cau) ---")
bad = []
for e in PK.parse_lines(ko_raw.splitlines()):
    for s in e.get("sentences", []):
        t = s["text"].strip()
        if t and t[0].isdigit():
            bad.append((e["id"], s["id"], t[:70]))
if bad:
    for i, sid, t in bad:
        print(f"  {i} {sid}: {t}")
else:
    print("  (none)")
