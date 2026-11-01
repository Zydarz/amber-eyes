# -*- coding: utf-8 -*-
"""QC audio Tập 05 (bản tiếng Việt, Higgs Audio v3).

Đo theo cổng A9 / AGENTS.md mục 2 bước 6:
  - 0 khoảng câm > 0,3 s ở -60 dB
  - -16 ± 1 LUFS
  - đỉnh <= -1,5 dBFS
  - lời đầu 22,8-23,5 s
  - picture (timeline.total) khớp audio ± 0,05 s
Bổ sung: thống kê CER của các take đã chọn trong higgs_selection_t05.json.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")
WORK = ROOT / ".work"
BIN = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin"
FF = str(BIN / "ffmpeg.exe")
FP = str(BIN / "ffprobe.exe")

MP3 = ROOT / "02_SAN_XUAT" / "Tap05" / "xuat_ban" / "Tap05_master.mp3"
WAV = WORK / "audio_master_t05.wav"
TIMELINE = WORK / "timeline_s_t05.json"
SELECTION = WORK / "higgs_selection_t05.json"
OUT = WORK / "_qc_audio_t05.json"


def run(cmd):
    """Chạy lệnh native, nuốt stderr (PowerShell coi stderr là exception)."""
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    return p.stdout, p.stderr, p.returncode


def ffprobe_duration(path):
    out, err, rc = run([FP, "-v", "error", "-show_entries", "format=duration",
                        "-show_entries", "stream=codec_name,sample_rate,channels,bit_rate",
                        "-of", "json", str(path)])
    if rc != 0:
        return {"error": err[:400]}
    d = json.loads(out)
    fmt = d.get("format", {})
    streams = d.get("streams", [])
    a = [s for s in streams if s.get("codec_name") not in ("mjpeg", "png", "bmp", "gif")]
    return {
        "duration_s": round(float(fmt.get("duration", 0)), 3),
        "size_bytes": int(fmt.get("size", 0)),
        "bit_rate": fmt.get("bit_rate"),
        "codec": a[0].get("codec_name") if a else None,
        "sample_rate": a[0].get("sample_rate") if a else None,
        "channels": a[0].get("channels") if a else None,
    }


def loudnorm(path):
    """Đo 1 lượt (đo được): trả về I, TP, LRA, threshold."""
    cmd = [FF, "-hide_banner", "-nostats", "-i", str(path),
           "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
           "-f", "null", "-"]
    out, err, rc = run(cmd)
    m = re.findall(r"\{[^{}]*\"input_i\"[^{}]*\}", out, re.S)
    if not m:
        m = re.findall(r"\{.*?\}", out, re.S)
    if not m:
        return {"error": (err or out)[-500:]}
    try:
        return json.loads(m[-1])
    except Exception as e:  # noqa: BLE001
        return {"error": f"{e}: {m[-1][:300]}"}


def silencedetect(path, noise_db=-60, min_dur=0.3):
    cmd = [FF, "-hide_banner", "-nostats", "-i", str(path),
           "-af", f"silencedetect=noise={noise_db}dB:d={min_dur}", "-f", "null", "-"]
    out, err, rc = run(cmd)
    sil = []
    for m in re.finditer(r"silence_start:\s*([0-9.]+)\s*silence_end:\s*([0-9.]+)",
                         out):
        s, e = float(m.group(1)), float(m.group(2))
        sil.append({"start": round(s, 3), "end": round(e, 3), "dur": round(e - s, 3)})
    return sil


def main():
    rep = {"file": str(MP3)}

    # 1. timeline
    tl = json.loads(TIMELINE.read_text(encoding="utf-8-sig"))
    items = tl.get("items", [])
    rep["timeline"] = {
        "total": tl.get("total"),
        "intro": tl.get("intro"),
        "n_items": len(items),
    }
    if items:
        rep["timeline"]["first_item"] = json.dumps(items[0], ensure_ascii=False)[:300]
        starts = [it.get("start", it.get("t", 0)) for it in items]
        rep["timeline"]["first_start"] = starts[0]
        rep["timeline"]["last_end"] = items[-1].get("end")
        rep["timeline"]["n_roles"] = len({it.get("role") for it in items})

    # 2. ffprobe
    rep["mp3"] = ffprobe_duration(MP3)
    if WAV.exists():
        rep["wav"] = ffprobe_duration(WAV)
    else:
        rep["wav"] = {"error": "missing"}

    # 3. loudnorm
    rep["loudnorm_mp3"] = loudnorm(MP3)

    # 4. silencedetect
    sil = silencedetect(MP3)
    rep["silence_count"] = len(sil)
    rep["silences_over_0_3s"] = [s for s in sil if s["dur"] > 0.3]
    rep["silences_all"] = sil[:40]

    # 5. khớp timeline vs audio
    try:
        d = rep["mp3"]["duration_s"]
        t = float(tl["total"])
        rep["sync"] = {"timeline_total": t, "mp3_duration": d, "drift_s": round(d - t, 3),
                       "pass_0_05": abs(d - t) <= 0.05}
    except Exception as e:  # noqa: BLE001
        rep["sync"] = {"error": str(e)}

    # 6. CER các take đã chọn
    if SELECTION.exists():
        sel = json.loads(SELECTION.read_text(encoding="utf-8-sig"))
        s = sel.get("selection", {})
        cers = [(k, float(v.get("cer", 0))) for k, v in s.items()]
        cers_sorted = sorted(cers, key=lambda x: -x[1])
        vals = [c for _, c in cers]
        over = [(k, round(c, 4)) for k, c in cers_sorted if c > 0.02]
        rep["cer_selected"] = {
            "n_sentences": len(cers),
            "mean_cer_pct": round(100 * sum(vals) / len(vals), 2) if vals else None,
            "max_cer_pct": round(100 * max(vals), 2) if vals else None,
            "n_over_2pct": len(over),
            "over_2pct": over[:20],
            "n_zero_cer": sum(1 for v in vals if v == 0),
            "n_over_max_cer_flag": sel.get("n_over_max_cer"),
            "max_cer_flag": sel.get("max_cer"),
            "by_role": {},
        }
        # theo vai
        byrole = {}
        for k, v in s.items():
            r = v.get("role", "?")
            byrole.setdefault(r, []).append(float(v.get("cer", 0)))
        for r, vs in sorted(byrole.items()):
            rep["cer_selected"]["by_role"][r] = {
                "n": len(vs),
                "mean_cer_pct": round(100 * sum(vs) / len(vs), 2),
                "max_cer_pct": round(100 * max(vs), 2),
                "n_over_2pct": sum(1 for v in vs if v > 0.02),
            }
        # phủ câu
        tl_ids = set()
        for it in items:
            tid = it.get("id") or it.get("sid")
            if tid:
                tl_ids.add(tid)
        sel_ids = set(s.keys())
        rep["coverage"] = {
            "n_timeline_ids": len(tl_ids),
            "n_selection_ids": len(sel_ids),
            "missing_in_selection": sorted(tl_ids - sel_ids)[:20],
            "extra_in_selection": sorted(sel_ids - tl_ids)[:20],
        }

    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---- in tóm tắt ----
    print("=" * 70)
    print("QC AUDIO TAP05 (VN) -", MP3.name)
    print("=" * 70)
    print("timeline.total      :", rep["timeline"]["total"], "s | intro:",
          rep["timeline"]["intro"], "s | items:", rep["timeline"]["n_items"])
    print("mp3                 :", rep["mp3"])
    print("wav                 :", rep["wav"])
    ln = rep["loudnorm_mp3"]
    if "error" in ln:
        print("loudnorm ERROR      :", ln["error"][:200])
    else:
        print("LUFS (I)            :", ln.get("input_i"), "| TP:", ln.get("input_tp"),
              "| LRA:", ln.get("input_lra"), "| thresh:", ln.get("input_thresh"))
    print("silence >0.3s @-60dB:", len(rep["silences_over_0_3s"]))
    for s_ in rep["silences_over_0_3s"][:15]:
        print("   ", s_)
    print("sync                :", rep["sync"])
    if "cer_selected" in rep:
        c = rep["cer_selected"]
        print("CER take đã chọn    : n=%s tb=%s%% max=%s%% >2%%: %s | zero-CER: %s"
              % (c["n_sentences"], c["mean_cer_pct"], c["max_cer_pct"],
                 c["n_over_2pct"], c["n_zero_cer"]))
        for r, v in c["by_role"].items():
            print("    vai %-3s n=%-4s tb=%5s%%  max=%5s%%  >2%%: %s"
                  % (r, v["n"], v["mean_cer_pct"], v["max_cer_pct"], v["n_over_2pct"]))
        print("coverage            :", rep["coverage"])
    print("báo cáo ->", OUT)


if __name__ == "__main__":
    main()
