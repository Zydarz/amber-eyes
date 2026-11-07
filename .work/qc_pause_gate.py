#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng NHỊP NGHỈ giữa câu (AGENTS A13 · tiêu chuẩn A4.3b · QUY_TAC_AUDIO_HIGGS §9).

  AE_EP=06 AE_LANG=vi py -3 .work/qc_pause_gate.py --pre    # TRƯỚC khi trộn: file diễn xuất
  AE_EP=06 AE_LANG=vi py -3 .work/qc_pause_gate.py          # SAU build_audio3: đo timeline + mp3

--pre : file diễn xuất của ĐÚNG ngôn ngữ phải tồn tại; mọi mã `_pause_after` tồn tại trong script;
        giá trị 0,2–1,2 s; số mục ≥ 40% số câu (cảnh báo, không chặn).
sau   : (1) trung vị khoảng nghỉ giữa 2 câu liền kề cùng hồi ≥ 0,60 s
        (2) tỉ lệ khoảng nghỉ < 0,40 s ≤ 25 %
        (3) timeline.total = thời lượng master mp3 ± 0,05 s (T20)
Thoát mã 1 khi không đạt. Số đo in ra để chép vào hồ sơ tập (L3, L6).
"""
import json, os, re, statistics as st, subprocess, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402

MED_MIN, SHORT_MAX, SHORT_GAP = 0.60, 0.25, 0.40
ok = True
lang = os.environ.get("AE_LANG", "vi")
print(f"Tập {os.environ.get('AE_EP', '01')} · {lang}")

script = json.loads(Path(ED.SCRIPT_JSON).read_text(encoding="utf-8"))
ids = [s["id"] for e in script for s in e.get("sentences", [])]

if "--pre" in sys.argv:
    p = Path(ED.ACTING) if ED.ACTING else None
    if not p or not p.exists():
        print(f"✗ THIẾU file diễn xuất {p} ⇒ máy trộn sẽ dùng 0 khoảng nghỉ. DỪNG."); sys.exit(1)
    pa = json.loads(p.read_text(encoding="utf-8")).get("_pause_after", {})
    bad = [k for k in pa if k not in ids]
    rng = [k for k, v in pa.items() if not 0.2 <= v <= 1.2]
    print(f"  {p.name}: {len(pa)} mục / {len(ids)} câu ({len(pa)/len(ids):.0%}) · mã lạ {len(bad)} · ngoài 0,2–1,2 s {len(rng)}")
    if bad or rng:
        print("  ✗", bad[:8], rng[:8]); ok = False
    if len(pa) < 0.4 * len(ids):
        print("  ⚠ ít hơn 40% số câu — gần như chắc chắn trượt cổng sau trộn (Tập 06: 37/212 ⇒ trung vị 0,35 s)")
    print("ĐẠT (trước trộn)" if ok else "KHÔNG ĐẠT"); sys.exit(0 if ok else 1)

tl_p = ED.w("timeline_s.json")
tl = json.loads(tl_p.read_text(encoding="utf-8"))
it = tl["items"]
g = [b["start"] - a["end"] for a, b in zip(it, it[1:]) if a["act"] == b["act"]]
med, short = st.median(g), sum(x < SHORT_GAP for x in g) / len(g)
print(f"  {tl_p.name}: {len(it)} câu · trung vị nghỉ {med:.2f} s (≥ {MED_MIN}) · "
      f"< {SHORT_GAP} s: {sum(x < SHORT_GAP for x in g)}/{len(g)} = {short:.0%} (≤ {SHORT_MAX:.0%})")
if med < MED_MIN or short > SHORT_MAX:
    ok = False; print("  ✗ nhịp nghỉ: câu nối nhau quá sát ⇒ nghe 'đọc nhanh, không chậm rãi'")
if len(it) != len(ids):
    ok = False; print(f"  ✗ timeline {len(it)} câu ≠ script {len(ids)}")
mp3 = ED.OUT_DIR / (ED.MASTER + ".mp3")
FP = Path(__file__).parent / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
if mp3.exists():
    d = float(subprocess.run([str(FP), "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                              str(mp3)], capture_output=True, text=True).stdout)
    print(f"  {mp3.name}: {d:.2f} s · timeline.total {tl['total']:.2f} s · lệch {d - tl['total']:+.2f}")
    if abs(d - tl["total"]) > 0.05 or it[-1]["end"] > d:
        ok = False; print("  ✗ T20: timeline không khớp master")
else:
    print(f"  ⚠ chưa có {mp3.name}")
print("ĐẠT" if ok else "KHÔNG ĐẠT"); sys.exit(0 if ok else 1)
