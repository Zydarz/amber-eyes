#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh mục 6 (bảng shot) cho Tập 08 — 3 ngôn ngữ: VN / EN / JA.

Bảng dữ liệu nằm ở .work/_t08_rows_a1..a5.py (mỗi hồi một file).
Cột "Mẫu" và cột "Nền" GIỮ NGUYÊN tiếng Việt ở cả 3 bản — parse_shots.py dò
"cờ" / "lời kể" / "ngày" / "so sánh" trong cột Mẫu để suy ra variant, và cột Mẫu
giữ tiếng Việt là quy ước của Tập 01/07. Chỉ tiêu đề mục 6 + cột "Chữ" mới dịch.

Chạy:  py -3 .work/_gen_plan_t08.py
Idempotent: chạy lại nhiều lần cho kết quả giống hệt (thay mục 6 cũ, không nhân bản).
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = Path(__file__).resolve().parent
ROOT = WORK.parent
sys.path.insert(0, str(WORK))

from _t08_rows_a1 import ACT1  # noqa: E402
from _t08_rows_a2 import ACT2  # noqa: E402
from _t08_rows_a3 import ACT3  # noqa: E402
from _t08_rows_a4 import ACT4  # noqa: E402
from _t08_rows_a5 import ACT5  # noqa: E402

ACTS = [(1, ACT1), (2, ACT2), (3, ACT3), (4, ACT4), (5, ACT5)]

HEAD_VN = """## 6. DANH SÁCH SHOT — TẬP 08 (viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.

**Trạng thái 06/11/2026:** kịch bản viết lại 05/11/2026 (53 phần tử · 171 câu) ⇒ bảng shot dựng lại **108 shot**. Master audio cũ đã bị dọn theo A11 §8 ⇒ `timeline_s_t08.json` là **bản ước lượng** (`.work/_build_timeline_t08.py`), chỉ dùng cho ảnh tĩnh; khi dựng video phải chạy lại TTS + `build_audio3.py` (sẽ ghi đè đúng file timeline này)."""

HEAD_EN = """## 6. DANH SÁCH SHOT — TẬP 08 (ENGLISH EDITION)

**How to read:** *Vai* = speaker (H Owl · D Wolf · C Fox · N1 Sheep · N2 Cat). The table describes **background + graphics**; badge and bust follow A5.4.
*Nhân vật*: `🅑` = add bust outside the first sentence · `→X` = Host invites X · `✦` = first appearance · `⊘` = hide bust.
Last column: empty = dissolve · `✂` cut · `◼` dip to black.

**Status 06/11/2026:** script rewritten 05/11/2026 (53 elements · 171 sentences) ⇒ shot table rebuilt with **108 shots**. The old master audio was cleaned up (A11 §8), so `timeline_s_EN_t08.json` is an **estimated** timeline (`.work/_build_timeline_t08.py`) usable for stills only; re-run TTS + `build_audio3.py` before building the video."""

HEAD_JA = """## 6. DANH SÁCH SHOT — TẬP 08 (JA)

**表の読み方:** *Vai* = 話者（H フクロウ · D オオカミ · C キツネ · N1 ヒツジ · N2 ネコ）。表は**背景とグラフィックス**を定義し、バッジと半身絵は A5.4 に従う。
*Nhân vật*: `🅑` = 最初の文の外で半身絵を追加 · `→X` = ホストが X を招き入れる · `✦` = 初登場 · `⊘` = 半身絵を非表示。
最終列: 空欄 = ディゾルブ · `✂` カット · `◼` 黒フェード。

**状況 2026年11月6日:** 台本を2026年11月5日に書き直した（53要素 · 171文）ため、ショット表を**108**で再構築。旧マスター音声はA11 §8の整理で削除済みなので、`timeline_s_JA_t08.json`は**概算タイムライン**（`.work/_build_timeline_t08.py`）であり、静止画描画専用。動画制作時はTTSと`build_audio3.py`を再実行すること。"""

INTRO = {
    "vn": ("### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`\n\n"
           "Đặt `assets/brand/intro_kenh.mov` ở 0,00 s (A5.7). Không câu thoại nào thuộc intro."),
    "en": ("### CHANNEL INTRO · 0.00–22.41 s · `bgm_music_box.mp3`\n\n"
           "Place `assets/brand/intro_kenh.mov` at 0.00 s (A5.7). No spoken line belongs to the intro."),
    "ja": ("### チャンネルイントロ · 0.00–22.41秒 · `bgm_music_box.mp3`\n\n"
           "`assets/brand/intro_kenh.mov` を0.00秒に配置（A5.7）。イントロに発話はありません。"),
}

ACT_HEAD = {
    "vn": ("### HỒI {n} — {t} · nền chủ đạo `{bg}`", {
        1: "BUỔI SÁNG ĐỊNH MỆNH DƯỚI LÒNG ĐẤT TOKYO",
        2: "KHU CĂN CỨ DƯỚI CHÂN NÚI PHÚ SĨ VÀ PHÒNG THÍ NGHIỆM TỬ THẦN",
        3: "NGHỊCH LÝ CỦA CÁC THIÊN TÀI KHOA HỌC",
        4: "MA THUẬT TẨY NÃO & KHÁI NIỆM POA ĐẪM MÁU",
        5: "PHÁN QUYẾT LỊCH SỬ & BÀI HỌC VỀ SỰ TỰ DO TƯ TƯỞNG",
    }),
    "en": ("### ACT {n} — {t} · main background `{bg}`", {
        1: "A FATEFUL MORNING BENEATH THE STREETS OF TOKYO",
        2: "THE BASE AT THE FOOT OF MOUNT FUJI AND THE DEATH LABORATORY",
        3: "THE PARADOX OF SCIENTIFIC GENIUS",
        4: "BRAINWASHING AND THE POA DOCTRINE",
        5: "THE HISTORIC VERDICT & THE LESSON ON FREE THOUGHT",
    }),
    "ja": ("### 第{n}幕 — {t} · 主演背景 `{bg}`", {
        1: "東京の地下に訪れた運命の朝",
        2: "富士山の麓の巨大拠点と「死の実験室」",
        3: "エリートの科学者たちの矛盾",
        4: "洗脳の技術と「ポア」",
        5: "歴史的判決と自由思想の教訓",
    }),
}

BG_MAIN = {1: "t8_tokyo_dawn_fog", 2: "t8_mount_fuji_dawn_somber",
           3: "t8_asahara_shadow_profile", 4: "t8_poa_twisted_doctrine",
           5: "t8_tokyo_dawn_restored_peace"}

COLS_VN = "| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |"
COLS_EN = "| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |"
COLS_JA = "| Shot | Câu | Vai | Mẫu | Nền | Chữ | Beat | Nhân vật | |"
SEP = "|---|---|---|---|---|---|---|---|---|"


def build_section(lang):
    head = {"vn": HEAD_VN, "en": HEAD_EN, "ja": HEAD_JA}[lang]
    cols = {"vn": COLS_VN, "en": COLS_EN, "ja": COLS_JA}[lang]
    idx = {"vn": 5, "en": 6, "ja": 7}[lang]
    out = [head, "", INTRO[lang], ""]
    for n, rows in ACTS:
        tmpl, titles = ACT_HEAD[lang]
        out.append(tmpl.format(n=n, t=titles[n], bg=BG_MAIN[n]))
        out.append("")
        out.append(cols)
        out.append(SEP)
        for r in rows:
            sid, cau, vai, mau, nen, vn, en, ja, beat, nv, tc = r
            out.append("| " + " | ".join([sid, cau, vai, mau, nen, r[idx],
                                         beat, nv, tc]) + " |")
        out.append("")
    nshot = sum(len(r) for _, r in ACTS)
    nbg = len({r[4].split(",")[0].strip(" `") for _, rows in ACTS for r in rows
               if r[4].split(",")[0].strip(" `") not in ("void",)})
    totals = {
        "vn": (f"**Tổng:** {nshot} shot · 171 câu · 33 element lời (5 hồi) · nền dùng {nbg} loại. "
               "Bảng dựng lại 06/11/2026 theo kịch bản viết lại 05/11/2026 (53 phần tử · 171 câu)."),
        "en": (f"**Tổng:** {nshot} shot · 171 câu · 33 element lời (5 hồi) · nền dùng {nbg} loại. "
               "Rebuilt 06/11/2026 from the rewritten script of 05/11/2026 (53 elements · 171 sentences)."),
        "ja": (f"**Tổng:** {nshot} shot · 171 câu · 33 element lời (5 hồi) · nền dùng {nbg} loại. "
               "2026年11月6日、書き直し台本（53要素・171文）に合わせてショット表を再構築。"),
    }
    return "\n".join(out) + "\n", totals[lang]


def upsert(path, block):
    """Thay mục 6 (từ '## 6. DANH SÁCH SHOT' tới hết dòng '**Tổng:') — idempotent."""
    p = Path(path)
    text = p.read_text(encoding="utf-8") if p.exists() else ""
    i = text.find("## 6. DANH SÁCH SHOT")
    if i >= 0:
        j = text.find("**Tổng:", i)
        if j < 0:
            end = len(text)
        else:
            nl = text.find("\n", j)
            end = len(text) if nl < 0 else nl + 1
        text = text[:i] + block + text[end:]
    else:
        text = text.rstrip("\n") + "\n\n" + block
    p.write_text(text, encoding="utf-8")
    return p


JA_HEADER = """# 制作計画 エピソード08 · 日本語版 · 「天才たちはいかにして洗脳されたのか」

**適用基準:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A)
**台本:** `01_KICH_BAN/Tap08_JA/kichban_tap08_JA.md` · **出力先:** `02_SAN_XUAT/Tap08_JA/xuat_ban/`
**更新日:** 2026年11月6日 — 書き直し台本（53要素 / 171文）に合わせてショット表を再構築

| 項目 | 内容 |
|---|---|
| 台本 | `01_KICH_BAN/Tap08_JA/kichban_tap08_JA.md` — 53要素 · 171文 |
| 所要時間 | **1564.9 秒（26:05）** — 暫定タイムライン（再録音待ち・ Mastercard は旧版） |
| ショット | **108** · 171文 · 5幕 |
| 背景 | ノワール 2K（2112×1188 16:9）74点 |
| 表記ルール | 読み上げ文が数字で表記（`1995年` `14名` `12名`）なら画面も数字で書く |

"""

if __name__ == "__main__":
    for lang, path, header in (
        ("vn", ROOT / "02_SAN_XUAT" / "Tap08" / "KeHoach_Video_Tap08.md", ""),
        ("en", ROOT / "02_SAN_XUAT" / "Tap08_EN" / "KeHoach_Video_Tap08_EN.md", ""),
        ("ja", ROOT / "02_SAN_XUAT" / "Tap08_JA" / "KeHoach_Video_Tap08_JA.md", JA_HEADER),
    ):
        body, totals = build_section(lang)
        block = body.rstrip("\n") + "\n\n" + totals + "\n"
        p = Path(path)
        if not p.exists() and header:
            p.write_text(header, encoding="utf-8")
        p = upsert(p, block)
        n = sum(1 for l in block.splitlines() if l.startswith("| ") and l[2].split("-")[0].isdigit())
        print(f"{lang}: {p.name} · mục 6 · {n} dòng shot")
