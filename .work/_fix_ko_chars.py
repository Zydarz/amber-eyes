"""Sua cac chu Han + rac trong file KO (dung khi edit tool khop khong chinh xac)."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

path = Path(sys.argv[1])
raw = path.read_text(encoding="utf-8")

REPL = [
    ("災祸", "재앙"),          # 災祸 -> 재앙
    ("灾祸", "재앙"),
    ("刺耳한", "한"),
    ("긴장감을Armyả는", "긴장감을 자아내는"),
    ("Colleen을", "Colleen을"),   # ky tu Kiril -> Hangul
]

# them ky tu Cyrillic / Greek trong file -> ky tu Hangul tuong duong
CYR = {"л": "을", "и": "이", "ш": "스", "ь": "으", "а": "아", "е": "에",
       "о": "오", "с": "스", "т": "트", "н": "н", "р": "르", "в": "브",
       "г": "그", "м": "으", "у": "우", "к": "크", "д": "드", "з": "즈",
       "п": "프", "я": "야", "ы": "이", "э": "에", "ж": "주", "ч": "ч"}

for a, b in REPL:
    if a in raw:
        raw = raw.replace(a, b)
        print(f"replaced {a!r} -> {b!r}")

for a, b in CYR.items():
    if a in raw:
        raw = raw.replace(a, b)
        print(f"replaced cyrillic {a!r} -> {b!r}")

path.write_text(raw, encoding="utf-8")

# bao cao con ky tu la
import re
ALLOWED = re.compile(
    "[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9\\s.,;:!?‘’“”\"'()\\[\\]\\-*/#&%=~@$"
    "…–—°©♥àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿłµ"
    "`_| +<>·※→←↑↓■□▲△●○◆◇★☆№§¶†‡•]"
)
bad = {}
for i, ch in enumerate(raw):
    if not ALLOWED.match(ch):
        bad.setdefault(ch, []).append(i)
print("--- con la ---")
for ch, pos in bad.items():
    print(f"  {ch!r} x{len(pos)} -> {raw[max(0,pos[0]-45):pos[0]+25]!r}")
if not bad:
    print("  (none)")
