#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đọc giọng cho trailer Concept A (6 câu, 1 vai Host).

Dùng: py -3 .work/make_trailer_tts.py [--lang en]
Input: .work/trailer_a/vo_manifest.json
Output: .work/trailer_a/vo/<mã>.mp3  + in thời lượng từng câu (để dựng timeline)

Giọng lấy từ `edition.CAST` (bộ A cho VN / bộ EN cho EN) — không hardcode.
Luật: G1 (không `...`, không `<#s#>`) · G3 (chỉ 4 cảm xúc an toàn) · G4 (speed lệch base trong −0,06…+0,02) · G5 (pitch = 0).
"""
import argparse
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work" / "trailer_a"
VO = WORK / "vo"
LOG = WORK / "tts"
MAN = WORK / "vo_manifest.json"
FFPROBE = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"


def mcode(args, timeout=900, tries=4):
    import time
    for n in range(tries):
        try:
            r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=timeout)
        except subprocess.TimeoutExpired:
            if n < tries - 1:
                time.sleep(10 * (n + 1))
                continue
            raise
        if r.returncode == 0:
            return json.loads(r.stdout)
        msg = (r.stderr or "")[:500] + (r.stdout or "")[:500]
        if "Network request failed" in msg and n < tries - 1:
            time.sleep(10 * (n + 1))
            continue
        raise RuntimeError(msg)


def dur(path):
    r = subprocess.run([str(FFPROBE), "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    return round(float(r.stdout.strip()), 3)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="vi", choices=["vi", "en"])
    ap.add_argument("--voice", default="", help="ghi đè giọng (mặc định: bộ A Host của kênh)")
    ap.add_argument("--base", type=float, default=0.0, help="ghi đè speed base (0 = theo ngôn ngữ)")
    ap.add_argument("--force", action="store_true", help="đọc lại dù file mp3 đã có (ghi đè)")
    a = ap.parse_args()

    man = json.loads(MAN.read_text(encoding="utf-8"))
    items = man["items"] if isinstance(man, dict) else man
    items = [it for it in items if it.get("lang", "vi") == a.lang]
    if not items:
        raise SystemExit("không có câu nào cho lang = " + a.lang)

    # Bộ A (AGENTS.md §4) — Host của kênh từ Tập 02 trở đi. KHÔNG dùng bộ ghim riêng của Tập 01
    # (audiobook_male_1) vì trailer đại diện cho kênh nói chung.
    DEFAULT_VOICE = {"vi": ("English_CaptivatingStoryteller", 0.90),
                      "en": ("English_magnetic_voiced_man", 0.95)}
    voice, base = DEFAULT_VOICE[a.lang]
    if a.voice:
        voice = a.voice
    if a.base:
        base = a.base
    vo_dir = VO if a.lang == "vi" else WORK / ("vo_" + a.lang)
    VO.mkdir(parents=True, exist_ok=True)
    LOG.mkdir(parents=True, exist_ok=True)
    vo_dir.mkdir(parents=True, exist_ok=True)

    todo = items if a.force else [it for it in items if not (vo_dir / f"{it['id']}.mp3").exists()]
    print(f"[{a.lang}] {len(items)} câu · cần đọc {len(todo)} · giọng {voice}", flush=True)

    for b in range(0, len(todo), 6):
        batch = todo[b:b + 6]
        reqs = [{"text": it["text"], "voice_id": voice, "emotion": it.get("emotion", "neutral"),
                 "speed": it.get("speed", base), "pitch": 0, "volume": 1.0,
                 "output_file": it["id"]} for it in batch]
        af = LOG / f"batch_{b // 6:02d}.json"
        af.write_text(json.dumps({"requests": reqs}, ensure_ascii=False), encoding="utf-8")  # UTF-8 KHÔNG BOM
        res = mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)])
        (LOG / f"res_{b // 6:02d}.json").write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
        for f in res.get("failed_items", []):
            print("!! fail:", batch[f["index"]]["id"], f.get("error_msg"))
        for it in res.get("success_items", []):
            stem = it["file_name"].rsplit(".", 1)[0]
            url = mcode(["get_asset_url", it["node_id"]], 120)["download_url"]
            urllib.request.urlretrieve(url, vo_dir / f"{stem}.mp3")

    print("\n=== thời lượng từng câu ===")
    out = {}
    for it in items:
        p = vo_dir / f"{it['id']}.mp3"
        out[it["id"]] = dur(p) if p.exists() else None
        print(f"  {it['id']}  {out[it['id']]} s   {it['text'][:60]}")
    (WORK / f"vo_durations_{a.lang}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1),
                                                       encoding="utf-8")


if __name__ == "__main__":
    main()
