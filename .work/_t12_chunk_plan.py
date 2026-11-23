# -*- coding: utf-8 -*-
"""Tập 12 — lập kế hoạch TÁCH NỀN theo H25 (chặn trước khi viết prompt).

Nguyên lý (giống Tập 11 — A11 #165):
  - Mỗi lần xuất hiện LIỀN MẠCH của một mã nền trong bảng shot = 1 "cụm".
    Cùng mã nền dùng lại ở hồi khác (cách quãng) = cảnh khác ⇒ phải tách mã.
  - Mỗi cụm chia thành các nhóm ≤ 2 shot (≤ 3 shot nếu thời lượng cho phép),
    tổng ≤ 30 s (≤ 28 s nếu ngay sau là thẻ chuyển hồi vì cổng --plan gán
    thẻ "void" (+1 shot, +2 s) vào nền trước)  — A11 #166.
  - Nhóm đầu tiên của mã cũ GIỮ mã cũ (dùng lại ảnh đã có).
  - Các nhóm còn lại cần MÃ MỚI + ẢNH MỚI.

KHÁC BIỆT VỚI TẬP 11: Tập 12 CHƯA CÓ AUDIO ⇒ bảng shot không ghi "(x s)".
Thời lượng shot được ƯỚC LƯỢNG từ số từ trong cột "Chữ" bằng hệ số
SEC_PER_WORD hiệu chuẩn đo từ Tập 11 (audio thật):
  Tập 11 (218 câu, timeline thật): median 0,293 · p75 0,303 · p90 0,314 · max 0,340 s/từ
  => dùng 0,32 (trên p90) để ƯỚC LƯỢNG THẬN TRỌNG (thiên về nhiều giây hơn),
     cộng 0,5 s đệm cho mỗi shot.
Sau khi dựng audio thật, cổng --plan phải đo lại (H25: cổng thường ĐẠT sau
parse_shots.py).

Dùng: py -3 .work/_t12_chunk_plan.py [--check-t11]
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap12/KeHoach_Video_Tap12.md"
ROW = re.compile(r"^\|\s*([1-5]-\d+)\s*\|(.*)$")
SEC_PER_WORD = 0.32
PAD = 0.5

# kế hoạch Tập 11 để kiểm chéo thuật toán (có sẵn thời lượng thật)
T11_MD = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/KeHoach_Video_Tap11.md"


def parse(path, estimate=False):
    """Parse bảng shot. Nếu estimate=True và dòng không có '(x s)' thì ước lượng."""
    rows = []
    for line in open(path, encoding="utf-8"):
        m = ROW.match(line.rstrip("\n"))
        if not m:
            continue
        sid, rest = m.group(1), m.group(2)
        cells = [c.strip() for c in rest.split("|")]
        cau_raw = cells[0]
        durs = re.findall(r"\((\d+(?:[.,]\d+)?) ?s\)", cau_raw)
        dur = sum(float(x.replace(",", ".")) for x in durs)
        measured = bool(durs)
        cau = re.search(r"`([^`]+)`", cau_raw)
        bg = re.search(r"`(t\d+_[a-z0-9_]+)`", cells[3] if len(cells) > 3 else "")
        chu = cells[4] if len(cells) > 4 else ""
        is_card = bool(re.search(r"nghỉ chuyển hồi|hết tập", cau_raw))
        words = len(re.findall(r"\S+", chu))
        if not dur and estimate and words:
            dur = round(words * SEC_PER_WORD + PAD, 1)
        rows.append(dict(sid=sid, dur=dur, measured=measured,
                         cau=cau.group(1) if cau else cau_raw,
                         vai=cells[1] if len(cells) > 1 else "",
                         mau=cells[2] if len(cells) > 2 else "",
                         bg=bg.group(1) if bg else None,
                         cam=(re.findall(r"`([^`]+)`", cells[3])[-1]
                              if len(re.findall(r"`([^`]+)`", cells[3])) > 1 else ""),
                         chu=chu, words=words,
                         card=is_card, end_card=bool(re.search(r"hết tập", cau_raw))))
    return rows


def build(rows, max_shot_per_chunk=2, max_sec=30.0):
    """Tách thẻ kết (hết tập) ra; gom cụm liền mạch; chia nhóm ≤2 shot/≤30 s."""
    content = [r for r in rows if not r["card"]]
    end_card = next((r for r in rows if r["end_card"]), None)
    runs = []
    for r in content:
        if runs and runs[-1][0] == r["bg"]:
            runs[-1][1].append(r)
        else:
            runs.append((r["bg"], [r]))
    chunks = []
    for bg, rs in runs:
        i = 0
        ci = 0
        while i < len(rs):
            take, t = [], 0.0
            while i < len(rs) and len(take) < max_shot_per_chunk:
                r = rs[i]
                if take and t + r["dur"] > max_sec:
                    break
                take.append(r)
                t += r["dur"]
                i += 1
            ci += 1
            chunks.append(dict(parent=bg, run_bg=bg, run_idx=ci, rows=take,
                               sec=round(t, 1), n=len(take)))
    return chunks, end_card


def group_limit_before_card(rows, chunks):
    """Nhóm đứng ngay trước thẻ chuyển hồi phải ≤2 shot & ≤28 s (A11 #166)."""
    problems = []
    idx = {r["sid"]: i for i, r in enumerate(rows)}
    for c in chunks:
        last = c["rows"][-1]["sid"]
        nxt = rows[idx[last] + 1] if idx[last] + 1 < len(rows) else None
        if nxt and nxt["card"] and not nxt["end_card"]:
            if c["n"] + 1 > 3 or c["sec"] + 2 > 30:
                problems.append((c["parent"], last, c["n"], c["sec"]))
    return problems


def report(rows, chunks, end_card, label):
    used = collections.Counter()
    for c in chunks:
        used[c["parent"]] += 1
    new_needed = sum(v - 1 for v in used.values())
    dist = collections.Counter(c["n"] for c in chunks)
    print(f"\n===== {label} =====")
    print(f"dòng bảng shot: {len(rows)} · nội dung: {len([r for r in rows if not r['card']])}"
          f" · thẻ kết: {end_card['sid'] if end_card else None}")
    print(f"nhóm nền sau khi tách: {len(chunks)} (+1 thẻ kết) = {len(chunks) + 1} mã nền")
    print(f"phân bố shot/nhóm: {dict(sorted(dist.items()))}")
    print(f"mã cũ giữ nguyên: {len(used)} · MÃ MỚI cần sinh: {new_needed}")
    tot = sum(c["n"] for c in chunks)
    print(f"shot/nền = {tot / max(len(chunks), 1):.2f}")
    print(f"tổng thời lượng ước lượng: {sum(c['sec'] for c in chunks):.0f} s")
    bad = [(c["parent"], c["n"], c["sec"]) for c in chunks if c["n"] > 3 or c["sec"] > 30]
    print(f"vi phạm (≤3 shot & ≤30 s): {len(bad)} {bad[:8]}")
    return new_needed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-t11", action="store_true",
                    help="kiểm chéo thuật toán trên Tập 11 (kỳ vọng 136 nền / 70 mã mới)")
    args = ap.parse_args()

    if args.check_t11:
        rows11 = parse(T11_MD, estimate=False)
        chunks11, end11 = build(rows11)
        report(rows11, chunks11, end11, "TẬP 11 (thời lượng thật)")
        print("  kỳ vọng: 136 nền / 70 mã mới")

    rows = parse(MD, estimate=True)
    chunks, end_card = build(rows)
    new_needed = report(rows, chunks, end_card, "TẬP 12 (thời lượng ước lượng)")
    probs = group_limit_before_card(rows, chunks)
    print(f"nhóm sát thẻ chuyển hồi có nguy cơ vượt: {len(probs)} {probs[:8]}")

    out = dict(chunks=[dict(parent=c["parent"], run_idx=c["run_idx"], n=c["n"],
                             sec=c["sec"], sids=[r["sid"] for r in c["rows"]],
                             caus=[r["cau"] for r in c["rows"]],
                             chus=[r["chu"] for r in c["rows"]],
                             bg=c["parent"]) for c in chunks],
               end_card=end_card["sid"] if end_card else None,
               sec_per_word=SEC_PER_WORD, pad=PAD)
    Path(".work/_t12_chunks.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n-> .work/_t12_chunks.json")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
