#!/usr/bin/env python3
"""Fix Tap26 KO: malformed role line, Hanja/garbage tokens, split multi-sentence
narration lines using the parser's own sentence-split regex."""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

KO = Path(r"D:\TEST\Gax\Audi\01_KICH_BAN\Tap26_KO\kichban_tap26_KO.md")
text = KO.read_text(encoding="utf-8")

# --- 1. role line fix -------------------------------------------------------
ROLE_FIX = [
    ("**호스트** *(*지옥 같은 계약과 궁지에 몰린 부모들*)*:",
     "**호스트** *(지옥 같은 계약과 궁지에 몰린 부모들)*:"),
]
for old, new in ROLE_FIX:
    if old in text:
        text = text.replace(old, new)
        print("fixed role line")
    else:
        print(f"!! role target not found: {old[:60]}")
        # fallback: any line with '**호스트** *(' pattern
        for m in re.finditer(r"^\*\*호스트\*\* \*\(.*$", text, re.M):
            print("   candidate:", m.group(0)[:100])

# --- 2. garbage tokens ------------------------------------------------------
REPL = [
    ("Sport했습니다", "말했습니다"),
    ("긴급 압수令을 집행했습니다", "긴급 압수 명령을 집행했습니다"),
    ("Tokyo 제국대학교 산원学科을", "Tokyo 제국대학교 산원 전공을"),
    ("성실한收养인을", "성실한 입양인을"),
    ("돌보거나收养인을", "돌보거나 입양인을"),
    ("가장识别하기 어렵고", "가장 식별하기 어렵고"),
    ("Ishikawa女士는", "Ishikawa 씨는"),
    ("안전한儿童 공동체를", "안전한 아동 공동체를"),
]
for old, new in REPL:
    if old in text:
        text = text.replace(old, new)
    else:
        print(f"!! replace target not found: {old[:60]}")

# --- 3. split multi-sentence narration lines --------------------------------
LATIN_SPLIT = PK.LATIN_SPLIT
ROLE_LINE = re.compile(r"^\*\*(호스트|수사관|심리학자|일반인)\*\*")
CUE_LINE = re.compile(r"^\*\*\[(BGM|SFX|NGHI)\]")
out = []
split_count = 0
for line in text.split("\n"):
    if ROLE_LINE.match(line) or CUE_LINE.match(line) or not line.strip():
        out.append(line)
        continue
    parts = re.split(LATIN_SPLIT, line)
    parts = [p for p in parts if p.strip()]
    if len(parts) > 1:
        split_count += 1
        print(f"split into {len(parts)}: {line[:70]}")
        out.extend(parts)
    else:
        out.append(line)

KO.write_text("\n".join(out), encoding="utf-8")
print(f"lines split: {split_count}")
