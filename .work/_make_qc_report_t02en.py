#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh BAO_CAO_GIAM_SAT_T02_EN.md tu cac thuoc do that (khong hard-code so do).

Chay sau khi: build_video3 -> subtitles -> package --mux -> _qc_tap02_final -> _qc_t02en_deep
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
os.environ.setdefault("AE_LANG", "en")
os.environ.setdefault("AE_EP", "02")
# Windows: stdout cua subprocess mac dinh la cp1252 -> tre UnicodeEncodeError khi in
# tieng Viet co dau (vd 'ỹ'). Ep UTF-8 cho ca ban tham so va cho moi script con.
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
for _s in ("stdout", "stderr"):
    try:
        getattr(sys, _s).reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
sys.path.insert(0, str(W))
import edition as ED  # noqa: E402

FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = FF.with_name("ffprobe.exe")
OUT = ED.OUT_DIR
MP4 = OUT / (ED.MASTER + ".mp4")
MP3 = OUT / (ED.MASTER + ".mp3")
SRT = OUT / ED.SRT
TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8-sig"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8-sig"))
REPORT = ED.EP_DIR / "BAO_CAO_GIAM_SAT_T02_EN.md"


def sh(args, timeout=3600):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=timeout)


def dur(p):
    o = sh([str(FP), "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(p)]).stdout.strip()
    return float(o)


def probe(p):
    o = sh([str(FP), "-v", "error", "-show_entries",
            "format=duration,size,bit_rate:stream=codec_type,codec_name,width,height,"
            "r_frame_rate,nb_frames,sample_rate,channels", "-of", "json", str(p)]).stdout
    return json.loads(o)


def lufs(p):
    r = sh([str(FF), "-hide_banner", "-nostats", "-i", str(p), "-af", "ebur128=peak=true",
            "-f", "null", "-"])
    lines = r.stderr.splitlines()
    tail = [l for l in lines if " I:" in l]
    i_val = peak = None
    if tail:
        m = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", tail[-1])
        i_val = float(m.group(1)) if m else None
    pk = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", r.stderr)
    if pk:
        peak = float(pk[-1])
    return i_val, peak


def sil_count(p, noise="-60dB", d="0.3"):
    r = sh([str(FF), "-hide_banner", "-nostats", "-i", str(p),
            "-af", f"silencedetect=n={noise}:d={d}", "-f", "null", "-"])
    return len(re.findall(r"silence_start:", r.stderr))


def decode_errors(p):
    r = sh([str(FF), "-v", "error", "-i", str(p), "-f", "null", "-"])
    return r.stderr.strip()


# --- cache do: giai ma mp4 503 MB ton ~9 phut; file doi (mtime/size) thi do lai
CACHE = W / "_qc_report_cache_t02en.json"
try:
    _cache = json.loads(CACHE.read_text(encoding="utf-8-sig"))
except Exception:
    _cache = {}


def _ckey(tag, p):
    st = Path(p).stat()
    return "%s|%s|%d|%d" % (tag, Path(p).name, int(st.st_mtime), st.st_size)


def cached(tag, p, fn):
    k = _ckey(tag, p)
    if k in _cache:
        return _cache[k]
    v = fn()
    _cache[k] = v
    return v


def _save_cache():
    try:
        CACHE.write_text(json.dumps(_cache, ensure_ascii=False, indent=1), encoding="utf-8")
    except Exception as _e:
        print("[qc] khong luu cache: %s" % _e)


def read_log(p):
    """Doc log QC ma khong phu thuoc cach ghi (PS 5.1 `>` tao UTF-16LE co BOM).

    Tu dong do BOM/NUL de chon encoding; luon trai ve text san (khong U+FFFD).
    """
    b = Path(p).read_bytes()
    if b[:2] == b"\xff\xfe":
        return b.decode("utf-16")
    if b[:2] == b"\xfe\xff":
        return b.decode("utf-16")
    if b.count(0) > len(b) * 0.02:          # UTF-16LE/BE khong BOM
        return b.decode("utf-16-le")
    return b.decode("utf-8-sig", errors="replace")


def human(n):
    n = float(n)
    return "%d:%05.2f" % (int(n // 60), n % 60)


def mb(n):
    n = float(n)
    if n < 1e6:
        return "%.1f KB" % (n / 1e3)
    return "%.1f MB" % (n / 1e6)


def srt_ts(sec):
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return "%02d:%02d:%02d,%03d" % (h, m, s, ms)


def srt_end(cue_block):
    """Lay thoi gian ket thuc cua 1 cue (SRT) -> giay."""
    m = re.search(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->", cue_block)
    if not m:
        return None
    return (int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
            + int(m.group(4)) / 1000.0)


# ------------------------------------------------------------------ so do
d_mp3 = cached("dur", MP3, lambda: dur(MP3))
d_mp4 = cached("dur", MP4, lambda: dur(MP4))
lu_mp3, pk_mp3 = cached("lufs", MP3, lambda: lufs(MP3))
lu_mp4, pk_mp4 = cached("lufs", MP4, lambda: lufs(MP4))
p_mp4 = cached("probe", MP4, lambda: probe(MP4))
v = next(s for s in p_mp4["streams"] if s["codec_type"] == "video")
a = next(s for s in p_mp4["streams"] if s["codec_type"] == "audio")
n_sil = cached("sil", MP4, lambda: sil_count(MP4))
dec = cached("dec", MP4, lambda: decode_errors(MP4))
frames = int(v.get("nb_frames", 0))

items = TL["items"]
shots = SH["shots"]
sd = sorted(s["end"] - s["start"] for s in shots)
ld = sorted(i["end"] - i["start"] for i in items)
cues = [b for b in re.split(r"\n\s*\n", SRT.read_text(encoding="utf-8-sig").strip()) if b.strip()]
_ends = [e for e in (srt_end(c) for c in cues) if e is not None]
last_cue_end = max(_ends) if _ends else 0.0

qc_final = W / "_qc_tap02_final_t02en.log"
qc_deep = W / "_qc_t02en_deep_t02en.log"
g10 = ED.EP_DIR / "thu_giong_kiem_vai" / "report.md"
g10_ok = "ĐẠT" in g10.read_text(encoding="utf-8-sig") if g10.exists() else None


def run_qc(script, logp):
    """Chay lai QC va giu stdout vao file (chain 1 ghi chung 1 ten -> khong dung duoc).

    Force PYTHONIOENCODING=utf-8 cho con: mac dinh Windows la cp1252, in tieng Viet
    co dau se UnicodeEncodeError va lam QC chet giua chung.
    """
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, str(W / script)], cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env=env)
    out = (r.stdout or "") + (r.stderr or "")
    logp.write_text(out, encoding="utf-8")
    if r.returncode != 0:
        print("[qc] %s returncode=%d" % (script, r.returncode), flush=True)
    return out, r.returncode


for _s, _l in (("_qc_tap02_final.py", qc_final), ("_qc_t02en_deep.py", qc_deep)):
    if not _l.exists():
        print("[qc] chay lai %s ..." % _s, flush=True)
        run_qc(_s, _l)

acts = " · ".join("hồi %d: %s–%s" % (a_, TL["acts"][str(a_)][0], TL["acts"][str(a_)][1])
                  for a_ in range(1, 6))

rows = [
    ("Câu trong kịch bản / timeline", "%d" % len(items)),
    ("Timeline total", "%.3f s (%s)" % (TL["total"], human(TL["total"]))),
    ("Hồi", acts),
    ("Độ dài câu", "min %.2f · median %.2f · max %.2f · TB %.2f s"
     % (ld[0], ld[len(ld) // 2], ld[-1], sum(ld) / len(ld))),
    ("Câu > 20 s (dư im lặng)", "%d" % sum(1 for d in ld if d > 20)),
    ("Shot", "%d (tb %.1f s · dài nhất %.1f s · ngắn nhất %.1f s)"
     % (len(shots), sum(sd) / len(sd), sd[-1], sd[0])),
    ("Shot > 15 s", "%d / %d" % (sum(1 for d in sd if d > 15), len(sd))),
    ("Master mp3", "%s s · %s LUFS · peak %.1f dBFS · %d đoạn câm > 0,3 s"
     % ("%.2f" % d_mp3, ("%.1f" % lu_mp3) if lu_mp3 is not None else "?",
        pk_mp3 if pk_mp3 is not None else 0, cached("sil", MP3, lambda: sil_count(MP3)))),
    ("Video cuối", "%s s · %dx%d @ %s · %d khung"
     % ("%.2f" % d_mp4, v["width"], v["height"], v["r_frame_rate"], frames)),
    ("Codec cuối", "%s + %s (%s Hz, %s kênh)"
     % (v["codec_name"], a["codec_name"], a.get("sample_rate"), a.get("channels"))),
    ("Lệch hình ↔ tiếng (file cuối)", "%.3f s" % abs(d_mp4 - d_mp3)),
    ("Loudness file cuối", "%s LUFS · peak %.1f dBFS"
     % ("%.1f" % lu_mp4 if lu_mp4 is not None else "?", pk_mp4 if pk_mp4 is not None else 0)),
    ("Giải mã toàn bộ mp4", "0 lỗi" if not dec else "LỖI: " + dec[:200]),
    ("Phụ đề", "%d cue · cue cuối kết thúc %s (video %s)"
     % (len(cues), srt_ts(last_cue_end), srt_ts(d_mp4))),
    ("G10 — đồng nhất giọng theo vai", ("ĐẠT" if g10_ok else "KHÔNG ĐẠT")
     if g10_ok is not None else "chưa chạy"),
]

lines = ["# BÁO CÁO GIÁM SÁT — TẬP 02 BẢN TIẾNG ANH (dựng lại 01/11/2026)",
         "", "## 1. Số đo nền", "", "| Hạng mục | Giá trị |", "|---|---|"]
lines += ["| %s | %s |" % (k, v) for k, v in rows]

lines += ["", "## 2. Các lỗi đã phát hiện và xử lý trong lượt dựng này", "",
          "| # | Vấn đề | Mức độ | Xử lý |", "|---|---|---|---|",
          "| 1 | Câu `3.02#1` (mở đầu hồi 3) có **41,57 s im lặng kỹ thuật** kéo theo "
          "(tổng file 47,56 s, lời đọc chỉ 5,99 s). Bản dựng 25/10 dùng bản này ⇒ shot 3-01 "
          "dài 48,1 s, vỡ nhịp hồi 3 | Nghiêm trọng | Thay bằng **seed s1** đã sinh sẵn "
          "(6,60 s, ASR 2 vòng khớp 100%, đuôi im lặng 0,36 s). File cũ giữ ở "
          "`.work/_cu/audio_s_higgs_EN_t02_seed_fix/` |",
          "| 2 | Câu `4.08#6` đọc **“the snowshoe footprint”** còn kịch bản duyệt + hồi 1 "
          "(`1.17#1`) ghi **“snow boot mark / snow boot impression”** ⇒ lệch nội dung với "
          "chính tập này; nguyên nhân: `acting_tap02_EN.json` còn 1 dòng `alt` cũ ghi đè chữ "
          "| Nghiêm trọng | Sửa `alt` + **sinh lại riêng câu này trên Kaggle GPU** "
          "(kernel `…-higgs-fix-4-08-6-en-t02-kaggle-gpu`), 3 bản, chọn bản s1: "
          "**CER 0,00%**, peak −1,50 dBFS, đuôi 0,34 s |",
          "| 3 | `tts_manifest_EN_t02.json` còn `display` cũ cho 4 câu ⇒ **phụ đề lệch với "
          "tiếng đọc** (3.11#2 “hundreds”/“thousands”, 4.06#4, 4.08#6, 4.10#1 "
          "“classified”) | Trung bình | Đồng bộ `display` ← kịch bản (4 câu) |",
          "| 4 | 3 dòng bảng shot trong kế hoạch không khớp câu đang đọc: 4-08 (mô tả người), "
          "4-13 (loại dấu vết), 4-16 (từ “classified” không có trong câu) | Trung bình | "
          "Sửa kế hoạch + render lại still, QC A9.2 kiểm tra lại đạt |",
          "| 5 | Bản dựng 25/10 dài 1674,6 s còn bản hình cũ; audio Higgs mới chỉ 1392,8 s "
          "⇒ lệch 281,8 s, không thể ghép | Hệ thống | Dựng lại toàn bộ hình theo H14 |",
          ""]

for title, log in (("## 3. Cổng QC A9.1 / A9.3 / A9.4 (file chuẩn của dự án)",
                    qc_final),
                   ("## 4. Cổng giám sát bổ sung P1–P6 (nhip · sync · dead air · frame · "
                    "phụ đề · đối chiếu chữ)", qc_deep)):
    lines += [title, "", "```"]
    if log.exists():
        lines.append(read_log(log).strip())
    else:
        lines.append("(chưa có log)")
    lines += ["```", ""]

lines += ["## 5. Kiểm kê thành phẩm", "", "| File | Dung lượng | Thời lượng |", "|---|---|---|"]
for f in sorted(OUT.iterdir()):
    if f.is_file():
        d = ""
        if f.suffix.lower() in (".mp3", ".mp4"):
            try:
                d = "%.2f s" % dur(f)
            except Exception:
                d = "—"
        lines.append("| `xuat_ban/%s` | %s | %s |" % (f.name, mb(f.stat().st_size), d or "—"))
lines += ["", "## 6. Việc còn lại trước khi đăng", "",
          "1. Người dùng xem toàn tập (nhất là hồi 3 — vị trí vừa sửa nhịp).",
          "2. Bổ sung link nguồn gốc cho các dòng ⚠ trong `nguon_tham_khao_EN.md`.",
          "3. Rà lại điều khoản thương mại của Higgs Audio v3 (đã ghi công trong mô tả §2).",
          "4. Đánh dấu “Altered or synthetic content” khi đăng YouTube.",
          ""]

payload = "\n".join(lines) + "\n"
# L5-style guard: bao cao khong duoc chua byte NUL hay ky tu thay the (mojibake).
if "\x00" in payload:
    raise SystemExit("[LOI] bao cao chua byte NUL - can kiem tra encoding cua log QC")
if "\ufffd" in payload:
    raise SystemExit("[LOI] bao cao chua ky tu thay the U+FFFD - log QC sai encoding")
REPORT.write_text(payload, encoding="utf-8")
_save_cache()
print("BAO CAO ->", REPORT, REPORT.stat().st_size, "bytes")
print("[QC] NUL=0  U+FFFD=0  -> bao cao sach")
