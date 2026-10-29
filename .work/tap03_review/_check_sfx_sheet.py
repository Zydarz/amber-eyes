#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra bảng âm thanh theo ĐÚNG quy tắc của build_audio3.py::place_sheet().

  ambience    : [từ câu, đến câu, file, dB]  → cả 2 mốc PHẢI là mã câu (có trong `sent`)
  cues        : [mốc, where, off, file, dB]  → mốc PHẢI là mã câu HOẶC element SFX/BGM/NGHI (có `id` trong markers)
  music_drop  : [từ câu, đến câu]            → cả 2 mốc PHẢI là mã câu
  file        : tồn tại dưới assets/sfx/ (tên có tiền tố thư mục) hoặc assets/sfx/t2/<tên trần>

Dùng: py -3 .work/tap03_review/_check_sfx_sheet.py [tap03]
"""
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
SFX = ROOT / "assets" / "sfx"
PARSED = json.loads((ROOT / ".work" / "tap03_review" / "parsed_final.json").read_text(encoding="utf-8"))

# mô phỏng đúng timeline của build_audio3.py
sent = {}
for e in PARSED:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sent[s["id"]] = s
markers = {e["id"] for e in PARSED if e["kind"] in ("SFX", "BGM", "NGHI")}


def file_ok(name):
    if (SFX / name).exists():
        return True
    if "/" not in name and (SFX / "t2" / name).exists():
        return True
    return False


def check_sheet(path, label):
    sheet = json.loads(path.read_text(encoding="utf-8"))
    err = []
    used = set()

    print(f"\n===== {label} =====")
    print("--- AMBIENCE (mốc phải là mã câu) ---")
    for a, b, f, db in sheet.get("ambience", []):
        used.add(f)
        bad = []
        if a not in sent:
            bad.append(f"'{a}' khong phai ma cau")
        if b not in sent:
            bad.append(f"'{b}' khong phai ma cau")
        if not file_ok(f):
            bad.append(f"thieu file {f}")
        if db > -6:
            bad.append(f"qua to ({db} dB)")
        err += [f"ambience {a}->{b} {f}: " + "; ".join(bad)] if bad else []
        print(f"  {a:<10} -> {b:<10} {f:<32} {db:>4} dB  {'OK' if not bad else 'LOI: ' + '; '.join(bad)}")

    print("--- CUES (mốc = ma cau HOAC element SFX/BGM/NGHI) ---")
    for ref, where, off, f, db in sheet.get("cues", []):
        used.add(f)
        bad = []
        if ref not in sent and ref not in markers:
            bad.append(f"'{ref}' khong phai ma cau va khong phai marker")
        if where not in ("start", "end"):
            bad.append(f"where='{where}' sai")
        if not file_ok(f):
            bad.append(f"thieu file {f}")
        err += [f"cue {ref} {f}: " + "; ".join(bad)] if bad else []
        print(f"  {ref:<10} {where:<6} {off:+.2f}s {f:<32} {db:>4} dB  {'OK' if not bad else 'LOI: ' + '; '.join(bad)}")

    print("--- MUSIC DROP (mốc phải là mã câu) ---")
    for a, b in sheet.get("music_drop", {}).get("ranges", []):
        bad = []
        if a not in sent:
            bad.append(f"'{a}' khong phai ma cau")
        if b not in sent:
            bad.append(f"'{b}' khong phai ma cau")
        err += [f"music_drop {a}->{b}: " + "; ".join(bad)] if bad else []
        print(f"  {a:<10} -> {b:<10} {'OK' if not bad else 'LOI: ' + '; '.join(bad)}")

    t3 = SFX / "t3"
    if t3.exists():
        for p in sorted(t3.glob("*.wav")):
            rel = f"t3/{p.stem}.wav"
            if rel not in used:
                err.append(f"file {rel} khong duoc dung trong bang")
                print(f"  [canh bao] {rel} khong dung")

    print(f"\nTong file tham chieu: {len(used)} · loi: {len(err)}")
    for e in err:
        print("  !!", e)
    return err


errs = check_sheet(ROOT / ".work" / "sfx_tap03.json", "TAP 03")
print("\nKET QUA:", "SACH" if not errs else f"{len(errs)} LOI")
sys.exit(0 if not errs else 1)
