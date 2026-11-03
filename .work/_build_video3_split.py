"""Bien ban cua build_video3.py: ghi PART ra thu muc rieng (env AE_VID).

Muc dich: chia mot lan build 37751 frame (~73 phut) thanh 2 nua chay SONG SONG
de moi nua nằm trong gioi han 1 gio/task cua bash.

KHONG sua .work/build_video3.py (file dung chung) -> khong phat sinh nghia vu
hoi quy Tap 01 cho file do (L9).

Cach dung:
    $env:AE_EP='06'
    $env:AE_VID='.work/video3_t06_A'
    py -3 .work/_build_video3_split.py --from 0 --to 629.185 --workers 6 --out .work/video3_t06_A/pictureA.mp4

render(fi) chi phu thuoc 'fi' nen chia theo khoang frame cho ket qua Y HET nhu
mot lan build lien tuc.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build_video3 as B  # noqa: E402
import edition as ED  # noqa: E402

_RAW = os.environ.get("AE_VID", "").strip()
if not _RAW:
    raise SystemExit("Thieu env AE_VID (thu muc chua part).")

_VD = Path(_RAW)
if not _VD.is_absolute():
    # duong dan tuong doi -> phai goc WORKSPACE (khong phai .work)
    _VD = (Path.cwd() / _VD).resolve()


class _EDProxy:
    """Chi doi duong dan 'video3'; moi ten khac giu nguyen (stems, shots...)."""

    def __init__(self, real, vd):
        self._real = real
        self._vd = vd

    def w(self, name):
        if name == "video3":
            return self._vd
        return self._real.w(name)

    def __getattr__(self, k):
        return getattr(self._real, k)


B.ED = _EDProxy(ED, _VD)

# --- AE_ENC_THREADS: gioi han so thread cua encoder libopenh264 -------------
# Mac dinh libopenh264 tu chon = so core -> 6 worker x N thread la qua tai.
# Thu nghiem: dat -threads khi can.
_ENC_THREADS = os.environ.get("AE_ENC_THREADS", "").strip()
if _ENC_THREADS:
    import subprocess as _sp

    _real_popen = _sp.Popen

    def _popen(cmd, *a, **kw):
        if isinstance(cmd, list) and "libopenh264" in cmd:
            cmd = list(cmd) + ["-threads", _ENC_THREADS]
        return _real_popen(cmd, *a, **kw)

    B.subprocess.Popen = _popen

# --- AE_PIPE_BUF: pipe buffer lon (Windows mac dinh chi 4 KB) ----------------
# Do duoc: 6 worker + pipe 4 KB -> 8.3 fps; render thuan -> 12.6 fps.
# Pipe 4 KB = ~1550 vong ghi/giac lich moi frame 6.2 MB -> tang buffer.
# Patch _winapi.CreatePipe (subprocess tu tao ca hai dau) de giu nguyen
# co che handle/EOF cua subprocess.
_PIPE_BUF = os.environ.get("AE_PIPE_BUF", "").strip()
if _PIPE_BUF:
    import _winapi

    _real_create_pipe = _winapi.CreatePipe
    _PIPE_SIZE = int(_PIPE_BUF)

    def _create_pipe(readable, writable):
        if readable is None and not writable:
            return _real_create_pipe(None, _PIPE_SIZE)
        return _real_create_pipe(readable, writable)

    _winapi.CreatePipe = _create_pipe
    print(f"[split] AE_PIPE_BUF={_PIPE_BUF}", flush=True)

# --- AE_FAST_FINISH: finishing() toi uu, BIT-IDENTICAL ----------------------
# Kiem chung bang .work/_bench_fast_check.py (120 frame x 2 nguon).
_FAST = os.environ.get("AE_FAST_FINISH", "").strip()
if _FAST:
    import numpy as np

    _ORIG_FIN = B.finishing          # ban goc: dung de khoi tao globals VIGNETTE/GRAIN
    _V3 = {"v": None}

    def _finishing_fast(arr, fi):
        if _V3["v"] is None:
            _ORIG_FIN(arr, fi)        # khoi tao VIGNETTE/GRAIN/ABUF trong module goc
            _V3["v"] = np.repeat(B.VIGNETTE, 3, axis=2).copy()
        a = arr.astype(np.float32)
        np.multiply(a, _V3["v"], out=a)
        np.add(a, B.GRAIN[fi % 6], out=a)
        red = a[:, :, 0].copy()
        a[:, 1:, 0] = red[:, :-1]
        np.clip(a, 0, 255, out=a)
        return a.astype(np.uint8)

    B.finishing = _finishing_fast
    print("[split] AE_FAST_FINISH=1", flush=True)

if __name__ == "__main__":
    print(f"[split] AE_VID={_VD}", flush=True)
    print(f"[split] total={B.TOTAL:.3f}s  fps={B.FPS}", flush=True)
    B.main()
