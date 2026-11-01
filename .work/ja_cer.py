"""CER cho ban TIENG NHAT (Higgs AE_LANG=ja) — cung giao dien voi `vi_cer.py` / `en_cer.py`.

Q3a: chuan hoa CA HAI VE. Tieng Nhat co them loi CHINH TA cua ASR (kana<->kanji:
すべて/全て, とき/時, 辿る/たどる — BaoCao_DoGiongMau_JA3_KO3_20261101) => so tren
CACH DOC: chu so -> so kanji (2009 -> 二千九), roi pykakasi -> hiragana o ca 2 ve.
CER tinh tren ky tu hiragana (khong co khoang trang).

  cer_pair(ref, hyp)        CER chinh thuc
  cer_pair_nonum(ref, hyp)  bo chu so/so kanji (tach loi doc so)
  cer_pair_prop(ref, hyp)   bo chu Latin + katakana (ten rieng — loi ASR nghe ten)
"""
import re
import unicodedata

import pykakasi

from voice_audition import cer  # noqa: F401

_K = pykakasi.kakasi()
_D = "〇一二三四五六七八九"


def _lt10000(n):
    out = ""
    for val, ch in ((1000, "千"), (100, "百"), (10, "十")):
        q, n = divmod(n, val)
        if q:
            out += ("" if q == 1 else _D[q]) + ch
    return out + (_D[n] if n else "")


def ja_number(n):
    if n == 0:
        return "零"
    out = ""
    for val, ch in ((10 ** 8, "億"), (10 ** 4, "万")):
        q, n = divmod(n, val)
        if q:
            out += _lt10000(q) + ch
    return out + _lt10000(n)


def ja_numbers(text):
    """Chu so (ca so toan goc ２０) -> so kanji; bo dau phay ngan cach nghin."""
    t = unicodedata.normalize("NFKC", text or "")
    return re.sub(r"\d+(?:,\d{3})*", lambda m: ja_number(int(m.group(0).replace(",", ""))), t)


def clean(t):
    """Bo the Higgs <|…|>, the MiniMax <#…#>."""
    t = re.sub(r"<\|[^|]*\|>", " ", t or "")
    return re.sub(r"<#.*?#>", " ", t)


def _hira(t):
    return "".join(x["hira"] for x in _K.convert(t))


def _norm(t):
    t = _hira(ja_numbers(clean(t))).lower()
    return "".join(ch for ch in t if unicodedata.category(ch)[0] in "LN")


def norm_ref(t):
    return _norm(t)


def norm_hyp(h):
    return _norm(h)


def cer_pair(ref_raw, hyp_raw):
    """CER chuan hoa 2 ve — con so phai dung de ket luan."""
    return cer(norm_ref(ref_raw), norm_hyp(hyp_raw))


_RE_NUM = re.compile(r"[\d〇一二三四五六七八九十百千万億零]+")


def cer_pair_nonum(ref_raw, hyp_raw):
    """CER bo so 2 ve — metric phu."""
    a = _norm(_RE_NUM.sub(" ", ja_numbers(clean(ref_raw))))
    b = _norm(_RE_NUM.sub(" ", ja_numbers(clean(hyp_raw))))
    return cer(a, b) if a else 0.0


_RE_PROPER = re.compile(r"[A-Za-z][A-Za-z.'\- ]*|[゠-ヿ＝・]+")


def strip_proper(raw):
    return _RE_PROPER.sub(" ", unicodedata.normalize("NFKC", clean(raw or "")))


def cer_pair_prop(ref_raw, hyp_raw):
    """CER bo chu Latin + katakana 2 ve — metric phu (ten rieng)."""
    a = _norm(strip_proper(ref_raw))
    b = _norm(strip_proper(hyp_raw))
    return cer(a, b) if a else 0.0


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for n in (7, 10, 27, 46, 82, 437, 1000, 2009, 2010, 12000):
        print(n, ja_number(n))
    r = "すべての事件は、2009年7月に始まります。"
    print(cer_pair(r, "全ての事件は二千九年七月に始まります"), cer_pair(r, "全ての事件は2009年7月に始まります"))
