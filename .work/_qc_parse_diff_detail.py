#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem chi tiết câu đổi do bản vá parser (dùng khi điều tra hồi quy)."""
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


old_src = subprocess.run(["git", "show", "HEAD:.work/parse_kichban.py"],
                         cwd=ROOT, capture_output=True).stdout.decode("utf-8")
tmp = Path(tempfile.gettempdir()) / "_pk_old.py"
tmp.write_text(old_src, encoding="utf-8")
OLD = load_module(tmp, "pk_old")
NEW = load_module(WORK / "parse_kichban.py", "pk_new")

targets = [
    "01_KICH_BAN/Tap01_KO/kichban_tap01_KO.md",
    "01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md",
    "01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md",
    "01_KICH_BAN/Tap03_EN/kichban_tap03_EN.md",
]
for rel in targets:
    p = ROOT / rel
    o = OLD.parse_lines(p.read_text(encoding="utf-8").splitlines())
    n = NEW.parse_lines(p.read_text(encoding="utf-8").splitlines())
    od = {s["id"]: s["text"] for e in o for s in (e.get("sentences") or [])}
    nd = {s["id"]: s["text"] for e in n for s in (e.get("sentences") or [])}
    diff = [k for k in nd if od.get(k) != nd[k]]
    print("=" * 74)
    print(rel, f"— {len(diff)} câu đổi")
    for k in diff[:4]:
        print(f"  {k}")
        print(f"    CŨ : {od.get(k)!r}")
        print(f"    MỚI: {nd.get(k)!r}")
