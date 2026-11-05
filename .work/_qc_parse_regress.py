#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L9 — hồi quy parser kịch bản.

parse_kichban.py dùng chung cho MỌI tập (L8/L9). Sửa nó => phải chứng minh
kết quả parse của mọi kịch bản trong repo KHÔNG đổi, trừ những tập cố ý sửa.

Cách đo: nạp bản HEAD (trước khi sửa) + bản hiện tại, parse cùng 1 file kịch bản,
so từng element (kind/role/sec/desc/text/sentences).

    py -3 .work/_qc_parse_regress.py
"""
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---- bản cũ (HEAD)
old_src = subprocess.run(["git", "show", "HEAD:.work/parse_kichban.py"],
                         cwd=ROOT, capture_output=True).stdout.decode("utf-8")
tmp = Path(tempfile.gettempdir()) / "_parse_kichban_old.py"
tmp.write_text(old_src, encoding="utf-8")
OLD = load_module(tmp, "parse_old")

# ---- bản mới
NEW = load_module(WORK / "parse_kichban.py", "parse_new")

MD = sorted((ROOT / "01_KICH_BAN").rglob("*.md"))
MD = [p for p in MD if "REVIEW" not in p.name and "BaoCao" not in p.name
      and "KHO_Y" not in p.name and "CanXacMinh" not in p.name]

changed, same, failed = [], 0, []
for p in MD:
    try:
        o = OLD.parse_lines(p.read_text(encoding="utf-8").splitlines())
        n = NEW.parse_lines(p.read_text(encoding="utf-8").splitlines())
    except Exception as e:
        failed.append((p, repr(e)))
        continue
    if json.dumps(o, ensure_ascii=False, sort_keys=True) == json.dumps(n, ensure_ascii=False, sort_keys=True):
        same += 1
    else:
        # chi tiết câu nào đổi
        od = {s["id"]: s["text"] for e in o for s in (e.get("sentences") or [])}
        nd = {s["id"]: s["text"] for e in n for s in (e.get("sentences") or [])}
        diff = [k for k in nd if od.get(k) != nd[k]]
        changed.append((p.relative_to(ROOT), diff))

print("=" * 74)
print("L9 — HỒI QUY PARSE_KICHBAN.PY")
print("=" * 74)
print(f"kịch bản đã kiểm tra : {len(MD)}")
print(f"parse lỗi            : {len(failed)}")
for p, e in failed:
    print(f"   [LOI] {p.relative_to(ROOT)}: {e}")
print(f"KHÔNG đổi             : {same}")
print(f"CÓ đổi               : {len(changed)}")
for p, diff in changed:
    print(f"   [{'CỐ Ý' if 'Tap03' in str(p) else 'Ngoài ý muốn'}] {p}  ({len(diff)} câu)")
    for k in diff[:12]:
        print(f"        {k}")
print("\nKẾT LUẬN:", "OK — chỉ Tap03 đổi (đúng mục tiêu)" if all("Tap03" in str(p) for p, _ in changed)
      else "CẢNH BÁO — có tập khác bị đổi ngoài dự kiến")
sys.exit(0 if all("Tap03" in str(p) for p, _ in changed) and not failed else 1)
