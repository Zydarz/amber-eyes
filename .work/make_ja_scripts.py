#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""make_ja_scripts.py — dựng bản kịch bản tiếng Nhật cho AMBER EYES.

    py -3 .work/make_ja_scripts.py --ep 01 --workers 8
    py -3 .work/make_ja_scripts.py --all --workers 8

Cách hoạt động:
    1. đọc kịch bản VN chuẩn (file mới nhất trong 01_KICH_BAN/TapXX, bỏ _ban_goc/_truoc_review/_EN)
    2. tách từng dòng thành "unit" (h1/h2/act/table/cue/pause/role/direction/dialogue)
    3. dịch theo TỪNG CÂU: 1 câu VN -> 1 câu JA (mã câu của bản diễn xuất được giữ nguyên)
    4. kiểm tra tự động: số câu, dấu **/*, sót tiếng Việt, lỡ tiếng Trung, rác Latin
    5. ghi 01_KICH_BAN/TapXX_JA/kichban_tapXX_JA.md + báo cáo QC
"""
import argparse
import json
import re
import sys
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ja_llm  # noqa: E402
from ja_glossary import TERMS, ROLES_JA  # noqa: E402
from ja_token import norm_token, token_set, foreign_scripts  # noqa: E402
from ja_split import (split_dialogue_sentences, move_trailing_markers,  # noqa: E402
                      parts_balanced, ja_sentences, ja_split)

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "01_KICH_BAN"
WORK = ROOT / ".work"
CACHE_DIR = WORK / "ja_cache"
REPORT = WORK / "ja_report"
MODEL = "MiniMax-M3.1-Flash"
CACHE_VERSION = 3

VN_ROLE_KEYS = set(ROLES_JA)

# ------------------------------------------------------------------ regex
RE_H1 = re.compile(r"^#\s+(.*)$")
RE_H2 = re.compile(r"^##\s+(.*)$")
RE_H3 = re.compile(r"^###\s+(.*)$")
RE_ROLE = re.compile(r"^\*\*([^*]+)\*\*\s*(?:\*\((.*?)\)\*)?\s*:\s*(.*)$")
RE_CUE = re.compile(r"^\*\*\[(SFX|BGM)\]:\*\*\s*(.*)$")
RE_PAUSE = re.compile(r"^\*\*\[(?:Nghỉ|Pause)(.*?)\]\*\*\s*(.*)$")
RE_BULLET = re.compile(r"^(\*\s+|\d+\.\s+)(.*)$")
RE_TABLE = re.compile(r"^\s*\|(.*)\|\s*$")
RE_LABELED = re.compile(r"^\*\*[^*]{1,40}\*\*\s+\S")
RE_ACT = re.compile(r"^HỒI\s*(\d+)\s*[:：]\s*(.*)$")
RE_RANGE = re.compile(r"(\([^()]*\)|（[^（）]*）)\s*$")
# mốc thời gian kiểu (10:00 – 16:30) — phần này GIỮ NGUYÊN (không dịch)
RE_TIME_RANGE = re.compile(r"\d{1,2}\s*[:：]\s*\d{2}")

# đúng luật tách câu của .work/parse_kichban.py (bản tiếng Việt/Anh)
OFFICIAL_SPLIT = re.compile(r'(?:(?<=[.?!…])|(?<=[.?!…]”))\s+(?=[A-ZÀ-ỸĐ“(])')

# ------------------------------------------------------------------ kiểm tra chất lượng
VN_EXTRA = set("ăâđêôơưĂÂĐÊÔƠƯ")
# chữ Hán giản thạch CHỈ có trong tiếng Trung, không dùng được trong tiếng Nhật
# (đã loại các chữ vốn là kanji Nhật hợp lệ: 点 断 医 両 図 圧 効 気 検 対 発 国 学 実 声 童…)
SIMP_CHARS = set(
    "罗爱这时说对为后实发经过们认识记访许论译调课谁让边远连运达进选适"
    "钟镇银钱铁错闻队阴阵际难离稳穷灵显惊术极权杀伤药检变儿军农"
    "产业务员单厂历压厌厉卖齐齿龄龙买卖头鸟亿仅从众优伤价开关书贝"
    "么伞兽听启冈庆场侦俩俭债倾偿储兑兰兴养冲决况净准凤划刘则刚创剂剑劝办动"
    "逊违邓邮郑邻酱释锋锐锡锦键闭闷陆陈险隐韩页项顺须顾顿颂预领频颗额飘饥丽")
# từ chức năng CHỈ có trong tiếng Trung (không phải tiếng Nhật) — dấu hiệu model lỡ tiếng Trung
CN_FUNC = ("因为 所以 但是 而且 虽然 如果 然后 我们 你们 他们 她们 什么 怎么 这么 那么 "
           "这种 那种 可以 应该 关于 通过 进行 对于 以及 或者 并且 已经 正在 非常 比较 "
           "需要 认为 出现 成为 由于 同时 之间 之后 之前 的话 一下 罢了 而已 起来 下去 "
           "上来 下来 一个 一些 一直 许多 很多 每个 别人 情况 东西 状态 常见 具有")
ALLOW_LATIN = {"munchausen", "syndrome", "proxy", "signature", "infantilization",
               "learned", "helplessness", "trauma", "bonding", "disneyland", "habitat",
               "for", "humanity", "dsm", "fdia", "bpd", "aspd", "ocpd", "ptsd", "adhd",
               "fbi", "bbc", "cnn", "youtube", "tiktok", "mr", "mrs", "ms", "dr", "st",
               "ok", "dna", "rna", "pdf", "gps", "tv", "us", "uk", "usa", "ceo", "md",
               "phd", "slasher", "camp", "amazon", "google", "wikipedia", "md", "csv",
               "txt", "json", "xml", "html", "jpg", "png", "pdf", "mp3", "mp4",
               # đơn vị / viết tắt hợp lệ hay bị bộ kiểm "rác" gắn cờ nhầm
               "db", "ph", "law", "fbi", "ceo", "phd", "mba"}
# Mượn từ Anh hợp lệ trong lời dẫn tài liệu Nhật — KHÔNG phải rác.
LOAN_WORDS = {
    "hospital", "hospitals", "poison", "church", "christian", "christ", "hurricane",
    "county", "prosecutor", "prosecutors", "employee", "reporting", "act", "ethnicity",
    "phrase", "space", "creates", "create", "identify", "dissect", "smelled", "troubled",
    "sadness", "nearly", "computer", "computers", "warning", "warnings", "state",
    "states", "police", "detective", "detectives", "agent", "agents", "special",
    "bureau", "federal", "coroner", "witness", "witnesses", "jury", "court", "courts",
    "trial", "trials", "verdict", "sentence", "profile", "behavior", "behaviour",
    "analysis", "mind", "serial", "killer", "murder", "murderer", "victim", "victims",
    "detention", "testimony", "evidence", "suspect", "suspects", "search", "warrant",
    "psychiatrist", "psychologist", "pediatrician", "doctor", "doctors", "nurse",
    "nurses", "medstation", "pathology", "xray", "mri", "eeg", "newsletter",
    "investigation", "investigations", "literature", "research", "multipartite",
    "schechter", "wechsler", "mmpi", "rorschach", "tatcher", "doubles",
}
# Latin + chữ Latin Mở rộng (tiếng Việt): "Dương" phải là MỘT token, không phải "D"+"ng"
RE_LATIN = re.compile(r"[A-Za-zÀ-ỹĐđ]{2,}")
RE_WORD = re.compile(r"[0-9A-Za-zÀ-ỹ]+")
RE_CN_FUNC = re.compile("|".join(re.escape(w) for w in CN_FUNC.split()))
# "了" dùng như trợ động từ Trung Quốc (VD "提到了") — tiếng Nhật KHÔNG dùng cách này.
# Loại trừ các từ Hán hợp lệ trong tiếng Nhật: 終了・修了・満了・処理・了解・為了
RE_CN_LE = re.compile(r"(?<![終修満処处处理解為为])了[。、，」』）)]")
# một từ Latin có thể chứa dấu tiếng Việt (VD tên riêng "Dương", "Tiến")
RE_VN_WORD = re.compile(r"[A-Za-zÀ-ỹĐđĂÂĐÊÔƠƯăâđêôơư]{2,}")

# ký tự "giống hình" Latin: fullwidth + Cyrillic + Hyroglyph hay gặp trong output của model
LATIN_FIX = {}
for _i in range(26):
    LATIN_FIX[chr(0xFF21 + _i)] = chr(0x41 + _i)      # Ａ-Ｚ
    LATIN_FIX[chr(0xFF41 + _i)] = chr(0x61 + _i)      # ａ-ｚ
for _s, _d in (("А", "A"), ("В", "B"), ("Е", "E"), ("К", "K"), ("М", "M"),
               ("Н", "H"), ("О", "O"), ("Р", "P"), ("С", "C"), ("Т", "T"),
               ("Х", "X"), ("а", "a"), ("е", "e"), ("о", "o"), ("р", "p"),
               ("с", "c"), ("у", "y"), ("х", "x")):
    LATIN_FIX[_s] = _d
for _s, _d in (("Α", "A"), ("Β", "B"), ("Ε", "E"), ("Ζ", "Z"), ("Η", "H"),
               ("Ι", "I"), ("Κ", "K"), ("Μ", "M"), ("Ν", "N"), ("Ο", "O"),
               ("Ρ", "P"), ("Τ", "T"), ("Υ", "Y"), ("Χ", "X"), ("ο", "o"),
               ("α", "a"), ("ρ", "p"), ("τ", "t")):
    LATIN_FIX[_s] = _d


RE_NUM_THOU = re.compile(r"\d{1,3}(?:\.\d{3})+")   # 1.600 = 1600 (quy ước VN)
RE_NUM_DEC = re.compile(r"\d+,\d+")               # 0,13 = 0.13  (quy ước VN)


def vn_num_to_ja(s: str):
    """Đổi số theo quy ước VN (châu Âu) sang quy ước Nhật."""
    if RE_NUM_THOU.fullmatch(s):
        return s.replace(".", ",")
    if RE_NUM_DEC.fullmatch(s):
        return s.replace(",", ".")
    return None


def fix_numbers(ja: str, vi: str) -> str:
    """Sửa số mà model chép nguyên quy ước VN: 1.600 -> 1,600 · 0,13 -> 0.13.

    Không có bước này thì người Nhật đọc "1.600" là 1,6 — sai số liệu.
    """
    if not ja or not vi:
        return ja
    for m in set(RE_NUM_THOU.findall(vi)) | set(RE_NUM_DEC.findall(vi)):
        conv = vn_num_to_ja(m)
        if conv and conv != m:
            ja = re.sub(r"(?<![\d.,])" + re.escape(m) + r"(?![\d.,])", conv, ja)
    return ja


def _clean_ja(ja: str, vi: str) -> str:
    """Chuẩn hoá output của model: ký tự giống hình + quy ước số."""
    return fix_numbers(fix_latin(ja), vi)


def _table_cell(ja: str) -> str:
    """Ô bảng phải nằm trên MỘT dòng vật lý.

    Bản VN dùng <br> để tách các mục trong cùng 1 ô. Model hay trả newline
    thật -> ô bị tách thành nhiều dòng -> lệch cấu trúc so với bản VN.
    Vì vậy mọi newline trong ô bảng đều quy lại thành <br>.
    """
    if not ja:
        return ja
    return re.sub(r"\r\n|\r|\n", "<br>", ja).strip()


def fix_latin(text: str) -> str:
    """Sửa ký tự Latin 'giống hình' (fullwidth / Cyrillic / Greek) về ASCII."""
    if not text:
        return text
    return "".join(LATIN_FIX.get(c, c) for c in text)


def _norm_key(t: str) -> str:
    """Chuẩn hoá để so khớp tên riêng có/không dấu: Nguyễn -> nguyen."""
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^0-9a-z]", "", t)


def vn_tokens_of(vn_text):
    """Tập khóa chuẩn hoá của MỌI từ trong bản VN (kể cả từ có dấu)."""
    return {_norm_key(w) for w in RE_WORD.findall(vn_text or "") if len(w) >= 2}


RE_PROPER = re.compile(r"\b([A-Z][A-Za-z'’.-]{2,}(?:\s+[A-Z][A-Za-z'’.-]{2,})*)\b")


def proper_names(vi_text: str) -> list:
    """Tên riêng viết HOA trong bản VN (>=2 từ) — nên giữ nguyên trong bản JA."""
    out = []
    for m in RE_PROPER.finditer(vi_text or ""):
        w = m.group(1).strip(" .,;:'’-")
        if " " in w:
            out.append(w)
    return out


# --- nhiễm ngôn ngữ: chữ Trung giản thạch / chữ Hàn / rác Latin -------------
# Dựng từ bảng tra CN2JP (mọi khoá đều là dạng CHỈ CÓ trong tiếng Trung,
# trừ 据 — 据える là từ Nhật hợp lệ).
# LƯU Ý: 残 / 殴 là shinjitai hợp lệ của tiếng Nhật (生き残る / 殴る)
# => KHÔNG được đưa vào danh sách chữ Trung-only.
CN_ONLY_CHARS = set(
    "严乐亏仓们伟伪兽变响圆处审对导带应弃强态恶惧护样污沟现监码种级结联肃胜脏节觉议设词话语谎财质辩这针门风马驱骤鲜"
)
RX_HANGUL = re.compile(r"[\u3131-\u318e\uac00-\ud7a3]")
RX_JUNK_LATIN = re.compile(r"(?<!<)_(?=[A-Za-z])")


def contamination_flags(ja: str):
    """Nhiễm ngôn ngữ trong 1 đoạn JA -> danh sách lỗi THẬT (ép dịch lại)."""
    probs = []
    cn = sorted({c for c in ja if c in CN_ONLY_CHARS})
    if cn:
        probs.append("中国語の簡体字を使っています: " + "".join(cn)
                     + "（日本語の漢字に直してください。例: 联邦→連邦、护→護、"
                       "语→語、结→結、样→様、码→コード）")
    ko = sorted({c for c in ja if RX_HANGUL.match(c)})
    if ko:
        probs.append("韓国語（ハングル）が混ざっています: " + "".join(ko)
                     + "（日本語に翻訳し直してください）")
    if RX_JUNK_LATIN.search(ja):
        probs.append("無関係な英単語や記号が混ざっています: "
                     + " ".join(RX_JUNK_LATIN.findall(ja))
                     + "（日本語の文に翻訳し直してください）")
    return probs


def quality_flags(ja: str, vn_tokens: set, vi_text: str = "", ep_tokens: set = None):
    """Lỗi chất lượng trong một đoạn tiếng Nhật -> (hard, soft).

    hard — lỗi khiến bản dịch không dùng được, buộc phải dịch lại
    soft — đáng cảnh báo nhưng không nên ép dịch lại vô điều kiện
    """
    if not ja:
        return (["rỗng"], [])
    hard, soft = [], []
    # Dấu tiếng Việt sót lại:
    #  - nằm trong một từ Latin CÓ TRONG bản gốc (VD tên riêng "Dương", "Tiến")
    #    -> ĐÚNG, vì quy ước là giữ tên riêng ở chữ Latin gốc.
    #  - nằm ngoài từ Latin, hoặc là chữ IN HOA -> LỖI thật (VD "CƠ CHẾ TẨY NÃO").
    allow_vn = {_norm_key(x) for x in (set(vn_tokens) | set(ep_tokens or ())) if x}
    bad_vn = []
    for m in RE_VN_WORD.finditer(ja):
        w = m.group(0)
        dias = sorted({c for c in w if c in VN_EXTRA or 0x1E00 <= ord(c) <= 0x1EFF})
        if not dias:
            continue
        if not w.isupper() and _norm_key(w) in allow_vn:
            continue
        bad_vn.extend(dias)
    if bad_vn:
        hard.append("còn sót tiếng Việt: " + "".join(sorted(set(bad_vn))))
    simp = sorted({c for c in ja if c in SIMP_CHARS})
    if simp:
        hard.append("chữ Hán giản thạch: " + "".join(simp))
    cn = sorted({m.group(0) for m in RE_CN_FUNC.finditer(ja)})
    if cn:
        hard.append("lỡ dùng từ tiếng Trung: " + ", ".join(cn[:4]))
    le = RE_CN_LE.search(ja)
    if le:
        hard.append("lỡ dùng trợ động từ Trung Quốc '了': "
                    + ja[max(0, le.start() - 10):le.end()])
    foreign = foreign_scripts(ja)
    if foreign:
        hard.append("ký tự lạ script (Cyrillic/Greek): " + "".join(foreign[:4]))
    allow = {norm_token(x) for x in (set(ALLOW_LATIN) | set(LOAN_WORDS) | set(vn_tokens)
                                     | set(ep_tokens or ())) if x}
    # token Latin CÓ DẤU tiếng Việt (VD "Dương"): khớp với bản gốc khi bỏ dấu
    unknown = sorted({t for t in RE_LATIN.findall(ja)
                      if norm_token(t) not in allow and _norm_key(t) not in allow_vn})
    # Chỉ coi là RÁC (ép dịch lại) khi trông như mảnh vỡ do model bóp méo:
    #   - camelCase (MyZS) hoặc chữ hoa ở giữa từ
    #   - mảnh rất ngắn (<=3 ký tự) không có trong bản VN
    #   - là mảnh vụn của một từ Latin có trong bản VN (nchausen <- Münchausen)
    # Mượn từ Anh hợp lệ (Hospital, Hurricane...) chỉ CẢNH BÁO, không ép dịch lại.
    vn_latin = {norm_token(w) for w in RE_LATIN.findall(vi_text or "")}
    garbage = []
    for t in unknown:
        if re.search(r"[a-z][A-Z]", t):
            garbage.append(t)
            continue
        if len(t) <= 3 and not t.isupper():
            garbage.append(t)
            continue
        low = t.lower()
        if len(t) >= 4 and any(low in v and low != v for v in vn_latin):
            garbage.append(t)
            continue
    if garbage:
        hard.append("từ tiếng Anh bị bóp méo: " + ", ".join(garbage[:4]))
    elif unknown:
        soft.append("từ tiếng Anh chưa có trong bản gốc: " + ", ".join(unknown[:4]))
    if re.search(r"[A-Za-z]{2,}_[A-Za-z_]{1,}", ja):
        hard.append("có dấu gạch dưới lạ trong tiếng Nhật")
    lost = [n for n in proper_names(vi_text) if n not in ja]
    if lost:
        soft.append("mất tên riêng: " + ", ".join(lost[:4]))
    return (hard, soft)


# ------------------------------------------------------------------ đếm câu
def count_sentences_ja(text: str) -> int:
    """Đếm 。 ！ ？ … (gộp …… thành một)."""
    t = text.replace("……", "…").replace("。。", "。")
    return len(re.findall(r"[。！？…]", t))


def _norm_line(s: str) -> str:
    """Chuẩn hóa dòng y như parse_kichban.py làm trước khi tách câu."""
    t = re.sub(r"^\*\s+", "", s.strip())
    t = re.sub(r"^\d+\.\s+", "", t)
    t = t.replace("**", "").replace("*", "")
    t = t.strip().strip('"“”').strip()
    t = re.sub(r"'([^']+)'", r"“\1”", t)
    t = re.sub(r"‘(.*?)’(?![A-Za-z])", r"“\1”", t)
    return t


def official_counts(lines):
    """Số câu của từng dòng — đúng luật của parse_kichban.py."""
    counts = []
    for l in lines:
        t = _norm_line(l)
        if not t:
            counts.append(0)
            continue
        counts.append(len(re.split(OFFICIAL_SPLIT, t)))
    return counts


def group_turns(units):
    """Gom các dòng thoại thành lượt — đúng luật của parse_kichban.py.

    Luật: một lượt mới bắt đầu khi (a) đổi vai, (b) có cue/nghỉ xen giữa.
    Cue và nhịp nghỉ ĐÓNG lượt cũ nhưng vai trò vẫn giữ, nên dòng thoại sau đó thuộc
    lượt mới cùng vai đó. Ở mốc hồi (HỒI N) thì vai bị xoá.
    """
    turns, turn, role = [], [], None

    def flush():
        nonlocal turn
        if turn and role:
            turns.append({"role": role, "units": list(turn)})
        turn = []

    for u in units:
        k = u["kind"]
        if k == "ROLE":
            flush()
            role = u["vi"]
        elif k == "DIRECTION":
            continue                      # chú dẫn diễn xuất đi kèm vai, không ngắt lượt
        elif k in ("TEXT", "BULLET", "NUM", "LABELED"):
            if role is None:
                continue
            turn.append(u)
        elif k in ("CUE", "PAUSE"):
            flush()                      # đóng lượt, giữ vai
        elif k == "ACT":
            flush()
            role = None                   # mốc hồi: parser xoá vai
        # RAW / H1 / H2 / H3 / TABLE: không ảnh hưởng lượt (parser cũng bỏ qua)
    flush()
    return turns


def assign_turn_counts(units):
    """Gán số câu (theo luật parse_kichban) cho từng dòng thoại."""
    for t in group_turns(units):
        counts = official_counts([u["vi"] for u in t["units"]])
        for u, c in zip(t["units"], counts):
            u["n"] = c
    for u in units:
        u.setdefault("n", 0)
    return units


def splittable(u):
    """Tách câu cho 1 dòng thoại nếu TÁCH ĐƯỢC và giữ được marker.

    Điều kiện:
      - số câu tách ra == số câu theo luật parse_kichban (u['n'])
      - mỗi câu tự cân bằng ** và * (không mở ở câu này, đóng ở câu sau)

    Trả về list câu, hoặc None nếu phải dịch cả dòng.
    """
    if u["kind"] not in ("TEXT", "BULLET"):
        return None
    parts = split_dialogue_sentences(u["vi"])
    if not parts or len(parts) != u.get("n", 0):
        return None
    if not parts_balanced(parts):
        return None
    return parts


# ------------------------------------------------------------------ parse
def canonical_vn(tap: str) -> Path:
    name = tap if tap.startswith("Tap") else f"Tap{tap}"
    d = KB / name
    cands = [f for f in d.glob("kichban_*.md")
             if not re.search(r"(_ban_goc|_truoc_review|_EN)", f.name)]
    if not cands:
        raise SystemExit(f"Không tìm thấy kịch bản VN cho {name}")
    return max(cands, key=lambda p: p.stat().st_mtime)


def parse_units(path: Path):
    """-> list unit: dict(id, kind, vi, note, ...)"""
    lines = path.read_text(encoding="utf-8").splitlines()
    units, uid = [], 0

    def add(kind, vi, note="", **kw):
        nonlocal uid
        uid += 1
        u = {"id": f"u{uid:04d}", "kind": kind, "vi": vi, "note": note}
        u.update(kw)
        units.append(u)
        return u

    def raw(line):
        units.append({"id": f"u{uid + 1:04d}", "kind": "RAW", "raw": line, "vi": line})

    for line in lines:
        s = line.strip()
        if not s or s == "---":
            raw(line)
            continue

        m = RE_ROLE.match(s)
        if m and m.group(1).strip() in VN_ROLE_KEYS:
            role = m.group(1).strip()
            direction = (m.group(2) or "").strip()
            rest = m.group(3).strip()
            add("ROLE", role, "role name")
            if direction:
                add("DIRECTION", direction, "acting direction in parentheses")
            if rest:
                add("TEXT", rest, "dialogue")
            continue

        m = RE_H1.match(s)
        if m:
            add("H1", m.group(1).strip(), "title of the script")
            continue
        m = RE_H2.match(s)
        if m:
            t = m.group(1).strip()
            am = RE_ACT.match(t)
            if am:
                num, rest = am.group(1), am.group(2)
                rng = ""
                tm = RE_RANGE.search(rest)
                # chỉ giữ nguyên ngoặc cuối nếu là MỐC THỜI GIAN (vd "(10:00 – 16:30)").
                # Ngoặc là thuật ngữ (vd "(FOLIE À DEUX)") phải được dịch cùng tiêu đề,
                # nếu không sẽ còn sót tiếng Việt trong bản JA.
                if tm and RE_TIME_RANGE.search(tm.group(1)):
                    rng, rest = tm.group(1), rest[: tm.start()].strip()
                add("ACT", rest, "title of the Act", num=num, rng=rng)
            else:
                add("H2", t, "section heading")
            continue
        m = RE_H3.match(s)
        if m:
            add("H3", m.group(1).strip(), "sub-heading")
            continue

        m = RE_CUE.match(s)
        if m:
            add("CUE", m.group(2).strip(), f"description of the {m.group(1)} sound cue", tag=m.group(1))
            continue

        m = RE_PAUSE.match(s)
        if m:
            add("PAUSE", (m.group(1) + " || " + m.group(2)).strip(),
                "pause marker: keep the number of seconds", secs=m.group(1).strip(),
                pause_note=m.group(2).strip())
            continue

        m = RE_TABLE.match(s)
        if m:
            cells = [c.strip() for c in m.group(1).split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c or "") for c in cells):
                raw(line)
                continue
            add("TABLE", "\t".join(cells), "table row: cells separated by TAB, keep the same number of cells")
            continue

        m = RE_BULLET.match(s)
        if m:
            add("BULLET", m.group(2).strip(), "bullet list item", prefix=m.group(1))
            continue

        # dòng nhãn đậm + nội dung (vd "**Chủ đề:** ...") = metadata, không phải thoại
        if RE_LABELED.match(s) and not s.endswith("**"):
            add("LABELED", s, "bold label + content (metadata line)")
            continue

        # dòng thoại (giữ nguyên dấu ** và * của file gốc)
        lead = s.startswith('"')
        trail = s.endswith('"') and len(s) > 1
        inner = s[1:] if lead else s
        inner = inner[:-1] if trail else inner
        add("TEXT", inner.strip(), "dialogue", quote_lead=lead, quote_trail=trail)

    return units


# ------------------------------------------------------------------ prompt
STYLE = """あなたは、犯罪心理学を題材とするポッドキャスト・チャンネルの日本語版を作る専門翻訳者です。
ベトナム語の台本を、日本人視聴者向けの自然で高品質な日本語のナレーション台本へ変換します。

【文体】
- 落ち着いた語りかけのナレーション調。書面語ではなく、音声で読んで自然な口語的な日本語にする。
- 敬体（です・ます調）で統一する。
- 中国語の語順・中国語の簡体字を使わない。日本語の漢字表記（点・断・国・学・実・声・発など）は正しく使う。
- 原文の情報量・事実関係・トーンを厳密に保つ。勝手な補足・解説・推測・警告を加えない。

【固有名詞】
- 人物名・事件名・組織名・文書名は原語のアルファベット表記のまま残す（例: Dee Dee Blanchard、Gypsy Rose、Jeffrey Dahmer、Patrick Kennedy、FBI）。
- 地名・州名・国名は自然な日本語表記にしてよい（例: Milwaukee→ミルウォーキー、Missouri→ミズリー、California→カリフォルニア）。
- 数字はそのまま残す。通貨記号は ドル・ユーロ・ポンド に直す。

【1文 = 1文】
- 入力の "vi" は台本の1文をそのまま切り出したもの。必ず1文に対して1文だけ出す。
- 出力の文は 。／？／！ のどれか1つで終える。句点は1文につき1個だけ。
- 1文の中に句点を2個置かない。文中に「、」や「――」で区切ること。
- 元の文が「:」や「–」で終わっていても、JA では句点で文を完結させる（意味は変わらない）。
- "ctx" があれば、その行全体の文脈。"vi" だけを翻訳する。ctx の中身を翻訳に混ぜない。

【書式】
- **強調** と *斜体* の記号は、位置と内容を含めてそのまま残す。
- 入力と同じ要素数で出力する。

【出力】
- 入力と同じ順序・同じ個数の JSON 配列だけを出力する。
- 各要素は {"id": "<入力のid>", "ja": "<1文の日本語訳>"}。
- 前置き・説明・コードフェンス・余計な文字は一切書かない。"""

STYLE_META = """あなたは、犯罪心理学を題材とするポッドキャスト・チャンネルの日本語版を作る専門翻訳者です。
ベトナム語の台本のメタ情報（見出し・表・効果音の説明・演技指示）を日本語に訳します。

【文体】
- 簡潔で、音声で読みやすい日本語。敬体（です・ます調）。
- 中国語の語順・中国語の簡体字を使わない。
- 固有名詞・数値・略号はそのまま残す。

【出力】
- 入力と同じ順序・同じ個数の JSON 配列だけを出力する。
- 各要素は {"id": "<入力のid>", "ja": "<日本語訳>"}。
- 前置き・説明・コードフェンス・余計な文字は一切書かない。"""


def glossary_block(items):
    blob = "\n".join(it["vi"] for it in items)
    rows = [f"- {vi} → {ja}" for vi, ja in TERMS.items() if vi in blob]
    if not rows:
        return ""
    return "\n【固 定 訳（該当箇所は必ずこの訳を使う）】\n" + "\n".join(rows) + "\n"


def build_prompt(items, kind):
    if kind == "dialogue":
        pl = []
        for it in items:
            d = {"id": it["id"], "vi": it["vi"]}
            if it.get("ctx") and it["ctx"] != it["vi"]:
                d["ctx"] = it["ctx"]
            pl.append(d)
        body = "台本の台詞（ナレーション）を1文ずつ日本語に翻訳してください。"
        sys_p = STYLE
    elif kind == "line":
        pl = []
        for it in items:
            d = {"id": it["id"], "vi": it["vi"], "n": it.get("n", 0)}
            if it.get("ctx") and it["ctx"] != it["vi"]:
                d["ctx"] = it["ctx"]
            pl.append(d)
        body = ("台本の台詞（ナレーション）を日本語に翻訳してください。"
                "入力の n はその行の文数。出力の句点（。／？／！）の個数を必ず n と一致させてください。"
                "1文を2文に割らず、2文を1文にまとめず、行末は句点で終えてください。"
                "「…」（三点リーダ）は使わないでください（文の区切りとして数えられます）。")
        sys_p = STYLE
    elif kind == "table":
        pl = []
        for it in items:
            pl.append({"id": it["id"], "cells": it.get("cells", it["vi"].split("\t"))})
        body = ("台本の表の行を日本語に翻訳してください。"
                "入力の cells は1行のセルを並べた配列。出力もcellsという名の配列にし、"
                "セルの個数(入力の cells と同数)を必ず守ってください。"
                "セルをまとめたり分けたりしないこと。"                "セル内の数値・固有名詞・略号はそのまま残す。"
                "1つ目のセルは項目名、2つ目以降は説明。")
        sys_p = STYLE_META
    else:
        pl = [{"id": it["id"], "vi": it["vi"], "note": it.get("note", "")} for it in items]
        body = ("台本のメタ情報（見出し・効果音の説明・演技指示など）を日本語に翻訳してください。"
                "見出しは簡潔で受け入れる日本語の見出しに。"
                "効果音・BGMの説明は、日本語のナレーション用サウンド Descriptionsとして、簡潔に1文で。"
                "演技指示は声の出演者向けの指示として、簡潔に。")
        sys_p = STYLE_META
    return (f"{body}\n{glossary_block(items)}\n入力（JSON 配列）：\n"
            f"{json.dumps(pl, ensure_ascii=False)}\n\n出力は JSON 配列のみ：\n"), sys_p


def make_retry_prompt(items, kind, why_lines):
    if kind == "dialogue":
        body = "台詞の翻訳を修正してください。"
    elif kind == "line":
        body = "台詞の翻訳を修正してください。句点（。／？／！）の個数を n と一致させてください。"
    elif kind == "table":
        body = ("表の行の翻訳を修正してください。"
                "セルの個数を入力と同じにしてください。")
    else:
        body = "メタ情報の翻訳を修正してください。"
    pl = []
    for it in items:
        if kind == "table":
            pl.append({"id": it["id"], "cells": it.get("cells", it["vi"].split("\t"))})
            continue
        d = {"id": it["id"], "vi": it["vi"]}
        if kind == "line":
            d["n"] = it.get("n", 0)
        if it.get("ctx") and it["ctx"] != it["vi"]:
            d["ctx"] = it["ctx"]
        pl.append(d)
    sys_p = STYLE if kind in ("dialogue", "line") else STYLE_META
    return (f"{body}\n以下は前回の出力で検査に引っかかった項目です。問題を直した JSON 配列だけ返してください。\n"
            + "\n".join(why_lines) + "\n\n入力：\n" + json.dumps(pl, ensure_ascii=False) +
            "\n\n出力は JSON 配列のみ：\n"), sys_p


# ------------------------------------------------------------------ kiểm tra
# Lưu ý quan trọng: parser chính tách câu JA bằng ja_split, tức MỌI ký tự
# 。！？… đều kết thúc một câu. Vì vậy bản JA không được dùng "…" (kể cả "……")
# và mỗi câu phải có đúng MỘT dấu kết câu ở cuối.
def fix_table_cells(cells, expected):
    """Cứu bảng khi model trả về số ô khác mong đợi.

    - gộp rồi tách lại theo TAB (model trả 1 ô chứa cả TAB)
    - nếu dư ô: gộp phần dư vào ô cuối
    - nếu thiếu ô: gộp các ô sau về ô cuối
    """
    if not isinstance(cells, list) or not cells:
        return None
    if len(cells) == expected:
        return cells
    parts = "\t".join(cells).split("\t")
    if len(parts) == expected:
        return parts
    if len(cells) < expected and len(parts) > expected:
        return parts[:expected - 1] + ["\t".join(parts[expected - 1:])]
    if len(cells) > expected:
        return list(cells[:expected - 1]) + ["\t".join(cells[expected - 1:])]
    return None


def repair_ja(ja: str, vi: str) -> str:
    """Sửa CƠ HỌC các lỗi hình thức model hay mắc (không đổi nghĩa).

    - "…" (parser coi MỖI … là 1 câu) -> "――" (gạch ngang Nhật, không ngắt câu)
    - khôi phục dấu * bị rớt ở cuối câu
    """
    if not ja:
        return ja
    s = ja.replace("……", "――").replace("…", "――")
    # dấu phẩy Trung Quốc "，" -> dấu phẩy Nhật "、" (tiếng Nhật không dùng "，")
    s = s.replace("，", "、")
    if vi.count("*") - vi.count("**") > s.count("*") - s.count("**"):
        t = s.rstrip()
        if t and not t.endswith("*"):
            s = t + "*"
    return s


def check_sentence(ja: str, vi: str, ep_tokens=None, ctx: str = ""):
    """Kiểm tra 1 câu JA dịch từ 1 câu VN. -> (ok, lý do, loại lỗi)

    loại lỗi: "" (đạt) · "structure" (sai cấu trúc -> phải dịch lại)
               · "quality" (rác/chất lượng -> có thể nhận kèm cảnh báo)
    """
    if not ja or not ja.strip():
        return False, "rỗng", "structure"
    ja = fix_latin(ja).strip()
    if "…" in ja:
        return False, "có ký tự … (parser tính mỗi … là 1 câu)", "structure"
    n_end = len(re.findall(r"[。？！]", ja))
    if n_end != 1:
        return False, f"câu JA có {n_end} dấu kết câu, cần đúng 1", "structure"
    if not re.search(r"[。？！][」』”\"）)\]]*(\*\*|\*)?$", ja):
        return False, "câu JA chưa kết thúc bằng dấu câu", "structure"
    if vi.count("**") != ja.count("**"):
        return False, "mất dấu **", "structure"
    if vi.count("*") - vi.count("**") != ja.count("*") - ja.count("**"):
        return False, "mất dấu *", "structure"
    if len(ja) > len(vi) * 3.2 + 120:
        return False, "quá dài", "structure"
    cont = contamination_flags(ja)
    if cont:
        return False, "; ".join(cont), "structure"
    hard, _ = quality_flags(ja, vn_tokens_of(ctx or vi), ctx or vi, ep_tokens)
    if hard:
        return False, "; ".join(hard), "quality"
    return True, "", ""


def check_line(ja: str, vi: str, n_sent: int, ep_tokens=None):
    """Kiểm tra 1 dòng thoại dịch cả dòng (dùng khi không tách câu được)."""
    if not ja or not ja.strip():
        return False, "rỗng", "structure"
    ja = fix_latin(ja).strip()
    cont = contamination_flags(ja)
    if cont:
        return False, "; ".join(cont), "structure"
    if "…" in ja:
        return False, "có ký tự … (parser tính mỗi … là 1 câu)", "structure"
    if ja_sentences(ja) != n_sent:
        return False, f"số câu JA = {ja_sentences(ja)}, cần = {n_sent}", "structure"
    if vi.count("**") != ja.count("**"):
        return False, "mất dấu **", "structure"
    if vi.count("*") - vi.count("**") != ja.count("*") - ja.count("**"):
        return False, "mất dấu *", "structure"
    if len(ja) > len(vi) * 3.2 + 120:
        return False, "quá dài", "structure"
    hard, _ = quality_flags(ja, vn_tokens_of(vi), vi, ep_tokens)
    if hard:
        return False, "; ".join(hard), "quality"
    return True, "", ""


def check_meta(ja: str, vi: str, ep_tokens=None):
    """Kiểm tra 1 dòng meta (tiêu đề / bảng / cue / nhãn)."""
    if not ja or not ja.strip():
        return False, "rỗng", "structure"
    ja = fix_latin(ja).strip()
    cont = contamination_flags(ja)
    if cont:
        return False, "; ".join(cont), "structure"
    if vi.count("**") != ja.count("**"):
        return False, "mất dấu **", "structure"
    if vi.count("*") - vi.count("**") != ja.count("*") - ja.count("**"):
        return False, "mất dấu *", "structure"
    if "\t" in vi and len(ja.split("\t")) != len(vi.split("\t")):
        return False, "số ô của bảng không khớp", "structure"
    if len(ja) > len(vi) * 3.2 + 120:
        return False, "quá dài", "structure"
    hard, _ = quality_flags(ja, vn_tokens_of(vi), vi, ep_tokens)
    if hard:
        return False, "; ".join(hard), "quality"
    return True, "", ""


def line_problems(ja_line: str, vn_line: str):
    """Kiểm tra ở MỨC DÒNG sau khi ghép các câu -> danh sách lỗi.

    Số câu được đối chiếu theo đúng luật parse_kichban: bỏ marker + prefix
    bullet + dấu nháy rồi mới tách.
    """
    probs = []
    if not ja_line:
        return ["dòng rỗng"]
    need = official_counts([vn_line])[0]
    got = ja_sentences(ja_line)
    if got != need:
        probs.append(f"số câu JA = {got}, cần = {need}")
    if vn_line.count("**") != ja_line.count("**"):
        probs.append("mất dấu **")
    if vn_line.count("*") - vn_line.count("**") != ja_line.count("*") - ja_line.count("**"):
        probs.append("mất dấu *")
    lost = [n for n in proper_names(vn_line) if n not in ja_line]
    if lost:
        probs.append("mất tên riêng: " + ", ".join(lost[:4]))
    return probs


# ------------------------------------------------------------------ gọi LLM
def _scan_objects(txt):
    """Trích từng đối tượng JSON cân bằng trong chuỗi (dự phòng khi mảng hỏng)."""
    out, depth, start, instr, esc = [], 0, None, False, False
    for i, ch in enumerate(txt):
        if instr:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                instr = False
            continue
        if ch == '"':
            instr = True
            continue
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}" and depth:
            depth -= 1
            if depth == 0 and start is not None:
                try:
                    out.append(json.loads(txt[start:i + 1]))
                except Exception:
                    pass
                start = None
    return out


def parse_json_array(txt):
    txt = txt.strip()
    if txt.startswith("```"):
        txt = re.sub(r"^```[a-zA-Z]*\s*", "", txt)
        txt = re.sub(r"\s*```$", "", txt)
    a, b = txt.find("["), txt.rfind("]")
    if a >= 0 and b > a:
        try:
            data = json.loads(txt[a:b + 1])
            if isinstance(data, list):
                return data
        except Exception:
            pass
    # dự phòng: mảng JSON hỏng -> quét từng đối tượng
    objs = _scan_objects(txt)
    if objs:
        return objs
    raise ValueError("không thấy mảng JSON")


def call_batch(items, kind, tries=3, ep_tokens=None, err_sink=None, warn_sink=None):
    """Dịch một lô -> dict id -> ja (chỉ những cái đạt kiểm tra).

    kind: "dialogue" = 1 câu -> 1 câu · "line" = cả dòng · "meta" = thông tin phụ
    err_sink: dict để ghi lý do lỗi của các mục cuối cùng vẫn hỏng (để chẩn đoán).
    warn_sink: dict để ghi các mục CHẤP NHẬN KÈM CẢNH BÁO (lỗi chất lượng, không mất câu).

    Nguyên tắc: KHÔNG BAO GIỜ bỏ trống một dòng thoại. Bỏ trống = mất nội dung và
    làm lệch số câu so với bản VN. Nếu chỉ còn lỗi chất lượng thì nhận bản dịch
    và ghi cảnh báo để rà soát thủ công.
    """
    out = {}
    last_err = err_sink if err_sink is not None else {}
    warns = warn_sink if warn_sink is not None else {}
    best = {}          # id -> (ja, reason, kind)  ưu tiên: đạt > lỗi chất lượng > lỗi cấu trúc
    pending = list(items)

    def evaluate(it, ja):
        ja = repair_ja(ja, it["vi"])
        if kind == "dialogue":
            ok, reason, k = check_sentence(ja, it["vi"], ep_tokens, it.get("ctx", ""))
        elif kind == "line":
            ok, reason, k = check_line(ja, it["vi"], it.get("n", 0), ep_tokens)
        else:
            ok, reason, k = check_meta(ja, it["vi"], ep_tokens)
        rank = 0 if ok else (1 if k == "quality" else 2)
        prev = best.get(it["id"])
        if prev is None or rank < prev[3]:
            best[it["id"]] = (ja, reason, k, rank)
        return ok, reason, k, ja
    for attempt in range(tries):
        if not pending:
            break
        try:
            prompt, sys_p = build_prompt(pending, kind)
            txt = ja_llm.call(prompt, sys_p, model=MODEL, max_tokens=16000,
                              temperature=0.2, timeout=420)
            data = parse_json_array(txt)
        except Exception as e:
            print(f"      [llm lỗi {attempt + 1}: {str(e)[:150]}]", flush=True)
            time.sleep(4 * (attempt + 1))
            continue
        got = {}
        vmap = {x["id"]: x.get("vi", "") for x in pending}
        for row in data:
            if not (isinstance(row, dict) and "id" in row):
                continue
            vi_row = vmap.get(str(row["id"]), "")
            if kind == "table":
                cells = row.get("cells")
                if isinstance(cells, list) and all(isinstance(c, str) for c in cells):
                    exp = len(vi_row.split("\t")) if vi_row else len(cells)
                    fixed = fix_table_cells(cells, exp)
                    if fixed:
                        got[str(row["id"])] = "\t".join(
                        _table_cell(_clean_ja(c, vi_row)) for c in fixed)
                continue
            if isinstance(row.get("ja"), str):
                got[str(row["id"])] = _clean_ja(row["ja"], vi_row)
        still, why = [], []
        for it in pending:
            ja = got.get(it["id"])
            if ja is None:
                still.append(it)
                last_err[it["id"]] = "model không trả về nội dung"
                why.append(f'  - id {it["id"]}: "{it["vi"][:110]}"\n    lý do: không có phản hồi')
                continue
            ok, reason, _k, ja = evaluate(it, ja)
            if ok:
                out[it["id"]] = ja
            else:
                still.append(it)
                last_err[it["id"]] = reason
                why.append(f'  - id {it["id"]}: "{it["vi"][:110]}"\n    lý do: {reason}')
        pending = still
        if pending and attempt >= 1:
            try:
                sub, sys_p = make_retry_prompt(pending, kind, why)
                txt2 = ja_llm.call(sub, sys_p, model=MODEL, max_tokens=8000,
                                   temperature=0.05, timeout=300)
                for row in parse_json_array(txt2):
                    if not isinstance(row, dict):
                        continue
                    it = next((x for x in pending if x["id"] == str(row["id"])), None)
                    if not it:
                        continue
                    if kind == "table":
                        cells = row.get("cells")
                        if not (isinstance(cells, list)
                                and all(isinstance(c, str) for c in cells)):
                            continue
                        exp = len(it["vi"].split("\t")) if it["vi"] else len(cells)
                        cells = fix_table_cells(cells, exp) or cells
                        ja = "\t".join(
                            _table_cell(_clean_ja(c, it["vi"])) for c in cells)
                    else:
                        if not isinstance(row.get("ja"), str):
                            continue
                        ja = _clean_ja(row["ja"], it["vi"])
                    ok, _r, _k, ja = evaluate(it, ja)
                    if ok:
                        out[it["id"]] = ja
                        pending = [x for x in pending if x["id"] != it["id"]]
            except Exception as e:
                print(f"      [retry lỗi: {str(e)[:120]}]", flush=True)
    if pending:
        # --- vòng cuối: dịch TỪNG MỘT, prompt siết, tối đa 2 lần nữa.
        # Khi nằm trong lô, 1 câu hỏng có thể kéo theo cả lô; tách ra riêng thì
        # model tập trung hơn và dễ ép đúng 1 dấu kết câu.
        for it in list(pending):
            for attempt in range(2):
                try:
                    prompt, sys_p = build_prompt([it], kind)
                    hint = last_err.get(it["id"], "")
                    if hint:
                        prompt = (f"前回の回答は検査で弾かれました: {hint}\n"
                                  f"この点を直して、指示どおりに翻訳し直してください。\n"
                                  f"{prompt}")
                    # max_tokens phải đủ cho cả phần "thinking" của Flash
                    # (~2500-3000 token) + phần text, nếu không sẽ "empty text".
                    txt = ja_llm.call(prompt, sys_p, model=MODEL, max_tokens=8000,
                                      temperature=0.1, timeout=300)
                    data = parse_json_array(txt)
                except Exception as e:
                    print(f"      [solo lỗi {it['id']}: {str(e)[:100]}]", flush=True)
                    time.sleep(3)
                    continue
                ja = ""
                for row in data:
                    if not isinstance(row, dict) or str(row.get("id")) != it["id"]:
                        continue
                    if kind == "table":
                        cells = row.get("cells")
                        if isinstance(cells, list) and all(isinstance(c, str) for c in cells):
                            exp = len(it["vi"].split("\t")) if it["vi"] else len(cells)
                            cells = fix_table_cells(cells, exp) or cells
                            ja = "\t".join(
                                _table_cell(_clean_ja(c, it["vi"])) for c in cells)
                        break
                    if isinstance(row.get("ja"), str):
                        ja = _clean_ja(row["ja"], it["vi"])
                        break
                ok, reason, _k, ja = evaluate(it, ja)
                if ok:
                    out[it["id"]] = ja
                    pending = [x for x in pending if x["id"] != it["id"]]
                    break
                last_err[it["id"]] = reason
    # --- cứu vãn: mục chỉ còn lỗi CHẤT LƯỢNG -> nhận kèm cảnh báo.
    # Bỏ trống dòng thoại sẽ làm mất nội dung và lệch số câu so với bản VN.
    still_bad = []
    for it in list(pending):
        cand = best.get(it["id"])
        if cand and cand[2] == "quality" and cand[0]:
            out[it["id"]] = cand[0]
            warns[it["id"]] = cand[1]
            pending = [x for x in pending if x["id"] != it["id"]]
        else:
            still_bad.append(it)
    if still_bad:
        print(f"      [còn {len(still_bad)} mục dịch hỏng: "
              f"{', '.join(p['id'] for p in still_bad[:8])}]", flush=True)
        for p in still_bad:
            last_err[p["id"]] = last_err.get(p["id"], "?")
    if warns:
        print(f"      [nhận kèm cảnh báo: {len(warns)} mục]", flush=True)
    return out


def find_review(ep: str) -> str:
    """Đường dẫn tới file review sự thật/pháp lý của tập (nếu có)."""
    import glob
    # ưu tiên: review của bản VN (nguồn trực tiếp của bản JA) -> review VN ở 02_SAN_XUAT
    # -> review bản EN (dùng khi không có bản VN).
    pats = [str(KB / f"Tap{ep}" / "REVIEW*.md"),
            str(ROOT / "02_SAN_XUAT" / f"Tap{ep}" / "REVIEW*.md"),
            str(ROOT / "02_SAN_XUAT" / f"Tap{ep}_*" / "REVIEW*.md")]
    for pat in pats:
        hits = sorted(glob.glob(pat))
        if hits:
            p = Path(hits[0])
            try:
                return p.relative_to(ROOT).as_posix()
            except ValueError:
                return p.as_posix()
    return ""


# ------------------------------------------------------------------ render
def render(units, src_rel="", review_ref=""):
    out, i, added_header = [], 0, False
    while i < len(units):
        u = units[i]
        k = u["kind"]
        if k == "RAW":
            out.append(u["raw"])
            i += 1
            continue
        ja = u.get("ja", "")
        if k == "H1":
            out.append(f"# {ja} — 日本語版")
        elif k == "H2":
            out.append(f"## {ja}")
        elif k == "H3":
            out.append(f"### {ja}")
        elif k == "ACT":
            head = f"## 第{u['num']}幕：{ja}"
            if u.get("rng"):
                head += f" {u['rng']}"
            out.append(head)
        elif k == "TABLE":
            out.append("| " + " | ".join(ja.split("\t")) + " |")
        elif k == "CUE":
            out.append(f"**[{u['tag']}]:** {ja}")
        elif k == "PAUSE":
            m = re.search(r"([\d.]+)", u.get("secs", ""))
            num = m.group(1) if m else ""
            txt = f"**[休止 {num}秒]**"
            if u.get("pause_note"):
                txt += f" {ja}"
            out.append(txt)
        elif k == "ROLE":
            direction = ""
            if i + 1 < len(units) and units[i + 1]["kind"] == "DIRECTION":
                direction = units[i + 1].get("ja", "")
                i += 1
            out.append(f"**{ja}** *({direction})*:" if direction else f"**{ja}**:")
        elif k == "BULLET":
            out.append(f"{u.get('prefix', '*   ')}{ja}")
        elif k == "LABELED":
            out.append(ja)
            if not added_header:
                added_header = True
                out.append(f"**原文:** `{src_rel}`. "
                           f"ベトナム語1文に対し日本語1文。構造・コードは同一。")
                if review_ref:
                    out.append(f"**事実・法務チェック:** {review_ref}")
        elif k == "TEXT":
            s = ja
            if u.get("quote_lead"):
                s = '"' + s
            if u.get("quote_trail"):
                s = s + '"'
            out.append(s)
        else:
            out.append(ja)
        i += 1
    return "\n".join(out) + "\n"


def cache_signature() -> str:
    """Chữ ký của cache: đổi glossary / prompt / model => cache cũ tự động vô hiệu.

    Nhờ vậy sửa thuật ngữ giữa chừng không làm sót bản dịch cũ.
    """
    import hashlib
    blob = json.dumps(
        {"terms": TERMS, "roles": ROLES_JA, "style": STYLE, "style_meta": STYLE_META,
         "model": MODEL},
        ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:12]


# ------------------------------------------------------------------ chạy 1 tập
def build_episode(ep: str, workers: int, batch_chars: int, batch_items: int):
    src = canonical_vn(ep)
    units = assign_turn_counts(parse_units(src))

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / f"tap{ep}.json"
    cache = {}
    sig = cache_signature()
    if cache_path.exists():
        try:
            raw_cache = json.loads(cache_path.read_text(encoding="utf-8"))
            if raw_cache.get("_v") == CACHE_VERSION and raw_cache.get("_sig") == sig:
                cache = raw_cache
            else:
                print(f"   [cache cũ bị vô hiệu (v={raw_cache.get('_v')} "
                      f"sig={raw_cache.get('_sig')}) -> dịch lại]", flush=True)
        except Exception:
            cache = {}

    for u in units:
        if u["kind"] == "ROLE":
            cache[u["id"]] = {"ja": ROLES_JA.get(u["vi"], u["vi"])}

    in_turn = {u["id"] for t in group_turns(units) for u in t["units"]}
    src_text = src.read_text(encoding="utf-8")
    ep_tokens = vn_tokens_of(src_text)

    # --- tách câu: mỗi câu VN thành 1 mục dịch riêng => 1 câu JA = 1 câu VN tuyệt đối
    all_jobs = []
    for u in units:
        if u["kind"] == "RAW":
            continue
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = splittable(u)
            if parts:
                for k, p in enumerate(parts):
                    all_jobs.append({"id": f"{u['id']}#{k}", "vi": p, "ctx": u["vi"],
                                     "kind": "dialogue", "unit": u})
                continue
            # không tách được -> dịch cả dòng, kiểm số câu ở mức dòng
            all_jobs.append({"id": f"{u['id']}#L", "vi": u["vi"], "ctx": u["vi"],
                             "kind": "line", "n": u.get("n", 0), "unit": u})
            continue
        if u["kind"] == "TABLE":
            all_jobs.append({"id": u["id"], "vi": u["vi"], "kind": "table",
                             "cells": u["vi"].split("\t"), "unit": u})
            continue
        all_jobs.append({"id": u["id"], "vi": u["vi"], "kind": "meta", "unit": u})

    # --- TỰ KIỂM LẠI CACHE: mục nào không còn đạt kiểm tra thì bỏ để dịch lại.
    # Nhờ vậy các lỗi tồn đọng từ lần chạy trước (rác Cyrillic, dòng bị rút còn
    # 1 câu do lỗi trộn kind) tự biến mất thay vì nằm mãi trong cache.
    stale = []
    for j in all_jobs:
        if j["id"] not in cache:
            continue
        if j["kind"] == "meta" and j["unit"]["kind"] in ("ROLE", "PAUSE"):
            continue        # vai & nhịp nghỉ do bộ dịch tự đặt, không cần kiểm lại
        raw = cache[j["id"]].get("ja", "") if isinstance(cache[j["id"]], dict) else ""
        ja = repair_ja(raw, j["vi"])
        if j["kind"] == "table" and ("\n" in ja or "\r" in ja):
            # ô bảng bị model đổi <br> thành newline -> quy lại <br>
            ja = re.sub(r"\r\n|\r|\n", "<br>", ja).strip()
        if j["kind"] == "dialogue":
            ok, reason, _k = check_sentence(ja, j["vi"], ep_tokens, j.get("ctx", ""))
        elif j["kind"] == "line":
            ok, reason, _k = check_line(ja, j["vi"], j.get("n", 0), ep_tokens)
        else:
            ok, reason, _k = check_meta(ja, j["vi"], ep_tokens)
        if ok:
            if ja != raw:
                cache[j["id"]] = {"ja": ja}
        else:
            stale.append((j["id"], reason))
    for jid, _r in stale:
        cache.pop(jid, None)
    if stale:
        print(f"   [cache: bỏ {len(stale)} mục không đạt kiểm tra -> dịch lại: "
              f"{', '.join(j for j, _r in stale[:8])}]", flush=True)

    jobs = [j for j in all_jobs if j["id"] not in cache]

    # QUAN TRỌNG: mỗi loại phải một batch riêng. Trộn "line" vào "dialogue" sẽ
    # khiến check_sentence (đòi đúng 1 dấu kết câu) áp cho dòng nhiều câu =>
    # dòng đó bị rút còn 1 câu mà vẫn lọt.
    dialogue_jobs = [j for j in jobs if j["kind"] == "dialogue"]
    line_jobs = [j for j in jobs if j["kind"] == "line"]
    table_jobs = [j for j in jobs if j["kind"] == "table"]
    meta_jobs = [j for j in jobs if j["kind"] == "meta"]

    def pack(items):
        out, cur, sz = [], [], 0
        for it in items:
            L = len(it["vi"])
            if cur and (len(cur) >= batch_items or sz + L > batch_chars):
                out.append(cur)
                cur, sz = [], 0
            cur.append(it)
            sz += L
        if cur:
            out.append(cur)
        return out

    batches = ([(b, "dialogue") for b in pack(dialogue_jobs)]
               + [(b, "line") for b in pack(line_jobs)]
               + [(b, "table") for b in pack(table_jobs)]
               + [(b, "meta") for b in pack(meta_jobs)])
    n_sent = sum(u["n"] for u in units if u["kind"] in ("TEXT", "BULLET"))
    print(f"[Tap{ep}] {src.name}: {len(units)} dòng · {len(dialogue_jobs)} câu · "
          f"{len(line_jobs)} dòng · {len(table_jobs)} bảng · {len(meta_jobs)} meta · "
          f"{n_sent} câu · {len(batches)} lô · cache {len(cache)}", flush=True)

    t0 = time.time()
    errs = {}
    warns = {}
    if batches:
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = [(ex.submit(call_batch, b, k, 3, ep_tokens, errs, warns), b, k)
                    for b, k in batches]
            for f, b, k in futs:
                res = f.result()
                for uid, ja in res.items():
                    cache[uid] = {"ja": ja}
                cache["_v"] = CACHE_VERSION
                cache["_sig"] = sig
                cache["_err"] = errs
                cache["_warn"] = warns
                cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1),
                                      encoding="utf-8")
                done = sum(1 for j in jobs if j["id"] in cache)
                print(f"   lô xong · {time.time() - t0:.0f}s · {done}/{len(jobs)}", flush=True)

    # --- ghép các câu thành dòng
    for u in units:
        if u["kind"] == "RAW":
            continue                      # dòng thô (trống / ---) -> giữ nguyên khi render
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = splittable(u)
            if parts:
                got = [cache.get(f"{u['id']}#{k}", {}).get("ja", "") for k in range(len(parts))]
                if all(got):
                    # nối thẳng: parse_kichban xoá ** và * TRƯỚC khi tách câu,
                    # nên vị trí marker trong JA giống hệt VN là an toàn.
                    u["ja"] = "".join(got)
                else:
                    u["ja"] = ""
            else:
                u["ja"] = cache.get(f"{u['id']}#L", {}).get("ja", "")
            # sửa quy ước số VN -> JA (áp lại lúc ghép để sửa luôn bản đã cache)
            u["ja"] = fix_numbers(u["ja"], u["vi"])
        else:
            u["ja"] = cache.get(u["id"], {}).get("ja", "")
            u["ja"] = fix_numbers(u["ja"], u["vi"])
    missing = [u["id"] for u in units if u["kind"] != "RAW" and not u.get("ja")]
    return units, src, missing, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ep")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--batch-chars", type=int, default=2200)
    ap.add_argument("--batch-items", type=int, default=12)
    args = ap.parse_args()

    eps = [f"{i:02d}" for i in range(1, 30)] if args.all else [args.ep]
    REPORT.mkdir(parents=True, exist_ok=True)
    for ep in eps:
        units, src, missing, warns = build_episode(ep, args.workers, args.batch_chars,
                                                    args.batch_items)
        outdir = KB / f"Tap{ep}_JA"
        outdir.mkdir(parents=True, exist_ok=True)
        src_rel = src.relative_to(ROOT).as_posix()
        review_ref = find_review(ep)
        md = render(units, src_rel, review_ref)
        (outdir / f"kichban_tap{ep}_JA.md").write_text(md, encoding="utf-8")
        rep = {"ep": ep, "src": src.name, "missing": missing, "units": len(units),
               "sentences": sum(u.get("n", 0) for u in units if u["kind"] == "TEXT"),
               "warn": warns}
        (REPORT / f"tap{ep}.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1),
                                              encoding="utf-8")
        print(f"[Tap{ep}] -> {outdir / f'kichban_tap{ep}_JA.md'}  thiếu={len(missing)}"
              f"  cảnh-báo={len(warns)}", flush=True)


if __name__ == "__main__":
    main()
