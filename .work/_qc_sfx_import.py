#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC các file SFX vừa nhập: định dạng, thời lượng, đỉnh âm lượng."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFP = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
PROV = ROOT / "provenance.json"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def probe(p):
    r = subprocess.run([str(FFP), "-v", "error", "-show_entries",
                        "format=duration,size:stream=codec_name,sample_rate,channels",
                        "-of", "json", str(p)], capture_output=True, text=True)
    d = json.loads(r.stdout or "{}")
    st = (d.get("streams") or [{}])[0]
    fmt = d.get("format") or {}
    return {"codec": st.get("codec_name"), "sr": st.get("sample_rate"),
            "ch": st.get("channels"), "dur": float(fmt.get("duration") or 0),
            "size": int(fmt.get("size") or 0)}


def maxvol(p):
    r = subprocess.run([str(FF), "-hide_banner", "-i", str(p), "-af", "volumedetect",
                        "-f", "null", "-"], capture_output=True, text=True, errors="replace")
    m = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else None


def main():
    prov = json.load(open(PROV, encoding="utf-8"))
    ytb = [e for e in prov if e.get("cat_goc") and e.get("track_youtube")
           and e.get("file", "").startswith("assets/sfx/")]
    print("So muc provenance YouTube: %d" % len(ytb))
    bad = 0
    for e in sorted(ytb, key=lambda x: x["file"]):
        p = ROOT / e["file"]
        if not p.exists():
            print("MISSING  %s" % e["file"])
            bad += 1
            continue
        pr = probe(p)
        mv = maxvol(p)
        ok = (pr["codec"] == "pcm_s16le" and pr["sr"] == "44100" and pr["ch"] == 2
              and pr["dur"] >= 0.5 and mv is not None and mv <= -0.5)
        flag = "OK " if ok else "BAD"
        if not ok:
            bad += 1
        print("%s %-44s %5.1fs  %s %sHz %sch  peak=%s dBFS  <- %s"
              % (flag, e["file"].replace("assets/sfx/", ""), pr["dur"], pr["codec"],
                 pr["sr"], pr["ch"], ("%.1f" % mv) if mv is not None else "?", e["track_youtube"]))
    print("--- %d/%d file dat yeu cau ---" % (len(ytb) - bad, len(ytb)))


if __name__ == "__main__":
    main()
