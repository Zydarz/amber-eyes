"""Do CER cho TOAN BO ban sinh cua luot san xuat Tap 02 (Higgs Audio v3).

Quy tac §7: moi cau 2 ban (seed khac) => do CER ca 2 ban, chon ban tot nhat.
ASR: `connector__matrix__listen_audio`, 2 luot/cau, lay luot XAU HON (giai quyet
da chot o H2). Q3(a): chuan hoa so -> chu cho CA HAI VE bang dung `vi_number()`
cua pipeline (copy nguyen ban trong `tts_sentences.py`).

Cache theo file trong `.work/kaggle_higgs/_asr_cache_prod/` nen chay lai khong ton
them luot ASR.

Usage:
  python .work/measure_cer_prod.py                # 1 luot (nhanh, xep do)
  python .work/measure_cer_prod.py --rounds 2     # 2 luot (dung de chot §7)
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

from voice_audition import cer, norm  # noqa: E402

CACHE = HERE / "kaggle_higgs" / "_asr_cache_prod"
CACHE.mkdir(parents=True, exist_ok=True)
OUT_ROWS = HERE / "higgs_cer_rows_t02.json"
OUT_REP = HERE / "higgs_cer_report_t02.md"

ap = argparse.ArgumentParser()
ap.add_argument("--rounds", type=int, default=1)
ap.add_argument("--dir", default=str(HERE / "kaggle_higgs" / "out_higgs_prod" / "out_higgs_prod"))
ap.add_argument("--workers", type=int, default=6)
a = ap.parse_args()
ROUNDS = a.rounds
WAVDIR = pathlib.Path(a.dir)

# ------------------------------------------------------------------ chuan hoa so (Q3a)
_DG = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]


def _vi_lt100(n, full):
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
    h, r = divmod(n, 1000)
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


def vi_numbers(text):
    def rep(m):
        s = m.group(0).replace(".", "")
        if not s.isdigit():
            return m.group(0)
        parts = []
        while len(s) > 3:
            parts.insert(0, s[-3:])
            s = s[:-3]
        if s:
            parts.insert(0, s)
        return " ".join(vi_number(p) for p in parts)
    return re.sub(r"\d[\d.]*", rep, text)


# ------------------------------------------------------------------ ASR
def mcode(args, timeout=600):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "")[:400])
    return json.loads(r.stdout)


def asr(path, rnd):
    cf = CACHE / f"{path.stem}__r{rnd}.json"
    if cf.exists():
        try:
            return json.loads(cf.read_text(encoding="utf-8"))
        except Exception:
            pass
    up = mcode(["upload-temp-url", str(path), "--mime-type", "audio/wav"])
    url = up.get("temp_url")
    if not url:
        return {"transcription": "", "code": -1, "error": "upload fail"}
    af = CACHE / f"{path.stem}__r{rnd}.args.json"
    af.write_text(json.dumps(
        {"audio_info": {"url": url, "mime_type": "audio/wav",
                        "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
        ensure_ascii=False), encoding="utf-8")
    res = mcode(["connector", "call", "connector__matrix__listen_audio",
                 "--args-file", str(af)])
    res["_round"] = rnd
    cf.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
    return res


def main():
    man_p = WAVDIR / "higgs_manifest.json"
    if not man_p.exists():
        cands = sorted((HERE / "kaggle_higgs" / "out_higgs_prod").rglob("higgs_manifest.json"))
        if not cands:
            raise SystemExit("khong tim thay manifest san xuat")
        man_p = cands[0]
    man = json.loads(man_p.read_text(encoding="utf-8-sig"))
    rows = [r for r in man if r.get("ok")]
    print("manifest:", man_p, "| OK:", len(rows), "| FAIL:", len(man) - len(rows))
    if not rows:
        return

    def work(r):
        p = WAVDIR / r["file"]
        if not p.exists():
            cands = list((HERE / "kaggle_higgs" / "out_higgs_prod").rglob(r["file"]))
            if not cands:
                r["_missing"] = True
                return r
            p = cands[0]
        hyps = []
        for rnd in range(1, ROUNDS + 1):
            try:
                res = asr(p, rnd)
            except Exception as e:
                res = {"transcription": "", "error": str(e)[:200]}
            h = res.get("transcription") or res.get("text") or ""
            if re.search(r"This request was blocked|blocked by|safety", h, re.I):
                h = ""
            hyps.append(h)
        r["hyps"] = hyps
        txt = r.get("text_plain") or r.get("text_sent") or ""
        txt = re.sub(r"<\|[^|]*\|>", " ", txt)
        txt = re.sub(r"<#.*?#>", " ", txt)
        r["text_norm"] = norm(vi_numbers(txt))
        best = None
        for h in hyps:
            if not h:
                continue
            c = cer(txt, h)
            best = c if best is None else max(best, c)   # lay luot XAU HON
        r["cer"] = best
        r["cer_ok"] = best is not None
        return r

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        rows = list(ex.map(work, rows))
    print("ASR xong trong %.0f s" % (time.time() - t0))

    OUT_ROWS.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---------------------------------------------------------------- bao cao
    from collections import defaultdict
    g = defaultdict(list)
    for r in rows:
        g[(r["role"], r["ref_wav"], r["temp"])].append(r)

    md = ["# CER lượt sản xuất Tập 02 — Higgs Audio v3", "",
          f"ASR `listen_audio` **{ROUNDS} lượt/câu**, lấy lượt xấu hơn. "
          f"`vi_numbers()` áp cho **cả hai vế** (Q3a). Ngưỡng: **CER < 2% mỗi vai**.", "",
          "| Vai | Clip | Temp | n | CER tb | CER max | >2% | F0 tb (AC thô) | Âm tiết/s |",
          "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    import wave
    import numpy as np
    from voice_audition import f0_median
    for (role, ref, temp), v in sorted(g.items()):
        cs = [x["cer"] for x in v if x.get("cer_ok")]
        f0s, syl = [], []
        for x in v:
            p = WAVDIR / x["file"]
            if not p.exists():
                continue
            with wave.open(str(p), "rb") as w:
                sr = w.getframerate()
                raw = w.readframes(w.getnframes())
            arr = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
            d = len(arr) / sr
            f0s.append(f0_median(arr, sr))
            syl.append(len(x.get("text_norm", "").split()) / max(0.1, d))
        md.append("| %s | %s | %s | %d | %s | %s | %d/%d | %s | %s |" % (
            role, ref, temp, len(v),
            ("%.2f%%" % (100 * sum(cs) / len(cs))) if cs else "-",
            ("%.1f%%" % (100 * max(cs))) if cs else "-",
            len([c for c in cs if c > 0.02]), len(cs),
            ("%.0f Hz" % np.median(f0s)) if f0s else "-",
            ("%.2f" % np.mean(syl)) if syl else "-"))

    # theo cau: bao cao cau CER > 2%
    by_id = defaultdict(list)
    for r in rows:
        by_id[r["id"]].append(r)
    bad = []
    for sid, v in by_id.items():
        cs = [x["cer"] for x in v if x.get("cer_ok")]
        if not cs:
            continue
        if max(cs) > 0.02:
            bad.append((sid, max(cs), len(v)))
    md += ["", "## Câu có ít nhất 1 bản CER > 2% (cần vòng 2 theo §7)", "",
           "| Câu | CER max | số bản |", "|---|---:|---:|"]
    for sid, c, n in sorted(bad, key=lambda x: -x[1]):
        md.append("| %s | %.1f%% | %d |" % (sid, 100 * c, n))
    md += ["", "**Tổng: %d/%d câu có ít nhất 1 bản vượt 2%.**" % (len(bad), len(by_id))]

    OUT_REP.write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))
    print("\n-> ", OUT_REP)
    print("-> ", OUT_ROWS)


if __name__ == "__main__":
    main()
