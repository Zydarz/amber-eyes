# -*- coding: utf-8 -*-
"""Dựng ảnh thumbnail (1280×720) cho Tập 23 — 3 ngôn ngữ: VI / EN / JA.

Chạy:  py -3 .work/_gen_thumb_t23.py

Nguyên tắc:
  * H11 — nền + chữ của ĐÚNG tập 23 (nền `thumb_bg` khai trong EPISODES["23"]).
  * A11 #148 — mỗi ngôn ngữ một cặp chữ riêng (VI / EN / JA), không in chữ VN cho bản EN/JA.
  * Chỉ gọi `package.thumbnail()` — KHÔNG gọi `package.py --mux` (tránh ghi đè mp4/mô tả
    của tập đã xuất).
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))

configs = [
    ("vi", None, ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap23" / "xuat_ban"),
    ("en", "en", ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap23_EN" / "xuat_ban"),
    ("ja", "ja", ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap23_JA" / "xuat_ban"),
]

for code, lang_env, out_dir in configs:
    os.environ["AE_EP"] = "23"
    if lang_env:
        os.environ["AE_LANG"] = lang_env
    else:
        os.environ.pop("AE_LANG", None)

    for mod in ["edition", "package"]:          # ép nạp lại theo AE_LANG/AE_EP
        sys.modules.pop(mod, None)

    import edition as ED
    import package as P

    out_dir.mkdir(parents=True, exist_ok=True)
    P.OUT_DIR = out_dir                            # trỏ đúng thư mục xuất bản của ngôn ngữ
    P.thumbnail()
    target = out_dir / "thumbnail.png"
    print(f"[{code.upper()}] thumbnail: {target}  ({target.stat().st_size:,} bytes)")
    print(f"        nền   : {ED.EP.get('thumb_bg')}")
    print(f"        chữ   : {ED.EP['thumb']}")
