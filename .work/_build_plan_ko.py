# -*- coding: utf-8 -*-
"""Generate 02_SAN_XUAT/Tap01_KO/KeHoach_Video_Tap01_KO.md from VN plan + shots_text_KO.json.
Keeps Câu/Vai/Mẫu/Nền/Nhân vật and the Vietnamese beat wording (renderer triggers);
swaps the Chữ cell and beat cues to Korean.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"

vn_text = (ROOT / "02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md").read_text(encoding="utf-8").splitlines()
ko_text = json.loads((WORK / "shots_text_KO.json").read_text(encoding="utf-8"))
ko_script = json.load(open(WORK / "script_tap01_KO.json", encoding="utf-8"))
S = {s['id']: s['text'] for e in ko_script if e['kind'] == 'LOI' for s in e['sentences']}

i0 = next(i for i, l in enumerate(vn_text) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_text) if i > i0 and l.startswith("**Tổng:"))

# Build headers and metadata
header = [
    "# HỒ SƠ SẢN XUẤT TẬP 01 · BẢN TIẾNG HÀN · 「엄마의 사랑이라는 이름의 독약」 (PHẦN B)",
    "",
    "> **TRẠNG THÁI: CHỜ DUYỆT GIỌNG ĐỌC & DỰNG**",
    "",
    "**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).",
    "**Kịch bản:** `01_KICH_BAN/Tap01_KO/kichban_tap01_KO.md` · **Chữ cố định:** `00_TIEU_CHUAN/CHU_CO_DINH_KO.md` · **Thành phẩm:** `02_SAN_XUAT/Tap01_KO/xuat_ban/`",
    "**Bản gốc:** `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md`. Bảng shot giữ nguyên các cột Câu, Vai, Mẫu, Nền, Nhân vật và mô tả beat; chỉ thay:",
    "- cột **Chữ** sang tiếng Hàn chuẩn phát thanh tài liệu (Pillow vẽ chữ với `malgun.ttf` / `malgunbd.ttf`);",
    "- các cụm `ở \"…\"` trong cột **Beat** sang cụm tiếng Hàn **có thật** trong câu KO tương ứng.",
    "",
    "## B1. Thông tin tập",
    "",
    "| Mục | Giá trị |",
    "|---|---|",
    "| Kịch bản | `01_KICH_BAN/Tap01_KO/kichban_tap01_KO.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_KO.md`, 128 câu, 33 lượt nói, passed `_qc_ko_parity.py`) |",
    "| Lượt nói / câu | 33 / **128**. Host 50% · Chuyên gia 24% · Điều tra viên 20% · Người bình thường 5%. Mã câu trùng 100% bản VN (`script_tap01_KO.json`) |",
    "| N1 / N2 | `1.07` 증인 (Cừu) / `4.03` 시청자 (Mèo) |",
    "| Bảng shot | 122 dòng = 104 shot có lời + 18 dòng không lời |",
    "| Nền dùng | 45 ảnh `assets/bg/` (dùng lại 100% của bản VN/EN/JA) |",
    "| Giọng dự kiến | H `Korean_CalmGentleman` 0.95 · D `Korean_ColdYoungMan` 0.95 · C `Korean_DecisiveQueen` 0.92 · N1 `Korean_GentleWoman` 0.95 · N2 `Korean_SweetGirl` 0.95 |",
    "",
    "## B3. Ánh xạ riêng (trong `parse_shots.py`)",
    "",
    "Giống hệt bản VN (`COMBO`, `BG2`, `INSET`), vì số hiệu shot và nền không đổi.",
    "",
    "## 6. DANH SÁCH SHOT — TẬP 01 BẢN TIẾNG HÀN",
    "",
    "**Đọc bảng:** *Vai* = người đang nói (H 호스트 · D 수사관 · C 심리학자 · N1 증인 · N2 시청자).",
    ""
]

table_lines = []
errs = []
done = set()

for l in vn_text[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        # Check if it's an act heading
        if l.startswith("### HỒI"):
            act_num = re.search(r"HỒI\s*(\d)", l).group(1)
            act_titles_ko = {
                "1": "제1막 — 신뢰가 무너지는 순간 · nền chủ đạo `house_night`",
                "2": "제2막 — 범죄 현장 & 진료 기록 · nền chủ đạo `wheelchair_room`",
                "3": "제3막 — 심리해부――FDIA 가해자의 뇌 속 · nền chủ đạo `clinical`",
                "4": "제4막 — 심문 & 전환점――왜 GYPSY는 도망치지 못했는가? · nền chủ đạo `interrogation`",
                "5": "제5막 — 사법적 단죄, 레드플래그 & 교훈 · nền chủ đạo `court_dawn`"
            }
            table_lines.append(f"### {act_titles_ko[act_num]}")
        elif l.startswith("### INTRO"):
            table_lines.append(l)
        else:
            table_lines.append(l)
        continue

    sid = m[1]
    c = l.strip().strip('|').split('|')
    if sid not in ko_text:
        if c[5].strip() != '—':
            errs.append(f"{sid}: thiếu bản KO")
        table_lines.append(l)
        continue

    chu, beat = ko_text[sid]
    done.add(sid)

    # c[0]=Shot, c[1]=Câu, c[2]=Vai, c[3]=Mẫu, c[4]=Nền+bóng, c[5]=Chữ, c[6]=Beat, c[7]=Nhân vật, c[8]=cuối
    c[5] = f" {chu} "
    c[6] = f" {beat} "
    table_lines.append("|" + "|".join(c) + "|")

out_dir = ROOT / "02_SAN_XUAT" / "Tap01_KO"
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "KeHoach_Video_Tap01_KO.md"
out_file.write_text("\n".join(header + table_lines[2:]), encoding="utf-8")
print(f"Generated {out_file} successfully. Processed {len(done)} shots.")
if errs:
    print("Errors:", errs)
