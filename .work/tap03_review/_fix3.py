import io
import sys

PATH = r"D:\TEST\Gax\Audi\01_KICH_BAN\Tap03\REVIEW_kichban_tap03.md"

with io.open(PATH, encoding="utf-8") as f:
    src = f.read()

FIXES = [
    (
        "| **Kết quả parse** | 54 element · 31 LOI · 11 NGHI · 7 BGM · 5 SFX · **5.133 từ / 218 câu ≈ 25,9 phút** (mục tiêu 25–27 phút ✅) |",
        "| **Kết quả parse** | 54 element · 31 LOI · 11 NGHI · 7 BGM · 5 SFX · **5.106 từ / 215 câu ≈ 25,8 phút** (mục tiêu 25–27 phút ✅) |\n"
        "| **Danh mục nguồn** | `02_SAN_XUAT/Tap03/xuat_ban/nguon_tham_khao.md` – 19 câu cần link + phụ lục nguyên văn tiếng Anh (đã tạo, chờ người dùng điền link) |",
    ),
    (
        "- Bản đã sửa: **5.133 từ / 218 câu ≈ 25,9 phút** (3,30 từ/giây theo hiệu chuẩn Tập 01) ✅ vừa khung.",
        "- Bản đã sửa: **5.106 từ / 215 câu ≈ 25,8 phút** (3,30 từ/giây theo hiệu chuẩn Tập 01) ✅ vừa khung.",
    ),
    (
        "### E7. Artifact đã cập nhật ✅\n"
        "`.work/script_tap03.json` đã **parse lại từ bản sửa** (84.357 bytes, 54 element). Các file cũ vẫn giữ nguyên trong `.work/tap03_review/` để đối chiếu.",
        "### E7. Artifact đã cập nhật ✅\n"
        "`.work/script_tap03.json` đã **parse lại từ bản sửa** (54 element). Các file cũ vẫn giữ nguyên trong `.work/tap03_review/` để đối chiếu.\n"
        "\n"
        "### E8. Quy ước trích dẫn + lỗi TTS tiếng Anh ⚠️ (đã xử lý)\n"
        "`tts_sentences.py` chỉ **bỏ dấu nháy**, vẫn đọc toàn bộ phần chữ trong ngoặc. Nghĩa là **đặt bản tiếng Anh nguyên văn trong dấu nháy sẽ bị giọng TTS tiếng Việt đọc sai**.\n"
        "Bản gốc (và bản sửa lần đầu của tôi) đặt nguyên văn tiếng Anh trong ngoặc → sai quy trình. Đã sửa theo đúng quy ước Tập 01/02: **trong dấu nháy là tiếng Việt**, còn **nguyên văn tiếng Anh nằm ở `02_SAN_XUAT/Tap03/xuat_ban/nguon_tham_khao.md`** (phụ lục) cho builder dựng thẻ chữ trích và cho người dùng điền link.\n"
        "Đã quét lại toàn bộ 11 dấu nháy trong kịch bản: không còn câu tiếng Anh nào nằm trong ngoặc (trừ tên riêng `Big Ed`, `Sally`).",
    ),
    (
        "1. **Link nguồn cho các trích dẫn mới** — 8 câu nguyên văn mới phải vào `nguon_tham_khao.md`:\n"
        "   `1.05` (Inside Detective confession) · `1.07` (*\"Stop me. I'm an inch from doing it again\"*) · `3.08` (quote \"Hello, I'm the coed killer\") · `4.05` (3 câu của Douglas) · `4.05` (lý do Kemper muốn khai) · `5.02` (quote 1988) · `5.08` (quote về Bruce Colomy).",
        "1. **Link nguồn cho 19 câu** — đã tạo sẵn `02_SAN_XUAT/Tap03/xuat_ban/nguon_tham_khao.md` (đúng format Tập 01) kèm **phụ lục nguyên văn tiếng Anh + nơi xuất bản** đã đối chiếu. Chỉ cần dán link công khai vào cột trống là xong.",
    ),
]

for i, (old, new) in enumerate(FIXES, 1):
    n = src.count(old)
    if n != 1:
        print(f"FIX {i}: MATCHED {n} TIMES -> ABORT")
        print("  old:", old[:120])
        sys.exit(1)
    src = src.replace(old, new, 1)
    print(f"FIX {i}: ok")

with io.open(PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(src)
print("written")
