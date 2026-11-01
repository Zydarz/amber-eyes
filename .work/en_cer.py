"""CER cho ban TIENG ANH (Higgs AE_LANG=en) — cung giao dien voi `vi_cer.py`.

Q3a: chuan hoa CA HAI VE. Loi doc EN giu chu so ("July 2009", "46 years old") con ASR
co the tra chu ("forty-six") hoac so => doi so -> chu tieng Anh o ca 2 ve.
Nam (1100-2099) doc theo kieu nam: 2009 -> "two thousand nine", 1990 -> "nineteen ninety".

  cer_pair(ref, hyp)        CER chinh thuc
  cer_pair_nonum(ref, hyp)  bo tu so (tach loi doc so)
  cer_pair_prop(ref, hyp)   bo danh tu rieng (tach loi ASR nghe ten)
"""
import re
import unicodedata

from voice_audition import cer, norm  # noqa: F401  (norm dung chung voi vi_cer)

_ONES = ("zero one two three four five six seven eight nine ten eleven twelve thirteen "
         "fourteen fifteen sixteen seventeen eighteen nineteen").split()
_TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def _lt1000(n):
    out = []
    if n >= 100:
        out += [_ONES[n // 100], "hundred"]
        n %= 100
        if n:
            out.append("and")
    if n >= 20:
        out.append(_TENS[n // 10] + ("" if n % 10 == 0 else " " + _ONES[n % 10]))
    elif n or not out:
        out.append(_ONES[n])
    return " ".join(out)


def en_number(n):
    if n == 0:
        return "zero"
    parts = []
    for val, name in ((10 ** 9, "billion"), (10 ** 6, "million"), (1000, "thousand")):
        if n >= val:
            parts.append(_lt1000(n // val) + " " + name)
            n %= val
    if n:
        parts.append(_lt1000(n))
    return " ".join(parts)


def en_year(n):
    if 2000 <= n <= 2009:
        return en_number(n)
    hi, lo = divmod(n, 100)
    if lo == 0:
        return _lt1000(hi) + " hundred"
    return _lt1000(hi) + " " + ("oh " + _ONES[lo] if lo < 10 else _lt1000(lo))


def en_numbers(text):
    # nam truoc (so 4 chu so khong dau phay), roi moi bo dau phay hang nghin: "1,400" khong phai nam
    text = re.sub(r"(?<![\d,])\b(1[1-9]\d\d|20\d\d)\b(?!,\d)", lambda m: en_year(int(m.group(1))), text)
    text = re.sub(r"(\d),(\d{3})", r"\1\2", text)                    # 1,400 -> 1400
    return re.sub(r"\d+", lambda m: en_number(int(m.group(0))), text)


def clean(t):
    """Bo the Higgs <|…|>, the MiniMax <#…#>, dau nhay cong, gach noi."""
    t = re.sub(r"<\|[^|]*\|>", " ", t or "")
    t = re.sub(r"<#.*?#>", " ", t)
    t = unicodedata.normalize("NFC", t)
    t = t.replace("’", "'").replace("‘", "'").replace("“", " ").replace("”", " ")
    t = re.sub(r"[-–—]", " ", t)
    t = re.sub(r"'s\b", "s", t)                                        # Williams's / Williams' -> williamss
    return t.replace("'", "")


def canon(t):
    t = re.sub(r"\bthe second\b", "ii", t)                             # "Elizabeth the Second" == "Elizabeth II"
    return t.replace(" and ", " ")                                      # "one hundred and five" == "one hundred five"


def norm_ref(t):
    return canon(norm(en_numbers(clean(t))))


def norm_hyp(h):
    return canon(norm(en_numbers(clean(h))))


def cer_pair(ref_raw, hyp_raw):
    return cer(norm_ref(ref_raw), norm_hyp(hyp_raw))


_NUM_WORDS = set((" ".join(_ONES) + " " + " ".join(_TENS[2:]) +
                  " hundred thousand million billion oh and").split())


def strip_numbers(norm_text):
    return " ".join(t for t in norm_text.split() if t not in _NUM_WORDS and not t.isdigit())


def cer_pair_nonum(ref_raw, hyp_raw):
    a, b = strip_numbers(norm_ref(ref_raw)), strip_numbers(norm_hyp(hyp_raw))
    return cer(a, b) if a else 0.0


def strip_proper(raw):
    """Bo danh tu rieng (token viet hoa giua cau); giu token dau cau va 'I'."""
    out, first = [], True
    for tok in clean(raw or "").split():
        core = tok.strip(".,;:!?\"()[]")
        if not core:
            out.append(tok)
            continue
        if core[0].isupper() and not first and core != "I":
            continue
        out.append(tok)
        first = tok[-1] in ".!?:"
    return " ".join(out)


def cer_pair_prop(ref_raw, hyp_raw):
    a = canon(norm(en_numbers(strip_proper(ref_raw))))
    b = canon(norm(en_numbers(strip_proper(hyp_raw))))
    return cer(a, b) if a else 0.0


def selfcheck():
    cases = [("July 2009.", "July two thousand nine."),
             ("At 46 years old,", "At forty-six years old"),
             ("Queen Elizabeth the Second", "Queen Elizabeth II"),
             ("Williams’s own boots", "Williams's own boots"),
             ("in 1990 and 1,400 people", "in nineteen ninety and one thousand four hundred people")]
    bad = [(a, b, cer_pair(a, b)) for a, b in cases if cer_pair(a, b) > 0]
    for a, b, c in bad:
        print("SAI:", a, "|", b, "|", norm_ref(a), "|", norm_hyp(b), c)
    print("en_cer selfcheck:", "OK" if not bad else "%d loi" % len(bad))
    return not bad


if __name__ == "__main__":
    selfcheck()
