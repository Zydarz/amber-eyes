#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collector MOT LAN: don file MP3 trong Downloads -> inbox.

QUAN TRONG: Chrome ghi file tam la <guid>.tmp, khi tai xong doi ten thanh
<Ten Track>.mp3. => phai quet ca hai dang:
  - *.mp3 : khop theo TEN TRACK (chinh xac, khong phan biet hoa thuong) -> chinh xac nhat
  - *.tmp : khop theo thoi luong (floor(dur) hoac |thuc - manifest| <= 0.75s)

Dung: py -3 .work/_yt_collect.py
"""
import json
import math
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = Path.home() / "Downloads"
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
REJECT = INBOX / "_reject"
MAP = ROOT / ".work" / "yt_map.tsv"
STATE = ROOT / ".work" / "yt_watch_state.json"
LOG = ROOT / ".work" / "yt_collect.log"
FFP = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"


def log(msg):
    line = time.strftime("%H:%M:%S") + " " + msg
    print(line, flush=True)
    try:
        with LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:  # noqa: BLE001
        pass


def load_map():
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
        out.append({"track": p[0].strip(), "ma": p[1].strip(), "dur": dur})
    return out


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
    return s2 if s2 == s1 else 0


def deliver(src, entry, how):
    ma = entry["ma"]
    dst = INBOX / (ma + ".mp3")
    if dst.exists():
        conf = INBOX / "_conflict"
        conf.mkdir(parents=True, exist_ok=True)
        alt = conf / (ma + "_" + src.stem + ".mp3")
        shutil.move(str(src), str(alt))
        log(f"DUP   {src.name} -> {dst.name} da co, giu o {alt.name}")
        return True
    shutil.move(str(src), str(dst))
    log(f"MOVED {src.name} -> {dst.relative_to(ROOT)} ({dst.stat().st_size} bytes)"
        f"  [{entry['track']}] {how}")
    return True


def reject(src, why):
    REJECT.mkdir(parents=True, exist_ok=True)
    dst = REJECT / src.name
    shutil.move(str(src), str(dst))
    log(f"REJECT {src.name} ({why}) -> {dst.name}")


def pick_by_dur(pending, d):
    """Khop theo thoi luong. CHI tra ve 1 ung vien duy nhat.

    Neu nhieu dong manifest cung co floor(dur) giong nhau => AMBIGUOUS -> bo qua
    (de lai file .tmp cho lan collector sau) de khong gan nham.
    """
    fd = math.floor(d)
    cands = [e for e in pending
             if e["dur"] > 0 and (abs(e["dur"] - d) <= 0.75 or math.floor(e["dur"]) == fd)]
    if len(cands) == 1:
        return cands[0]
    if len(cands) > 1:
        best = min(cands, key=lambda e: abs(e["dur"] - d))
        others = [c for c in cands if c is not best and abs(c["dur"] - d) < 0.3]
        if not others:
            return best
        log(f"AMBIG floor({fd}) co {len(cands)} dong -> bo qua, de lai file .tmp")
        return None
    return None


def main():
    INBOX.mkdir(parents=True, exist_ok=True)
    st = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"used": []}
    used = set(st.get("used", []))
    mp = load_map()
    pending = [e for e in mp if e["ma"] not in used and e["track"]]

    by_name = {}
    for e in pending:
        by_name.setdefault(e["track"].strip().lower(), []).append(e)

    n_moved = n_reject = 0

    # 1) File da hoan tat: <Ten Track>.mp3 -> khop theo ten.
    #    Loop nhieu lan: Chrome doi ten .tmp -> .mp3 khi tai xong, nen phai cho.
    for _round in range(10):
        moved_now = 0
        for f in sorted(DOWNLOADS.glob("*.mp3")):
            stem = f.stem.strip()
            # Chrome them "(1)", "(2)" hoac " 1" khi trung ten -> bo suffix de khop
            base = re.sub(r"\s*(?:\(\d+\)|\d+)$", "", stem)
            cands = by_name.get(stem.lower()) or by_name.get(base.lower()) or []
            if not cands:
                continue
            if len(cands) > 1:
                # cung ten nhieu dong manifest -> phan biet bang thoi luong thuc
                d = probe_duration(f)
                cands = sorted(cands, key=lambda e: abs(e["dur"] - d))
                if len(cands) > 1 and abs(cands[0]["dur"] - d) < 0.3 and abs(cands[1]["dur"] - d) < 0.3:
                    log(f"AMBIG ten '{stem}' -> bo qua")
                    continue
            e = cands[0]
            deliver(f, e, "ten")
            used.add(e["ma"])
            pending.remove(e)
            by_name[e["track"].strip().lower()] = [
                x for x in by_name[e["track"].strip().lower()] if x is not e]
            moved_now += 1
            n_moved += 1
        if moved_now == 0 and not list(DOWNLOADS.glob("*.tmp")):
            break
        if moved_now == 0:
            time.sleep(2.5)
        else:
            time.sleep(1.0)

    # 2) File tam dang tai: <guid>.tmp -> khop theo thoi luong
    tmps = sorted(DOWNLOADS.glob("*.tmp"), key=lambda p: p.stat().st_mtime)
    for tmp in tmps:
        if not stable_size(tmp):
            log(f"SKIP  {tmp.name} (dichuyen khong on dinh)")
            continue
        d = probe_duration(tmp)
        if d <= 0.2:
            continue
        best = pick_by_dur(pending, d)
        if best is None:
            reject(tmp, f"khong co dong manifest khop floor({d:.2f})={math.floor(d)}")
            n_reject += 1
            continue
        pending.remove(best)
        used.add(best["ma"])
        deliver(tmp, best, "thoi luong")
        n_moved += 1

    st["used"] = sorted(used)
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"=== xong: chuyen {n_moved}, reject {n_reject}, used={len(used)} ===")


if __name__ == "__main__":
    main()
