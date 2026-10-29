#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC — transcribe every TTS sentence with listen_audio and compare with the script (CER).

    AE_LANG=en py -3 .work/qc_asr.py        -> .work/qc_asr_EN/report.md
Re-running reuses cached transcriptions. Numbers are compared after spelling digits
as words (ASR writes "three" for "3"), so a flagged sentence is worth listening to.
"""
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402
import tts_sentences as TS  # noqa: E402
from voice_audition import cer  # noqa: E402

OUT = ED.w("qc_asr")
MAN = json.loads(ED.w("tts_manifest.json").read_text(encoding="utf-8"))
PROMPT = ("Transcribe verbatim in English. Do not add or omit anything." if ED.EN
          else "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt.")
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen " \
       "sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def words(n):
    n = int(n)
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
    if 1900 <= n <= 2099:                       # years
        hi, lo = divmod(n, 100)
        return ("two thousand" + ("" if lo == 0 else " " + words(lo))) if hi == 20 and lo < 10 \
            else words(hi) + " " + (words(lo) if lo >= 10 else "oh " + ONES[lo] if lo else "hundred")
    return str(n)


def spell(t):
    t = re.sub(r"<#[\d.]+#>", " ", t)            # engine pause markers are not spoken
    if not ED.EN:
        return t
    t = re.sub(r"(\d+)%", lambda m: words(m.group(1)) + " percent", t)
    t = re.sub(r"(\d+)(st|nd|rd|th)\b", lambda m: words(m.group(1)), t)
    t = re.sub(r"\d+", lambda m: words(m.group(0)), t)
    t = t.replace("-", " ").replace("—", " ")
    for a, b in (("fourteen", "fourteenth"),):
        t = t.replace(b, a)
    return t


def one(it):
    cache = OUT / f"{it['file'][:-4]}.json"
    if cache.exists():
        return it, json.loads(cache.read_text(encoding="utf-8")).get("transcription", "")
    tmp = OUT / f"{it['file'][:-4]}_req.json"
    url = TS.mcode(["upload-temp-url", str(ED.w("audio_s") / it["file"])], 300)["temp_url"]
    tmp.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg", "prompt": PROMPT}},
                              ensure_ascii=False), encoding="utf-8")
    res = TS.mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(tmp)], 600)
    cache.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
    return it, res.get("transcription", "")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with ThreadPoolExecutor(4) as ex:
        for it, hyp in ex.map(one, MAN):
            c = cer(spell(it["text"]), spell(hyp))
            rows.append((it["id"], it["role"], c, it["text"], hyp))
    rows.sort(key=lambda r: -r[2])
    bad = [r for r in rows if r[2] > 0.03]
    md = [f"# QC ASR · {len(rows)} câu · CER trung bình {100 * sum(r[2] for r in rows) / len(rows):.2f}% · "
          f"{len(bad)} câu > 3%", "", "| Câu | Vai | CER | Kịch bản | Nghe được |", "|---|---|---:|---|---|"]
    md += [f"| `{r[0]}` | {r[1]} | {100 * r[2]:.1f}% | {r[3]} | {r[4]} |" for r in rows[:40]]
    (OUT / "report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(md[0])
    for r in bad:
        print(f"  {r[0]} {100 * r[2]:.1f}%  REF: {r[3]}\n{'':10}ASR: {r[4]}")


if __name__ == "__main__":
    main()
