#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R — Do Host (H) va Chuyen gia (C) tren 20 cau cua chinh ho (audio thanh pham, 0 TTS)
de so sanh cong bang 3 vai voi ung vien moi cua vai D."""
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_EP"] = "02"
WORK = Path(__file__).resolve().parents[1] / ".work"
OUT = WORK / "cer_xac_minh_giong_nam"
AUDIO = WORK / "audio_s_t02"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
sys.path.insert(0, str(WORK))
import tts_sentences as TS  # noqa: E402

BLOCK = re.compile(r"(This request was blocked.*|You can \[send feedback\].*)$", re.S)


def fname(sid):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}.mp3"


def norm(t):
    t = unicodedata.normalize("NFC", t.lower())
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def cer(ref, hyp):
    a, b = norm(ref), norm(hyp)
    if not a:
        return 0.0
    d = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(b) + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (a[i - 1] != b[j - 1]))
            prev = cur
    return d[-1] / len(a)


def mcode(args, timeout=600):
    for n in range(3):
        p = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        if p.returncode == 0:
            return json.loads(p.stdout)
        import time
        time.sleep(5 * (n + 1))
    raise RuntimeError((p.stderr or p.stdout or "")[:300])


def asr_url(url, tag):
    cache = OUT / f"asr_{tag}.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    af = OUT / f"req_{tag}.json"
    af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg",
                                             "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
                              ensure_ascii=False), encoding="utf-8")
    tr = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600)
    cache.write_text(json.dumps(tr, ensure_ascii=False), encoding="utf-8")
    return tr


def hyp_of(tr):
    s = (tr.get("transcription") or tr.get("text") or "") if isinstance(tr, dict) else str(tr)
    return BLOCK.sub("", s).strip()


def f0_median(path, sr=16000):
    r = subprocess.run([str(FF), "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr),
                        "-f", "s16le", "-"], capture_output=True)
    if not r.stdout:
        return 0.0
    x = np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768
    win, hop, out = int(0.04 * sr), int(0.01 * sr), []
    for s in range(0, len(x) - win, hop):
        f = x[s:s + win]
        if np.sqrt((f ** 2).mean()) < 0.02:
            continue
        f = f - f.mean()
        ac = np.correlate(f, f, "full")[win - 1:]
        lo, hi = int(sr / 400), int(sr / 70)
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.3 * ac[0]:
            out.append(sr / k)
    return float(np.median(out)) if out else 0.0


items = json.loads((WORK / "tts_manifest_t02.json").read_text(encoding="utf-8"))
allrows = []
for role, vid in (("H", "English_CaptivatingStoryteller"), ("C", "English_AssertiveQueen")):
    rl = [it for it in items if it["role"] == role]
    step = max(1, len(rl) // 20)
    sub = rl[::step][:20]
    for it in sub:
        f = AUDIO / fname(it["id"])
        if not f.exists():
            continue
        tag = f"prod_{fname(it['id'])[:-4]}"
        try:
            url = mcode(["get_asset_url", mcode(["upload_temp_url", str(f)], 300)["node_id"]], 180)["download_url"] \
                if False else None
        except Exception:  # noqa: BLE001
            url = None
        # dung upload_temp_url + listen_audio (production file local)
        try:
            up = mcode(["upload_temp_url", str(f)], 300)
            u = up.get("temp_url") or up.get("url")
            tr = asr_url(u, tag)
        except Exception as e:  # noqa: BLE001
            print(f"  !! {role} {it['id']}: {e}", flush=True)
            tr = {"transcription": ""}
        h = hyp_of(tr)
        hh = TS.vi_numbers(h)
        ref = re.sub(r"<#[\d.]+#>", " ", it["text"]).strip()
        allrows.append({"cand": f"{role} · {vid} (audio T2)", "role": role, "id": it["id"],
                        "ref": ref, "hyp": hh, "cer": cer(ref, hh), "f0": f0_median(f)})
    print(f"xong vai {role}: {sum(1 for x in allrows if x['role'] == role)} cau", flush=True)

(OUT / "rows_hc.json").write_text(json.dumps(allrows, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Host & Chuyen gia — 20 cau moi (audio thanh pham)", "",
      "| vai | n | CER tb | median | max | >2% | F0 |", "|---|---:|---:|---:|---:|---:|---:|"]
for role in ("H", "C"):
    rs = [x for x in allrows if x["role"] == role]
    if not rs:
        continue
    cs = sorted(x["cer"] for x in rs)
    f0s = sorted(x["f0"] for x in rs if x["f0"])
    md.append(f"| {role} | {len(cs)} | {100*sum(cs)/len(cs):.1f}% | {100*cs[len(cs)//2]:.1f}% | "
              f"{100*cs[-1]:.1f}% | {sum(1 for c in cs if c>0.02)}/{len(cs)} | {f0s[len(f0s)//2]:.0f} Hz |")
md.append("")
for role in ("H", "C"):
    md.append(f"## Vai {role} — cau loi")
    md.append("")
    md.append("| id | CER | từ | Nghe được |")
    md.append("|---|---:|---:|---|")
    for x in sorted([y for y in allrows if y["role"] == role], key=lambda y: -y["cer"]):
        if x["cer"] <= 0:
            continue
        md.append(f"| `{x['id']}` | {100*x['cer']:.1f}% | {len(norm(x['ref']).split())} | {x['hyp'][:100]} |")
    md.append("")
(OUT / "report_hc.md").write_text("\n".join(md), encoding="utf-8")
print("\n".join(md))
