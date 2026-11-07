#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC chuyên sâu các file mô tả và nguồn của Tập 12 trên cả 4 ngôn ngữ (VN, EN, JA, KO).
Đảm bảo 100% tuân thủ Hệ sinh thái 10 chỉ dấu tâm lý (A2c) và trần 5000 ký tự (YouTube).
"""

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
    "CHỮ KÝ SIGNATURE VS. THỦ ĐOẠN MO",
    "QUỸ ĐẠO LEO THANG ẢO TƯỞNG",
    "HIỆU ỨNG HÀO QUANG",
    "NẠN NHÂN HỌC & CẢNH BÁO ĐỎ SINH TỒN",
]

markers_en = [
    "SOCIAL IMPACT & COLLECTIVE PARANOIA",
    "OBJECTIFICATION OF THE VICTIM",
    "COGNITIVE COMPARTMENTALIZATION",
    "NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY",
    "TECHNIQUES OF NEUTRALIZATION & HERO COMPLEX",
    "PSYCHOLOGICAL TRIGGER & TIPPING POINT",
    "SIGNATURE VS. MODUS OPERANDI (MO)",
    "FANTASY ADDICTION & ESCALATION TRAJECTORY",
    "HALO EFFECT & COLLECTIVE BLIND SPOTS",
    "VICTIMOLOGY & SURVIVAL RED FLAGS",
]

markers_ja = [
    "社会的余波と集団的パラノイア",
    "被害者の客体化",
    "心理的区画化",
    "自己愛の崩壊",
    "自己正当化と中和の技術",
    "心理的引き金",
    "署名（Signature）対 手口（MO）",
    "妄想への耽溺とエスカレーション軌道",
    "後光効果（ハロー効果）と社会的盲点",
    "被害者学と生存のためのレッドフラッグ",
]

markers_ko = [
    "사회적 파장과 집단적 불안·파라노이아",
    "피해자의 사물화 및 객체화",
    "인지적 구획화",
    "나르시시즘적 붕괴와 병적 자기연민",
    "자기 정당화 및 중화 기술",
    "심리적 방아쇠와 티핑 포인트",
    "시그니처(Signature) vs 범행 수법(MO)",
    "환상 중독과 에스컬레이션 궤적",
    "후광 효과(Halo Effect)와 제도의 맹점",
    "피해자학 및 생존을 위한 레드플래그",
]

lang_checks = [
    ("VI", ROOT / "02_SAN_XUAT" / "Tap12" / "mo_ta.txt", markers_vi),
    ("EN", ROOT / "02_SAN_XUAT" / "Tap12_EN" / "description.txt", markers_en),
    ("JA", ROOT / "02_SAN_XUAT" / "Tap12_JA" / "description.txt", markers_ja),
    ("KO", ROOT / "02_SAN_XUAT" / "Tap12_KO" / "description.txt", markers_ko),
]

all_pass = True

print("=== 1. KIỂM ĐỊNH 10 CHỈ DẤU TÂM LÝ & ĐỘ DÀI (TRẦN <= 5000 KÝ TỰ) ===")
for lang, file_path, markers in lang_checks:
    text = file_path.read_text(encoding="utf-8")
    char_len = len(text.strip())
    found = [m for m in markers if m in text]
    missing = [m for m in markers if m not in text]
    
    len_ok = char_len <= 5000
    markers_ok = len(found) == 10
    
    if not len_ok or not markers_ok:
        all_pass = False
        status = "FAIL"
    else:
        status = "PASS"
        
    print(f"[{lang}] {file_path.name}: {len(found)}/10 chỉ dấu | {char_len:,}/5000 ký tự | {status}")
    if missing:
        print(f"       Thiếu markers: {missing}")
    if not len_ok:
        print(f"       VƯỢT TRẦN: {char_len} > 5000!")

print("\n=== 2. KIỂM ĐỊNH ĐỒNG BỘ FILE XUẤT BẢN & GỐC ===")
pairs = [
    (ROOT / "02_SAN_XUAT" / "Tap12" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap12" / "xuat_ban" / "mo_ta.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap12" / "nguon_tham_khao.md", ROOT / "02_SAN_XUAT" / "Tap12" / "xuat_ban" / "nguon_tham_khao.md"),
    (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "description.txt", ROOT / "02_SAN_XUAT" / "Tap12_EN" / "xuat_ban" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap12_EN" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "nguon_tham_khao_EN.md", ROOT / "02_SAN_XUAT" / "Tap12_EN" / "xuat_ban" / "nguon_tham_khao_EN.md"),
    (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "description.txt", ROOT / "02_SAN_XUAT" / "Tap12_JA" / "xuat_ban" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap12_JA" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "nguon_tham_khao_JA.md", ROOT / "02_SAN_XUAT" / "Tap12_JA" / "xuat_ban" / "nguon_tham_khao_JA.md"),
    (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "description.txt", ROOT / "02_SAN_XUAT" / "Tap12_KO" / "xuat_ban" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap12_KO" / "description.txt"),
    (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "nguon_tham_khao_KO.md", ROOT / "02_SAN_XUAT" / "Tap12_KO" / "xuat_ban" / "nguon_tham_khao_KO.md"),
]

for src, dst in pairs:
    match = src.read_bytes() == dst.read_bytes()
    if not match:
        all_pass = False
        print(f"  MISMATCH: {src.relative_to(ROOT)} != {dst.relative_to(ROOT)}")
    else:
        print(f"  OK: {src.relative_to(ROOT)} == {dst.relative_to(ROOT)}")

print("\n=== 3. KIỂM ĐỊNH LINE ENDING (DOUBLE CR == 0) ===")
target_files = [
    ROOT / "02_SAN_XUAT" / "Tap12" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap12" / "nguon_mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap12" / "nguon_tham_khao.md",
    ROOT / "02_SAN_XUAT" / "Tap12_EN" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap12_EN" / "nguon_mo_ta_EN.txt",
    ROOT / "02_SAN_XUAT" / "Tap12_EN" / "nguon_tham_khao_EN.md",
    ROOT / "02_SAN_XUAT" / "Tap12_JA" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap12_JA" / "nguon_mo_ta_JA.txt",
    ROOT / "02_SAN_XUAT" / "Tap12_JA" / "nguon_tham_khao_JA.md",
    ROOT / "02_SAN_XUAT" / "Tap12_KO" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap12_KO" / "nguon_mo_ta_KO.txt",
    ROOT / "02_SAN_XUAT" / "Tap12_KO" / "nguon_tham_khao_KO.md",
]

for p in target_files:
    b = p.read_bytes()
    crcrlf = b.count(b"\r\r\n")
    if crcrlf > 0:
        all_pass = False
        print(f"  LỖI DOUBLE CR: {p.relative_to(ROOT)} có {crcrlf} cặp CRCRLF")
    else:
        print(f"  OK: {p.relative_to(ROOT)} (clean LF/CRLF)")

print("\n=== 4. KIỂM ĐỊNH TỪ CẤM V9 (YOUTUBE MONETIZATION SAFETY) ===")
v9_forbidden = [
    "tự sát", "tự tử", "suicide", "chảy máu", "vết chém", "thi thể đẫm máu"
]
for lang, file_path, _ in lang_checks:
    text_lower = file_path.read_text(encoding="utf-8").lower()
    found_forbidden = [w for w in v9_forbidden if w in text_lower]
    if found_forbidden:
        # Check context
        print(f"  CẢNH BÁO TỪ KHÓA: [{lang}] {file_path.name} có từ: {found_forbidden}")
    else:
        print(f"  OK: [{lang}] {file_path.name} không có từ cấm V9")

if all_pass:
    print("\n>>> TẤT CẢ CÁC CỔNG KIỂM ĐỊNH MÔ TẢ TẬP 12: 100% PASS! <<<")
else:
    print("\n>>> CÓ LỖI TRONG KIỂM ĐỊNH MÔ TẢ TẬP 12! <<<")
    sys.exit(1)
