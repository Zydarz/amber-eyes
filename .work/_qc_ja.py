#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""_qc_ja.py — kiểm tra 29 bản kịch bản tiếng Nhật.

    py -3 .work/_qc_ja.py            # tất cả
    py -3 .work/_qc_ja.py 01 05      # vài tập

Kiểm tra:
    1. cấu trúc: số hồi, cue, nghỉ, vai, bảng, dòng — khớp file VN
    2. câu: parse JA bằng chính parse_kichban => số lượt và số câu phải khớp file VN
    3. sót tiếng Việt (ký tự Latin Mở rộng B / thanh điệu VN)
    4. chữ Hán giản thạch Trung Quốc lọt vào
    5. tên riêng quan trọng có còn trong bản JA
    6. thuật ngữ trong glossary đã dùng đúng chưa
    7. từ cấm (YouTube Safe)
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import parse_kichban as PK  # noqa: E402
import make_ja_scripts as M  # noqa: E402
from ja_glossary import TERMS  # noqa: E402
from ja_token import norm_token, token_set, foreign_scripts  # noqa: E402
from make_ja_scripts import ALLOW_LATIN, LOAN_WORDS, _norm_key  # noqa: E402

# token Latin hợp lệ (viết tắt, mượn từ Anh) -> KHÔNG phải rác
OK_LATIN = {norm_token(x) for x in (set(ALLOW_LATIN) | set(LOAN_WORDS)) if x}

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "01_KICH_BAN"
OUT = Path(__file__).parent / "_ja_qc.txt"

# ký tự chỉ có trong tiếng Việt (Latin Extended Additional U+1E00-U+1EFF) + ăâđêôơư
VN_CHARS = set("ăâđêôơưĂÂĐÊÔƠƯ")
# chữ giản thạch Trung Quốc KHÔNG dùng trong tiếng Nhật.
# Đã loại các chữ Nhật hợp lệ: 点・断・童・声・実・両・図・圧・効・気・検・対・発・国・学・医
SIMPLIFIED = set("罗爱这时说对为后发经过们认识记访许论译调课谁让边远连运达进选适"
                 "钟镇银钱铁错闻队阴阵际难离稳穷灵显惊术极权杀伤药检变儿军农"
                 "产业务员单厂历压厌厉卖齐齿龄龙买卖头鸟亿仅从众优伤价")
# Từ cấm, dịch từ FORBIDDEN của .work/_qc_tap02_shots.py (chuẩn YouTube Safe).
# LƯU Ý: danh sách này áp cho CHỮ TRÊN HÌNH (shot plan), không áp cho lời dẫn.
# Lời dẫn bản VN vốn đã chứa các từ này => bản JA dịch tương ứng là ĐÚNG.
# Vì vậy chỉ báo lỗi khi bản JA có từ cấm mà bản VN KHÔNG có.
# (ja_word, từ tương đương trong bản VN, cụm được phép ngoại lệ)
BANNED_JA = [
    ("死体", "thi thể", ()),                    # thi thể
    ("殺害", "sát hại", ()),                    # sát hại
    ("絞首", "treo cổ", ()),                    # (không có trong VN)
    ("首吊り", "treo cổ", ()),
    ("斬首", "chém đầu", ()),
    ("首斬り", "chém đầu", ()),
    ("性関係", "quan hệ tình dục", ()),          # quan hệ tình dục
    ("強姦", "hiếp", ()),                       # hiếp
    ("強制", "cưỡng ép", ("強制力",)),           # cưỡng ép (trừ 強制力)
    ("拷問", "tra tấn", ()),                    # tra tấn
    ("頭部に毒", "đầu độc", ()),                 # đầu độc
    ("大量殺人", "diệt cỏ", ()),                 # diệt cỏ
    ("大量死", "diệt cỏ", ()),
    ("餓死", "bỏ đói", ()),                     # bỏ đói
    ("窃盗", "móc áo", ()),                     # móc áo
    ("下着", "đồ lót", ()),                     # đồ lót
    ("血", "máu", ("血液がん", "血液型", "血圧", "血管", "血球", "血糖", "血症",
                   "血漿", "輸血", "血種", "白血球", "赤血球", "血色素", "血中")),
]
SAFE_JA = {"血液がん", "血液型", "血圧", "血管", "血球", "血糖", "血症", "血漿",
           "輸血", "血種", "白血球", "赤血球", "血色素", "血中", "強制力"}
# "了" dùng như trợ động từ Trung Quốc — loại trừ 終了・修了・満了・処理・了解・為了
RE_CN_LE = re.compile(r"(?<![終修満処处处理解為为])了[。、，」』）)]")


# Latin + chữ Latin Mở rộng (tiếng Việt): "Dương" là MỘT token
RE_LATIN_QC = re.compile(r"[A-Za-zÀ-ỹĐđ]{2,}")
RE_VN_WORD_QC = re.compile(r"[A-Za-zÀ-ỹĐđĂÂĐÊÔƠƯăâđêôơư]{2,}")


def vn_leftovers(text, vn_text=""):
    """Dấu tiếng Việt sót lại.

    Cho phép nếu nằm trong một từ CÓ TRONG bản gốc (VD tên riêng "Dương", "Tiến")
    và không viết HOA; chữ IN HOA (VD "CƠ CHẾ TẨY NÃO") vẫn bị báo.
    """
    allow_vn = {_norm_key(w) for w in re.findall(r"[0-9A-Za-zÀ-ỹĐđ]+", vn_text or "")}
    bad = []
    for m in RE_VN_WORD_QC.finditer(text):
        w = m.group(0)
        dias = sorted({c for c in w
                       if c in VN_CHARS or "1E00" <= f"{ord(c):04X}" <= "1EFF"})
        if not dias:
            continue
        if not w.isupper() and _norm_key(w) in allow_vn:
            continue
        bad.extend(dias)
    return bad


def sim_chars(text):
    return [c for c in text if c in SIMPLIFIED]


def shape_count(path):
    """Đếm cấu trúc theo NHÓM (không phụ thuộc ngôn ngữ: HỒI/ACT/막/第 đều là H2)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    c = {"H1": 0, "H2": 0, "CUE": 0, "PAUSE": 0, "ROLE": 0, "TABLE": 0, "TEXT": 0,
         "BULLET": 0, "LINE": 0}
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("<!--"):
            continue
        # dòng provenance do bản dịch thêm vào (giống bản EN/KO) -> không tính
        if s.startswith(("**原文:**", "**Translated from:**", "**事実・法務チェック:**",
                         "**Fact and legal review:**", "**원본:**", "**사실 및 법률 검토:**")):
            continue
        c["LINE"] += 1
        if s.startswith("## "):
            c["H2"] += 1
        elif s.startswith("# "):
            c["H1"] += 1
        elif re.match(r"^\*\*\[(SFX|BGM)\]:\*\*", s):
            c["CUE"] += 1
        elif re.match(r"^\*\*\[(Nghỉ|Pause|정지|休止)", s):
            c["PAUSE"] += 1
        elif re.match(r"^\*\*[^*]+\*\*", s):
            c["ROLE"] += 1
        elif s.startswith("|"):
            c["TABLE"] += 1
        elif re.match(r"^(\*\s+|\d+\.\s+)", s):
            c["BULLET"] += 1
        else:
            c["TEXT"] += 1
    return c


def latin_junk(ja_body: str, vn_text: str):
    """Latin lẫn trong tiếng Nhật mà KHÔNG có trong file VN => rác do model.

    BGM / FDIA / FBI / DSM-5-TR... là viết tắt có thật trong file VN => không báo.
    """
    ok = token_set(vn_text)
    vn_latin = set(ok)
    allow_vn = {_norm_key(x) for x in ok}
    found = []
    for w in RE_LATIN_QC.findall(ja_body):
        low = norm_token(w)
        if not low or low in ok or low in OK_LATIN:
            continue
        if _norm_key(w) in allow_vn:
            continue
        if re.search(r"[a-z][A-Z]", w):
            found.append(w)
            continue
        if len(w) <= 3 and not w.isupper():
            found.append(w)
            continue
        if len(w) >= 4 and any(low in v and low != v for v in vn_latin):
            found.append(w)
            continue
    return sorted(set(found))


def names_of(vn_text):
    """Tên riêng viết HOA trong bản VN (ít nhất 2 chữ) -> danh sách kiểm tra."""
    out = set()
    for m in re.finditer(r"\b([A-Z][A-Za-z'’.-]+(?:\s+[A-Z][A-Za-z'’.-]+)+)\b", vn_text):
        w = m.group(1)
        if len(w) > 6 and w.upper() != w and not w.startswith("The "):
            out.add(w)
    return out


# từ nối tiếng Việt hay đứng đầu câu -> "Khi Conrad" KHÔNG phải tên riêng
VN_CONNECT = {"Khi", "Nhưng", "Sau", "Trong", "Với", "Từ", "Tại", "Như", "Còn",
              "Đó", "Đây", "Về", "Theo", "Sau", "Trước", "Bởi", "Nếu", "Khi",
              "Một", "Chúng", "Anh", "Bà", "Ông", "Cô", "Chị", "Em", "Tôi",
              "Rồi", "Vẫn", "Chỉ", "Cùng", "Các", "Những", "Đã", "Đang", "Sẽ",
              "Phải", "Muốn", "Có", "Không", "Đến", "Ra", "Vào", "Qua", "Bởi"}
# tiền tố/hậu tố địa danh
GEO_WORD = {"port", "san", "new", "st", "saint", "lake", "mount", "fort", "cape",
            "bay", "north", "south", "east", "west", "little", "great", "upper",
            "lower", "island", "county", "city", "state", "town", "township",
            "district", "valley", "river", "beach", "park", "hills", "heights",
            "springs", "junction", "crossing", "creek", "falls", "point"}
US_STATES = {"Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
             "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
             "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
             "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
             "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
             "New Hampshire", "New Jersey", "New Mexico", "New York",
             "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
             "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
             "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
             "West Virginia", "Wisconsin", "Wyoming"}
GEO_CONTEXT = ("tỉnh", "bang", "huyện", "quận", "thành phố", "thị xã", "hành",
               "County", "State", "City", "Township", "District", "Province",
               "thuộc", "vùng", "khu vực")


def is_geographic(name: str, vn_text: str) -> bool:
    """Tên địa danh được phép dịch sang Katakana => không báo mất tên."""
    if name in US_STATES:
        return True
    words = [w.lower().strip(".,") for w in name.split()]
    if any(w in GEO_WORD for w in words):
        return True
    i = vn_text.find(name)
    if i >= 0:
        ctx = vn_text[max(0, i - 30):i + len(name) + 60]
        if any(g in ctx for g in GEO_CONTEXT):
            return True
    return False


def _num_value(s):
    """Giá trị của một chuỗi số (1.600 -> 1600.0 ; 0,13 -> 0.13)."""
    t = s.replace(".", "").replace(",", ".")
    try:
        return float(t)
    except ValueError:
        return None


def numbers_in(text):
    """Các con số trong văn bản (năm, số lượng) — dùng để đối chiếu VN vs JA."""
    out = set()
    for m in re.finditer(r"\d[\d.,]*", text):
        s = m.group(0).rstrip(".,")
        if s:
            out.add(s)
    return out


def number_mismatch(ja_text, vn_text):
    """Số nào lệch giá trị giữa VN và JA (theo GIÁ TRỊ, bỏ khác biệt định dạng).

    KHÔNG dùng làm điều kiện đạt: bản VN hay viết số bằng chữ ("mười tám tháng")
    và JA viết thành 18か月 — đúng và đẹp hơn.
    """
    jn = {_num_value(s) for s in numbers_in(ja_text)} - {None}
    vn_n = {_num_value(s) for s in numbers_in(vn_text)} - {None}
    only_vn = sorted(vn_n - jn)
    only_ja = sorted(jn - vn_n)
    return only_vn, only_ja


def unconverted_numbers(ja_text, vn_text):
    """Số theo quy ước VN (1.600 / 0,13) còn sót trong bản JA -> LỖI thật."""
    bad = []
    for s in numbers_in(ja_text):
        if (re.fullmatch(r"\d{1,3}(?:\.\d{3})+", s) or re.fullmatch(r"\d+,\d+", s)):
            if s in numbers_in(vn_text):
                bad.append(s)
    return sorted(set(bad))


def main():
    eps = sys.argv[1:] or [f"{i:02d}" for i in range(1, 30)]
    rep, all_bad = [], 0
    for ep in eps:
        vn = M.canonical_vn(ep)
        ja = KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
        if not ja.exists():
            rep.append(f"Tap{ep}: CHƯA CÓ file JA")
            all_bad += 1
            continue
        vn_els = PK.parse_file(vn)
        ja_els = PK.parse_file(ja)
        vn_loi = [e for e in vn_els if e["kind"] == "LOI"]
        ja_loi = [e for e in ja_els if e["kind"] == "LOI"]
        vn_sent = sum(len(e["sentences"]) for e in vn_loi)
        ja_sent = sum(len(e["sentences"]) for e in ja_loi)

        c_vn, c_ja = shape_count(vn), shape_count(ja)
        diff = {k: (c_vn.get(k, 0), c_ja.get(k, 0)) for k in c_vn
                if c_vn.get(k, 0) != c_ja.get(k, 0)}

        ja_text = ja.read_text(encoding="utf-8")
        ja_body = re.sub(r"<!--.*?-->", "", ja_text, flags=re.S)
        vn_text = vn.read_text(encoding="utf-8")
        vn_bad = vn_leftovers(ja_body, vn_text)
        sim = sim_chars(ja_body)
        banned = []
        banned_new = []
        for w, vn_src, safe in BANNED_JA:
            probe = ja_body
            for s in safe:                 # bỏ cụm được phép trước, rồi mới tìm từ cấm
                probe = probe.replace(s, "")
            if w not in probe:
                continue
            # Danh sách cấm áp cho CHỮ TRÊN HÌNH (shot plan), không áp lời dẫn.
            # Lời dẫn bản VN vốn đã chứa khái niệm này => JA dịch tương ứng là đúng.
            banned.append(w)
            if not (vn_src and vn_src in vn_text):
                banned_new.append(w)
        # chữ Latin lạc giữa tiếng Nhật (rác do model) — chỉ báo khi KHÔNG có trong file VN
        junk = latin_junk(ja_body, vn_text)
        # ký tự Cyrillic/Greek lẫn vào => model bóp méo ký tự
        foreign = foreign_scripts(ja_body)

        # tên riêng: so các tên xuất hiện trong bản VN (>=3 lần) phải còn trong bản JA
        names = [n for n in names_of(vn_text)
                 if vn_text.count(n) >= 3 and n.split()[0] not in VN_CONNECT]
        lost = [n for n in names if n not in ja_text and not is_geographic(n, vn_text)]

        # thuật ngữ glossary: nếu VN có cụm từ thì JA phải có bản dịch cố định
        miss_terms = []
        for vi, ja_t in TERMS.items():
            if vi in vn_text and ja_t not in ja_text and len(vi) > 8:
                miss_terms.append(f"{vi} → {ja_t}")

        # so câu theo từng lượt
        turn_diff = 0
        for a, b in zip(vn_loi, ja_loi):
            if len(a["sentences"]) != len(b["sentences"]):
                turn_diff += 1

        # số liệu: quy ước số VN phải được đổi sang quy ước Nhật.
        # (khác biệt số theo GIÁ TRỊ chỉ để tham khảo: VN hay viết số bằng chữ)
        only_vn, only_ja = number_mismatch(ja_body, vn_text)
        bad_num = unconverted_numbers(ja_body, vn_text)

        # LỖI THẬT: sai cấu trúc / sót tiếng Việt / chữ Trung / số / thuật ngữ
        hard = []
        if vn_sent != ja_sent:
            hard.append(f"số câu lệch {ja_sent - vn_sent}")
        if len(vn_loi) != len(ja_loi):
            hard.append(f"số lượt lệch {len(ja_loi) - len(vn_loi)}")
        if diff:
            hard.append(f"cấu trúc lệch {diff}")
        if vn_bad:
            hard.append(f"sót tiếng Việt {''.join(sorted(set(vn_bad)))}")
        if sim:
            hard.append(f"chữ Hán giản {''.join(sorted(set(sim)))}")
        if foreign:
            hard.append(f"ký tự lạ {foreign}")
        if bad_num:
            hard.append(f"số chưa đổi quy ước {bad_num}")
        n_comma = ja_body.count("，")
        if n_comma:
            hard.append(f"dấu phẩy Trung Quốc '，' {n_comma} lần")
        cn_le = RE_CN_LE.findall(ja_body)
        if cn_le:
            hard.append(f"trợ động từ Trung Quốc '了' {len(cn_le)} lần")
        if miss_terms:
            hard.append(f"thiếu thuật ngữ {len(miss_terms)}")
        # CẢNH BÁO: cần người rà tay, không làm hỏng tập
        soft = []
        if junk:
            soft.append(f"rác Latin {junk[:4]}")
        if lost:
            soft.append(f"mất tên {lost[:5]}")
        if banned:
            soft.append(f"từ nhạy cảm {banned[:5]}")
        if banned_new:
            soft.append(f"JA tự thêm {banned_new}")
        ok = not hard
        if not ok:
            all_bad += 1
        rep.append(f"{'OK  ' if ok else 'LỖI'} Tap{ep}: câu VN={vn_sent} JA={ja_sent} | "
                   f"lượt VN={len(vn_loi)} JA={len(ja_loi)} | lượt lệch câu={turn_diff} | "
                   + (f"LỖI: {'; '.join(hard)}" if hard else "lỗi: không")
                   + (" | CẢNH BÁO: " + "; ".join(soft) if soft else ""))
        if miss_terms:
            rep.append(f"      thuật ngữ chưa dùng: {miss_terms[:6]}")
        if lost:
            rep.append(f"      tên riêng không thấy trong JA: {lost[:8]}")
    OUT.write_text("\n".join(rep), encoding="utf-8")
    print("\n".join(rep))
    print(f"\n==> {29 - all_bad if len(eps) == 29 else len(eps) - all_bad}/{len(eps)} tập đạt · -> {OUT}")


if __name__ == "__main__":
    main()
