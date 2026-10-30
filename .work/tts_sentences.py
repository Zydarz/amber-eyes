#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B2 — read every sentence of the episode script (edition.SCRIPT_JSON), one file each.

Voices / emotion / speed follow plan v9 sections 3.2–3.3. Batches of 10.
Re-running only re-requests sentences whose mp3 is missing.
Output: .work/audio_s/<id>.mp3 (id "1.11#5" -> "1.11_05.mp3") + manifest.json
"""
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402  (AE_LANG=en -> English edition)

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT = ED.w("audio_s")
LOG = ED.w("tts_s")
SCRIPT = json.loads(ED.SCRIPT_JSON.read_text(encoding="utf-8"))

CAST = ED.CAST
N_ELEMENT = ED.N_ELEMENT

# direction keyword -> (emotion, speed delta)   plan 3.3
DIR = [("xúc động", ("sad", 0.0)), ("Đẩy nhanh", ("neutral", 0.04)),
       ("sắc lạnh", ("neutral", 0.02)), ("đanh thép", ("neutral", 0.02)),
       ("trầm lắng", ("sad", -0.02)), ("trăn trở", ("sad", -0.02)),
       ("Hạ giọng trầm, chậm rãi", ("neutral", -0.04)),
       ("trầm ấm", ("neutral", -0.02)), ("chậm, trầm", ("neutral", -0.02))]


def fname(sid):
    """'1.11#5' -> 's1_11_05' (no dot: the server treats it as an extension)."""
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}"


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
        msg = r.stderr[:500] or r.stdout[:500]
        if "Network request failed" in msg and n < tries - 1:
            time.sleep(10 * (n + 1))
            continue
        raise RuntimeError(msg)


# English edition: the stage directions are in English, so emotion and speed delta are
# taken per sentence id from the Vietnamese manifest of the SAME episode (same ids, same acting).
VN_MAN = {}
if ED.EN:
    VN_MAN = {m["id"]: (m["emotion"], round(m["speed"] - ED.VN_CAST_BASE[m["role"]], 2))
              for m in json.loads(ED.VN_MANIFEST.read_text(encoding="utf-8"))}


def plan_items():
    items, last_dir = [], {}
    for e in SCRIPT:
        if e["kind"] != "LOI":
            continue
        role = N_ELEMENT.get(e["id"], e["role"])
        key = (e["id"].split(".")[0], role)
        d = e["direction"] or last_dir.get(key, "")
        last_dir[key] = d
        emo, dsp = "neutral", 0.0
        for kw, val in DIR:
            if kw in d:
                emo, dsp = val
                break
        voice, base = CAST[role]
        for s in e["sentences"]:
            text = s["text"].replace("“", "").replace("”", "").replace('"', "").replace("‘", "").replace("’", "")
            text = ED.TTS_FIX.get(s["id"], text)
            extra = {}
            if VN_MAN:                       # English edition: same acting as the VN sentence
                emo, dsp = VN_MAN[s["id"]]
            if s["id"] in ACT:               # diễn xuất từng câu (acting_EN.json / acting_tap02.json)
                emo, dsp, pitch, alt = ACT[s["id"]]
                text = alt or text
                extra = {"pitch": pitch}
            if ED.EN:                        # bản EN: ngắt nghỉ đã viết sẵn trong file diễn xuất
                text = pause_tags(text)
            if not (ED.EN or ED.KO or ED.JA):       # bản VN: số → chữ (chỉ lời đọc)
                text = vi_numbers(text)     # tiếng Nhật / Hàn / Anh đọc số tự nhiên nên KHÔNG đổi
            items.append({"id": s["id"], "element": e["id"], "role": role, "voice": voice,
                          "emotion": emo, "speed": round(base + dsp, 2), "text": text,
                          "display": s["text"], "file": fname(s["id"]) + ".mp3", **extra})
    return items


ACT = {k: v for k, v in json.loads(ED.ACTING.read_text(encoding="utf-8")).items()
       if not k.startswith("_")} if ED.ACTING and ED.ACTING.exists() else {}


# ---------------------------------------------------------------- số → chữ tiếng Việt (chỉ lời đọc, bản VN)
# Giọng đa ngôn ngữ đọc số theo kiểu tiếng Anh: "1.400" (một nghìn bốn trăm) thành "một phẩy bốn trăm",
# năm "2009" có thể thành "twenty oh nine". Phụ đề và chữ trên hình giữ nguyên chữ số.
_DG = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]


def _vi_lt100(n, full):
    """0–99. full=True: đứng sau hàng trăm nên số < 10 đọc kèm 'lẻ'."""
    if n < 10:
        return ("lẻ " if full else "") + _DG[n] if (n or not full) else ""
    t, u = divmod(n, 10)
    s = "mười" if t == 1 else _DG[t] + " mươi"
    if u == 0:
        return s
    if u == 5:
        return s + " lăm"
    if u == 1 and t > 1:
        return s + " mốt"
    if u == 4 and t > 1:
        return s + " tư"
    return s + " " + _DG[u]


def _vi_lt1000(n, full):
    h, r = divmod(n, 100)
    if h == 0 and not full:
        return _vi_lt100(r, False)
    s = _DG[h] + " trăm"
    return s + (" " + _vi_lt100(r, True) if r else "")


def vi_number(n):
    if n == 0:
        return "không"
    parts, units = [], ["", " nghìn", " triệu", " tỷ"]
    groups = []
    while n:
        n, g = divmod(n, 1000)
        groups.append(g)
    for i in range(len(groups) - 1, -1, -1):
        g = groups[i]
        if g == 0:
            continue
        lead = i == len(groups) - 1
        parts.append(_vi_lt1000(g, not lead) + units[i])
    return " ".join(parts)


ROMAN = {"II": "Đệ nhị", "III": "Đệ tam", "IV": "Đệ tứ"}


def vi_numbers(text):
    """Đổi chữ số trong lời đọc sang chữ; bỏ qua thẻ ngắt <#s#>. Dấu chấm giữa nhóm 3 số là dấu nghìn."""
    if ED.EN:
        return text
    tags = []

    def keep(m):
        tags.append(m.group(0))
        return f"@@{len(tags) - 1}@@"

    text = re.sub(r"<#[\d.]+#>", keep, text)
    text = re.sub(r"\b(Elizabeth|Charles|John Paul|Henry)\s+(II|III|IV)\b",
                  lambda m: f"{m.group(1)} {ROMAN[m.group(2)]}", text)
    text = re.sub(r"\d{1,3}(?:\.\d{3})+(?!\d)", lambda m: vi_number(int(m.group(0).replace(".", ""))), text)
    text = re.sub(r"(?<!@)\d+(?!@)", lambda m: vi_number(int(m.group(0))), text)
    return re.sub(r"@@(\d+)@@", lambda m: tags[int(m.group(1))], text)


def pause_tags(t):
    """Engine pause markers <#s#> at dramatic punctuation (English edition only)."""
    import re
    t = re.sub(r"\.\.\.\s+(?!<#)", "... <#0.45#> ", t)
    t = re.sub(r"\s—\s(?!<#)", " — <#0.15#> ", t)
    t = re.sub(r":\s+(?=[A-Z])", ": <#0.3#> ", t)
    return t


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    LOG.mkdir(parents=True, exist_ok=True)
    items = plan_items()
    ED.w("tts_manifest.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    todo = [it for it in items if not (OUT / it["file"]).exists()]
    print(f"{len(items)} câu · cần đọc {len(todo)}")
    failed = []
    for b in range(0, len(todo), 10):
        batch = todo[b:b + 10]
        reqs = [{"text": it["text"], "voice_id": it["voice"], "emotion": it["emotion"],
                 "speed": it["speed"], "pitch": it.get("pitch", 0), "volume": 1.0,
                 "output_file": it["file"][:-4]} for it in batch]
        af = LOG / f"batch_{b // 10:02d}.json"
        af.write_text(json.dumps({"requests": reqs}, ensure_ascii=False), encoding="utf-8")
        try:
            res = mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)])
        except Exception as ex:  # noqa: BLE001
            print(f"!! batch {b // 10}: {ex}")
            failed += [it["id"] for it in batch]
            continue
        (LOG / f"res_{b // 10:02d}.json").write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
        for f in res.get("failed_items", []):
            failed.append(batch[f["index"]]["id"])
            print(f"!! {batch[f['index']]['id']}: {f.get('error_msg')}")
        want = {it["file"][:-4] for it in batch}
        for it in res.get("success_items", []):
            stem = it["file_name"].rsplit(".", 1)[0]
            if stem not in want:
                raise SystemExit(f"!! tên file trả về không khớp: {it['file_name']}")
            url = mcode(["get_asset_url", it["node_id"]], 120)["download_url"]
            urllib.request.urlretrieve(url, OUT / (stem + ".mp3"))
        print(f"  batch {b // 10:02d}: {res.get('total_success')}/{len(batch)}", flush=True)
    if failed:
        print("FAILED:", failed)
        sys.exit(2)
    print("done")


if __name__ == "__main__":
    main()
