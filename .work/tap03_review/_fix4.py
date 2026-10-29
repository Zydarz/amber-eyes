import io
import sys

PATH = r"D:\TEST\Gax\Audi\01_KICH_BAN\Tap03\kichban_tap03_22102026.md"

with io.open(PATH, encoding="utf-8") as f:
    src = f.read()

# Restore the tape-recorder SFX that existed in the original draft (anchor for t3_tape_start)
OLD = (
    "Khi cuộc gọi bị cắt, anh ta gọi lại. Lần đầu, phía Santa Cruz không tin; lần thứ hai, Kemper nói thẳng rằng hắn sợ mình sẽ giết thêm người nữa và bảo họ cử người tới. Vài giờ sau đó, một xe tuần tra của cảnh sát Pueblo dừng lại bên bốt điện thoại. Edmund Kemper đầu thú mà không kháng cự, với ba khẩu súng và hàng trăm viên đạn trong xe.\"\n"
    "\n"
    "**CẢNH SÁT ĐỊA PHƯƠNG**"
)
NEW = (
    "Khi cuộc gọi bị cắt, anh ta gọi lại. Lần đầu, phía Santa Cruz không tin; lần thứ hai, Kemper nói thẳng rằng hắn sợ mình sẽ giết thêm người nữa và bảo họ cử người tới. Vài giờ sau đó, một xe tuần tra của cảnh sát Pueblo dừng lại bên bốt điện thoại. Edmund Kemper đầu thú mà không kháng cự, với ba khẩu súng và hàng trăm viên đạn trong xe.\"\n"
    "\n"
    "**[SFX]:** Tiếng băng ghi âm bật nhẹ \"Tách\".\n"
    "\n"
    "**CẢNH SÁT ĐỊA PHƯƠNG**"
)

n = src.count(OLD)
if n != 1:
    print(f"MATCHED {n} TIMES -> ABORT")
    sys.exit(1)
src = src.replace(OLD, NEW, 1)

with io.open(PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(src)
print("tape SFX restored")
