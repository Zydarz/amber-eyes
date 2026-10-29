#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sửa cơ học 2 nhóm lỗi còn lại trong cache JA:

  1) Tên riêng tiếng Việt bị BỎ DẤU (Nguyen Hai Duong -> Nguyễn Hải Dương).
     Quy ước nhà: tên riêng giữ nguyên chữ Latin GỐC, kể cả dấu tiếng Việt.
  2) Từ Trung dùng kanji hợp lệ ở Nhật (氛围 / 气氛 -> 雰囲気).

    py -3 .work/_ja_fix_names.py          # dry-run
    py -3 .work/_ja_fix_names.py --do
"""
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

APPLY = "--do" in sys.argv

# (mẫu cũ, mẫu mới, dùng ranh giới từ?)
NAME_FIX = [
    ("Nguyen Hai Duong", "Nguyễn Hải Dương", False),
    ("Le Thi Anh Linh", "Lê Thị Ánh Linh", False),
    ("Vu Van Tien", "Vũ Văn Tiến", False),
    ("Tran Dinh Thoai", "Trần Đình Thoại", False),
    ("Cuc Canh sat Hinh su", "Cục Cảnh sát Hình sự", False),
    ("Du Minh Vy", "Dư Minh Vy", False),
    ("Ngoc Bich", "Ngọc Bích", False),
    ("Duong", "Dương", True),
    ("Tien", "Tiến", True),
    ("Thoai", "Thoại", True),
    ("Ngoc", "Ngọc", True),
    ("Bich", "Bích", True),
]

# từ Trung -> tiếng Nhật
WORD_FIX = [
    ("氛围", "雰囲気"),
    ("气氛", "雰囲気"),
]


def main():
    files = {}
    counts = {}
    for i in range(1, 30):
        ep = "%02d" % i
        cp = HERE / "ja_cache" / f"tap{ep}.json"
        if not cp.exists():
            continue
        d = files.setdefault(ep, (cp, json.loads(cp.read_text(encoding="utf-8"))))[1]
        for k, v in d.items():
            if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
                continue
            ja = v.get("ja", "")
            if not isinstance(ja, str) or not ja:
                continue
            orig = ja
            for old, new, wb in NAME_FIX:
                if wb:
                    ja = re.sub(r"(?<![A-Za-zÀ-ỹĐđ])" + re.escape(old) + r"(?![A-Za-zÀ-ỹĐđ])",
                                new, ja)
                else:
                    ja = ja.replace(old, new)
            for old, new in WORD_FIX:
                ja = ja.replace(old, new)
            if ja != orig:
                v["ja"] = ja
                counts.setdefault(ep, []).append(k)

    tot = sum(len(x) for x in counts.values())
    print(f"Da sua {tot} muc:")
    for ep in sorted(counts):
        print(f"  Tap{ep}: {len(counts[ep])}  {counts[ep][:12]}")

    if not APPLY:
        print("\nDRY-RUN. Them --do de ghi.")
        return
    for ep, (cp, d) in files.items():
        shutil.copy2(cp, cp.with_suffix(".json.bak_names"))
        cp.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"   da ghi tap{ep}.json")


if __name__ == "__main__":
    main()
