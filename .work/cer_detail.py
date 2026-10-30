"""Soi chi tiet CER (chuẩn hóa 2 vế) cho 1 lượt Higgs — in từng câu lỗi.

Dùng cache ASR nếu có, không gọi lại connector (trừ khi --asr và thiếu cache).

Input : .work/kaggle_higgs/out_higgs_v6/out_higgs_v6/higgs_manifest.json
Cache : .work/kaggle_higgs/_asr_cache_v6/<stem>__r1.json , __r2.json
Output: .work/cer_detail_v6.txt (hoac theo --out)

Ví dụ:
  python .work/cer_detail.py --cell N1:W6_LOW_S35
  python .work/cer_detail.py --all --out .work/cer_detail_v6.txt
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import vi_cer  # noqa: E402

WAV = HERE / "kaggle_higgs" / "out_higgs_v6" / "out_higgs_v6"
CACHE = HERE / "kaggle_higgs" / "_asr_cache_v6"


def mcode(args, timeout=600):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=timeout)
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
        return {"transcription": "", "code": -1}
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


def hyp_of(res):
    h = res.get("transcription") or res.get("text") or ""
    if re.search(r"This request was blocked|blocked by|safety", h, re.I):
        return ""
    return h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None)
    ap.add_argument("--cell", default=None, help="role:ref_wav, vd N1:W6_LOW_S35")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", default=None)
    ap.add_argument("--asr", action="store_true", help="goi ASR cho file thieu cache")
    a = ap.parse_args()

    wavdir = pathlib.Path(a.dir) if a.dir else WAV
    man_p = wavdir / "higgs_manifest.json"
    if not man_p.exists():
        cands = sorted((wavdir.parent).rglob("higgs_manifest.json"))
        if not cands:
            raise SystemExit("khong tim thay higgs_manifest.json")
        man_p = cands[0]
    rows = json.loads(man_p.read_text(encoding="utf-8-sig"))
    rows = [r for r in rows if r.get("ok")]
    print("manifest:", man_p, "| n =", len(rows))

    want_role = want_ref = None
    if a.cell and ":" in a.cell:
        want_role, want_ref = a.cell.split(":", 1)

    lines = []
    by_cell = {}
    for r in rows:
        if want_role and r["role"] != want_role:
            continue
        if want_ref and r["ref_wav"] != want_ref:
            continue
        p = wavdir / r["file"]
        if not p.exists():
            continue
        txt = r.get("text_plain") or r.get("text_sent") or ""
        hyps = []
        for rnd in (1, 2):
            if not (CACHE / f"{p.stem}__r{rnd}.json").exists() and not a.asr:
                hyps.append("")
                continue
            try:
                hyps.append(hyp_of(asr(p, rnd)))
            except Exception as e:
                hyps.append("")
                print("  !! ASR loi", p.name, e)
        key = (r["role"], r["ref_wav"])
        c = max([vi_cer.cer_pair(txt, h) for h in hyps if h], default=None)
        cn = max([vi_cer.cer_pair_nonum(txt, h) for h in hyps if h], default=None)
        cp = max([vi_cer.cer_pair_prop(txt, h) for h in hyps if h], default=None)
        by_cell.setdefault(key, []).append(
            {"id": r["id"], "file": r["file"], "text": txt, "hyps": hyps,
             "cer": c, "cer_nonum": cn, "cer_prop": cp, "variant": r.get("variant"),
             "dur": r.get("duration_s")})

    for key in sorted(by_cell):
        v = by_cell[key]
        cs = [x["cer"] for x in v if x["cer"] is not None]
        cn = [x["cer_nonum"] for x in v if x["cer_nonum"] is not None]
        lines.append("=" * 100)
        lines.append("CELL %s <- %s   (n=%d)" % (key[0], key[1], len(v)))
        if cs:
            lines.append("  CER tb %.2f%%  max %.1f%%  >2%%: %d/%d   | bo so: tb %.2f%% max %.1f%%"
                         % (100 * sum(cs) / len(cs), 100 * max(cs),
                            len([c for c in cs if c > 0.02]), len(cs),
                            100 * sum(cn) / len(cn) if cn else 0,
                            100 * max(cn) if cn else 0))
        else:
            lines.append("  khong co ASR")
        cps = [x["cer_prop"] for x in v if x["cer_prop"] is not None]
        if cps:
            lines.append("  CER BO DANH TU RIENG: tb %.2f%%  max %.1f%%  >2%%: %d/%d"
                         % (100 * sum(cps) / len(cps), 100 * max(cps),
                            len([c for c in cps if c > 0.02]), len(cps)))
        for x in sorted(v, key=lambda z: -(z["cer"] or 0)):
            if x["cer"] is None or x["cer"] <= 0.02:
                continue
            lines.append("  - %-22s v%d cer=%.1f%%  nonum=%.1f%%  prop=%.1f%%  dur=%s" %
                         (x["id"], x["variant"], 100 * x["cer"], 100 * (x["cer_nonum"] or 0),
                          100 * (x["cer_prop"] or 0), x["dur"]))
            lines.append("      REF : %s" % x["text"])
            for i, h in enumerate(x["hyps"], 1):
                if h:
                    lines.append("      HYP%d: %s" % (i, h))
        lines.append("")

    out = "\n".join(lines)
    if a.out:
        p = pathlib.Path(a.out)
        p.write_text(out, encoding="utf-8")
        print("->", p)
    else:
        print(out)


if __name__ == "__main__":
    main()
