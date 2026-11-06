#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 05 — ghi bảng shot MỚI vào KeHoach_Video_Tap05.md (và bản EN/JA).

Dùng:
  py -3 .work/_write_t05_table.py vi     # bảng VN
  py -3 .work/_write_t05_table.py en     # bảng EN
  py -3 .work/_write_t05_table.py ja     # bảng JA

Nguyên tắc:
  * Cột Shot  : ID MỚI (skeleton) — META cũng đánh số lại để không trùng.
  * Cột Câu   : sinh lại từ skeleton (theo kịch bản mới).
  * Cột Chữ   : lớp phủ mới của từng ngôn ngữ (META giữ chữ cũ của bản đó).
  * Cột còn lại (Vai/Mẫu/Nền/Beat/Nhân vật): lấy từ BẢN CŨ CỦA CHÍNH NGÔN NGỮ ĐÓ
    (không dùng bản VN cho bản EN/JA) — dòng mới 3.09/3.10 thì lấy từ skeleton.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
LANG = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()

TARGET = {
    "vi": (ROOT / "02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md", "_t05_chu_vi.json"),
    "en": (ROOT / "02_SAN_XUAT/Tap05_EN/KeHoach_Video_Tap05_EN.md", "_t05_chu_en.json"),
    "ja": (ROOT / "02_SAN_XUAT/Tap05_JA/KeHoach_Video_Tap05_JA.md", "_t05_chu_ja.json"),
}[LANG]
PLAN, CHU_FILE = TARGET
sk = json.loads((W / "_t05_skeleton.json").read_text(encoding="utf-8"))
CHU = json.loads((W / CHU_FILE).read_text(encoding="utf-8"))
# beat của dòng MỚI (3.09/3.10) — chỉ có ở bản VN, cần dịch cho EN/JA
BEAT_EXTRA = {}
bx = W / f"_t05_beat_extra_{LANG}.json"
if bx.exists():
    BEAT_EXTRA = json.loads(bx.read_text(encoding="utf-8"))


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def read_old_rows(path):
    """Đọc bảng shot CŨ của bản này -> {old_id: cells}.

    QUAN TRỌNG: đọc từ snapshot JSON (chụp từ git HEAD), KHÔNG đọc từ file đích —
    nếu đọc file đích thì lần chạy sau lấy bảng đã ghi làm "bảng cũ" => dòng dịch chuyển.
    """
    snap = W / f"_t05_old_rows_{LANG}.json"
    if snap.exists():
        data = json.loads(snap.read_text(encoding="utf-8"))
        return data["rows"]
    raise SystemExit(f"thiếu snapshot {snap.name} — chạy: py -3 .work/_t05_snapshot.py")


OLD = read_old_rows(PLAN)


def esc(cell):
    return cell.replace("|", "\\|").strip()


def cau_of(r):
    if r["kind"] != "shot":
        return None
    eid, a, b = r["spans"][0]
    return f"`{eid}#{a}`" if a == b else f"`{eid}#{a}`–`#{b}`"


lines, acts = [], {}
used_old = set()
for r in sk["rows"]:
    sid = r["sid"]
    src = r["from"]
    if src in OLD:
        c = list(OLD[src])
        used_old.add(src)
    else:
        c = list(r["cells"]) + [""] * 9
        c = c[:9]
    c[0] = sid
    if r["kind"] == "shot":
        c[1] = cau_of(r)
        if sid not in CHU:
            raise SystemExit(f"thiếu chữ cho shot {sid}")
        c[5] = CHU[sid]
        if sid in BEAT_EXTRA:
            c[6] = BEAT_EXTRA[sid]
    # META: giữ nguyên chữ + beat của bản gốc của ngôn ngữ này
    lines.append("| " + " | ".join(esc(x) for x in c) + " |")
    act = sid.split("-")[0]
    acts[act] = acts.get(act, 0) + 1

head = ("| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |\n"
        "|---|---|---|---|---|---|---|---|---|")
body = "\n".join(lines)
n_shot = sum(1 for r in sk["rows"] if r["kind"] == "shot")
n_sent = sum(r["spans"][0][2] - r["spans"][0][1] + 1 for r in sk["rows"] if r["kind"] == "shot")
tot = (f"**Tổng: {n_shot} shot** (Hồi 1: {acts['1']} shot · Hồi 2: {acts['2']} shot · "
       f"Hồi 3: {acts['3']} shot · Hồi 4: {acts['4']} shot · Hồi 5: {acts['5']} shot) · "
       f"Phủ 100% {n_sent}/{n_sent} câu · chữ trên hình lấy từ câu đang đọc (H6).")

text = PLAN.read_text(encoding="utf-8")
i = text.find("## 6. DANH SÁCH SHOT")
if i < 0:
    raise SystemExit("không tìm thấy mục 6")
j = text.find("**Tổng:", i)
if j < 0:
    raise SystemExit("không tìm thấy dòng Tổng")
k = text.find("\n", j)
new_sec = (f"## 6. DANH SÁCH SHOT — TẬP 05 "
           f"(dựng lại 05/11/2026 theo kịch bản v4 — 209 câu, {n_sent} câu phủ)\n\n"
           f"{head}\n{body}\n\n{tot}\n")
# text[k:] bắt đầu bằng '\n' -> bỏ đi để không chồng dòng trống khi chạy lại
text = text[:i] + new_sec + text[k + 1:]
PLAN.write_text(text, encoding="utf-8", newline="\n")

ids = [r["sid"] for r in sk["rows"]]
dup = [x for x in set(ids) if ids.count(x) > 1]
print(f"[{LANG}] ghi {PLAN.name}: {n_shot} shot · {n_sent} câu · "
      f"dòng {len(ids)} · ID trùng {len(dup)} {dup if dup else ''}")
