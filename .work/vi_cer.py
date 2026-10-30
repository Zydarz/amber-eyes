"""Chuan hoa 2 ve de tinh CER — DUNG CHUNG cho moi script do CER.

BA LY DO PHAI CO MODULE RIENG:
1. **Q3(a)** — `tts_sentences.py:105` gui "so -> chu" cho TTS, ASR tra "so".
   => phai chuan hoa **CA HAI VE** bang **DUNG `vi_number()` cua pipeline**.
2. `vi_number()` o pipeline them tien to "le" (101 -> "mot tram le mot").
   Dung ban khac se lech o cac so hang tram+1..9 => CER phong to gia.
3. Bien the cach doc so (mot/mot, tu/bon, lam/nam, linh/nghin) can canonical hoa.

`vi_number`/`vi_numbers` o day **copy nguyen ban** tu `.work/tts_sentences.py`.
`selfcheck()` tu so sanh voi file pipeline that (import that) va bao loi neu lech.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent        # .work/
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from voice_audition import cer, norm  # noqa: E402

# ------------------------------------------------------------------ copy tu tts_sentences.py
_DG = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]


def _vi_lt100(n, full):
    """0–99. full=True: đứng sau hàng trăm nên số < 10 đọc kèm 'lẻ'."""
    if n < 10:
        return ("lẻ " if full else "") + _DG[n] if (n or not full) else ""
    t, u = divmod(n, 10)
    s = "mười" if t == 1 else _DG[t] + " mươi"
    if u == 0:
        return s
    if u == 5:
        return s + " lăm"
    if u == 1 and t > 1:
        return s + " mốt"
    if u == 4 and t > 1:
        return s + " tư"
    return s + " " + _DG[u]


def _vi_lt1000(n, full):
    h, r = divmod(n, 100)
    if h == 0 and not full:
        return _vi_lt100(r, False)
    s = _DG[h] + " trăm"
    return s + (" " + _vi_lt100(r, True) if r else "")


def vi_number(n):
    if n == 0:
        return "không"
    parts, units = [], ["", " nghìn", " triệu", " tỷ"]
    groups = []
    while n:
        n, g = divmod(n, 1000)
        groups.append(g)
    for i in range(len(groups) - 1, -1, -1):
        g = groups[i]
        if g == 0:
            continue
        lead = i == len(groups) - 1
        parts.append(_vi_lt1000(g, not lead) + units[i])
    return " ".join(parts)


ROMAN = {"II": "Đệ nhị", "III": "Đệ tam", "IV": "Đệ tứ"}


def vi_numbers(text):
    """Đổi chữ số trong lời đọc sang chữ; dấu chấm giữa nhóm 3 số là dấu nghìn."""
    tags = []

    def keep(m):
        tags.append(m.group(0))
        return "@@%d@@" % (len(tags) - 1)

    text = re.sub(r"<#[\d.]+#>", keep, text)
    text = re.sub(r"\b(Elizabeth|Charles|John Paul|Henry)\s+(II|III|IV)\b",
                  lambda m: f"{m.group(1)} {ROMAN[m.group(2)]}", text)
    text = re.sub(r"\d{1,3}(?:\.\d{3})+(?!\d)",
                  lambda m: vi_number(int(m.group(0).replace(".", ""))), text)
    text = re.sub(r"(?<!@)\d+(?!@)", lambda m: vi_number(int(m.group(0))), text)
    return re.sub(r"@@(\d+)@@", lambda m: tags[int(m.group(1))], text)


# ------------------------------------------------------------------ bien the cach doc so
_VARIANT = [(" mốt", " một"), (" tư", " bốn"), (" lăm", " năm"),
            (" linh", " nghìn"), (" ngàn", " nghìn")]


def canon(t):
    for a, b in _VARIANT:
        t = t.replace(a, b)
    return t


def clean(t):
    """Bỏ thẻ Higgs <|…|>, thẻ MiniMax <#…#>, và dấu nháy."""
    t = re.sub(r"<\|[^|]*\|>", " ", t or "")
    t = re.sub(r"<#.*?#>", " ", t)
    t = t.replace("\u201c", " ").replace("\u201d", " ")
    return t


def norm_ref(t):
    """Chuẩn hóa vế THAM CHIẾU (văn bản gửi đi, đã số→chữ sẵn)."""
    return norm(canon(vi_numbers(clean(t))))


def norm_hyp(h):
    """Chuẩn hóa vế BẢN CHÉP (ASR có thể trả số)."""
    return norm(canon(vi_numbers(clean(h))))


def cer_pair(ref_raw, hyp_raw):
    """CER chuẩn hóa 2 vế — đây là con số phải dùng để kết luận."""
    return cer(norm_ref(ref_raw), norm_hyp(hyp_raw))


# ------------------------------------------------------------------ metric phu: bo so
_NUM_WORDS = set("""
không một hai ba bốn năm sáu bảy tám chín mười mươi lẻ trăm nghìn ngàn linh
triệu tỷ mốt tư lăm không
""".split())


def strip_numbers(norm_text):
    """Bỏ mọi từ số + chữ số khỏi text đã norm — dùng cho metric phụ."""
    toks = [t for t in norm_text.split() if t not in _NUM_WORDS and not t.isdigit()]
    return " ".join(toks)


def cer_pair_nonum(ref_raw, hyp_raw):
    """CER bỏ số 2 vế — metric phụ để tách lỗi đọc số khỏi lỗi đọc chữ."""
    a = strip_numbers(norm_ref(ref_raw))
    b = strip_numbers(norm_hyp(hyp_raw))
    if not a:
        return 0.0
    return cer(a, b)


# ------------------------------------------------------------------ metric phu: bo danh tu rieng
def strip_proper(raw):
    """Bỏ danh từ riêng (token viết hoa giữa câu) khỏi text thô.

    Lý do: ASR đọc sai tên riêng ("Tweed" -> "Thuyết", "Russell" -> "Rosso") là lỗi
    của ASR chứ không phải của TTS. Bỏ chúng ra khỏi cả 2 vế để metric chỉ đo lỗi
    phát âm nội dung. Token đầu câu KHÔNG bỏ (tiếng Việt viết hoa đầu câu).
    """
    t = clean(raw or "")
    out, first_of_sent = [], True
    for tok in t.split():
        core = tok.strip(".,;:!?\"“”()[]")
        if not core:
            out.append(tok)
            continue
        is_cap = core[0].isupper()
        ends_sent = bool(tok and tok[-1] in ".!?…")
        if is_cap and not first_of_sent:
            continue                     # danh tu rieng -> bo
        out.append(tok)
        first_of_sent = ends_sent
    return " ".join(out)


def cer_pair_prop(ref_raw, hyp_raw):
    """CER bỏ danh từ riêng 2 vế — metric phụ để đo lỗi phát âm nội dung."""
    a = norm(canon(vi_numbers(strip_proper(ref_raw))))
    b = norm(canon(vi_numbers(strip_proper(hyp_raw))))
    if not a:
        return 0.0
    return cer(a, b)


# ------------------------------------------------------------------ selfcheck
def selfcheck(verbose=True):
    """So sanh `vi_number`/`vi_numbers` voi ban trong .work/tts_sentences.py."""
    import importlib.util
    p = HERE / "tts_sentences.py"
    if not p.exists():
        if verbose:
            print("selfcheck: khong tim thay tts_sentences.py -> BO QUA")
        return True
    spec = importlib.util.spec_from_file_location("_tts_sentences_ref", p)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        if verbose:
            print("selfcheck: khong import duoc tts_sentences.py (%s) -> BO QUA" % e)
        return True
    bad = []
    for n in [0, 1, 5, 9, 10, 11, 15, 21, 25, 100, 101, 105, 110, 115, 200, 999,
              1000, 1001, 1005, 1010, 2009, 1400, 10000, 100000, 123456, 1000000]:
        a, b = vi_number(n), mod.vi_number(n)
        if a != b:
            bad.append(("vi_number", n, a, b))
    for s in ["năm 2009", "1.400 người", "101 người", "tháng bảy 2009",
              "2.05", "<#0.45#> đợi 3 giây", "John Paul II"]:
        a, b = vi_numbers(s), mod.vi_numbers(s)
        if a != b:
            bad.append(("vi_numbers", s, a, b))
    if verbose:
        if bad:
            print("selfcheck: %d KHAC BIET — phai sua module nay!" % len(bad))
            for x in bad[:10]:
                print("   ", x)
        else:
            print("selfcheck: OK — giong het voi tts_sentences.py")
    return not bad


if __name__ == "__main__":
    ok = selfcheck()
    print()
    print("vi_number: 2009 ->", vi_number(2009))
    print("vi_number: 101  ->", vi_number(101))
    print("vi_numbers('năm 2009') ->", vi_numbers("năm 2009"))
    print("cer_pair('năm 2009', 'năm 2009') ->", cer_pair("năm 2009", "năm 2009"))
    print("cer_pair('tháng bảy năm 2009', 'tháng bảy năm 2009') ->",
          cer_pair("tháng bảy năm 2009", "tháng bảy năm 2009"))
    sys.exit(0 if ok else 1)
