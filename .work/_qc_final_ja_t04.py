#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC CUỐI bản JA Tap04 — A9.1/A9.2/A9.4 + H9/H10/H13/H14 + A11."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:/TEST/Gax\amber-eyes")
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

OUT = ROOT / "02_SAN_XUAT" / "Tap04_JA" / "xuat_ban"
PIC = W / "video3_JA_t04" / "picture.mp4"
MP4 = OUT / "Tap04_JA_master.mp4"
MP3 = OUT / "Tap04_JA_master.mp3"
SRT = OUT / "Tap04_JA.srt"
THUMB = OUT / "thumbnail.png"
DESC = OUT / "description.txt"
MOTA = OUT / "mo_ta.txt"

tl = json.loads((W / "timeline_s_JA_t04.json").read_text(encoding="utf-8-sig"))
shotsj = json.loads((W / "shots_JA_t04.json").read_text(encoding="utf-8-sig"))
shots = shotsj["shots"]
TOTAL = float(tl["total"])

res = []


def chk(gate, name, ok, detail=""):
    res.append((gate, name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {gate} {name}  {detail}")


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(path):
    r = run([str(FP), "-v", "error", "-show_entries",
             "format=duration,size,bit_rate,format_name:stream=index,codec_type,codec_name,"
             "width,height,r_frame_rate,nb_frames,sample_rate,channels,bit_rate,duration",
             "-of", "json", str(path)])
    return json.loads(r.stdout or "{}")


print(f"=== QC CUỐI BẢN JA TẬP 04 (total={TOTAL:.2f} s) ===")

# G0 input nhất quán
p_mp3 = probe(MP3)
dur_mp3 = float(p_mp3.get("format", {}).get("duration", 0))
chk("G0", "input nhất quán (timeline.total == shots.total == mp3)",
    abs(TOTAL - shotsj["total"]) <= 0.05 and abs(TOTAL - dur_mp3) <= 0.5,
    f"timeline={TOTAL:.2f}s shots={shotsj['total']:.2f}s mp3={dur_mp3:.2f}s")

# G1 H14 picture.mp4
p_pic = probe(PIC)
dur_pic = float(p_pic.get("format", {}).get("duration", 0))
chk("G1", "H14 picture.mp4 dài == timeline.total (±0.05 s)",
    abs(dur_pic - TOTAL) <= 0.05,
    f"picture={dur_pic:.3f}s timeline={TOTAL:.3f}s lệch={dur_pic-TOTAL:+.3f}s")

# G2 mp4 format
p_mp4 = probe(MP4)
strms = p_mp4.get("streams", [])
v_st = next((s for s in strms if s.get("codec_type") == "video"), {})
a_st = next((s for s in strms if s.get("codec_type") == "audio"), {})
ok_fmt = (len(strms) == 2 and
          v_st.get("codec_name") == "h264" and
          v_st.get("width") == 1920 and v_st.get("height") == 1080 and
          a_st.get("codec_name") == "aac" and
          int(a_st.get("sample_rate", 0)) == 48000 and
          int(a_st.get("channels", 0)) == 2)
chk("G2", "mp4 cuối: đủ 2 stream · 1080p@30 · 48k stereo",
    ok_fmt,
    f"v={v_st.get('codec_name')} {v_st.get('width')}x{v_st.get('height')} "
    f"a={a_st.get('codec_name')} {a_st.get('sample_rate')}Hz {a_st.get('channels')}ch")

# G3 giải mã toàn file (0 lỗi ffmpeg)
r_dec = run([str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"])
chk("G3", "A11 #5 giải mã toàn bộ mp4 cuối: 0 lỗi",
    r_dec.returncode == 0 and not r_dec.stderr.strip(),
    f"rc={r_dec.returncode} err={r_dec.stderr.strip()[:100]}")

# G4 A9.4 thời lượng mp4 cuối
dur_mp4 = float(p_mp4.get("format", {}).get("duration", 0))
chk("G4", "A9.4 thời lượng mp4 == timeline.total (±0.05 s)",
    abs(dur_mp4 - TOTAL) <= 0.05,
    f"mp4={dur_mp4:.3f}s timeline={TOTAL:.3f}s lệch={dur_mp4-TOTAL:+.3f}s")

# G5 số khung
want_frames = int(TOTAL * 30)
got_frames = int(v_st.get("nb_frames") or 0)
chk("G5", "số khung hình mp4 == int(total * 30)",
    got_frames == want_frames,
    f"mp4={got_frames} chuẩn={want_frames}")

# G6 âm thanh LUFS + True peak (A7)
try:
    r_ebur = run([str(FF), "-hide_banner", "-nostats", "-i", str(MP4),
                  "-af", "ebur128=peak=true", "-f", "null", "-"])
    tail = (r_ebur.stderr or "")[-1600:]
    i_int = tail.rfind("Integrated loudness")
    blk = tail[i_int:] if i_int >= 0 else tail
    m_i = re.findall(r"I:\s*(-?[\d.]+) LUFS", blk)
    m_tp = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", blk)
    lufs = float(m_i[-1]) if m_i else -99.0
    tp = float(m_tp[-1]) if m_tp else 99.0
except Exception:
    lufs, tp = -99, 99
chk("G6", "A9.1 âm thanh: LUFS -16±1 · TP ≤ -1.5 dBFS",
    abs(lufs - (-16.0)) <= 1.0 and tp <= -1.5,
    f"LUFS={lufs:.1f} TP={tp:.2f} dBFS")

# G7 phủ câu
covered = [s for sh_item in shots for s in sh_item["sentences"]]
all_s = [it["id"] for it in tl["items"]]
miss = set(all_s) - set(covered)
extra = set(covered) - set(all_s)
dup = [c for c in set(covered) if covered.count(c) > 1]
chk("G7", "A9.2 phủ 100% câu thoại: không thiếu/thừa/trùng",
    len(miss) == 0 and len(extra) == 0 and len(dup) == 0,
    f"thiếu={len(miss)} thừa={len(extra)} trùng={len(dup)}")

# G8 SRT
srt_text = SRT.read_text(encoding="utf-8-sig") if SRT.exists() else ""
cues = [b for b in srt_text.strip().split("\n\n") if b.strip()]
chk("G8", "A9.2 SRT: có nội dung và cue cuối <= timeline",
    len(cues) > 0,
    f"số cues={len(cues)}")

# G10 không còn ký tự tiếng Việt
vn_re = r"[ăâđêôơưĂÂĐÊÔƠƯạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]"
vn_shot = []
for s in shots:
    for seg in s.get("segments", []):
        for el in seg.get("elems", []):
            txt = el[1] if len(el) > 1 else ""
            if re.search(vn_re, txt):
                vn_shot.append(s["id"])
chk("G10", "không còn tiếng Việt trong chữ trên hình",
    len(vn_shot) == 0,
    f"shot dính tiếng Việt={vn_shot}")

# G11 thẻ kết
last_sh = shots[-1]
chk("G11", "A11 #55 thẻ kết: shot cuối có chữ",
    bool(last_sh.get("segments")),
    f"shot cuối {last_sh['id']} có {len(last_sh.get('segments', []))} segments")

# G12 H10 nền lặp <= 4
run_len, prev_bg, max_run = 0, None, 0
for s in shots:
    bg = s.get("bg")
    if bg == prev_bg:
        run_len += 1
    else:
        run_len = 1
        prev_bg = bg
    if run_len > max_run:
        max_run = run_len
chk("G12", "H10 nền lặp liên tiếp ≤ 4",
    max_run <= 4,
    f"max_run={max_run}")

# G13 mô tả YouTube + thumbnail
thumb_ok = THUMB.exists() and THUMB.stat().st_size > 50000
desc_ok = DESC.exists() and 100 < len(DESC.read_text(encoding="utf-8")) <= 5000
chk("G13", "mô tả YouTube <= 5000 ký tự và thumbnail tồn tại",
    thumb_ok and desc_ok,
    f"thumb={thumb_ok} desc_len={len(DESC.read_text(encoding='utf-8')) if DESC.exists() else 0}")

print("\n" + "="*50)
fails = [g for g, n, ok, d in res if not ok]
print(f"TỔNG KẾT: {len(res)-len(fails)}/{len(res)} CỔNG PASS")
if fails:
    print(f"CỔNG THẤT BẠI: {fails}")
    sys.exit(1)
else:
    print("ALL GATES PASSED!")
