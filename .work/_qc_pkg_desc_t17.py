# -*- coding: utf-8 -*-
"""Kiểm tra pipeline: package.description() cho Tập 17 (4 ngôn ngữ).

Mục đích: chứng minh lần chạy `package.py` TIẾP THEO vẫn giữ được thân bài
10 chỉ dấu (summary_vn/ja/ko + CHU_CO_DINH_EN.md), không crash, không vượt 5000.
Sau khi kiểm tra ⇒ chạy lại make_descriptions_t17.py để ghi đè bản "chuẩn".
"""
import importlib
import os
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
R = str(ROOT)
sys.path.insert(0, R + r"\.work")

TARGETS = {
    "VI": ["02_SAN_XUAT/Tap17/mo_ta.txt", "02_SAN_XUAT/Tap17/xuat_ban/mo_ta.txt"],
    "EN": ["02_SAN_XUAT/Tap17_EN/description.txt", "02_SAN_XUAT/Tap17_EN/mo_ta.txt",
           "02_SAN_XUAT/Tap17_EN/xuat_ban/description.txt", "02_SAN_XUAT/Tap17_EN/xuat_ban/mo_ta.txt"],
    "JA": ["02_SAN_XUAT/Tap17_JA/description.txt", "02_SAN_XUAT/Tap17_JA/mo_ta.txt",
           "02_SAN_XUAT/Tap17_JA/xuat_ban/description.txt", "02_SAN_XUAT/Tap17_JA/xuat_ban/mo_ta.txt"],
    "KO": ["02_SAN_XUAT/Tap17_KO/description.txt", "02_SAN_XUAT/Tap17_KO/mo_ta.txt",
           "02_SAN_XUAT/Tap17_KO/xuat_ban/description.txt", "02_SAN_XUAT/Tap17_KO/xuat_ban/mo_ta.txt"],
}

bak = ROOT / ".work" / "_cu" / "desc_t17_pkgtest"
bak.mkdir(parents=True, exist_ok=True)
for rels in TARGETS.values():
    for rel in rels:
        p = ROOT / rel
        if p.exists():
            shutil.copy2(p, bak / rel.replace("/", "__"))

print("=== package.description() cho Tập 17 (kiểm tra không mất nội dung) ===")
for lang in ["VI", "EN", "JA", "KO"]:
    os.environ["AE_EP"] = "17"
    os.environ["AE_LANG"] = "" if lang == "VI" else lang
    import edition as ED
    importlib.reload(ED)
    import package as PK
    importlib.reload(PK)
    try:
        chap = PK.description()
    except Exception as e:
        print(f"  [{lang}] CRASH: {type(e).__name__}: {e}")
        continue
    out = PK.OUT_DIR / ("description.txt" if lang != "VI" else "mo_ta.txt")
    txt = out.read_text(encoding="utf-8").strip() if out.exists() else ""
    marker = {"VI": "10. NẠN NHÂN HỌC", "EN": "10. VICTIMOLOGY",
              "JA": "10. 被害者学", "KO": "10. 피해자학"}[lang]
    keeps = marker in txt
    print(f"  [{lang}] OK — {len(txt):5d} ký tự | giữ mục 10: {keeps} | "
          f"{'<=5000 OK' if len(txt) <= 5000 else 'OVER 5000'}")

print("\n>>> Khôi phục bản chuẩn bằng make_descriptions_t17.py …")
