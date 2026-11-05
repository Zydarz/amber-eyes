#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — kiểm nghiêm lớp phủ chữ EN (bổ sung cho _qc_chu_t04.py).

Kiểm thêm:
  A. Trích dẫn “…” đứng RIÊNG phải NGUYÊN VĂN trong câu (hoa/thường + dấu câu)
     — đúng cổng QC dự án (_qc_tap02_shots.py) — lược bằng "…" được phép.
  B. Khung giống bản VN: cùng số khối, cùng mốc `#N`, cùng loại phần tử (đậm/nghiêng/trích).
  C. Không có "|" (phá bảng markdown).
  D. Không còn tiếng Việt trong chữ EN.
  E. Không dùng từ cấm (FORBIDDEN_EN của cổng QC dự án).
  F. Beat: cụm trigger phải nằm trong câu EN; beat có trigger phải giữ lệnh "ở".

Dùng: py -3 .work/_t04_check_en_overlay.py
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

SK = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
SENT = json.loads((W / "_t04_sentences.json").read_text(encoding="utf-8"))["en"]
CHU_EN = json.loads((W / "_t04_chu_en.json").read_text(encoding="utf-8"))
CHU_VN = json.loads((W / "_t04_chu_vn.json").read_text(encoding="utf-8"))
BEAT_EN = json.loads((W / "_t04_beat_en.json").read_text(encoding="utf-8"))

FORBIDDEN_EN = ["blood", "corpse", "strangle", "choke", "struggle", "raped", "rape",
                "underwear", "sexual intercourse", "orgasm", "penis", "vagina", "suffocat",
                "mutilat", "dismember", "torture"]
SAFE_EN = ["blood type", "blood pressure", "blood vessel", "bloodstream", "blood cell",
           "struggle to survive", "struggled to"]
VN_CHARS = re.compile(r"[ăâđêôơưĂÂĐÊÔƠƯàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệ"
                      r"ìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]")


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    return " ".join(re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE).split())


def contains(frag, ctx):
    f, c = norm(frag), norm(ctx)
    fw, cw = f.split(), c.split()
    return any(cw[i:i + len(fw)] == fw for i in range(len(cw) - len(fw) + 1))


def parse_cell(cell):
    """parse_shots.parse_text — tách khối theo ' → ', rồi lấy (kind, text)."""
    segs = []
    cell = re.sub(r"\*\*.+?\*\*|\*[^*]+?\*|“.+?”", lambda m: m.group(0).replace("→", "⟶"), cell)
    for raw in re.split(r"\s+→\s+", cell):
        raw = raw.replace("⟶", "→")
        at = None
        m = re.match(r"(?:ở\s+)?`#(\d+)`:?\s*(.*)", raw, re.S)
        if m:
            at, raw = int(m.group(1)), m.group(2)
        elems = []
        for tok in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", raw, re.S):
            if tok.group(1):
                elems.append(("bold", tok.group(1)))
            elif tok.group(2):
                elems.append(("ital", tok.group(2)))
            else:
                elems.append(("quote", tok.group(3)))
        if elems:
            segs.append({"at_sentence": at, "elems": elems})
    return segs


errs = []
n_shot = n_beat = 0
for r in SK["rows"]:
    if r["kind"] != "shot":
        continue
    sid = r["sid"]
    n_shot += 1
    eid, a, b = r["spans"][0]
    sents = [d["text"] if isinstance(d, dict) else d for d in SENT.get(eid, [])]
    ctx_all = " ".join(sents[a - 1:b])

    en = CHU_EN.get(sid)
    if en is None:
        errs.append((sid, "THIẾU CHỮ"))
        continue

    # ---- C. không "|"
    if "|" in en:
        errs.append((sid, "có ký tự | (phá bảng markdown)"))

    # ---- D. không tiếng Việt
    m_vn = VN_CHARS.search(en)
    if m_vn:
        errs.append((sid, f"còn tiếng Việt: «{m_vn.group(0)}»"))

    # ---- E. từ cấm
    low = en.lower()
    for w in FORBIDDEN_EN:
        if not re.search(r"(?<!\w)" + r"\s+".join(re.escape(x) for x in w.split()) + r"(?!\w)", low):
            continue
        if any(g in low for g in SAFE_EN if g in w or w in g):
            continue
        errs.append((sid, f"từ cấm «{w}»"))

    # ---- A. trích dẫn nguyên văn
    for seg in parse_cell(en):
        for kind, txt in seg["elems"]:
            if kind != "quote":
                continue
            core = txt.strip().strip("“”\"")
            for frag in [f.strip() for f in core.split("…") if f.strip()]:
                if frag not in ctx_all:
                    errs.append((sid, f"trích dẫn KHÔNG nguyên văn: «{frag[:50]}»"))

    # ---- B. khung giống bản VN
    se_vn, se_en = parse_cell(CHU_VN.get(sid, "")), parse_cell(en)
    if len(se_vn) != len(se_en):
        errs.append((sid, f"số khối khác VN: {len(se_en)} vs {len(se_vn)}"))
    else:
        for i, (sv, se) in enumerate(zip(se_vn, se_en)):
            if (sv["at_sentence"] or 0) != (se["at_sentence"] or 0):
                errs.append((sid, f"mốc #N khối {i+1} khác VN: {se['at_sentence']} vs {sv['at_sentence']}"))
            kv = [k for k, _ in sv["elems"]]
            ke = [k for k, _ in se["elems"]]
            if kv != ke:
                errs.append((sid, f"loại phần tử khối {i+1} khác VN: {ke} vs {kv}"))

    # ---- quy tắc H6/V3: liên tục + số (giống _qc_chu_t04.py)
    parts = re.split(r"\s+→\s+", en)
    cur = a
    for part in parts:
        m = re.match(r"(?:ở\s+)?`#(\d+)`:?\s*(.*)", part, re.S)
        if m:
            n = int(m.group(1))
            if not (a <= n <= b):
                errs.append((sid, f"`#{n}` ngoài khoảng câu {a}-{b}"))
            cur = max(cur, n)
            part = m.group(2)
        ctx = " ".join(sents[cur - 1:b])
        for frag in re.findall(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", part, re.S):
            txt = frag[0] or frag[1] or frag[2]
            if not contains(txt, ctx):
                errs.append((sid, f"mảnh không liên tục trong câu (từ #{cur}): «{txt[:50]}»"))
        for num in re.findall(r"\d[\d.,]*", part):
            if num.strip(".,") and not contains(num, ctx):
                errs.append((sid, f"số không có trong câu: «{num}»"))

    # ---- F. beat
    beat = BEAT_EN.get(sid)
    if r["cells"][6].strip() not in ("", "—"):
        n_beat += 1
        if beat is None:
            errs.append((sid, "THIẾU BEAT EN"))
        else:
            for ph in re.findall(r"\"([^\"]+)\"", beat):
                if norm(ph) not in norm(ctx_all):
                    errs.append((sid, f"beat trigger không có trong câu EN: «{ph}»"))
                if not re.search(r"ở \"[^\"]+\"", beat):
                    errs.append((sid, "beat có trigger nhưng mất lệnh 'ở \"...\"'"))
    elif beat is not None:
        errs.append((sid, "có beat EN nhưng shot không có beat"))

print(f"[en] shot kiểm: {n_shot} · shot có beat: {n_beat} · lỗi: {len(errs)}")
for sid, msg in errs:
    print(f"  ✗ {sid}: {msg}")
print("KẾT QUẢ:", "PASS" if not errs else "FAIL")

# ---------------------------------------------------------------------------
# Mô phỏng đúng cổng QC dự án (_qc_tap02_shots.py mục 4/5/6, chế độ EN)
# ---------------------------------------------------------------------------
MONTHS_EN = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6",
             "july": "7", "august": "8", "september": "9", "october": "10", "november": "11",
             "december": "12"}
ORD_EN_RE = [(r"red flag number one\b", "1"), (r"red flag number two\b", "2"),
             (r"red flag number three\b", "3"), (r"red flag number four\b", "4"),
             (r"\bfirst\b", "1"), (r"\bsecond\b", "2"), (r"\bthird\b", "3"), (r"\bfourth\b", "4")]
STRUCT_ANY = r"(?:HỒI|TẬP|NẤC|TẦNG|ACT|STAGE|LAYER|COMPARTMENT|EPISODE|第\s*\d+\s*幕)"
gate = []
for r in SK["rows"]:
    if r["kind"] != "shot":
        continue
    sid = r["sid"]
    eid, a, b = r["spans"][0]
    sents = [d["text"] if isinstance(d, dict) else d for d in SENT.get(eid, [])]
    ctx = " ".join(sents[a - 1:b])
    en = CHU_EN.get(sid, "")
    screen = " ".join(t for _k, t in parse_cell(en) for _ in [(0,)] for t in [t])  # text mọi phần tử
    screen = " ".join(t for _k, t in [e for sg in parse_cell(en) for e in sg["elems"]])

    # 4. trích dẫn nguyên văn
    for sg in parse_cell(en):
        for kind, t in sg["elems"]:
            if kind != "quote":
                continue
            core = t.strip().strip("“”\"")
            for frag in [f.strip() for f in core.split("…") if f.strip()]:
                if frag not in ctx:
                    gate.append(f"{sid}: trích dẫn «{frag[:45]}» không nguyên văn")

    # 5. số trên hình
    flat = ctx.replace(" ", "")
    allowed = set(re.findall(r"\d+", flat))
    for a2 in list(allowed):
        allowed.add(a2.zfill(2))
        allowed.add(str(int(a2)))
    for word, d in [("first", "1"), ("second", "2"), ("third", "3"), ("fourth", "4")]:
        if word in ctx.lower():
            allowed.add(d)
            allowed.add(d.zfill(2))
    for pat, d in ORD_EN_RE:
        if re.search(pat, ctx.lower()):
            allowed.add(d)
            allowed.add(d.zfill(2))
    for word, d in MONTHS_EN.items():
        if word in ctx.lower():
            allowed.add(d)
            allowed.add(d.zfill(2))
    if "4 stages" in ctx.lower():
        allowed.add("4")
        allowed.add("04")
    for m in set(re.findall(r"\d[\d.,]*", screen)):
        tok = m.replace(".", "")
        if m in allowed or m in flat or tok in allowed:
            continue
        if re.search(r"第\s*" + re.escape(m) + r"\s*幕", screen):
            continue
        if re.search(STRUCT_ANY + r"\s*" + re.escape(m) + r"\b", screen):
            continue
        gate.append(f"{sid}: số «{m}» không có trong câu")

    # 6. từ cấm
    low = screen.lower()
    for w in FORBIDDEN_EN:
        if not re.search(r"(?<!\w)" + r"\s+".join(re.escape(x) for x in w.split()) + r"(?!\w)", low):
            continue
        if any(g in low for g in SAFE_EN if g in w or w in g):
            continue
        gate.append(f"{sid}: từ cấm «{w}»")

print(f"[cổng QC dự án — trích dẫn/số/từ cấm] lỗi: {len(gate)}")
for g in gate:
    print(f"  ✗ {g}")
print("KẾT QUẢ CỔNG:", "PASS" if not gate else "FAIL")

# ---------------------------------------------------------------------------
# Phủ đủ id + file đầu ra (UTF-8 không BOM, LF)
# ---------------------------------------------------------------------------
shot_ids = [r["sid"] for r in SK["rows"] if r["kind"] == "shot"]
beat_ids = [r["sid"] for r in SK["rows"]
            if r["kind"] == "shot" and r["cells"][6].strip() not in ("", "—")]
miss = sorted(set(shot_ids) - set(CHU_EN))
extra = sorted(set(CHU_EN) - set(shot_ids))
miss_b = sorted(set(beat_ids) - set(BEAT_EN))
extra_b = sorted(set(BEAT_EN) - set(beat_ids))
for f, keys in (("_t04_chu_en.json", miss + extra), ("_t04_beat_en.json", miss_b + extra_b)):
    if keys:
        print(f"  ✗ {f}: lệch id {keys}")
raw = (W / "_t04_chu_en.json").read_bytes()
rawb = (W / "_t04_beat_en.json").read_bytes()
for f, b in (("_t04_chu_en.json", raw), ("_t04_beat_en.json", rawb)):
    print(f"  {f}: {len(b)} byte · BOM={b[:3] == b'\xef\xbb\xbf'} · CRLF={b'\r\n' in b}")
ok_cov = not (miss or extra or miss_b or extra_b) and raw[:3] != b"\xef\xbb\xbf" \
    and rawb[:3] != b"\xef\xbb\xbf" and b"\r\n" not in raw and b"\r\n" not in rawb
print(f"[phủ id] chu={len(CHU_EN)}/{len(shot_ids)} beat={len(BEAT_EN)}/{len(beat_ids)} · "
      + ("PASS" if ok_cov else "FAIL"))


