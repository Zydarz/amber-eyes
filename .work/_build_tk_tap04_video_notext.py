#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung clip TikTok Tap04 (VN/EN/JA) - KHONG CHU tren hinh, CO LOGO kenh (H29).

Chi: anh nen doc goc tk04_*.png + camera still/push/pull/pan + audio master san co.
Khong hook, khong the overlay, khong phu de, khong logo wordmark.

LUAT H29 (27/11/2026): moi shot noi dung PHAI ghep logo kenh
`assets/brand/watermark.png` (96 px, do mo 35 % da nam san trong PNG alpha=89),
chi an trong intro va the chuong. Video 9:16 TikTok: vung goc duoi-phai bi UI
platform che (nut hanh dong x~940-1060 y~1060-1690, caption o duoi y>1520) =>
dat logo o GOC TREN-PHAI trong safe zone T6 (x 120-780, y 60-200) de logo that
su nhin thay duoc. Doi vi tri: bam WM_POS.

Dung:  py -3 .work/_build_tk_tap04_video_notext.py <VN|EN|JA> [TK1 TK2 ...]
Ra:    02_SAN_XUAT/TIKTOK/<Tap04|Tap04_EN|Tap04_JA>/TKn_video.mp4 (1080x1920, 30fps, H.264 + AAC)
Input: SPEC_AUDIO_CLIP_TAP04.json (bg + motion) - timeline_tkn.json (moc thoi gian) - TKn_master_audio.mp3
"""
import glob
import json
import pathlib
import subprocess
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
FP = FF.replace("ffmpeg.exe", "ffprobe.exe")
W, H, FPS, PAD = 1080, 1920, 30, 1.12
LANGDIR = {"VN": "Tap04", "EN": "Tap04_EN", "JA": "Tap04_JA"}

# --- H29: logo kenh 96 px, do mo 35 % (alpha=89 trong PNG) ---
WM_SIZE = 96
WM_POS = (684, 60)          # goc tren-phai, trong safe zone T6 (x<=780, y<=200)
WM_FILE = ROOT / "assets" / "brand" / "watermark.png"


def camera_box(cam, p, W0, H0):
    z = {"push": 1.0 + 0.05 * p, "pull": 1.05 - 0.05 * p, "pan": 1.03, "still": 1.0}.get(cam, 1.0)
    cw, ch = W0 / z, H0 / z
    ox = (W0 - cw) / 2 + ((-60 + 120 * p) if cam == "pan" else 0)
    oy = (H0 - ch) / 2
    ox = max(0.0, min(ox, W0 - cw))
    oy = max(0.0, min(oy, H0 - ch))
    return (ox, oy, ox + cw, oy + ch)


def dur(path):
    return float(subprocess.check_output([FP, "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", str(path)]).decode().strip())


def lines_of(spec, clip):
    c = spec["clips"]
    if isinstance(c, list):
        return [(l["id"], l["nen"], l["chuyen_dong"]) for l in next(x for x in c if x["id"] == clip)["lines"]]
    return [(l["clip_line_id"], l["bg"], l.get("motion", "still")) for l in c[clip]["lines"]]


def build(lang, clip):
    d = ROOT / "02_SAN_XUAT" / "TIKTOK" / LANGDIR[lang]
    n = clip[2:]
    spec = json.loads((d / "SPEC_AUDIO_CLIP_TAP04.json").read_text(encoding="utf-8-sig"))
    tl = json.loads((d / f"timeline_tk{n}.json").read_text(encoding="utf-8-sig"))
    meta = {i: (b, m) for i, b, m in lines_of(spec, clip)}
    audio = d / f"TK{n}_master_audio.mp3"
    total = dur(audio)
    nfr = int(round(total * FPS))
    # shot i: tu start cau i den start cau i+1 (khoang nghi thuoc shot truoc); shot dau tu 0; shot cuoi den het audio
    shots = []
    for k, l in enumerate(tl):
        s0 = 0.0 if k == 0 else l["start"]
        s1 = tl[k + 1]["start"] if k + 1 < len(tl) else total
        shots.append({"id": l["id"], "bg": meta[l["id"]][0], "cam": meta[l["id"]][1], "s0": s0, "s1": s1})
    bgs = {}
    for s in shots:
        if s["bg"] not in bgs:
            p = ROOT / "assets" / "bg" / (s["bg"] + ".png")
            if not p.exists():
                raise SystemExit("THIEU NEN " + str(p))
            bgs[s["bg"]] = Image.open(p).convert("RGB").resize((int(W * PAD), int(H * PAD)), Image.LANCZOS)
    # H29: logo kenh ghep len moi khung
    wm = Image.open(WM_FILE).convert("RGBA")
    if wm.size != (WM_SIZE, WM_SIZE):
        wm = wm.resize((WM_SIZE, WM_SIZE), Image.LANCZOS)
    out = d / f"TK{n}_video.mp4"
    cmd = [FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-i", str(audio), "-map", "0:v", "-map", "1:a",
           "-c:v", "libopenh264", "-b:v", "6000k", "-maxrate", "9000k", "-bufsize", "12000k",
           "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
           "-t", f"{total:.3f}", "-movflags", "+faststart", str(out)]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    si = 0
    for fi in range(nfr):
        t = fi / FPS
        while si + 1 < len(shots) and t >= shots[si + 1]["s0"]:
            si += 1
        s = shots[si]
        p = max(0.0, min(1.0, (t - s["s0"]) / max(1e-6, s["s1"] - s["s0"])))
        im = bgs[s["bg"]]
        fr = im.resize((W, H), Image.BILINEAR, box=camera_box(s["cam"], p, im.width, im.height))
        fr = fr.convert("RGBA")
        fr.alpha_composite(wm, WM_POS)
        pr.stdin.write(fr.convert("RGB").tobytes())
    pr.stdin.close()
    pr.wait()
    if pr.returncode != 0:
        raise SystemExit(f"FFmpeg loi khi render {clip} (code {pr.returncode})")
    print(f"[{lang} {clip}] {out.name}  audio={total:.2f}s  {len(shots)} shot  {len(bgs)} nen  logo={WM_POS}", flush=True)
    return {"lang": lang, "clip": clip, "audio_s": total, "shots": shots, "file": str(out),
            "logo_pos": list(WM_POS), "logo_size": WM_SIZE}


if __name__ == "__main__":
    lang = sys.argv[1].upper()
    clips = sys.argv[2:] or ["TK1", "TK2", "TK3", "TK4", "TK5"]
    res = [build(lang, c) for c in clips]
    (ROOT / ".work" / f"_tk_notext_manifest_{lang}_t04.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
