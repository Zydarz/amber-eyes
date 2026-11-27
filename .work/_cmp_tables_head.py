# -*- coding: utf-8 -*-
"""So sanh so dong loi bang markdown giua phien ban hien tai va ban HEAD (git show)."""
import io
import pathlib
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _check_md_tables4 import check  # noqa: E402

ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")
for rel in ["AGENTS.md", "00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md",
            "02_SAN_XUAT/TIKTOK/Tap04/BAO_CAO_QC_TIKTOK_TAP04.md"]:
    head = subprocess.check_output(["git", "-C", str(ROOT), "show", f"HEAD:{rel}"])
    tmp = pathlib.Path(tempfile.gettempdir()) / ("head_" + pathlib.Path(rel).name)
    tmp.write_bytes(head)
    print(f"===== HEAD: {rel}")
    n = check(tmp)
    print(f"===== HIEN TAI: {rel}")
    m = check(ROOT / rel)
    print(f">>> {rel}: HEAD loi={n} | hien tai loi={m} | delta={m - n}\n")
