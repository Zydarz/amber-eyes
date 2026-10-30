#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đưa 2 track BGM tải từ YouTube Audio Library vào assets/bgm/ + ghi provenance.

Nguồn:
  bgm_guitar_acoustic_60s  <- "Jewelry Box - Tim Bluhm.mp3" (Chrome tự thêm hậu tố nghệ sĩ)
  bgm_church_organ         <- "bgm_church_organ.mp3" trong inbox sfx_youtube
"""
import io
import json
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
DL = Path.home() / "Downloads"
BGM = ROOT / "assets" / "bgm"
PROV = ROOT / "provenance.json"
MAP = ROOT / ".work" / "yt_map.tsv"
STATE = ROOT / ".work" / "yt_watch_state.json"
NGAY = "2026-10-24"

DIEU_KHOAN = ("YouTube Audio Library — miễn phí dùng trong video/nội dung do chính kênh sáng tạo; "
              "KHÔNG được cung cấp, phân phối hoặc phát hành riêng file âm thanh")
KIEM_TM = "đạt (có điều kiện: chỉ dùng trong video của kênh, không phát hành riêng file)"

PLAN = [
    {
        "ma": "bgm_guitar_acoustic_60s",
        "src": DL / "Jewelry Box - Tim Bluhm.mp3",
        "track": "Jewelry Box",
        "file_ten": "Jewelry Box - Tim Bluhm.mp3",
        "the_loai": "Nhạc đồng quê và dân gian",
        "mo_ta": "guitar acoustic fingerpicked mộc mạc (nền Hồi 1 T09, sẽ xử lý thêm để u tối)",
    },
    {
        "ma": "bgm_church_organ",
        "src": INBOX / "bgm_church_organ.mp3",
        "track": "Sinister Cathedral",
        "file_ten": "bgm_church_organ.mp3",
        "the_loai": "Không gian xung quanh",
        "mo_ta": "organ nhà thờ u tối (nền Hồi 1 T16)",
    },
]

BGM.mkdir(parents=True, exist_ok=True)
prov = json.load(io.open(PROV, encoding="utf-8"))
prov = [e for e in prov if not str(e.get("file", "")).startswith("assets/bgm/"
                                                             + "bgm_guitar_acoustic_60s")
        and not str(e.get("file", "")).startswith("assets/bgm/bgm_church_organ")]

for p in PLAN:
    src = p["src"]
    if not src.exists():
        print("!! KHONG tim thay nguon: %s" % src)
        continue
    dst = BGM / (p["ma"] + ".mp3")
    if dst.exists():
        dst.unlink()
    shutil.move(str(src), str(dst))
    entry = {
        "file": "assets/bgm/%s.mp3" % p["ma"],
        "loai": "nhạc nền (BGM)",
        "cong_cu": ("YouTube Audio Library (YouTube Studio → Thư viện âm thanh) — tải tay, "
                    "đặt vào assets/bgm/ (file gốc: %s)" % p["file_ten"]),
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "mo_ta": p["mo_ta"],
        "font": None,
        "dieu_khoan": DIEU_KHOAN,
        "kiem_tra_thuong_mai": KIEM_TM,
        "track_youtube": p["track"],
        "the_loai_youtube": p["the_loai"],
        "nguon_goc": p["file_ten"],
    }
    prov.append(entry)
    print("OK  %-26s -> %s  (%d bytes)" % (p["ma"], dst.name, dst.stat().st_size))

json.dump(prov, io.open(PROV, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("--- provenance.json hien co %d muc ---" % len(prov))

# dong manifest: sua ten track cho khop ten file that + danh dau da dung
lines = MAP.read_text(encoding="utf-8-sig").splitlines()
out = []
for ln in lines:
    p = ln.split("\t")
    if len(p) >= 2 and p[1].strip() == "bgm_guitar_acoustic_60s":
        p[0] = "Jewelry Box - Tim Bluhm"
        ln = "\t".join(p)
    out.append(ln)
MAP.write_text("\n".join(out) + "\n", encoding="utf-8")

st = json.loads(STATE.read_text(encoding="utf-8"))
u = set(st.get("used", []))
for p in PLAN:
    u.add(p["ma"])
st["used"] = sorted(u)
STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
print("state used =", len(u))
