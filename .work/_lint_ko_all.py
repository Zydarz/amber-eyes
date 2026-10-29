"""Lint TAT CA file KO co san: bat Latin la / chu Han / ky tu la trong TOAN BO file."""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = HERE.parent
SRC = {"01": "Tap01/kichban_tap01_22102026_v2.md", "02": "Tap02/kichban_tap02_22102026.md",
       "03": "Tap03/kichban_tap03_22102026.md"}
for n in range(4, 30):
    SRC[f"{n:02d}"] = f"Tap{n:02d}/kichban_tap{n:02d}_23102026.md"

TOK = re.compile(r"[A-Za-z][A-Za-z'\u2019\-]+")
HANJA = re.compile("[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]")
QUOTED = re.compile("[\u2018\u201c][^\u2019\u201d]*[\u2019\u201d]")
ALLOWED = re.compile(
    "[\uac00-\ud7a3\u1100-\u11ff\u3130-\u318fA-Za-z0-9\\s.,;:!?"
    "\u2018\u2019\u201c\u201d\"'()\\[\\]\\-*/#&%=~@$"
    "\u2026\u2013\u2014\u00b0\u00a9\u2665\u00e0-\u00ff\u0142\u00b5"
    "`_| +<>"
    "\u00b7\u203b\u2192\u2190\u2191\u2193\u25a0\u25a1\u25b2\u25b3\u25cf\u25cb"
    "\u25c6\u25c7\u2605\u2606\u2116\u00a7\u00b6\u2020\u2021\u2022"
    "\u300e\u300f]"
)

ALLOW_WORDS = {
    "first", "lady", "chicago", "sign", "stair", "massacre", "monster", "called", "they", "me",
    "white", "trauma", "bonding", "album", "beatles", "system", "machiavellianism",
    "extreme", "sensory", "deprivation", "syndrome", "learned", "helplessness",
    "x", "n", "s", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "o", "p", "q", "r", "t", "u", "v", "w", "y", "z", "kiss", "ass", "ceo", "api", "ok",
    "www", "http", "https", "com", "org", "net", "mr", "mrs", "dr", "st", "lsd",
}

bad_files = 0
for ep in sorted(SRC):
    vn_path = ROOT / "01_KICH_BAN" / SRC[ep]
    ko_path = ROOT / "01_KICH_BAN" / f"Tap{ep}_KO" / f"kichban_tap{ep}_KO.md"
    if not ko_path.exists():
        continue
    vn_raw = vn_path.read_text(encoding="utf-8")
    ko_raw = ko_path.read_text(encoding="utf-8")
    els = PK.parse_lines(ko_raw.splitlines())
    ko_txt = " ".join(e.get("text", "") for e in els if e["kind"] == "LOI")
    ko_txt_nq = QUOTED.sub(" ", ko_txt)      # bo trich dan (tieng Anh goc)
    vn_tokens = {t.lower() for t in TOK.findall(vn_raw)}

    issues = []
    vn_low = vn_raw.lower()
    for t in sorted(set(TOK.findall(ko_txt_nq))):
        if t.lower() not in vn_low:
            issues.append(f"latin-la:{t}")
    han = sorted(set(HANJA.findall(ko_raw)))
    if han:
        issues.append("hanja:" + "".join(han))
    stray = sorted({c for c in ko_raw if not ALLOWED.match(c)})
    if stray:
        issues.append("ky-la:" + "".join(stray))
    glued = sorted(set(re.findall(r"[\uac00-\ud7a3][A-Za-z]{2,}[\uac00-\ud7a3]", ko_txt)))
    if glued:
        issues.append("dinh-Hangul:" + ",".join(glued))

    if issues:
        bad_files += 1
        print(f"{ep}  ISSUE  " + " | ".join(issues))
    else:
        print(f"{ep}  clean")

print(f"\nfiles co issue: {bad_files}")
