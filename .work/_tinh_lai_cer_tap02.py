#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""J — Tính LẠI CER từ cache ASR đã có, sửa lỗi chuẩn hóa số + lỗi ASR bị chặn.

Lỗi 1 (số): ref đã qua vi_numbers() nên là CHỮ ("tám mươi tám"),
              còn ASR trả về SỐ ("88") -> CER phình to. Phải vi_numbers() cả hyp.
Lỗi 2 (chặn): 1 câu bị Gemini filter chặn, chuỗi lỗi bị dính vào transcription.
"""
import json
import os
import re
import sys
import unicodedata
import difflib
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_EP"] = "02"
WORK = Path(__file__).resolve().parents[1] / ".work"
OUT = WORK / "cer_bo_a_tap02"
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402
import tts_sentences as TS  # noqa: E402

BLOCK = re.compile(r"(This request was blocked.*|You can \[send feedback\].*)$", re.S)


def norm(t):
    t = unicodedata.normalize("NFC", t.lower())
    t = re.sub(r"[^\w\s]", " ", t)
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


def words(t):
    return norm(t).split()


def diff_words(ref, hyp):
    a, b = words(ref), words(hyp)
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b).get_opcodes():
        if tag == "equal":
            continue
        out.append({"op": tag, "ref": " ".join(a[i1:i2]), "hyp": " ".join(b[j1:j2])})
    return out


rows = json.loads((OUT / "rows.json").read_text(encoding="utf-8"))

# --- phat hien va lam lai cac cau bi CHAN ---
bad = 0
for r in rows:
    h = r["hyp"]
    if BLOCK.search(h):
        bad += 1
        r["_retry"] = True
        print(f"  -> ASR bi chan, se chay lai: {r['id']}")
print(f"So cau bi chan: {bad}")

if bad:
    import subprocess
    import urllib.request

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

    for r in rows:
        if not r.get("_retry"):
            continue
        local = WORK / "audio_s_t02" / fname(r["id"])
        up = mcode(["upload_temp_url", str(local), "--mime-type", "audio/mpeg"], 300)
        url = up.get("temp_url") or up.get("url")
        af = OUT / f"req_{local.stem}.json"
        af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg",
                                                 "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
                                  ensure_ascii=False), encoding="utf-8")
        tr = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600)
        (OUT / f"asr_{local.stem}.json").write_text(json.dumps(tr, ensure_ascii=False), encoding="utf-8")
        r["hyp"] = tr.get("transcription") or tr.get("text") or ""
        print(f"  -> chay lai xong: {r['id']}")

# --- tinh lai CER ---
for r in rows:
    h = BLOCK.sub("", r["hyp"]).strip()
    h = TS.vi_numbers(h)               # hyp -> dang chu, giong ref
    r["hyp_clean"] = h
    r["cer"] = cer(r["ref"], h)
    r["diff"] = diff_words(r["ref"], h)

(OUT / "rows_fixed.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

ROLE = {"H": "Host", "D": "Dieu tra vien", "C": "Chuyen gia", "CTRL": "Doi chung"}
md = ["# CER tiếng Việt — Tập 02 (đã sửa chuẩn hóa số + loại lỗi ASR bị chặn)", "",
      "Đo trên chính file TTS đã xuất của Tập 02. ASR = `listen_audio`, CER = `cer()` của dự án.",
      "Cả hai vế (chuẩn và giọng đọc) đều đưa về dạng chữ bằng `vi_numbers()` trước khi so.",
      "Ngưỡng dự án: **< 2%**.", ""]
for grp in ("H", "D", "C", "CTRL"):
    sub = [x for x in rows if x["role"] == grp]
    if not sub:
        continue
    cers = sorted(x["cer"] for x in sub)
    med = cers[len(cers) // 2]
    mean = sum(cers) / len(cers)
    voices = sorted({x["voice"] for x in sub})
    md.append(f"## {ROLE[grp]} — {', '.join('`'+v+'`' for v in voices)}")
    md.append(f"- Số câu: **{len(sub)}** · CER trung vị **{100*med:.1f}%** · trung bình **{100*mean:.1f}%** · "
              f"thấp nhất {100*cers[0]:.1f}% · cao nhất {100*cers[-1]:.1f}%")
    md.append(f"- Vượt ngưỡng 2%: **{sum(1 for c in cers if c > 0.02)}/{len(cers)}** câu")
    md.append("")
    md.append("| id | CER | AI nghe sai chỗ nào |")
    md.append("|---|---:|---|")
    for x in sorted(sub, key=lambda y: -y["cer"]):
        if x["cer"] <= 0:
            continue
        d = "; ".join(f"[{o['op']}] \"{o['ref']}\" -> \"{o['hyp']}\"" for o in x["diff"]) or "(khac o muc do khoi dong)"
        md.append(f"| `{x['id']}` | {100*x['cer']:.1f}% | {d[:260]} |")
    clean = [x for x in sub if x["cer"] == 0]
    md.append(f"| _({len(clean)} câu CER = 0,0%)_ | 0,0% | |")
    md.append("")

(OUT / "report_fixed.md").write_text("\n".join(md), encoding="utf-8")
print("\n".join(md))
