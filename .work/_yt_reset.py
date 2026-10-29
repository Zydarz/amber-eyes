#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reset cac file bi gan nham: bo khoi state 'used' va chuyen sang _reject.

Dung: py -3 .work/_yt_reset.py <ma_sfx> [ma_sfx ...]
Sau do phai BAM TAI LAI track tuong ung tren trang thu vien.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\Audi")
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
REJECT = INBOX / "_reject"
STATE = ROOT / ".work" / "yt_watch_state.json"


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:8]


def main():
    mas = sys.argv[1:]
    st = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"used": []}
    used = set(st.get("used", []))
    REJECT.mkdir(parents=True, exist_ok=True)
    for ma in mas:
        used.discard(ma)
        src = INBOX / (ma + ".mp3")
        if src.exists():
            dst = REJECT / (ma + "_" + md5(src) + ".mp3")
            shutil.move(str(src), str(dst))
            print("-> _reject:", dst.name)
        else:
            print("-> khong co file:", ma)
    st["used"] = sorted(used)
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    print("state used con %d ma" % len(used))


if __name__ == "__main__":
    main()
