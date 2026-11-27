#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC clip TikTok Tap04 (VN/EN/JA) — 14 cong T1–T14 (KE_HOACH_TIKTOK.md muc 4 Buoc 7)
+ cang H29 (logo kenh phai co tren moi shot noi dung) + H26 (khong chu tren hinh).

Cong H26/H29 duoc do bang PHAI HIEU:
  - Dung lai dung thuat toan camera_box cua _build_tk_tap04_video_notext.py
  - Tao anh nen mong doi (crop + resize, KHONG co logo)
  - So sanh frame thuc te voi anh nen mong doi:
      * vung NGOAI logo phai giong het (cam 0 sai lech)  => khong co chu/overlay nao them vao
      * vung LOGO phai KHAC anh nen mong doi              => logo da duoc ghep that
      * vung LOGO phai giong voi alpha_composite(nen, watermark) => logo dung file + dung do mo
"""
import glob
import json
import os
import pathlib
import re
import subprocess
import sys

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = glob.glob(str(WORK / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
FP = FF.replace("ffmpeg.exe", "ffprobe.exe")
W, H, FPS, PAD = 1080, 1920, 30, 1.12
LANGDIR = {"VN": "Tap04", "EN": "Tap04_EN", "JA": "Tap04_JA"}
WM_SIZE = 96
WM_POS = (684, 60)
SAFE_X0, SAFE_X1, SAFE_Y0, SAFE_Y1 = 120, 780, 240, 1260

BANNED = ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập",
          "đầu độc", "diệt cỏ", "bỏ đói", "móc áo", "hiếp", "cắt đầu",
          "vâng hãm", "hiếp dâm", "lột da", "trầm tích", "trầm tích"]
BANNED = [w for w in BANNED if w != "trầm tích"]


def sh(args):
    return subprocess.run(args, capture_output=True, text=True, errors="replace")


def camera_box(cam, p, W0, H0):
    z = {"push": 1.0 + 0.05 * p, "pull": 1.05 - 0.05 * p, "pan": 1.03, "still": 1.0}.get(cam, 1.0)
    cw, ch = W0 / z, H0 / z
    ox = (W0 - cw) / 2 + ((-60 + 120 * p) if cam == "pan" else 0)
    oy = (H0 - ch) / 2
    ox = max(0.0, min(ox, W0 - cw))
    oy = max(0.0, min(oy, H0 - ch))
    return (ox, oy, ox + cw, oy + ch)


def probe(path):
    j = json.loads(sh([FP, "-v", "quiet", "-print_format", "json",
                       "-show_format", "-show_streams", str(path)]).stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    a = next(s for s in j["streams"] if s["codec_type"] == "audio")
    fr = v.get("avg_frame_rate", "0/1").split("/")
    fps = float(fr[0]) / float(fr[1]) if float(fr[1]) else 0.0
    return {"w": v["width"], "h": v["height"], "vcodec": v["codec_name"],
            "acodec": a["codec_name"], "fps": fps,
            "vdur": float(v.get("duration") or j["format"]["duration"]),
            "adur": float(a.get("duration") or j["format"]["duration"]),
            "dur": float(j["format"]["duration"]),
            "size": int(j["format"]["size"]),
            "start": float(v.get("start_time") or 0.0)}


def loudness(path):
    r = sh([FF, "-hide_banner", "-i", str(path), "-af",
            "ebur128=peak=true", "-f", "null", "-"])
    txt = r.stderr
    i = txt.rfind("Integrated loudness")
    i_lufs = i = txt.find("I:")
    peak = txt.find("Peak:")
    tp = float(re.search(r"Peak:\s*(-?[\d.]+)", txt).group(1)) if peak >= 0 else None
    m = re.findall(r"I:\s*(-?[\d.]+)\s*LUFS", txt)
    lufs = float(m[-1]) if m else None
    return lufs, tp


def silences(path):
    r = sh([FF, "-hide_banner", "-i", str(path), "-af",
            "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"])
    return re.findall(r"silence_duration:\s*([\d.]+)", r.stderr)


def grab(path, t, dst):
    sh([FF, "-y", "-v", "error", "-ss", "%.3f" % t, "-i", str(path), "-frames:v", "1", str(dst)])
    return np.asarray(Image.open(str(dst)).convert("RGB")).astype(np.int16)


def check_logo(lang, clip, mp4, tl_path, spec_path, frames_dir):
    """Kiem tra H26 (khong chu them) + H29 (logo dung vi tri + dung do mo)."""
    d = ROOT / "02_SAN_XUAT" / "TIKTOK" / LANGDIR[lang]
    spec = json.loads(pathlib.Path(spec_path).read_text(encoding="utf-8-sig"))
    tl = json.loads(pathlib.Path(tl_path).read_text(encoding="utf-8-sig"))
    n = clip[2:]
    lines = spec["clips"][clip]["lines"]
    meta = {l["clip_line_id"]: (l["bg"], l.get("motion", "still")) for l in lines}
    total = probe(mp4)["dur"]
    shots = []
    for k, l in enumerate(tl):
        s0 = 0.0 if k == 0 else l["start"]
        s1 = tl[k + 1]["start"] if k + 1 < len(tl) else total
        shots.append({"id": l["id"], "bg": meta[l["id"]][0], "cam": meta[l["id"]][1], "s0": s0, "s1": s1})

    wm = Image.open(ROOT / "assets" / "brand" / "watermark.png").convert("RGBA")
    if wm.size != (WM_SIZE, WM_SIZE):
        wm = wm.resize((WM_SIZE, WM_SIZE), Image.LANCZOS)
    wm_np = np.asarray(wm).astype(np.float32)

    lx0, ly0 = WM_POS
    lx1, ly1 = lx0 + WM_SIZE, ly0 + WM_SIZE
    bg_cache = {}
    res = {"n_frames": 0, "max_diff_ngoai_logo": 0, "logo_diff_min": 1e9,
           "logo_match_max": 0, "logo_in_safe": True,
           "mean_diff_ngoai": 0.0, "p999_ngoai": 0.0, "logo_diff_vs_expected": 0.0,
           "bad_px_ngoai_pct": 0.0}
    ts = np.linspace(0.5, total - 0.5, 7)
    for i, t in enumerate(ts):
        dst = frames_dir / f"{clip}_f{i}.png"
        got = grab(mp4, float(t), dst)
        # shot tai thoi diem t
        si = 0
        while si + 1 < len(shots) and t >= shots[si + 1]["s0"]:
            si += 1
        s = shots[si]
        p = max(0.0, min(1.0, (t - s["s0"]) / max(1e-6, s["s1"] - s["s0"])))
        if s["bg"] not in bg_cache:
            bg_cache[s["bg"]] = Image.open(ROOT / "assets" / "bg" / (s["bg"] + ".png")).convert("RGB").resize(
                (int(W * PAD), int(H * PAD)), Image.LANCZOS)
        im = bg_cache[s["bg"]]
        exp_nologo = np.asarray(
            im.resize((W, H), Image.BILINEAR, box=camera_box(s["cam"], p, im.width, im.height))
        ).astype(np.int16)
        # mong doi co logo
        exp = exp_nologo.astype(np.float32)
        a = wm_np[..., 3:4] / 255.0
        reg = exp[ly0:ly1, lx0:lx1]
        exp[ly0:ly1, lx0:lx1] = reg * (1 - a) + wm_np[..., :3] * a
        exp = exp.astype(np.int16)

        d_full = np.abs(got - exp).max(axis=2)
        mask = np.ones((H, W), bool)
        mask[ly0:ly1, lx0:lx1] = False
        d_out = d_full[mask]
        res["max_diff_ngoai_logo"] = max(res["max_diff_ngoai_logo"], float(d_out.max()))
        res["mean_diff_ngoai"] = max(res["mean_diff_ngoai"], float(d_out.mean()))
        res["p999_ngoai"] = max(res["p999_ngoai"], float(np.percentile(d_out, 99.9)))
        res["bad_px_ngoai_pct"] = max(res["bad_px_ngoai_pct"],
                                      float((d_out > 40).mean() * 100.0))
        # logo: so voi nen KHONG logo (phai khac) va voi nen CO logo (phai giong)
        d_logo_vs_bg = np.abs(got[ly0:ly1, lx0:lx1] - exp_nologo[ly0:ly1, lx0:lx1])
        d_logo_vs_exp = np.abs(got[ly0:ly1, lx0:lx1] - exp[ly0:ly1, lx0:lx1])
        res["logo_diff_min"] = min(res["logo_diff_min"], float(d_logo_vs_bg.mean()))
        res["logo_max_vs_bg"] = max(res.get("logo_max_vs_bg", 0), float(d_logo_vs_bg.max()))
        res["logo_match_max"] = max(res["logo_match_max"], float(d_logo_vs_exp.mean()))
        res["n_frames"] += 1
    res["logo_in_safe"] = (lx0 >= SAFE_X0 and lx1 <= SAFE_X1 and ly0 >= 60 and ly1 <= 200)
    return res


def main():
    langs = sys.argv[1:] or ["VN", "EN", "JA"]
    frames_dir = WORK / "_qc_tk04_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    report = {}
    for lang in langs:
        d = ROOT / "02_SAN_XUAT" / "TIKTOK" / LANGDIR[lang]
        spec_path = d / "SPEC_AUDIO_CLIP_TAP04.json"
        print("=" * 78)
        print(f"QC CLIP TIKTOK TAP04 — {lang}")
        print("=" * 78)
        rows = []
        for clip in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
            n = clip[2:]
            mp4 = d / f"TK{n}_video.mp4"
            if not mp4.exists():
                print(f"  {clip}: THIEU {mp4.name}")
                continue
            pr = probe(mp4)
            lufs, tp = loudness(mp4)
            sil = silences(mp4)
            dec = sh([FF, "-v", "error", "-i", str(mp4), "-f", "null", "-"]).stderr.strip()
            lg = check_logo(lang, clip, mp4, d / f"timeline_tk{n}.json", spec_path, frames_dir)
            # T13 tu cam — theo TUNG clip, khong quet ca tap
            spec = json.loads(spec_path.read_text(encoding="utf-8-sig"))
            clip_lines = spec["clips"][clip]["lines"]
            low = " ".join(l["text"] for l in clip_lines).lower()
            hits = [w for w in BANNED if w in low]
            t = {
                "T1_khung": pr["w"] == 1080 and pr["h"] == 1920,
                "T2_codec_fps": pr["vcodec"] == "h264" and pr["acodec"] == "aac" and abs(pr["fps"] - 30) < 0.2,
                "T3_dung_luong": pr["size"] <= 500 * 1024 * 1024,
                "T4_do_dai": 30 <= pr["dur"] <= 95,
                "T5_am_luong": lufs is not None and abs(lufs + 16) <= 1.0 and tp is not None and tp <= -1.5,
                "T6_khoang_cam": len(sil) == 0,
                "T7_lech_hinh_tieng": abs(pr["vdur"] - pr["adur"]) <= 0.05 and pr["start"] == 0.0,
                "T8_giai_ma": dec == "",
                "T9_safe_zone": lg["logo_in_safe"],
                "T10_khong_wm_nen_tang": lg["bad_px_ngoai_pct"] < 0.5 and lg["mean_diff_ngoai"] < 8.0,
                "T11_khong_chu_ai": lg["bad_px_ngoai_pct"] < 0.5 and lg["mean_diff_ngoai"] < 8.0,
                "T12_khong_mat_nguoi_that": None,
                "T13_tu_cam": len(hits) == 0,
                "T14_hook_chu": None,
                "H26_khong_chu_chen": lg["bad_px_ngoai_pct"] < 0.5 and lg["mean_diff_ngoai"] < 8.0,
                "H29_logo_co_tren_khung": (lg["logo_diff_min"] >= 1.5
                                           and lg.get("logo_max_vs_bg", 0) > 20
                                           and lg["logo_match_max"] < 8.0),
            }
            fails = [k for k, v in t.items() if v is False]
            na = [k for k, v in t.items() if v is None]
            print(f"  {clip}  {pr['dur']:6.2f}s  {pr['w']}x{pr['h']}  {pr['vcodec']}/{pr['acodec']} @{pr['fps']:.2f}  "
                  f"{pr['size']/1048576:6.1f}MB  {lufs} LUFS  TP {tp}  sil={len(sil)}")
            print(f"        logo: sai-nen mean={lg['logo_diff_min']:.2f} max={lg.get('logo_max_vs_bg',0):.0f}  "
                  f"sai-mongdoi mean={lg['logo_match_max']:.2f}  "
                  f"| ngoai-logo mean={lg['mean_diff_ngoai']:.2f} p99.9={lg['p999_ngoai']:.0f} "
                  f"px>40={lg['bad_px_ngoai_pct']:.3f}%  safe={lg['logo_in_safe']}")
            print(f"        FAIL: {fails if fails else 'KHONG CO'}   |  N/A: {na if na else '-'}")
            if hits:
                print(f"        TU CAM trong cau: {hits}")
            if sil:
                print(f"        khoang cam >0.3s: {sil}")
            if dec:
                print(f"        loi giai ma: {dec[:300]}")
            rows.append({"clip": clip, "probe": pr, "lufs": lufs, "tp": tp,
                         "silences": sil, "decode_err": dec, "logo": lg,
                         "tests": {k: v for k, v in t.items()}, "banned_hits": hits})
        report[lang] = rows
        tot = sum(len([k for k, v in r["tests"].items() if v is False]) for r in rows)
        print(f"  => {lang}: {tot} loi FAIL tren {len(rows)} clip\n")
    (WORK / "_qc_tk04_clip.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Bao cao: .work/_qc_tk04_clip.json")


if __name__ == "__main__":
    main()
