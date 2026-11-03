#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Boc pipe cua Windows: buffer mac dinh 4 KB -> 4 MB.

Windows vong dem an danh (anonymous pipe) chi 4 KB buffer => moi khung hinh
1920x1080x3 = 6,2 MB phai qua ~1.550 vong ghi/giac lich. Do duoc tren Tap 06:
  6 tien trinh, pipe 4 KB  :  8,32 fps
  6 tien trinh, pipe 4 MB  : 11,58 fps  (+39 %)
Khong sua file dung chung build_video3.py - wrapper nay monkey-patch
`_winapi.CreatePipe` roi goi main() cua renderer.

QUAN TRONG: chi doi `size` cua CreatePipe. KHONG tu tao pipe roi tra ve
(p2cwrite = -1 => ffmpeg khong nhan handle stdin => "Bad file descriptor").
subprocess van tu quan ly handle va EOF nhu cu.

Dung:
    py -3 .work/_render_patched.py --stills all
    py -3 .work/_render_patched.py --workers 6
"""
import os
import sys
from pathlib import Path

os.environ.setdefault("AE_EP", "03")
os.environ.setdefault("AE_LANG", "en")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")

import _winapi  # noqa: E402

_PIPE_BYTES = 4 * 1024 * 1024
_orig = _winapi.CreatePipe
_patched = False


def _big_pipe(pipe_attrs=None, size=0):
    global _patched
    _patched = True
    return _orig(pipe_attrs, _PIPE_BYTES)


_winapi.CreatePipe = _big_pipe

W = Path(__file__).resolve().parent
sys.path.insert(0, str(W))
import build_video3 as B  # noqa: E402

if __name__ == "__main__":
    print(f"[patched] CreatePipe size = {_PIPE_BYTES // 1024} KB")
    B.main()
    print(f"[patched] CreatePipe duoc goi: {_patched}")
