# -*- coding: utf-8 -*-
"""Cổng M3b (QUY_TAC_HIGGS_MAC.md) — kiểm TỪNG FILE CÂU Higgs ngay sau khi sinh,
TRƯỚC khi chuyển sang trộn. Chạy được trên Mac (chỉ cần numpy; Whisper tuỳ chọn).

    # Mac, sau Bước 3 (sinh xong) — tách pha với MLX theo M2:
    AE_EP=10 AE_LANG=en python3 .work/qc_voice_sentence.py \
        --dir .work/audio_s_higgs_EN_t10 --manifest .work/tts_manifest_EN_t10.json [--fix] [--asr]

Lỗi đã gặp (Tập 10 EN, 12/11 và 15/11/2026): file câu chứa 21–26 s không có lời
(câu 2.06#3–#6 rồi 2.08#1) ⇒ master mất giọng, mọi cổng cũ vẫn xanh.
`trim_silence_tail` cũ dò ngược từ cuối, dừng ở cửa sổ 20 ms đầu tiên ≥ −45 dB
⇒ 1 tiếng tách/xì ở đuôi là thoát; và không xét câm ở ĐẦU hay GIỮA file.

Đo mỗi file (cửa sổ 20 ms). "Câm" = dưới max(−45 dBFS, mức nói trung vị − 30 dB)
⇒ bắt được cả đoạn xì nền to hơn −45 dB.
  REGEN (sinh lại, variant khác) khi:
    · đoạn câm ở GIỮA dài nhất > 1,0 s
    · tỉ lệ có lời < 70 %
    · [--asr] từ cuối Whisper nghe được kết thúc sớm hơn cuối file > 0,8 s, hoặc 2 từ liền cách > 1,5 s
  NGHE (cảnh báo, nghe kiểm — không tự sinh lại): thời lượng > 1,6 × dự kiến hoặc > dự kiến + 3 s
        (dự kiến = số từ / tốc độ nói trung vị của vai, tính trên cả file)
  TRIM (cắt được, không cần sinh lại): câm đầu > 0,5 s hoặc đuôi > 0,8 s
    --fix ⇒ cắt còn 0,1 s đầu / 0,3 s đuôi + fade 30 ms, sao lưu bản gốc sang <dir>/_truoc_trim/
Xuất <dir>/qc_voice_sentence.json (số đo + sha256 từng file = manifest giao cho Windows)
và <dir>/regen_ids.txt. Exit 1 khi còn câu REGEN.
"""
import argparse
import hashlib
import json
import re
import shutil
import sys
import wave
from pathlib import Path

import numpy as np

WIN = 0.02
GAP_MID_MAX, ACTIVE_MIN, RATIO_MAX, OVER_MAX = 1.0, 0.70, 1.6, 3.0
LEAD_MAX, TAIL_MAX, KEEP_LEAD, KEEP_TAIL = 0.5, 0.8, 0.1, 0.3
ASR_TAIL_MAX, ASR_GAP_MAX = 0.8, 1.5


def sid_to_file(sid):
    a, rest = sid.split(".")
    b, k = rest.split("#")
    return f"s{a}_{b}_{int(k):02d}.wav"


def read(p):
    with wave.open(str(p), "rb") as wf:
        sr, ch, n = wf.getframerate(), wf.getnchannels(), wf.getnframes()
        x = np.frombuffer(wf.readframes(n), np.int16).astype(np.float32) / 32768
    if ch > 1:
        x = x.reshape(-1, ch).mean(1)
    return x, sr, ch


def measure(x, sr):
    hop = int(sr * WIN)
    k = max(len(x) // hop, 1)
    db = 20 * np.log10(np.sqrt((x[: k * hop].reshape(k, hop) ** 2).mean(1)) + 1e-9)
    loud = db[db > -45]
    med = float(np.median(loud)) if loud.size else -90.0
    thr = max(-45.0, med - 30.0)
    act = db >= thr
    idx = np.flatnonzero(act)
    dur = len(x) / sr
    if idx.size == 0:
        return dict(dur=dur, lead=dur, tail=dur, gap_mid=dur, active=0.0, speech=0.0, thr=thr, first=0, last=0)
    first, last = int(idx[0]), int(idx[-1]) + 1
    inner = ~act[first:last]
    run = mx = 0
    for v in inner:
        run = run + 1 if v else 0
        mx = max(mx, run)
    return dict(dur=dur, lead=first * WIN, tail=(k - last) * WIN, gap_mid=mx * WIN,
                active=float(act.sum()) / k, speech=float(act.sum()) * WIN, thr=thr, first=first, last=last)


def write(p, x, sr):
    y = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(p), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(y.tobytes())


def trim(p, x, sr, m, bak):
    hop = int(sr * WIN)
    a = max(m["first"] * hop - int(KEEP_LEAD * sr), 0)
    b = min(m["last"] * hop + int(KEEP_TAIL * sr), len(x))
    bak.mkdir(exist_ok=True)
    if not (bak / p.name).exists():
        shutil.copy2(p, bak / p.name)
    y = x[a:b].copy()
    f = int(0.03 * sr)
    if len(y) > 2 * f:
        y[:f] *= np.linspace(0, 1, f)
        y[-f:] *= np.linspace(1, 0, f)
    write(p, y, sr)
    return y


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--manifest", required=True, help="tts_manifest_*.json (id, role, text)")
    ap.add_argument("--fix", action="store_true", help="cắt câm đầu/đuôi (sao lưu bản gốc)")
    ap.add_argument("--asr", action="store_true", help="đo thêm bằng Whisper word timestamps (chạy SAU khi tắt MLX, M2)")
    ap.add_argument("--asr-model", default="base")
    a = ap.parse_args()
    d = Path(a.dir)
    man = json.loads(Path(a.manifest).read_text(encoding="utf-8"))
    man = man if isinstance(man, list) else man.get("items", [])

    rows = []
    for it in man:
        p = d / sid_to_file(it["id"])
        r = {"id": it["id"], "role": it.get("role"), "file": p.name,
             "words": len(re.findall(r"\w+", it.get("text", "")))}
        if not p.exists():
            r.update(verdict="REGEN", why=["thiếu file"])
            rows.append(r)
            continue
        x, sr, _ = read(p)
        m = measure(x, sr)
        r["_x"], r["_sr"], r["_m"] = x, sr, m
        rows.append(r)

    # tốc độ nói trung vị theo vai (từ / giây cả file) — chỉ dùng câu không có câm giữa
    wps = {}
    for role in {r["role"] for r in rows}:
        v = [r["words"] / r["_m"]["dur"] for r in rows
             if r["role"] == role and "_m" in r and r["_m"]["speech"] > 0.5 and r["_m"]["gap_mid"] <= GAP_MID_MAX
             and r["_m"]["active"] >= ACTIVE_MIN]
        wps[role] = float(np.median(v)) if v else 2.5

    asr = None
    if a.asr:
        import whisper  # noqa: PLC0415
        asr = whisper.load_model(a.asr_model, device="cpu")

    for r in rows:
        if "_m" not in r:
            continue
        x, sr, m = r.pop("_x"), r.pop("_sr"), r.pop("_m")
        why, verdict = [], "OK"
        exp = r["words"] / wps[r["role"]] if r["words"] else m["dur"]
        if m["gap_mid"] > GAP_MID_MAX:
            why.append(f"câm giữa {m['gap_mid']:.1f}s")
        if m["active"] < ACTIVE_MIN:
            why.append(f"có lời {m['active']:.0%}")
        if why:
            verdict = "REGEN"
        elif m["dur"] > RATIO_MAX * exp or m["dur"] > exp + OVER_MAX:
            verdict = "NGHE"                     # dài bất thường nhưng không câm: người nghe quyết
            why.append(f"dài {m['dur']:.1f}s / dự kiến {exp:.1f}s")
        elif m["lead"] > LEAD_MAX or m["tail"] > TAIL_MAX:
            verdict = "TRIM"
            why.append(f"câm đầu {m['lead']:.1f}s · đuôi {m['tail']:.1f}s")
            if a.fix:
                x = trim(d / r["file"], x, sr, m, d / "_truoc_trim")
                m2 = measure(x, sr)
                verdict, m = "TRIMMED", m2
        if asr is not None and verdict != "REGEN":
            res = asr.transcribe(str(d / r["file"]), word_timestamps=True, language=None, fp16=False)
            ws = [w for s in res.get("segments", []) for w in s.get("words", [])]
            if ws:
                tail = len(x) / sr - ws[-1]["end"]
                gap = max([b["start"] - c["end"] for c, b in zip(ws, ws[1:])] or [0])
                r.update(asr_tail=round(tail, 2), asr_gap=round(gap, 2))
                if tail > ASR_TAIL_MAX or gap > ASR_GAP_MAX:
                    verdict = "REGEN"
                    why.append(f"ASR: đuôi {tail:.1f}s · khe {gap:.1f}s")
            else:
                verdict = "REGEN"
                why.append("ASR không nghe được từ nào")
        r.update(verdict=verdict, why=why, dur=round(m["dur"], 2), lead=round(m["lead"], 2),
                 tail=round(m["tail"], 2), gap_mid=round(m["gap_mid"], 2), active=round(m["active"], 3),
                 expected=round(exp, 2),
                 sha256=hashlib.sha256((d / r["file"]).read_bytes()).hexdigest()[:16])

    out = {"dir": str(d), "wps": wps, "thresholds": dict(gap_mid=GAP_MID_MAX, active=ACTIVE_MIN, ratio=RATIO_MAX,
           over=OVER_MAX, lead=LEAD_MAX, tail=TAIL_MAX, asr_tail=ASR_TAIL_MAX, asr_gap=ASR_GAP_MAX), "items": rows}
    (d / "qc_voice_sentence.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    regen = [r["id"] for r in rows if r["verdict"] == "REGEN"]
    (d / "regen_ids.txt").write_text("\n".join(regen) + ("\n" if regen else ""), encoding="utf-8")
    cnt = {v: sum(r["verdict"] == v for r in rows) for v in ("OK", "NGHE", "TRIM", "TRIMMED", "REGEN")}
    print(f"{len(rows)} câu · {cnt} · tốc độ nói (từ/s): " + ", ".join(f"{k} {v:.2f}" for k, v in sorted(wps.items())))
    for r in rows:
        if r["verdict"] in ("REGEN", "TRIM", "NGHE"):
            print(f"  {r['verdict']:5} {r['id']:8} {r.get('role')}: {'; '.join(r['why'])}")
    print("KẾT QUẢ:", "ĐẠT" if not regen and not cnt["TRIM"] else f"TRƯỢT — sinh lại {len(regen)} câu (regen_ids.txt)"
          + (f", {cnt['TRIM']} câu cần --fix" if cnt["TRIM"] else ""))
    sys.exit(1 if regen or cnt["TRIM"] else 0)


if __name__ == "__main__":
    main()
