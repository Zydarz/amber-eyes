"""Kiem gia thuyet: CER truot do ASR bo sot tu dau hay Higgs nuot chu that.
Chen 0.5 s lang vao dau moi file truot CER (pilot v9), ASR lai 1 luot, so CER."""
import json, subprocess, sys, wave, pathlib
from concurrent.futures import ThreadPoolExecutor
import os
import numpy as np
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import vi_cer
PAD = HERE / "kaggle_higgs" / f"_{os.environ.get('TAG','v9')}_pad"
PAD.mkdir(exist_ok=True)

def mcode(args):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=600)
    if r.returncode: raise RuntimeError(r.stderr[:200])
    return json.loads(r.stdout)

def work(r):
    src = pathlib.Path(r["path"]); dst = PAD / src.name
    cf = PAD / (src.stem + ".asr.json")
    if not cf.exists():
        with wave.open(str(src)) as w:
            p = w.getparams(); fr = w.readframes(w.getnframes())
        with wave.open(str(dst), "wb") as w:
            w.setparams(p); w.writeframes(b"\x00" * (int(0.5 * p.framerate) * p.sampwidth * p.nchannels) + fr)
        for _ in range(3):
            try:
                up = mcode(["upload-temp-url", str(dst), "--mime-type", "audio/wav"])
                af = PAD / (src.stem + ".args.json")
                af.write_text(json.dumps({"audio_info": {"url": up["temp_url"], "mime_type": "audio/wav",
                    "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}}, ensure_ascii=False), encoding="utf-8")
                cf.write_text(json.dumps(mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)]),
                                         ensure_ascii=False), encoding="utf-8")
                break
            except Exception as e:
                err = str(e)
    if not cf.exists():
        return r, None, ""
    h = json.loads(cf.read_text(encoding="utf-8")).get("transcription", "")
    return r, vi_cer.cer_pair(r["text"], h), h

R = json.load(open(HERE / f"pilot_{os.environ.get('TAG','v9')}_result.json", encoding="utf-8"))
fails = [r for r in R["rows"] if r.get("cer_fail")]
print("file truot CER:", len(fails))
with ThreadPoolExecutor(2) as ex:
    res = list(ex.map(work, fails))
out = []
for r, c, h in res:
    out.append({"key": r["key"], "ref": r["ref"], "cer_goc": r["cer_min"], "cer_pad": c, "hyp_pad": h})
    print(f"{r['ref']:8} {r['key'].split('__')[2]:>2} v{r['variant']}  goc {100*r['cer_min']:5.1f}%  pad {('%.1f%%' % (100*c)) if c is not None else 'loi':>6}")
json.dump(out, open(HERE / f"pilot_{os.environ.get('TAG','v9')}_padtest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ok = [o for o in out if o["cer_pad"] is not None]
print("\nsau khi chen lang: con >2%%: %d/%d" % (sum(o["cer_pad"] > 0.02 for o in ok), len(ok)))
from collections import Counter
print("theo clip (con >2% / tong truot):", {k: f"{sum(1 for o in ok if o['ref']==k and o['cer_pad']>0.02)}/{v}" for k, v in Counter(o['ref'] for o in ok).items()})
