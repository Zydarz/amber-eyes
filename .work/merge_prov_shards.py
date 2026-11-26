#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gộp các shard provenance (.work/_prov_shard_tXX.json) vào provenance.json.

Chạy SAU KHI tất cả tiến trình sinh ảnh đã kết thúc (tránh ghi đè lẫn nhau).
Ghi file tạm + os.replace => atomic.
"""
import json
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
PROV_FILE = ROOT / "provenance.json"


def main():
    eps = sys.argv[1:] or ["37", "38", "39"]
    prov = json.loads(PROV_FILE.read_text(encoding="utf-8"))
    by_file = {r["file"]: i for i, r in enumerate(prov)}
    added = updated = 0
    total = 0

    for ep in eps:
        shard = WORK / f"_prov_shard_t{ep}.json"
        if not shard.exists():
            print(f"Tập {ep}: không có shard ({shard.name})")
            continue
        entries = json.loads(shard.read_text(encoding="utf-8"))
        total += len(entries)
        for entry in entries:
            fpath = entry["file"]
            if fpath in by_file:
                prov[by_file[fpath]] = entry
                updated += 1
            else:
                prov.append(entry)
                by_file[fpath] = len(prov) - 1
                added += 1
        print(f"Tập {ep}: gộp {len(entries)} dòng")

    fd, tmp = tempfile.mkstemp(dir=str(ROOT), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(prov, f, ensure_ascii=False, indent=2)
        os.replace(tmp, PROV_FILE)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise

    print(f"\nprovenance.json: +{added} mới, ~{updated} cập nhật, tổng shard {total} dòng.")
    print(f"Tổng số dòng provenance: {len(prov)}")


if __name__ == "__main__":
    main()
