#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC cuoi T03 — A9.1 (am thanh) + A9.3 (hinh) + A9.4 (file cuoi) + kiem tra them.

Chay sau khi package.py --mux xong:
    $env:AE_EP='03'; py -3 .work/_qc_final_t03.py

Kiem tra dac biet cua T03:
  - picture.mp4 khop timeline.total (±0,05 s)                    [H14]
  - LUFS/peak tren CHINH file mp4 cuoi (AAC lam doi true peak)    [A11 #38]
  - the ket o GIUA shot cuoi, khong phai khung cuoi (mo den 3 s)  [A11 #65]
  - KHUNG TRONG MP4 khop anh tinh da duyet (pixel) -> anh khop loi  [H3/H13]
  - dong bo hinh-tieng: shot bat dau dung luc cau dau tien        [H14]
  - phu de khong chong lap, phu de cuoi dung cau cuoi
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
os.environ.setdefault("AE_EP", "03")
import edition as ED  # noqa: E402

FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = FF.with_name("ffprobe.exe")
OUT = ED.OUT_DIR
MP4 = OUT / (ED.MASTER + ".mp4")
WAV = ED.w("audio_master.wav")
PIC = ED.w("video3") / "picture.mp4"
STILLS = ED.w("video3") / "stills"
QC = ED.w("qc_final")
THUMB = OUT / "thumbnail.png"
FPS = 30
TOL = 0.05

ok = True


def chk(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK  ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))


def run(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout, r.stderr, r.returncode


def dur(p):
    out, _, _ = run([str(FP), "-v", "error", "-show_entries", "format=duration",
                     "-of", "default=noprint_wrappers=1:nokey=1", str(p)])
    return float(out.strip())


tl = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8-sig"))
shots = json.loads(ED.w("shots.json").read_text(encoding="utf-8-sig"))["shots"]

print("=" * 74)
print("QC CUOI TAP 03 — file:", MP4)
print("=" * 74)

# ---------------------------------------------------------------- A9.4 file cuoi
print("\n=== A9.4 file cuoi ===")
for p, lbl in ((MP4, "mp4 cuoi"), (WAV, "wav"), (PIC, "picture")):
    if not p.exists():
        chk(f"{lbl} ton tai", False, str(p))
        print("\nCO VIEC CHUA XONG")
        sys.exit(1)

d_mp4, d_wav, d_pic = dur(MP4), dur(WAV), dur(PIC)
print(f"   mp4 cuoi = {d_mp4:.3f} s ({int(d_mp4 // 60)}:{d_mp4 % 60:05.2f})")
print(f"   wav      = {d_wav:.3f} s")
print(f"   picture  = {d_pic:.3f} s")
print(f"   timeline = {tl['total']:.3f} s")
chk("Hinh va tieng cung thoi luong (±0,05 s)", abs(d_mp4 - d_wav) <= TOL, f"lech {abs(d_mp4 - d_wav):.3f} s")
chk("H14: picture khop timeline.total (±0,05 s)", abs(d_pic - tl["total"]) <= TOL, f"lech {abs(d_pic - tl['total']):.3f} s")
chk("H14: mp4 cuoi khop timeline.total (±0,05 s)", abs(d_mp4 - tl["total"]) <= TOL, f"lech {abs(d_mp4 - tl['total']):.3f} s")

out, _, _ = run([str(FP), "-v", "error", "-select_streams", "v:0", "-show_entries",
                 "stream=width,height,r_frame_rate,nb_frames,codec_name,pix_fmt", "-of", "default=noprint_wrappers=1", str(MP4)])
print("   video: " + out.replace("\n", " "))
chk("Video 1920x1080 @ 30 fps", "width=1920" in out and "height=1080" in out and "r_frame_rate=30/1" in out)
chk("Video H.264 + yuv420p", "codec_name=h264" in out and "pix_fmt=yuv420p" in out)
m = re.search(r"nb_frames=(\d+)", out)
frames = int(m.group(1)) if m else -1
chk("So khung video = so giay x 30", frames == round(d_mp4 * 30), f"{frames} khung")
exp_frames = int(round(tl["total"] * FPS))
chk("So khung video = timeline.total x 30", abs(frames - exp_frames) <= 2, f"{frames} vs {exp_frames}")

out, _, _ = run([str(FP), "-v", "error", "-select_streams", "a:0", "-show_entries",
                 "stream=codec_name,sample_rate,channels,bit_rate,duration", "-of", "default=noprint_wrappers=1", str(MP4)])
print("   audio: " + out.replace("\n", " "))
chk("Audio AAC 48 kHz stereo", "codec_name=aac" in out and "sample_rate=48000" in out and "channels=2" in out)

print("   giai ma toan bo mp4 ...")
_, err, rc = run([str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"])
chk("Giai ma khong loi", rc == 0 and not err.strip(), err.strip()[:300])

# ---------------------------------------------------------------- A9.1 am thanh
print("\n=== A9.1 am thanh ===")
for lbl, path in (("wav", WAV), ("mp4 cuoi", MP4)):
    _, err, _ = run([str(FF), "-i", str(path), "-af", "silencedetect=n=-60dB:d=0.3", "-f", "null", "-"])
    sil = re.findall(r"silence_start:\s*([\d.]+)", err)
    chk(f"V4 [{lbl}]: khong co khoang cam > 0,3 s", not sil, f"{len(sil)} doan: {sil[:5]}")

for lbl, path in (("wav", WAV), ("mp4 cuoi", MP4)):
    _, err, _ = run([str(FF), "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"])
    lufs_m = re.findall(r"I:\s*(-?[\d.]+)\s*LUFS", err)
    lufs = float(lufs_m[-1]) if lufs_m else None
    pk = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", err)
    print(f"   [{lbl}] I: {lufs} LUFS · Peak: {pk[-1] if pk else '?'} dBFS")
    chk(f"Do lon [{lbl}] trong khoang -16 ± 1 LUFS", lufs is not None and -17 <= lufs <= -15, f"{lufs} LUFS")
    chk(f"Dinh ghe [{lbl}] doc duoc", bool(pk), "khong tim thay Peak")
    if pk:
        chk(f"Dinh ghe [{lbl}] <= -1,5 dBFS (A11 #38)", float(pk[-1]) <= -1.5, f"{pk[-1]} dBFS")

first = tl["items"][0]["start"]
last = tl["items"][-1]["end"]
chk("Loi dau tien trong khoang 22,8 – 23,5 s", 22.8 <= first <= 23.5, f"{first} s")
print(f"   Loi cuoi cung het tai {last} s · video {d_mp4:.2f} s · phu du {d_mp4 - last:.2f} s")

# ---------------------------------------------------------------- A9.3 hinh
print("\n=== A9.3 hinh: kiem tra pixel trong mp4 cuoi ===")
from PIL import Image  # noqa: E402
import numpy as np  # noqa: E402

stills_out = ED.w("video3") / "stills_final"
stills_out.mkdir(parents=True, exist_ok=True)
QC.mkdir(parents=True, exist_ok=True)

# lay 1 khung giua moi shot TU CHINH mp4 cuoi
for s in shots:
    mid = (s["start"] + s["end"]) / 2
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{mid:.3f}", "-i", str(MP4),
                    "-frames:v", "1", str(stills_out / f"{s['id']}.png")], check=True)
n_got = len(list(stills_out.glob("*.png")))
chk(f"Lay du {len(shots)} khung giua shot tu mp4 cuoi", n_got == len(shots), f"{n_got}/{len(shots)}")

# so pixel: khung trong video vs anh tinh da duyet (cung bo render)
mads, worst, missing = [], [], []
for s in shots:
    ref_p = STILLS / f"shot_{s['id']}.png"
    got_p = stills_out / f"{s['id']}.png"
    if not ref_p.exists():
        missing.append(s["id"])
        continue
    a = np.asarray(Image.open(got_p).convert("RGB"), dtype=np.int16)
    b = np.asarray(Image.open(ref_p).convert("RGB"), dtype=np.int16)
    if a.shape != b.shape:
        worst.append((s["id"], 999.0))
        continue
    mad = float(np.abs(a - b).mean())
    mads.append((s["id"], mad))
    if mad > 12.0:
        worst.append((s["id"], mad))

chk("Anh tinh tham chieu ton tai cho moi shot", not missing, str(missing[:8]))
if mads:
    vals = [m for _, m in mads]
    vmax = max(vals)
    vmean = sum(vals) / len(vals)
    print(f"   Sai lech pixel (video vs anh tinh da duyet): TB {vmean:.2f} · MAX {vmax:.2f} · n={len(vals)}")
    chk("Khung trong video khop anh tinh da duyet (MAD < 12)", not worst, str(worst[:8]))

    # doi chieu: cung khung video, so voi anh tinh cua shot KE (phai lech lon hon nhieu)
    ctrl = []
    for i in range(min(20, len(shots) - 1)):
        s = shots[i]
        nx = shots[i + 1]
        gp = stills_out / f"{s['id']}.png"
        rp = STILLS / f"shot_{nx['id']}.png"
        if not gp.exists() or not rp.exists():
            continue
        a = np.asarray(Image.open(gp).convert("RGB"), dtype=np.int16)
        b = np.asarray(Image.open(rp).convert("RGB"), dtype=np.int16)
        if a.shape != b.shape:
            continue
        wrong = float(np.abs(a - b).mean())
        own = dict(mads).get(s["id"], 0.0)
        ctrl.append((s["id"], own, wrong))
    if ctrl:
        print(f"   DOI CHIEU (anh tinh shot N+1): sai lech TB {sum(c[2] for c in ctrl) / len(ctrl):.2f} · "
              f"MIN {min(c[2] for c in ctrl):.2f} · dung TB {sum(c[1] for c in ctrl) / len(ctrl):.2f}")
        bad_ctrl = [c[0] for c in ctrl if c[1] >= c[2]]
        chk("Khung video dung shot (sai lech voi anh tinh SAI luon lon hon)", not bad_ctrl,
            f"{len(bad_ctrl)}/20: {bad_ctrl[:8]}")

# contact sheet tu mp4
from PIL import ImageDraw, ImageFont  # noqa: E402
COLS, ROWS, TW, TH, PER = 4, 4, 480, 270, 16
try:
    fl = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 22)
except OSError:
    fl = ImageFont.load_default()
sheets = (len(shots) + PER - 1) // PER
for k in range(sheets):
    chunk = shots[k * PER:(k + 1) * PER]
    sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + 30)), (14, 14, 17))
    d = ImageDraw.Draw(sheet)
    for i, s in enumerate(chunk):
        p = stills_out / f"{s['id']}.png"
        if not p.exists():
            continue
        im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
        x, y = (i % COLS) * TW, (i // COLS) * (TH + 30)
        sheet.paste(im, (x, y))
        mid = (s["start"] + s["end"]) / 2
        d.text((x + 8, y + TH + 4), f"{s['id']} · {int(mid // 60)}:{mid % 60:05.2f} · {s['template']}",
               font=fl, fill=(242, 239, 233))
    sheet.save(QC / f"sheet_{k + 1:02d}.png")
print(f"   {sheets} contact sheet -> {QC}")

# ---------------------------------------------------------------- the ket (A11 #65)
print("\n=== the ket ===")
last_shot = shots[-1]
mid_last = (last_shot["start"] + last_shot["end"]) / 2
kf = QC / "endcard_mid.png"
subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{mid_last:.3f}", "-i", str(MP4),
                "-frames:v", "1", str(kf)], check=True)
a = np.array(Image.open(kf).convert("RGB"))
chk("The ket: khung giua shot cuoi khong den (khong phai khung cuoi)", float(a.mean()) > 8,
    f"do sang trung binh {a.mean():.1f} tai {mid_last:.2f}s")
kfin = QC / "endcard_last.png"
subprocess.run([str(FF), "-y", "-v", "error", "-sseof", "-1.0", "-i", str(MP4),
                "-frames:v", "1", str(kfin)], check=True)
af = np.array(Image.open(kfin).convert("RGB"))
print(f"   khung cuoi (mo den 3 s cuoi): do sang trung binh {af.mean():.1f}")
chk("Khung cuoi toi hon khung giua shot cuoi", float(af.mean()) < float(a.mean()),
    f"{af.mean():.1f} < {a.mean():.1f}")
print(f"   shot cuoi: {last_shot['id']} {last_shot['start']:.2f}-{last_shot['end']:.2f}s  bg={last_shot['bg']}")

# ---------------------------------------------------------------- dong bo hinh-tieng
print("\n=== dong bo hinh-tieng ===")
SENT = {i["id"]: i for i in tl["items"]}
# (a) Shot KHONG được bat dau sau cau dau (thi loi thoai dau tien bi bo qua)
late, lead = [], []
for s in shots:
    if not s["sentences"]:
        continue
    d = s["start"] - SENT[s["sentences"][0]]["start"]
    (late if d > 0.001 else lead).append((s["id"], round(d, 3)))
chk("Khong shot nao bat dau SAU cau dau (khong bo loi thoai dau)", not late, f"{late[:6]}")
print(f"   Shot vao canh truoc cau dau: {len(lead)} · bien do {min(d for _, d in lead):.3f} .. {max(d for _, d in lead):.3f} s")

# (b) Shot lien khít — khong lo trong giua hai shot (khong co loi hinh den)
gaps = [(a["id"], a["end"], b["id"], round(b["start"] - a["end"], 3))
        for a, b in zip(shots, shots[1:]) if b["start"] - a["end"] > 0.001]
chk("Cac shot lien khit, khong lo trong giua (khong co loi hinh den)", not gaps, f"{gaps[:5]}")

# (c) Shot cuoi phai ket <= bat dau cau sau (khong tre hinh qua loi sau)
nxt = {}
for i, s in enumerate(shots):
    nxt[s["id"]] = shots[i + 1] if i + 1 < len(shots) else None
overlap = []
for s in shots:
    if not s["sentences"]:
        continue
    n = nxt[s["id"]]
    if n and n["sentences"]:
        first_next = SENT[n["sentences"][0]]["start"]
        if n["start"] > first_next + 0.001:
            overlap.append((s["id"], n["id"]))
chk("Shot sau khong bat dau sau khi cau sau da noi", not overlap, f"{overlap[:5]}")

# (d) Shot giu hinh bao lau sau cau cuoi (cho phep, nhung phai <= 1,5 s)
tails = []
for s in shots:
    if not s["sentences"]:
        continue
    tails.append((s["id"], round(s["end"] - SENT[s["sentences"][-1]]["end"], 3)))
big_tail = [t for t in tails if t[1] > 1.5]
chk("Shot giu hinh sau loi cuoi <= 1,5 s", not big_tail, f"{big_tail[:6]}")
print(f"   Shot giu hinh sau loi cuoi: TB {sum(t[1] for t in tails) / len(tails):.2f} · MAX {max(t[1] for t in tails):.2f} s")

# so cau: 218 cau trong timeline, phu het bang bao shot
covered = set()
for s in shots:
    covered.update(s["sentences"])
missing_s = [i["id"] for i in tl["items"] if i["id"] not in covered]
chk("Moi cau thoai deu xuat hien tren hinh", not missing_s, f"{len(missing_s)} thieu: {missing_s[:6]}")
order = [sid for s in shots for sid in s["sentences"]]
chk("Thu tu cau trong hinh dung thu tu kich ban", order == [i["id"] for i in tl["items"]])

# chay lai QC bang shot chinh thuc cua du an (bang kiem tra bang liet ke)
print("\n=== QC bang shot chinh thuc du an (qc_shots_t04.py --ep 03) ===")
qcs = WORK / "qc_shots_t04.py"
if qcs.exists():
    e = dict(os.environ)
    e["AE_EP"] = "03"
    e["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, str(qcs), "--ep", "03"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=e)
    tail = (r.stdout or "").strip().splitlines()[-6:]
    for l in tail:
        print("   " + l)
    chk("QC bang shot cua du an pass", r.returncode == 0, f"rc={r.returncode}")
else:
    print("   (khong tim thay qc_shots_t04.py — bo qua)")

# ---------------------------------------------------------------- phu de
print("\n=== phu de ===")
srt_p = OUT / ED.SRT
chk("File phu de ton tai", srt_p.exists(), str(srt_p))
srt = srt_p.read_text(encoding="utf-8-sig")
cues = [b for b in re.split(r"\n\s*\n", srt.strip()) if b.strip()]
bad, last = [], 0.0
for b in cues:
    L = b.splitlines()
    ts = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", L[1])
    a = int(ts[0][0]) * 3600 + int(ts[0][1]) * 60 + int(ts[0][2]) + int(ts[0][3]) / 1000
    z = int(ts[1][0]) * 3600 + int(ts[1][1]) * 60 + int(ts[1][2]) + int(ts[1][3]) / 1000
    if a < last:
        bad.append(L[0])
    if z <= a:
        bad.append(f"{L[0]} (ket thuc <= bat dau)")
    last = z
chk("Phu de khong co cue chong lap / vo trong", not bad, ", ".join(bad[:5]))
last_sent = tl["items"][-1]["end"]
chk("Cue cuoi phu de ket thuc khong qua loi cuoi", last <= last_sent + 1.0,
    f"cue cuoi {last:.2f} s · loi cuoi {last_sent:.2f} s")
print(f"   {len(cues)} cue · cue cuoi ket thuc luc {last:.1f} s · video {d_mp4:.1f} s")

# ---------------------------------------------------------------- thumbnail + tai lieu
print("\n=== thumbnail + tai lieu di kem ===")
if THUMB.exists():
    tim = Image.open(THUMB).convert("RGB")
    chk("Thumbnail 1280x720", tim.size == (1280, 720), str(tim.size))
    chk("Thumbnail khong den/trang het", 10 < float(np.array(tim).mean()) < 200,
        f"do sang TB {float(np.array(tim).mean()):.1f}")
else:
    chk("Thumbnail ton tai", False, str(THUMB))
for f in ("mo_ta.txt", "nguon_tham_khao.md"):
    chk(f"{f} ton tai", (OUT / f).exists(), str(OUT / f))

print()
print("=" * 74)
print("TAT CA DA DAT" if ok else "CO VIEC CHUA XONG")
print("=" * 74)
sys.exit(0 if ok else 1)
