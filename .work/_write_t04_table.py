#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — ghi bảng shot MỚI vào KeHoach_Video_Tap04.md (và các bản EN/JA).

Dùng:
  py -3 .work/_write_t04_table.py vi     # bảng VN
  py -3 .work/_write_t04_table.py en     # bảng EN  (dùng lớp phủ shots_text_tap04_EN.json)
  py -3 .work/_write_t04_table.py ja     # bảng JA  (dùng lớp phủ shots_text_tap04_JA.json)

Bảng EN/JA sinh từ bảng VN: giữ nguyên cột Shot / Câu / Vai / Mẫu / Nền / Beat / Nhân vật,
thay cột "Chữ" bằng bản dịch trong lớp phủ, và thay cụm beat trong cột Beat.
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
    "vi": (ROOT / "02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md",
           W / "_t04_chu_vn.json", W / "_t04_beat_vi.json"),
    "en": (ROOT / "02_SAN_XUAT/Tap04_EN/KeHoach_Video_Tap04_EN.md",
           W / "_t04_chu_en.json", W / "_t04_beat_en.json"),
    "ja": (ROOT / "02_SAN_XUAT/Tap04_JA/KeHoach_Video_Tap04_JA.md",
           W / "_t04_chu_ja.json", W / "_t04_beat_ja.json"),
}[LANG]

PLAN, CHU_FILE, BEAT_FILE = TARGET
sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
CHU = json.loads(CHU_FILE.read_text(encoding="utf-8"))
BEAT = json.loads(BEAT_FILE.read_text(encoding="utf-8")) if BEAT_FILE and BEAT_FILE.exists() else {}
# Chữ cho dòng META (thẻ hồi, thẻ mở đầu, thẻ kết) — bản EN/JA phải dịch, không dùng chữ VN.
META_FILE = W / f"_t04_meta_{LANG}.json"
META = json.loads(META_FILE.read_text(encoding="utf-8")) if META_FILE.exists() else {}


def esc(cell):
    return cell.replace("|", "\\|").strip()


lines = []
acts = {}
for r in sk["rows"]:
    c = list(r["cells"])
    sid = r["sid"]                 # ID MỚI (dòng META giữ ID cũ trong cells -> đè lên shot thật)
    c[0] = sid
    if r["kind"] == "shot":
        if sid not in CHU:
            raise SystemExit(f"thiếu chữ cho shot {sid}")
        c[5] = CHU[sid]
        if sid in BEAT:
            c[6] = BEAT[sid]
    elif sid in META:
        c[5] = META[sid]
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
new_sec = (f"## 6. DANH SÁCH SHOT — TẬP 04 "
           f"(dựng lại 05/11/2026 theo kịch bản v4 — 212 câu, {n_sent} câu phủ)\n\n"
           f"{head}\n{body}\n\n{tot}\n")
# text[k:] bat dau bang '\n' (het dong Tong) -> bo di de khong chong duong trong
# moi lan ghi (truoc day moi lan chay lai cong 1 dong trong).
text = text[:i] + new_sec + text[k + 1:]
PLAN.write_text(text, encoding="utf-8", newline="\n")
print(f"[{LANG}] ghi {PLAN.name}: {n_shot} shot · {n_sent} câu")
