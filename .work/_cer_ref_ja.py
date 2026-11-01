"""CER giong mau tieng Nhat (listen_audio, 2 luot, ja_cer). Doi giong H/D ban JA (01/11/2026)."""
import json, pathlib, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent))
import ja_cer  # noqa: E402
A = HERE.parent / "assets"
CACHE = HERE / "kaggle_higgs" / "_asr_cache_refclip_ja"; CACHE.mkdir(parents=True, exist_ok=True)
PROMPT = "日本語でそのまま書き起こしてください。追加も省略もしないでください。"

def mcode(args):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600)
    if r.returncode != 0: raise RuntimeError((r.stderr or r.stdout)[:400])
    return json.loads(r.stdout)

def asr(p, rnd):
    cf = CACHE / f"{p.stem}__r{rnd}.json"
    if cf.exists(): return json.loads(cf.read_text(encoding="utf-8"))
    url = mcode(["upload-temp-url", str(p), "--mime-type", "audio/wav"]).get("temp_url")
    af = CACHE / f"{p.stem}__r{rnd}.args.json"
    af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/wav", "prompt": PROMPT}}, ensure_ascii=False), encoding="utf-8")
    res = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)])
    cf.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8"); return res

def one(c):
    p = A / c; ref = p.with_suffix(".txt").read_text(encoding="utf-8")
    hs = [(asr(p, r).get("transcription") or "") for r in (1, 2)]
    hs = [h for h in hs if "blocked" not in h.lower()]
    return c, [round(100 * ja_cer.cer_pair(ref, h), 1) for h in hs], hs

for c, cs, hs in ThreadPoolExecutor(4).map(one, sys.argv[1:]):
    print(c, "CER%", cs); print("   ", hs[0][:90] if hs else "")
