# -*- coding: utf-8 -*-
"""
Ghi dong provenance cho cac ung vien SFX tu Freesound.

Doc .work/freesound_candidates.json (sinh boi fs_fetch.py), tra ve
02_SAN_XUAT/Danh_Sach_SFX_Tap03-29.md muc 4.2 de lay duong dan dich
("Dat tai") cua tung ma SFX, roi ghi dong vao provenance.json.

Trang thai ghi la "ung vien - chua nghe duyet": theo A3, SFX tai veo phai
duoc nghe kiem truoc khi nhap vao assets/sfx/ va dua vao video.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from freesound_client import append_provenance  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
DOC = ROOT / "02_SAN_XUAT" / "Danh_Sach_SFX_Tap03-29.md"
CAND = WORK / "freesound_candidates.json"

ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*`([a-z0-9_]+)`\s*\|.*?`(assets/sfx/[^`]+)`")


def target_paths() -> dict[str, str]:
    """Ma SFX -> duong dan dich trong repo (tu cot 'Dat tai' muc 4.2)."""
    out: dict[str, str] = {}
    for line in DOC.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if m:
            out.setdefault(m.group(2), m.group(3))
    return out


def main() -> int:
    if not CAND.exists():
        print(f"Thieu {CAND} - chay fs_fetch.py truoc", file=sys.stderr)
        return 1

    data = json.loads(CAND.read_text(encoding="utf-8"))
    targets = target_paths()
    rows = []

    for entry in data["codes"]:
        code = entry["code"]
        dest = targets.get(code)
        for c in entry["candidates"]:
            if not c.get("file_local"):
                continue
            lic = c.get("license_id", "unknown")
            rows.append({
                "file": dest or c["file_local"],
                "loai": "sfx_freesound",
                "cong_cu": "Freesound APIv2 (Token auth) - .work/freesound_client.py",
                "ngay": "2026-10-24",
                "prompt": None,
                "seed": None,
                "font": None,
                "dieu_khoan": (
                    f"Freesound id={c['sound_id']} | {c.get('license')} | "
                    f"tac gia: {c.get('attribution') or c.get('author')} | "
                    f"link: {c.get('url')} | "
                    f"file tam: {c['file_local']} (PREVIEW hq mp3, khong phai file goc) | "
                    f"thoi luong: {c.get('duration_file')}s | "
                    f"mean {c.get('mean_db')} dBFS / max {c.get('max_db')} dBFS"
                ),
                "kiem_tra_thuong_mai": (
                    "cc0 - cho phep thuong mai; CHUA nghe duyet (A3)"
                    if lic == "cc0"
                    else f"{lic} - can kiem dieu khoan thuong mai truoc khi dung"
                ),
            })

    staging = WORK / "freesound_provenance.json"
    staging.write_text(
        json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Da ghi {len(rows)} dong vao SO TAM: {staging}")

    if "--merge" in sys.argv:
        path, added = append_provenance(rows)
        print(f"Da ghi them {added} dong vao {path} "
              f"(tong {len(json.loads(path.read_text(encoding='utf-8')))})")
    else:
        print("CHUA ghi vao provenance.json (dung --merge sau khi nguoi dung duyet)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
