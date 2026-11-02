#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sua ban shot T03 cho khop cau thoai (H6/V3) sau khi kich ban doi so cau (V9)."""
import re, sys
from pathlib import Path

PLAN = Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03\KeHoach_Video_Tap03.md")
text = PLAN.read_text(encoding="utf-8-sig")

FIXES = [
    # ---- 1) So ngay: bo dem 0 de khop cau (A9.2) -------------------------
    ("| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t3_case_file` | **24 · 04 · 1973** · *Bốn giờ sáng · Pueblo, Colorado*",
     "| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t3_case_file` | **24 · 4 · 1973** · *Bốn giờ sáng · Pueblo, Colorado*"),

    # ---- 2) 1.13: '36' noi sai cau -> chuyen sang shot nao doc cau do ------
    ("| 1-24 | `1.13#5`–`#6` | D | T2 | `t3_fbi_corridor` | *BSU · FBI* · **DỰ ÁN NGHIÊN CỨU TÍNH CÁCH TỘI PHẠM** · *36 can phạm giết người tình dục*",
     "| 1-24 | `1.13#5`–`#6` | D | T2 | `t3_fbi_corridor` | *BSU · FBI* · **DỰ ÁN NGHIÊN CỨU TÍNH CÁCH TỘI PHẠM** · *Ca nghiên cứu đầu tiên*"),
    ("| 1-25 | `1.13#7`–`#9` | D | T8 | `t3_case_file` | *Nền móng xây dựng mạng lưới VICAP 1985 · Quy chuẩn hóa khoa học lập hồ sơ tội phạm*",
     "| 1-25 | `1.13#7`–`#9` | D | T8 | `t3_case_file` | *36 đối tượng giết người tình dục · Nền móng xây dựng mạng lưới VICAP · Hệ thống khoa học quy chuẩn*"),

    # ---- 3) 2.04: 'THANG 5 · 1972' noi truoc khi cau do doc -------------
    ("| 2-04 | `2.04#1`–`#2` | H | T2 | `t3_case_photos` | *THÁNG 5 · 1972* · **HỒ SƠ CÁC NẠN NHÂN MẤT TÍCH**",
     "| 2-04 | `2.04#1`–`#2` | H | T2 | `t3_case_photos` | **HỒ SƠ CÁC NẠN NHÂN MẤT TÍCH** · *Sáu nạn nhân trong chuỗi án mạng*"),

    # ---- 4) 2.04 #3-#6: ngay khop 'Ngày ...' de hien dung luc doc -------
    ("| 2-05 | `2.04#3`–`#4` | H | T8 | `t3_santacruz_street` | *07 · 05 · 1972: Mary Ann Pesce & Anita Luchessa (18 tuổi) · Nhốt vào cốp xe*",
     "| 2-05 | `2.04#3`–`#4` | H | T8 | `t3_santacruz_street` | *Ngày 7 · 5 · 1972: Mary Ann Pesce & Anita Luchessa (18 tuổi) · Nhốt người kia vào cốp xe*"),
    ("| 2-06 | `2.04#5`–`#6` | H | T8 | `t3_case_photos` | *14 · 09 · 1972: Aiko Koo (15 tuổi) · 07 · 01 · 1973: Cindy Schall (18 tuổi)*",
     "| 2-06 | `2.04#5`–`#6` | H | T8 | `t3_case_photos` | *Ngày 14 · 9 · 1972: Aiko Koo (15 tuổi) · Ngày 7 · 1 · 1973: Cindy Schall (18 tuổi)*"),

    # ---- 5) 3.05: 'TANG 01' phai trung voi cau 'Tang thu nhat' (#3) ------
    ("| 3-04 | `3.05#1`–`#3` | C | T2 | `t3_mother_shadow` | *CHẤN THƯƠNG MẪU HỆ ĐỘC HẠI* · **BÀ CLARNELL STRANDBERG** · *Khí chất độc đoán, áp chế*",
     "| 3-04 | `3.05#1`–`#2` | C | T2 | `t3_mother_shadow` | *CHẤN THƯƠNG MẪU HỆ ĐỘC HẠI* · **3 TẦNG CƠ CHẾ** · *Nhân cách chống đối xã hội bẩm sinh*"),
    ("| 3-05 | `3.05#4`–`#5` | C | T9 `1/3` | `t3_coal_furnace` | **TẦNG 01: CĂN NGỤC DƯỚI TẦNG HẦM** · *Sự thiến hoạn tâm lý (Psychological Castration)*",
     "| 3-05 | `3.05#3`–`#5` | C | T9 `1/3` | `t3_coal_furnace` | **TẦNG 01: CĂN NGỤC DƯỚI TẦNG HẦM** · *Sự thiến hoạn tâm lý (Psychological Castration)* → **BÀ CLARNELL STRANDBERG** · *Khí chất độc đoán, áp chế*"),

    # ---- 6) 3.10/3.11: cau 'tang thu ba' nam o 3.10 (Host) --------------
    ("| 3-16 | `3.10#1` | H | T1 | `t3_brain_mirror` | **ĐIỀU LÀM NÊN SỰ KHÁC BIỆT HOÀN TOÀN GIỮA KEMPER VÀ KẺ KHÁC?**",
     "| 3-16 | `3.10#1` | H | T1 | `t3_brain_mirror` | *TẦNG 03* · **ĐIỀU LÀM NÊN SỰ KHÁC BIỆT HOÀN TOÀN GIỮA KEMPER VÀ KẺ KHÁC?**"),
    ("| 3-17 | `3.11#1`–`#3` | C | T9 `3/3` | `t3_self_observation` | **TẦNG 03: PHÂN LY TRÍ TUỆ** · *Kẻ thái nhân cách tự phản tỉnh (The Introspective Psychopath)*",
     "| 3-17 | `3.11#1`–`#3` | C | T9 `3/3` | `t3_self_observation` | **PHÂN LY TRÍ TUỆ** · *Kẻ thái nhân cách tự phản tỉnh (The Introspective Psychopath)*"),

    # ---- 7) 4.05: trich danh 'Co le ho...' nam o #16 (shot 4-10) --------
    ("| 4-09 | `4.05#12`–`#15` | D | T4 lời kể | `t3_interview_room` | “Hy vọng mình có thể tìm được cách giúp đỡ người khác… Có lẽ họ có thể nghiên cứu tôi.”",
     "| 4-09 | `4.05#12`–`#16` | D | T4 lời kể | `t3_interview_room` | → `#15`: “Sau đó, tôi hy vọng mình có thể tìm được cách để giúp đỡ người khác... Có lẽ họ có thể nghiên cứu tôi và tìm ra điều gì khiến những người như tôi làm những điều chúng tôi làm.”"),
    ("| 4-10 | `4.05#16`–`#19` | D | T2 | `t3_fbi_corridor` | *DỰ ÁN NGHIÊN CỨU TÍNH CÁCH TỘI PHẠM* · **36 TÙ NHÂN GIẾT NGƯỜI TÌNH DỤC** · *Mạng lưới VICAP 1985*",
     "| 4-10 | `4.05#17`–`#19` | D | T2 | `t3_fbi_corridor` | *DỰ ÁN NGHIÊN CỨU TÍNH CÁCH TỘI PHẠM* · **36 TÙ NHÂN GIẾT NGƯỜI TÌNH DỤC** · *Mạng lưới VICAP 1985*"),

    # ---- 8) 1.05: trich danh 'chon ho' -> script da doi thanh 'mang vun' --
    ("| 1-09 | `1.05#5`–`#7` | H | T4 lời kể | `t3_case_file` | “Và tôi đã giết mấy cô nữ sinh đó. Sáu người. Tôi có thể chỉ cho các anh biết tôi đã chôn họ ở đâu.”",
     "| 1-09 | `1.05#5`–`#7` | H | T4 lời kể | `t3_case_file` | “Và tôi đã giết mấy cô nữ sinh đó. Sáu người. Tôi có thể chỉ cho các anh biết tôi đã chôn những mảnh vụn của họ ở đâu.”"),

    # ---- 9) 1.09: trich danh phai nguyen van, tach theo tung cau ---------
    ("| 1-13 | `1.09#1`–`#3` | N1 | T4 lời kể | `t3_dispatch_desk` mờ | “Ban đầu tôi cứ tưởng Ed uống say rồi gọi điện trêu đùa…” → `#3`: “Bảo chúng tôi cử người tới nhà kiểm tra.”",
     "| 1-13 | `1.09#1`–`#4` | N1 | T4 lời kể | `t3_dispatch_desk` mờ | “Ban đầu, tôi cứ tưởng Ed uống say rồi gọi điện trêu đùa.” → `#4`: “bảo chúng tôi cử người tới nhà kiểm tra.”"),
    ("| 1-14 | `1.09#4`–`#6` | N1 | T4 lời kể | `t3_phone_booth` | “Xe tuần tra cảnh sát Pueblo dừng bên bốt điện thoại… Tìm thấy hắn ngồi đó bình thản như chờ mua cà phê.”",
     "| 1-14 | `1.09#5`–`#6` | N1 | T4 lời kể | `t3_phone_booth` | → `#5`: “Vài giờ sau, xe tuần tra của cảnh sát Pueblo dừng bên bốt điện thoại.” → `#6`: “Chúng tôi tìm thấy hắn ngồi đó, bình thản như người đang chờ xếp hàng mua cà phê.”"),
    ("| 1-15 | `1.09#7`–`#9` | N1 | T4 lời kể | `t3_bar_stool_shadow` | “Chúng tôi đưa hắn về Santa Cruz… Kẻ cả bang đang truy lùng lại từng ngồi cạnh chúng tôi mỗi tối.”",
     "| 1-15 | `1.09#7`–`#9` | N1 | T4 lời kể | `t3_bar_stool_shadow` | “Chúng tôi đưa hắn về Santa Cruz.” → `#9`: “Kẻ mà cả bang California đang ráo riết truy lùng bấy lâu nay... lại từng ngồi ngay cạnh chúng tôi mỗi tối.”"),

    # ---- 10) 2.09: trich danh 'Big Ed...' o #2 (shot 2-20), khac sang 2-21
    ("| 2-20 | `2.09#1`–`#3` | N2 | T1 | `t3_bar_jury_room` | **QUÁN RƯỢU THE JURY ROOM** · *Đối diện Tòa án Quận Santa Cruz*",
     "| 2-20 | `2.09#1`–`#3` | N2 | T1 | `t3_bar_jury_room` | **QUÁN RƯỢU THE JURY ROOM** · *Đối diện Tòa án Quận Santa Cruz* → `#2`: “Big Ed luôn ngồi ở góc quầy bar quen thuộc.”"),
    ("| 2-21 | `2.09#4`–`#6` | N2 | T4 lời kể | `t3_bar_stool_shadow` | “Big Ed luôn ngồi ở góc quầy bar quen thuộc… Từng muốn được làm cảnh sát nhưng không nơi nào nhận nổi.”",
     "| 2-21 | `2.09#4`–`#6` | N2 | T4 lời kể | `t3_bar_stool_shadow` | → `#4`: “Cậu ấy thậm chí muốn được làm cảnh sát.” → `#5`: “Nhưng với thân hình kia, không nơi nào nhận nổi.”"),
    ("| 2-22 | `2.09#7`–`#9` | N2 | T4 lời kể | `t3_bar_stool_shadow`, `push` | “Ed vừa uống bia vừa gợi ý những giả thuyết tâm lý… Kẻ chúng tôi săn tìm lại đang ngồi uống bia cùng chúng tôi.”",
     "| 2-22 | `2.09#7`–`#9` | N2 | T4 lời kể | `t3_bar_stool_shadow`, `push` | → `#7`: “Ed vừa uống bia vừa gật gù, phân tích và còn gợi ý cho chúng tôi những giả thuyết về tâm lý của kẻ sát nhân.” → `#8`: “Kẻ chúng tôi đang săn tìm... đang ngồi uống bia cùng chúng tôi và cười đùa về chính cuộc săn lùng đó.”"),

    # ---- 11) 5.08: dau cham nam NGOAI trich danh trong script ------------
    ("| 5-15 | `5.08#4`–`#5` | H | T4 lời kể | `t3_courtroom_1973` | “Với tôi, ông ấy là người cha mà tôi ước mình từng có.”",
     "| 5-15 | `5.08#4`–`#5` | H | T4 lời kể | `t3_courtroom_1973` | “Với tôi, ông ấy là người cha mà tôi ước mình từng có”"),
]

fail = 0
for old, new in FIXES:
    n = text.count(old)
    if n != 1:
        print(f"[FAIL x{n}] khong khop duy nhat:\n   {old[:150]}")
        fail += 1
        continue
    text = text.replace(old, new)
    print(f"[OK ] {new.split('|')[1].strip():6s} {old.split('|')[1].strip()}")

if fail:
    print(f"\n{fail} that bai - KHONG ghi file.")
    sys.exit(1)

PLAN.write_text(text, encoding="utf-8")
print(f"\nDa ghi {PLAN} ({len(text)} ky tu)")
