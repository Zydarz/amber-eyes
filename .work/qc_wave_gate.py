# -*- coding: utf-8 -*-
"""Cổng H24 — sóng giọng trên badge phải lên xuống, không thành dải ngang.

    AE_EP=10 [AE_LANG=en] py -3 .work/qc_wave_gate.py          # đo theo cấu hình tập
    AE_EP=10 py -3 .work/qc_wave_gate.py --mode 0.12           # đo với hằng cũ (so sánh)

Chạy sau build_audio3.py, TRƯỚC ảnh tĩnh / dựng. Dùng đúng wave_env.normalize
mà build_video3.py dùng để vẽ. Exit 1 = TRƯỢT ⇒ DỪNG, không dựng.
Ngưỡng (theo vai có lời): chạm trần ≤ 10 % · lệch chuẩn ≥ 0,15 ·
phân vị 95 trong 0,6–1,0 · stem tồn tại, khác 0.
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import edition as ED  # noqa: E402
import wave_env  # noqa: E402

CEIL_MAX, STD_MIN, P95_LO, P95_HI = 0.10, 0.15, 0.6, 1.0


def roles_with_lines():
    tl = ED.w("timeline_s.json")
    if not tl.exists():
        return ["H", "D", "C"]
    items = json.loads(tl.read_text(encoding="utf-8")).get("items", [])
    return sorted({it["role"] for it in items if it.get("role")})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default=None, help="số cố định để so sánh; mặc định = EPISODES[xx]['wave_norm'] hoặc auto")
    a = ap.parse_args()
    mode = float(a.mode) if a.mode else ED.EP.get("wave_norm")
    sd = ED.w("stems")
    print(f"Tập {ED.EPN} · {ED.LANG} · stems {sd.name} · chuẩn hoá {mode or 'auto'}")
    fail = 0
    for r in roles_with_lines():
        p = sd / f"{r}.wav"
        if not p.exists():
            print(f"  {r:3} TRƯỢT: thiếu stem {p.name} (badge sẽ vẽ vạch phẳng)")
            fail += 1
            continue
        e = wave_env.rms_frames(p)
        v = wave_env.normalize(e, mode)[e > wave_env.VOICED_RMS]
        if v.size == 0:
            print(f"  {r:3} TRƯỢT: stem câm")
            fail += 1
            continue
        ceil, std, p95 = float(np.mean(v >= 0.99)), float(v.std()), float(np.percentile(v, 95))
        ok = ceil <= CEIL_MAX and std >= STD_MIN and P95_LO <= p95 <= P95_HI
        fail += not ok
        print(f"  {r:3} {'ĐẠT ' if ok else 'TRƯỢT'} chạm trần {ceil:5.1%} (≤10%) · lệch chuẩn {std:.2f} (≥0,15)"
              f" · p95 {p95:.2f} (0,6–1,0) · {v.size} khung nói")
    print("KẾT QUẢ:", "ĐẠT" if not fail else f"TRƯỢT {fail} vai")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
