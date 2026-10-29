"""Higgs Audio v3 TTS on the Mac mini (MLX-Audio), one fixed reference clip per role.

Run ON THE MAC from the project root (copy/sync the project folder first):
    python3 .work/higgs_tts_mac.py --test            # 3 sentences per role -> thu_giong_higgs/
    AE_EP=02 python3 .work/higgs_tts_mac.py          # whole episode -> .work/audio_s_higgs_tXX/
Options: --model <repo>  --temp 0.7  --takes 2
Rules: 00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md (no reference clip = random voice per sentence).
"""
import argparse
import hashlib
import inspect
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "assets" / "voice_ref_higgs"
EP = os.environ.get("AE_EP", "02")
# MiniMax emotion -> Higgs v3 tag (§5); neutral = no tag
EMO = {"neutral": "", "sad": "<|emotion:sadness|>", "fearful": "<|emotion:fear|>",
       "surprised": "<|emotion:surprise|>"}
ALLOWED = {"<|emotion:sadness|>", "<|emotion:fear|>", "<|emotion:surprise|>", "<|prosody:pause|>"}


def higgs_text(it, tags):
    t = it["text"].replace("<#0.35#>", "<|prosody:pause|>" if tags else " ")
    t = re.sub(r"<#[\d.]+#>", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    if tags:
        t = EMO[it["emotion"]] + t
    else:
        t = t.replace("<|prosody:pause|>", " ")
    bad = set(re.findall(r"<\|[^|]*\|>", t)) - ALLOWED
    if bad:
        raise SystemExit(f"!! thẻ không cho phép {bad} ở câu {it['id']}")
    return t


def seed_of(sid, take):
    return int(hashlib.md5(f"{sid}#{take}".encode()).hexdigest()[:8], 16)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="bosonai/higgs-audio-v3-tts-4b")
    ap.add_argument("--temp", type=float, default=0.7)
    ap.add_argument("--takes", type=int, default=1)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--no-tags", action="store_true", help="dùng nếu MLX đọc thẻ <|...|> thành chữ")
    a = ap.parse_args()

    import mlx.core as mx
    from mlx_audio.audio_io import write as audio_write
    from mlx_audio.tts.utils import load

    items = json.loads((ROOT / ".work" / f"tts_manifest_t{EP}.json").read_text(encoding="utf-8"))
    if a.test:
        pick = []
        for role in ("H", "D", "C", "N1", "N2"):
            pick += [it for it in items if it["role"] == role][:3]
        items, out = pick, ROOT / "02_SAN_XUAT" / f"Tap{EP}" / "thu_giong_higgs"
    else:
        out = ROOT / ".work" / f"audio_s_higgs_t{EP}"
    out.mkdir(parents=True, exist_ok=True)

    model = load(a.model)  # load once (§2: never reload ~9 GB per sentence)
    params = set(inspect.signature(model.generate).parameters)
    print("model:", a.model, "| generate() nhận:", sorted(params))
    man_p = out / "higgs_manifest.json"
    man = json.loads(man_p.read_text(encoding="utf-8")) if man_p.exists() else {}
    for it in items:
        ref_wav, ref_txt = REF / f"{it['role']}.wav", (REF / f"{it['role']}.txt").read_text(encoding="utf-8")
        text = higgs_text(it, not a.no_tags)
        for k in range(a.takes):
            f = out / f"{it['file'][:-4]}_k{k}.wav"
            if f.exists():
                continue
            s = seed_of(it["id"], k)
            mx.random.seed(s)
            kw = {"text": text, "ref_audio": str(ref_wav), "ref_text": ref_txt}
            if "temperature" in params:
                kw["temperature"] = a.temp
            res = list(model.generate(**kw))
            chunks, sr = [r.audio for r in res], res[0].sample_rate
            audio_write(str(f), mx.concatenate(chunks) if len(chunks) > 1 else chunks[0], sr)
            man[f.name] = {"id": it["id"], "role": it["role"], "text_sent": text, "ref": ref_wav.name,
                           "model": a.model, "temperature": a.temp if "temperature" in params else None,
                           "seed": s, "take": k}
            man_p.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"{it['id']} {it['role']} k{k} -> {f.name}", flush=True)
    print("done", len(man))


if __name__ == "__main__":
    main()
