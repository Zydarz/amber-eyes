import io
import sys

PATH = r"D:\TEST\Gax\Audi\01_KICH_BAN\Tap03\REVIEW_kichban_tap03.md"

with io.open(PATH, encoding="utf-8") as f:
    src = f.read()

R = [
    (
        "| **Kết quả parse** | 54 element · 31 LOI · 11 NGHI · 7 BGM · 5 SFX · **5.106 từ / 215 câu ≈ 25,8 phút** (mục tiêu 25–27 phút ✅) |",
        "| **Kết quả parse** | 55 element · 31 LOI · 12 NGHI · 7 BGM · 5 SFX · **5.106 từ / 215 câu ≈ 25,8 phút** (mục tiêu 25–27 phút ✅) |",
    ),
    (
        '    "n_element": {"1.08": "N1", "2.09": "N2"},',
        '    "n_element": {"1.09": "N1", "2.09": "N2"},',
    ),
    (
        "- `1.08` – viên cảnh sát trực ban (Hồi 1)",
        "- `1.09` – viên cảnh sát trực ban (Hồi 1)",
    ),
    (
        '2. **Hai lượt "CẢNH SÁT ĐỊA PHƯƠNG"** (1.08 và 2.09)',
        '2. **Hai lượt "CẢNH SÁT ĐỊA PHƯƠNG"** (1.09 và 2.09)',
    ),
    (
        "### E7. Artifact đã cập nhật ✅\n"
        "`.work/script_tap03.json` đã **parse lại từ bản sửa** (54 element). Các file cũ vẫn giữ nguyên trong `.work/tap03_review/` để đối chiếu.",
        "### E7. Artifact đã cập nhật ✅\n"
        "`.work/script_tap03.json` đã **parse lại từ bản sửa** (55 element). Các file cũ vẫn giữ nguyên trong `.work/tap03_review/` để đối chiếu.\n"
        "\n"
        "### E9. Đã đồng bộ `Danh_Sach_Anh_Tap03.md` (nhánh sản xuất chạy song song) ⚠️\n"
        "Trong lúc review, một tiến trình sản xuất song song đã sinh xong **45 ảnh nền** + `02_SAN_XUAT/Tap03/Danh_Sach_Anh_Tap03.md` dựa trên **bản kịch bản cũ**. Đã đồng bộ lại file này (48 thay thế):\n"
        "- **48 mốc câu (B2)** dịch lại theo parse mới (các element dịch chuyển vì kịch bản dài thêm).\n"
        "- **4 mô tả ảnh sửa nội dung**: địa chỉ hiện trường → *609A đường Ord Drive*; \"8 án liên tiếp\" → **thi hành đồng thời**; bỏ **Rorschach**; phiên ân xá không còn \"từ chối mọi buổi\"; \"Mùa hè 1978 / Nhà tù\" → **Năm 1978 / Cơ sở Y tế Bang California**.\n"
        "- **`t3_car_door` → KHÔNG DÙNG**: ảnh vẽ \"hai lỗ trống sau khi tháo tay nắm\" — chi tiết này không có nguồn nên đã bị loại khỏi kịch bản → ảnh mất mốc. File ảnh vẫn còn trên đĩa, không cần sinh lại.\n"
        "- Header + mục B4/B5 cập nhật số liệu và trạng thái việc còn lại.",
    ),
    (
        "| **Tổng lỗi tìm ra** | **21 lỗi fact** · **4 trích dẫn không có nguồn** · **18 chi tiết bổ sung** |",
        "| **Tổng lỗi tìm ra** | **21 lỗi fact** · **4 trích dẫn không có nguồn** · **18 chi tiết bổ sung** · **48 mốc câu trong manifest sản xuất đã đồng bộ lại** |",
    ),
]

for i, (old, new) in enumerate(R, 1):
    n = src.count(old)
    if n != 1:
        print(f"REPL {i}: MATCHED {n} TIMES -> ABORT")
        print("  old:", old[:120])
        sys.exit(1)
    src = src.replace(old, new, 1)
    print(f"REPL {i}: ok")

with io.open(PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(src)
print("review updated")
