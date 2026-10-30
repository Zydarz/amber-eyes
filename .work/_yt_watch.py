#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Watcher: nhận MP3 tải từ YouTube Studio -> Thư viện âm thanh, đưa về inbox.

Vì sao cần script này: khi automation bấm nút "Tải xuống", Chromium mở một
navigation tới file mp3 rồi bị abort (net::ERR_ABORTED) — nội dung vẫn tải
đủ nhưng file nằm lại dưới tên GUID `.tmp` và không bao giờ được đổi tên.

QUY TẮC GÁN FILE (đã sửa sau khi phát hiện gán nhầm):
  Thư viện hiển thị thời lượng làm TRÒN XUỐNG, nên
        floor(thoi luong_that)  ==  floor(thoi luong_trong_manifest)
  là điều kiện khớp CHẮN CHẮN. File nào không khớp được đưa sang
  02_SAN_XUAT/sfx_youtube/_reject/ và KHÔNG tiêu thụ dòng manifest,
  để bấm tải lại được.

  Thứ tự ưu tiên: đầu hàng đợi trước (manifest ghi đúng thứ tự bấm), nếu
  không khớp thì quét phía sau tìm dòng có cùng floor(thoi luong).

Manifest (.work/yt_map.tsv), phân tách bằng TAB:
    tên_track <TAB> mã_sfx <TAB> loại <TAB> thư_mục_đích <TAB> thể_loại_youtube <TAB> thời_lượng_giây

Chạy:  py -3 .work/_yt_watch.py
"""
import json
import math
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = Path(os.environ["USERPROFILE"]) / "Downloads"
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
REJECT = INBOX / "_reject"
MAP = ROOT / ".work" / "yt_map.tsv"
LOG = ROOT / ".work" / "yt_watch.log"
FFP = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
STATE = ROOT / ".work" / "yt_watch_state.json"


def log(msg):
    line = time.strftime("%H:%M:%S") + " " + msg
    try:
        print(line, flush=True)
    except Exception:  # noqa: BLE001  (console cp1252 không in được tiếng Việt)
        pass
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:  # noqa: BLE001
        pass


def load_map():
    """[{track, ma, loai, dest, genre, dur}] theo thứ tự thêm vào."""
    out = []
    if not MAP.exists():
        return out
    for raw in MAP.read_text(encoding="utf-8-sig").splitlines():
        raw = raw.rstrip()
        if not raw.strip() or raw.startswith("#"):
            continue
        p = (raw.split("\t") + [""] * 6)[:6]
        try:
            dur = float(p[5]) if p[5].strip() else 0.0
        except ValueError:
            dur = 0.0
        out.append({"track": p[0].strip(), "ma": p[1].strip(), "loai": p[2].strip(),
                    "dest": p[3].strip(), "genre": p[4].strip(), "dur": dur})
    return out


def load_state():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            return {"used": []}
    return {"used": []}


def save_state(st):
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")


def probe_duration(p):
    r = subprocess.run([str(FFP), "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", str(p)],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def stable_size(p, wait=1.2):
    s1 = p.stat().st_size
    time.sleep(wait)
    s2 = p.stat().st_size
    return s2 if s1 == s2 else 0


def deliver(src, entry, rename_to=None):
    ma = entry["ma"]
    dest_dir = (ROOT / entry["dest"]) if entry["dest"] else INBOX
    dest_dir.mkdir(parents=True, exist_ok=True)
    dst = dest_dir / (ma + ".mp3")
    if dst.exists():
        conf = INBOX / "_conflict"
        conf.mkdir(parents=True, exist_ok=True)
        alt = conf / (ma + "_" + src.stem + ".mp3")
        try:
            shutil.move(str(src), str(alt))
            log("DUP   %s -> %s đã có, giữ ở %s" % (src.name, dst.name, alt.name))
        except OSError as e:
            log("ERR dup %s: %r" % (src.name, e))
        return True
    if rename_to:
        tmp = src.with_name(rename_to)
        try:
            src.rename(tmp)
        except OSError as e:
            log("ERR rename %s: %r" % (src.name, e))
            return False
        src = tmp
    size = src.stat().st_size
    shutil.move(str(src), str(dst))
    log("MOVED %s -> %s (%d bytes)" % (src.name, dst.relative_to(ROOT), size))
    return True


def reject(src, why):
    REJECT.mkdir(parents=True, exist_ok=True)
    dst = REJECT / src.name
    try:
        shutil.move(str(src), str(dst))
    except OSError as e:
        log("ERR reject %s: %r" % (src.name, e))
        return
    log("REJECT %s (%s) -> %s" % (src.name, why, dst.name))


def pick(pending, d):
    """Chọn dòng manifest khớp file có thời lượng d.

    Thư viện hiển thị thời lượng làm tròn, mp3 đo được có thể lệch ~0.01-0.1s
    (encoder delay) -> chấp nhận dung sai 0.75s HOẶC cùng floor().
    """
    fd = math.floor(d)
    head = pending[0]

    def ok(e):
        return (e["dur"] > 0 and
                (abs(e["dur"] - d) <= 0.75 or math.floor(e["dur"]) == fd))

    if ok(head):
        return head
    for e in pending[1:]:
        if ok(e):
            return e
    return None


def main():
    INBOX.mkdir(parents=True, exist_ok=True)
    log("=== watcher bat dau (downloads=%s) ===" % DOWNLOADS)
    st = load_state()
    while True:
        try:
            mp = load_map()
            used = set(st.get("used", []))
            pending = [e for e in mp if e["ma"] not in used and e["track"]]
            for tmp in sorted(DOWNLOADS.glob("*.tmp"), key=lambda p: p.stat().st_mtime):
                if not stable_size(tmp):
                    continue
                d = probe_duration(tmp)
                if d <= 0.2:
                    continue
                best = pick(pending, d)
                if best is None:
                    reject(tmp, "khong co dong manifest khop floor(%.2f)=%d" % (d, math.floor(d)))
                    continue
                pending.remove(best)
                used.add(best["ma"])
                st["used"] = sorted(used)
                save_state(st)
                deliver(tmp, best, rename_to=best["track"] + ".mp3")
            # 2) file .mp3 đã đúng tên (Chromium đổi tên được)
            for f in DOWNLOADS.glob("*.mp3"):
                hit = next((e for e in mp if e["track"].lower() == f.stem.lower()), None)
                if hit is None:
                    continue
                if hit["ma"] in used and (INBOX / (hit["ma"] + ".mp3")).exists():
                    continue
                if not stable_size(f):
                    continue
                used.add(hit["ma"])
                st["used"] = sorted(used)
                save_state(st)
                deliver(f, hit)
        except Exception as e:  # noqa: BLE001
            log("ERR " + repr(e))
        time.sleep(5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("=== watcher dung ===")
        sys.exit(0)
