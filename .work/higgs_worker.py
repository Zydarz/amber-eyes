#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WORKER sinh audio Higgs v3 — chay 1 tiến trinh tren 1 GPU.

Mot tiến trinh = 1 card. Kernel bo 2 tiến trinh song song (CUDA_VISIBLE_DEVICES=0/1)
=> thoi gian sinh giam ~2 lan. Ket qua KHONG doi: seed co dinh theo
(id|role|ref|temp|variant) nen moi cau co ket qua nhat dinh bat ke card nao sinh.

Dung nhung dau vao (do cell cha truyen vao):
  --model-dir  thu muc trong so da tai san (boi 1 lan)
  --ref-dir    thu muc chua clip tham chieu .wav + .txt
  --payload    file JSON payload (items: id -> text/emotion)
  --tasks      file JSON danh sach task phong vien
  --out        thu muc ghi wav + manifest.json
  --shard/--n-shards  chia task theo index % n_shards == shard
  --only       (tu chon) file JSON danh sach key can sinh lai (catch-up)
"""
import argparse
import hashlib
import json
import os
import sys
import time
import traceback

import numpy as np
import soundfile as sf
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

p = argparse.ArgumentParser()
p.add_argument("--model-dir", required=True)
p.add_argument("--ref-dir", required=True)
p.add_argument("--payload", required=True)
p.add_argument("--tasks", required=True)
p.add_argument("--out", required=True)
p.add_argument("--shard", type=int, default=0)
p.add_argument("--n-shards", type=int, default=1)
p.add_argument("--only", default=None)
p.add_argument("--top-p", type=float, default=0.95)
p.add_argument("--top-k", type=int, default=50)
p.add_argument("--fade-ms", type=float, default=30.0)
args = p.parse_args()

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OUT = args.out
os.makedirs(OUT, exist_ok=True)
MAN = os.path.join(OUT, "manifest.json")


def log(*a):
    print(*a, flush=True)


log(f"=== WORKER shard {args.shard}/{args.n_shards} | CUDA_VISIBLE_DEVICES={os.environ.get('CUDA_VISIBLE_DEVICES')} ===")
log("torch:", torch.__version__, "| cuda:", torch.version.cuda, "| avail:", torch.cuda.is_available())
if torch.cuda.is_available():
    log("visible GPU count:", torch.cuda.device_count())
    for i in range(torch.cuda.device_count()):
        pr = torch.cuda.get_device_properties(i)
        log(f"  GPU{i}: {pr.name}  VRAM {pr.total_memory/1e9:.1f} GB  cc=sm_{pr.major}{pr.minor}")

DTYPE = torch.bfloat16 if (torch.cuda.is_available() and torch.cuda.is_bf16_supported()) else torch.float16

# ------------------------------------------------------------------ tai du lieu
TASKS = json.load(open(args.tasks, encoding="utf-8"))
if args.only:
    only = set(json.load(open(args.only, encoding="utf-8")))
    TASKS = [t for t in TASKS if t["key"] in only]
    log(f"catch-up mode: {len(TASKS)} task trong danh sach --only")
else:
    TASKS = [t for t in TASKS if t["idx"] % args.n_shards == args.shard]
log("task cua shard nay:", len(TASKS))

PAYLOAD = json.load(open(args.payload, encoding="utf-8"))
ITEMS = {it["id"]: it for it in PAYLOAD["items"]}

# ------------------------------------------------------------------ nap model
t0 = time.time()
model = AutoModelForCausalLM.from_pretrained(args.model_dir, trust_remote_code=True, dtype=DTYPE)
model = model.to("cuda").eval()
tok = AutoTokenizer.from_pretrained(args.model_dir, trust_remote_code=True)
log(f"model len {time.time()-t0:.0f}s | class={type(model).__name__} | codebooks={model.num_codebooks}")
log("VRAM allocated:", round(torch.cuda.memory_allocated() / 1e9, 2), "GB")

# ------------------------------------------------------------------ do frame-rate
first_ref = TASKS[0]["ref_wav"] if TASKS else None
MAXTOK = 1196
if first_ref:
    w0, sr0 = sf.read(os.path.join(args.ref_dir, first_ref), dtype="float32")
    if w0.ndim > 1:
        w0 = w0.mean(axis=1)
    cp = model._encode_reference(torch.from_numpy(w0).float().unsqueeze(0), sr0)
    FR = cp.shape[0] / (len(w0) / sr0)
    MAXTOK = int(47.5 * FR) + int(model.num_codebooks)
    log(f"frame-rate {FR:.2f} Hz -> max_new_tokens={MAXTOK}")

# ------------------------------------------------------------------ encode reference 1 lan/clip
REFS = sorted({t["ref_wav"] for t in TASKS})
REF_CACHE = {}
for rw in REFS:
    arr, sr = sf.read(os.path.join(args.ref_dir, rw), dtype="float32")
    if arr.ndim > 1:
        arr = arr.mean(axis=1)
    codes = model._encode_reference(torch.from_numpy(arr).float().unsqueeze(0), sr)
    txt = open(os.path.join(args.ref_dir, rw.replace(".wav", ".txt")), encoding="utf-8").read().strip()
    REF_CACHE[rw] = {"codes": codes, "text": txt}
    log(f"ref {rw}: {len(arr)/sr:.2f}s -> codes {tuple(codes.shape)}")

# ------------------------------------------------------------------ ham phu
def seed_for(sid, role, ref, temp, vi=0):
    h = hashlib.sha256(f"{sid}|{role}|{ref}|{temp:.2f}|v{vi}".encode("utf-8")).hexdigest()
    return int(h[:8], 16)


def to_arr(w):
    a = w.detach().float().cpu().numpy() if torch.is_tensor(w) else np.asarray(w)
    a = np.asarray(a, dtype=np.float32).squeeze()
    if a.ndim > 1:
        a = a.mean(axis=-1)
    return a


def save_wav(path, a, sr, fade_ms):
    if a.size:
        n = int(sr * fade_ms / 1000.0)
        n = min(n, len(a) // 2)
        if n > 1:
            ramp = np.linspace(0.0, 1.0, n, dtype=np.float32)
            a[:n] *= ramp
            a[-n:] *= ramp[::-1]
    sf.write(path, a, sr)
    peak = float(np.max(np.abs(a))) if a.size else 0.0
    return peak, len(a) / sr


def has_tag_words(text):
    low = text.lower()
    return any(w in low for w in ("emotion", "sadness", "surprise", "fear",
                                  "prosody", "pause", "style:", "sfx:"))


MANIFEST = json.load(open(MAN, encoding="utf-8")) if os.path.exists(MAN) else []
DONE = {r["key"] for r in MANIFEST}
n_ok = n_fail = 0
t_start = time.time()

for t in TASKS:
    key = t["key"]
    if key in DONE:
        continue
    sid, role, ref, temp, vi = t["id"], t["role"], t["ref_wav"], float(t["temp"]), int(t["variant"])
    it = ITEMS[sid]
    rc = REF_CACHE[ref]
    seed = seed_for(sid, role, ref, temp, vi)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.cuda.reset_peak_memory_stats()
    t1 = time.time()
    try:
        wav = model.generate_speech(
            it["text"], tok,
            reference_codes=rc["codes"],
            reference_text=rc["text"],
            max_new_tokens=int(t.get("max_new_tokens", MAXTOK)),
            temperature=temp,
            top_p=args.top_p,
            top_k=args.top_k,
        )
        dt = time.time() - t1
        a = to_arr(wav)
        fname = (f"{sid.replace('#','_').replace('.','_')}_{role}_"
                 f"{ref.replace('.wav','')}_t{temp:.1f}_s{vi}.wav")
        peak, dur = save_wav(os.path.join(OUT, fname), a, int(t.get("sr", 24000)), args.fade_ms)
        MANIFEST.append({
            "key": key, "id": sid, "role": role, "ref_wav": ref,
            "emotion": it.get("emotion"), "emotion_tag": it.get("emotion_tag", ""),
            "text_sent": it["text"], "text_plain": it.get("text_plain", ""),
            "temp": temp, "variant": vi, "seed": seed,
            "top_p": args.top_p, "top_k": args.top_k,
            "max_new_tokens": int(t.get("max_new_tokens", MAXTOK)), "sr": int(t.get("sr", 24000)),
            "file": fname, "duration_s": round(dur, 2), "gen_s": round(dt, 2),
            "rtf": round(dt / dur, 3) if dur else None,
            "peak": round(peak, 4), "peak_dbfs": round(20 * np.log10(peak + 1e-12), 2),
            "vram_gb": round(torch.cuda.max_memory_allocated() / 1e9, 2),
            "tag_words_risk": has_tag_words(it["text"]),
            "shard": args.shard, "ok": True,
        })
        n_ok += 1
        log(f"OK  {key:56} {dur:6.2f}s RTF={dt/dur if dur else 0:5.2f} "
            f"vram={MANIFEST[-1]['vram_gb']}GB  [{n_ok}/{len(TASKS)}]")
    except Exception as e:
        n_fail += 1
        log(f"FAIL {key}: {type(e).__name__}: {str(e)[:220]}")
        traceback.print_exc()
        MANIFEST.append({"key": key, "id": sid, "role": role, "ref_wav": ref,
                         "temp": temp, "variant": vi, "shard": args.shard, "ok": False,
                         "error": f"{type(e).__name__}: {str(e)[:300]}"})
    json.dump(MANIFEST, open(MAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

json.dump(MANIFEST, open(MAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
log(f"=== WORKER {args.shard} XONG: {n_ok} OK / {n_fail} FAIL | {time.time()-t_start:.0f}s ===")
sys.exit(0 if n_fail == 0 else 3)
