import json, re
from pathlib import Path
W = Path(r"D:\TEST\Gax\Audi\.work")
man = json.loads((W / "tts_manifest_t02.json").read_text(encoding="utf-8"))
by = {m["id"]: m for m in man}
for sid in ["2.05#2", "4.08#7", "2.05#9", "2.08#6"]:
    it = by[sid]
    fn = f"s{sid.split('#')[0].replace('.', '_').split('_')[0]}_{sid.split('#')[0].split('.')[1]}_{int(sid.split('#')[1]):02d}.mp3"
    f = W / "cer_xac_minh_giong_nam" / f"asr_prod_{fn[:-4]}.json"
    raw = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    print(f"--- {sid} | role={it['role']} | emotion={it['emotion']} | speed={it['speed']}")
    print(f"    CHUAN : {it['text'][:160]}")
    print(f"    ASR   : {raw.get('transcription','')[:160]!r}")
    print(f"    code={raw.get('code')} msg={raw.get('message')!r} err={raw.get('error','')!r}")
    print()
