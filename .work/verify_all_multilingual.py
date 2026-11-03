#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra toàn diện 116 bộ tài nguyên mô tả & nguồn của 29 tập trên 4 ngôn ngữ."""
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

languages = ["VI", "EN", "JA", "KO"]
total_checks = 0
passed_checks = 0
failed_episodes = []

for i in range(1, 30):
    ep = f"{i:02d}"
    for lang in languages:
        total_checks += 1
        if lang == "VI":
            ep_dir = ROOT / "02_SAN_XUAT" / f"Tap{ep}"
            desc_file = ep_dir / "mo_ta.txt"
            xb_desc = ep_dir / "xuat_ban" / "mo_ta.txt"
            src_md = ep_dir / "nguon_tham_khao.md"
        else:
            ep_dir = ROOT / "02_SAN_XUAT" / f"Tap{ep}_{lang}"
            desc_file = ep_dir / "description.txt"
            xb_desc = ep_dir / "xuat_ban" / "description.txt"
            src_md = ep_dir / f"nguon_tham_khao_{lang}.md"

        if not (desc_file.exists() and xb_desc.exists() and src_md.exists()):
            failed_episodes.append((ep, lang, "MISSING_FILES"))
            continue

        c = desc_file.read_text(encoding="utf-8")
        
        # Kiểm tra placeholder chưa có nguồn
        has_placeholder = any(p in c for p in ["[CHƯA CÓ", "[CHUA CO", "[PENDING", "[未確認", "[출처 미확인"])
        has_chap = "⏱" in c
        has_note = "⚠️" in c
        has_src = "📚" in c
        has_hotline = "🆘" in c
        has_hash = "#" in c

        if has_placeholder or not (has_chap and has_note and has_src and has_hotline and has_hash):
            failed_episodes.append((ep, lang, "CONTENT_FAIL"))
        else:
            passed_checks += 1

print(f"Tổng số bản kiểm tra: {total_checks} (29 tập x 4 ngôn ngữ)")
print(f"Số bản ĐẠT CHUẨN:    {passed_checks}/{total_checks}")

if failed_episodes:
    print(f"LỖI ({len(failed_episodes)}):", failed_episodes)
else:
    print("KẾT LUẬN: 100% ĐẠT CHUẨN TRÊN CẢ 4 NGÔN NGỮ (VI, EN, JA, KO)!")
