#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nghe thử file audio bang audios_understand de kiem tra NOI DUNG that su.

Dung: py -3 .work/_audio_check.py <file1.mp3> [file2.mp3 ...]
- upload moi file -> temp_url
- goi 1 lan audios_understand voi toi da 10 file
"""
import json
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROMPT = (
    "Describe ONLY the main sound of this clip in at most 10 words. "
    "Name the concrete sound source, for example: footsteps on concrete, "
    "car engine revving, sewing machine, crowd cheering, door slamming, "
    "metal hum. If the clip is silent or ambiguous, say exactly that."
)


def run(cmd):
    # mcode-tools la file .cmd -> phai chay qua cmd.exe
    return subprocess.run(subprocess.list2cmdline(cmd), shell=True,
                          capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def upload(path):
    r = run(["mcode-tools", "upload_temp_url", path])
    if r.returncode != 0:
        raise RuntimeError("upload fail %s: %s" % (path, r.stderr[:400]))
    return json.loads(r.stdout)["temp_url"]


def main():
    files = sys.argv[1:]
    if not files:
        print("thieu file")
        return 1
    audio_info = []
    for f in files:
        try:
            audio_info.append({"url": upload(f), "prompt": PROMPT})
            print("uploaded:", Path(f).name)
        except Exception as e:  # noqa: BLE001
            print("LOI upload", f, repr(e))
    if not audio_info:
        return 1
    args = {"audio_info": audio_info}
    ap = Path(__file__).resolve().parents[1] / ".work" / "_audio_args.json"
    ap.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print("--- goi audios_understand ---")
    r = run(["mcode-tools", "connector", "call",
             "connector__matrix__audios_understand", "--args-file", str(ap)])
    print(r.stdout[:12000])
    if r.returncode != 0:
        print("ERR", r.stderr[:2000])
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
