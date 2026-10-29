"""Sinh riêng thumbnail + bảng nguồn EN (không cần video/timeline cuối).

python .work/_make_thumb_en.py
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"D:\TEST\Gax\Audi\.work")
import package as P  # noqa: E402

P.OUT_DIR.mkdir(parents=True, exist_ok=True)
P.thumbnail()
print("thumbnail ->", P.OUT_DIR / "thumbnail.png")
P.write_sources_en()
print("nguon tham chieu ->", P.ED.EP_DIR / "nguon_tham_khao_EN.md")
