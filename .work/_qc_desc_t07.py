#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC chuyên sâu các file mô tả và nguồn của Tập 07 trên 4 ngôn ngữ."""

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
    ("VI", ROOT / "02_SAN_XUAT" / "Tap07" / "mo_ta.txt", markers_vi),
    ("EN", ROOT / "02_SAN_XUAT" / "Tap07_EN" / "description.txt", markers_en),
    ("JA", ROOT / "02_SAN_XUAT" / "Tap07_JA" / "description.txt", markers_ja),
    ("KO", ROOT / "02_SAN_XUAT" / "Tap07_KO" / "description.txt", markers_ko),
]

print("=== KIỂM ĐỊNH 10 CHỈ DẤU TÂM LÝ TRONG MÔ TẢ TẬP 07 ===")
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

print("\n=== KIỂM ĐỊNH ĐỒNG BỘ NGUỒN VÀ FILE XUẤT BẢN ===")
target_files = [
    ROOT / "02_SAN_XUAT" / "Tap07" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap07" / "nguon_mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap07" / "nguon_tham_khao.md",
    ROOT / "02_SAN_XUAT" / "Tap07_EN" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_EN" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_EN" / "xuat_ban" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_EN" / "xuat_ban" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_EN" / "nguon_mo_ta_EN.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_EN" / "nguon_tham_khao_EN.md",
    ROOT / "02_SAN_XUAT" / "Tap07_JA" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_JA" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_JA" / "xuat_ban" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_JA" / "xuat_ban" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_JA" / "nguon_mo_ta_JA.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_JA" / "nguon_tham_khao_JA.md",
    ROOT / "02_SAN_XUAT" / "Tap07_KO" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_KO" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_KO" / "xuat_ban" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_KO" / "xuat_ban" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_KO" / "nguon_mo_ta_KO.txt",
    ROOT / "02_SAN_XUAT" / "Tap07_KO" / "nguon_tham_khao_KO.md",
]

crlf_double_errors = []
for p in target_files:
    raw = p.read_bytes()
    if b"\r\r\n" in raw:
        crlf_double_errors.append(str(p))

if crlf_double_errors:
    print(f"LỖI T19 (CRLF doubling): {crlf_double_errors}")
    all_pass = False
else:
    print(f"✅ 100% ({len(target_files)}/{len(target_files)}) files không bị lỗi double CR (\\r\\r\\n)")

print(f"\nKẾT QUẢ TỔNG THỂ TẬP 07: {'✅ ĐẠT 100% TIÊU CHUẨN MỚI' if all_pass else '❌ CÓ LỖI'}")
