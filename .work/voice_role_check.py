#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G10 (tiêu chuẩn A4.2) — nghe liền theo vai trước khi dựng.

Mỗi vai: ghép tối đa 12 câu rải đều trong tập (giữ đúng tham số đã đọc) → hỏi audios_understand
"mấy người?". Đạt khi mọi vai = 1 người. Thêm một file xen kẽ 3 vai chính (G9).
Chạy:  AE_EP=02 py -3 .work/voice_role_check.py
Output: <EP_DIR>/thu_giong_kiem_vai/report.md + file nghe
"""
import json
import re
import subprocess
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402

FF = ED.WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
OUT = ED.EP_DIR / "thu_giong_kiem_vai"
NAMES = {"H": "Host", "D": "Điều tra viên", "C": "Chuyên gia tâm lý", "N1": "N1", "N2": "N2"}
NAMES_EN = {"H": "Host / Narrator", "D": "Investigator", "C": "Psychologist",
            "N1": "Base personnel", "N2": "Case observer"}
NAMES_JA = {"H": "ホスト", "D": "捜査官", "C": "心理学者",
            "N1": "スプリングフィールド住民 (N1)", "N2": "視聴者 (N2)"}
NAMES_KO = {"H": "호스트", "D": "수사관", "C": "심리학자",
            "N1": "스프링필드 주민 (N1)", "N2": "시청자 (N2)"}


def mcode(args, timeout=900):
    for n in range(4):
        r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        if r.returncode == 0:
            return json.loads(r.stdout)
        time.sleep(10 * (n + 1))
    raise RuntimeError(r.stderr[:300] or r.stdout[:300])


def join(paths, out):
    args = [str(FF), "-y", "-v", "error"]
    for p in paths:
        args += ["-i", str(p)]
    n = len(paths)
    parts = "".join(f"[{i}:a]aresample=32000,aformat=channel_layouts=mono,apad=pad_dur=1.0[a{i}];" for i in range(n))
    parts += "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[o]"
    subprocess.run(args + ["-filter_complex", parts, "-map", "[o]", "-c:a", "libmp3lame", "-b:a", "128k", str(out)], check=True)


def ask(path, prompt):
    url = mcode(["upload-temp-url", str(path)], 300)["temp_url"]
    af = OUT / "_q.json"
    af.write_text(json.dumps({"audio_info": [{"url": url, "mime_type": "audio/mpeg", "prompt": prompt}]}, ensure_ascii=False),
                  encoding="utf-8")
    r = mcode(["connector", "call", "connector__matrix__audios_understand", "--args-file", str(af)])
    return (r.get("results") or [{}])[0].get("description", json.dumps(r)[:300])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    man = json.loads(ED.w("tts_manifest.json").read_text(encoding="utf-8"))
    names = NAMES_KO if ED.KO else (NAMES_JA if ED.JA else (NAMES_EN if ED.EN else NAMES))
    lang = "Korean" if ED.KO else ("Japanese" if ED.JA else ("English" if ED.EN else "Vietnamese"))
    md = [f"# G10 — nghe liền theo vai ({ED.MASTER})", ""]
    ok_all = True
    picks = {}
    for role in ("H", "D", "C", "N1", "N2"):
        items = [m for m in man if m["role"] == role]
        if not items:
            continue
        step = max(1, len(items) // 12)
        pick = items[::step][:12]
        picks[role] = pick
        out = OUT / f"vai_{role}.mp3"
        join([ED.w("audio_s") / m["file"] for m in pick], out)
        if len(pick) < 3:
            md += [f"## {names[role]} ({ED.CAST[role][0]}): {len(pick)} câu — bỏ qua (quá ít)", ""]
            continue
        ans = ask(out, f"This file has {len(pick)} short {lang} sentences separated by ~1 s silence, all supposedly by ONE narrator. "
                       "Ignore the words; judge only VOICE IDENTITY (timbre, age, accent). First line exactly: 'SPEAKERS: <number>'. "
                       "Then list any sentence numbers that sound like a different person and why (one line each).")
        m = re.search(r"SPEAKERS:\s*(\d+)", ans)
        n = int(m.group(1)) if m else -1
        ok = n == 1
        ok_all &= ok
        emos = sorted({x["emotion"] for x in pick})
        md += [f"## {names[role]} — `{ED.CAST[role][0]}` — {'ĐẠT' if ok else 'KHÔNG ĐẠT'} ({n} người)", "",
               f"{len(pick)} câu: {', '.join(x['id'] for x in pick)} · cảm xúc có mặt: {', '.join(emos)}", "", ans, ""]
        print(names[role], "->", n, "người", flush=True)
    # G9: xen kẽ 3 vai chính
    trio = [x for k in range(3) for x in (picks["H"][k * 3], picks["D"][k * 3], picks["C"][k * 3])]
    out = OUT / "xen_ke_3_vai.mp3"
    join([ED.w("audio_s") / m["file"] for m in trio], out)
    ans = ask(out, f"9 {lang} readings ~1 s apart. Ignore words; judge VOICE IDENTITY. First line exactly 'SPEAKERS: <number>'. "
                   "Then label each reading S1/S2/S3..., describe each speaker in 5 words, and rate 1-10 how clearly distinct they are.")
    md += ["## G9 — xen kẽ Host · Điều tra viên · Chuyên gia (9 câu, đúng phải là S1 S2 S3 lặp 3 lần)", "", ans, ""]
    md.insert(2, f"**KẾT LUẬN: {'ĐẠT — được chạy build_audio3' if ok_all else 'KHÔNG ĐẠT — xem vai lỗi, chưa dựng'}**\n")
    (OUT / "report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("G10:", "ĐẠT" if ok_all else "KHÔNG ĐẠT", "->", OUT / "report.md")


if __name__ == "__main__":
    main()
