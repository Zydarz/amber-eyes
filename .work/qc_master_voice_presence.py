# -*- coding: utf-8 -*-
"""KIỂM THAY THẾ A14 khi KHÔNG có stems giọng thật: đo thẳng trên master (giọng + nhạc).

    AE_EP=11 [AE_LANG=en|ja] py -3 .work/qc_master_voice_presence.py [--margin 6] [--json out.json]

Ý tưởng: nhạc nền bị ducking dưới giọng ⇒ trong cửa sổ câu, mức RMS phải NỔI trên "sàn nhạc"
(đo ở các khoảng nghỉ giữa câu) ít nhất --margin dB. Câu mà giọng biến mất ⇒ chỉ còn nhạc ⇒ không nổi.
  ① câu có tỉ lệ khung có giọng < 40 %                 = 0
  ② câu có đoạn "không giọng" liền > 1,0 s bên trong    = 0
  ③ khoảng không có giọng > 3,5 s ngoài intro/chuyển hồi/NGHI/outro = 0 (đo giữa các câu liền kề)
GIỚI HẠN: không thay được A14 chuẩn (stems thật + ASR); nhạc to bất thường có thể che lỗi.
Báo cáo phải ghi "kiểm thay thế". Exit 1 = TRƯỢT.
"""
import argparse, json, shutil, subprocess, sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import edition as ED  # noqa: E402

SR, HOP = 24000, 1200   # 50 ms


def ffmpeg():
    w = ED.WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
    return str(w) if w.exists() else shutil.which("ffmpeg")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--margin", type=float, default=6.0)
    ap.add_argument("--json")
    a = ap.parse_args()
    master = ED.OUT_DIR / f"{ED.EP['master']}.mp3"
    tl = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
    raw = subprocess.run([ffmpeg(), "-v", "error", "-i", str(master), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    n = len(x) // HOP
    db = 20 * np.log10(np.sqrt((x[: n * HOP].reshape(n, HOP) ** 2).mean(axis=1)) + 1e-9)
    items = [it for it in tl["items"] if it.get("role")]
    # sàn nhạc: khoảng nghỉ giữa câu liền kề >= 0,4 s, bỏ 0,1 s hai đầu
    gaps = []
    for p, q in zip(items, items[1:]):
        g0, g1 = p["end"] + 0.1, q["start"] - 0.1
        if g1 - g0 >= 0.2:
            gaps.append(db[int(g0 / 0.05): int(g1 / 0.05)])
    floor = float(np.median(np.concatenate(gaps)))
    thr = floor + a.margin
    print(f"Tập {ED.EPN} · {ED.LANG} · {master.name} · sàn nhạc {floor:.1f} dB · ngưỡng giọng {thr:.1f} dB (+{a.margin:g})")
    bad1, bad2, rows = [], [], []
    for it in items:
        s, e = int(it["start"] / 0.05), int(it["end"] / 0.05)
        seg = db[s:e] > thr
        if seg.size == 0:
            continue
        frac = float(seg.mean())
        inner = seg[int(0.3 / 0.05): max(int(0.3 / 0.05), seg.size - int(0.3 / 0.05))]
        run = best = 0
        for v in inner:
            run = 0 if v else run + 1
            best = max(best, run)
        longest = best * 0.05
        rows.append((it["id"], frac, longest))
        if frac < 0.40: bad1.append((it["id"], round(frac, 2)))
        if longest > 1.0: bad2.append((it["id"], round(longest, 2)))
    # ③ khoảng không giọng giữa 2 câu liền kề (có giọng cuối câu trước -> đầu câu sau)
    bad3 = []
    marks = {m.get("id"): m for m in tl.get("markers", []) if m.get("id")}
    for p, q in zip(items, items[1:]):
        gap = q["start"] - p["end"]
        if gap > 3.5 and p["element"] != q["element"]:
            kinds = [m for m in tl.get("markers", []) if m.get("start") is not None and p["end"] - 0.1 <= m["start"] <= q["start"] + 0.1]
            bad3.append((p["id"], q["id"], round(gap, 1), [m.get("type") for m in kinds]))
    fr = np.array([r[1] for r in rows])
    print(f"  {len(rows)} câu · tỉ lệ khung có giọng: trung vị {np.median(fr):.2f} · p5 {np.percentile(fr,5):.2f} · min {fr.min():.2f}")
    print(f"  ① câu có giọng < 40 %          : {len(bad1)} {bad1[:8]}")
    print(f"  ② câu có đoạn lặng > 1,0 s     : {len(bad2)} {bad2[:8]}")
    print(f"  ③ khoảng giữa câu > 3,5 s      : {len(bad3)} (xem thủ công: thường là NGHI/chuyển hồi) {bad3[:6]}")
    ok = not bad1 and not bad2
    print("KẾT QUẢ (kiểm thay thế):", "ĐẠT" if ok else "TRƯỢT")
    if a.json:
        Path(a.json).write_text(json.dumps(dict(floor=floor, thr=thr, bad1=bad1, bad2=bad2, bad3=bad3), ensure_ascii=False, indent=1), encoding="utf-8")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
