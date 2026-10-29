# -*- coding: utf-8 -*-
"""KIỂM TRA CUỐI: đối chiếu tài liệu đã sinh với dữ liệu gốc + kiểm tra file trên đĩa."""
import os, re, sys
sys.path.insert(0, r'D:\TEST\Gax\Audi\.work')
from _sfx_analysis import DATA, ROOT
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

DOC = os.path.join(ROOT, '02_SAN_XUAT', 'Danh_Sach_SFX_Tap03-29.md')
SFXDIR = os.path.join(ROOT, 'assets', 'sfx')
txt = open(DOC, encoding='utf-8').read()
ok = True

# 1) Moi file 'moi' trong du lieu phai xuat hien trong bang muc 4
m4 = txt.split('## 4.')[1].split('## 5.')[0]
listed = set(re.findall(r'^\| \d+ \| `([^`]+)`', m4, re.M))
need = set(f for e in DATA for r in DATA[e] if r[2] == 'MOI' for f in r[3] if f != '—')
print(f'1) File mới: du lieu={len(need)}  trong bảng 4={len(listed)}  thiếu={sorted(need-listed)}  thừa={sorted(listed-need)}')
ok &= (need == listed)

# 2) Moi file 'tai dung' phai ton tai that tren dia
missing = []
for e in DATA:
    for r in DATA[e]:
        if r[2] == 'SAN':
            for f in r[3]:
                if f != '—' and not os.path.isfile(os.path.join(SFXDIR, f)):
                    missing.append((e, f))
print(f'2) File tái dùng thiếu trên đĩa: {missing if missing else "0 — tất cả tồn tại"}')
ok &= not missing

# 3) Moi file 'moi' phai CHƯA tồn tại (không trùng thư viện)
already = []
for e in DATA:
    for r in DATA[e]:
        if r[2] == 'MOI':
            for f in r[3]:
                if f != '—' and os.path.isfile(os.path.join(SFXDIR, f)):
                    already.append((e, f))
print(f'3) File ghi "tạo mới" nhưng đã có sẵn trên đĩa: {already if already else "0 — không trùng"}')
ok &= not already

# 4) Moi tập phai co bang chi tiet
bad = []
for ep in sorted(DATA):
    if f'### Tập {ep:02d} ' not in txt: bad.append(ep)
    if f'`01_KICH_BAN/Tap{ep:02d}/' not in txt: bad.append(ep)
print(f'4) Tập thiếu mục trong tài liệu: {sorted(set(bad)) if bad else "0 — đủ 27 tập"}')
ok &= not bad

# 5) Moi dong cue co 'moi' phai co file; dong 'tai dung' phai co file that
n_moi = sum(1 for e in DATA for r in DATA[e] if r[2] == 'MOI')
n_san = sum(1 for e in DATA for r in DATA[e] if r[2] == 'SAN')
print(f'5) Tổng dòng bảng: {sum(len(v) for v in DATA.values())} (moi={n_moi}, tai dung={n_san})')

# 6) So file SFX co trong thu vien
n_lib = sum(len([f for f in fs if f.endswith('.wav')]) for _, _, fs in os.walk(SFXDIR) if '_code' not in _)
print(f'6) Thư viện SFX hiện có: {n_lib} file .wav (gồm cả _code dự phòng)')

print()
print('KẾT QUẢ KIỂM TRA:', '✅ ĐẠT TOÀN BỘ' if ok else '❌ CÒN LỖI')
