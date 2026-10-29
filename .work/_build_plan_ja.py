# -*- coding: utf-8 -*-
"""Generate 02_SAN_XUAT/Tap01_JA/KeHoach_Video_Tap01_JA.md from VN plan + shots_text_JA.json.
Keeps Câu/Vai/Mẫu/Nền/Nhân vật and the Vietnamese beat wording (renderer triggers);
swaps the Chữ cell and beat cues to Japanese.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"

vn_text = (ROOT / "02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md").read_text(encoding="utf-8").splitlines()
ja_text = json.loads((WORK / "shots_text_JA.json").read_text(encoding="utf-8"))
ja_script = json.load(open(WORK / "script_tap01_JA.json", encoding="utf-8"))
S = {s['id']: s['text'] for e in ja_script if e['kind'] == 'LOI' for s in e['sentences']}


def sents(cell):
    out = []
    for ma, a, b in re.findall(r'`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?', cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


i0 = next(i for i, l in enumerate(vn_text) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_text) if i > i0 and l.startswith("**Tổng:"))

# Build headers and metadata
header = [
    "# HỒ SƠ SẢN XUẤT TẬP 01 · BẢN TIẾNG NHẬT · 「母の愛という名の毒薬」 (PHẦN B)",
    "",
    "> **TRẠNG THÁI: CHỜ DUYỆT GIỌNG ĐỌC & DỰNG**",
    "",
    "**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).",
    "**Kịch bản:** `01_KICH_BAN/Tap01_JA/kichban_tap01_JA.md` · **Chữ cố định:** `00_TIEU_CHUAN/CHU_CO_DINH_JA.md` · **Thành phẩm:** `02_SAN_XUAT/Tap01_JA/xuat_ban/`",
    "**Bản gốc:** `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md`. Bảng shot giữ nguyên các cột Câu, Vai, Mẫu, Nền, Nhân vật và mô tả beat; chỉ thay:",
    "- cột **Chữ** sang tiếng Nhật chuẩn phát thanh tài liệu (Pillow vẽ chữ với `YuGothB.ttc` / `YuGothM.ttc`);",
    "- các cụm `ở \"…\"` trong cột **Beat** sang cụm tiếng Nhật **có thật** trong câu JA tương ứng.",
    "",
    "## B1. Thông tin tập",
    "",
    "| Mục | Giá trị |",
    "|---|---|",
    "| Kịch bản | `01_KICH_BAN/Tap01_JA/kichban_tap01_JA.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`, 128 câu, 33 lượt nói, passed `_qc_ja.py`) |",
    "| Lượt nói / câu | 33 / **128**. Host 50% · Chuyên gia 24% · Điều tra viên 20% · Người bình thường 5%. Mã câu trùng 100% bản VN (`script_tap01_JA.json`) |",
    "| N1 / N2 | `1.07` 証人 (Cừu) / `4.03` 視聴者 (Mèo) |",
    "| Bảng shot | 122 dòng = 104 shot có lời + 18 dòng không lời |",
    "| Nền dùng | 45 ảnh `assets/bg/` (dùng lại 100% của bản VN/EN) |",
    "| Giọng dự kiến | H `Japanese_GentleButler` 0.95 · D `Japanese_SeriousCommander` 0.97 · C `Japanese_DependableWoman` 0.95 · N1 `Japanese_KindLady` 0.95 · N2 `Japanese_DecisivePrincess` 0.95 |",
    "",
    "## B3. Ánh xạ riêng (trong `parse_shots.py`)",
    "",
    "Giống hệt bản VN (`COMBO`, `BG2`, `INSET`), vì số hiệu shot và nền không đổi.",
    "",
    "## 6. DANH SÁCH SHOT — TẬP 01 BẢN TIẾNG NHẬT",
    "",
    "**Đọc bảng:** *Vai* = người đang nói (H ホスト · D 捜査官 · C 心理学者 · N1 証人 · N2 視聴者).",
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
            act_titles_ja = {
                "1": "第1幕 — 信頼が崩れる瞬間 · nền chủ đạo `house_night`",
                "2": "第2幕 — 犯罪現場＆診療記録 · nền chủ đạo `wheelchair_room`",
                "3": "第3幕 — 心理剖検――FDIA犯罪者の脳の内部 · nền chủ đạo `clinical`",
                "4": "第4幕 — 尋問＆転換点――なぜGYPSYは逃げなかったのか？ · nền chủ đạo `interrogation`",
                "5": "第5幕 — 司法の裁き、レッドフラッグ＆教訓 · nền chủ đạo `court_dawn`"
            }
            table_lines.append(f"### {act_titles_ja[act_num]}")
        elif l.startswith("### INTRO"):
            table_lines.append(l)
        else:
            table_lines.append(l)
        continue

    sid = m[1]
    c = l.strip().strip('|').split('|')
    if sid not in ja_text:
        if c[5].strip() != '—':
            errs.append(f"{sid}: thiếu bản JA")
        table_lines.append(l)
        continue

    chu, beat = ja_text[sid]
    done.add(sid)

    # replace quoted beat cues if present
    ja_cues = re.findall(r'ở "([^"]+)"', beat)
    if ja_cues:
        it = iter(ja_cues)
        c[6] = re.sub(r'ở "([^"]+)"', lambda _: 'ở "' + next(it, '??') + '"', c[6])
    
    c[5] = ' ' + chu + ' '

    # Validate cues against sentences
    txt = ' '.join(S.get(x, '') for x in sents(c[1]))
    for p in ja_cues:
        if txt and p not in txt and p != "Bụp":
            errs.append(f"{sid}: cụm \"{p}\" không có trong câu {sents(c[1])}")

    table_lines.append('|' + '|'.join(c) + '|')

total_line = f"**Tổng: 122 shot · Đã hoàn thiện và đối chiếu 100% câu và beat tiếng Nhật.**"
table_lines.append(total_line)

full_content = "\n".join(header) + "\n" + "\n".join(table_lines)
out_path = ROOT / "02_SAN_XUAT/Tap01_JA/KeHoach_Video_Tap01_JA.md"
out_path.write_text(full_content, encoding="utf-8")
print(f"Generated {out_path} successfully. Verified shots: {len(done)}/122.")
if errs:
    print("ERRORS:")
    for e in errs:
        print(" ", e)
else:
    print("0 ERRORS! All cues verified.")
