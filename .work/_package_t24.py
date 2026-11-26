#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đóng gói Tập 24 (VN/EN/JA): mux hình + audio, thumbnail, cập nhật MỐC CHƯƠNG.

KHÔNG dùng `package.py --mux` cho Tập 24 vì sinh mô tả sẽ HỎNG:
  - VN : package.description() sinh mô tả rút gọn → mất khối "10 chỉ dấu" đã viết.
  - EN : description_en() đọc `CHU_CO_DINH_EN.md` — Tập 24 KHÔNG có file này ⇒ crash.
  - JA : description_ja() lấy `EPISODES["24"]["title"]` là tiếng Việt ⇒ in tiếng Việt.
→ Ở đây chỉ MUX + THUMBNAIL (dùng lại đúng hàm của package.py) và THAY MỐC CHƯƠNG
  trong file mô tả sẵn có bằng mốc đo thật từ timeline từng ngôn ngữ.

Dùng:  AE_EP=24 AE_LANG=vi|en|ja  py -3 .work/_package_t24.py
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))

import edition as ED  # noqa: E402

FF = (Path(shutil.which("ffmpeg")) if shutil.which("ffmpeg")
      else WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe")


def mmss(t):
    """mm:ss — làm tròn giây (không cắt cụt), giống package.mmss."""
    total = int(t + 0.5)
    return f"{total // 60:02d}:{total % 60:02d}"


def act_starts(tl):
    """Mốc bắt đầu thật của từng hồi = câu thoại ĐẦU TIÊN của hồi đó."""
    starts = {}
    for it in tl.get("items", []):
        a = it.get("act")
        if a and a not in starts:
            starts[a] = it["start"]
    if not starts:
        for m in tl.get("markers", []):
            if m["type"] == "ACT":
                starts.setdefault(m["act"], m["start"])
    return starts


def mux():
    """Hình (picture.mp4) + audio master → mp4 thành phẩm. Giữ nguyên chuỗi lệnh của package.mux."""
    ED.OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = ED.OUT_DIR / (ED.MASTER + ".mp4")
    mux_af = ED.EP.get("mux_af",
                       "alimiter=limit=0.7943:attack=5:release=50:level=disabled")
    cmd = [str(FF), "-y", "-v", "error", "-i", str(ED.w("video3") / "picture.mp4"),
           "-i", str(ED.w("audio_master.wav")), "-map", "0:v", "-map", "1:a", "-c:v", "copy"]
    if mux_af:
        cmd += ["-af", mux_af]
    cmd += ["-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    return out


def patch_chapters(path, times):
    """Thay mốc thời gian trong khối MỐC CHƯƠNG, GIỮ NGUYÊN nhãn và toàn bộ nội dung còn lại."""
    if not path.exists():
        return False
    txt = path.read_text(encoding="utf-8")
    lines = txt.split("\n")
    # tìm dòng tiêu đề khối chương (⏱ ...)
    hi = next((i for i, l in enumerate(lines) if l.startswith("⏱")), None)
    if hi is None:
        return False
    k, changed = 0, False
    for i in range(hi + 1, len(lines)):
        m = re.match(r"^(\d\d:\d\d)(\s.*)$", lines[i])
        if not m:
            break
        if k < len(times):
            new = times[k] + m.group(2)
            if new != lines[i]:
                lines[i] = new
                changed = True
            k += 1
    if changed:
        path.write_text("\n".join(lines), encoding="utf-8")
    return changed


def main():
    lang = os.environ.get("AE_LANG", "vi")
    tl_p = ED.w("timeline_s.json")
    tl = __import__("json").loads(tl_p.read_text(encoding="utf-8"))
    starts = act_starts(tl)
    times = ["00:00"] + [mmss(starts[a]) for a in sorted(starts)]
    print(f"[{lang}] act starts -> {times}")

    # 1) mux
    pic = ED.w("video3") / "picture.mp4"
    if not pic.exists():
        raise SystemExit(f"THIEU hinh: {pic}")
    out = mux()
    print(f"[{lang}] mux -> {out}")

    # 2) thumbnail (dùng lại hàm gốc của package.py)
    import package as PK
    PK.thumbnail()
    print(f"[{lang}] thumbnail -> {ED.OUT_DIR / 'thumbnail.png'}")

    # 3) cập nhật mốc chương trong các file mô tả đã có
    targets = [ED.OUT_DIR / "description.txt", ED.OUT_DIR / "mo_ta.txt",
               ED.EP_DIR / "mo_ta.txt", ED.EP_DIR / "description.txt"]
    for t in targets:
        if t.exists():
            print(f"[{lang}] chapters {'OK ' if patch_chapters(t, times) else 'khong doi'} -> {t}")


if __name__ == "__main__":
    main()
