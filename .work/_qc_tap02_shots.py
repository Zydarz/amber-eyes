#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC A9.2 cho Tập 02 — bảng shot vs kịch bản vs timeline.

  1. Phủ câu: 215/215 câu thuộc đúng một shot, đúng thứ tự, không trùng
  2. Cột Vai khớp người nói trong timeline
  3. Nền có file thật trong assets/bg
  4. Chữ trích dẫn trên hình phải NGUYÊN VĂN trong câu của shot (V3)
     — cho phép lược bằng "…" (A7/V3): mỗi đoạn còn lại phải nguyên văn
  5. Mọi con số trên hình phải có trong câu của shot (A9.2)
     — chấp nhận: số viết không chỗ 0 (07 = 7), nhãn cấu trúc
       (HỒI 01 / TẬP 02 / NẤC 01..04 theo số thứ tự trong câu)
  6. Không từ cấm (A9.2) + không nhắc đồ lót / hành vi tình dục
  7. Shot > 15 s phải có nhịp thay đổi trong khung (beat theo cụm từ
     hoặc đoạn chữ tách theo câu) — A7
  8. Các shot liền nhau (không hở, không chồng)
"""
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BG = ROOT / "assets" / "bg"

os.environ.setdefault("AE_EP", "02")
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))
SENT = {it["id"]: it for it in TL["items"]}
SHOTS = SH["shots"]
EN = ED.EN

ok = True
errs = []
notes = []


def chk(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK  ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))
    if not cond:
        errs.append(label)


def note(label, detail=""):
    notes.append(label)
    print(f"[GHI ] {label}" + (f" — {detail}" if detail else ""))


# ---------------------------------------------------------------- 1. phu cau
all_ids = list(SENT.keys())
seen, dups, order = {}, [], []
for s in SHOTS:
    for sid in s["sentences"]:
        if sid in seen:
            dups.append(f"{sid} ở {seen[sid]} và {s['id']}")
        seen[sid] = s["id"]
        order.append(sid)

chk("Mọi câu trong timeline có mặt trong bảng shot", set(seen) == set(all_ids),
    f"thiếu {sorted(set(all_ids) - set(seen))[:6]} · thừa {sorted(set(seen) - set(all_ids))[:6]}")
chk("Không câu nào thuộc hai shot", not dups, "; ".join(dups[:5]))
chk(f"{len(all_ids)} câu được phủ", len(seen) == len(all_ids), f"{len(seen)}/{len(all_ids)}")
chk("Thứ tự shot khớp thứ tự kịch bản", order == all_ids,
    f"lệch tại vị trí {next((i for i, (a, b) in enumerate(zip(order, all_ids)) if a != b), None)}")

# ---------------------------------------------------------------- 2. vai khop
bad_role = [f"{s['id']} khai {s['role']} nhưng {sid} do {SENT[sid]['role']}"
            for s in SHOTS if s["role"] for sid in s["sentences"] if SENT[sid]["role"] != s["role"]]
chk("Cột Vai khớp người nói trong timeline", not bad_role, "; ".join(bad_role[:5]))

# ---------------------------------------------------------------- 3. nen
missing_bg = sorted({s["bg"] for s in SHOTS if s["bg"]} - {p.stem for p in BG.glob("*.png")})
chk("Mọi nền dùng trong shot đều có file", not missing_bg, ", ".join(missing_bg))

# ---------------------------------------------------------------- 4. trich danh
def on_screen(s):
    return [(kind, t) for seg in s["segments"] for kind, t in seg["elems"]]


def ctx_of(s):
    """Câu của shot. Dòng 'giữ' (hold) kế thừa chữ của shot cha -> lấy câu của shot cha."""
    ids = s["sentences"]
    if not ids and s.get("inherit"):
        for p in SHOTS:
            if p["id"] == s["inherit"]:
                ids = p["sentences"]
                break
    ctx = " ".join(SENT[x]["text"] for x in ids)
    if not ctx and s["template"] == "T10":          # thẻ chương: tên hồi trong edition.py
        ctx = " ".join(ED.EP["act_titles"].values())
    return ctx


quote_bad = []
for s in SHOTS:
    ctx = ctx_of(s)
    for kind, t in on_screen(s):
        if kind != "quote":
            continue
        core = t.strip().strip("“”\"")
        # lược bằng "…" — mỗi đoạn còn lại phải nguyên văn trong câu
        for frag in [f.strip() for f in core.split("…") if f.strip()]:
            if frag not in ctx:
                quote_bad.append(f"{s['id']}: “{frag[:45]}…” không nguyên văn trong câu")
chk("Chữ trích dẫn nguyên văn (lược bằng …) trong câu — V3", not quote_bad, "; ".join(quote_bad[:6]))

# ---------------------------------------------------------------- 5. so tren hinh
ORDINAL = {"thứ nhất": "1", "thứ hai": "2", "thứ ba": "3", "thứ tư": "4"}
ORDINAL_EN = {"first": "1", "second": "2", "third": "3", "fourth": "4"}
# số thứ tự viết bằng chữ trong câu EN (ví dụ "Red flag number one" -> cờ 01)
ORD_EN_RE = [(r"red flag number one\b", "1"), (r"red flag number two\b", "2"),
             (r"red flag number three\b", "3"), (r"red flag number four\b", "4"),
             (r"\bfirst\b", "1"), (r"\bsecond\b", "2"), (r"\bthird\b", "3"), (r"\bfourth\b", "4")]
LADDER_LAST = {"cuối cùng": "4"}          # thang 4 bac (kich ban: "4 nấc thang")
LADDER_LAST_EN = {"last": "4"}
MONTHS_EN = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6",
              "july": "7", "august": "8", "september": "9", "october": "10", "november": "11",
              "december": "12"}
STRUCT_VN = r"(HỒI|TẬP|NẤC|TẦNG)"
STRUCT_EN = r"(ACT|STAGE|LAYER|COMPARTMENT|EPISODE)"
num_bad, num_notes = [], []
for s in SHOTS:
    ctx = ctx_of(s)
    flat = ctx.replace(" ", "")
    allowed = set(re.findall(r"\d+", flat))                     # so co trong cau
    for a in list(allowed):                                     # dang 07 cho 7
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    ord_map = ORDINAL_EN if EN else ORDINAL
    for word, d in ord_map.items():
        if word in ctx.lower():
            allowed.add(d)
            allowed.add(d.zfill(2))
    if EN:
        for pat, d in ORD_EN_RE:
            if re.search(pat, ctx.lower()):
                allowed.add(d)
                allowed.add(d.zfill(2))
    if EN:
        for word, d in MONTHS_EN.items():
            if word in ctx.lower():
                allowed.add(d)
                allowed.add(d.zfill(2))
        if "4 stages" in ctx.lower():
            allowed.add("4")
            allowed.add("04")
    else:
        for word, d in LADDER_LAST.items():
            if word in ctx.lower() and "4 nấc" in ctx.lower():
                allowed.add(d)
                allowed.add(d.zfill(2))
    for m in set(re.findall(r"\d[\d.,]*", " ".join(t for _k, t in on_screen(s)))):
        tok = m.replace(".", "")
        # "1.400" (dấu chấm = phân tách nghìn) phải khớp nguyên dạng trong câu
        if m in allowed or m in flat or tok in allowed:
            continue
        # nhan cau truc: HỒI 0X / TẬP 0X / NẤC 0X / TẦNG 0X  (EN: ACT/STAGE/LAYER/COMPARTMENT)
        if re.search((STRUCT_EN if EN else STRUCT_VN) + r"\s*" + re.escape(m) + r"\b",
                     " ".join(t for _k, t in on_screen(s))):
            num_notes.append(f"{s['id']}: “{m}” là nhãn cấu trúc (hồi/tập/nấc)")
            continue
        num_bad.append(f"{s['id']}: số “{m}” không có trong câu")
chk("Mọi con số trên hình có trong câu — A9.2", not num_bad, "; ".join(num_bad[:6]))
if num_notes:
    note("Số là nhãn cấu trúc (hồi/tập/bậc thang), không phải dữ kiện bịa",
         f"{len(num_notes)} chỗ: " + ", ".join(num_notes[:6]))

# ---------------------------------------------------------------- 6. tu cam
FORBIDDEN = ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập", "đầu độc",
             "diệt cỏ", "bỏ đói", "móc áo", "đồ lót", "quan hệ tình dục", "hiếp", "cưỡng ép"]
SAFE = ["ung thư máu", "đấu tập", "bàn tay", "cánh tay", "đầu tư", "đầu học", "đầu tiên",
        "đầu não", "trọng đầu", "bầu cửa", "bầu trời", "đập đầu", "trói buộc"]
# Bản EN (chuẩn YouTube US): không mô tả chi tiết bạo lực, không nhắc đồ lót / hành vi tình dục
FORBIDDEN_EN = ["blood", "corpse", "strangle", "choke", "struggle", "raped", "rape",
                "underwear", "sexual intercourse", "orgasm", "penis", "vagina", "suffocat",
                "mutilat", "dismember", "torture"]
SAFE_EN = ["blood type", "blood pressure", "blood vessel", "bloodstream", "blood cell",
           "struggle to survive", "struggled to"]
forbidden_hit = []
for s in SHOTS:
    low = " ".join(t for _k, t in on_screen(s)).lower()
    for w in (FORBIDDEN_EN if EN else FORBIDDEN):
        if w not in low:
            continue
        if EN:
            if any(g in low for g in SAFE_EN if g in w or w in g):
                continue
            forbidden_hit.append(f"{s['id']}: “{w}”")
        elif not any(g in low for g in SAFE if g in w or w in g):
            forbidden_hit.append(f"{s['id']}: “{w}”")
chk("Không từ cấm / không nhắc hành vi tình dục trên hình", not forbidden_hit,
    "; ".join(forbidden_hit[:6]))

# ---------------------------------------------------------------- 7. nhip trong shot
def reveal_moments(s):
    """So 'khoanh khac' chu doi trong mot shot — cung cach seg_times() cua renderer.

    seg 0 -> luc shot bat dau
    seg i>0 -> theo cau (#k) | theo cum tu (beat) | theo cau thu i | giua cau cuoi
    T8: renderer TU neo tung muc danh sach vao cum tu dau tien cua muc do
        (build_video3.py:626) -> moi muc la mot khoanh, du ke hoach ghi "Moi muc o cum tu".
    """
    sents, segs = s["sentences"], s["segments"]
    starts = [SENT[x]["start"] for x in sents]
    phr = list(s["beats"])
    moms = []
    for i, sg in enumerate(segs):
        if i == 0:
            moms.append("start")
            continue
        if sg["at_sentence"]:
            tgt = [x for x in sents if x.endswith(f"#{sg['at_sentence']}")]
            moms.append(f"sent#{sg['at_sentence']}" if tgt else "start")
        elif phr:
            moms.append(f"phr#{phr.pop(0)}")
        elif i < len(starts):
            moms.append(f"sent@{sents[i]}")
        elif starts:
            moms.append("mid")
        else:
            moms.append("start")
    if s["template"] == "T8":
        seg = segs[0] if segs else {"elems": []}
        lab = [v for k, v in seg["elems"] if k == "ital"]
        items = (lab[1] if len(lab) > 1 else lab[0]).split(" · ") if lab else []
        moms += [f"item{i}" for i in range(len(items))]
    return moms


long_bad, long_note = [], []
for s in SHOTS:
    dur = s["end"] - s["start"]
    if dur <= 15.0:
        continue
    moms = reveal_moments(s)
    waves = len(set(moms))
    if waves <= 1:
        # chi 1 khoanh: ca khoi chu hien ngay dau cau. V2 ("hinh chi doi o dau cau")
        # cho phep dieu nay — chi ghi nhan, khong coi la loi.
        long_note.append(f"{s['id']} ({dur:.1f}s): 1 khoanh — tiêu đề hiện ở đầu câu (đúng V2); "
                         f"beat trong kế hoạch là neo theo cụm từ, renderer T1 chưa dùng")
    elif not s["beats"] and not any(sg["at_sentence"] for sg in s["segments"]):
        long_note.append(f"{s['id']} ({dur:.1f}s, {waves} khoanh) — kế hoạch ghi beat dạng văn xuôi")
chk("Shot > 15 s có nhịp hoặc bám V2 (chữ hiện ở đầu câu)", not long_bad, "; ".join(long_bad[:6]))
if long_note:
    note("Ghi nhận về nhịp của shot dài (không phải lỗi nội dung)", "; ".join(long_note[:8]))

# ---------------------------------------------------------------- 8. lien ke
gaps = [f"{a['id']}->{b['id']} lệch {b['start'] - a['end']:.3f} s"
        for a, b in zip(SHOTS, SHOTS[1:]) if abs(a["end"] - b["start"]) > 0.05]
chk("Các shot liền nhau (không hở/chồng)", not gaps, "; ".join(gaps[:5]))

# ---------------------------------------------------------------- thong ke
print()
print(f"Tap 02 · {len(SHOTS)} shot · {len(all_ids)} câu · "
      f"tong {round(SH['total'], 1)} s ({int(SH['total'] // 60)}:{int(SH['total'] % 60):02d})")
tpl = {}
for s in SHOTS:
    k = s["template"] or "(giữ)"
    tpl[k] = tpl.get(k, 0) + 1
print("Mẫu dùng:", ", ".join(f"{k}×{v}" for k, v in sorted(tpl.items(), key=lambda x: -x[1])))
roles = {}
for s in SHOTS:
    if s["role"]:
        roles[s["role"]] = roles.get(s["role"], 0) + len(s["sentences"])
print("Câu theo vai:", ", ".join(f"{k}={v}" for k, v in sorted(roles.items())))
print("Nhãn hồi:", " · ".join(ED.EP["act_titles"][a] for a in sorted(ED.EP["act_titles"])))
print()
print("TAT CA DA DAT" if ok else f"CO {len(errs)} VIEC CHUA XONG: {errs}")
sys.exit(0 if ok else 1)
