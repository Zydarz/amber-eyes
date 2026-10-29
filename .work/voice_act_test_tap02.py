#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thử diễn xuất từng câu cho bản tiếng Việt (Tập 02).

Phản hồi Tập 01: giọng đều đều, không lên xuống. Mỗi câu then chốt được đọc 3 kiểu:
  A  như Tập 01: cảm xúc theo lượt, tốc độ gốc, không ngắt nghỉ
  B  diễn xuất từng câu: cảm xúc + tốc độ + cao độ riêng, ngắt nghỉ <#s#> và "..."
  C  như B nhưng với giọng thay thế
Đo: thời lượng, âm tiết/giây, tỉ lệ ngắt nghỉ, F0 trung vị, CER (listen_audio), thẻ có bị đọc ra không.
Output: 02_SAN_XUAT/Tap02/thu_giong/report.md + so_sanh_dien_xuat.mp3
"""
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from voice_audition import pcm, cer, FF, f0_median  # noqa: E402

ROOT = Path(r"D:\TEST\Gax\Audi")
import os
ROUND = os.environ.get("ROUND", "1")
OUT = ROOT / "02_SAN_XUAT" / "Tap02" / ("thu_giong" if ROUND == "1" else f"thu_giong_vong{ROUND}")
CUR = {"H": "audiobook_male_1", "D": "male-qn-qingse", "C": "audiobook_female_1",
       "N2": "English_captivating_female1"}
ALT = {"H": ["English_magnetic_voiced_man", "English_expressive_narrator", "English_Trustworth_Man"],
       "D": ["English_Deep-VoicedGentleman", "English_ManWithDeepVoice", "Chinese (Mandarin)_Gentleman"],
       "C": ["English_Wiselady", "English_CalmWoman", "Chinese (Mandarin)_Wise_Women"],
       "N2": ["English_SereneWoman", "Vietnamese_kindhearted_girl"]}
BASE = {"H": 0.90, "D": 0.95, "C": 0.92, "N2": 0.95}

# (câu, vai, lời gốc, cảm xúc Tập 01, [cảm xúc B, tốc độ B, cao độ B, lời đọc B])
LINES = [
    ("1.08#3", "H", "Chỉ còn một kẻ rình rập, lặng lẽ bước qua những hàng rào tuyết trắng.", "sad",
     ["fearful", 0.84, -2, "Chỉ còn... <#0.3#> một kẻ rình rập. <#0.4#> Lặng lẽ bước qua những hàng rào tuyết trắng."]),
    ("1.14#3", "H", "Người ngồi sau vô-lăng hạ cửa kính xuống – chính là Chỉ huy trưởng căn cứ không quân Trenton.", "sad",
     ["surprised", 0.86, -1, "Người ngồi sau vô-lăng hạ cửa kính xuống... <#0.6#> chính là... <#0.3#> Chỉ huy trưởng căn cứ không quân Trenton."]),
    ("4.10#8", "D", "Khoảng bốn tiếng bốn mươi phút sau khi buổi thẩm vấn bắt đầu, Smyth hỏi khẽ: Vậy, cô ấy ở đâu?", "neutral",
     ["sad", 0.88, -1, "Khoảng bốn tiếng bốn mươi phút sau khi buổi thẩm vấn bắt đầu... <#0.4#> Smyth hỏi khẽ: <#0.5#> Vậy... <#0.3#> cô ấy ở đâu?"]),
    ("4.10#9", "D", "Và Williams hỏi lại: Có bản đồ không?", "neutral",
     ["neutral", 0.84, -2, "Và Williams hỏi lại... <#0.7#> Có bản đồ không?"]),
    ("3.05#11", "C", "Đó là một chiếc dốc không đáy: ngưỡng thỏa mãn liên tục bị đẩy xa hơn cho đến khi dẫn tới án mạng.", "neutral",
     ["fearful", 0.86, -1, "Đó là một chiếc dốc... <#0.3#> không đáy. <#0.5#> Ngưỡng thỏa mãn liên tục bị đẩy xa hơn... <#0.3#> cho đến khi dẫn tới án mạng."]),
    ("4.11#11", "C", "Đó là sự sợ hãi – sợ mất đi hình tượng mà hắn đã dày công xây dựng.", "neutral",
     ["sad", 0.88, -1, "Đó là sự sợ hãi. <#0.5#> Sợ mất đi... <#0.2#> hình tượng mà hắn đã dày công xây dựng."]),
    ("4.06#3", "N2", "Vậy bằng cách nào mà một người sắt đá như thế lại tự miệng thú nhận toàn bộ chỉ sau vài tiếng đồng hồ?", "neutral",
     ["surprised", 0.95, 1, "Vậy bằng cách nào... <#0.3#> mà một người sắt đá như thế... <#0.2#> lại tự miệng thú nhận toàn bộ, chỉ sau vài tiếng đồng hồ?"]),
]


def mcode(args, timeout=900, tries=4):
    import time
    for n in range(tries):
        r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        if r.returncode == 0:
            return json.loads(r.stdout)
        msg = r.stderr[:500] or r.stdout[:500]
        if "Network request failed" in msg and n < tries - 1:
            time.sleep(10 * (n + 1))
            continue
        raise RuntimeError(msg)


def moderate(text):
    """Vòng 2: bỏ ngắt đôi ('...' + thẻ), tối đa 2 thẻ/câu, mỗi thẻ ≤ 0,35 s; '...' còn lại thành dấu phẩy."""
    text = re.sub(r"\.\.\.\s*<#([\d.]+)#>", lambda m: f", <#{min(float(m.group(1)), 0.35)}#>", text)
    text = re.sub(r"<#([\d.]+)#>", lambda m: f"<#{min(float(m.group(1)), 0.35)}#>", text)
    tags = [(float(m.group(1)), m.start()) for m in re.finditer(r"<#([\d.]+)#>", text)]
    drop = {pos for _, pos in sorted(tags, reverse=True)[2:]}
    out, last = "", 0
    for m in re.finditer(r"\s?<#([\d.]+)#>", text):
        out += text[last:m.start()] + ("" if m.start() + (1 if m.group(0).startswith(" ") else 0) in drop else m.group(0))
        last = m.end()
    out += text[last:]
    out = out.replace("...", ",")
    return re.sub(r",\s*,", ",", re.sub(r"\s{2,}", " ", out)).replace(", .", ".").strip()


BEST_ALT = {"H": "English_Trustworth_Man", "D": "Chinese (Mandarin)_Gentleman", "C": "English_CalmWoman"}


def variants():
    if ROUND == "3":                     # vòng 3: lấy đúng diễn xuất đã làm mềm trong acting_tap02.json
        act = json.loads((ROOT / ".work" / "acting_tap02.json").read_text(encoding="utf-8"))
        out = []
        for sid, role, text, emo_a, _ in LINES:
            emo, dsp, pi, alt = act[sid]
            sp = round(BASE[role] + dsp, 2)
            out.append((sid, role, "A", CUR[role], emo_a, BASE[role], 0, text))
            out.append((sid, role, "S", CUR[role], emo, sp, pi, alt or text))
            if role in BEST_ALT:
                out.append((sid, role, "S2", BEST_ALT[role], emo, sp, pi, alt or text))
        return out
    if ROUND != "1":
        out = []
        for sid, role, text, emo_a, (emo, sp, pi, alt) in LINES:
            msp = round(min(BASE[role], max(BASE[role] - 0.06, sp + 0.04)), 2)
            out.append((sid, role, "A", CUR[role], emo_a, BASE[role], 0, text))
            out.append((sid, role, "M", CUR[role], emo, msp, pi, moderate(alt)))
            if role in BEST_ALT:
                out.append((sid, role, "M2", BEST_ALT[role], emo, msp, pi, moderate(alt)))
        return out
    out = []
    for sid, role, text, emo_a, (emo, sp, pi, alt) in LINES:
        out.append((sid, role, "A", CUR[role], emo_a, BASE[role], 0, text))
        out.append((sid, role, "B", CUR[role], emo, sp, pi, alt))
        for k, v in enumerate(ALT.get(role, []), 1):
            out.append((sid, role, f"C{k}", v, emo, sp, pi, alt))
    return out


def pause_share(x, sr):
    hop = int(0.02 * sr)
    e = np.array([np.sqrt((x[i:i + hop] ** 2).mean()) for i in range(0, len(x) - hop, hop)])
    on = np.where(e > 0.02)[0]
    if len(on) == 0:
        return 0.0
    e = e[on[0]:on[-1] + 1]                      # trong câu, bỏ lặng đầu/cuối
    return float((e < 0.012).mean())


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    V = variants()
    files = {}
    for b in range(0, len(V), 10):
        cache = OUT / f"res_{b // 10}.json"
        reqs = [{"text": v[7].replace("“", "").replace("”", ""), "voice_id": v[3], "emotion": v[4],
                 "speed": v[5], "pitch": v[6], "volume": 1.0,
                 "output_file": f"{b + k:02d}_{v[0].replace('.', '_').replace('#', '-')}_{v[2]}"}
                for k, v in enumerate(V[b:b + 10])]
        if cache.exists():
            res = json.loads(cache.read_text(encoding="utf-8"))
        else:
            af = OUT / f"args_{b // 10}.json"
            af.write_text(json.dumps({"requests": reqs}, ensure_ascii=False), encoding="utf-8")
            res = mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)])
            if res.get("total_success"):
                cache.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        for f in res.get("failed_items", []):
            print("!! TTS lỗi", reqs[f["index"]]["output_file"], f.get("error_msg"))
        for it in res.get("success_items", []):
            i = int(it["file_name"][:2])
            local = OUT / it["file_name"]
            url_cache = OUT / f"url_{i:02d}.txt"
            if not local.exists():
                url = mcode(["get_asset_url", it["node_id"]], 120)["download_url"]
                urllib.request.urlretrieve(url, local)
                url_cache.write_text(url, encoding="utf-8")
            files[i] = (local, url_cache.read_text(encoding="utf-8") if url_cache.exists() else None)

    rows = []
    for i, (sid, role, var, voice, emo, sp, pi, said) in enumerate(V):
        if i not in files:
            continue
        local, url = files[i]
        x, sr = pcm(local)
        dur = len(x) / sr
        ref = next(l[2] for l in LINES if l[0] == sid)
        hyp = ""
        asr = OUT / f"asr_{i:02d}.json"
        if asr.exists():
            hyp = json.loads(asr.read_text(encoding="utf-8")).get("transcription", "")
        elif url:
            af = OUT / f"asr_args_{i:02d}.json"
            af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg",
                                                     "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
                                     ensure_ascii=False), encoding="utf-8")
            try:
                tr = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600)
                asr.write_text(json.dumps(tr, ensure_ascii=False), encoding="utf-8")
                hyp = tr.get("transcription", "")
            except Exception as e:  # noqa: BLE001
                hyp = f"(lỗi nhận dạng: {e})"
        leak = bool(re.search(r"thăng|#|chấm bốn|không phẩy", hyp))
        rows.append({"i": i, "sid": sid, "role": role, "var": var, "voice": voice, "emo": emo, "speed": sp,
                     "pitch": pi, "dur": dur, "rate": len(ref.split()) / dur, "pause": pause_share(x, sr),
                     "f0": f0_median(x, sr), "cer": cer(ref, hyp), "leak": leak, "hyp": hyp})

    md = ["# Thử diễn xuất giọng tiếng Việt — Tập 02", "",
          "A = như Tập 01 · B = diễn xuất từng câu (giọng hiện tại) · C1–C3 = diễn xuất + giọng thay thế. "
          "Nghe theo thứ tự trong `so_sanh_dien_xuat.mp3` (mỗi câu: A → B → C1 → C2 → C3, cách nhau 1 s).", "",
          "| # | Câu | Vai | Kiểu | Giọng | cảm xúc · tốc độ · cao độ | Thời lượng | Âm tiết/s | Tỉ lệ ngắt | F0 | CER | Thẻ bị đọc? |",
          "|---|---|---|---|---|---|---:|---:|---:|---:|---:|---|"]
    for r in rows:
        md.append(f"| {r['i']:02d} | `{r['sid']}` | {r['role']} | {r['var']} | `{r['voice']}` | {r['emo']} · {r['speed']} · {r['pitch']:+d} "
                  f"| {r['dur']:.1f} s | {r['rate']:.2f} | {100 * r['pause']:.0f}% | {r['f0']:.0f} Hz | {100 * r['cer']:.1f}% "
                  f"| {'CÓ' if r['leak'] else 'không'} |")
    md += ["", "## Nhận dạng lại (ASR)", ""] + [f"- {r['i']:02d} {r['var']}: {r['hyp']}" for r in rows]
    (OUT / "report.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # file nghe so sánh: các bản cách nhau 1 s
    sil = OUT / "_sil.wav"
    subprocess.run([str(FF), "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=32000:cl=mono", "-t", "1.0", str(sil)])
    lst = OUT / "list.txt"
    lst.write_text("".join(f"file '{files[i][0].as_posix()}'\nfile '{sil.as_posix()}'\n" for i in sorted(files)),
                   encoding="utf-8")
    subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-ar", "32000", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "160k", str(OUT / "so_sanh_dien_xuat.mp3")])
    print("\n".join(md[:len(rows) + 5]))


if __name__ == "__main__":
    main()
