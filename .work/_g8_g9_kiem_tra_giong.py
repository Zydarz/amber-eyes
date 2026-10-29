#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O — PHA 3: G8 (danh tinh giong) + G9 (tach bach voi Host) cho ung vien thay the vai D.

Dung chinh `audios_understand` mu nhu voice_role_check.py:
  G8: gop 15 cau cua ung vien -> hoi "SPEAKERS: <n>"  -> dat neu n == 1
  G9: xen ke Host (audio T2) · ung vien D · Chuyen gia (audio T2) -> hoi SPEAKERS + rating 1-10
"""
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_EP"] = "02"
ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
P2 = WORK / "cer_xac_minh_giong_nam"
OUT = WORK / "g8_g9_kiem_tra_giong"
AUDIO = WORK / "audio_s_t02"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"


def mcode(args, timeout=900):
    for n in range(4):
        p = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        if p.returncode == 0:
            return json.loads(p.stdout)
        time.sleep(10 * (n + 1))
    raise RuntimeError((p.stderr or p.stdout or "")[:300])


def fname(sid):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}.mp3"


def safe(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s)[:40]


def join(paths, out):
    args = [str(FF), "-y", "-v", "error"]
    for p in paths:
        args += ["-i", str(p)]
    n = len(paths)
    parts = "".join(f"[{i}:a]aresample=32000,aformat=channel_layouts=mono,apad=pad_dur=1.0[a{i}];" for i in range(n))
    parts += "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[o]"
    subprocess.run(args + ["-filter_complex", parts, "-map", "[o]", "-c:a", "libmp3lame", "-b:a", "128k", str(out)],
                   check=True)


def ask(path, prompt):
    url = mcode(["upload-temp-url", str(path)], 300)["temp_url"]
    af = OUT / "_q.json"
    af.write_text(json.dumps({"audio_info": [{"url": url, "mime_type": "audio/mpeg", "prompt": prompt}]},
                              ensure_ascii=False), encoding="utf-8")
    r = mcode(["connector", "call", "connector__matrix__audios_understand", "--args-file", str(af)])
    return (r.get("results") or [{}])[0].get("description", json.dumps(r)[:400])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    items = json.loads((WORK / "tts_manifest_t02.json").read_text(encoding="utf-8"))
    H = [it for it in items if it["role"] == "H"]
    D = [it for it in items if it["role"] == "D"]
    C = [it for it in items if it["role"] == "C"]

    def pick(lst, n):
        step = max(1, len(lst) // n)
        return lst[::step][:n]

    ph, pc = pick(H, 4), pick(C, 4)
    pd_ = pick(D, 4)

    md = ["# PHA 3 — G8 (danh tinh) + G9 (tach bach) cho ung vien vai Dieu tra vien", ""]
    results = {}

    # ---------- BASELINE: giong dang dung (audio T2) ----------
    trio_paths = []
    for i in range(4):
        trio_paths += [AUDIO / fname(ph[i]["id"]), AUDIO / fname(pd_[i]["id"]), AUDIO / fname(pc[i]["id"])]
    f = OUT / "trio_baseline.mp3"
    join(trio_paths, f)
    ans = ask(f, "12 Vietnamese readings ~1 s apart, 3 different speakers repeating in order "
                 "(S1 narrator, S2 investigator, S3 psychologist). Ignore words; judge VOICE IDENTITY. "
                 "First line exactly 'SPEAKERS: <number>'. Then label each speaker S1/S2/S3, describe each "
                 "in 5 words, and rate 1-10 how clearly distinct they are.")
    m = re.search(r"SPEAKERS:\s*(\d+)", ans)
    results["BASELINE Korean_ColdYoungMan"] = {"speakers": int(m.group(1)) if m else -1, "g9": ans}
    md += ["## BASELINE — `Korean_ColdYoungMan` (audio thành phẩm T2)", "", ans, ""]
    print("BASELINE xong", flush=True)

    # ---------- tung ung vien ----------
    p2rows = json.loads((P2 / "rows2.json").read_text(encoding="utf-8"))
    for vi, vid in enumerate(sorted({r["cand"] for r in p2rows} - {"Korean_ColdYoungMan (audio T2)"})):
        files = sorted((P2.glob(f"p2_*_{safe(vid)}_*.mp3")))
        if len(files) < 10:
            print(f"  !! {vid}: chi {len(files)} file, bo qua", flush=True)
            continue
        # --- G8: gop 12 cau cua ung vien ---
        g8f = OUT / f"g8_{safe(vid)}.mp3"
        join(files[:12], g8f)
        ans8 = ask(g8f, "This file has 12 short Vietnamese sentences separated by ~1 s silence, all by ONE narrator. "
                         "Ignore the words; judge only VOICE IDENTITY (timbre, age, accent). "
                         "First line exactly: 'SPEAKERS: <number>'. "
                         "Then list any sentence numbers that sound like a different person and why (one line each).")
        m8 = re.search(r"SPEAKERS:\s*(\d+)", ans8)
        n8 = int(m8.group(1)) if m8 else -1
        print(f"  {vid}: G8 -> {n8} nguoi", flush=True)

        # --- G9: xen ke Host · ung vien · Chuyen gia ---
        trio = []
        for i in range(4):
            trio += [AUDIO / fname(ph[i]["id"]), files[i], AUDIO / fname(pc[i]["id"])]
        g9f = OUT / f"trio_{safe(vid)}.mp3"
        join(trio, g9f)
        ans9 = ask(g9f, "12 Vietnamese readings ~1 s apart, 3 different speakers repeating in order "
                        "(S1 narrator, S2 investigator, S3 psychologist). Ignore words; judge VOICE IDENTITY. "
                        "First line exactly 'SPEAKERS: <number>'. Then label each speaker S1/S2/S3, describe each "
                        "in 5 words, and rate 1-10 how clearly distinct they are.")
        m9 = re.search(r"SPEAKERS:\s*(\d+)", ans9)
        n9 = int(m9.group(1)) if m9 else -1
        rating = re.search(r"\b(10|[1-9])\b\s*(?:/\s*10|out of 10)?", ans9)
        print(f"  {vid}: G9 -> {n9} nguoi", flush=True)

        results[vid] = {"g8_speakers": n8, "g8": ans8, "g9_speakers": n9, "g9": ans9}
        md += [f"## `{vid}`", "",
               f"**G8 (danh tinh): {'ĐẠT' if n8 == 1 else 'KHÔNG ĐẠT'} — {n8} người**", "", ans8, "",
               f"**G9 (tach bach voi Host + Chuyen gia): {n9} người**", "", ans9, ""]

    (OUT / "report.md").write_text("\n".join(md), encoding="utf-8")
    (OUT / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
