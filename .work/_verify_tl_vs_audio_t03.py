#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap03 VN — CỔNG: lời đọc trong audio có khớp câu của timeline tại đúng mốc thời gian.

Cách kiểm (không phụ thuộc thuật toán căn):
  Với MỖI câu trong timeline, lấy các đoạn ASR nằm trong cửa sổ
  [start-0.35, end+0.35] rồi so văn bản với câu đó.
  - Câu khớp  => audio đúng chỗ đang đọc đúng câu.
  - Câu lệch  => timeline sai mốc -> ảnh sẽ lệch tiếng.
Báo thêm độ lệch (ASR - timeline) của nhóm câu khớp để phát hiện TRƯỢT dần.
"""
import json
import re
import statistics
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
tl = json.loads((WORK / "timeline_s_t03.json").read_text(encoding="utf-8"))
recog = json.loads((WORK / "speech_full_recognized_vi_t03.json").read_text(encoding="utf-8"))
items = tl["items"]

WORD_RE = re.compile(r"[a-z0-9]+", re.I)


def toks(t):
    t = unicodedata.normalize("NFC", t or "").lower()
    return WORD_RE.findall(t)


def sim(a, b):
    if not a or not b:
        return 0.0
    A, B = set(a), set(b)
    if not (A & B):
        return 0.0
    return len(A & B) / (len(A | B) ** 0.5)


# ma hoa cau -> bo token, bo stopword de so dung
STOP = set("và của là có được cho trong với những một các như đã khi đến ra "
           "thì nhưng cũng để từ mà này người không khi".split())


def key(t):
    return [w for w in toks(t) if w not in STOP]


rec = [(r["start"], r["end"], r["text"], key(r["text"])) for r in recog]

rows = []
for it in items:
    a, b = it["start"] - 0.35, it["end"] + 0.35
    win = [r for r in rec if (r[0] + r[1]) / 2 > a and (r[0] + r[1]) / 2 < b]
    txt = " ".join(r[2] for r in win)
    kk = key(it["text"])
    s = sim(kk, key(txt))
    # do lech: mau tin dau trong cua so so voi start cua timeline
    d = (win[0][0] - it["start"]) if win else None
    rows.append({"id": it["id"], "act": it["act"], "start": it["start"], "end": it["end"],
                 "sim": s, "delta": d, "nseg": len(win), "text": it["text"]})

good = [r for r in rows if r["sim"] >= 0.55]
weak = [r for r in rows if 0.30 <= r["sim"] < 0.55]
bad = [r for r in rows if r["sim"] < 0.30]

print(f"Cau trong timeline : {len(rows)}")
print(f"  KHO' (sim>=0.55) : {len(good)}  ({100*len(good)/len(rows):.1f}%)")
print(f"  yeu (0.30-0.55)  : {len(weak)}  ({100*len(weak)/len(rows):.1f}%)")
print(f"  YEU/KHONG khop   : {len(bad)}  ({100*len(bad)/len(rows):.1f}%)")

dl = [r["delta"] for r in good if r["delta"] is not None]
if dl:
    print(f"\nDo lech (ASR - timeline) tren {len(dl)} cau khop:")
    print(f"  mean={statistics.mean(dl):+.3f}s  median={statistics.median(dl):+.3f}s  "
          f"min={min(dl):+.3f}s  max={max(dl):+.3f}s")
    for lim in (0.5, 1.0, 2.0):
        print(f"  |lech| > {lim}s : {sum(1 for d in dl if abs(d) > lim)}/{len(dl)}")
    n = len(dl)
    for frac in (0.25, 0.5, 0.75):
        seg = dl[:int(n * frac)]
        if seg:
            print(f"  trung binh trong {int(frac*100)}% dau: {statistics.mean(seg):+.3f}s")
    tail = dl[int(n * 0.75):]
    if tail:
        print(f"  trung binh trong 25% cuoi: {statistics.mean(tail):+.3f}s")
    # trượt tuần tự: so lech theo chi so
    drift = [dl[i + 1] - dl[i] for i in range(len(dl) - 1)]
    print(f"  buoc lech trung binh giua cac cau lien tiep: {statistics.mean(drift):+.4f}s")

print("\nCau KHONG khop (sim < 0.30) — xem lai:")
for r in bad[:30]:
    print(f"  {r['id']:>10s} t={r['start']:8.2f} sim={r['sim']:.2f} nseg={r['nseg']} "
          f"| {r['text'][:70]}")

# --- kiem tra moc hoi: sau ACT/NGHI phai co lai giọng
print("\nMoc hoi va ke tiep:")
for m in tl["markers"]:
    if m["type"] in ("ACT", "NGHI"):
        nxt = [i for i in items if i["start"] >= m["end"] - 0.05]
        first = nxt[0] if nxt else None
        gap = round(first["start"] - m["end"], 3) if first else None
        print(f"  {m['type']:4s} {m.get('act', m.get('id'))}: {m['start']:.2f}->{m['end']:.2f} | "
              f"cau sau: {first['id'] if first else '-'} start={first['start'] if first else '-'} gap={gap}")

print(f"\ntotal={tl['total']} | last item end={items[-1]['end']} | "
      f"duoi={tl['total'] - items[-1]['end']:.2f}s | ASR last end={recog[-1]['end']}")
