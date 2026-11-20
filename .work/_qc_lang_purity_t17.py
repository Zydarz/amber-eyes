# -*- coding: utf-8 -*-
"""QC độ sạch ngôn ngữ cho 4 bản mô tả Tập 17 (chặn ký tự lạn quốc/ngôn ngữ trộn).

- VI / EN: KHÔNG được có CJK, Hangul, Cyrillic.
- JA: KHÔNG được có Cyrillic, Hangul; chữ Latin chỉ được là tên riêng / thuật ngữ trong
  danh sách cho phép.
- KO: KHÔNG được có Cyrillic, Hán tự; chữ Latin chỉ được là tên riêng / thuật ngữ cho phép.
"""
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT / ".work"))
import make_descriptions_t17 as M  # noqa: E402

ALLOW_LATIN = {
    "jordan", "turpin", "amber", "eyes", "objectification", "compartmentalization",
    "signature", "gift", "fear", "gavin", "de", "becker", "coercive", "control",
    "folie", "deux", "ptg", "mo", "the", "and", "or", "of", "a", "in", "to", "is",
    "it", "on", "for", "with", "as", "at", "by", "from", "up", "out", "los", "angeles",
    "times", "new", "york", "guardian", "bbc", "cnn", "nyt", "abc", "news", "diane",
    "sawyer", "michael", "hestrin", "riverside", "perris", "california", "david",
    "louise", "ann", "allen", "ep", "17", "911", "usa", "n1", "n2", "h", "d", "c",
    "sns", "halo", "effect", "america", "wanted", "escape", "house", "horror", "sisters",
    "speak", "people", "state", "v", "kids", "2021", "children", "12", "29", "37",
    "56", "49", "18", "19", "2018", "kids",
}
ALLOW_CJK_JA = set("第幕社会的余波と制度改革隣人の中で発見された地獄に郊外の街集団的恐怖偏執支配この事件EDI")


def script_of(ch):
    try:
        name = unicodedata.name(ch)
    except ValueError:
        return "?"
    for s in ("CYRILLIC", "HANGUL", "CJK", "HIRAGANA", "KATAKANA", "LATIN", "DIGIT"):
        if name.startswith(s):
            return s
    return "OTHER"


def latin_tokens(text):
    return [t for t in re.findall(r"[A-Za-z][A-Za-z'\-]*", text)]


def check(lang, text):
    bad = []
    for ch in text:
        sc = script_of(ch)
        if lang in ("VI", "EN"):
            if sc in ("CJK", "HIRAGANA", "KATAKANA", "HANGUL", "CYRILLIC"):
                bad.append(f"ký tự {lang}-forbidden [{sc}] '{ch}'")
        elif lang == "JA":
            if sc in ("CYRILLIC", "HANGUL"):
                bad.append(f"ký tự JA-forbidden [{sc}] '{ch}'")
        elif lang == "KO":
            if sc in ("CYRILLIC", "CJK"):
                bad.append(f"ký tự KO-forbidden [{sc}] '{ch}'")
    if lang in ("JA", "KO"):
        for t in latin_tokens(text):
            if t.lower().strip("'") in ALLOW_LATIN and len(t) > 1:
                continue
            if len(t) > 1:
                bad.append(f"chữ Latin lạ trong {lang}: '{t}'")
    # ký tự điều khiển / thay thế
    for ch in text:
        if ch in "\ufffd\u0000" or (unicodedata.category(ch) == "Cc" and ch not in "\n\t"):
            bad.append(f"ký tự điều khiển lạ U+{ord(ch):04X}")
    return bad


print("=== QC SẠCH NGÔN NGỮ — MÔ TẢ TẬP 17 ===")
all_ok = True
for lang, body in [("VI", M.BODY_VI), ("EN", M.BODY_EN), ("JA", M.BODY_JA), ("KO", M.BODY_KO)]:
    issues = check(lang, body)
    # thêm: JA/KO phải có đủ 10 mục chỉ dấu
    n_items = len(re.findall(r"^\d+\.\s", body, re.M))
    print(f"[{lang}] {len(body):5d} ký tự | mục chỉ dấu: {n_items}/10 | "
          f"{'SẠCH' if not issues and n_items == 10 else 'CÓ VẤN ĐỀ'}")
    if n_items != 10:
        issues.append(f"thiếu/thừa mục chỉ dấu: {n_items}/10")
    for i in dict.fromkeys(issues):
        print(f"    - {i}")
        all_ok = False
print("\nKẾT QUẢ:", "PASS" if all_ok else "FAIL")
sys.exit(0 if all_ok else 1)
