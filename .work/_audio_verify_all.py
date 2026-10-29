#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify noi dung that cua cac file MP3 trong inbox bang audios_understand.

Moi file duoc upload -> audios_understand (toi da 5 file/lan) -> ket qua ghi vao
.work/audio_verify.json va in ra bang markdown de doi chieu voi ten track.

Dung: py -3 .work/_audio_verify_all.py [thu_muc_inbox] [so_file_toi_da]
"""
import json
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\Audi")
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
OUT = ROOT / ".work" / "audio_verify.json"

CATS = ("crowd/people | crowd-cheering | machine/mechanical | vehicle | footsteps | "
        "glass-break | water/liquid | paper/fabric | metal-clang | animal | "
        "music/tone/siren | wind/weather | indoor-ambience | door | typing/keys | "
        "gun/impact | click/beep | breathing/voice | other")

PROMPT = (
    "Listen to this clip and answer with exactly two lines:\n"
    "CATEGORY: <one of: " + CATS + ">\n"
    "DESC: <at most 12 words describing the main sound>\n"
    "Be concrete. If the clip is silent, say SILENT."
)


def run(cmd):
    return subprocess.run(subprocess.list2cmdline(cmd), shell=True,
                          capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def upload(path):
    r = run(["mcode-tools", "upload_temp_url", str(path)])
    if r.returncode != 0:
        raise RuntimeError("upload fail: %s" % r.stderr[:300])
    return json.loads(r.stdout)["temp_url"]


def call_batch(paths):
    audio_info = []
    for p in paths:
        audio_info.append({"url": upload(p), "prompt": PROMPT})
    ap = ROOT / ".work" / "_audio_args.json"
    ap.write_text(json.dumps({"audio_info": audio_info}, ensure_ascii=False), encoding="utf-8")
    r = run(["mcode-tools", "connector", "call",
             "connector__matrix__audios_understand", "--args-file", str(ap)])
    try:
        return json.loads(r.stdout)
    except Exception:  # noqa: BLE001
        return {"error": r.stdout[:500] + r.stderr[:500]}


def main():
    inbox = Path(sys.argv[1]) if len(sys.argv) > 1 else INBOX
    files = sorted(inbox.glob("*.mp3"))
    res = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    todo = [f for f in files if f.name not in res]
    print("da co: %d / can kiem tra: %d" % (len(res), len(todo)), flush=True)
    for i in range(0, len(todo), 5):
        chunk = [f for f in todo[i:i + 5] if f.exists()]
        if not chunk:
            continue
        out = call_batch(chunk)
        results = out.get("results") or []
        for f, rr in zip(chunk, results):
            res[f.name] = rr.get("description", "").replace("\n", " | ")
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print("[%d/%d] %s" % (min(i + 5, len(todo)), len(todo),
                              ", ".join(f.name for f in chunk)), flush=True)
    print("--- KET QUA ---")
    for k in sorted(res):
        print("%-38s %s" % (k, res[k]))


if __name__ == "__main__":
    main()
