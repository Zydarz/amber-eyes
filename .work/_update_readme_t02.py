import re
from pathlib import Path

readme_p = Path("README.md")
text = readme_p.read_text(encoding="utf-8")

lines = text.splitlines()
new_lines = []
for l in lines:
    if "02 · Đại tá hai mặt" in l:
        new_lines.append("| **02 · Đại tá hai mặt** | `02_SAN_XUAT/Tap02/` — kế hoạch (161 shot), ảnh (37 nền), âm thanh master | ✅ `Tap02_master.mp4` **25:19** (1.519,07 s · 525,7 MB · 1920×1080@30 · H.264+AAC) — **bản 10 chỉ dấu tâm lý & 4 bậc thang vực thẳm** · dựng lại 05/11/2026 · **QC đạt toàn bộ 10/10 cổng**: lệch hình/tiếng 0,017 s (17,2 ms) · −16,3 LUFS · đỉnh âm lượng −2,0 dB · giải mã 0 lỗi · 0 khoảng lặng · thẻ kết shot 5-36 hoàn chỉnh · phụ đề 408 cue · còn: điền link nguồn + nghe toàn tập |")
    else:
        new_lines.append(l)

readme_p.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
print("README.md updated successfully!")
