#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L9 hồi quy: so mux_af của BẢN SỬA vs BẢN SAO LƯU cho MỌI tập × MỌI ngôn ngữ.

Kỳ vọng: khác biệt DUY NHẤT ở (EP03, ja). Mọi ngôn ngữ/tập khác phải giống hệt.
"""
import importlib.util
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
NEW = W / "edition.py"
OLD = W / "edition_bak_muxaf_tmp.py"


def load(path, lang, ep):
    for k in ("AE_LANG", "AE_EP"):
        os.environ[k] = str(ep) if k == "AE_EP" else lang
    # nạp lại module từ đường dẫn (tên module khác nhau để không đụng sys.modules)
    spec = importlib.util.spec_from_file_location("ed_" + str(abs(hash((str(path), lang, ep)))), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


LANGS = ["vi", "en", "ko", "ja"]
diffs = []
errs = []
for ep in range(1, 30):
    epk = "%02d" % ep          # khoá EPISODES là chuỗi 2 chữ số: "01".."29" (str(3)="3" ≠ "03")
    for lang in LANGS:
        try:
            a = load(OLD, lang, ep).EPISODES.get(epk, {}).get("mux_af")
        except SystemExit:
            a = "ERR"
        except Exception as e:
            a = "ERR:%s" % type(e).__name__
        try:
            b = load(NEW, lang, ep).EPISODES.get(epk, {}).get("mux_af")
        except SystemExit:
            b = "ERR"
        except Exception as e:
            b = "ERR:%s" % type(e).__name__
        if a != b:
            diffs.append((ep, lang, a, b))

print("=== HỒI QUY mux_af (bản sửa vs bản sao lưu) ===")
if not diffs:
    print("  KHÔNG có khác biệt nào (không mong đợi — lỗi)")
for ep, lang, a, b in diffs:
    print(f"  EP{ep:02d} [{lang}]")
    print(f"      cu : {a}")
    print(f"      moi: {b}")

expected = [(3, "ja")]
got = sorted((e, l) for e, l, _, _ in diffs)
print()
print("  mong doi:", expected)
print("  thuc te :", got)
ok = got == sorted(expected)
print("KET QUA:", "PASS - chi doi (03, ja)" if ok else "FAIL - sai pham vi thay doi")
sys.exit(0 if ok else 1)
