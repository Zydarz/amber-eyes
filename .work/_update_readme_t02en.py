from pathlib import Path

p = Path("README.md")
c = p.read_text(encoding="utf-8")
lines = c.splitlines(True)

for i, l in enumerate(lines):
    if l.startswith("| 02 EN |") or l.startswith("| **02 EN** |"):
        lines[i] = (
            '| **02 EN** | `02_SAN_XUAT/Tap02_EN/` | ✅ `Tap02_EN_master.mp4` **23:17** '
            '(1.396,9 s · 505,3 MB · 1920x1080@30 · 41.907 frame · H.264+AAC) — '
            '"Ep. 02: A Predator Disguised as Honor" · **giọng Higgs Audio v3** '
            '(vai D `English_Trustworth_Man`) · **G10 ĐẠT** (5/5 vai 1 người) · '
            '**QC 10/10 cổng đạt toàn bộ** (lệch hình/tiếng **10,7 ms** · -16,4 LUFS · '
            'peak -2,9 dBFS · giải mã 0 lỗi · 0 khoảng câm) · `BaoCao_QC_Tap02_EN_MasterVideo_20261105.md` |\n'
        )
        break

p.write_text("".join(lines), encoding="utf-8")
print("README.md updated successfully!")
