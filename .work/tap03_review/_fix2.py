import io
import sys

PATH = r"D:\TEST\Gax\Audi\01_KICH_BAN\Tap03\kichban_tap03_22102026.md"

with io.open(PATH, encoding="utf-8") as f:
    src = f.read()

FIXES = [
    # 1) English original in quotes would be read by the VI voice -> use VI rendering in quotes,
    #    keep the English original in nguon_tham_khao.md
    (
        "Trong hồ sơ lưu trữ của tạp chí Inside Detective số tháng 8 năm 1973, lời khai của chính Kemper được ghi lại nguyên văn:\n"
        "*'I killed my mother and her friend. And I killed those college girls. I killed six of them and I can show you where I hid the pieces of their bodies.'*\n"
        "'Tôi đã giết mẹ tôi và người bạn của bà. Và tôi đã giết mấy cô nữ sinh đó. Sáu người. Tôi có thể chỉ cho các anh biết tôi đã chôn những mảnh vụn của họ ở đâu.'",
        "Trong hồ sơ lưu trữ của tạp chí Inside Detective số tháng 8 năm 1973, lời khai của chính Kemper được ghi lại nguyên văn:\n"
        "*'Tôi đã giết mẹ tôi và người bạn của bà. Và tôi đã giết mấy cô nữ sinh đó. Sáu người. Tôi có thể chỉ cho các anh biết tôi đã chôn những mảnh vụn của họ ở đâu.'*",
    ),
    # 2) English quote -> VI rendering (verbatim English kept in nguon_tham_khao.md)
    (
        "Kemper gọi ông là 'more like a father to me than anyone I have ever known'.",
        "Kemper gọi ông là 'với tôi, ông ấy còn giống một người cha hơn bất kỳ ai tôi từng biết'.",
    ),
    # 3) unsourced quote from the original draft -> reported speech, no quote marks
    (
        "Sự ngược đãi tinh thần có hệ thống ấy đã gieo vào tâm trí một đứa trẻ một thông điệp độc hại: *'Mày là một sinh vật quái dị, đáng tởm và không xứng đáng tồn tại.'*",
        "Sự ngược đãi tinh thần có hệ thống ấy đã gieo vào tâm trí một đứa trẻ một thông điệp độc hại: hắn là một sinh vật quái dị, đáng tởm và không xứng đáng tồn tại.",
    ),
]

for i, (old, new) in enumerate(FIXES, 1):
    n = src.count(old)
    if n != 1:
        print(f"FIX {i}: MATCHED {n} TIMES -> ABORT")
        print("  old:", old[:110])
        sys.exit(1)
    src = src.replace(old, new, 1)
    print(f"FIX {i}: ok")

with io.open(PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(src)
print("written")
