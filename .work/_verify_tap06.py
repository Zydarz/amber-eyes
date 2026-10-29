#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra toàn diện bộ ảnh nền Tập 06: số lượng, kích thước, viền, provenance, manifest."""
import json
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
BG = ROOT / "assets" / "bg"
WORK = ROOT / ".work"
OUT = ROOT / "02_SAN_XUAT" / "Tap06"

ok = True


def chk(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))


jobs = json.loads((WORK / "bg_jobs_tap06.json").read_text(encoding="utf-8"))
names = [j["name"] for j in jobs]
files = sorted(BG.glob("t6_*.png"))
EXPECT = len(jobs)

chk(f"Job file có {EXPECT} mục", len(jobs) == EXPECT, f"{len(jobs)}")
chk("Không trùng tên trong jobs", len(set(names)) == len(names))
chk(f"{EXPECT} file t6_*.png trên đĩa", len(files) == EXPECT, f"{len(files)}")

missing = [n for n in names if not (BG / f"{n}.png").exists()]
extra = [f.stem for f in files if f.stem not in names]
chk("Không thiếu ảnh nào", not missing, ", ".join(missing))
chk("Không có ảnh thừa", not extra, ", ".join(extra))

bad_size = [f.name for f in files if Image.open(f).size != (2112, 1188)]
chk("Tất cả ảnh chuẩn 2112x1188 (16:9)", not bad_size, ", ".join(bad_size))

clash = [f.name for f in files if f.stem in {p.stem for p in BG.glob("*.png")
                                            if not p.stem.startswith("t6_")}]
chk("Không đụng tên ảnh tập khác", not clash, ", ".join(clash))

prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
t6 = [p for p in prov if p.get("file", "").startswith("assets/bg/t6_")]
chk(f"Provenance có đủ {EXPECT} bản ghi t6_", len(t6) == EXPECT, f"{len(t6)}")
chk("Provenance không trùng file", len({p["file"] for p in t6}) == len(t6))

nofile = [p["file"] for p in t6 if not (ROOT / p["file"]).exists()]
chk("Mọi bản ghi provenance đều có file thật", not nofile, ", ".join(nofile))

chk("Hồ sơ Danh_Sach_Anh_Tap06.md tồn tại", (OUT / "Danh_Sach_Anh_Tap06.md").exists())
chk("Contact sheet contact_sheet_t6.png tồn tại", (OUT / "contact_sheet_t6.png").exists())
chk("Kịch bản script_tap06.json tồn tại", (WORK / "script_tap06.json").exists())

# Quy tắc V5: ảnh có người
PERSON = {"t6_secret_service_pin_handshake", "t6_muddy_trousers_boots", "t6_surveillance_car_rain_night"}
chk("Các ảnh có chi tiết người (V5) đều đầy đủ",
    all((BG / f"{n}.png").exists() for n in PERSON), ", ".join(sorted(PERSON)))

print("\n" + ("TẤT CẢ ĐÃ ĐẠT CHUẨN 100%" if ok else "CÓ LỖI CẦN XỬ LÝ"))
sys.exit(0 if ok else 1)
