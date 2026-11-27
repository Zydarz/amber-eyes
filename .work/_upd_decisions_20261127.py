# -*- coding: utf-8 -*-
"""Ghi 3 QUYET DINH cua nguoi dung (27/11/2026) vao ho so tap + A11 #202.

Quyet dinh:
 1. Nguoi dung se DUYET KICH BAN cho tu cam 'sat hai' (VN TK1/TK3) - AI khong tu doi.
 2. Nguoi dung se XAC NHAN nguon nhac nen cho 14 clip con lai (T9/L7).
 3. GIU kernel Kaggle da push - KHONG huy.

Dung: py -3 .work/_upd_decisions_20261127.py
"""
import pathlib
import re
import shutil
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")

# ---------------------------------------------------------------- 1. bao cao tap
P = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04" / "BAO_CAO_QC_TIKTOK_TAP04.md"
raw = P.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
lines = raw.replace("\r\n", "\n").split("\n")

i6 = next(i for i, l in enumerate(lines) if l.startswith("## 6. Việc còn lại"))
i7 = next(i for i, l in enumerate(lines) if l.startswith("## 7. Script đã tạo"))

new6 = """## 6. Quyết định của người dùng (27/11/2026) + việc còn lại

### 6.1. Ba quyết định đã chốt

| # | Việc | Quyết định của người dùng | Hệ quả cho AI |
|---|---|---|---|
| 1 | **Từ cấm `sát hại` ở VN TK1/TK3** (cổng T13 trượt) | **Người dùng sẽ tự duyệt kịch bản** | AI **KHÔNG tự sửa kịch bản** (L2/L4). Khi người dùng đổi câu ⇒ phải **chạy lại TTS cho câu đó** (engine Higgs Audio v3 của dự án chỉ chạy trên Kaggle GPU/Apple MLX — máy này không có) ⇒ phải chạy lại ASR + timeline + render + QC cho clip bị ảnh hưởng |
| 2 | **Nguồn nhạc nền 14 clip còn lại** (T9/L7 — bed đã mất file nguồn) | **Người dùng sẽ xác nhận** | Chờ xác nhận. **EN TK2 đã tách riêng**: dùng `bgm_ambient_deep.mp3` (có trên đĩa + có dòng provenance đầy đủ) ⇒ EN TK2 **không còn** vướng T9/L7 |
| 3 | **Kernel Kaggle đã push** (`chiduong2026/amber-eyes-higgs-fix-en-tk02-t04-kaggle-gpu` + dataset `...-t04`) | **GIỮ, KHÔNG HỦY** | Không gọi API Kaggle để hủy. Kernel này **không còn cần thiết** vì EN TK2 đã vá xong bằng cách trộn lại master (không cần sinh lại TTS) — nhưng người dùng chọn giữ. AI **không push/không chạy** kernel đó |

> Ghi nhận cho lượt sau: quyết định "giữ kernel" **không** có nghĩa cho phép chạy/push Kaggle. Lệnh đang có hiệu lực vẫn là **dừng kết nối Kaggle** — chỉ được phép hủy khi có yêu cầu riêng, và chưa có yêu cầu đó.

### 6.2. Việc còn lại

1. **EN TK2 — ĐÃ XONG** (trộn lại master + dựng lại clip + QC 14 cổng **ĐẠT**). Xác nhận nhỏ còn treo: `bgm_ambient_deep.mp3` (MiniMax) có được phép dùng cho TikTok không — **người dùng sẽ xác nhận cùng lượt với #2**.
2. **VN TK1 / TK3** — chờ người dùng duyệt kịch bản (xem 6.1 #1).
3. **14 clip còn lại** — chờ người dùng xác nhận nguồn nhạc nền (xem 6.1 #2).
4. **Kernel Kaggle** — giữ, không hủy (xem 6.1 #3). Dataset `chiduong2026/amber-eyes-higgs-fix-en-tk02-t04` cũng giữ.
5. **Caption/mô tả**: 5 file caption mỗi ngôn ngữ vẫn là placeholder — chưa điền link YouTube Tập 04 (Bước 8 của kế hoạch).
6. **Không commit media** (L10): 15 mp4 + 15 timeline + ảnh QC đều bị `.gitignore` loại — chỉ commit tài liệu + script.

---

"""
lines[i6:i7] = new6.rstrip("\n").split("\n")
P.write_text("\n".join(lines), encoding="utf-8", newline="")
print("da ghi bao cao:", P.name)

# ---------------------------------------------------------------- 2. A11 #202
T = ROOT / "00_TIEU_CHUAN" / "TIEU_CHUAN_DUNG_VIDEO.md"
raw = T.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
tl = raw.split(nl)
backup = ROOT / ".work" / "_cu" / f"a11_202_{datetime.now():%Y%m%d_%H%M}"
backup.mkdir(parents=True, exist_ok=True)
shutil.copy2(T, backup / T.name)
print("backup ->", backup)

rows = [(i, int(m.group(1))) for i, l in enumerate(tl) if (m := re.match(r"^\| (\d+) \|", l))]
nums = [n for _, n in rows]
assert 202 not in nums, "A11 202 da ton tai"

row202 = (
    "| 202 | **Quyết định của người dùng phải được GHI LẠI trong hồ sơ — kể cả quyết định \"không làm gì cả\"; và "
    "\"giữ kernel\" KHÔNG đồng nghĩa \"được phép chạy/push\" nếu lệnh dừng còn hiệu lực.** TikTok Tap 04 (27/11/2026): "
    "sau khi vá xong EN TK2, người dùng chốt 3 việc: (1) **tự duyệt kịch bản** cho từ cấm `sát hại` ở VN TK1/TK3 ⇒ "
    "AI **không tự sửa**; (2) **tự xác nhận** nguồn nhạc nền 14 clip còn lại (T9/L7 — bed đã mất file nguồn); "
    "(3) **GIÚ kernel Kaggle đã push, không hủy** (`chiduong2026/amber-eyes-higgs-fix-en-tk02-t04-kaggle-gpu`) | "
    "**Ghi vào `BAO_CAO_QC_TIKTOK_TAP04.md` §6.1** (bảng 3 quyết định + hệ quả cho AI) + **A11 #202** + CSV/provenance. "
    "**Quy tắc:** (a) quyết định nào của người dùng cũng phải có **mục riêng trong hồ sơ tập** kèm **hệ quả cụ thể cho AI** "
    "— kể cả \"giữ nguyên\"; (b) **phân biệt rõ 2 loại lệnh**: lệnh cho phép HÀNH ĐỘNG (được phép gọi API) khác lệnh "
    "cho phép GIỮ (không hủy, không xoá) — **không được suy diễn quyền gọi API từ quyết định giữ**; (c) lệnh "
    "\"dừng kết nối Kaggle\" vẫn còn hiệu lực cho tới khi có lệnh gỡ rõ ràng; (d) khi người dùng sửa kịch bản ⇒ "
    "phải nhớ **đổi câu = phải chạy lại TTS** (Higgs chỉ chạy trên Kaggle GPU/MLX — máy dựng không có) ⇒ chạy lại "
    "ASR + timeline + render + QC cho clip bị ảnh hưởng |"
)

last = max(i for i, n in rows)
tl.insert(last + 1, row202)
T.write_text(nl.join(tl), encoding="utf-8", newline="")
cnums = [int(m.group(1)) for l in T.read_text(encoding="utf-8").split(nl) if (m := re.match(r"^\| (\d+) \|", l))]
print("A11 max =", max(cnums), "| 202 co:", 202 in cnums, "| CRCRLF:", T.read_text(encoding="utf-8").count("\r\r\n"))
