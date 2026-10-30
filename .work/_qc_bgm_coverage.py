# -*- coding: utf-8 -*-
"""QC độ phủ nhạc nền (BGM) cho 29 tập kênh Amber Eyes.

Đo gì:
  1. Mỗi tập dùng pattern bed nào (5 hồi) -> pattern nào bị lặp.
  2. File BGM nào trên đĩa được tham chiếu / không được dùng / thiếu.
  3. Số vòng loop thực tế của 1 file trong 1 hồi (dài tập ~25-30 phút).
  4. Từ khóa nhạc yêu cầu trong thẻ [BGM] của 29 kịch bản VN -> file nào đảm nhiệm.

Chạy:  py -3 .work/_qc_bgm_coverage.py
"""
import ast
import collections
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BGM_DIR = ROOT / "assets" / "bgm"

# ----------------------------------------------------------------- 1. bed theo tập
src = (WORK / "edition.py").read_text(encoding="utf-8")
ep_re = re.compile(r'^\s{4}"(\d\d)":\s*\{', re.M)
ep_pos = [(m.group(1), m.start(), m.end()) for m in ep_re.finditer(src)]

beds = {}
for i, (ep, _s, e) in enumerate(ep_pos):
    end = ep_pos[i + 1][1] if i + 1 < len(ep_pos) else len(src)
    chunk = src[e:end]
    b = chunk.find('"bed":')
    if b == -1:
        continue
    i0 = chunk.index("{", b)
    depth, j = 0, i0
    while j < len(chunk):
        if chunk[j] == "{":
            depth += 1
        elif chunk[j] == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    beds[ep] = ast.literal_eval(chunk[i0:j + 1])

print("=" * 78)
print("1) PATTERN BED (nhạc nền 5 hồi) CỦA 29 TẬP")
print("=" * 78)
patterns = collections.Counter()
for ep in sorted(beds):
    b = beds[ep]
    pat = tuple(sorted((int(k), v if isinstance(v, str) else tuple(v)) for k, v in b.items()))
    patterns[pat] += 1
print(f"Tập có cấu hình bed: {len(beds)}/29")
print(f"Số pattern khác nhau: {len(patterns)}\n")
for pat, n in patterns.most_common():
    desc = " | ".join(
        f"H{k}: {'+'.join(v) if isinstance(v, tuple) else v}" for k, v in pat)
    eps = [ep for ep in sorted(beds)
           if tuple(sorted((int(k), v if isinstance(v, str) else tuple(v))
                           for k, v in beds[ep].items())) == pat]
    print(f"  {n:>2} tập  {desc}")
    print(f"        -> Tập: {', '.join(eps)}")

print()
print("=" * 78)
print("2) FILE BGM TRÊN ĐĨA vs ĐƯỢC THAM CHIẾU")
print("=" * 78)
on_disk = {p.name for p in BGM_DIR.glob("*.mp3")}
used = set()
for ep, b in beds.items():
    for k, v in b.items():
        used.update([v] if isinstance(v, str) else list(v))
used.add("bgm_music_box.mp3")          # intro kênh, dùng trong build_audio3.py
print(f"Trên đĩa: {len(on_disk)} file")
print(f"Được dùng: {len(used)} file")
missing = sorted(used - on_disk)
unused = sorted(on_disk - used)
print(f"THIẾU (dựng sẽ lỗi): {missing if missing else 'không có'}")
print(f"ĐÃ TẢI NHƯNG KHÔNG DÙNG TRONG TẬP NÀO: {unused if unused else 'không có'}")

# ----------------------------------------------------------------- 3. số vòng loop
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
dur = {}
if FF.exists():
    import subprocess
    for p in sorted(BGM_DIR.glob("*.mp3")):
        out = subprocess.run([str(FF), "-v", "error", "-show_entries", "format=duration",
                              "-of", "csv=p=0", str(p)], capture_output=True, text=True)
        try:
            dur[p.name] = float(out.stdout.strip())
        except ValueError:
            pass

ACT_S = 310          # 1 hồi của tập 26-30 phút
print()
print("=" * 78)
print(f"3) SỐ VÒNG LOOP TRONG 1 HỒI (~{ACT_S} s) — dùng ffprobe")
print("=" * 78)
for name in sorted(dur, key=lambda n: dur[n]):
    loops = ACT_S / dur[name]
    flag = ""
    if loops >= 10:
        flag = "  <-- LẶP RÕ"
    elif loops >= 5:
        flag = "  <-- lặp vừa"
    print(f"  {name:<32} {dur[name]:7.2f} s   ~{loops:5.1f} vòng/hồi{flag}")

# ----------------------------------------------------------------- 4. thẻ [BGM] trong kịch bản
print()
print("=" * 78)
print("4) TỪ KHÓA NHẠC TRONG THẺ [BGM] CỦA 29 KỊCH BẢN VIỆT")
print("=" * 78)
KW = {
    "Cello": "bgm_cello_sad / cello_sad_v2",
    "cello": "bgm_cello_sad / cello_sad_v2",
    "Piano": "bgm_piano_minimal / _v2 / piano_warm",
    "Dương cầm": "bgm_piano_minimal / _v2 / piano_warm",
    "Violin": "bgm_violin_heart",
    "vĩ cầm": "bgm_violin_heart",
    "Ambient": "bgm_ambient_deep",
    "Drone": "bgm_sub_drone",
    "Sub": "bgm_sub_drone",
    "guitar": "bgm_guitar_acoustic_60s",
    "Guitar": "bgm_guitar_acoustic_60s",
    "Organ": "bgm_church_organ",
    "Synth": "bgm_piano_minimal (xem lại)",
    "music box": "bgm_music_box",
}
hits = collections.Counter()
n_tags = 0
n_files = 0
scripts = {}
for p in sorted((ROOT / "01_KICH_BAN").glob("Tap*/kichban_tap*.md")):
    if "REVIEW" in p.name:
        continue
    txt = p.read_text(encoding="utf-8")
    if "[BGM]" not in txt:
        continue
    n_files += 1
    for m in re.finditer(r"\*\*\[BGM\]:\*\*\s*(.+)", txt):
        n_tags += 1
        line = m.group(1)
        for kw in KW:
            if kw in line:
                hits[kw] += 1
                break
print(f"Số kịch bản VN đọc được: {n_files}")
print(f"Tổng thẻ [BGM]: {n_tags}")
print("\nTừ khóa nhạc và file đảm nhiệm:")
for kw, n in hits.most_common():
    print(f"  {n:>3} lần  {kw:<12} -> {KW[kw]}")
print()
print("File trên đĩa KHÔNG file nào đảm nhiệm:")
for n in sorted(on_disk):
    key = n.replace("bgm_", "").replace(".mp3", "")
    if not any(key.lower().split("_")[0] in kw.lower() for kw in KW):
        print(f"  - {n}")

# ----------------------------------------------------------------- 5. đối chiếu tài liệu chuẩn
print()
print("=" * 78)
print("5) ĐỐI CHIẾU BẢNG NHẠC NỀN THEO TẬP TRONG TÀI LIỆU CHUẨN vs edition.py")
print("=" * 78)
doc = ROOT / "02_SAN_XUAT" / "Danh_Sach_SFX_Tap03-29.md"
lines = doc.read_text(encoding="utf-8").splitlines()
ep_from = re.compile(r"01_KICH_BAN/Tap(\d\d)/")
doc_beds = {}
cur = None
for i, ln in enumerate(lines):
    m = ep_from.search(ln)
    if m:
        cur = m.group(1)
    if "**Nhạc nền / dải nền theo hồi:**" in ln and cur:
        # dòng ngay sau là mapping H1..H5
        for j in range(i + 1, min(i + 4, len(lines))):
            if "H1" in lines[j] and "→" in lines[j]:
                files = re.findall(r"bgm_[a-zA-Z0-9_]+(?:\.mp3)?", lines[j])
                doc_beds[cur] = [f if f.endswith(".mp3") else f + ".mp3" for f in files]
                break
print(f"Số tập có bảng nhạc nền trong tài liệu: {len(doc_beds)}\n")
mismatch = 0
for ep in sorted(doc_beds):
    want = doc_beds[ep]
    got = []
    for k in sorted(beds.get(ep, {}), key=int):
        v = beds[ep][k]
        got.extend([v] if isinstance(v, str) else list(v))
    # so sánh theo tập hợp file
    ok = set(want) == set(got)
    if not ok:
        mismatch += 1
        print(f"  Tập {ep}: KHÁC")
        print(f"      tài liệu: {', '.join(want)}")
        print(f"      edition : {', '.join(got)}")
print(f"\nTập lệch: {mismatch}/{len(doc_beds)}")

# ----------------------------------------------------------------- 6. đối chiếu từng hồi
print()
print("=" * 78)
print("6) ĐỐI CHIẾU TỪNG HỒI (H1..H5) — bảng chuẩn vs edition.py")
print("=" * 78)


def parse_doc_acts(line):
    """Chia dòng 'H1 ... → `x` · H2 ... → `y`' thành {hồi: [file bgm]}."""
    acts = {}
    for part in line.split("·"):
        m = re.match(r"\s*H(\d)\b(.*)", part)
        if not m:
            continue
        files = re.findall(r"bgm_[a-zA-Z0-9_]+(?:\.mp3)?", m.group(2))
        acts[int(m.group(1))] = [f if f.endswith(".mp3") else f + ".mp3" for f in files]
    return acts


bad = []
for ep in sorted(doc_beds):
    line = ""
    cur = None
    for i, ln in enumerate(lines):
        m = ep_from.search(ln)
        if m:
            cur = m.group(1)
        if cur == ep and "**Nhạc nền / dải nền theo hồi:**" in ln:
            for j in range(i + 1, min(i + 4, len(lines))):
                if lines[j].strip().startswith("H1"):
                    line = lines[j].strip()
                    break
            break
    want = parse_doc_acts(line)
    got = {}
    for k, v in beds.get(ep, {}).items():
        got[int(k)] = [v] if isinstance(v, str) else list(v)
    for act in range(1, 6):
        w = want.get(act, [])
        g = got.get(act, [])
        # chuẩn có thể ghi nhiều file cho 1 hồi (vd cello + sub_drone)
        if set(w) != set(g):
            bad.append((ep, act, w, g))
print(f"Tập có ít nhất 1 hồi lệch: {len({b[0] for b in bad})}/{len(doc_beds)}")
print(f"Tổng hồi lệch: {len(bad)}\n")
print(f"{'Tập':<6}{'Hồi':<6}{'Bảng chuẩn':<34}{'edition.py'}")
print("-" * 110)
for ep, act, w, g in bad:
    print(f"T{ep:<5}H{act:<5}{', '.join(w) or '(trống)':<34}{', '.join(g) or '(trống)'}")

print()
print("=" * 78)
print("7) TẬP ĐÃ CÓ ÂM THANH (bed đã khoá) vs TẬP CÒN MỞ")
print("=" * 78)
masters = sorted(p.name for p in (WORK).glob("audio_master*.wav"))
built = set()
for mn in masters:
    if mn == "audio_master.wav":
        built.add("01")
    m = re.search(r"_t(\d\d)\.wav$", mn)
    if m:
        built.add(m.group(1))
print(f"Đã có âm thanh: tập {sorted(built)}")
print(f"Chưa có âm thanh: tập {[e for e in sorted(beds) if e not in built]}")
print("→ Đổi bed tập chưa có âm thanh: KHÔNG phải dựng lại.")
print("→ Đổi bed tập đã có âm thanh: phải chạy lại build_audio3.py + ghép lại (hình không đổi).")


