#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""K — In chi tiet cac cau loi + chay ASR LAN 2 de kiem chung doc lap (ASR khong tat dinh)."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_EP"] = "02"
WORK = Path(r"D:\TEST\Gax\Audi\.work")
OUT = WORK / "cer_bo_a_tap02"
sys.path.insert(0, str(WORK))
import tts_sentences as TS  # noqa: E402

BLOCK = re.compile(r"(This request was blocked.*|You can \[send feedback\].*)$", re.S)


def norm(t):
    t = re.sub(r"[^\w\s]", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()


def cer(ref, hyp):
    a, b = norm(ref), norm(hyp)
    if not a:
        return 0.0
    d = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(b) + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (a[i - 1] != b[j - 1]))
            prev = cur
    return d[-1] / len(a)


def mcode(args, timeout=600):
    p = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "")[:300])
    return json.loads(p.stdout)


def fname(sid):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}.mp3"


rows = json.loads((OUT / "rows_fixed.json").read_text(encoding="utf-8"))

print("=" * 100)
print("CHI TIET CAU CO CER > 0  (vai chinh)")
print("=" * 100)
bad = [r for r in rows if r["role"] in ("H", "D", "C") and r["cer"] > 0]
for r in sorted(bad, key=lambda x: -x["cer"]):
    print(f"\n[{r['role']}] {r['id']}  CER={100*r['cer']:.1f}%   voice={r['voice']}")
    print(f"  CHUAN : {r['ref']}")
    print(f"  NGHE  : {r['hyp_clean']}")

# ---- LAN 2: chi lai cac cau > 2% (ca vai chinh) ----
targets = [r for r in rows if r["role"] in ("H", "D", "C") and r["cer"] > 0.02]
print("\n" + "=" * 100)
print(f"CHAY LAN 2: {len(targets)} cau vượt ngưỡng 2% -> kiem chung doc lap")
print("=" * 100)
for r in targets:
    local = WORK / "audio_s_t02" / fname(r["id"])
    try:
        up = mcode(["upload_temp_url", str(local), "--mime-type", "audio/mpeg"], 300)
        url = up.get("temp_url") or up.get("url")
        af = OUT / f"req2_{local.stem}.json"
        af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg",
                                                 "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
                                  ensure_ascii=False), encoding="utf-8")
        tr = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600)
        h2 = BLOCK.sub("", tr.get("transcription") or tr.get("text") or "").strip()
        c2 = cer(r["ref"], TS.vi_numbers(h2))
        same = "SAME" if abs(c2 - r["cer"]) < 1e-9 else "KHAC"
        print(f"\n[{r['role']}] {r['id']}: LAN1 {100*r['cer']:.1f}%  ->  LAN2 {100*c2:.1f}%   ({same})")
        print(f"  LAN2 NGHE: {TS.vi_numbers(h2)}")
    except Exception as e:  # noqa: BLE001
        print(f"\n[{r['role']}] {r['id']}: LAN2 that bai: {e}")
