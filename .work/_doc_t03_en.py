#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ghi bai hoc vao TIEU_CHUAN (A11) + AGENTS.md cho lượt dựng EN Tap03.

Theo A11 #95: them muc bang SCRIPT (khong go tay) — quet so lon nhat + 1,
roi kiem tra toan bang: cac so phai lien tiep 1..N va khong trung.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
STD = ROOT / "00_TIEU_CHUAN" / "TIEU_CHUAN_DUNG_VIDEO.md"
AG = ROOT / "AGENTS.md"

NEW = [
    ("| **Renderer dùng `hash()` của Python làm seed ⇒ cùng 1 shot render ra 2 khung hình khác nhau**"
     " (Tập 03 EN, 03/11/2026): `np.random.default_rng(abs(hash(shot[\"id\"])) % 999)` trong `t2_card` — "
     "`hash()` của chuỗi trong Python **được ngẫu nhiên hoá theo PYTHONHASHSEED ở mỗi tiến trình** "
     "⇒ 2 lần render cho 2 khung hình khác nhau (đo được: 1/6 shot lệch, lệch tới 90/765 mức xám trên vùng thẻ T2). "
     "Hậu quả: **ảnh tĩnh QC (H9) KHÔNG bảo đảm khớp với video dựng thật** ⇒ cổng QC hình ảnh vô nghĩa với shot T2 "
     "| Dùng seed **ổn định giữa các tiến trình**: "
     "`np.random.default_rng(zlib.crc32(shot[\"id\"].encode(\"utf-8\")) % 999)`. Sau khi sửa, A/B 2 lần render cho "
     "**6/6 shot giống byte** (`.work/_ab_pipe_test.py`). Sửa script dùng chung ⇒ kiểm hồi quy Tập 01 (L9) |"),
    ("| **Bản tiếng Anh thiếu khoá `roles_en` ⇒ badge vai rơi về nhãn CỨNG của Tập 01 — sai vụ án hiện lên màn hình**"
     " (Tập 03 EN, 03/11/2026): `ROLE_NAME`/`SUB_TAG` trong `edition.py` dùng "
     "`EP.get(\"roles_en\") or {…nhãn cứng Tập 01…}`; chỉ Tập 02/04/05 (+29) có khoá này ⇒ "
     "**Tập 03 EN hiện badge Điều tra viên \"Blanchard case file\"** (vụ Gypsy Rose Blanchard) và N1 "
     "\"**SPRINGFIELD RESIDENT**\" trong khi đang kể vụ Edmund Kemper; phụ đề `.srt` cũng gắn nhãn sai "
     "| Mỗi tập EN **bắt buộc** khai `roles_en` + `sub_tags_en` trong `EPISODES[\"XX\"]` (mẫu: Tập 02/04/05) — "
     "lấy N1/N2 từ `EP[\"n1\"]`/`EP[\"n2\"]` của chính tập đó. Hoặc sửa **fallback dùng chung** để suy ra từ "
     "`EP[\"case\"]`/`EP[\"n1\"]`/`EP[\"n2\"]` (Tập 01 không đổi vì `n1/n2` Tập 01 EN trùng nhãn cứng). "
     "Kiểm sau khi khai: badge N1/N2 trên ảnh tĩnh phải là nhãn của tập, và nhãn vai trong `.srt` phải khớp |"),
    ("| **Validator \"trích dẫn nguyên văn\" chỉ quét dấu nháy cong (“ ”) ⇒ dấu nháy thẳng ASCII (\") lọt qua**"
     " (Tập 03 EN, 03/11/2026): `_build_plan_tap03_en.py` dùng `re.findall(r\"“([^”]+)”\", chu)` ⇒ shot `2-15` có "
     "`hunting knife (\"The General\")` — **nhãn thương hiệu không hề có trong lời thoại, cũng không có trong bản tiếng Việt** — "
     "vẫn qua cổng QC; chỉ 1/110 shot lộ, số còn lại sạch "
     "| Quét **cả hai kiểu**: `re.findall(r\"“([^”]+)”\", t) + re.findall(r'\"([^\"]+)\"', t)`. Nhớ rằng "
     "\"chữ trên hình là một nguồn khẳng định\" (A11 #94): mọi nhãn trong ngoặc kép đều phải nguyên văn trong câu đang đọc |"),
    ("| **Đổi audio ⇒ phải SINH LẠI cả phụ đề `.srt`, không chỉ dựng lại hình** (Tập 03 EN, 03/11/2026): "
     "audio Tập 03 EN được dựng lại 02/11 (timeline mới 1646,62 s) nhưng `.srt` vẫn là bản 25/10 ⇒ "
     "**cue cuối kết thúc lúc 1961,75 s — dài hơn video 315 s** ⇒ phụ đề lệch toàn bộ phần sau "
     "| `subtitles.py` đọc `ED.w(\"timeline_s.json\")` ⇒ chạy lại sau **mỗi** lần đổi audio: "
     "`AE_EP=03 AE_LANG=en py -3 .work/subtitles.py`. Cổng: cue cuối kết thúc **≤** `timeline.total`, không cue chồng nhau |"),
    ("| **`Tee-Object` của PowerShell 5.1 ghi log UTF-16LE ⇒ đọc log ra ký tự `\\x00`; và kích thước file "
     "`part_*.mp4` KHÔNG phản ánh tiến độ** (Tập 03 EN, 03/11/2026): đo file size cho ra \"còn 912 phút\" trong khi "
     "render thật đang chạy ~12,4 fps ⇒ **ước lượng sai gấp 2 lần** (ffmpeg ghi `mdat` theo lô) "
     "| Đọc log bằng `Path.read_text(encoding=\"utf-16\")` khi file bắt đầu bằng BOM `fffe`; **đo tiến độ bằng bộ đếm khung "
     "trong log** (`[part_XX] fi/total`), không bằng kích thước file. Ghi log bằng `Out-File -Encoding utf8` khi cần đọc bằng công cụ khác |"),
]

H15 = ("| H15 | **Renderer phải TẤT ĐỊNH**: cùng 1 shot, chạy 2 lần phải ra **cùng khung hình** (byte-for-byte). "
       "Seed của Python theo `hash()` bị ngẫu nhiên hoá theo `PYTHONHASHSEED` mỗi tiến trình ⇒ ảnh tĩnh QC **không** "
       "bảo đảm khớp video dựng thật | Dùng `zlib.crc32(shot[\"id\"].encode(\"utf-8\"))` làm seed. Sau khi sửa script dùng chung "
       "⇒ A/B 2 lượt render trên ≥ 6 shot phải cho **6/6 giống byte** (`.work/_ab_pipe_test.py`) + kiểm hồi quy Tập 01 (L9) |")

T14 = ("| T14 | **PowerShell 5.1 `Tee-Object` ghi log UTF-16LE** ⇒ đọc log ra ký tự `\\x00`; **đừng dùng kích thước file "
       "`part_*.mp4` để đo tiến độ** (ffmpeg ghi `mdat` theo lô ⇒ ước lượng sai gấp 2 lần) | Đọc log bằng `encoding=\"utf-16\"` khi có BOM `fffe`; "
       "đo tiến độ bằng **bộ đếm khung trong log** (`[part_XX] fi/total`) |")


def patch_a11():
    txt = STD.read_text(encoding="utf-8")
    lines = txt.split("\n")
    # tim dong dau bang A11 va dong ket thuc
    i0 = next(i for i, l in enumerate(lines) if l.startswith("| # | Bẫy | Cách làm đúng |"))
    i1 = i0 + 1
    while i1 < len(lines) and lines[i1].startswith("|"):
        i1 += 1
    nums = []
    for l in lines[i0 + 1:i1]:
        m = re.match(r"\|\s*(\d+)\s*\|", l)
        if m:
            nums.append(int(m.group(1)))
    print(f"A11: {len(nums)} muc · so lon nhat {max(nums)}")
    if nums != list(range(1, len(nums) + 1)):
        raise SystemExit(f"A11 khong lien tiep/trung truoc khi them: {nums}")
    nxt = max(nums) + 1
    new_rows = []
    for k, body in enumerate(NEW):
        new_rows.append(f"| {nxt + k} {body[1:]}")
    out = lines[:i1] + new_rows + lines[i1:]
    # validate toan bang
    chk = [l for l in out if re.match(r"\|\s*\d+\s*\|", l)]
    cnums = [int(re.match(r"\|\s*(\d+)\s*\|", l).group(1)) for l in chk]
    if cnums != list(range(1, len(cnums) + 1)):
        raise SystemExit(f"A11 sau khi them khong lien tiep: {cnums[-8:]}")
    if len(set(cnums)) != len(cnums):
        raise SystemExit("A11 trung so sau khi them")
    STD.write_text("\n".join(out), encoding="utf-8")
    print(f"A11: da them muc {nxt}..{nxt + len(NEW) - 1} · tong {len(cnums)} muc, lien tiep 1..{len(cnums)}")
    return nxt, nxt + len(NEW) - 1


def patch_agents():
    txt = AG.read_text(encoding="utf-8")
    lines = txt.split("\n")
    if any(l.startswith("| H15 |") for l in lines):
        print("AGENTS.md: H15 da ton tai — bo qua")
    else:
        i = next(i for i, l in enumerate(lines) if l.startswith("| H14 |"))
        lines.insert(i + 1, H15)
        print("AGENTS.md: da them H15")
    if any(l.startswith("| T14 |") for l in lines):
        print("AGENTS.md: T14 da ton tai — bo qua")
    else:
        i = next(i for i, l in enumerate(lines) if l.startswith("| T13 |"))
        lines.insert(i + 1, T14)
        print("AGENTS.md: da them T14")
    AG.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    patch_a11()
    patch_agents()
    print("xong")
