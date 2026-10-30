#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bổ sung dòng provenance cho tài sản chưa có hồ sơ.

Phát hiện bằng kiểm toán 23/10/2026: 346 file trong assets/ chưa có dòng,
trong đó quan trọng nhất là **9 file nhạc nền** (assets/bgm/) — A10 dựa vào
provenance để kháng nghị khi bị Content ID nhận nhầm, nên thiếu dòng là mất
lớp bảo vệ đầu tiên. Các nhóm còn lại: linh thú (P0/full/mascot), ảnh gốc
chưa cắt của nền Tập 02, bản dự phòng SFX, bộ nhận diện kênh, SFX Tập 01.

Script chỉ GHI THÊM dòng cho file chưa có; không sửa dòng cũ.
Chạy: python .work/_prov_backfill.py
"""
import json
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
PROV = ROOT / "provenance.json"

prov = json.loads(PROV.read_text(encoding="utf-8"))
seen = {p.get("file") for p in prov}
added = []


def day(p: Path) -> str:
    return date.fromtimestamp(p.stat().st_mtime).isoformat()


def add(rel: str, rec: dict):
    if rel in seen:
        return
    rec = {"file": rel, **rec}
    prov.append(rec)
    seen.add(rel)
    added.append(rel)


# ---------------------------------------------------------------- 1. nhạc nền
BGM_DESC = {
    "bgm_music_box": "intro kênh (22,41 s)",
    "bgm_cello_sad": "Hồi 1 · cello u ám",
    "bgm_cello_sad_v2": "Hồi 3 · cello biến thể",
    "bgm_piano_minimal": "Hồi 2 · piano lạnh lẽo",
    "bgm_piano_minimal_v2": "Hồi 2 · piano biến thể",
    "bgm_piano_warm": "Hồi 5 · piano ấm + đoạn kết",
    "bgm_sub_drone": "Hồi 4 · sub-bass drone",
    "bgm_ambient_deep": "nền trầm lặp xuyên tập (chỉ đoạn 0,5–13,4 s)",
    "bgm_violin_heart": "Tập 01 · violin",
}
for p in sorted((ROOT / "assets" / "bgm").glob("*.mp3")):
    stem = p.stem
    add(f"assets/bgm/{p.name}", {
        "loai": "nhạc nền (BGM)",
        "cong_cu": "MiniMax Music — sinh nhạc qua mcode-tools",
        "ngay": day(p),
        "prompt": None,
        "mo_ta": BGM_DESC.get(stem, "nhạc nền kênh"),
        "dieu_khoan": "Sinh bằng MiniMax — PHẢI kiểm tra điều khoản thương mại của MiniMax trước khi bật kiếm tiền (A13); nhạc AI có thể bị Content ID nhận nhầm",
        "kiem_tra_thuong_mai": "chưa",
    })

# ---------------------------------------------------------------- 2. linh thú
for role in ("H", "D", "C", "N1", "N2"):
    for sub in ("P0", "full"):
        p = ROOT / "assets" / "cast" / role / f"{sub}.png"
        if p.exists():
            add(f"assets/cast/{role}/{sub}.png", {
                "loai": "linh thú (tách nền)",
                "cong_cu": "Ảnh người dùng tạo + rembg BiRefNet, .work/make_cast_cutouts.py",
                "ngay": day(p),
                "prompt": "<người dùng cung cấp>",
                "dieu_khoan": "<công cụ người dùng đã dùng — cần bổ sung>",
                "kiem_tra_thuong_mai": "chưa",
            })

for p in sorted((ROOT / "assets" / "cast").glob("*_mascot.png")):
    add(f"assets/cast/{p.name}", {
        "loai": "linh thú (ảnh gốc)",
        "cong_cu": "Ảnh người dùng tạo + rembg BiRefNet, .work/make_cast_cutouts.py",
        "ngay": day(p),
        "prompt": "<người dùng cung cấp>",
        "dieu_khoan": "<công cụ người dùng đã dùng — cần bổ sung>",
        "kiem_tra_thuong_mai": "chưa",
    })

for p in sorted((ROOT / "assets" / "cast" / "silhouettes").glob("*.jpg")):
    add(f"assets/cast/silhouettes/{p.name}", {
        "loai": "bóng người (Tập 01)",
        "cong_cu": "Cắt từ nền sinh ảnh của Tập 01 (assets/bg/*.png)",
        "ngay": day(p),
        "prompt": None,
        "dieu_khoan": "Kế thừa điều khoản của ảnh nền gốc (sinh bằng MiniMax) — kiểm tra cùng ảnh nền",
        "kiem_tra_thuong_mai": "chưa",
        "ghi_chu": "Bóng người trong vụ án; mặt chìm hoàn toàn (V5)",
    })

# ---------------------------------------------------------------- 3. ảnh gốc nền Tập 02
raw = ROOT / "assets" / "bg" / "_raw"
for p in sorted(raw.glob("t2_*")):
    final = ROOT / "assets" / "bg" / f"{p.stem}.png"
    add(f"assets/bg/_raw/{p.name}", {
        "loai": "ảnh gốc chưa cắt của nền Tập 02",
        "cong_cu": "connector__matrix__generate_image (MiniMax qua mcode-tools)",
        "ngay": day(p),
        "prompt": "xem dòng provenance của ảnh đã cắt: assets/bg/" + p.stem + ".png",
        "dieu_khoan": "Sinh bằng MiniMax — kiểm tra điều khoản thương mại cùng ảnh đã cắt",
        "kiem_tra_thuong_mai": "chưa",
        "cat_goc": f"assets/bg/{p.stem}.png" if final.exists() else None,
    })

# ---------------------------------------------------------------- 4. SFX tự tổng hợp
for p in sorted((ROOT / "assets" / "sfx").glob("*.wav")):
    add(f"assets/sfx/{p.name}", {
        "loai": "hiệu ứng âm thanh (SFX)",
        "cong_cu": ".work/make_sfx.py (tổng hợp bằng numpy: modal synthesis + lọc băng FFT)",
        "ngay": day(p),
        "prompt": None,
        "mo_ta": f"tiếng động '{p.stem}'",
        "dieu_khoan": "Kênh tự tạo bằng code, không dùng AI hay tài sản bên thứ ba",
        "kiem_tra_thuong_mai": "đạt",
    })
for p in sorted((ROOT / "assets" / "sfx" / "t2" / "_code").glob("*.wav")):
    add(f"assets/sfx/t2/_code/{p.name}", {
        "loai": "SFX Tập 02 — bản tự tổng hợp dự phòng",
        "cong_cu": ".work/make_sfx3.py (tổng hợp bằng numpy/scipy)",
        "ngay": day(p),
        "prompt": None,
        "mo_ta": f"bản code dự phòng của '{p.stem}'",
        "dieu_khoan": "Kênh tự tạo bằng code, không dùng AI hay tài sản bên thứ ba",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "Bản dự phòng khi file tải về bị sai; dùng để quay lại",
    })

# ---------------------------------------------------------------- 5. bộ nhận diện kênh
for p in sorted((ROOT / "assets" / "brand").glob("*.png")):
    add(f"assets/brand/{p.name}", {
        "loai": "nhận diện kênh",
        "cong_cu": ".work/make_logo.py (vẽ bằng code: Pillow, không dùng mẫu bên ngoài)",
        "ngay": day(p),
        "prompt": None,
        "font": "Georgia / Segoe UI (logo chỉ dùng chữ không dấu)",
        "dieu_khoan": "Kênh sở hữu trọn vẹn — vẽ bằng code, không dùng tài sản bên thứ ba",
        "kiem_tra_thuong_mai": "đạt",
    })
for name in ("intro_kenh.mov", "intro_kenh_EN.mov", "intro_preview.mp4", "intro_preview_EN.mp4"):
    p = ROOT / "assets" / "brand" / name
    if p.exists():
        add(f"assets/brand/{name}", {
            "loai": "intro kênh (22,41 s)",
            "cong_cu": ".work/make_intro.py (dựng bằng code: Pillow + ffmpeg, không dùng video bên ngoài)",
            "ngay": day(p),
            "prompt": None,
            "dieu_khoan": "Kênh sở hữu trọn vẹn — dựng bằng code, không dùng tài sản bên thứ ba",
            "kiem_tra_thuong_mai": "đạt",
        })
p = ROOT / "assets" / "brand" / "channel.json"
if p.exists():
    add("assets/brand/channel.json", {
        "loai": "cấu hình kênh",
        "cong_cu": "viết tay (cấu hình nội bộ)",
        "ngay": day(p),
        "prompt": None,
        "dieu_khoan": "Dữ liệu nội bộ của kênh",
        "kiem_tra_thuong_mai": "đạt",
    })

# ---------------------------------------------------------------- 6. ảnh người dùng cung cấp
for p in sorted((ROOT / "assets" / "photos").rglob("*")):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT).as_posix()
    add(rel, {
        "loai": "ảnh tham chiếu do người dùng cung cấp",
        "cong_cu": "người dùng cung cấp (không dùng AI)",
        "ngay": day(p),
        "prompt": None,
        "dieu_khoan": "Do người dùng cung cấp — kênh có quyền sử dụng theo thoả thuận với người dùng",
        "kiem_tra_thuong_mai": "chưa",
        "ghi_chu": "Ảnh gốc tham chiếu; bản dùng trong video đã được sinh bằng MiniMax",
    })

# ---------------------------------------------------------------- ghi
import shutil  # noqa: E402
BAK = ROOT / ".work" / "provenance.backup_23102026.json"
if not BAK.exists():
    shutil.copy2(PROV, BAK)
    print(f"sao luu sổ cũ -> {BAK.relative_to(ROOT)}")
PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"provenance.json: {len(prov)} dong (them {len(added)})")
from collections import Counter  # noqa: E402
c = Counter(a.split("/")[1] for a in added)
for k, v in sorted(c.items()):
    print(f"   {k}: +{v}")
