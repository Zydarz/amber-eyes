#!/usr/bin/env python3
"""List every KO narration line containing junk: unknown latin, disallowed chars,
sentence-count anomalies. Usage: _scan_ko.py <vn.md> <ko.md>"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

vn_path, ko_path = Path(sys.argv[1]), Path(sys.argv[2])
vn_raw = vn_path.read_text(encoding="utf-8")
ko_raw = ko_path.read_text(encoding="utf-8")

TOK = re.compile(r"[A-Za-z][A-Za-z'’\-]+")
vn_tokens = {t.lower() for t in TOK.findall(vn_raw)}
ALLOWED_CHARS = set(
    "가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9 \t.,;:!?‘’“”\"'()\[\]\-*/#&%=~@$"
    "…–—°©♥àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿłµ"
    "`_| +<>·※→←↑↓■□▲△●○◆◇★☆№§¶†‡•"
)

KO_KEEP = {  # latin tokens legitimately introduced by the KO edition
    "imperial", "university", "imp", "to", "of", "in", "for", "the", "and",
    "emotional", "desensitization", "moral", "decay", "post", "war", "crisis",
    "exploitation", "of", "desperation", "benevolent", "façade", "facade",
    "rationalization", "dehumanization", "proud", "recounting", "confession",
    "without", "fear", "coerced", "power", "control", "serial", "killer",
    "amber", "eyes", "deep", "ambient", "cello", "piano", "violin", "drone",
    "minimalist", "golden", "benchmark", "youtube", "safe", "rule", "v9",
    "ab", "mpd", "waseda", "shinjuku", "kotobuki", "miyuki", "ishikawa",
    "takeshi", "shiro", "nakayama", "yurie", "taniguchi", "tokyo", "kanto",
    "kansai", "osaka", "kyoto", "yokohama", "nagoya", "sapporo", "fukuoka",
    "hiroshima", "nagasaki", "sendai", "kobe", "okinawa", "hokkaido",
    "korean", "japanese", "chinese", "american", "european", "german",
    "french", "russian", "american", "united", "states", "kingdom",
    "city", "tokyo", "meta", "flex", "ai", "wav", "mp3", "aiff",
}


def bad_tokens(line):
    out = []
    for t in TOK.findall(line):
        low = t.lower()
        if low in vn_tokens or low in KO_KEEP:
            continue
        out.append(t)
    return out


def bad_chars(line):
    return sorted({c for c in line if c not in ALLOWED_CHARS})


vn_els = PK.parse_lines(vn_raw.splitlines())
ko_els = PK.parse_lines(ko_raw.splitlines())
vn_map = {e["id"]: e for e in vn_els}

# map each KO physical line -> element id, by walking elements and their sentences
line_of_sentence = {}
for e in ko_els:
    for s in e.get("sentences", []):
        line_of_sentence[id(s)] = e["id"]

print("=== per-line junk scan ===")
for i, line in enumerate(ko_raw.splitlines(), 1):
    bt = bad_tokens(line)
    bc = bad_chars(line)
    if bt or bc:
        print(f"{i:4d} | tokens={bt} chars={bc}")
        print(f"     {line[:200]}")

print("\n=== sentence count per element (VN vs KO) ===")
if len(vn_els) == len(ko_els):
    for a, b in zip(vn_els, ko_els):
        na, nb = len(a["sentences"]), len(b["sentences"])
        if na != nb:
            print(f"  {a['id']:5s} {a.get('role')} VN={na} KO={nb}")
            for s in a["sentences"]:
                print(f"      V| {s['text'][:120]}")
            for s in b["sentences"]:
                print(f"      K| {s['text'][:120]}")
else:
    print(f"  element count differs VN={len(vn_els)} KO={len(ko_els)}")
