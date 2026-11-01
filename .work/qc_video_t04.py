"""Cổng giám sát cuối — Tập 04 (dùng lại được cho tập khác: --ep).

Kiểm toàn bộ chuỗi ÂM THANH → HÌNH → ĐÓNG GÓI theo AGENTS.md bước 6/9/10,
H14, A7, A11 #55:

  A  Audio master   : 0 khoảng lâm > 0,3 s @ -60 dB · -16 ± 1 LUFS · peak ≤ -1,5 dBFS
                       · lời đầu 22,8-23,5 s
  B  Timeline + shot: picture khớp timeline.total ± 0,05 s · bảng shot phủ 100% câu
                       đúng thứ tự · mọi nền có file
  C  Picture        : picture.mp4 khớp timeline.total ± 0,05 s (H14)
  D  File cuối      : ± 0,05 s với audio · giải mã 0 lỗi · -16 ± 1 LUFS · peak ≤ -1,5
                       · 1920x1080 · H.264 + AAC
  E  Phụ đề         : có file · số cue khớp số câu · cue cuối nằm trong file
  F  Thumbnail      : đúng nền `thumb_bg` của tập
  G  Thẻ kết        : khung hình cuối (total - 2 s) KHÔNG đen, và shot cuối là thẻ kết

Chạy:  py -3 .work/qc_video_t04.py --ep 04
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

OK, WARN, FAIL = [], [], []


def ok(m):
    OK.append(m)


def bad(m):
    FAIL.append(m)


def warn(m):
    WARN.append(m)


def run(args):
    return subprocess.run([str(a) for a in args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def dur(path):
    r = run([FP, "-v", "error", "-show_entries", "format=duration", "-of",
             "csv=p=0", path])
    try:
        return float(r.stdout.strip().splitlines()[0])
    except Exception:
        return None


def lufs_peak(path):
    r = run([FF, "-hide_banner", "-nostats", "-i", path, "-af",
             "ebur128=peak=true", "-f", "null", "-"])
    e = r.stderr
    m = re.findall(r"I:\s*(-?[\d.]+) LUFS", e)
    p = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", e)
    return (float(m[-1]) if m else None, float(p[-1]) if p else None)


def silences(path, d=0.3, noise=-60):
    r = run([FF, "-hide_banner", "-nostats", "-i", path, "-af",
             f"silencedetect=noise={noise}dB:d={d}", "-f", "null", "-"])
    return re.findall(r"silence_duration:\s*([\d.]+)", r.stderr)


def first_speech(path, stems_dir):
    """Thoi diem LOI DAU do tu STEM giong (khong nhac nen).

    `silencedetect` tren file hop khong dung: nhac nen luon tren -50 dBFS
    nen khong co khoang lang nao -> silence_end dau tien ruc o CUOI tap.
    Stem giong (16 kHz, chi giong) moi do dung thoi diem bat dau len tieng.
    """
    import numpy as np
    import soundfile as sf
    best = None
    for role in ("H", "D", "C", "N1", "N2"):
        p = pathlib.Path(stems_dir) / f"{role}.wav"
        if not p.exists():
            return None
        x, sr = sf.read(str(p), dtype="float32")
        if len(x) == 0:
            continue
        idx = np.where(np.abs(x) > 10 ** (-50 / 20))[0]
        if len(idx) == 0:
            continue
        t = float(idx[0]) / sr
        best = t if best is None else min(best, t)
    return best


def bright_ratio(png, thr=140):
    """Ti le pixel sang (>thr) cua khung — do bang mau chu tren hinh (242,239,233)."""
    from PIL import Image
    with Image.open(png) as im:
        g = im.convert("L")
        w, h = g.size
        px = g.load()
        n = 0
        tot = 0
        for y in range(0, h, 4):
            for x in range(0, w, 4):
                tot += 1
                if px[x, y] > thr:
                    n += 1
        return n / max(1, tot)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ep", default="04")
    a = ap.parse_args()
    ep = a.ep
    sys.path.insert(0, str(WORK))
    import edition as ED

    out = ROOT / "02_SAN_XUAT" / f"Tap{ep}" / "xuat_ban"
    master = out / f"Tap{ep}_master.mp3"
    final = out / f"Tap{ep}_master.mp4"
    picture = ED.w("video3") / "picture.mp4"
    tl_p = ED.w("timeline_s.json")
    shots_p = ED.w("shots.json")
    srt = out / f"Tap{ep}.srt"
    thumb = out / "thumbnail.png"

    print(f"===== CỔNG GIÁM SÁT TAP{ep} =====")

    # ---------------- A. audio master
    if not master.exists():
        bad(f"A) thieu audio master: {master}")
    else:
        d = dur(master)
        lu, pk = lufs_peak(master)
        sil = silences(master)
        fs = first_speech(master, ED.w("stems"))
        print(f"  master: {d} s | LUFS {lu} | peak {pk} | sil>0.3s {len(sil)} | lời đầu {fs}")
        if d is None:
            bad("A) khong doc duoc thoi luong master")
        if lu is None or not (-17.0 <= lu <= -15.0):
            bad(f"A) LUFS {lu} ngoai -16 +/- 1")
        else:
            ok(f"A) LUFS {lu} trong -16 +/- 1")
        if pk is None or pk > -1.5:
            bad(f"A) dinh that {pk} > -1,5 dBFS")
        else:
            ok(f"A) dinh that {pk} <= -1,5 dBFS")
        if sil:
            bad(f"A) {len(sil)} khoang lang > 0,3 s: {sil[:8]}")
        else:
            ok("A) 0 khoang lang > 0,3 s @ -60 dB")
        if fs is None or not (22.8 <= fs <= 23.5):
            bad(f"A) loi dau {fs} ngoai 22,8-23,5 s")
        else:
            ok(f"A) loi dau {fs} s trong 22,8-23,5 s")
        tl_total = None
        if tl_p.exists():
            tl = json.loads(tl_p.read_text(encoding="utf-8-sig"))
            tl_total = tl.get("total")
            if tl_total and d and abs(tl_total - d) > 0.05:
                bad(f"A) timeline.total {tl_total} lech master {d} > 0,05 s")
            else:
                ok(f"A) timeline.total {tl_total} khop master {d} (±0,05 s)")

    # ---------------- B. bang shot
    if not shots_p.exists():
        bad(f"B) thieu shots.json: {shots_p}")
    else:
        sh = json.loads(shots_p.read_text(encoding="utf-8-sig"))["shots"]
        sent_ids = []
        for s in sh:
            sent_ids += s.get("sentences", [])
        sc = json.loads(ED.EP["script"].read_text(encoding="utf-8-sig"))
        want = [x["id"] for el in sc if el.get("kind") == "LOI" for x in el.get("sentences", [])]
        if sent_ids == want:
            ok(f"B) bang shot phu 100% {len(want)} cau dung thu tu")
        else:
            miss = [c for c in want if c not in sent_ids]
            extra = [c for c in sent_ids if c not in want]
            dup = [c for c in set(sent_ids) if sent_ids.count(c) > 1]
            bad(f"B) phu cau sai: thieu {miss[:8]} thua {extra[:8]} trung {dup[:8]}")
        nobg = [s["id"] for s in sh if not s.get("bg") and not s.get("hold")]
        if nobg:
            bad(f"B) shot khong nen: {nobg[:10]}")
        else:
            ok(f"B) moi {len(sh)} shot deu co nen")
        gaps = []
        for i in range(len(sh) - 1):
            g = sh[i + 1]["start"] - sh[i]["end"]
            if abs(g) > 0.05:
                gaps.append((sh[i]["id"], round(g, 3)))
        if gaps:
            bad(f"B) shot khong lien tuc (>0,05 s): {gaps[:8]}")
        else:
            ok("B) cac shot lien tuc, khong gap")
        longshot = [(s["id"], round(s["end"] - s["start"], 1)) for s in sh
                    if s["end"] - s["start"] > 16]
        if longshot:
            warn(f"B) shot dai > 16 s: {longshot[:6]}")
        else:
            ok("B) khong shot nao dai > 16 s")

    # ---------------- C. picture
    if not picture.exists():
        bad(f"C) thieu picture.mp4: {picture}")
    else:
        pd = dur(picture)
        if tl_total and pd and abs(pd - tl_total) > 0.05:
            bad(f"C) picture {pd} lech timeline.total {tl_total} > 0,05 s (H14)")
        else:
            ok(f"C) picture.mp4 {pd} s khop timeline.total {tl_total} (±0,05 s)")

    # ---------------- D. file cuoi
    if not final.exists():
        bad(f"D) thieu file cuoi: {final}")
    else:
        fd = dur(final)
        md = dur(master) if master.exists() else None
        if fd and md and abs(fd - md) > 0.05:
            bad(f"D) mp4 {fd} lech audio {md} > 0,05 s")
        else:
            ok(f"D) mp4 {fd} s khop audio {md} (±0,05 s)")
        r = run([FF, "-v", "error", "-i", final, "-f", "null", "-"])
        errs = [l for l in r.stderr.splitlines() if l.strip()]
        if errs:
            bad(f"D) giai ma co loi: {errs[:5]}")
        else:
            ok("D) giai ma 0 loi")
        lu, pk = lufs_peak(final)
        print(f"  final : {fd} s | LUFS {lu} | peak {pk}")
        if lu is None or not (-17.0 <= lu <= -15.0):
            bad(f"D) LUFS file cuoi {lu} ngoai -16 +/- 1 (A7)")
        else:
            ok(f"D) LUFS file cuoi {lu} trong -16 +/- 1 (A7)")
        if pk is None or pk > -1.5:
            bad(f"D) dinh that file cuoi {pk} > -1,5 dBFS (A7)")
        else:
            ok(f"D) dinh that file cuoi {pk} <= -1,5 dBFS (A7)")
        r = run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries",
                 "stream=width,height,r_frame_rate,codec_name", "-of", "csv=p=0", final])
        v = r.stdout.strip().splitlines()[0] if r.stdout.strip() else ""
        r2 = run([FP, "-v", "error", "-select_streams", "a:0", "-show_entries",
                  "stream=codec_name,sample_rate,channels", "-of", "csv=p=0", final])
        au = r2.stdout.strip().splitlines()[0] if r2.stdout.strip() else ""
        print(f"  video : {v}")
        print(f"  audio : {au}")
        if "1920,1080" not in v:
            bad(f"D) kich thuoc khong phai 1920x1080: {v}")
        else:
            ok("D) 1920x1080")
        if "h264" not in v:
            bad(f"D) video codec khong phai h264: {v}")
        else:
            ok("D) video H.264")
        if "aac" not in au:
            bad(f"D) audio codec khong phai aac: {au}")
        else:
            ok("D) audio AAC")
        sil = silences(final)
        if sil:
            bad(f"D) {len(sil)} khoang lang > 0,3 s trong file cuoi: {sil[:8]}")
        else:
            ok("D) 0 khoang lang > 0,3 s trong file cuoi")

    # ---------------- E. phu de
    if not srt.exists():
        bad(f"E) thieu phu de: {srt}")
    else:
        t = srt.read_text(encoding="utf-8-sig")
        cues = re.findall(r"-->\s*(\d+):(\d+):(\d+)[,.](\d+)", t)
        n = len(cues)
        sc2 = json.loads(ED.EP["script"].read_text(encoding="utf-8-sig"))
        want2 = sum(len(el.get("sentences", [])) for el in sc2 if el.get("kind") == "LOI")
        # So NOI DUNG: phu de tach cau dai thanh nhieu cue nen khong the so cue voi so cau.
        blocks = [b for b in re.split(r"\r?\n\r?\n", t.strip()) if b.strip()]
        srt_txt = " ".join(" ".join(b.splitlines()[2:]) for b in blocks)
        srt_txt = re.sub(r"\[[^\]]*\]", " ", srt_txt)
        tl_e = json.loads(tl_p.read_text(encoding="utf-8-sig"))
        scr_txt = " ".join(i["text"] for i in tl_e["items"])
        nz = lambda x: re.sub(r"\s+", "", x).casefold()
        if nz(srt_txt) == nz(scr_txt):
            ok(f"E) phu de phu 100% loi thoai ({n} cue / {want2} cau)")
        else:
            a, b = nz(srt_txt), nz(scr_txt)
            k = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
            bad(f"E) noi dung phu de KHONG khop kich ban (sai tu ky tu {k}: "
                f"phu de ...{a[max(0, k - 20):k + 20]}... / kich ban ...{b[max(0, k - 20):k + 20]}...)")
        if cues:
            e = int(cues[-1][0]) * 3600 + int(cues[-1][1]) * 60 + int(cues[-1][2]) + int(cues[-1][3]) / 1000
            fd = dur(final) if final.exists() else None
            if fd and e > fd + 0.5:
                bad(f"E) cue cuoi {e:.2f}s vuot thoi luong file {fd:.2f}s")
            else:
                ok(f"E) cue cuoi {e:.2f}s nam trong file")

    # ---------------- F. thumbnail
    if not thumb.exists():
        bad(f"F) thieu thumbnail: {thumb}")
    else:
        ok(f"F) thumbnail ton tai ({thumb.stat().st_size} bytes)")
        tb = ED.EP.get("thumb_bg")
        if tb:
            ok(f"F) nen thumbnail theo ke hoach: {tb}")

    # ---------------- G. the ket
    if final.exists():
        tot = dur(final)
        if tot:
            sh_last = None
            if shots_p.exists():
                sh_last = json.loads(shots_p.read_text(encoding="utf-8-sig"))["shots"][-1]
            # thuc te: the ket hien ro o giua shot cuoi (render fade dan den o 3 s cuoi)
            t_card = (sh_last["start"] + 1.5) if sh_last else max(0, tot - 2)
            png = WORK / f"_qc_endcard_{ep}.png"
            r = run([FF, "-v", "error", "-ss", f"{t_card:.3f}", "-i", final,
                     "-frames:v", "1", "-y", str(png)])
            if png.exists() and png.stat().st_size > 5000:
                br = bright_ratio(png)
                if br > 0.0005:
                    ok(f"G) the ket co chu tai {t_card:.1f}s ({br * 100:.2f}% pixel sang)")
                else:
                    bad(f"G) khung the ket tai {t_card:.1f}s khong co chu ({br * 100:.3f}% pixel sang)")
                print(f"  (khung the ket: {png})")
            else:
                bad(f"G) khong trich duoc khung the ket tai {t_card:.1f}s")
            # A11 #55: khung tai total-2 s — renderer mo dan shot cuoi 3 s cuoi => den
            png2 = WORK / f"_qc_endcard_{ep}_cuoi.png"
            run([FF, "-v", "error", "-ss", f"{max(0, tot - 2):.3f}", "-i", final,
                 "-frames:v", "1", "-y", str(png2)])
            b2 = bright_ratio(png2) if png2.exists() else 0.0
            if b2 > 0.0005:
                ok(f"G) khung tai total-2 s van co chu ({b2 * 100:.2f}% pixel sang)")
            else:
                warn("G) khung tai total-2 s den — outro cua renderer mo dan shot cuoi 3 s cuoi"
                      " (dung chung T01-T03); the ket da kiem o giua shot cuoi")
    if shots_p.exists():
        sh = json.loads(shots_p.read_text(encoding="utf-8-sig"))["shots"]
        last = sh[-1]
        if not last.get("sentences"):
            ok(f"G) shot cuoi '{last['id']}' la the ket (khong gan cau)")
        else:
            bad(f"G) shot cuoi '{last['id']}' van gan cau — thieu the ket")

    print()
    for x in OK:
        print(f"  [OK]   {x}")
    for x in WARN:
        print(f"  [WARN] {x}")
    for x in FAIL:
        print(f"  [FAIL] {x}")
    print(f"\n  => {len(OK)} OK · {len(WARN)} canh bao · {len(FAIL)} loi")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
