# -*- coding: utf-8 -*-
"""Patch vong 2 — lam ro mau thong nhat con lai trong bo text Tap 02 (sua o GENERATOR, G6)."""
import io, os, sys, shutil, datetime

GEN = r"D:/TEST/Gax/amber-eyes/.work/_build_tk_tap02.py"
BAK = r"D:/TEST/Gax/amber-eyes/.work/_cu"

REPL = [
    # NẤC 1 bản ngắn: lặp từ "rình rập... rình rập" -> lấy nhãn NẤC 1 của bản dài
    ('• NẤC 1 — rình rập ban đêm, đứng ngoài bóng tối để rình rập phụ nữ qua khung cửa sổ.',
     '• NẤC 1 — nhìn trộm ban đêm: đứng ngoài bóng tối để rình rập phụ nữ qua khung cửa sổ.', 1),
    # "82 vụ" — thong nhat voi hook ("Tám mươi hai vụ trộm") va TK3 ("82 vụ trộm đầu tiên")
    ('tổng cộng 82 vụ đột nhập và đột nhập bất thành. Hắn không lấy tiền bạc',
     'tổng cộng 82 vụ trộm đồ riêng tư. Hắn không lấy tiền bạc', 1),
    ('tổng cộng 82 vụ đột nhập và đột nhập bất thành. Không lấy tiền',
     'tổng cộng 82 vụ trộm đồ riêng tư. Không lấy tiền', 1),
]

src = io.open(GEN, encoding="utf-8").read()
out = src
bad = []
for old, new, cnt in REPL:
    got = out.count(old)
    if got != cnt:
        bad.append((old[:70], got, cnt))
    else:
        out = out.replace(old, new)

if bad:
    print("KHONG PATCH:")
    for o, g, c in bad:
        print("  [%d/%d] %s" % (g, c, o))
    sys.exit(1)

print("OK - %d cua hang khop." % len(REPL))
os.makedirs(BAK, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
bk = os.path.join(BAK, "_build_tk_tap02_%s.py" % stamp)
shutil.copy2(GEN, bk)
print("Backup:", bk)
with io.open(GEN, "w", encoding="utf-8", newline="\n") as f:
    f.write(out)
print("Da ghi:", GEN, len(out), "bytes")
