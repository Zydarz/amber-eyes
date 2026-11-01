"""Vá bed nhạc nền Tập 04 theo A10 — y hệt cách Tập 03 đã vá 31/10/2026.

A10: bed nhạc nền phải KHỚP KỊCH BẢN, mỗi hồi lấy mood thẻ [BGM] đầu hồi.
Tập 04 vi phạm 2 slot (kiểm bằng `py -3 .work/_qc_bgm_bed_start.py`):
  H1 (mốc act1_cue 1.15): "Sub-bass drop ... Cello u uất hòa cùng tiếng piano lạnh lẽo"
        -> cần bgm_sub_drone.mp3 + bgm_cello_sad.mp3 + bgm_piano_minimal.mp3
  H5 (5.01): "Nhạc nền Piano tối giản hòa cùng tiếng vĩ cầm ngân dài"
        -> cần bgm_violin_heart.mp3 + bgm_piano_minimal.mp3
        (Tập 03 H5 đã vá đúng y hệt: bgm_piano_warm -> violin_heart + piano_minimal)

Luật áp dụng: A11 (vá ĐÚNG giá trị của hồi, giữ dấu nháy, import thật để kiểm),
L5 (đã sao lưu .work/_cu/bed_t04_20261031/edition.py).

Chạy:  py -3 .work/_patch_bed_t04.py
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
ED = ROOT / ".work" / "edition.py"

src = ED.read_text(encoding="utf-8")

# --- khoanh đúng khối EPISODES["04"] -------------------------------------
i04 = src.index('"04": {')
nxt = src.index('"05": {', i04)
chunk = src[i04:nxt]

b = chunk.index('"bed":')
d = chunk.index("{", b)
depth, p = 0, d
while p < len(chunk):
    if chunk[p] == "{":
        depth += 1
    elif chunk[p] == "}":
        depth -= 1
        if depth == 0:
            break
    p += 1
old_bed = chunk[d:p + 1]
print("BED CU:\n  " + old_bed)

new_bed = ('{1: ("bgm_sub_drone.mp3", "bgm_cello_sad.mp3", "bgm_piano_minimal.mp3"), '
           '2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"), '
           '3: "bgm_sub_drone.mp3", '
           '4: "bgm_ambient_deep.mp3", '
           '5: ("bgm_violin_heart.mp3", "bgm_piano_minimal.mp3")}')

new_chunk = chunk[:d] + new_bed + chunk[p + 1:]
new_src = src[:i04] + new_chunk + src[nxt:]

# --- chốt: chỉ khác ở EPISODES["04"] và chỉ trong khối bed ---------------
old_blk = src[i04:nxt]
new_blk = new_chunk
if old_blk.replace(old_bed, "") != new_blk.replace(new_bed, ""):
    print("SAI: thay đổi ngoài khối bed — DỪNG")
    sys.exit(1)
if src[:i04] != new_src[:i04] or src[nxt:] != new_src[nxt:]:
    print("SAI: thay đổi ngoài EPISODES['04'] — DỪNG")
    sys.exit(1)

ED.write_text(new_src, encoding="utf-8")
print("BED MOI:\n  " + new_bed)
print("Da ghi", ED)
