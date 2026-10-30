# -*- coding: utf-8 -*-
"""Phép thử NGHE MÙ cho Tập 02 — dùng connector__matrix__audios_understand.

Không nói trước đáp án (không nói vai nào là file nào). Chỉ hỏi về danh tính người nói.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
VID = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp4"
LISTEN = WORK / "_review_tap02_listen"
OUT = WORK / "_review_tap02_listen"
LISTEN.mkdir(parents=True, exist_ok=True)

tl = json.loads((WORK / "timeline_s_t02.json").read_text(encoding="utf-8"))
items = tl["items"]


def pick(role, n):
    cands = [it for it in items if it["role"] == role and (it["end"] - it["start"]) >= 1.2]
    if not cands:
        return []
    step = len(cands) / n
    return [cands[int(i * step)] for i in range(min(n, len(cands)))]


def build(name, chosen, gap=0.7):
    seg_dir = LISTEN / (name + "_seg")
    seg_dir.mkdir(exist_ok=True)
    sil = LISTEN / "_silence.wav"
    if not sil.exists():
        subprocess.run([str(FF), "-y", "-v", "error", "-f", "lavfi",
                        "-i", f"anullsrc=r=48000:cl=stereo:d={gap}", str(sil)], check=True)
    seq = []
    for i, it in enumerate(chosen):
        dur = it["end"] - it["start"]
        p = seg_dir / f"{i:02d}.wav"
        if not p.exists():
            subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{it['start']:.3f}",
                            "-t", f"{dur:.3f}", "-i", str(VID), "-vn",
                            "-af", "aformat=sample_fmts=s16:channel_layouts=stereo,aresample=48000",
                            str(p)], check=True)
        seq.append(p)
        if i != len(chosen) - 1:
            seq.append(sil)
    lst = seg_dir / "list.txt"
    lst.write_text("".join(f"file '{f.as_posix()}'\n" for f in seq), encoding="utf-8")
    final = OUT / f"{name}.mp3"
    if not final.exists():
        subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c:a", "libmp3lame", "-b:a", "128k", str(final)], check=True)
    (OUT / f"{name}.json").write_text(
        json.dumps([{ "id": c["id"], "role": c["role"], "start": c["start"],
                      "text": c["text"][:60]} for c in chosen], ensure_ascii=False, indent=2),
        encoding="utf-8")
    return final


def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


# ---- tao file 5 vai xen ke (bat buoc cho G9/G10) ----
all5 = []
for r, n in (("H", 5), ("D", 5), ("C", 5), ("N1", 2), ("N2", 2)):
    all5 += pick(r, n)
all5.sort(key=lambda x: x["start"])
build("role_all5", all5)

# ---- tai len ----
names = ["role_H", "role_D", "role_C", "role_HDC", "role_N12", "role_all5"]
urls = {}
for n in names:
    f = OUT / f"{n}.mp3"
    if not f.exists():
        print(f"THIEU {f}")
        continue
    r = sh(f'mcode-tools upload_temp_url "{f}"')
    try:
        j = json.loads(r.stdout)
        urls[n] = j["temp_url"]
        print(f"upload {n}: OK")
    except Exception as e:
        print(f"upload {n}: LOI {r.stdout[:200]} {r.stderr[:200]}")

# ---- goi audios_understand ----
PROMPT_SINGLE = (
    "Bạn là một người nghe mù, không biết trước ai đang nói. "
    "Trong đoạn âm thanh này có nhiều đoạn lời nói tiếng Việt ngắn, ngăn cách bằng khoảng lặng ngắn. "
    "Hãy trả lời bằng tiếng Việt: "
    "(1) Có bao nhiêu người nói KHÁC NHAU trong toàn bộ đoạn? "
    "(2) Mô tả từng người: giới tính, khoảng cao độ (trầm hay cao), chất giọng, cảm xúc chung. "
    "(3) Có đoạn nào nghe ra là đột nhiên đổi giọng/đổi người không? Nêu vị trí. "
    "(4) Chấm độ ổn định danh tính của người đọc trên thang 1-10. "
    "Tập trung vào GIỌNG NGƯỜI, bỏ qua nội dung lời."
)
PROMPT_MIX = (
    "Bạn là một người nghe mù, không biết trước ai đang nói. "
    "Trong đoạn âm thanh này, các đoạn lời nói tiếng Việt được xen kẽ, mỗi đoạn cách nhau khoảng lặng. "
    "Hãy trả lời bằng tiếng Việt: "
    "(1) Có bao nhiêu người nói khác nhau? "
    "(2) Mỗi người khác nhau ở điểm nào (giới tính, cao độ, chất giọng)? "
    "(3) Người nghe không nhìn hình có tách được các người này không? Chấm độ tách bạch 1-10. "
    "(4) Có cặp người nào gần giống nhau đến mức dễ nhầm không? "
    "Tập trung vào GIỌNG NGƯỜI, bỏ qua nội dung lời."
)

entries = []
for n in names:
    if n not in urls:
        continue
    p = PROMPT_MIX if n in ("role_HDC", "role_N12", "role_all5") else PROMPT_SINGLE
    entries.append({"url": urls[n], "prompt": p, "mime_type": "audio/mpeg"})

all_out = {}
for bi in range(0, len(entries), 5):
    batch = entries[bi:bi + 5]
    args_file = OUT / f"blind_args_{bi // 5}.json"
    args_file.write_text(json.dumps({"audio_info": batch}, ensure_ascii=False), encoding="utf-8")
    print(f"goi audios_understand lot {bi // 5 + 1} voi {len(batch)} file ...")
    r = sh(f'mcode-tools connector call connector__matrix__audios_understand --args-file "{args_file}"')
    print("exit:", r.returncode)
    all_out[f"batch_{bi // 5}"] = r.stdout
    print(r.stdout[:6000])
    if r.stderr.strip():
        print("STDERR:", r.stderr[:1200])
(OUT / "blind_results.json").write_text(json.dumps(all_out, ensure_ascii=False, indent=2),
                                        encoding="utf-8")
print("XONG")
