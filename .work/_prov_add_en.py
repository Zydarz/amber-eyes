import json
from pathlib import Path

P = Path(r"D:\TEST\Gax\Audi\provenance.json")
rows = json.loads(P.read_text(encoding="utf-8"))
NEW = "assets/brand/intro_kenh_EN_t02.mov"
if any(r.get("file") == NEW for r in rows):
    print("đã có trong provenance, không thêm")
else:
    rows.append({
        "file": NEW,
        "loai": "intro kênh bản tiếng Anh — Tập 02 (22,41 s)",
        "cong_cu": ".work/make_intro.py (dựng bằng code: Pillow + ffmpeg, không dùng video bên ngoài)",
        "ngay": "2026-10-24",
        "prompt": None,
        "dieu_khoan": "Kênh sở hữu trọn vẹn — dựng bằng code, không dùng tài sản bên thứ ba",
        "kiem_tra_thuong_mai": "đạt",
    })
    P.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"đã thêm {NEW} · tổng {len(rows)} dòng")
