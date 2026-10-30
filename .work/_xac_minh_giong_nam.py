#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""N — PHA 2: XAC MINH 4 ung vien tot nhat tren 15 cau day du cu vai Dieu tra vien (Tap 02).

Moi cau dung DUNG emotion + speed cua manifest (giai lap production), nen so sanh cong bang
voi baseline Korean_ColdYoungMan tren chinh audio thanh pham T2.
"""
import json
import os
import re
import subprocess
import sys
import unicodedata
import urllib.request
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_EP"] = "02"
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT = WORK / "cer_xac_minh_giong_nam"
AUDIO = WORK / "audio_s_t02"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
sys.path.insert(0, str(WORK))
import tts_sentences as TS  # noqa: E402

BLOCK = re.compile(r"(This request was blocked.*|You can \[send feedback\].*)$", re.S)
# 4 ung vien tot nhat theo phan sang loc, DA loai audiobook_male_1
# (no G8: doi danh tinh khi doi cam xuc + G9: chi cach Host 2 nua cung)
CANDS = ["English_Diligent_Man", "English_DecentYoungMan", "Korean_CockyGuy", "male-qn-qingse"]
BASELINE = "Korean_ColdYoungMan"
HOST_F0 = 102.6          # do o Tap02 (English_CaptivatingStoryteller)


def mcode(args, timeout=600):
    p = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "")[:300])
    return json.loads(p.stdout)


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


def fname(sid):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}.mp3"


def safe(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s)[:40]


def pcm(path, sr=16000):
    r = subprocess.run([str(FF), "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr),
                        "-f", "s16le", "-"], capture_output=True)
    if not r.stdout:
        return None, sr
    return np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768, sr


def f0_median(x, sr=16000):
    if x is None:
        return 0.0
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


def asr(local, tag):
    cache = OUT / f"asr_{tag}.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    up = mcode(["upload_temp_url", str(local), "--mime-type", "audio/mpeg"], 300)
    url = up.get("temp_url") or up.get("url")
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


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    items = json.loads((WORK / "tts_manifest_t02.json").read_text(encoding="utf-8"))
    dlines = [it for it in items if it["role"] == "D"]
    refs = {it["id"]: re.sub(r"<#[\d.]+#>", " ", it["text"]).strip() for it in dlines}
    print(f"Vai D Tap 02: {len(dlines)} cau\n")

    rows = []
    # ---- BASELINE: audio thanh pham (0 TTS) ----
    for it in dlines:
        f = AUDIO / fname(it["id"])
        if not f.exists():
            continue
        try:
            h = hyp_of(asr(f, f"prod_{fname(it['id'])[:-4]}"))
        except Exception:  # noqa: BLE001
            h = ""
        hh = TS.vi_numbers(h)
        x, sr = pcm(f)
        rows.append({"cand": f"{BASELINE} (audio T2)", "id": it["id"], "ref": refs[it["id"]],
                     "hyp": hh, "cer": cer(refs[it["id"]], hh), "f0": f0_median(x, sr)})
    print("xong baseline", flush=True)

    # ---- 4 ung vien: TTS voi dung emotion/speed cua tung cau ----
    for ci, vid in enumerate(CANDS):
        reqs = [{"text": refs[it["id"]], "voice_id": vid, "emotion": it["emotion"], "speed": it["speed"],
                 "pitch": it.get("pitch", 0), "volume": 1.0,
                 "output_file": f"p2_{ci:02d}_{safe(vid)}_{it['id'].replace('.', '_').replace('#', '-')}"}
                for it in dlines]
        af = OUT / f"tts_{ci:02d}_{safe(vid)}.json"
        af.write_text(json.dumps({"requests": reqs}, ensure_ascii=False), encoding="utf-8")
        try:
            res = mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)], 900)
        except Exception as e:  # noqa: BLE001
            print(f"  !! {vid}: TTS fail {e}", flush=True)
            continue
        got = 0
        for ok_i in res.get("success_items", []):
            fn = ok_i["file_name"]
            tid = next((it["id"] for it in dlines
                        if it["id"].replace(".", "_").replace("#", "-") in fn), None)
            if tid is None:
                continue
            try:
                url = mcode(["get_asset_url", ok_i["node_id"]], 180)["download_url"]
            except Exception:  # noqa: BLE001
                continue
            local = OUT / fn
            urllib.request.urlretrieve(url, local)
            tag = f"p2_{ci:02d}_{safe(vid)}_{tid.replace('.', '_').replace('#', '-')}"
            try:
                h = hyp_of(asr(local, tag))
            except Exception:  # noqa: BLE001
                h = ""
            hh = TS.vi_numbers(h)
            x, sr = pcm(local)
            rows.append({"cand": vid, "id": tid, "ref": refs[tid], "hyp": hh,
                         "cer": cer(refs[tid], hh), "f0": f0_median(x, sr)})
            got += 1
        print(f"  [{ci+1}/{len(CANDS)}] {vid}: {got}/{len(dlines)} cau", flush=True)

    (OUT / "rows.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

    g2 = {}
    for r in rows:
        g2.setdefault(r["cand"], []).append(r)
    summ = []
    for c, rs in g2.items():
        cs = sorted(x["cer"] for x in rs)
        f0s = [x["f0"] for x in rs if x["f0"]]
        med_f0 = sorted(f0s)[len(f0s) // 2] if f0s else 0
        summ.append({"cand": c, "n": len(cs), "med": cs[len(cs) // 2], "mean": sum(cs) / len(cs),
                     "max": cs[-1], "over": sum(1 for x in cs if x > 0.02),
                     "f0": med_f0, "gap": 12 * np.log2(med_f0 / HOST_F0) if med_f0 else 0, "rows": rs})
    summ.sort(key=lambda s: s["mean"])
    md = ["# PHA 2 — Xac minh ung vien cho vai Dieu tra vien (Tap 02, 15 cau)", "",
          "Moi cau dung DUNG emotion + speed cua manifest (giai lap production).",
          f"Baseline = audio thanh pham cua `{BASELINE}`. Host F0 = {HOST_F0} Hz (do o) → cot 'cach Host' la nua cung.",
          "", "| # | voice_id | n | CER tb | CER median | CER max | >2% | F0 | cach Host |",
          "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for i, s in enumerate(summ, 1):
        md.append(f"| {i} | `{s['cand']}` | {s['n']} | {100*s['mean']:.1f}% | {100*s['med']:.1f}% | "
                  f"{100*s['max']:.1f}% | {s['over']}/{s['n']} | {s['f0']:.0f} Hz | {s['gap']:+.1f} |")
    md.append("")
    for s in summ:
        md.append(f"## `{s['cand']}` — tb {100*s['mean']:.1f}% · median {100*s['med']:.1f}% · "
                  f"max {100*s['max']:.1f}% · F0 {s['f0']:.0f} Hz · cach Host {s['gap']:+.1f} nua cung")
        md.append("")
        md.append("| id | CER | F0 | Nghe được |")
        md.append("|---|---:|---:|---|")
        for x in sorted(s["rows"], key=lambda y: -y["cer"]):
            if x["cer"] <= 0:
                continue
            md.append(f"| `{x['id']}` | {100*x['cer']:.1f}% | {x['f0']:.0f} | {x['hyp'][:110]} |")
        md.append("")
    (OUT / "report.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
