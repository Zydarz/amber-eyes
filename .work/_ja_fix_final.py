#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vá nốt 2 mục cuối bằng ESCAPE UNICODE (không phụ thuộc gõ tay),
rồi QUÉT TOÀN BỘ cache để chắc chắn không còn ký tự Trung-only / Hangul.

    py -3 .work/_ja_fix_final.py          # dry-run
    py -3 .work/_ja_fix_final.py --do
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

APPLY = "--do" in sys.argv

# (tap, key, old, new) -- dùng \uXXXX để chắc chắn đúng codepoint
FIX = [
    # 暴风雨 -> 暴風雨   (风 U+98CE -> 風 U+98A8)
    ("25", "u0097#0", "\u66b4\u98ce\u96e8\u306e\u591c\u3001",
     "\u66b4\u98a8\u96e8\u306e\u591c\u3001"),
    # 両手の多处 -> 両手のあちこち   (处 U+5904 -> 処 U+51e6 / 場所)
    ("28", "u0067#0", "\u4e21\u624b\u306e\u591a\u5904",
     "\u4e21\u624b\u306e\u3042\u3053\u3054\u3061"),
]

RX_HANGUL = re.compile(r"[\u3131-\u318e\uac00-\ud7a3]+")
RX_CN = re.compile("[" + "".join(sorted(M.CN_ONLY_CHARS)) + "]")


def main():
    miss = []
    files = {}
    for ep, key, old, new in FIX:
        cp = HERE / "ja_cache" / f"tap{ep}.json"
        d = files.get(ep) or files.setdefault(ep, (cp, json.loads(cp.read_text(encoding="utf-8"))))[1]
        v = d.get(key)
        if not isinstance(v, dict) or old not in v.get("ja", ""):
            miss.append((ep, key, old))
            continue
        v["ja"] = v["ja"].replace(old, new)
        print(f"  Tap{ep} {key}: OK")

    if miss:
        print("KHONG KHAI THAC:", miss)

    # ---- quét toàn bộ cache
    leftover = []
    for i in range(1, 30):
        ep = "%02d" % i
        cp = HERE / "ja_cache" / f"tap{ep}.json"
        if not cp.exists():
            continue
        d = files.get(ep, (cp, json.loads(cp.read_text(encoding="utf-8"))))[1]
        for k, v in d.items():
            if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
                continue
            ja = v.get("ja", "")
            if not isinstance(ja, str) or not ja:
                continue
            cn = sorted({c for c in ja if c in M.CN_ONLY_CHARS})
            ko = RX_HANGUL.findall(ja)
            if cn or ko:
                leftover.append((ep, k, "".join(cn), ko, ja))

    print(f"\n=== CON LAI {len(leftover)} muc nhiem ===")
    for ep, k, cn, ko, ja in leftover:
        print(f"  Tap{ep} {k}: CN={cn} KO={ko}")
        print(f"     {ja[:120]}")

    if not APPLY:
        print("\nDRY-RUN. Them --do de ghi.")
        return
    for ep, (cp, d) in files.items():
        cp.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"   da ghi tap{ep}.json")


if __name__ == "__main__":
    main()
