#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC CUỐI bản JA Tap03 — A9.1/A9.2/A9.4 + H9/H10/H13/H14 + A11.

Chạy SAU khi package.py --mux xong.

Cổng:
  G0  input nhất quán: timeline.total == shots.total == mp3 == wav
  G1  H14  picture.mp4 dài == timeline.total (±0,05 s)
  G2  mp4 cuối: đủ 2 stream · 1920x1080@30 · 48 kHz stereo · faststart
  G3  A11 #5  giải mã toàn file: 0 lỗi ffmpeg
  G4  A9.4  thời lượng mp4 cuối == timeline.total (±0,05 s)
  G5  số khung == int(total*30) và == tổng khung các part
  G6  A9.1  âm thanh: LUFS −16±1 · true peak ≤ −1,5 dBFS · 0 khoảng lặng > 0,3 s
  G7  A9.2  phủ câu: timeline.items ↔ shot.sentences (thiếu/thừa/trùng)
  G8  A9.2  SRT: khối hợp lệ, không dòng rỗng, cue cuối ≤ timeline
  G9  A9.2  font JA phủ hết ký tự trên hình (YuGothB / YuGothM)
  G10 không còn ký tự tiếng Việt sót trong chữ trên hình + SRT
  G11 A11 #55 thẻ kết: khung giữa shot cuối có chữ (không đen)
  G12 H10  nền lặp liên tiếp ≤ 4 · số liệu shot · handoff · ⊘
  G13 mô tả YouTube ≤ 5.000 ký tự + link nguồn + thumbnail
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

OUT = ROOT / "02_SAN_XUAT" / "Tap03_JA" / "xuat_ban"
PIC = W / "video3_JA_t03" / "picture.mp4"
WAV = W / "audio_master_JA_t03.wav"
MP4 = OUT / "Tap03_JA_master.mp4"
MP3 = OUT / "Tap03_JA_master.mp3"
SRT = OUT / "Tap03_JA.srt"
THUMB = OUT / "thumbnail.png"
DESC = OUT / "description.txt"
MOTA = OUT / "mo_ta.txt"

tl = json.loads((W / "timeline_s_JA_t03.json").read_text(encoding="utf-8-sig"))
shotsj = json.loads((W / "shots_JA_t03.json").read_text(encoding="utf-8-sig"))
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


def dur(path):
    p = probe(path)
    return float(p.get("format", {}).get("duration", 0) or 0)


def ebur(path):
    r = run([str(FF), "-hide_banner", "-nostats", "-i", str(path),
             "-af", "ebur128=peak=true", "-f", "null", "-"])
    tail = (r.stderr or "")[-1600:]
    i = tail.rfind("Integrated loudness")
    blk = tail[i:] if i >= 0 else tail
    def last(pat):
        m = re.findall(pat, blk)
        return float(m[-1]) if m else None
    return last(r"I:\s*(-?[\d.]+) LUFS"), last(r"LRA:\s*(-?[\d.]+) LU"), last(r"Peak:\s*(-?[\d.]+) dBFS")


def silences(path, thr, dur_s):
    r = run([str(FF), "-hide_banner", "-nostats", "-i", str(path),
             "-af", f"silencedetect=n={thr}dB:d={dur_s}", "-f", "null", "-"])
    st = re.findall(r"silence_start: ([\d.]+)", r.stderr or "")
    en = re.findall(r"silence_end: ([\d.]+)", r.stderr or "")
    return [(float(a), float(b)) for a, b in zip(st, en)], st


print("=" * 78)
print(f"QC CUOI — JA TAP03   timeline.total = {TOTAL:.2f} s")
print("=" * 78)

# ---------------- G0 input nhất quán
print("\n-- G0 input nhất quán --")
chk("G0", "shots.total == timeline.total", abs(float(shotsj.get("total", -1)) - TOTAL) <= 0.05,
    f"shots={shotsj.get('total')} timeline={TOTAL}")
if MP3.exists():
    d3 = dur(MP3)
    chk("G0", "master mp3 == timeline.total (±0,05s)", abs(d3 - TOTAL) <= 0.05, f"mp3={d3:.3f}")
else:
    chk("G0", "master mp3 tồn tại", False, str(MP3))
if WAV.exists():
    dw = dur(WAV)
    chk("G0", "wav master == timeline.total (±0,05s)", abs(dw - TOTAL) <= 0.05, f"wav={dw:.3f}")
else:
    chk("G0", "wav master tồn tại", False, str(WAV))

# ---------------- G1 H14 picture
print("\n-- G1 H14 picture.mp4 --")
if PIC.exists():
    dp = dur(PIC)
    chk("G1", "picture.mp4 == timeline.total (±0,05s)", abs(dp - TOTAL) <= 0.05,
        f"picture={dp:.3f} timeline={TOTAL:.3f} lech={abs(dp-TOTAL):.3f}")
else:
    chk("G1", "picture.mp4 tồn tại", False, str(PIC))

# ---------------- G2/G3/G4/G5 mp4 cuối
print("\n-- G2..G5 file cuối --")
if not MP4.exists():
    chk("G2", "mp4 cuối tồn tại", False, str(MP4))
else:
    p = probe(MP4)
    fmt = p.get("format", {})
    st = p.get("streams", [])
    vs = [s for s in st if s.get("codec_type") == "video"]
    as_ = [s for s in st if s.get("codec_type") == "audio"]
    chk("G2", "đủ 1 video + 1 audio", len(vs) == 1 and len(as_) == 1, f"v={len(vs)} a={len(as_)}")
    if vs:
        chk("G2", "video 1920x1080 @30fps h264", vs[0].get("width") == 1920 and vs[0].get("height") == 1080
            and vs[0].get("r_frame_rate") == "30/1" and vs[0].get("codec_name") == "h264",
            f"{vs[0].get('codec_name')} {vs[0].get('width')}x{vs[0].get('height')} @{vs[0].get('r_frame_rate')}")
    if as_:
        chk("G2", "audio 48kHz stereo aac", as_[0].get("sample_rate") == "48000"
            and as_[0].get("channels") == 2 and as_[0].get("codec_name") == "aac",
            f"{as_[0].get('codec_name')} {as_[0].get('sample_rate')}Hz {as_[0].get('channels')}ch")
    sz = int(fmt.get("size", 0))
    chk("G2", "dung lượng > 100 MB", sz > 100_000_000, f"{sz/1e6:.1f} MB")
    # faststart: moov trước mdat
    with open(MP4, "rb") as fh:
        head = fh.read(4_000_000)
    i_moov = head.find(b"moov")
    i_mdat = head.find(b"mdat")
    chk("G2", "faststart (moov trước mdat)", i_moov != -1 and (i_mdat == -1 or i_moov < i_mdat),
        f"moov@{i_moov} mdat@{i_mdat}")
    # G4 thời lượng
    df = float(fmt.get("duration", 0))
    chk("G4", "mp4 cuối == timeline.total (±0,05s)", abs(df - TOTAL) <= 0.05,
        f"mp4={df:.3f} timeline={TOTAL:.3f} lech={abs(df-TOTAL):.3f}")
    # G5 số khung (renderer cắt chân: int(total*30))
    nfr = int(vs[0].get("nb_frames") or 0) if vs else 0
    if not nfr:
        r = run([str(FP), "-v", "error", "-count_frames", "-select_streams", "v:0",
                 "-show_entries", "stream=nb_read_frames", "-of", "default=nw=1:nk=1", str(MP4)])
        try:
            nfr = int((r.stdout or "0").strip().splitlines()[0])
        except Exception:
            nfr = 0
    exp = int(TOTAL * 30)
    chk("G5", "số khung == int(total*30)", nfr == exp, f"thuc={nfr} mong doi={exp}")
    # G3 decode
    r = run([str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"])
    errs = [l for l in (r.stderr or "").splitlines() if l.strip()]
    chk("G3", "giải mã toàn file: 0 lỗi", len(errs) == 0, f"{len(errs)} dòng lỗi")
    for l in errs[:4]:
        print("        ", l[:150])

# ---------------- G6 âm thanh
print("\n-- G6 A9.1 âm thanh --")
if MP4.exists():
    L, LRA, PK = ebur(MP4)
    chk("G6", "LUFS mp4 trong −16±1", L is not None and -17.0 <= L <= -15.0, f"LUFS={L}")
    chk("G6", "true peak mp4 ≤ −1,5 dBFS (A7)", PK is not None and PK <= -1.5, f"peak={PK} dBFS")
    print(f"         LRA = {LRA} LU")
    segs, starts = silences(MP4, "-60dB", 0.3)
    chk("G6", "0 khoảng lặng > 0,3 s @ −60 dB", len(segs) == 0, f"{len(segs)} {starts[:6]}")
    segs2, starts2 = silences(MP4, "-35dB", 2.5)
    chk("G6", "0 khoảng lặng ≥ 2,5 s @ −35 dB", len(segs2) == 0, f"{len(segs2)} {starts2[:6]}")
    # lời đầu tiên
    first = min((it["start"] for it in tl["items"]), default=None)
    if first is not None:
        chk("G6", "lời đầu tiên > 20,5 s (sau intro)", first > 20.5, f"lời đầu={first:.2f}s")

# ---------------- G7 phủ câu
print("\n-- G7 A9.2 phủ câu --")
sent = {it["id"]: it for it in tl["items"]}
allids = [it["id"] for it in tl["items"]]
cov = []
for s in shots:
    cov += s["sentences"]
miss = [i for i in allids if i not in cov]
extra = [c for c in cov if c not in allids]
dup = sorted({c for c in cov if cov.count(c) > 1})
chk("G7", "phủ câu 218/218, 0 thiếu/thừa/trùng",
    len(cov) == len(allids) and not miss and not extra and not dup,
    f"phu={len(cov)}/{len(allids)} thieu={len(miss)} thua={len(extra)} trung={len(dup)}")
# thứ tự
order_ok = True
flat = [c for s in shots for c in s["sentences"]]
if flat != [i for i in allids if i in set(flat)]:
    order_ok = False
chk("G7", "thứ tự câu khớp timeline", order_ok, "")

# ---------------- G8 SRT
print("\n-- G8 A9.2 phụ đề --")
if SRT.exists():
    raw = SRT.read_bytes()
    txt = raw.decode("utf-8-sig", errors="replace").replace("\r\n", "\n")
    blocks = [b for b in txt.strip().split("\n\n") if b.strip()]

    def sec(ts):
        h, m, s = ts.split(":")
        s, ms = s.split(",")
        return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

    bad = [i for i, b in enumerate(blocks, 1) if len(b.splitlines()) < 3 or "-->" not in b.splitlines()[1]]
    blank = [i for i, b in enumerate(blocks, 1) if any(x.strip() == "" for x in b.splitlines()[2:])]
    ends = [sec(b.splitlines()[1].split(" --> ")[1]) for b in blocks if len(b.splitlines()) >= 3 and "-->" in b.splitlines()[1]]
    last = max(ends) if ends else 0
    chk("G8", "SRT khối hợp lệ, không dòng rỗng", not bad and not blank,
        f"{len(blocks)} cue · khoi loi={len(bad)} · dong rong={len(blank)}")
    chk("G8", "cue cuối ≤ timeline.total", last <= TOTAL + 0.05, f"het {last:.2f}s")
    # cue chồng nhau
    starts = [sec(b.splitlines()[1].split(" --> ")[0]) for b in blocks if len(b.splitlines()) >= 3 and "-->" in b.splitlines()[1]]
    ov = sum(1 for i in range(1, len(starts)) if starts[i] < starts[i - 1])
    chk("G8", "0 cue chồng nhau", ov == 0, f"{ov} chồng")
else:
    chk("G8", "SRT tồn tại", False, str(SRT))

# ---------------- G9 font coverage
print("\n-- G9 A9.2 font JA --")
try:
    from PIL import Image, ImageDraw, ImageFont
    FONTS = Path(r"C:\Windows\Fonts")
    allchars = set()
    for s in shots:
        for seg in s["segments"]:
            for k, v in seg["elems"]:
                allchars |= set(v)
    allchars |= set("AMBER EYES 実際の事件記録から読み解く犯罪心理学 ホスト 捜査官 心理学者 証人 一般人 関係者 住民")

    def rmask(f, ch):
        im = Image.new("L", (f.size * 2 + 20, f.size * 2 + 20), 0)
        ImageDraw.Draw(im).text((10, 10), ch, font=f, fill=255)
        return im.tobytes()

    for fname in ["YuGothB.ttc", "YuGothM.ttc"]:
        f = ImageFont.truetype(str(FONTS / fname), 40)
        ref = rmask(f, "\uffff")
        miss_f = sorted({c for c in allchars if c not in " \n\t" and rmask(f, c) == ref})
        chk("G9", f"font {fname} phủ hết ký tự", not miss_f,
            f"{len(miss_f)} thiếu {miss_f[:8]}")
except Exception as e:
    chk("G9", "kiểm tra font", False, f"{type(e).__name__}: {e}")

# ---------------- G10 ký tự tiếng Việt sót
print("\n-- G10 ký tự tiếng Việt sót --")
VN_CH = set("ăâđêôơưĂÂĐÊÔƠƯ"
            "ắằẳẵặẤẦẨẪẬẮẰẲẴẶẾỀỂỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪỬỮỰỲỴỶỸ"
            "íìíòíóìíùìíý")
vn_hits = {}
for s in shots:
    for seg in s["segments"]:
        for k, v in seg["elems"]:
            bad = sorted(set(v) & VN_CH)
            if bad:
                vn_hits.setdefault(s["id"], []).append((k, "".join(bad)))
if SRT.exists():
    t2 = SRT.read_text(encoding="utf-8-sig", errors="replace")
    sb = sorted(set(t2) & VN_CH)
    if sb:
        vn_hits.setdefault("__SRT__", []).append(("", "".join(sb)))
chk("G10", "0 ký tự tiếng Việt trong chữ trên hình + SRT", not vn_hits,
    f"{len(vn_hits)} nơi {list(vn_hits)[:5]}")

# ---------------- G11 thẻ kết
print("\n-- G11 A11 #55 thẻ kết --")
if MP4.exists():
    from PIL import Image
    import io
    lastshot = shots[-1]
    tshot = lastshot["start"] + 2.0
    fr = subprocess.run([str(FF), "-v", "error", "-ss", f"{tshot:.3f}", "-i", str(MP4),
                         "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                        capture_output=True).stdout
    if fr:
        im = Image.open(io.BytesIO(fr)).convert("L")
        import numpy as np
        arr = np.asarray(im, dtype=np.float64)
        bright = float((arr > 140).mean())
        out = W / "_qc_sheets_ja_t03" / "endcard_ja_t03.png"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(fr)
        chk("G11", "thẻ kết có chữ (không đen)", bright > 0.005,
            f"t={tshot:.1f}s pixel sang>140 = {bright*100:.2f}%  -> {out.name}")
    else:
        chk("G11", "trích khung thẻ kết", False, "không lấy được frame")
    # khung cuối file
    fr2 = subprocess.run([str(FF), "-v", "error", "-sseof", "-3", "-i", str(MP4),
                          "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                         capture_output=True).stdout
    if fr2:
        im2 = Image.open(io.BytesIO(fr2)).convert("L")
        import numpy as np
        a2 = np.asarray(im2, dtype=np.float64)
        b2 = float((a2 > 140).mean())
        print(f"         khung cuoi file (-3s): pixel sang>140 = {b2*100:.2f}% (mo dan sang den la binh thuong)")

# ---------------- G12 H10 số liệu shot
print("\n-- G12 H10 số liệu shot --")
durs = [(s["id"], float(s["end"]) - float(s["start"])) for s in shots]
durs_sorted = sorted(durs, key=lambda x: -x[1])
n_long = sum(1 for _, d in durs if d > 15)
n_short = sum(1 for _, d in durs if d < 3)
print(f"         TB {sum(d for _, d in durs)/len(durs):.1f}s · dài nhất {durs_sorted[0][0]} "
      f"{durs_sorted[0][1]:.1f}s · ngắn nhất {durs_sorted[-1][0]} {durs_sorted[-1][1]:.1f}s")
print(f"         >15s: {n_long}/{len(shots)} · <3s: {n_short}/{len(shots)}")
# nền lặp liên tiếp
mx = 1
cur = 1
for a, b in zip(shots, shots[1:]):
    if a["bg"] == b["bg"] and a.get("bg2") == b.get("bg2"):
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 1
chk("G12", "nền lặp liên tiếp ≤ 4 shot", mx <= 4, f"max={mx}")
n_handoff = sum(1 for s in shots if s.get("flags", {}).get("handoff"))
n_nobust = sum(1 for s in shots if s.get("flags", {}).get("nobust"))
n_bust = sum(1 for s in shots if s.get("flags", {}).get("bust"))
n_guests = sum(1 for s in shots if s.get("flags", {}).get("guests"))
print(f"         handoff={n_handoff} · ⊘(nobust)={n_nobust} · bust={n_bust} · guests={n_guests}")
chk("G12", "shot cuối là thẻ kết (5-21) không gắn câu",
    shots[-1]["id"] == "5-21" and not shots[-1]["sentences"], f"{shots[-1]['id']}")

# ---------------- G13 mô tả + thumbnail
print("\n-- G13 mô tả + thumbnail --")
if MOTA.exists():
    d = MOTA.read_text(encoding="utf-8", errors="replace")
    n_links = len(re.findall(r"https?://\S+", d))
    chk("G13", "mô tả ≤ 5.000 ký tự (T15)", len(d) <= 5000, f"{len(d)} ký tự · {n_links} link")
    chk("G13", "không còn [PENDING", "[PENDING" not in d, "")
    if DESC.exists():
        d2 = DESC.read_text(encoding="utf-8", errors="replace")
        chk("G13", "description.txt == mo_ta.txt", d2.strip() == d.strip(),
            f"{len(d2)} vs {len(d)}")
else:
    chk("G13", "mo_ta.txt tồn tại", False, str(MOTA))
if THUMB.exists():
    from PIL import Image
    ti = Image.open(THUMB)
    chk("G13", "thumbnail 1280x720", ti.size == (1280, 720), f"{ti.size}")
else:
    chk("G13", "thumbnail tồn tại", False, str(THUMB))

# ---------------- tổng kết
print("\n" + "=" * 78)
npass = sum(1 for _, _, ok, _ in res if ok)
nfail = [r for r in res if not r[2]]
print(f"KET QUA: {npass}/{len(res)} cong dat · {len(nfail)} loi")
for g, n, ok, d in nfail:
    print(f"  FAIL [{g}] {n}  {d}")
print("=" * 78)
sys.exit(0 if not nfail else 1)
