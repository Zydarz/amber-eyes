"""Debug: kiem tra danh dau nhip cua TD-PSOLA tren W6_LOW."""
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import importlib.util

spec = importlib.util.spec_from_file_location("psmod", HERE / "g9_psola_shift.py")
mod = importlib.util.module_from_spec(spec)
# chi load phan dinht nghia (khong chay phan 'chay')
src = (HERE / "g9_psola_shift.py").read_text(encoding="utf-8-sig")
head = src.split("# ------------------------------------------------------------------ chay")[0]
exec(compile(head, "psola_head", "exec"), mod.__dict__)

x0, sr = mod.read_wav(mod.SRC)
marks, xl = mod.build_marks(x0, sr)
M = len(marks)
print("len x0 = %d (%.2f s) | M = %d" % (len(x0), len(x0) / sr, M))
if M:
    T0m = len(x0) / M
    print("T0m = %.1f mau -> F0 mong doi %.1f Hz" % (T0m, sr / T0m))
    d = [marks[i + 1][0] - marks[i][0] for i in range(min(M - 1, 12))]
    print("khoang cach 12 mark dau:", d)
    t0s = np.array([t for _, t in marks])
    print("T0 median %.1f mau -> F0 %.1f Hz | T0 p10 %.1f p90 %.1f"
          % (np.median(t0s), sr / np.median(t0s), np.percentile(t0s, 10), np.percentile(t0s, 90)))
    print("mark dau:", marks[0], "| mark cuoi:", marks[-1], "| do dai vung vang %.2f s"
          % ((marks[-1][0] - marks[0][0]) / sr))
