#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Viet lai bang shot Tap06 cho khop 154 cau hien tai + sua cot handoff.

Sua theo NOI DUNG (map cu -> moi), khong theo so thu tu.
Sau khi sua, tinh lai cot "Nhan vat": handoff luon = vai cua dong KE TIEP
(quy uoc da xac nhan o Tap04/Tap05), va dua "→X" ve dung cot (Tap06 truoc
day dat o cot chuyen tiep nen parse_shots.py doc sai -> 0 shot co handoff).
"""
import re
import shutil
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PLAN = ROOT / "02_SAN_XUAT" / "Tap06" / "KeHoach_Video_Tap06.md"
BACKUP = ROOT / ".work" / "_cu" / "t06_shottable_165cu"

# ---------------------------------------------------------------- sua noi dung
EDITS = {
    # ---------------- HOI 1
    "1-10": {
        "chu": "**HIỆU THUỐC NISSON PHARMACY** · *Cậu là một thiếu niên ngoan ngoãn, chăm chỉ*",
    },
    "1-11": {
        "cau": "`1.06#6`",
        "chu": "**KHOẢNG CHÍN GIỜ TỐI** · *Robert xin mẹ đợi thêm vài phút*",
    },
    "1-12": {
        "cau": "`1.06#7`, `1.08#1`",
        "chu": "**MỨC LƯƠNG NĂM ĐÔ LA MỘT GIỜ** · *Cao gần gấp đôi mức lương tối thiểu liên bang năm 1978*",
    },
    "1-14": {
        "chu": "**BÃI ĐỖ XE HOANG VẮNG GIỮA GIÓ TUYẾT** · *Mười phút, hai mươi phút rồi một tiếng đồng hồ trôi qua · Robert không bao giờ quay lại*",
    },
    "1-15": {   # CU LA 1-15 (N1 lan 1) -> moi 1-16
        "cau": "`1.09#1`–`#2`",
        "chu": "“Tối hôm đó, hiệu thuốc đang được sửa lại một số kệ hàng. Nhà thầu John Gacy trò chuyện khá cởi mở với nhân viên.”",
    },
    "1-16": {   # CU LA 1-16 (N1 lan 2) -> moi 1-17
        "cau": "`1.09#3`–`#5`",
        "chu": "“Robert hào hứng lắm, cậu bảo chỉ ra nói chuyện vài phút rồi sẽ về mừng sinh nhật mẹ. Nhưng Robert không quay lại… Người đàn ông vui tính ấy lại là kẻ mang đến bóng tối kinh hoàng.”",
    },
    "1-20": {   # CU LA 1-20 -> moi 1-21
        "cau": "`1.14#1`–`#2`",
        "chu": "**QUẦN ÁO DÍNH ĐẦY BÙN ĐẤT** · *Một chi tiết nhỏ lọt vào mắt các điều tra viên dày dạn*",
    },
    # ---------------- HOI 2
    "2-02": {
        "vai": "D",
        "chu": "**1968** · *Kết án mười năm tù tại thị trấn Waterloo, bang Iowa · Ân xá sớm sau mười tám tháng*",
    },
    "2-03": {"vai": "D"},
    "2-10": {"vai": "D"},
    "2-14": {
        "chu": "**MỜI CÀ PHÊ VÀ TRẢ TIỀN BỮA ĂN** · *Nụ cười rạng rỡ như thể đang tiếp đãi bạn bè*",
    },
    # ---------------- HOI 3
    "3-03": {
        "vai": "H",
        "chu": "**NẮP HẦM KỸ THUẬT PHÒNG NGỦ** · *Họ dần nhận ra điều mình lo sợ nhất có thể đã thành sự thật*",
    },
    "3-06": {   # CU LA 3-06 -> moi 3-05
        "cau": "`3.07#1`",
        "vai": "H",
        "chu": "**ÁNH ĐÈN PIN QUÉT QUA MẶT ĐẤT** · *Mặt đất phủ đầy bụi bặm*",
    },
    "3-07": {   # CU LA 3-07 -> moi 3-06
        "cau": "`3.07#2`, `3.09#1`",
        "vai": "H",
        "chu": "**MỘT SỰ THẬT KINH HOÀNG XÉ TOẠC MÀN ĐÊM** · *Đội ngũ pháp y lần lượt xác định thêm nhiều nạn nhân*",
    },
    "3-08": {   # CU LA 3-08 -> moi 3-07
        "cau": "`3.10#1`–`#4`",
        "chu": "**TỘI ÁC GIẤU NGAY DƯỚI NƠI SINH HOẠT** · *Nhu cầu kiểm soát và chiếm hữu ở mức bệnh hoạn*",
    },
    "3-09": {   # CU LA 3-09 -> moi 3-08
        "cau": "`3.11#1`–`#3`",
    },
    "3-10": {   # CU LA 3-10 -> moi 3-09
        "cau": "`3.12#1`–`#4`",
        "vai": "D",
        "chu": "**33 NẠN NHÂN** · *26 dưới sàn · 3 trong khuôn viên · 4 ở sông Des Plaines*",
    },
    # ---------------- HOI 4
    "4-02": {"vai": "D"},
    "4-03": {
        "vai": "N2",
        "chu": "“Hãy hình dung cảm giác của những sĩ quan ngồi đối diện Gacy… Hắn có thể rơi nước mắt, phân trần rằng nhân cách Jack Hanley đã làm tất cả mà hắn không hề hay biết.”",
    },
    "4-05": {
        "chu": "**CÁI TÔI ÁI KỶ BÙ ĐẮP BẤT LỰC** · *Tuổi thơ bị bạo hành và tính mục đích lập kế hoạch chi tiết*",
    },
    "4-07": {
        "chu": "**HÀNH ĐỘNG CÓ KẾ HOẠCH TỪ TRƯỚC** · *Hắn sai thợ phụ đào rãnh dưới nền nhà để che giấu tội ác*",
    },
    "4-08": {
        "cau": "`4.08#3`",
        "nen": "`t6_lawyer_office_night`",
        "chu": "**MÁNH KHÓE LỪA GẠT** · *Hắn khiến các nạn nhân mất cảnh giác*",
        "beat": "—",
    },
    "4-10": {
        "chu": "**12 · 03 · 1980** · *Bồi thẩm đoàn kết tội ba mươi ba vụ tước đoạt mạng · Phán quyết: Án tử hình*",
    },
    # ---------------- HOI 5
    "5-03": {
        "cau": "`5.02#4`",
        "chu": "**“NẠN NHÂN THỨ BA MƯƠI TƯ”** · *Gacy tự tuyên bố trong tự truyện và các đoạn ghi âm trước ngày thi hành án*",
    },
    "5-05": {
        "cau": "`5.04#1`",
        "chu": "**10 · 05 · 1994** · *Trại giam Stateville · Bản án tử hình được thi hành đối với John Wayne Gacy*",
    },
    "5-06": {
        "cau": "`5.04#2`–`#3`",
        "chu": "**LỜI CUỐI CÙNG** · *Không hề ăn năn · Chỉ một câu chửi thề thô tục · Chống đối đến hơi thở cuối cùng*",
    },
}

INSERT_AFTER = {
    "1-14": [
        "1-15", "`1.08#6`", "H", "T1", "`t6_pharmacy_counters_renovation`",
        "**TÂM TRẠNG KIM BYERS** · *Cô đồng nghiệp mười bảy tuổi của Robert ở hiệu thuốc tối hôm ấy*",
        "—", "", "",
    ],
}

DELETE = {"3-04"}     # "sáp thơm khử mùi" - noi dung da bi cat khoi kich ban

RENUMBER = {
    "1": {f"1-{i:02d}": f"1-{i+1:02d}" for i in range(15, 23)},
    "3": {f"3-{i:02d}": f"3-{i-1:02d}" for i in range(5, 12)},
}

# B2: tat ban than o cac khoanh khac nang ne
NOBUST = {"3-03", "3-04", "3-05", "3-06", "3-08", "3-09", "5-01", "5-05", "5-06"}

COL = {"cau": 1, "vai": 2, "mau": 3, "nen": 4, "chu": 5, "beat": 6, "nv": 7}
SPEAKERS = {"H", "D", "C", "N1", "N2"}


def main():
    BACKUP.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PLAN, BACKUP)
    print(f"backup -> {BACKUP}")

    lines = PLAN.read_text(encoding="utf-8-sig").split("\n")
    rows = []          # (line_index_in_source, cells)
    out = []
    seen = set()

    for ln in lines:
        m = re.match(r"^\|\s*([1-5]-\d+)\s*\|", ln)
        if not m:
            out.append(ln)
            continue
        sid = m.group(1)
        if sid in DELETE:
            seen.add(sid)
            continue                      # xoa dong
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if sid in EDITS:
            for k, v in EDITS[sid].items():
                cells[COL[k]] = v
            seen.add(sid)
        act = sid.split("-")[0]
        if act in RENUMBER and sid in RENUMBER[act]:
            cells[0] = RENUMBER[act][sid]
        out.append(("ROW", cells))
        if sid in INSERT_AFTER:
            out.append(("ROW", list(INSERT_AFTER[sid])))

    missing = set(EDITS) - seen
    if missing:
        raise SystemExit(f"khong tim thay dong can sua: {sorted(missing)}")

    # ---- tinh lai cot "Nhan vat": handoff = vai dong KE TIEP
    idx = [i for i, x in enumerate(out) if isinstance(x, tuple)]
    for n, i in enumerate(idx):
        cells = out[i][1]
        # giu phan "Nhan vat" goc (⊘ / ✦ Ten / 🅑), bo handoff sai cho
        base = re.sub(r"→[A-Z0-9+]+", "", cells[7]).strip()
        if cells[0] in NOBUST:
            base = "⊘"
        nxt = out[idx[n + 1]][1] if n + 1 < len(idx) else None
        handoff = ""
        if (cells[2] in SPEAKERS and nxt and nxt[2] in SPEAKERS
                and nxt[2] != cells[2]):
            handoff = f"→{nxt[2]}"
        cells[7] = (base + " " + handoff).strip()
        # cot chuyen tiep (cuoi): chi giu ◼, bo "→X" sai cho
        if len(cells) > 8 and "→" in cells[8]:
            cells[8] = ""

    final = []
    for x in out:
        final.append(x if isinstance(x, str) else "| " + " | ".join(x[1]) + " |")
    PLAN.write_text("\n".join(final), encoding="utf-8")
    print(f"da ghi {PLAN}")
    print(f"  sua {len(seen & set(EDITS))} dong · xoa {len(DELETE)} · chen 1 · "
          f"handoff recalc tren {len(idx)} dong")


if __name__ == "__main__":
    main()
