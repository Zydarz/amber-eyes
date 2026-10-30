# -*- coding: utf-8 -*-
"""Kiểm tra EPISODES[*]['summary'] của mọi tập: mã câu có tồn tại trong script?

summary trỏ vào element [BGM] (không có câu thoại) -> package.py --mux crash
KeyError. Sửa: trỏ sang câu thoại đầu hồi 1.

Có sao lưu trước khi ghi (luật L5).
"""
import json
import pathlib
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WORK = pathlib.Path(__file__).resolve().parents[1] / ".work"
EP = WORK / "edition.py"
src = EP.read_text(encoding="utf-8")


def script_ids(ep):
    p = WORK / (f"script_tap{ep}.json" if ep != "01" else "script_v2.json")
    if not p.exists():
        return None
    sc = json.loads(p.read_text(encoding="utf-8"))
    ids = [s["id"] for e in sc for s in e.get("sentences", [])]
    return ids


def first_spoken(ep):
    """Mã câu thoại đầu tiên của hồi 1 trong script."""
    p = WORK / (f"script_tap{ep}.json" if ep != "01" else "script_v2.json")
    sc = json.loads(p.read_text(encoding="utf-8"))
    for e in sc:
        if e.get("act") == 1 and e.get("sentences"):
            return e["sentences"][0]["id"]
    return None


# --- quét từng khối tập
ep_re = re.compile(r'^\s{4}"(\d\d)":\s*\{', re.M)
ep_pos = [(m.group(1), m.start(), m.end()) for m in ep_re.finditer(src)]
broken = {}
for i, (ep, s, e) in enumerate(ep_pos):
    end = ep_pos[i + 1][1] if i + 1 < len(ep_pos) else len(src)
    chunk = src[s:end]
    m = re.search(r'"summary":\s*\(([^)]*)\)', chunk)
    if not m:
        continue
    ids = re.findall(r'"([\d.]+#\d+)"', m.group(1))
    if not ids:
        continue
    have = script_ids(ep)
    if have is None:
        continue
    miss = [x for x in ids if x not in have]
    if miss:
        repl = first_spoken(ep)
        # offset phải tính từ đầu FILE, không phải từ đầu chunk
        broken[ep] = (s + m.start(), s + m.end(), ids, miss, repl)
        print(f"T{ep}: summary {ids} -> THIEU {miss}   (de sua = '{repl}')")
    else:
        print(f"T{ep}: summary {ids} -> OK")

if not broken:
    print("\nKhong co tap nao hong.")
    raise SystemExit(0)

bak = WORK / "_cu" / f"edition.py.bak_summary_{time.strftime('%y%m%d_%H%M%S')}"
bak.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(EP, bak)
print(f"\nSAO LUU: {bak}")

out = src
# sua tu cuoi ve dau de khong lech offset
for ep in sorted(broken, reverse=True):
    st, en, ids, miss, repl = broken[ep]
    out = out[:st] + f'"summary": ("{repl}", "{ids[1]}")' + out[en:]

# kiem tra: file chi doi o 2 dong summary
import difflib
dl = list(difflib.unified_diff(src.splitlines(), out.splitlines(), lineterm="", n=0))
changes = [l for l in dl if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
print(f"\nSo dong thay doi trong file: {len(changes)}")
for l in changes:
    print("   ", l.strip())
if len(changes) != 4:
    raise SystemExit("!! So dong doi khong dung so ky vong (2 truong x 2 dong) - DA ABORT, file khong ghi")
EP.write_text(out, encoding="utf-8")
print(f"DA GHI: {EP}")

# xac nhan
import importlib
sys.path.insert(0, str(WORK))
for m in list(sys.modules):
    if m == "edition":
        del sys.modules[m]
import edition
for ep in sorted(broken):
    ids = edition.EPISODES[ep]["summary"]
    have = script_ids(ep)
    ok = all(x in have for x in ids)
    print(f"  T{ep}: {ids} -> {'OK' if ok else '!! VAN HONG'}")
