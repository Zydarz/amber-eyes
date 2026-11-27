# -*- coding: utf-8 -*-
"""Them A11 #203 vao TIEU_CHUAN_DUNG_VIDEO.md + H32 vao AGENTS.md (chen sau dong cuoi)."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

A11_ROW = (
    "| 203 | **Bước 8 (đóng gói) phải có 3 thứ cho MỌI tập TikTok, và số liệu trong đó phải ĐO từ file mp4 thành phẩm — không ước lượng.** "
    "TikTok Tap 04 (27/11/2026): 15 file `Caption_TK*.txt` (5 clip × 3 ngôn ngữ) **đều thiếu dòng nhãn AIGC** và **thiếu khối “Ghi chú khi đăng”** ⇒ người đăng tay phải tự thêm 15 lần, hoặc đăng mà không có nhãn AIGC (TikTok bắt buộc nhãn). "
    "Tiền lệ KHÔNG nhất quán: Tap 03 VN có đủ 2 phần, Tap 03 EN/JA thiếu ⇒ mẫu duy nhất là `Tap03/Caption_TK1.txt` (VN). "
    "Đã đóng gói: **15 caption** (594–624 ký tự VN · 638–664 EN · 301–317 JA) + **3 `mo_ta.txt`** + **3 `checklist_dang.md`** (theo mẫu `Tap01/mo_ta.txt` và yêu cầu Bước 8 của `KE_HOACH_TIKTOK.md`) "
    "| **Quy tắc:** (1) mỗi `Caption_TK*.txt` = **phần dán** (hook · giới thiệu tập · CTA · **dòng nhãn AIGC ở dòng 9** · hashtag) + `---` + **khối “Ghi chú khi đăng”** (toggle AIGC · link bio · độ dài caption · file + thời lượng + số câu · trạng thái QC · nguồn BGM · 2 bản mô tả); "
    "(2) mỗi thư mục tập phải có **`mo_ta.txt`** ([A] caption dán của cả 5 clip + [A2] link YouTube + [B] dòng AIGC bắt buộc + [C] lưu ý an toàn + hotline + [D] bảng số đo) và **`checklist_dang.md`** (trạng thái từng clip + 7 việc chung + cảnh báo); "
    "(3) **số đo trong ghi chú phải lấy từ file mp4 thành phẩm** (ffprobe: thời lượng · dung lượng · LUFS · TP · số câu) — báo cáo QC cũng phải cập nhật lại khi render lại clip (Tap 04: bảng QC ghi EN TK2 = 25,6 MB nhưng file sau khi render lại là **24,5 MiB** ⇒ đã sửa); "
    "(4) **clip chưa đạt cổng T13 ⇒ đánh dấu “CHẶN” trong checklist + cảnh báo ngay trong caption**, không được đăng (Tap 04: VN TK1 `TK1.01#6` và VN TK3 `TK3.01#9`); "
    "(5) link YouTube tập chưa có ⇒ **placeholder rõ ràng ở CẢ 3 nơi** (caption · mo_ta · checklist) và ghi “chưa đủ điều kiện đăng”; "
    "(6) **không dán** khối ghi chú vào caption — phải ghi rõ trong file. Công cụ: `.work/_tk04_package_b8.py` (idempotent, chạy lại được) |"
)

H32_ROW = (
    "| **H32** | **Mỗi tập TikTok phải đóng gói Bước 8 trước khi coi là “xong”: caption có dòng nhãn AIGC + khối ghi chú khi đăng, có `mo_ta.txt`, có `checklist_dang.md` — và mọi số liệu trong đó phải ĐO từ file mp4 thành phẩm.** "
    "Tap 04 (27/11/2026): 15 caption thiếu nhãn AIGC + thiếu khối ghi chú (người đăng tay phải tự thêm 15 lần, hoặc đăng không nhãn AIGC); thiếu cả `mo_ta.txt` lẫn `checklist_dang.md` ở cả 3 thư mục ngôn ngữ. "
    "Tiền lệ không nhất quán (Tap 03 EN/JA cũng thiếu) ⇒ mẫu duy nhất lấy `Tap03/Caption_TK1.txt` + `Tap01/mo_ta.txt` "
    "| **Cổng QC 14 cổng KHÔNG phủ được phần đóng gói** — phải kiểm riêng: (1) caption có **dòng nhãn AIGC** (dòng 9) và khối ghi chú sau `---`; (2) `mo_ta.txt` + `checklist_dang.md` có tồn tại; "
    "(3) số đo (thời lượng · MB · LUFS · TP · số câu) **khớp file mp4 thành phẩm** — đo được sai số: bảng QC ghi EN TK2 25,6 MB, file thật 24,5 MiB (bảng lấy số file cũ trước khi render lại); "
    "(4) clip trượt cổng T13 ⇒ **CHẶN** trong checklist + cảnh báo trong caption; (5) link YouTube chưa có ⇒ placeholder ở cả 3 nơi. Luật chi tiết: **A11 #203**. Công cụ: `.work/_tk04_package_b8.py` |"
)


def insert_after(path, anchor_prefix, row):
    p = ROOT / path
    lines = p.read_text(encoding="utf-8").split("\n")
    idx = None
    for i, l in enumerate(lines):
        if l.startswith(anchor_prefix):
            idx = i
    if idx is None:
        raise SystemExit(f"khong tim thay dong bat dau bang {anchor_prefix!r} trong {path}")
    if any(l.startswith(row[:12]) for l in lines):
        print("  [skip] da co roi")
        return
    lines.insert(idx + 1, row)
    p.write_bytes("\n".join(lines).encode("utf-8"))
    print(f"  chen vao {path} sau dong {idx + 1}")


insert_after("00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md", "| 202 |", A11_ROW)
insert_after("AGENTS.md", "| **H31** |", H32_ROW)
