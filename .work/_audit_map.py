#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit mapping inbox <-> manifest.

Kiem tra 2 dieu kien cho tung file mp3 trong 02_SAN_XUAT/sfx_youtube:
 1) THOI LUONG: floor(thoi luong that) == floor(thoi luong ghi trong manifest).
    (YouTube hien thi thoi luong lam tron xuong, nen day la dieu kien chat chan
    de file dang nam sai track)
 2) TRUNG NOI DUNG: 2 file khac ma ma co cung MD5 -> mot trong hai sai.

Ket qua ghi ra console + .work/map_audit.json
"""
import hashlib
import json
import math
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
MAP = ROOT / ".work" / "yt_map.tsv"
FFP = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"


def load_map():
    rows = []
    for raw in MAP.read_text(encoding="utf-8-sig").splitlines():
        if not raw.strip():
            continue
        p = (raw.split("\t") + [""] * 6)[:6]
        try:
            dur = float(p[5]) if p[5].strip() else 0.0
        except ValueError:
            dur = 0.0
        rows.append({"track": p[0].strip(), "ma": p[1].strip(), "dur": dur,
                     "loai": p[2].strip(), "genre": p[4].strip()})
    return rows


def dur_of(p):
    import subprocess
    r = subprocess.run([str(FFP), "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", str(p)],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    mp = load_map()
    by_ma = {}
    for r in mp:
        by_ma[r["ma"]] = r               # dong MOI ghi de dong cu
    files = sorted(INBOX.glob("*.mp3"))
    res = {"check": [], "bad_duration": [], "dupe": []}
    hashes = {}
    for f in files:
        ma = f.stem
        d = dur_of(f)
        row = by_ma.get(ma)
        md = md5(f)
        hashes.setdefault(md, []).append(ma)
        item = {"ma": ma, "file": f.name, "dur_real": round(d, 2),
                "track": row["track"] if row else None,
                "dur_manifest": row["dur"] if row else None}
        if row is None:
            item["issue"] = "khong co trong manifest"
            res["bad_duration"].append(item)
            continue
        if row["dur"] > 0 and math.floor(d) != math.floor(row["dur"]):
            item["issue"] = "LECH THOI LUONG: that=floor%.0f manifest=floor%.0f" % (
                d, row["dur"])
            res["bad_duration"].append(item)
        res["check"].append(item)
    for md, mas in hashes.items():
        if len(mas) > 1:
            res["dupe"].append({"md5": md[:10], "ma": mas})
    (ROOT / ".work" / "map_audit.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print("=== LECH THOI LUONG (%d) ===" % len(res["bad_duration"]))
    for it in res["bad_duration"]:
        print("  %-34s that=%-8.2f manifest=%-8s  track=%s  | %s" % (
            it["ma"], it["dur_real"], it["dur_manifest"], it["track"], it.get("issue", "")))
    print("=== TRUNG NOI DUNG (%d) ===" % len(res["dupe"]))
    for it in res["dupe"]:
        print("  %s : %s" % (it["md5"], ", ".join(it["ma"])))
    ok = len(res["check"]) - len(res["bad_duration"])
    print("=== TONG %d file, %d khop, %d lech ===" % (len(res["check"]), ok, len(res["bad_duration"])))


if __name__ == "__main__":
    main()
