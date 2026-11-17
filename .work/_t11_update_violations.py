#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cập nhật hồ sơ 32 nền có chữ AI: thêm vòng sinh lại + trạng thái đã xử lý."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / ".work" / "_t11" / "violations_t11.json"

# nền nào cần tới vòng nào
ROUNDS = {
    "t11_haunted_new_identity_shadow": 3,
    "t11_triumphant_smile_deal_with_devil": 2,
    "t11_six_8mm_tapes_bag": 2,
    "t11_control_room_dark_monitors": 4,
}


def main():
    rows = json.loads(V.read_text(encoding="utf-8"))
    for r in rows:
        r["vong_sinh_lai"] = ROUNDS.get(r["name"], 1)
        r["trang_thai"] = "DA_XU_LY_SACH_CHU"
        r["soi_lai"] = ("full-res 2112x1188" if r["vong_sinh_lai"] > 1
                        else "montage o 700px + full-res")
    V.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    c = Counter(r["vong_sinh_lai"] for r in rows)
    print(f"{V.relative_to(ROOT)} · {len(rows)} nen · phan bo vong: {dict(sorted(c.items()))}")
    print("trang thai: tat ca DA_XU_LY_SACH_CHU")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
