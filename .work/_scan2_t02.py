# -*- coding: utf-8 -*-
import io
s = io.open(r"D:/TEST/Gax/amber-eyes/.work/_build_tk_tap02.py", encoding="utf-8").read()
for pat in ["Hồ sơ có thật, dữ kiện có nguồn.",
            "quân hàm bị thu hồi, huân chương bị cắt",
            "hai luồng nhận thức và cảm xúc trái ngược nhau",
            '“', '”']:
    print("=== %s ===" % pat)
    for i, line in enumerate(s.splitlines(), 1):
        if pat in line:
            print("  %4d | %s" % (i, line.rstrip()[:170]))
