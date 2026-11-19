"""QC audio TK1 (clip TikTok Tap 01) — do that, khong sua gi.

Kiem: khop spec · hinh thuc · do dai · khoang cam · F0/G9 theo vai · nhip doc · nhieu.
"""
import json
import pathlib
import subprocess
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFPROBE = FF.with_name("ffprobe.exe")
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"
WAV = D / "TK1_master_audio.wav"
MP3 = D / "TK1_master_audio.mp3"
TL = D / "timeline_tk1.json"
SPEC = D / "SPEC_AUDIO_CLIP_TAP01.json"

SIL_DB = -60.0
SIL_MIN = 0.3
TARGET_I = (-17.0, -15.0)
MAX_TP = -1.5
DUR_MIN, DUR_MAX = 45.0, 95.0


def read_wav(p):
    with wave.open(str(p), "rb") as wf:
        sr = wf.getframerate()
        ch = wf.getnchannels()
        sw = wf.getsampwidth()
        n = wf.getnframes()
        raw = wf.readframes(n)
    dt = {1: np.int16, 2: np.int16, 4: np.int32}[sw]
    x = np.frombuffer(raw, dtype=dt).astype(np.float32)
    x /= float(2 ** (8 * sw - 1))
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    return x, sr


def f0_median(x, sr, fmin=60, fmax=450):
    """F0 trung vị theo tuong quan (AC) — cung phuong phuc voi estimate_f0() cua du an."""
    fl = int(sr * 0.04)
    hop = int(sr * 0.01)
    out = []
    min_lag, max_lag = int(sr / fmax), int(sr / fmin)
    for i in range(0, len(x) - fl, hop):
        seg = x[i:i + fl]
        if np.std(seg) < 0.01:
            continue
        c = np.correlate(seg, seg, "full")[fl - 1:]
        if len(c) <= max_lag:
            continue
        p = int(np.argmax(c[min_lag:max_lag])) + min_lag
        if c[0] > 0 and c[p] / c[0] > 0.4:
            out.append(sr / p)
    return float(np.median(out)) if out else 0.0


def semis(f1, f2):
    if f1 <= 0 or f2 <= 0:
        return 0.0
    return 12.0 * np.log2(f2 / f1)


def main():
    tl = json.loads(TL.read_text(encoding="utf-8-sig"))
    spec = json.loads(SPEC.read_text(encoding="utf-8-sig"))
    tk1 = next(c for c in spec["clips"] if c["id"] == "TK1")
    spec_lines = {l["id"]: l for l in tk1["lines"]}

    x, sr = read_wav(WAV)
    dur = len(x) / sr

    print("=" * 78)
    print("QC AUDIO TK1 · clip TikTok Tap 01 · 18/11/2026")
    print("=" * 78)

    # ---------- 1. FORMAT ----------
    pr = subprocess.run([str(FFPROBE), "-v", "quiet", "-print_format", "json",
                         "-show_format", "-show_streams", str(WAV)],
                        capture_output=True, text=True)
    j = json.loads(pr.stdout)
    a = next(s for s in j["streams"] if s["codec_type"] == "audio")
    print("\n[1] HINH THUC")
    print("    WAV : %s %d Hz · %d kenh · %s bit · %.3f s · %.2f MB"
          % (a["codec_name"], int(a["sample_rate"]), a["channels"],
             a.get("bits_per_raw_sample", "16"), dur, WAV.stat().st_size / 1e6))
    pr2 = subprocess.run([str(FFPROBE), "-v", "quiet", "-print_format", "json",
                          "-show_format", "-show_streams", str(MP3)],
                         capture_output=True, text=True)
    j2 = json.loads(pr2.stdout)
    a2 = next(s for s in j2["streams"] if s["codec_type"] == "audio")
    d2 = float(j2["format"]["duration"])
    print("    MP3 : %s %d Hz · %d kenh · %d kbps · %.3f s"
          % (a2["codec_name"], int(a2["sample_rate"]), a2["channels"],
             int(a2["bit_rate"]) // 1000, d2))
    print("    Lech WAV-MP3 : %.3f s  %s" % (abs(d2 - dur), "OK" if abs(d2 - dur) <= 0.05 else "LOI"))

    # ---------- 2. LOUDNESS ----------
    eb = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(WAV),
                         "-af", "ebur128=peak=true", "-f", "null", "-"],
                        capture_output=True, text=True, errors="replace").stderr
    I = tp = None
    for ln in eb.splitlines():
        if "I:" in ln and "LUFS" in ln:
            try:
                I = float(ln.split("I:")[1].split("LUFS")[0].strip())
            except Exception:
                pass
        if "Peak:" in ln and "dBFS" in ln:
            try:
                tp = float(ln.split("Peak:")[1].split("dBFS")[0].strip())
            except Exception:
                pass
    print("\n[2] DO LUONG")
    print("    I (tich hop) : %.1f LUFS   (chuan -16 +/- 1)  %s"
          % (I, "DAT" if TARGET_I[0] <= I <= TARGET_I[1] else "TRUOT"))
    print("    True peak    : %.1f dBFS  (chuan <= -1.5)     %s"
          % (tp, "DAT" if tp <= MAX_TP else "TRUOT"))
    print("    Do dai clip  : %.2f s  (cong 45-95 s)         %s"
          % (dur, "DAT" if DUR_MIN <= dur <= DUR_MAX else "TRUOT"))
    clip = float(np.max(np.abs(x)))
    print("    Dinh bien WAV: %.4f (%s)   DC offset: %.6f"
          % (clip, "OK (khong clip)" if clip < 0.999 else "CLIP", float(x.mean())))

    # ---------- 3. KHOANG CAM ----------
    sd = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(WAV),
                         "-af", "silencedetect=noise=%ddB:d=%.2f" % (abs(SIL_DB), SIL_MIN),
                         "-f", "null", "-"],
                        capture_output=True, text=True, errors="replace").stderr
    sils = []
    for ln in sd.splitlines():
        if "silence_start" in ln:
            sils.append([float(ln.split("silence_start:")[1].split(" ")[0]), None])
        elif "silence_end" in ln and sils and sils[-1][1] is None:
            sils[-1][1] = float(ln.split("silence_end:")[1].split(" ")[0])
    sils = [s for s in sils if s[1] is not None]
    print("\n[3] KHOANG CAM (trong file GOC VO, nguong -60 dB, >= %.1f s)" % SIL_MIN)
    print("    So khoang   : %d  (nhung gi: %d %s)"
          % (len(sils), len(sils),
             "-> can lop nen moi truong/SFX khi mix, hoac se vi pham A1/V4" if sils else "-> sach"))
    for st, en in sils:
        print("       %7.2f s -> %7.2f s  (%.2f s)" % (st, en, en - st))

    # ---------- 4. KHop TIMELINE vs SPEC ----------
    print("\n[4] KHOP TIMELINE vs SPEC")
    ids_tl = [l["id"] for l in tl]
    ids_sp = list(spec_lines.keys())
    print("    So cau        : timeline %d · spec %d · %s"
          % (len(tl), len(ids_sp), "KHOP" if ids_tl == ids_sp else "KHAC"))
    err_txt = err_vai = err_pause = 0
    rows = []
    for l in tl:
        s = spec_lines.get(l["id"])
        if not s:
            print("    ! cau khong co trong spec: %s" % l["id"])
            continue
        same_txt = l["text"].strip() == s["text"].strip()
        same_vai = l["vai"] == s["vai"]
        same_pause = abs(l["pause"] - s["pause_after"]) < 1e-6
        err_txt += not same_txt
        err_vai += not same_vai
        err_pause += not same_pause
        rows.append((l, s, same_txt, same_vai, same_pause))
    print("    Loi text %d · loi vai %d · loi pause %d  -> %s"
          % (err_txt, err_vai, err_pause,
             "0 LOI (G6 khop 100%)" if err_txt + err_vai + err_pause == 0 else "CO LOI"))

    # gap thuc te vs pause khai
    gap_bad = 0
    for i in range(len(rows) - 1):
        l1, _, _, _, _ = rows[i]
        l2 = rows[i + 1][0]
        gap = l2["start"] - l1["end"]
        if abs(gap - l1["pause"]) > 0.02:
            gap_bad += 1
            print("    ! gap %s->%s = %.2f s, khai %s" % (l1["id"], l2["id"], gap, l1["pause"]))
    print("    Gap ke giua cac cau: %d sai (nghi <= 0.02 s)" % gap_bad)

    # ---------- 5. NHIP DOC + F0 ----------
    print("\n[5] NHIP DOC + F0 THEO VAI")
    print("    %-11s %-3s %4s %6s %8s %9s %8s" %
          ("mau cau", "vai", "word", "dur(s)", "w/s", "F0(Hz)", "peak dB"))
    role_f0 = {}
    for l, s, *_ in rows:
        i0, i1 = int(l["start"] * sr), int(l["end"] * sr)
        seg = x[i0:i1]
        f0 = f0_median(seg, sr)
        pk = 20 * np.log10(max(float(np.max(np.abs(seg))), 1e-9))
        w = len(l["text"].split())
        dd = l["end"] - l["start"]
        role_f0.setdefault(l["vai"], []).append(f0)
        print("    %-11s %-3s %4d %6.2f %8.2f %9.1f %8.1f"
              % (l["id"], l["vai"], w, dd, w / dd, f0, pk))
    print("\n    F0 trung viet theo vai:")
    med = {}
    for r, v in role_f0.items():
        med[r] = float(np.median(v))
        print("      %s : %6.1f Hz  (%d cau)" % (r, med[r], len(v)))
    # G9: hai giong phai cach nhau >= 4 nua cung F0 trung viet (bat ky chieu nao)
    pairs = [("H", "D"), ("C", "H"), ("C", "D")]
    g9_min = 99.0
    for a_, b_ in pairs:
        if a_ in med and b_ in med:
            # semis() co dau theo chieu (f2/f1) -> lay tri tuyet doi de xet "cach nhau"
            s_ = abs(semis(med[a_], med[b_]))
            g9_min = min(g9_min, s_)
            print("      G9 %s vs %s : %5.2f nua cung  %s"
                  % (a_, b_, s_, "DAT" if s_ >= 4 else "TRUOT"))
    print("      G9 khoang cach nho nhat : %.2f nua cung ( yeu cau >= 4 )  -> %s"
          % (g9_min, "DAT" if g9_min >= 4 else "TRUOT"))

    # ---------- 6. NHIEU / DOI CHIEU ----------
    print("\n[6] NHIEU")
    seg = x[int(0.3 * sr):int(2.0 * sr)]
    print("    RMS 0.3-2.0 s : %.1f dBFS" % (20 * np.log10(max(float(np.sqrt(np.mean(seg ** 2))), 1e-9))))

    # ---------- 7. KET LUAN ----------
    print("\n" + "=" * 78)
    print("KET LUAN")
    print("=" * 78)
    ok = (TARGET_I[0] <= I <= TARGET_I[1] and tp <= MAX_TP
          and DUR_MIN <= dur <= DUR_MAX and err_txt == 0 and err_vai == 0
          and gap_bad == 0 and abs(d2 - dur) <= 0.05 and g9_min >= 4)
    print("  File           : %s" % WAV.name)
    print("  Do dai         : %.2f s" % dur)
    print("  Cau            : %d / %d" % (len(tl), len(ids_sp)))
    print("  Khop spec      : %s" % ("100%" if err_txt + err_vai == 0 else "CO LOI"))
    print("  G9 (>= 4 nc)   : %s (nho nhat %.2f nc)" % ("DAT" if g9_min >= 4 else "TRUOT", g9_min))
    print("  Clip co the dung ngay de dung video: %s" % ("CO" if ok else "XEM muc 3 (can lop nen)"))
    if sils:
        print("  CAN LAM TRUOC KHI DUNG:")
        print("   - %.0f khoang cam 0.5-0.7 s giua cac cau: bat buoc phai co lop nen moi truong/SFX")
        print("     khi mix (A1/V4) hoac cat ghep lai de thu ngan nhung doan nghi")
        print("   - nen/SFX lay tu .work/make_sfx.py (tu tong hop) hoac Freesound CC0")
        print("     -> KHONG dung 211 file SFX cua YouTube Audio Library (khong co license TikTok)")


if __name__ == "__main__":
    main()
