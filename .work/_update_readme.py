p = 'README.md'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

target = '| **05 · Chiếc đĩa mềm màu tím** | `02_SAN_XUAT/Tap05/` — kế hoạch (83 shot), ảnh (61 nền), âm thanh, báo cáo giọng | ✅ `Tap05_master.mp4` **24:18** (1.458,1 s · 505,2 MB · 1920×1080@30 · H.264+AAC) — **giọng bộ A**, số đọc bằng chữ · **H13 đạt 100%** (khớp 3 chiều ảnh - chữ - thoại) · QC A9.1–A9.4 đạt toàn bộ (lệch hình/tiếng 0,019 s · −16,2 LUFS · giải mã 0 lỗi) · còn: nghe duyệt SFX t05 + điền nguồn |'
row_en = '| 05 EN | `02_SAN_XUAT/Tap05_EN/` | ✅ `Tap05_EN_master.mp4` **24:09** (1.449,2 s · 496,9 MB · 1920×1080@30 · H.264+AAC) — "The Purple Floppy Disk: Narcissistic Addiction & Compartmentalization (The BTK Dennis Rader Case)" · **G10 đạt** (5/5 vai 1 người, G9 tách bạch 10/10) · **H13 đạt 100%** (khớp 3 chiều ảnh - chữ tiếng Anh - thoại) · **QC A9.1–A9.4 đạt toàn bộ** (lệch hình/tiếng 0,017 s · −16,2 LUFS · 0 khoảng câm > 0,3s · giải mã 0 lỗi) · còn: điền link nguồn vào `nguon_tham_khao_EN.md` |'

if target in text:
    text = text.replace(target, target + '\n' + row_en)
    # Also update top video list
    top_target = '`02_SAN_XUAT/Tap01_EN/xuat_ban/Tap01_EN_master.mp4` (hồ sơ: `02_SAN_XUAT/Tap01_EN/README.md`)'
    top_rep = '`02_SAN_XUAT/Tap01_EN/xuat_ban/Tap01_EN_master.mp4` · `02_SAN_XUAT/Tap02_EN/xuat_ban/Tap02_EN_master.mp4` · **Tập 05 EN**: `02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp4`'
    text = text.replace(top_target, top_rep)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text)
    print('SUCCESS')
else:
    print('Target not found')
