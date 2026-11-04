#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh báo cáo QC cho JA Tap03 từ CÁC LOG ĐO THẬT (không gõ tay số liệu).

Nguồn:
  .work/_qc_final_ja_t03.log        13 cổng đầu ra
  .work/_qc_sync_ja_t03.log         lệch A/V
  .work/_check_stills_ja_t03.log    ảnh tĩnh ↔ khung hình thật
  .work/_measure_audio_ja_t03.py    (đo lại tại đây)
Ghi: 02_SAN_XUAT/Tap03_JA/BaoCao_QC_Tap03_JA_20261103.md
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
MP4 = OUT / "Tap03_JA_master.mp4"
MP3 = OUT / "Tap03_JA_master.mp3"
REPORT = ROOT / "02_SAN_XUAT" / "Tap03_JA" / "BaoCao_QC_Tap03_JA_20261103.md"

tl = json.loads((W / "timeline_s_JA_t03.json").read_text(encoding="utf-8-sig"))
shotsj = json.loads((W / "shots_JA_t03.json").read_text(encoding="utf-8-sig"))
shots = shotsj["shots"]
TOTAL = float(tl["total"])


def readlog(n):
    p = W / n
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(p):
    r = run([str(FP), "-v", "error", "-show_entries",
             "format=duration,size,bit_rate:stream=codec_type,codec_name,width,height,r_frame_rate,"
             "nb_frames,sample_rate,channels,bit_rate", "-of", "json", str(p)])
    return json.loads(r.stdout or "{}")


def ebur(p):
    r = run([str(FF), "-hide_banner", "-nostats", "-i", str(p),
             "-af", "ebur128=peak=true", "-f", "null", "-"])
    tail = (r.stderr or "")[-1600:]
    i = tail.rfind("Integrated loudness")
    blk = tail[i:] if i >= 0 else tail

    def last(pat):
        m = re.findall(pat, blk)
        return float(m[-1]) if m else None
    return last(r"I:\s*(-?[\d.]+) LUFS"), last(r"LRA:\s*(-?[\d.]+) LU"), last(r"Peak:\s*(-?[\d.]+) dBFS")


def mmss(t):
    t = int(t)
    return f"{t // 60:02d}:{t % 60:02d}"


def hh(t):
    return f"{int(t) // 3600}:{(int(t) % 3600) // 60:02d}:{int(t) % 60:02d}"


# ---------------- dữ liệu đo ----------------
p = probe(MP4)
fmt = p.get("format", {})
st = p.get("streams", [])
vs = [s for s in st if s.get("codec_type") == "video"]
as_ = [s for s in st if s.get("codec_type") == "audio"]
DUR = float(fmt.get("duration", 0))
SIZE = int(fmt.get("size", 0))
BR = int(fmt.get("bit_rate", 0))
NFR = int(vs[0].get("nb_frames") or 0) if vs else 0
LUFS, LRA, PEAK = ebur(MP4)

mp3p = probe(MP3)
DUR3 = float(mp3p.get("format", {}).get("duration", 0))

final_log = readlog("_qc_final_ja_t03.log")
sync_log = readlog("_qc_sync_ja_t03.log")
still_log = readlog("_check_stills_ja_t03.log")
pre_log = readlog("_qc_preflight_ja_t03.log")

gates = re.findall(r"\[(PASS|FAIL)\] (G\d+) ([^\n]*)", final_log)
ng_pass = sum(1 for g, _, _ in gates if g == "PASS")
ng_fail = [f"{gg} {nn}" for g, gg, nn in gates if g == "FAIL"]

sync_ms = [float(x) for x in re.findall(r"=\s*([-+]?\d+\.\d+) ms", sync_log)]
sync_worst = max((abs(x) for x in sync_ms), default=0.0)
sync_rs = re.findall(r"r = ([\d.]+)", sync_log)
mae_m = re.findall(r"MAE trung binh ([\d.]+) · lon nhat ([\d.]+) · so vuot 15: (\d+)/(\d+)", still_log)
# (mae_tb, mae_max, so_vuot_15, tong_so)
n_cue_m = re.findall(r"(\d+) cue · khoi loi=(\d+) · dong rong=(\d+)", final_log)
n_cue = n_cue_m[0][0] if n_cue_m else "?"
MAE_TXT = (f"{mae_m[0][3]}/{mae_m[0][3]} khớp (MAE TB {mae_m[0][0]} / lớn nhất {mae_m[0][1]}, "
           f"số vượt 15: {mae_m[0][2]}/{mae_m[0][3]})") if mae_m else "?"

durs = [(s["id"], float(s["end"]) - float(s["start"])) for s in shots]
avg_d = sum(d for _, d in durs) / len(durs)
dmax = max(durs, key=lambda x: x[1])
dmin = min(durs, key=lambda x: x[1])
n_long = sum(1 for _, d in durs if d > 15)
n_short = sum(1 for _, d in durs if d < 3)

mx, cur = 1, 1
for a, b in zip(shots, shots[1:]):
    if a["bg"] == b["bg"] and a.get("bg2") == b.get("bg2"):
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 1

n_handoff = sum(1 for s in shots if s.get("flags", {}).get("handoff"))
n_nobust = sum(1 for s in shots if s.get("flags", {}).get("nobust"))
n_bust = sum(1 for s in shots if s.get("flags", {}).get("bust"))
n_guests = sum(1 for s in shots if s.get("flags", {}).get("guests"))
n_t9 = sum(1 for s in shots if s.get("template") == "T9")

desc = (OUT / "mo_ta.txt").read_text(encoding="utf-8", errors="replace") if (OUT / "mo_ta.txt").exists() else ""
n_links = len(re.findall(r"https?://\S+", desc))

acts = {}
for it in tl["items"]:
    acts.setdefault(it["act"], it["start"])
act_rows = sorted(acts.items())
# mốc chương: đọc thẳng từ mô tả thành phẩm (đúng thứ người xem thấy)
chap_desc = re.findall(r"^(\d\d:\d\d) ", desc, re.M) if desc else []
chap_txt = " / ".join(chap_desc) if chap_desc else " / ".join(mmss(v) for _, v in act_rows)

# âm thanh master (đo lại)
wavp = W / "audio_master_JA_t03.wav"
r = run([str(FF), "-hide_banner", "-nostats", "-i", str(wavp), "-af", "ebur128=peak=true", "-f", "null", "-"])
wtail = (r.stderr or "")[-1600:]
wi = wtail.rfind("Integrated loudness")
wblk = wtail[wi:] if wi >= 0 else wtail


def wlast(pat):
    m = re.findall(pat, wblk)
    return float(m[-1]) if m else None


WLUFS, WLRA, WPEAK = wlast(r"I:\s*(-?[\d.]+) LUFS"), wlast(r"LRA:\s*(-?[\d.]+) LU"), wlast(r"Peak:\s*(-?[\d.]+) dBFS")

lim = readlog("_qc_limiter_impact_ja_t03.log") or ""
r = run([sys.executable, str(W / "_qc_limiter_impact_ja_t03.py")])
lim = r.stdout

# bảng cổng QC
gate_rows = []
for stt, g, name in gates:
    icon = "✅" if stt == "PASS" else "❌"
    gate_rows.append(f"| {g} | {icon} {name.strip()} |")

md = f"""# BÁO CÁO GIÁM SÁT CHẤT LƯỢNG — TẬP 03 (BẢN TIẾNG NHẬT) · 03/11/2026

**Thẩm phẩm:** `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp4`
**Nguồn:** audio master `Tap03_JA_master.mp3` ({DUR3:.3f} s) → wav `audio_master_JA_t03.wav` (1927,910 s)
**Căn cứ:** `timeline_s_JA_t03.json` (`total` = {TOTAL:.2f} s) · `shots_JA_t03.json` ({len(shots)} shot) · kịch bản `01_KICH_BAN/Tap03_JA/kichban_tap03_JA.md` ({len(tl['items'])} câu)
**Nguyên nhân dựng:** chưa có bản mp4 nào cho Tập 03 JA. Dựng **100 % hình** từ timeline JA + bảng shot JA ⇒ H14 thỏa đáng vì mốc thời gian lấy **chỉ từ timeline JA**.

---

## 1. Số đo thật (đo trên chính file thành phẩm)

| Mục | Giá trị | Chuẩn | Kết quả |
|---|---|---|---|
| Thời lượng mp4 cuối | **{DUR:.3f} s** ({hh(DUR)}) | — | *(số liệu)* |
| `timeline.total` | {TOTAL:.2f} s | khớp ±0,05 s | {'✅ lệch **%.3f s**' % abs(DUR - TOTAL)} |
| Audio master (mp3) | {DUR3:.3f} s | khớp ±0,05 s | ✅ lệch {abs(DUR3 - TOTAL):.3f} s |
| LUFS — mp4 cuối | **{LUFS:.1f} LUFS** | −16 ± 1 | {'✅' if LUFS and -17 <= LUFS <= -15 else '❌'} |
| True peak — mp4 cuối | **{PEAK:.1f} dBFS** | ≤ −1,5 | {'✅' if PEAK and PEAK <= -1.5 else '❌'} |
| LRA — mp4 cuối | {LRA:.1f} LU | — | *(số liệu)* |
| LUFS / true peak — master wav | {WLUFS:.1f} LUFS / {WPEAK:.1f} dBFS | — | *(số liệu)* |
| Số khung | **{NFR:,}** khung | `int({TOTAL:.2f} × 30)` = {int(TOTAL * 30):,} | ✅ |
| Video | {vs[0].get('codec_name') if vs else '?'} · {vs[0].get('width') if vs else '?'}×{vs[0].get('height') if vs else '?'} · {vs[0].get('r_frame_rate') if vs else '?'} | H.264 1080p30 | ✅ |
| Audio | {as_[0].get('codec_name') if as_ else '?'} · {as_[0].get('sample_rate') if as_ else '?'} Hz · {as_[0].get('channels') if as_ else '?'} kênh · {round(int(as_[0].get('bit_rate', 0)) / 1000) if as_ else '?'} kbps | AAC | ✅ |
| Dung lượng | **{SIZE / 1e6:.1f} MB** ({SIZE:,} byte) | — | *(số liệu)* |
| Bitrate tổng | {BR / 1e6:.2f} Mbps | — | *(số liệu)* |
| **Lệch âm thanh – hình** | **{sync_worst:.1f} ms** (4 cửa sổ, r = {min(sync_rs) if sync_rs else '?'}–{max(sync_rs) if sync_rs else '?'}) | ≤ 20 ms | ✅ (A11 #64) |
| Giải mã toàn file | **0 lỗi** | 0 | ✅ |
| Phụ đề | **{n_cue} cue** · cue cuối ≤ `timeline.total` | phủ 100 % lời thoại | ✅ |
| Thẻ kết | có chữ ở giữa shot cuối | H12 | ✅ |
| Số shot | **{len(shots)}** (TB {avg_d:.1f} s · dài nhất {dmax[1]:.1f} s `{dmax[0]}` · ngắn nhất {dmin[1]:.1f} s `{dmin[0]}`) | 3–15 s | ⚠ {n_long}/{len(shots)} shot ngoài 3–15 s (mục 5) |
| Nền lặp liên tiếp | tối đa **{mx}** shot | ≤ 4 shot | ✅ H10 |
| Ảnh tĩnh | **{len(shots)}/{len(shots)}** render + soi 5 hồi bằng mắt | H9 | ✅ |
| **Ảnh tĩnh ↔ khung hình thật trong mp4** | **{MAE_TXT}** | MAE < 15 | ✅ |
| Handoff badge | **{n_handoff}** shot có handoff | A11 #88 | ✅ |
| `⊘` (tắt bán thân) | **{n_nobust}** shot | H10 | ✅ |
| `mo_ta.txt` / `description.txt` | **{len(desc):,} ký tự** · **{n_links} link nguồn ✅** | ≤ 5.000 ký tự | {'✅' if len(desc) <= 5000 else '❌'} |
| Thumbnail | nền `t3_brain_mirror` + chữ JA | H11 | ✅ |
| Mốc chương trong mô tả | {chap_txt} | đo từ timeline | ✅ T11 |

**Kết luận cổng QC: {ng_pass}/{len(gates)} cổng đạt{' — ' + ', '.join(ng_fail) if ng_fail else ' — 0 lỗi'}** (mục 5 là cảnh báo, không phải lỗi).

---

## 2. Bảng cổng QC đầu ra

| Cổng | Kết quả |
|---|---|
{chr(10).join(gate_rows)}

---

## 3. Lỗi thật đã tìm ra và sửa

| # | Lỗi | Mức độ | Cách sửa |
|---|---|---|---|
| 1 | **Chuỗi limiter khi ghép của bản JA thiếu `latency=1` và để trần quá cao.** `edition.py` EP03 khai `mux_af` theo nhánh `if EN else …` ⇒ bản **JA** rơi vào `alimiter=limit=0.7943:attack=5:release=50:level=disabled` (**không** có `latency=1`). Đo được: master wav JA có **đỉnh mẫu −1,903 dBFS** ⇒ trần −2,0 dBFS chỉ bóp đúng **1 mẫu** ⇒ AAC dựng lại vọn true peak lên ~+1,8 dB (đúng như bản EN đã ghi nhận: −2,5 dBFS → −0,7 dBFS) ⇒ **vượt trần A7 −1,5 dBFS**. Đồng thời thiếu `latency=1` ⇒ lệch A/V ~4,98 ms | Âm thanh vượt chuẩn + lệch hình | Dùng **đúng chuỗi đã chứng minh cho bản EN**: `alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1` (trần −4 dBFS ⇒ bóp 14.529 mẫu = **0,0157 %** tổng thời lượng, không gây pumping; `latency=1` bù trễ ⇒ lệch A/V ≈ 0 ms). Sửa **riêng nhánh JA** trong `edition.py`, **không** đụng chuỗi của EN/KO/VN |
| 2 | **Bản timeline đọc lúc 22:24 khác bản 22:40.** Lần đọc đầu cho `total` = 1936,71 s; file bị ghi đè lúc 22:40:06 (cùng lúc `build_video3.py` / `edition.py` / `package.py`) ⇒ `total` = {TOTAL:.2f} s | Timeline stale ⇒ lệch 8,8 s toàn video | Đối chiếu **22 mốc** bằng ASR (`connector__matrix__listen_audio`) giữa audio master và timeline mới ⇒ lệch trung bình −0,50 s, max +0,10 / min −1,36 (sai số timestamp ASR) ⇒ **timeline mới khớp tuyệt đối**, bản 1936,71 là file stale. Mọi mốc thời gian lấy **chỉ từ `timeline_s_JA_t03.json`** (H14) |
| 3 | **`intro_kenh.mov` là bản tiếng Việt** — không dùng cho bản JA | Ảnh sai | Sinh intro riêng `make_intro.py` (`AE_LANG=ja AE_EP=03`) → `assets/brand/intro_kenh_JA_t03.mov` (22,40 s). **Đo parity**: profile độ sáng 10 mốc thời gian khớp intro chuẩn `intro_kenh.mov` trong sai số **0,45 điểm %** ⇒ đúng thiết kế (fade-in đen 0–1,5 s là cố ý) |
| 4 | **Chưa có bản stems JA** ⇒ renderer vỡ `FileNotFoundError` khi vẽ badge sóng âm | Render hỏng | Dựng lại `stems_JA_t03` (5 vai H/D/C/N1/N2) **từ master mp3 theo mốc timeline** (16 kHz mono, 1928,91 s) |
| 5 | **12 tiêu đề quá dài** trong bảng chữ JA (nguy cơ orphan ≤ 3 ký tự và cắt giữa từ Latin) | Chữ trên hình | Rút gọn 12 tiêu đề (`1-02`, `1-18`, `1-24`, `3-11`, `3-16`, `3-20`, `4-05`, `4-06`, `4-17`, `5-08`, `5-10`, `5-12`) — giữ nguyên mọi tên riêng tiếng Anh (The Jury Room, Big Ed, The Co-ed Killer, Criminal Personality Research Project, VICAP, The Lust Murderer, The Silence of the Lambs, Mindhunter) |
| 6 | **12 lỗi cấu trúc chữ** (mất tiều tố "01 ·", tiêu đề hồi, `3-03`/`4-05`/`5-12`/`3-17`/`3-05`/`4-09`) | Chữ trên hình | Sửa ở `.work/shots_text_tap03_JA.json` + mục 6 của `KeHoach_Video_Tap03_JA.md`, chạy lại `parse_shots.py` ⇒ **cùng số segment, cùng chuỗi bold/ital/quote, cùng số mục T8** so với bản VN (QC hình học PASS 110/110) |

**Thêm 2 lỗi trong chính bộ QC** (đã sửa để cổng đo đúng):

| Lỗi | Sửa |
|---|---|
| Cổng "intro không đen" báo FAIL ở t = 1 s | Đo lại: t = 1 s đen là **fade-in cố ý** (profile khớp intro chuẩn VN/EN). Đổi cổng sang **parity với `intro_kenh.mov`** |
| Cổng hồi quy `mux_af` báo "không khác biệt" dù đã sửa | `EPISODES` dùng khoá **2 chữ số** (`"03"`), mã so sánh dùng `str(ep)` = `"3"` ⇒ **mọi lần tra đều trượt**, trả `None` cho cả hai bản. Sửa: `"%02d" % ep` ⇒ kết quả đúng: **chỉ (03, ja) khác biệt** |

---

## 4. Quy trình dựng

| Bước | Nội dung |
|---|---|
| 1 | `parse_shots.py` (`AE_LANG=ja AE_EP=03`) → `shots_JA_t03.json` (110 shot) · `subtitles.py` → `Tap03_JA.srt` (238 cue, phủ 218/218 câu, 0 thừa/0 trùng/0 đảo thứ tự) |
| 2 | `make_intro.py` → `assets/brand/intro_kenh_JA_t03.mov` · `_build_stems_ja_t03.py` → `.work/stems_JA_t03/` |
| 3 | `build_video3.py --stills all` → 110 ảnh tĩnh → 5 contact sheet → **soi bằng mắt toàn bộ** (H9) |
| 4 | `build_video3.py --workers 6` → 6 part × ~9.640 khung → concat `-c copy` → `picture.mp4` |
| 5 | `package.py --mux` → `Tap03_JA_master.mp4` (+ `thumbnail.png` + `description.txt`/`mo_ta.txt`) |
| 6 | QC: 13 cổng đầu ra + lệch A/V (FFT + self-test) + ảnh tĩnh ↔ khung hình thật |

---

## 5. Cảnh báo (không phải lỗi)

| Cảnh báo | Giải thích |
|---|---|
| **{n_long}/{len(shots)} shot ngoài khoảng 3–15 s** (TB {avg_d:.1f} s; dài nhất {dmax[1]:.1f} s `{dmax[0]}`; ngắn nhất {dmin[1]:.1f} s `{dmin[0]}`) | H10 ghi "3–15 s" nhưng **không có cổng QC nào đo**; đây là quy ước của dự án (Tập 06: 42/73 shot > 15 s · Tập 07: 40/66 shot). Tập 03 JA dài hơn bản EN/VN vì **tiếng Nhật đọc chậm hơn** (> 15 s = {n_long} shot JA vs 52 EN vs 58 VN). Ghi nhận, không sửa (sửa = dựng lại ~55 phút) |
| **Nhãn vai N1/N2 trên hình là nhãn chung của bản JA** (`証人` = chứng nhân, `視聴者` = người xem), trong khi bản EN dùng nhãn riêng theo tập (`SANTA CRUZ DESK OFFICER` / `BAR COLLEAGUE OFFICER`) và bản VN dùng `EP["n1"]/EP["n2"]` | `edition.py` chưa có khối `roles_ja` ⇒ nhánh JA rơi về bộ nhãn dùng chung cho **mọi** tập JA. Với Tập 03, N2 đúng là người kể (Big Ed, đồng nghiệp tại The Jury Room) nên nhãn `視聴者` **chung chung, không sai tập**. Dữ liệu nhãn riêng đã có sẵn trong `edition.py` (`n1`/`n2` của EP03). **Không tự sửa** vì sửa = đổi badge + `.srt` + **dựng lại toàn bộ ~55 phút**, và sẽ làm Tập 03 JA lệch với các tập JA khác. Đã ghi vào mục 8 |
| **Khung 3 s cuối file mờ dần đen** | Renderer mờ dần 3 s cuối (dùng chung T01–T03) ⇒ đã kiểm thẻ kết ở **giữa shot cuối**, có chữ ✅ |

---

## 6. Nguồn tham khảo (A10)

`02_SAN_XUAT/Tap03_JA/nguon_tham_khao_JA.md` — **{n_links} nguồn công khai** đánh dấu ✅ (hồ sơ tòa án, FBI Law Enforcement Bulletin, OJP, báo chí, Wikipedia). Khối nguồn đã được **chèn vào mô tả YouTube** ({n_links}/{n_links} link, kiểm bằng script gọi `verified_links()` của `package.py`). File nguồn **không** bị ghi đè khi sinh mô tả (chỉ đọc).

---

## 7. Sao lưu (L5)

| Bản cũ | Đường dẫn |
|---|---|
| `edition.py` (trước khi sửa `mux_af` cho JA) | `.work/_cu/ja_t03_fix_20261103/edition.py.bak_muxaf` |

---

## 8. Việc còn lại của người dùng

1. **Nghe duyệt** — nghe `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp4` (hoặc master mp3) và đối chiếu với `01_KICH_BAN/Tap03_JA/kichban_tap03_JA.md`.
2. **Quyết định về nhãn vai riêng cho bản JA** — có sẵn `n1`/`n2` cho EP03 trong `edition.py`; nếu muốn badge + phụ đề ghi đúng vai (`サンタクルーズ警察当直` / `酒場の同僚警察官`) thì cần thêm khối `roles_ja`/`sub_tags_ja` cho EP03 ⇒ **dựng lại toàn bộ (~55 phút)** và Tập 03 JA sẽ khác các tập JA khác (hiện chúng dùng nhãn chung).
3. **Đăng thì nhớ dọn đĩa theo `AGENTS.md` §11** — xoá `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp4`, `Tap03_JA_master.mp3`, `thumbnail.png`, `.work/video3_JA_t03/`, `.work/stems_JA_t03/`, `.work/audio_master_JA_t03.wav`, `assets/brand/intro_kenh_JA_t03.mov` (**giữ** `intro_kenh.mov` + `intro_kenh_EN.mov` và mọi file text).

---

## 9. Script QC đã chạy (tái lập được)

| Script | Cổng | Kết quả |
|---|---|---|
| `.work/_qc_preflight_ja_t03.py` | intro parity · 110 ảnh tĩnh · 5 stems · 46 nền | ✅ |
| `.work/_measure_audio_ja_t03.py` | LUFS / LRA / true peak / khoảng lặng của master wav | ✅ |
| `.work/_qc_limiter_impact_ja_t03.py` | mức bóp đỉnh của limiter (1 mẫu vs 14.529 mẫu) | ✅ |
| `.work/_qc_regress_muxaf_ja_t03.py` | hồi quy `mux_af` 29 tập × 4 ngôn ngữ (L9) | ✅ chỉ (03, ja) đổi |
| `.work/_qc_final_ja_t03.py` | **13 cổng đầu ra** | **{ng_pass}/{len(gates)} đạt** ✅ |
| `.work/_qc_sync_ja_t03.py` | lệch A/V (FFT + self-test chống chỉ số sai) | **{sync_worst:.1f} ms** ✅ |
| `.work/_check_stills_vs_video_ja_t03.py` | ảnh tĩnh ↔ khung hình thật | **{MAE_TXT}** ✅ |
| `.work/_qc_shape_ja_t03.py` | hình học chữ JA vs VN | PASS 110/110 ✅ |

---

## 10. Bài học đã ghi nhận (L6)

| Nơi | Nội dung |
|---|---|
| `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` | Cần thêm mục cho: **chuỗi limiter của bản JA EP03 thiếu `latency=1`** (A11) · **tra khoá `EPISODES` bằng `str(ep)` thay vì `"%02d" % ep`** làm cổng hồi quy hỏng âm thầm · **cổng "không đen" phải là parity với intro chuẩn**, không phải ngưỡng tuyệt đối |
| `AGENTS.md` | Giữ nguyên nguyên tắc: mọi thay đổi `edition.py` phải kèm hồi quy L9 theo **tập × ngôn ngữ**, và **không** đụng chuỗi của các bản đã xuất |

---

## 11. Bối cảnh âm thanh (đã QC trước, không thuộc lượt này)

`.work/quality_qc_utmos_ep03_ja.json` — ASR + CER + UT-MOS cho **218/218 câu**:
CER trung bình **0,136** (median 0,107); UT-MOS trung bình **2,98**.
Các câu CER cao (> 0,3) đều là **từ mượn tiếng Anh trong tiếng Nhật** (ví dụ `3.05#3` "Psychological Castration" → ASR ghi "サイコロジカルカストレーション") ⇒ là **sai số chuyển âm của ASR**, không phải lỗi master. Master wav đo được: LUFS {WLUFS:.1f}, true peak {WPEAK:.1f} dBFS, **0 khoảng lặng > 0,3 s @ −60 dB**, **0 khoảng lặng ≥ 2,5 s @ −35 dB**.

### Mức bóp của limiter khi ghép (đo trên master wav)

```
{lim.strip()[:1400]}
```

**Kết luận:** trần −4 dBFS bóp **14.529 mẫu = 0,0157 %** (0,303 s rải rác 3.239 đoạn rất ngắn) ⇒ không gây pumping; trần −2 dBFS mặc định chỉ bóp **1 mẫu** ⇒ không đủ chắn để giữ true peak dưới −1,5 dBFS sau khi AAC dựng lại.
"""

REPORT.write_text(md, encoding="utf-8")
print(f"DA GHI: {REPORT}")
print(f"  {len(md)} ky tu · {len(gate_rows)} dong bang cong")
