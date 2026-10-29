import json, subprocess, sys, os
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(r"D:\TEST\Gax\Audi\.work")
OUT = W / "cer_xac_minh_giong_nam"
BLOCK = __import__("re").compile(r"(This request was blocked.*|You can \[send feedback\].*)$", __import__("re").S)
def mcode(args, timeout=600):
    p = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "")[:300])
    return json.loads(p.stdout)
def asr_url(url, tag):
    cache = OUT / f"asr_{tag}.json"
    if cache.exists():
        t = json.loads(cache.read_text(encoding="utf-8"))
        if t:
            return t
    af = OUT / f"req_{tag}.json"
    af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg",
        "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}}, ensure_ascii=False), encoding="utf-8")
    tr = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600)
    cache.write_text(json.dumps(tr, ensure_ascii=False), encoding="utf-8")
    return tr
print("=== HASH 2 file cung kich thuoc ===")
import hashlib
for vid in ("English_Diligent_Man", "English_DecentYoungMan"):
    for f in sorted(OUT.glob(f"p2_*_{vid}_2_05-11*.mp3")):
        h = hashlib.md5(f.read_bytes()).hexdigest()[:16]
        print(f"  {vid:26s} {f.name}  md5={h}  {f.stat().st_size} bytes")
print("\n=== CHAY LAI 2 CAU ASR RONG ===")
for vid in ("English_Diligent_Man", "English_DecentYoungMan"):
    fs = sorted(OUT.glob(f"p2_*_{vid}_2_05-11*.mp3"))
    if not fs:
        continue
    local = fs[0]
    up = mcode(["upload_temp_url", str(local), "--mime-type", "audio/mpeg"], 300)
    u = up.get("temp_url") or up.get("url")
    tag = f"p2_{local.stem.split('_', 2)[1]}_{vid}_2_05-11"
    tag = f"p2_{[t for t in ['00','01','02','03'] if f'p2_{t}_{vid}_' in local.name][0]}_{vid}_2_05-11"
    tr = asr_url(u, tag)
    print(f"  {vid}: {json.dumps(tr, ensure_ascii=False)[:220]}")
