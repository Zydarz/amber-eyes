#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thử chọn giọng cho 3 vai chính (23/10/2026, theo yêu cầu người dùng):
    Host: trầm ấm · Điều tra viên: lạnh lùng · Chuyên gia tâm lý: nhấn mạnh — mỗi vai khác hẳn nhau.

Mọi bản đọc dùng BỘ THAM SỐ AN TOÀN (neutral, cao độ 0) — báo cáo BaoCao_GiongDoc_Tap02.md: đổi cảm xúc/cao độ
có thể làm giọng đổi "người". Mỗi ứng viên đọc 2 câu đặc trưng của vai.
Đo: CER (listen_audio), F0, rồi mô hình nghe chấm hợp vai + có giữ nguyên 1 người qua 2 câu không.
Output: 02_SAN_XUAT/Tap02/thu_giong_vai/  (report.md, <vai>_ung_vien.mp3)
"""
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from voice_audition import pcm, cer  # noqa: E402
from voice_expr_test import f0_track  # noqa: E402

ROOT = Path(r"D:\TEST\Gax\Audi")
OUT = ROOT / "02_SAN_XUAT" / "Tap02" / "thu_giong_vai"
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

ROLES = {
    "H": {"ten": "Host", "chat": "trầm ấm", "en": "warm, deep, intimate late-night podcast narrator — captivating, trustworthy",
          "speed": 0.90,
          "cau": ["Thế nhưng, có ai ngờ rằng người đàn ông khoác trên mình bộ quân phục đính đầy huân chương danh dự ấy, lại biến mất vào bóng tối của những thị trấn ngoại ô.",
                  "Chúng ta hãy luôn nhớ: bộ óc tinh hoa không bảo vệ được ai cả. Nó chỉ làm cho lần sụp đổ ấy đến muộn hơn, và nặng hơn."],
          "giong": ["audiobook_male_1", "English_magnetic_voiced_man", "English_Deep-VoicedGentleman", "English_Trustworth_Man",
                    "English_CaptivatingStoryteller", "Chinese (Mandarin)_Radio_Host", "English_Steadymentor",
                    "Chinese (Mandarin)_Sincere_Adult"]},
    "D": {"ten": "Điều tra viên", "chat": "lạnh lùng", "en": "cold, detached, clinical police investigator — flat affect, precise, unemotional",
          "speed": 0.95,
          "cau": ["Tuyết mới rơi đã lưu lại gần nhà nạn nhân một dấu vết lốp xe vô cùng đặc thù, cùng một dấu giày đi tuyết cỡ lớn.",
                  "Rồi Smyth đặt lên bàn dấu giày của chính Williams, và nói: Chúng giống hệt nhau."],
          "giong": ["male-qn-qingse", "Korean_ColdYoungMan", "Japanese_SeriousCommander", "English_ReservedYoungMan",
                    "Chinese (Mandarin)_News_Anchor", "Korean_IntellectualMan", "Japanese_ColdQueen"]},
    "C": {"ten": "Chuyên gia tâm lý", "chat": "nhấn mạnh", "en": "emphatic, assertive psychologist — stresses key words, persuasive, confident, intellectual",
          "speed": 0.92,
          "cau": ["Khi phân tích trường hợp của Russell Williams, chúng ta không thể nhìn nhận hắn như một kẻ loạn thần mất trí.",
                  "Đó không phải là sự hối hận. Đó là sự sợ hãi, sợ mất đi hình tượng mà hắn đã dày công xây dựng."],
          "giong": ["audiobook_female_1", "English_AssertiveQueen", "English_ConfidentWoman", "Korean_DecisiveQueen",
                    "English_Wiselady", "Chinese (Mandarin)_Mature_Woman", "English_MatureBoss"]},
}


def mcode(args, timeout=900, tries=4):
    for n in range(tries):
        r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        if r.returncode == 0:
            return json.loads(r.stdout)
        if n < tries - 1:
            time.sleep(10 * (n + 1))
            continue
        raise RuntimeError(r.stderr[:400] or r.stdout[:400])


def safe(v):
    return v.replace("(", "").replace(")", "").replace(" ", "_")


def jobs():
    out = []
    for r, R in ROLES.items():
        for v in R["giong"]:
            for k, txt in enumerate(R["cau"]):
                out.append((r, v, k, txt, f"{r}_{safe(v)}_{k}"))
    return out


def tts(J):
    OUT.mkdir(parents=True, exist_ok=True)
    todo = [j for j in J if not (OUT / (j[4] + ".mp3")).exists()]
    for b in range(0, len(todo), 10):
        batch = todo[b:b + 10]
        req = [{"text": t, "voice_id": v, "emotion": "neutral", "speed": ROLES[r]["speed"], "pitch": 0,
                "volume": 1.0, "output_file": f} for r, v, k, t, f in batch]
        af = OUT / f"_args_{b // 10}.json"
        af.write_text(json.dumps({"requests": req}, ensure_ascii=False), encoding="utf-8")
        res = mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)])
        for it in res.get("success_items", []):
            url = mcode(["get_asset_url", it["node_id"]], 120)["download_url"]
            urllib.request.urlretrieve(url, OUT / it["file_name"])
        for f in res.get("failed_items", []):
            print("!! TTS lỗi", batch[f["index"]][4], f.get("error_msg"))
        print(f"  TTS lô {b // 10}: {res.get('total_success')}/{len(batch)}", flush=True)


def asr(J):
    res = {}
    cache = OUT / "_asr.json"
    if cache.exists():
        res = json.loads(cache.read_text(encoding="utf-8"))
    for r, v, k, t, f in J:
        if f in res or not (OUT / (f + ".mp3")).exists():
            continue
        url = mcode(["upload-temp-url", str(OUT / (f + ".mp3"))], 300)["temp_url"]
        af = OUT / "_asr_args.json"
        af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg",
                                                 "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
                                 ensure_ascii=False), encoding="utf-8")
        try:
            res[f] = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600).get("transcription", "")
        except Exception as e:  # noqa: BLE001
            res[f] = f"(lỗi: {e})"
        cache.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res


def join(paths, out):
    args = [str(FF), "-y", "-v", "error"]
    for p in paths:
        args += ["-i", str(p)]
    n = len(paths)
    parts = "".join(f"[{i}:a]aresample=32000,aformat=channel_layouts=mono,apad=pad_dur=1.0[a{i}];" for i in range(n))
    parts += "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[o]"
    subprocess.run(args + ["-filter_complex", parts, "-map", "[o]", "-c:a", "libmp3lame", "-b:a", "128k", str(out)], check=True)


def judge():
    """Mỗi vai một file: ứng viên lần lượt, mỗi người 2 câu. Mô hình chấm hợp vai + 1 người hay 2."""
    res = {}
    for r, R in ROLES.items():
        vs = [v for v in R["giong"] if all((OUT / f"{r}_{safe(v)}_{k}.mp3").exists() for k in (0, 1))]
        out = OUT / f"{r}_ung_vien.mp3"
        join([OUT / f"{r}_{safe(v)}_{k}.mp3" for v in vs for k in (0, 1)], out)
        url = mcode(["upload-temp-url", str(out)], 300)["temp_url"]
        labels = ", ".join(f"V{i + 1} = readings {2 * i + 1}-{2 * i + 2}" for i in range(len(vs)))
        p = (f"This file has {2 * len(vs)} Vietnamese readings separated by ~1 s silence: {len(vs)} candidate voices, "
             f"each reading 2 sentences in a row ({labels}). Role being cast: {R['en']}. "
             "For EACH candidate V1..Vn give 1-10 scores: (a) fit to the role's tone, (b) natural Vietnamese pronunciation/tones, "
             "(c) appeal (would listeners enjoy a 25-minute documentary with this voice). Also (d) do its 2 readings sound like the SAME person (yes/no). "
             "Then rank the top 3 for this role with one line each. Compact table, be critical.")
        af = OUT / f"_judge_{r}.json"
        af.write_text(json.dumps({"audio_info": [{"url": url, "mime_type": "audio/mpeg", "prompt": p}]}, ensure_ascii=False),
                      encoding="utf-8")
        out_j = mcode(["connector", "call", "connector__matrix__audios_understand", "--args-file", str(af)], 900)
        res[r] = {"order": vs, "text": (out_j.get("results") or [{}])[0].get("description", json.dumps(out_j)[:300])}
        print(f"  chấm vai {r} xong", flush=True)
    (OUT / "_judge.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res


def main():
    J = jobs()
    tts(J)
    A = asr(J)
    rows = []
    for r, v, k, t, f in J:
        p = OUT / (f + ".mp3")
        if not p.exists():
            continue
        x, sr = pcm(p)
        f0 = f0_track(x, sr)
        rows.append((r, v, k, float(np.median(f0)) if len(f0) else 0, cer(t, A.get(f, "")), A.get(f, "")))
    Jd = judge()
    md = ["# Thử chọn giọng 3 vai chính — Tập 02 (23/10/2026)", "",
          "Tất cả đọc ở bộ tham số an toàn: neutral, cao độ 0. Nghe: `<vai>_ung_vien.mp3` — mỗi ứng viên 2 câu liền, theo thứ tự bảng.", ""]
    for r, R in ROLES.items():
        md += [f"## {R['ten']} — {R['chat']}", "", "| # | Giọng | F0 câu 1 / câu 2 | CER câu 1 / câu 2 |", "|---|---|---|---|"]
        for i, v in enumerate(Jd[r]["order"]):
            rr = [x for x in rows if x[0] == r and x[1] == v]
            f0s = " / ".join(f"{x[3]:.0f} Hz" for x in sorted(rr, key=lambda x: x[2]))
            cers = " / ".join(f"{100 * x[4]:.1f}%" for x in sorted(rr, key=lambda x: x[2]))
            md.append(f"| V{i + 1} | `{v}` | {f0s} | {cers} |")
        md += ["", "**Mô hình nghe chấm:**", "", Jd[r]["text"], ""]
    md += ["## Nhận dạng lại (ASR)", ""] + [f"- `{r}` `{v}` câu {k + 1}: {h}" for r, v, k, _, _, h in rows]
    (OUT / "report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("xong:", OUT / "report.md")


if __name__ == "__main__":
    main()
