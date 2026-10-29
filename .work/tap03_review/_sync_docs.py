#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đồng bộ 3 tài liệu sau khi thêm EPISODES['03'] + sửa bảng âm thanh + sửa bảng nguồn."""
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
REVIEW = ROOT / "01_KICH_BAN" / "Tap03" / "REVIEW_kichban_tap03.md"
AMTH = ROOT / "02_SAN_XUAT" / "Tap03" / "AmThanh_Tap03.md"
MANIF = ROOT / "02_SAN_XUAT" / "Tap03" / "Danh_Sach_Anh_Tap03.md"


def cut(text, start_marker, end_marker, new):
    i = text.index(start_marker)
    j = text.index(end_marker)
    assert i < j
    return text[:i] + new + text[j:]


# ---------------------------------------------------------------- REVIEW
r = REVIEW.read_text(encoding="utf-8")

E1 = """### E1. `edition.py` — ĐÃ thêm khối Tập 03 ✅ (23/10/2026)
`EPISODES["03"]` đã được thêm vào `.work/edition.py` (đặt trước khối `"04"`), dùng `script_tap03.json` + `sfx_tap03.json`.
`AE_EP=03` không còn dừng ở `raise SystemExit`.

**Ba mốc đã sửa so với bản đề xuất ở bản review** — bản đề xuất sai theo docstring của `build_audio3.py`:

| Khoá | Đề xuất cũ | **Đã áp dụng** | Vì sao |
|---|---|---|---|
| `act1_cue` | `1.02` | **`1.14`** | phải là mốc **nhạc** mở đầu hồi 1 — `1.02` là SFX đồng xu. `1.14` = [BGM] "Cello u uất hòa cùng tiếng piano chậm rãi" (giống Tập 02 dùng `1.16`) |
| `silence_cue` | `1.10` | **`1.11`** | phải là element **NGHI** (có `start`/`end`) — `1.10` là LOI nên sẽ `StopIteration`. `1.11` = [NGHI] "Nhạc nền dừng lại, chỉ còn tiếng bước chân vang vọng trong hành lang nhà tù" |
| `click_cues` | `("1.02",)` | **`("1.08",)`** | phải là mốc SFX "băng ghi âm bật" — `1.08` = [SFX] "Tiếng băng ghi âm bật nhẹ 'Tách'." (giống Tập 02 dùng `1.06`) |

**`bed` cũng đã chỉnh theo đúng cue BGM trong kịch bản** (bản đề xuất cũ đặt act 2 là piano, không khớp cue):
`1: (cello_sad, piano_minimal)` · `2: (ambient_deep,)` · `3: cello_sad_v2` · `4: sub_drone` · `5: piano_warm`

Đã kiểm bằng `.work/tap03_review/_check_ep03.py`: cả 3 mốc đúng kiểu (BGM / NGHI / SFX), 21 mã câu trong `need`+`summary` đều tồn tại, 6 file BGM có thật, **không hỏng Tập 01/02/04/05**.

"""

E2 = """### E2. `n_element` khác Tập 01/02/04 — ĐÃ áp dụng ✅
Tập 02 và 04 đều dùng `{"1.07": "N1", "4.06": "N2"}`. Tập 03 có **hai element vai N ở vị trí khác**:
- `1.09` – viên cảnh sát trực ban (Hồi 1) → **N1**
- `2.09` – viên cảnh sát tại quán The Jury Room (Hồi 2) → **N2**

Đã đặt `n_element = {"1.09": "N1", "2.09": "N2"}` trong khối `"03"`. Đã kiểm: cả hai element đều mang `role = N` trong kịch bản.

### E3. Nhãn vai N1/N2 — ĐÃ đổi ✅
`SUB_TAG` mặc định gán `N2` → **"KHÁNH GIẢ"**. Tập 03 **không có vai khán giả** – N2 là viên cảnh sát quán rượu. Đã sửa trong khối `"03"`:
- `n1 = ("TRỰC BAN CẢNH SÁT SANTA CRUZ", "Người trực đêm", "TRỰC BAN")`
- `n2 = ("CẢNH SÁT QUÁN RƯỢU", "Đồng nghiệp tại The Jury Room", "CẢNH SÁT")`

Thẻ vai trên hình sẽ ghi đúng, không còn ghi "KHÁNH GIẢ".

"""

r = cut(r, "### E1. `edition.py` CHƯA có khai báo Tập 03 ⛔", "### E2. `n_element` khác", E1)
r = cut(r, "### E2. `n_element` khác", "### E4. Thư mục sản xuất chưa có", E2)

old_e4 = "### E4. Thư mục sản xuất chưa có ⛔\n`02_SAN_XUAT/` hiện có `Tap01`, `Tap01_EN`, `Tap02`. Chưa có `Tap03/` → cần `KeHoach_Video_Tap03.md`, `Danh_Sach_Anh_Tap03.md`, `acting_tap03.json`, `sfx_tap03.json`, `Tap03_master`, `Tap03.srt`."
new_e4 = """### E4. Thư mục sản xuất — ĐÃ tạo một phần ⚠️
`02_SAN_XUAT/Tap03/` **đã có**: `Danh_Sach_Anh_Tap03.md` (47 ảnh) · `AmThanh_Tap03.md` · `xuat_ban/nguon_tham_khao.md` · `sfx_youtube/` (10 mp3 nguồn) · `contact_sheet_t3.png`.
**Còn thiếu**: `KeHoach_Video_Tap03.md` (bảng shot) · `.work/acting_tap03.json` (diễn xuất TTS) · `.work/shots.json` · `Tap03_master.mp3` · `Tap03.srt`."""
assert r.count(old_e4) == 1
r = r.replace(old_e4, new_e4, 1)

# them muc E10 cho cac sua chua cua lượt nay
old_tail = "### E9. Đã đồng bộ `Danh_Sach_Anh_Tap03.md` (nhánh sản xuất chạy song song) ⚠️"
new_tail = """### E10. Sửa chữa lượt 23/10/2026 (sau khi sinh ảnh + tải SFX) ✅
- **Bảng nguồn A10** (`xuat_ban/nguon_tham_khao.md`): 3 mã câu đã dịch sau khi viết lại kịch bản → đã sửa `1.09#1`→`1.10#1`, `1.09#10`→`1.10#10`, `1.12#7`→`1.13#7` (và `1.09`→`1.10` trong phụ lục). Đã quét lại: 19/19 dòng khớp, 0 sai.
- **Bảng âm thanh** (`.work/sfx_tap03.json`): mọi mốc `ambience` / `music_drop` đổi sang **mã câu** (`build_audio3.py` chỉ tra cứu `sent` cho 2 loại này — mã element sẽ bị bỏ qua im lặng), và cue `"3.05"` → `"3.05#1"` (trước đó trỏ vào element LOI ⇒ bị bỏ qua). Đã kiểm lại theo đúng quy tắc builder: 0 lỗi.
- **Manifest ảnh**: thêm `t3_backyard_garden` (mốc `2.06#2`), sửa tên ảnh không tồn tại `t2_cellar` → `t2_cell_medical`, cắt nốt viền sáng sót của `t3_textbooks`.

### E9. Đã đồng bộ `Danh_Sach_Anh_Tap03.md` (nhánh sản xuất chạy song song) ⚠️"""
assert r.count(old_tail) == 1
r = r.replace(old_tail, new_tail, 1)
REVIEW.write_text(r, encoding="utf-8")
print("  OK  REVIEW_kichban_tap03.md")

# ---------------------------------------------------------------- AmThanh_Tap03.md
a = AMTH.read_text(encoding="utf-8")
old = """| 1 | `.work/edition.py` → khai báo `EPISODES["03"]` | **Chưa** — file có `"01"`, `"02"`, `"04"`, thiếu `"03"` |
| 2 | `.work/edition.py` → `N_ELEMENT` cho Tap03 | **Chưa** — cần `{... "1.09": "N1", "2.09": "N2"}`; nhãn `N2` mặc định là "KHÁNH GIẢ" nhưng Tap03 không có vai khán giả (vai `2.09` là **cảnh sát quán rượu**) → phải đổi nhãn |"""
new = """| 1 | `.work/edition.py` → khai báo `EPISODES["03"]` | ✅ **Đã làm 23/10** — thêm khối `"03"` (đặt trước `"04"`), `AE_EP=03` chạy được. Ba mốc đã sửa theo docstring của builder: `act1_cue` = `1.14` (mốc nhạc), `silence_cue` = `1.11` (NGHI), `click_cues` = `("1.08",)` (SFX băng ghi âm) |
| 2 | `.work/edition.py` → `N_ELEMENT` cho Tap03 | ✅ **Đã làm 23/10** — `{"1.09": "N1", "2.09": "N2"}`; nhãn `N1` = "TRỰC BAN CẢNH SÁT SANTA CRUZ", `N2` = **"CẢNH SÁT QUÁN RƯỢU"** (đã đổi, không còn "KHÁNH GIẢ") |"""
assert a.count(old) == 1
a = a.replace(old, new, 1)

old2 = "| 5 | Bảng shot + `.work/shots.json` cho tập 3 | **Chưa** — `parse_shots.py` hiện còn trỏ Tập 01 |"
new2 = "| 5 | Bảng shot + `.work/shots.json` cho tập 3 | **Chưa** — `parse_shots.py` hiện còn trỏ Tập 01; `KeHoach_Video_Tap03.md` chưa có |"
assert a.count(old2) == 1
a = a.replace(old2, new2, 1)

old3 = "**Đã kiểm bằng script** (`.work/tap03_review/_check_sfx_sheet.py`): 22 file được tham chiếu đều tồn tại · mọi mốc câu đều khớp với kịch bản đã parse · cả 10 file `t3/` đều được dùng."
new3 = """**Đã kiểm bằng script** (`.work/tap03_review/_check_sfx_sheet.py`) — theo **đúng quy tắc** của `build_audio3.py::place_sheet()`:
- `ambience` và `music_drop` bắt buộc dùng **mã câu** (`2.06#2`), không dùng mã element (mã element sẽ bị bỏ qua **im lặng** — không báo lỗi).
- `cues` chấp nhận cả hai: mã câu **hoặc** mã element SFX/BGM/NGHI.
- 22 file được tham chiếu đều tồn tại · mọi mốc đều resolve · cả 10 file `t3/` đều được dùng. **0 lỗi.**"""
assert a.count(old3) == 1
a = a.replace(old3, new3, 1)
AMTH.write_text(a, encoding="utf-8")
print("  OK  AmThanh_Tap03.md")

# ---------------------------------------------------------------- Danh_Sach_Anh_Tap03.md
m = MANIF.read_text(encoding="utf-8")
oldm = """| 7 | Bảng âm thanh Tập 03 | ✅ `.work/sfx_tap03.json` (10 nền + 20 tiếng động) — xem `02_SAN_XUAT/Tap03/AmThanh_Tap03.md` |
| 8 | Dựng audio TTS + trộn cho Tập 03 | **Chưa làm** — cần `EPISODES["03"]` trong `.work/edition.py` (mục 3, 4 ở trên) trước khi `build_audio3.py` chạy được |"""
newm = """| 7 | Bảng âm thanh Tập 03 | ✅ `.work/sfx_tap03.json` (10 nền + 20 tiếng động) — xem `02_SAN_XUAT/Tap03/AmThanh_Tap03.md` |
| 8 | Dựng audio TTS + trộn cho Tập 03 | ⚠️ **Khối `EPISODES["03"]` đã thêm xong** (mục 3) — còn thiếu `.work/acting_tap03.json` (diễn xuất 215 câu) và bảng shot thì `build_audio3.py` mới chạy trọn |"""
assert m.count(oldm) == 1
m = m.replace(oldm, newm, 1)
MANIF.write_text(m, encoding="utf-8")
print("  OK  Danh_Sach_Anh_Tap03.md")

print("\nDa dong bo 3 tai lieu.")
