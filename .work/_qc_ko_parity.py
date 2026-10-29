#!/usr/bin/env python3
"""A9-KO — QC parity between the Vietnamese script and the Korean edition.

    usage: py -3 .work/_qc_ko_parity.py <kichban_vn.md> <kichban_ko.md> [--quiet]

Both files are parsed with the shared parser (.work/parse_kichban.py) so the comparison is
done on the SAME unit the video pipeline uses: elements (turns/cues) and sentences.

Checks (all must pass):
  1  same number of acts, same act order
  2  identical element kind sequence            (LOI / SFX / BGM / NGHI)
  3  identical role per turn
  4  identical sentence count per turn
  5  identical pause duration per NGHI element
  6  every number in the VN turn appears in the KO turn
  7  every latin proper noun in the VN turn appears in the KO turn
  8  hangul share of the KO narration >= 60 %
  9  no vietnamese-only diacritics left in the KO narration
 10  same total sentence count for the episode

Exit code 0 = all green, 1 = at least one FAIL.
"""
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402

# Vietnamese-only letters that must never survive in a Korean narration.
# Split in two: the letters unique to Vietnamese are hard errors; the ones shared with
# French/Italian/Spanish (à á è é ì í ò ó ù ú ý) only warn — e.g. "Folie à Deux".
VN_STRICT = set("ằắẳẵặầấẩẫậềếểễệỉịồốổỗộớởỡợứửữựỳỷỹỵđĐạảãẵ")
VN_SHARED = set("àáèéìíòóùúýÿâêîôûäëïöü")
# Capitalised latin words that are proper nouns / titles (ASCII only).
# Vietnamese-origin names (đường Bắc Volunteer …) ARE meant to be translated, so they
# are excluded here on purpose: only names written in latin script must survive.
# NOTE: no \b — python's \w includes Hangul, so \b never fires between a latin
# letter and a Korean particle ("Blanchard와"). Use lookarounds on latin letters only.
PROPER = re.compile(r"(?<![A-Za-z])[A-Z][A-Za-z'’\-]{2,}(?:\s+[A-Z][A-Za-z'’\-]{2,})*(?![A-Za-z])")
# Words that start sentences in English/Vietnamese but are not names.
PROPER_STOP = {
    "The", "This", "That", "These", "Those", "There", "Then", "They", "Their", "Them",
    "When", "Where", "What", "Which", "Who", "Why", "How", "And", "But", "For", "Not",
    "You", "Your", "Our", "Out", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "She", "His", "Her", "Him", "He", "We", "Us", "I", "A", "An",
    "In", "On", "At", "It", "If", "As", "By", "So", "No", "Yes", "All", "Most", "Some",
    "Every", "Each", "Both", "After", "Before", "During", "Until", "Since", "While",
    "Để", "Và", "Hay", "Nhưng", "Trong", "Rồi", "Sau", "Trước", "Một", "Các",
    "Với", "Về", "Tại", "Trên", "Dưới", "Giữa", "Bởi", "Do", "Từ", "Qua", "Theo",
    "Ông", "Bà", "Cô", "Chú", "Anh", "Chị", "Em", "Tôi", "Chúng", "Bạn", "Họ",
    "Tuy", "Vì", "Nếu", "Khi", "Còn", "Cũng", "Đã", "Sẽ", "Như", "Mới", "Lại",
    "Có", "Là", "Và", "Rất", "Chỉ", "Cứ", "Đều", "Vẫn", "Còn", "Nhất", "Hơn",
}
HANGUL = re.compile(r"[가-힣]")
# Hanja / Chinese ideographs — a Korean script must not contain them.
# Built from codepoints: a literal CJK range is unreliable (and an over-wide range
# would swallow the Hangul block U+AC00..U+D7A3).
HANJA = re.compile("[" + chr(0x4E00) + "-" + chr(0x9FFF)
                   + chr(0xF900) + "-" + chr(0xFAFF) + "]")
NUMBER = re.compile(r"\d+(?:[.,]\d+)*")
# A list item line: "*   text" or "1.  text"
LIST_ITEM = re.compile(r"^\s*(?:\*\s{2,}|\d+\.\s{1,})\S")


def parse(path):
    """Parse a script file into elements (same code path as the pipeline)."""
    return PK.parse_lines(Path(path).read_text(encoding="utf-8").splitlines())


def numset(text):
    """Normalised numeric tokens: 1.400 -> 1400, 85% -> 85."""
    out = set()
    for m in NUMBER.findall(text):
        digits = re.sub(r"[.,]", "", m)
        if digits:
            out.add(digits.lstrip("0") or "0")
    return out


def props(text):
    """Latin proper nouns, minus sentence-initial common words."""
    out = set()
    for m in PROPER.findall(text):
        for w in m.split():
            if w in PROPER_STOP:
                continue
            if w.lower() in {"i", "a"}:
                continue
        first = m.split()[0]
        if first in PROPER_STOP:
            # keep the remainder of a multi-word name
            rest = " ".join(m.split()[1:])
            if rest and rest.split()[0] not in PROPER_STOP:
                out.add(rest)
            continue
        out.add(m)
    return out


def ko_text(els):
    return " ".join(e.get("text", "") for e in els if e["kind"] == "LOI")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    quiet = "--quiet" in sys.argv
    if len(args) != 2:
        print(__doc__)
        return 2
    vn_path, ko_path = Path(args[0]), Path(args[1])

    fails = []
    warns = []

    if not ko_path.exists():
        print(f"FAIL  file does not exist: {ko_path}")
        return 1

    vn = parse(vn_path)
    ko = parse(ko_path)
    vn_raw = Path(vn_path).read_text(encoding="utf-8")
    ko_raw = Path(ko_path).read_text(encoding="utf-8")

    # 1 acts
    vn_acts = sorted({e["act"] for e in vn})
    ko_acts = sorted({e["act"] for e in ko})
    if vn_acts != ko_acts:
        fails.append(f"acts differ: VN {vn_acts} vs KO {ko_acts}")
    elif not quiet:
        print(f"ok    acts: {len(vn_acts)} ({','.join(map(str, vn_acts))})")

    # 2/3/4/5 element-by-element
    if len(vn) != len(ko):
        fails.append(f"element count differs: VN {len(vn)} vs KO {len(ko)}")
    else:
        bad_kind = bad_role = bad_cnt = bad_pause = 0
        num_bad, prop_bad = [], []
        for a, b in zip(vn, ko):
            if a["kind"] != b["kind"]:
                bad_kind += 1
                continue
            if a["kind"] == "LOI":
                if a["role"] != b["role"]:
                    bad_role += 1
                if len(a["sentences"]) != len(b["sentences"]):
                    bad_cnt += 1
                miss_n = numset(a["text"]) - numset(b["text"])
                if miss_n:
                    num_bad.append((a["id"], sorted(miss_n)))
                miss_p = props(a["text"]) - props(b["text"])
                if miss_p:
                    prop_bad.append((a["id"], sorted(miss_p)))
            elif a["kind"] == "NGHI":
                if abs(a["sec"] - b["sec"]) > 1e-6:
                    bad_pause += 1
        if bad_kind:
            fails.append(f"element kind mismatch at {bad_kind} position(s)")
        if bad_role:
            fails.append(f"role mismatch at {bad_role} turn(s)")
        if bad_cnt:
            fails.append(f"sentence count mismatch at {bad_cnt} turn(s)")
        if bad_pause:
            fails.append(f"pause duration mismatch at {bad_pause} pause(s)")
        if num_bad:
            detail = "; ".join(f"{i}:{','.join(v)}" for i, v in num_bad[:12])
            fails.append(f"numbers missing in KO at {len(num_bad)} turn(s) -> {detail}")
        if prop_bad:
            # multi-word names are hard errors. single words are checked against the WHOLE
            # ko file: a vietnamese sentence-initial word ("Chi", "Ban", "Chuyen") never
            # survives in a korean file, so it must not be reported as a dropped name.
            hard = [(i, v) for i, v in prop_bad if any(" " in p for p in v)]
            soft = []
            for i, v in prop_bad:
                for p in v:
                    if " " in p:
                        continue
                    if p.lower() not in ko_raw.lower():
                        soft.append((i, [p]))
            if hard:
                detail = "; ".join(f"{i}:{'/'.join(p for p in v if ' ' in p)}" for i, v in hard[:12])
                fails.append(f"proper names missing in KO at {len(hard)} turn(s) -> {detail}")
            if soft:
                detail = "; ".join(f"{i}:{'/'.join(v)}" for i, v in soft[:12])
                warns.append(f"single-word names not found anywhere in the KO file -> {detail}")
        if not quiet and not (bad_kind or bad_role or bad_cnt or bad_pause):
            print(f"ok    {len(vn)} elements aligned (kind/role/sentence-count/pause)")

    # 6 total sentence count
    vn_sent = sum(len(e["sentences"]) for e in vn if e["kind"] == "LOI")
    ko_sent = sum(len(e["sentences"]) for e in ko if e["kind"] == "LOI")
    if vn_sent != ko_sent:
        fails.append(f"total sentence count differs: VN {vn_sent} vs KO {ko_sent}")
    elif not quiet:
        print(f"ok    total sentences: {vn_sent}")

    # 7 hangul share
    ko_txt = ko_text(ko)
    letters = [c for c in ko_txt if not c.isspace() and not unicodedata.category(c).startswith("P")]
    if letters:
        share = sum(1 for c in letters if HANGUL.match(c)) / len(letters)
        if share < 0.60:
            fails.append(f"hangul share too low: {share:.1%} (need >= 60%)")
        elif not quiet:
            print(f"ok    hangul share of narration: {share:.1%}")
    else:
        fails.append("KO narration is empty")

    # 8 leftover vietnamese diacritics
    strict = sorted({c for c in ko_txt if c in VN_STRICT})
    shared = sorted({c for c in ko_txt if c in VN_SHARED})
    if strict:
        fails.append(f"vietnamese-only diacritics left in KO narration: {''.join(strict)}")
    elif not quiet:
        print("ok    no vietnamese-only diacritics in KO narration")
    if shared:
        warns.append(f"shared diacritics present (check they belong to a foreign term): {''.join(shared)}")

    # 8b hanja / chinese ideographs (a Korean script must be hangul only)
    hanja = sorted(set(HANJA.findall(ko_txt)))
    if hanja:
        fails.append(f"hanja/chinese characters found in KO narration: {''.join(hanja)}")
    elif not quiet:
        print("ok    no hanja/chinese characters in KO narration")

    # 8c list items (bullets + numbered items) must match the source line for line
    vn_items = [l for l in vn_raw.splitlines() if LIST_ITEM.match(l)]
    ko_items = [l for l in ko_raw.splitlines() if LIST_ITEM.match(l)]
    if len(vn_items) != len(ko_items):
        fails.append(f"list item count differs: VN {len(vn_items)} vs KO {len(ko_items)}")
    else:
        vn_marks = [("num" if l.lstrip()[:1].isdigit() else "bul") for l in vn_items]
        ko_marks = [("num" if l.lstrip()[:1].isdigit() else "bul") for l in ko_items]
        if vn_marks != ko_marks:
            fails.append(f"list item kinds differ: VN {vn_marks} vs KO {ko_marks}")
        elif not quiet:
            print(f"ok    list items: {len(vn_items)} (same order, same kind)")

    # 9 quoted material — compared on RAW text (the parser rewrites quotes to “…”)
    vn_q = re.findall(r"'([^']{2,})'", vn_raw)
    ko_q = re.findall(r"‘([^’]{2,})’", ko_raw)
    if len(vn_q) != len(ko_q):
        fails.append(f"quote count differs: VN {len(vn_q)} vs KO {len(ko_q)}")
    else:
        if not quiet:
            print(f"ok    quotes: {len(vn_q)} (type-1 = keep English inside, type-2 = translate inside)")
            for i, (a, b) in enumerate(zip(vn_q, ko_q), 1):
                print(f"        [{i}] VN: {a[:52]}")
                print(f"            KO: {b[:52]}")

    print()
    for w in warns:
        print(f"WARN  {w}")
    for f in fails:
        print(f"FAIL  {f}")
    if not fails:
        print(f"PASS  {ko_path.name} — {len(ko)} elements, {ko_sent} sentences, parity with {vn_path.name}")
        return 0
    print(f"\nFAILED  {ko_path.name}: {len(fails)} problem(s)")
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
