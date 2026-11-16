# -*- coding: utf-8 -*-
"""Cổng A14 (AGENTS) — sau build_audio3.py: không được có khoảng MẤT GIỌNG.

    AE_EP=10 AE_LANG=en py -3 .work/qc_voice_gap.py

Đo trên STEMS GIỌNG gộp (không có nhạc — nhạc che mất khoảng câm nên cổng V4 trên
master không bắt được). Lỗi đã gặp Tập 10 EN: 25,5 s mất giọng ở 635–660 s.
  ① khoảng không có giọng > 3,5 s ngoài vùng được phép (intro, chuyển hồi, thẻ NGHI, outro) = 0
  ② trong [start, end] của mỗi câu, khoảng không có giọng > 1,0 s = 0
  ③ stems / timeline / master cùng một lượt trộn (mtime lệch ≤ 120 s) — tránh đo bản cũ (T17)
  ④ [nếu có timeline_asr4_*] |asr_start − tl_start| ≤ 0,5 s — chỉ CẢNH BÁO (ASR lệch từ tự nhiên)
Exit 1 = TRƯỢT ⇒ DỪNG, quay lại Mac chạy qc_voice_sentence.py cho câu bị nêu tên.
"""
import json
import sys
import wave
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import edition as ED  # noqa: E402

GAP_FREE, GAP_IN, MTIME_TOL, ASR_TOL, WIN = 3.5, 1.0, 120, 0.5, 0.1
SIL = 0.002   # RMS tuyệt đối (stem chỉ có giọng; nền = 0)


def main():
    sd, tlp = ED.w("stems"), ED.w("timeline_s.json")
    master = ED.w("audio_master.wav")
    tl = json.loads(tlp.read_text(encoding="utf-8"))
    print(f"Tập {ED.EPN} · {ED.LANG} · {sd.name} · {tlp.name}")
    fail = 0

    mt = {p.name: p.stat().st_mtime for p in [tlp, master, *sd.glob("*.wav")] if p.exists()}
    spread = max(mt.values()) - min(mt.values())
    ok3 = spread <= MTIME_TOL
    fail += not ok3
    print(f"  ③ cùng lượt trộn: lệch mtime {spread:.0f} s {'ĐẠT' if ok3 else 'TRƯỢT — stems/timeline/master khác lượt, trộn lại'}")

    tot = None
    for r in ("H", "D", "C", "N1", "N2"):
        p = sd / f"{r}.wav"
        if not p.exists():
            continue
        with wave.open(str(p)) as wf:
            sr = wf.getframerate()
            a = np.frombuffer(wf.readframes(wf.getnframes()), np.int16).astype(np.float32) / 32768
        tot = a ** 2 if tot is None else tot[: len(a)] + a[: len(tot)] ** 2
    hop = int(sr * WIN)
    k = len(tot) // hop
    voiced = np.sqrt(tot[: k * hop].reshape(k, hop).mean(1)) > SIL

    allowed = np.zeros(k, bool)
    items = tl["items"]
    allowed[: int(items[0]["start"] / WIN)] = True
    allowed[int(items[-1]["end"] / WIN):] = True
    for m in tl.get("markers", []):
        if m.get("type") in ("ACT", "NGHI", "INTRO"):
            allowed[int(m["start"] / WIN): int((m["end"] + 1.0) / WIN)] = True

    bad, i = [], 0
    while i < k:
        if not voiced[i] and not allowed[i]:
            j = i
            while j < k and not voiced[j] and not allowed[j]:
                j += 1
            if (j - i) * WIN > GAP_FREE:
                t0, t1 = i * WIN, j * WIN
                near = [it["id"] for it in items if it["end"] >= t0 - 1 and it["start"] <= t1 + 1]
                bad.append((t0, t1 - t0, near))
            i = j
        else:
            i += 1
    fail += len(bad)
    print(f"  ① khoảng mất giọng > {GAP_FREE} s: {len(bad)}")
    for t0, L, near in bad:
        print(f"       {t0:7.1f} s · {L:5.1f} s · câu {near}")

    inn = []
    for it in items:
        seg = ~voiced[int(it["start"] / WIN): int(it["end"] / WIN)]
        run = mx = 0
        for v in seg:
            run = run + 1 if v else 0
            mx = max(mx, run)
        if mx * WIN > GAP_IN:
            inn.append((it["id"], it["role"], round(it["start"], 1), mx * WIN))
    fail += len(inn)
    print(f"  ② câu có câm bên trong > {GAP_IN} s: {len(inn)}")
    for x in sorted(inn, key=lambda z: -z[3])[:20]:
        print(f"       {x[0]:8} {x[1]:3} @ {x[2]} s · câm {x[3]:.1f} s")

    asr = ED.WORK / f"timeline_asr4_{ED.LANG}{'' if ED.EPN == '01' else '_t' + ED.EPN}.json"
    if asr.exists():
        A = json.loads(asr.read_text(encoding="utf-8")).get("items", [])
        off = [abs(x["asr_start"] - x["tl_start"]) for x in A if "asr_start" in x and "tl_start" in x]
        if off:
            n = sum(o > ASR_TOL for o in off)
            print(f"  ④ (cảnh báo) ASR lệch timeline > {ASR_TOL} s: {n}/{len(off)} câu · tối đa {max(off):.1f} s ({asr.name})")

    print("KẾT QUẢ:", "ĐẠT" if not fail else "TRƯỢT")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
