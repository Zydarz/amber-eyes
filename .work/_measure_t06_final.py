"""ĐO TOÀN BỘ số liệu thành phẩm Tap06 sau khi dựng lại — nguồn sự thật cho báo cáo.

Chạy sau: concat 12 part -> picture.mp4 -> package.mux() -> Tap06_master.mp4.
In số đo thật (không ước lượng). Mọi con số trong báo cáo/hồ sơ phải lấy từ đây.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("AE_EP", "06")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
BIN = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin"
FF = BIN / "ffmpeg.exe"
FP = BIN / "ffprobe.exe"
OUT = ROOT / "02_SAN_XUAT" / "Tap06" / "xuat_ban"
PICTURE = WORK / "video3_t06" / "picture.mp4"
MASTER = OUT / "Tap06_master.mp4"
MP3 = OUT / "Tap06_master.mp3"
SRT = OUT / "Tap06.srt"
TMP = WORK / "_qc_final_t06_v2"
TMP.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

R = {}


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", **kw)


def probe(p, extra=()):
    r = run([str(FP), "-v", "error", "-show_streams", "-show_format", *extra, "-of", "json", str(p)])
    return json.loads(r.stdout)


def main():
    tl = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
    R["timeline_total"] = tl["total"]
    R["frame_expected"] = int(tl["total"] * 30)

    # ---- picture.mp4 ----
    d = probe(PICTURE)
    v = next(s for s in d["streams"] if s["codec_type"] == "video")
    R["picture_size"] = PICTURE.stat().st_size
    R["picture_dur"] = float(d["format"]["duration"])
    R["picture_res"] = f'{v["width"]}x{v["height"]}'
    R["picture_fps"] = v["r_frame_rate"]
    R["picture_codec"] = v["codec_name"]
    rc = run([str(FP), "-v", "error", "-select_streams", "v:0", "-count_frames",
              "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", str(PICTURE)])
    R["picture_frames"] = int(rc.stdout.strip())

    # ---- master.mp4 ----
    d = probe(MASTER)
    v = next(s for s in d["streams"] if s["codec_type"] == "video")
    a = next(s for s in d["streams"] if s["codec_type"] == "audio")
    R["master_size"] = MASTER.stat().st_size
    R["master_dur"] = float(d["format"]["duration"])
    R["master_vdur"] = float(v["duration"])
    R["master_adur"] = float(a["duration"])
    R["master_res"] = f'{v["width"]}x{v["height"]}'
    R["master_fps"] = v["r_frame_rate"]
    R["master_vcodec"] = v["codec_name"]
    R["master_acodec"] = a["codec_name"]
    R["master_sha256"] = sha(MASTER)
    R["master_abr"] = a.get("bit_rate")
    R["master_vbr"] = v.get("bit_rate")
    R["av_dur_diff"] = abs(R["master_vdur"] - R["master_adur"])

    # ---- giai ma: loi ----
    r = run([str(FF), "-v", "error", "-i", str(MASTER), "-f", "null", "-"])
    errs = [L for L in r.stderr.splitlines() if L.strip()]
    R["decode_errors"] = len(errs)

    # ---- loudness tren CHINH file master ----
    r = run([str(FF), "-hide_banner", "-nostats", "-i", str(MASTER), "-af", "ebur128=peak=true",
             "-f", "null", "-"])
    m = re.findall(r"I:\s*(-?\d+(?:\.\d+)?)\s*LUFS", r.stderr)
    R["lufs"] = float(m[-1]) if m else None
    p = re.findall(r"Peak:\s*(-?\d+(?:\.\d+)?)\s*dBFS", r.stderr)
    R["true_peak"] = float(p[-1]) if p else None

    # ---- khoang lang ----
    r = run([str(FF), "-hide_banner", "-nostats", "-i", str(MASTER),
             "-af", "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"])
    R["silences"] = len(re.findall(r"silence_start", r.stderr))

    # ---- phu de ----
    raw = SRT.read_bytes()
    txt = raw.decode("utf-8-sig")
    R["srt_cues"] = len(re.findall(r"^\d+$", txt, re.M))
    R["srt_bytes"] = len(raw)
    R["srt_bom"] = raw[:3] == b"\xef\xbb\xbf"
    R["srt_nul"] = raw.count(0)
    R["srt_crlf"] = raw.count(b"\r\n")

    # ---- mo ta ----
    mo = OUT / "mo_ta.txt"
    if mo.exists():
        b = mo.read_bytes()
        R["mo_ta_chars"] = len(b.decode("utf-8-sig"))
        R["mo_ta_bom"] = b[:3] == b"\xef\xbb\xbf"
        R["mo_ta_nul"] = b.count(0)

    # ---- audio master wav ----
    R["audio_wav_dur"] = None
    wav = ED.w("audio_master.wav")
    if wav.exists():
        import wave
        with wave.open(str(wav), "rb") as wf:
            R["audio_wav_dur"] = round(wf.getnframes() / wf.getframerate(), 3)

    print(json.dumps(R, ensure_ascii=False, indent=2))
    (TMP / "measure_final.json").write_text(json.dumps(R, ensure_ascii=False, indent=2),
                                             encoding="utf-8")
    print(f"\n-> {TMP / 'measure_final.json'}")


if __name__ == "__main__":
    main()
