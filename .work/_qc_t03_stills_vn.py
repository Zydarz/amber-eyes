#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap03 VN — CỔNG QC ẢNH TĨNH (H9/H10/H12/H13/V3/A9.2).

Cổng:
  G1  Đủ ảnh: đúng 1 PNG cho mỗi shot, không thiếu, không thừa
  G2  Ảnh hợp lệ: mở được, 1920x1080, >= 20 KB
  G3  H13 khớp 3 chiều: chữ VẼ trên hình tại thời điểm của ảnh tĩnh phải truy
      được về câu đang ĐỌC đúng lúc đó (số trên hình phải có trong câu;
      câu trích phải nguyên văn)
  G4  H12 thẻ kết: có nhãn + tên kênh + khẩu hiệu
  G5  H10: thời lượng shot + chuỗi nền liền nhau
  G6  Badge vai có sóng âm (stem thật) — không được là đường gạch phẳng
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
import os
os.environ.setdefault("AE_EP", "03")
os.environ.setdefault("AE_LANG", "vi")
import build_video3 as BV  # noqa: E402

SH = BV.SH
TL = BV.TL
SENT = BV.SENT
STILLS = WORK / "video3_t03" / "stills"
fails = []

# ---------------------------------------------------------------- G1 đủ ảnh
ids = [s["id"] for s in SH]
files = {p.name for p in STILLS.glob("*.png")}
want = {f"shot_{i}.png" for i in ids}
miss, extra = sorted(want - files), sorted(files - want)
print(f"[G1] ảnh: {len(files)} file · cần {len(want)}")
if miss:
    print(f"     ✗ THIẾU {len(miss)}: {miss[:8]}")
    fails.append("G1")
if extra:
    print(f"     ✗ THỪA {len(extra)}: {extra[:8]}")
    fails.append("G1")
if not miss and not extra:
    print("     ✔ đủ ảnh, không thừa")
dup = [i for i in set(ids) if ids.count(i) > 1]
if dup:
    print(f"     ✗ ID shot trùng: {dup}")
    fails.append("G1")

# ---------------------------------------------------------------- G2 ảnh hợp lệ
bad = []
for n in sorted(want & files):
    p = STILLS / n
    if p.stat().st_size < 20000:
        bad.append((n, f"nhỏ {p.stat().st_size}B"))
        continue
    try:
        with Image.open(p) as im:
            im.verify()
        with Image.open(p) as im:
            if im.size != (1920, 1080):
                bad.append((n, f"size {im.size}"))
    except Exception as e:
        bad.append((n, f"lỗi mở: {e}"))
print(f"[G2] ảnh hỏng/sai kích thước: {len(bad)} {bad[:5] if bad else ''}")
if bad:
    fails.append("G2")

# ---------------------------------------------------------------- G3 khớp 3 chiều
NUM_RE = re.compile(r"\d[\d.,]*")
FOLD = {"0": "0"}


def norm_txt(t):
    t = unicodedata.normalize("NFC", t or "")
    t = t.replace("“", '"').replace("”", '"').replace("’", "'")
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def nums_in(t):
    out = set()
    for m in NUM_RE.findall(norm_txt(t)):
        raw = m.rstrip(".,")
        out.add(raw)
        # "145" -> "145"; "0,13%" -> "0,13" và "13"
        out.add(raw.replace(",", "."))
        if raw.replace(",", "").isdigit():
            out.add(raw.replace(",", ""))
    return {x for x in out if x}


def sent_at(t):
    """Câu đang đọc tại thời điểm t (theo timeline)."""
    best = None
    for it in TL["items"]:
        if it["start"] - 0.05 <= t <= it["end"] + 0.05:
            best = it
            break
    return best


# ---- theo ĐÚNG quy tắc cổng dự án (_qc_tap02_shots.py):
#      ngữ cảnh = các câu của shot (dòng "giữ" mượn của shot cha;
#      thẻ tiêu đề không có câu -> lấy tên hồi trong edition.py)
#      số trên hình phải có trong ngữ cảnh, TRỪ nhãn cấu trúc HỒI/TẬP/NẤC/TẦNG.
def ctx_of(s):
    ids = s["sentences"]
    if not ids and s.get("inherit"):
        for p in SH:
            if p["id"] == s["inherit"]:
                ids = p["sentences"]
                break
    ctx = " ".join(SENT[x]["text"] for x in ids)
    if not ctx and (s.get("template") == "T10" or not s.get("sentences")):
        ctx = " ".join(BV.ED.EP["act_titles"].values())
    return ctx


STRUCT_ANY = r"(?:HỒI|TẬP|NẤC|TẦNG)"
ORDINAL = {"thứ nhất": "1", "thứ hai": "2", "thứ ba": "3", "thứ tư": "4"}

print("[G3] chữ trên hình vs câu của shot (V3 + A9.2)")
g3_bad, g3_rows, struct_notes = [], [], 0
for s in SH:
    ctx = ctx_of(s)
    flat = ctx.replace(" ", "")
    allowed = set(re.findall(r"\d+", flat))
    for a in list(allowed):
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    for word, d in ORDINAL.items():
        if word in ctx.lower():
            allowed.add(d)
            allowed.add(d.zfill(2))
    screen = " ".join(str(e[1]) for seg in s.get("segments") or [] for e in seg.get("elems", []) if len(e) >= 2)
    # số trên hình
    miss_n = []
    for m in set(re.findall(r"\d[\d.,]*", screen)):
        tok = m.replace(".", "")
        # đúng quy tắc cổng dự án: số có trong câu (kể cả nguyên dạng "1.600")
        if m in allowed or m in flat or tok in allowed:
            continue
        if re.search(STRUCT_ANY + r"\s*" + re.escape(m) + r"\b", screen):
            struct_notes += 1
            continue
        miss_n.append(m)
    # câu trích phải nguyên văn trong câu của shot (cho phép lược bằng …)
    quote_bad = []
    for seg in s.get("segments") or []:
        for kind, t in seg.get("elems", []):
            if kind != "quote":
                continue
            core = str(t).strip().strip("“”\"")
            for frag in [f.strip() for f in core.split("…") if f.strip()]:
                if frag not in ctx:
                    quote_bad.append(frag[:50])
    ok = not miss_n and not quote_bad
    g3_rows.append((s["id"], ok))
    if not ok:
        g3_bad.append((s["id"], screen[:60], miss_n, quote_bad))

print(f"     shot có chữ được kiểm: {len(g3_rows)} · sai: {len(g3_bad)}")
for b in g3_bad[:15]:
    print(f"     ✗ {b[0]} | hình: {b[1]!r} | số thiếu {b[2]} | trích {b[3]}")
if struct_notes:
    print(f"     (GHI) {struct_notes} số là nhãn cấu trúc hồi/tập — không tính lỗi")
if g3_bad:
    fails.append("G3")
else:
    print("     ✔ mọi số trên hình đều truy được về câu của shot; không câu trích sai")

# ---- phần đối chiếu "ảnh tĩnh nào đang hiện khi đọc câu nào"
#      Ảnh của shot X chỉ được chiếu khi chính câu của shot X đang được đọc.
print("[G3b] ảnh tĩnh: câu đang đọc có thuộc shot không")
mismatch = []
for s in SH:
    t_mid = (s["start"] + s["end"]) / 2
    spoken = sent_at(t_mid)
    if spoken is None:
        continue
    own = list(s["sentences"])
    if not own and s.get("inherit"):
        for p in SH:
            if p["id"] == s["inherit"]:
                own = list(p["sentences"])
                break
    if not own:
        continue          # thẻ tiêu đề / dòng giữ: không có câu riêng
    if spoken["id"] not in own:
        mismatch.append((s["id"], spoken["id"], spoken["text"][:50]))
print(f"     ảnh hiện khi đang đọc câu KHÔNG thuộc shot: {len(mismatch)}")
for m in mismatch[:10]:
    print(f"     ✗ shot {m[0]} đang hiện lúc đọc {m[1]} :: {m[2]!r}")
if mismatch:
    fails.append("G3b")
else:
    print("     ✔ mọi ảnh tĩnh hiện đúng lúc câu của nó được đọc")

# ---------------------------------------------------------------- G4 thẻ kết
last = SH[-1]
drawn = " ".join(str(e[1]) for seg in last.get("segments") or [] for e in seg.get("elems", []) if len(e) >= 2)
print(f"[G4] thẻ kết [{last['id']}] template={last.get('template')}")
print(f"     chữ: {drawn!r}")
need = ["HỒ SƠ TẬP", "AMBER EYES", "Phân tích tâm lý tội phạm"]
mn = [k for k in need if k.upper() not in drawn.upper()]
if mn:
    print(f"     ✗ thiếu: {mn}")
    fails.append("G4")
else:
    print("     ✔ có nhãn + tên kênh + khẩu hiệu")

# ---------------------------------------------------------------- G5 H10
durs = [(s["id"], round(s["end"] - s["start"], 2)) for s in SH]
out_of = [(i, d) for i, d in durs if d < 3 or d > 15]
chain, cur, curid = [], [], None
for s in SH:
    if s.get("bg") == curid:
        cur.append(s["id"])
    else:
        if len(cur) > 4:
            chain.append(cur)
        cur, curid = [s["id"]], s.get("bg")
if len(cur) > 4:
    chain.append(cur)
print(f"[G5] H10 thời lượng: min {min(d for _, d in durs)}s · max {max(d for _, d in durs)}s · ngoài 3–15s: {len(out_of)}")
print(f"     nền lặp liền >4 shot: {len(chain)} chuỗi {[len(c) for c in chain]}")
if chain:
    fails.append("G5")

# ---------------------------------------------------------------- G6 sóng âm badge
import wave
import numpy as np
print("[G6] sóng âm trên badge vai (stem theo vai)")
stems_ok = True
for role in ("H", "D", "C", "N1", "N2"):
    p = WORK / "stems_t03" / f"{role}.wav"
    if not p.exists():
        print(f"     ✗ thiếu stem {role}.wav")
        stems_ok = False
        continue
    with wave.open(str(p)) as wf:
        x = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    voiced = x[np.abs(x) > 0.01]
    env = np.abs(voiced)
    # sóng phải biến động (không phải đường thẳng): so tỉ lệ đỉnh RMS theo cửa sổ
    if len(env) < 1000:
        print(f"     ✗ {role}: gần như không có tiếng")
        stems_ok = False
        continue
    k = max(1, len(env) // 200)
    blocks = env[:200 * k].reshape(-1, k).max(axis=1)
    var = float(np.std(blocks) / (np.mean(blocks) + 1e-9))
    print(f"     {role:2s}: voiced {len(voiced)/16000:7.1f}s · biến động {var:5.2f} "
          f"{'✔' if var > 0.05 else '✗ phẳng'}")
    if var <= 0.05:
        stems_ok = False
if not stems_ok:
    fails.append("G6")

print("=" * 78)
print("KẾT LUẬN:", "ĐẠT" if not fails else f"LỖI: {sorted(set(fails))}")
sys.exit(0 if not fails else 1)
