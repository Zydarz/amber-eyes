#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""M — SANG LOC giong nam cho vai "Dieu tra vien" (Tap 02).

Phan 1: baseline  = Korean_ColdYoungMan tren CHINH audio thanh pham T2 (khong ton TTS).
Phan 2: 12 ung vien -> TTS 4 cau kho + ASR + do CER + do F0 -> xep hang.
        (2 giong legacy nam trong catalog nhung co the da bi go khoi danh muc.)
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
ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
OUT = WORK / "cer_sang_loc_giong_nam"
AUDIO = WORK / "audio_s_t02"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
sys.path.insert(0, str(WORK))
import tts_sentences as TS  # noqa: E402

BLOCK = re.compile(r"(This request was blocked.*|You can \[send feedback\].*)$", re.S)


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
    by_id = {it["id"]: it for it in items}

    # 4 cau thuoc vai D, uu tien cau da biet kho + cau thuan tieng Viet
    TEST = ["2.05#9", "2.05#12", "1.17#5", "3.11#3"]
    refs = {}
    for t in TEST:
        if t not in by_id:
            continue
        txt = re.sub(r"<#[\d.]+#>", " ", by_id[t]["text"]).strip()
        if by_id[t]["role"] == "D" and not re.search(r"[A-Za-z]{3,}", txt):
            refs[t] = txt
    # them 2 cau da biet kho (co the chua ten rieng -> van giu de so sanh voi baseline)
    for t in ("2.05#9", "2.05#12"):
        if t in by_id and t not in refs:
            refs[t] = re.sub(r"<#[\d.]+#>", " ", by_id[t]["text"]).strip()
    print("CAU THUOC:", list(refs.keys()))
    for k, v in refs.items():
        print(f"   {k}: {v}")
    print()

    CANDS = [
        ("male-qn-qingse", "LEGACY - bo cu, da do CER 0%"),
        ("audiobook_male_1", "LEGACY - bo cu, da do CER 0%"),
        ("English_Diligent_Man", "catalog"),
        ("English_ReservedYoungMan", "catalog"),
        ("English_DecentYoungMan", "catalog"),
        ("English_Steadymentor", "catalog"),
        ("English_PatientMan", "catalog"),
        ("English_FriendlyPerson", "catalog"),
        ("Korean_CalmGentleman", "catalog"),
        ("Korean_DominantMan", "catalog"),
        ("Korean_IntellectualMan", "catalog"),
        ("Korean_CockyGuy", "catalog"),
        ("Korean_ColdYoungMan", "BASELINE - giong dang dung"),
    ]

    rows = []
    # ---------- PHAN 1: baseline tren audio thanh pham (0 TTS) ----------
    for t, ref in refs.items():
        f = AUDIO / fname(t)
        if not f.exists():
            continue
        try:
            h = hyp_of(asr(f, f"prod_{fname(t)[:-4]}"))
        except Exception as e:  # noqa: BLE001
            h = f"(LOI {e})"
        x, sr = pcm(f)
        rows.append({"cand": "Korean_ColdYoungMan (audio T2)", "id": t, "ref": ref,
                     "hyp": TS.vi_numbers(h), "cer": cer(ref, TS.vi_numbers(h)), "f0": f0_median(x, sr)})
    print("xong baseline (audio thanh pham)", flush=True)

    # ---------- PHAN 2: 12 ung vien ----------
    for ci, (vid, note) in enumerate(CANDS):
        if vid == "Korean_ColdYoungMan":
            continue
        reqs = [{"text": refs[t], "voice_id": vid, "emotion": "neutral", "speed": 0.90,
                 "pitch": 0, "volume": 1.0, "output_file": f"{ci:02d}_{safe(vid)}_{t.replace('.', '_').replace('#', '-')}"}
                for t in refs]
        af = OUT / f"tts_{ci:02d}_{safe(vid)}.json"
        af.write_text(json.dumps({"requests": reqs}, ensure_ascii=False), encoding="utf-8")
        try:
            res = mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)], 900)
        except Exception as e:  # noqa: BLE001
            print(f"  !! {vid}: TTS that bai {e}", flush=True)
            rows.append({"cand": vid, "note": note, "err": f"TTS fail: {e}"})
            continue
        got = 0
        for ok_i in res.get("success_items", []):
            fn = ok_i["file_name"]
            t = next((k for k in refs if k.replace(".", "_").replace("#", "-") in fn), None)
            if t is None:
                continue
            try:
                url = mcode(["get_asset_url", ok_i["node_id"]], 180)["download_url"]
            except Exception:  # noqa: BLE001
                continue
            local = OUT / fn
            urllib.request.urlretrieve(url, local)
            tag = f"{ci:02d}_{safe(vid)}_{t.replace('.', '_').replace('#', '-')}"
            try:
                h = hyp_of(asr(local, tag))
            except Exception as e:  # noqa: BLE001
                h = f"(LOI {e})"
            hh = TS.vi_numbers(h)
            x, sr = pcm(local)
            rows.append({"cand": vid, "note": note, "id": t, "ref": refs[t], "hyp": hh,
                         "cer": cer(refs[t], hh), "f0": f0_median(x, sr)})
            got += 1
        print(f"  [{ci+1}/{len(CANDS)}] {vid}: {got}/{len(refs)} cau", flush=True)

    (OUT / "rows.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---------- bao cao ----------
    groups = {}
    for r in rows:
        if "cer" in r:
            groups.setdefault(r["cand"], []).append(r)
    summary = []
    for c, rs in groups.items():
        cs = sorted(x["cer"] for x in rs)
        f0s = [x["f0"] for x in rs if x["f0"]]
        summary.append({
            "cand": c, "n": len(cs), "med": cs[len(cs) // 2], "mean": sum(cs) / len(cs),
            "max": cs[-1], "over": sum(1 for x in cs if x > 0.02),
            "f0": sum(f0s) / len(f0s) if f0s else 0.0, "rows": rs})
    summary.sort(key=lambda s: (s["mean"], s["max"]))
    md = ["# Sang loc giong nam cho vai Dieu tra vien — Tap 02", "",
          f"Bộ thu: {len(refs)} câu (tiêu chuẩn tiếng Việt thuần). Đo CER + F0 trên audio TTS mới.", ""]
    md += ["| # | voice_id | n | CER tb | CER max | >2% | F0 (Hz) | Nhận xét |", "|---|---|---:|---:|---:|---:|---:|---|"]
    for i, s in enumerate(summary, 1):
        md.append(f"| {i} | `{s['cand']}` | {s['n']} | {100*s['mean']:.1f}% | {100*s['max']:.1f}% | "
                  f"{s['over']}/{s['n']} | {s['f0']:.0f} | {s['rows'][0].get('note','')} |")
    md.append("")
    for s in summary:
        md.append(f"## `{s['cand']}` — tb {100*s['mean']:.1f}% · max {100*s['max']:.1f}% · F0 {s['f0']:.0f} Hz")
        md.append("")
        md.append("| id | CER | F0 | Nghe được |")
        md.append("|---|---:|---:|---|")
        for x in sorted(s["rows"], key=lambda y: -y["cer"]):
            md.append(f"| `{x['id']}` | {100*x['cer']:.1f}% | {x['f0']:.0f} | {x['hyp'][:120]} |")
        md.append("")
    (OUT / "report.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
