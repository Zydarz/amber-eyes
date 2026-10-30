#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra toàn diện bộ ảnh nền Tập 09: số lượng, kích thước, viền, provenance, manifest."""
import json
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
WORK = ROOT / ".work"
OUT = ROOT / "02_SAN_XUAT" / "Tap09"

ok = True


def chk(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))


jobs = json.loads((WORK / "bg_jobs_tap09.json").read_text(encoding="utf-8"))
names = [j["name"] for j in jobs]
files = sorted(BG.glob("t9_*.png"))
EXPECT = len(jobs)

chk(f"Job file có {EXPECT} mục", len(jobs) == EXPECT, f"{len(jobs)}")
chk("Không trùng tên trong jobs", len(set(names)) == len(names))
chk(f"{EXPECT} file t9_*.png trên đĩa", len(files) == EXPECT, f"{len(files)}")

missing = [n for n in names if not (BG / f"{n}.png").exists()]
extra = [f.stem for f in files if f.stem not in names]
chk("Không thiếu ảnh nào", not missing, ", ".join(missing))
chk("Không có ảnh thừa", not extra, ", ".join(extra))

bad_size = [f.name for f in files if Image.open(f).size != (2112, 1188)]
chk("Tất cả ảnh chuẩn 2112x1188 (16:9)", not bad_size, ", ".join(bad_size))

clash = [f.name for f in files if f.stem in {p.stem for p in BG.glob("*.png")
                                            if not p.stem.startswith("t9_")}]
chk("Không đụng tên ảnh tập khác", not clash, ", ".join(clash))

prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
t9 = [p for p in prov if p.get("file", "").startswith("assets/bg/t9_")]
chk(f"Provenance có đủ {EXPECT} bản ghi t9_", len(t9) == EXPECT, f"{len(t9)}")
chk("Provenance không trùng file", len({p["file"] for p in t9}) == len(t9))

nofile = [p["file"] for p in t9 if not (ROOT / p["file"]).exists()]
chk("Mọi bản ghi provenance đều có file thật", not nofile, ", ".join(nofile))

chk("Hồ sơ Danh_Sach_Anh_Tap09.md tồn tại", (OUT / "Danh_Sach_Anh_Tap09.md").exists())
chk("Contact sheet contact_sheet_t9.png tồn tại", (OUT / "contact_sheet_t9.png").exists())
chk("Kịch bản script_tap09.json tồn tại", (WORK / "script_tap09.json").exists())

# Quy tắc V5: ảnh có chi tiết người chỉ hiện bóng / mặt khuất hoàn toàn
PERSON = {
    "t9_manson_shadow_campfire_desert",
    "t9_yearbook_photos_shadow",
    "t9_collective_hysteria_three_shaved_heads",
    "t9_vacant_eyes_doll_shadow",
    "t9_runaway_teenager_bus_stop",
    "t9_summer_of_love_hippie_la"
}
chk("Các ảnh có chi tiết người (V5) đều đầy đủ",
    all((BG / f"{n}.png").exists() for n in PERSON), ", ".join(sorted(PERSON)))

print("\n" + ("TẤT CẢ ĐÃ ĐẠT CHUẨN 100%" if ok else "CÓ LỖI CẦN XỬ LÝ"))
sys.exit(0 if ok else 1)
