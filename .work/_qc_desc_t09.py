#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC chuyên sâu các file mô tả và nguồn của Tập 09 trên 4 ngôn ngữ."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

markers_vi = [
    "DƯ CHẤN XÃ HỘI",
    "VẬT HÓA NẠN NHÂN",
    "CƠ CHẾ CHIA NGĂN",
    "BẢN NGÃ ÁI KỶ SỤP ĐỔ",
    "HỆ THỐNG TỰ BÀO CHỮA",
    "NGÒI NỔ TÂM LÝ",
    "DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO",
    "QUỸ ĐẠO LEO THANG ẢO TƯỞNG 5 NẤC THANG",
    "HIỆU ỨNG HÀO QUANG",
    "NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ SINH TỒN",
]

markers_en = [
    "SOCIAL IMPACT & COLLECTIVE PARANOIA",
    "OBJECTIFICATION & EMPATHY DEFICIT",
    "COGNITIVE COMPARTMENTALIZATION & SECONDARY VICTIMS",
    "NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY",
    "TECHNIQUES OF NEUTRALIZATION",
    "PRECIPITATING TRIGGER & TIPPING POINT",
    "SIGNATURE VS. MODUS OPERANDI (MO)",
    "5-STAGE ESCALATION TRAJECTORY & TOLERANCE BUILDUP",
    "HALO EFFECT & COLLECTIVE BLIND SPOTS",
    "VICTIMOLOGY & SURVIVAL RED FLAGS",
]

markers_ja = [
    "社会的余波と集団的パラノイア",
    "被害者の客体化と共感の欠如",
    "精神の分断（区画化）と二次被害の悲劇",
    "自己愛の崩壊と病的な自己憐憫",
    "中和の技術と自己正当化",
    "心理的引き金と限界点",
    "精神的シグネチャー対手口",
    "5段階のエスカレーション軌道",
    "後光効果（ハロー効果）と社会の死角",
    "被害者学と生存のための4大レッドフラッグ",
]

markers_ko = [
    "사회적 충격과 집단적 편집증",
    "피해자의 사물화 및 공감 결여",
    "인지적 구획화와 2차 피해자의 비극",
    "나르시시즘적 붕괴와 병적 자기연민",
    "도덕적 중화 기술과 자기 정당화",
    "심리적 방아쇠와 임계점",
    "시그니처 vs 범행 수법",
    "5단계 에스컬레이션 궤적",
    "후광 효과와 사회적 맹점",
    "피해자학 및 생존을 위한 4대 레드플래그",
]

lang_checks = [
    ("VI", ROOT / "02_SAN_XUAT" / "Tap09" / "mo_ta.txt", markers_vi),
    ("EN", ROOT / "02_SAN_XUAT" / "Tap09_EN" / "description.txt", markers_en),
    ("JA", ROOT / "02_SAN_XUAT" / "Tap09_JA" / "description.txt", markers_ja),
    ("KO", ROOT / "02_SAN_XUAT" / "Tap09_KO" / "description.txt", markers_ko),
]

print("=== KIỂM ĐỊNH 10 CHỈ DẤU TÂM LÝ TRONG MÔ TẢ TẬP 09 ===")
all_pass = True

for lang, file_path, markers in lang_checks:
    text = file_path.read_text(encoding="utf-8")
    found = [m for m in markers if m in text]
    missing = [m for m in markers if m not in text]
    status = "PASS" if len(found) == 10 else "FAIL"
    if status == "FAIL":
        all_pass = False
    print(f"[{lang}] {file_path.name}: {len(found)}/10 chỉ dấu | {len(text)} ký tự | Trạng thái: {status}")
    if missing:
        print(f"       Thiếu: {missing}")

print("\n=== KIỂM ĐỊNH ĐỒNG BỘ FILE XUẤT BẢN & GỐC ===")
pairs = [
    (ROOT / "02_SAN_XUAT" / "Tap09" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap09" / "xuat_ban" / "mo_ta.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap09" / "nguon_tham_khao.md", ROOT / "02_SAN_XUAT" / "Tap09" / "xuat_ban" / "nguon_tham_khao.md"),
    (ROOT / "02_SAN_XUAT" / "Tap09_EN" / "description.txt", ROOT / "02_SAN_XUAT" / "Tap09_EN" / "xuat_ban" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap09_EN" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap09_EN" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap09_EN" / "nguon_tham_khao_EN.md", ROOT / "02_SAN_XUAT" / "Tap09_EN" / "xuat_ban" / "nguon_tham_khao_EN.md"),
    (ROOT / "02_SAN_XUAT" / "Tap09_JA" / "description.txt", ROOT / "02_SAN_XUAT" / "Tap09_JA" / "xuat_ban" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap09_JA" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap09_JA" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap09_JA" / "nguon_tham_khao_JA.md", ROOT / "02_SAN_XUAT" / "Tap09_JA" / "xuat_ban" / "nguon_tham_khao_JA.md"),
    (ROOT / "02_SAN_XUAT" / "Tap09_KO" / "description.txt", ROOT / "02_SAN_XUAT" / "Tap09_KO" / "xuat_ban" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap09_KO" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap09_KO" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap09_KO" / "nguon_tham_khao_KO.md", ROOT / "02_SAN_XUAT" / "Tap09_KO" / "xuat_ban" / "nguon_tham_khao_KO.md"),
]

for src, dst in pairs:
    src_bytes = src.read_bytes()
    dst_bytes = dst.read_bytes()
    if src_bytes == dst_bytes:
        print(f"  OK: {src.relative_to(ROOT)} == {dst.relative_to(ROOT)}")
    else:
        print(f"  DIFF: {src.relative_to(ROOT)} != {dst.relative_to(ROOT)}")
        all_pass = False

print("\n=== KIỂM ĐỊNH LINE ENDING (DOUBLE CR == 0) ===")
check_files = [
    ROOT / "02_SAN_XUAT" / "Tap09" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap09" / "nguon_mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap09" / "nguon_tham_khao.md",
    ROOT / "02_SAN_XUAT" / "Tap09_EN" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap09_EN" / "nguon_mo_ta_EN.txt",
    ROOT / "02_SAN_XUAT" / "Tap09_EN" / "nguon_tham_khao_EN.md",
    ROOT / "02_SAN_XUAT" / "Tap09_EN" / "CHU_CO_DINH_EN.md",
    ROOT / "02_SAN_XUAT" / "Tap09_JA" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap09_JA" / "nguon_mo_ta_JA.txt",
    ROOT / "02_SAN_XUAT" / "Tap09_JA" / "nguon_tham_khao_JA.md",
    ROOT / "02_SAN_XUAT" / "Tap09_KO" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap09_KO" / "nguon_mo_ta_KO.txt",
    ROOT / "02_SAN_XUAT" / "Tap09_KO" / "nguon_tham_khao_KO.md",
]

double_cr_pass = True
for f in check_files:
    raw = f.read_bytes()
    c = raw.count(b"\r\r\n")
    if c > 0:
        print(f"  LỖI DOUBLE CR ({c}): {f.relative_to(ROOT)}")
        double_cr_pass = False
        all_pass = False
if double_cr_pass:
    print(f"  ✅ 100% ({len(check_files)}/{len(check_files)}) files đạt chuẩn LF thuần (double_cr=0)")

print("\n" + "=" * 50)
if all_pass:
    print(">>> TẤT CẢ CÁC CỔNG KIỂM ĐỊNH MÔ TẢ TẬP 09: 100% PASS! <<<")
else:
    print(">>> CÓ LỖI TRONG QUÁ TRÌNH KIỂM ĐỊNH MÔ TẢ TẬP 09! <<<")
    sys.exit(1)
