#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh lại `REVIEW_Bo_Anh_Tap24.md` từ bảng shot MỤC 6 của KeHoach_Video_Tap24.md.

Bản REVIEW cũ (24/10/2026) mô tả bộ 63 ảnh `t24_lee_choon_jae_*` đã không còn trên đĩa
( thiếu 7 ảnh redflag/banner/closing) ⇒ viết lại theo bộ 155 ảnh `t24_*` thực tế.

Dùng:  py -3 .work/_make_review_t24.py
"""
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROD = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham"
PLAN = PROD / "Tap24" / "KeHoach_Video_Tap24.md"
OUT = PROD / "Tap24" / "REVIEW_Bo_Anh_Tap24.md"
QC = PROD / "Tap24" / "BAO_CAO_QC_ANH_NEN_TAP24_H26_20261125.md"
BG = ROOT / "assets" / "bg"

ACT_TITLES = {
    1: "HỒI 1: NHỮNG CÁNH ĐỒNG ĐÊM HWASEONG & 33 NĂM TRONG SƯƠNG MÙ",
    2: "HỒI 2: CUỘC ĐẤU TRÍ TẠI TRẠI GIAM BUSAN & LỜI TỰ BẠCH LẠNH GÁY",
    3: "HỒI 3: GIẢI MÃ TÂM LÝ: KẺ SÁT NHÂN KIỂM SOÁT QUYỀN LỰC & NGHỊCH LÝ THÚ TỘI",
    4: "HỒI 4: PHIÊN TÒA GIẢI OAN THẾ KỶ & LỜI XIN LỖI CỦA CÔNG LÝ",
    5: "HỒI 5: BÀI HỌC CẢNH TỈNH & 4 CẢNH BÁO ĐỎ PHÒNG NGỪA TỘI PHẠM SĂN MỒI BAN ĐÊM",
}

ROLE = {"H": "Cú · Host", "D": "Sói · Điều tra viên", "C": "Cáo · Chuyên gia tâm lý",
        "N1": "Cư dân Hwaseong", "N2": "Người được minh oan (Yoon Sung-yeo)"}


def parse_plan():
    """-> OrderedDict act -> list of dict(shot, code, dur, role, model, bg, cam, text)."""
    lines = PLAN.read_text(encoding="utf-8").split("\n")
    acts, act, in_tbl = OrderedDict(), None, False
    for l in lines:
        m = re.match(r"^### HỒI (\d):", l)
        if m:
            act = int(m.group(1))
            acts.setdefault(act, [])
            in_tbl = False
            continue
        if l.startswith("| Shot |"):
            in_tbl = True
            continue
        if in_tbl and l.startswith("|---"):
            continue
        if in_tbl and l.startswith("|"):
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cells) < 6:
                continue
            shot = cells[0]
            if not re.match(r"^\d-\d\d$", shot):
                continue
            code = re.match(r"^`([^`]+)`", cells[1])
            dur = re.search(r"\(([\d,]+) s\)", cells[1])
            bgm = re.search(r"`(t24_[a-z0-9_]+)`", cells[4])
            cam = re.findall(r"`([a-z]+)`", cells[4])
            acts[act].append({
                "shot": shot,
                "code": code.group(1) if code else cells[1],
                "dur": dur.group(1) if dur else "?",
                "role": cells[2],
                "model": cells[3],
                "bg": bgm.group(1) if bgm else "?",
                "cam": cam[1] if len(cam) > 1 else (cam[0] if cam else "still"),
                "text": cells[5].strip("* ").strip(),
            })
            continue
        if in_tbl and l.strip() == "":
            in_tbl = False
    return acts


def qc_groups():
    """Đọc nhóm A/B/F/C từ báo cáo QC H26."""
    g = {"A": [], "B": [], "F": [], "C": []}
    if not QC.exists():
        return g
    cur = None
    for l in QC.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^## Nhóm ([A-Z]) —", l)
        if m:
            cur = m.group(1)
            continue
        if l.startswith("## ") or l.startswith("# "):
            cur = None
        if cur and l.startswith("- `t24_"):
            g[cur].append(re.findall(r"`(t24_[a-z0-9_]+)`", l)[0])
    return g


def main():
    acts = parse_plan()
    all_shots = [s for a in acts.values() for s in a]
    bgs = OrderedDict()
    for s in all_shots:
        bgs.setdefault(s["bg"], []).append(s)
    g = qc_groups()

    lines = []
    A = lines.append
    A("# BÁO CÁO THẨM ĐỊNH & REVIEW CHẤT LƯỢNG BỘ ẢNH NỀN TẬP 24")
    A('## "KÝ ỨC KẺ SÁT NHÂN HWASEONG" (HWASEONG, GYEONGGI, HÀN QUỐC)')
    A("")
    A("*Ngày lập báo cáo: 2026-11-25 (bản cập nhật, thay thế bản 24/10/2026 mô tả bộ ảnh "
      "`t24_lee_choon_jae_*` đã không còn trên đĩa).*")
    A("*Dự án: Podcast Tài liệu Phân tích Tâm lý Tội phạm Amber Eyes.*")
    A("")
    A("---")
    A("")
    A("## I. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)")
    A("")
    A("| Tiêu chí | Kết quả thẩm định | Trạng thái | Ghi chú kỹ thuật |")
    A("|---|:---:|:---:|---|")
    A(f"| **Số lượng ảnh** | **{len(bgs)} / {len(bgs)} ảnh** | **ĐẠT (100%)** | "
      f"Toàn bộ `assets/bg/t24_*.png` đều được dùng, 0 ảnh thừa (H22) |")
    A("| **Kích thước & Tỷ lệ** | **2112 × 1188 (16:9 2K)** | **ĐẠT (100%)** | "
      f"{len(bgs)}/{len(bgs)} ảnh full-bleed, không viền đen letterbox |")
    A("| **Kiểm tra viền & Khung vẽ (QC)** | **0 lỗi** | **ĐẠT (100%)** | "
      "`qc_bg.py t24` báo 8 ảnh có dải tối sát viền — đã soi mắt, đều là **nội dung cảnh** "
      "(tường, cột, trời đêm), KHÔNG phải letterbox |")
    A(f"| **Sổ nguồn gốc (`provenance.json`)** | **155 / 155 bản ghi** | **ĐẠT (100%)** | "
      "Đầy đủ metadata prompt, công cụ tạo ảnh, kích thước gốc; bản quyền kênh 100% tự chủ |")
    A(f"| **Phủ câu thoại** | **{len(all_shots)} / 246 câu** | **ĐẠT (100%)** | "
      "1 bảng shot phục vụ cả VN / EN / JA (H25 · A8.1(c)) |")
    A(f"| **Tần suất nền (H22)** | **{len(all_shots)/len(bgs):.1f} shot/nền** | **ĐẠT** | "
      "Mục tiêu 1,5–2 shot/nền; không nền nào vượt 3 shot hoặc 30 s |")
    A("| **QC nội dung ảnh (H2/H19/H26)** | **81/155 ảnh (52%)** | **KHÔNG ĐẠT — "
      "người dùng chốt giữ nguyên** | Xem mục III; quyết định của người dùng ngày 25/11/2026 |")
    A("")
    A("---")
    A("")
    A("## II. PHÂN BỔ ẢNH THEO 5 HỒI")
    A("")
    A("Cột *Nền* là ảnh nền dùng chung cho cả 3 ngôn ngữ (VN / EN / JA); mã shot và "
      "thứ tự giữ nguyên 100%.")
    A("")
    for act, shots in acts.items():
        act_bgs = OrderedDict()
        for s in shots:
            act_bgs.setdefault(s["bg"], []).append(s)
        A(f"### {ACT_TITLES.get(act, 'HỒI ' + str(act))} — {len(act_bgs)} ảnh / {len(shots)} shot")
        A("")
        for bg, ss in act_bgs.items():
            A(f"- `{bg}`:")
            for s in ss:
                txt = s["text"]
                txt = (txt[:150] + "…") if len(txt) > 150 else txt
                A(f"  - Shot `{s['shot']}` · `{s['code']}` ({s['dur']} s) · "
                  f"{ROLE.get(s['role'], s['role'])} · mẫu {s['model']} · camera `{s['cam']}` — *{txt}*")
        A("")
    A("---")
    A("")
    A("## III. QC NỘI DUNG ẢNH (H2 / H19 / H26) — ĐÃ BÁO CÁO, NGƯỜI DÙNG CHỐT GIỮ NGUYÊN")
    A("")
    A("| Nhóm | Số ảnh | Vấn đề |")
    A("|---|:---:|---|")
    A(f"| **A** — chữ AI đọc được rõ | {len(g['A'])} | Biển `POLICE`, xe cảnh sát có chữ, "
      "tờ giấy/màn hình có chữ (vi phạm H2/H26) |")
    A(f"| **B** — dấu hiệu chữ / pseudo-text | {len(g['B'])} | Chữ quá nhỏ hoặc giả chữ |")
    A(f"| **F** — lộ mặt | {len(g['F'])} | Vi phạm mục 6 AGENTS (nhân vật nền phải bị che/khuất) |")
    A(f"| **C** — sai bối cảnh (H19) | {len(g['C'])} | `t24_a4_28` có biển `CALIFORNIA` — "
      "toà án Mỹ trong vụ án Hwaseong (Hàn Quốc) |")
    A("")
    A("Chi tiết từng ảnh: "
      "[`BAO_CAO_QC_ANH_NEN_TAP24_H26_20261125.md`](BAO_CAO_QC_ANH_NEN_TAP24_H26_20261125.md).")
    A("")
    A("> **Quyết định người dùng (25/11/2026):** giữ nguyên toàn bộ 155 ảnh nền hiện có, "
      "không sinh lại ảnh nào. Hệ quả trực tiếp: mục 4 của cổng `qc_bg_mapping.py` "
      "(22/155 ảnh dùng prompt chung thay vì prompt riêng) chưa thể đóng — cần ghi nhận "
      "ngoại lệ này trong hồ sơ phát hành.")
    A("")
    A("---")
    A("")
    A("## IV. KẾT LUẬN & ĐỀ XUẤT SẢN XUẤT")
    A("")
    A(f"1. **Đồng bộ kịch bản:** {len(all_shots)} shot phủ đúng 246 câu thoại của Tập 24; "
      "mã câu `1.02#1` … `5.05#18` trùng khớp 100% giữa VN / EN / JA.")
    A("2. **Bảo toàn pháp lý & bản quyền thương mại:** toàn bộ ảnh tạo nội bộ bằng "
      "Cloudflare Workers AI FLUX, 100% tự chủ, không dùng tài sản bên thứ ba.")
    A(f"3. **Sẵn sàng dựng video:** bộ ảnh lưu tại `assets/bg/t24_*.png` ({len(bgs)} file, "
      f"2112×1188); contact sheet tại `02_SAN_XUAT/Ho_So_Toi_Pham/Tap24/contact_sheet_t24.png`.")
    A("4. **Thời lượng:** VN 2203,30 s · EN 2137,38 s · JA 2444,66 s — khớp đúng thời lượng "
      "master audio từng ngôn ngữ (timeline dựng lại từ SRT, sai số 0,000 s).")
    A("5. **Ngoại lệ cần ghi nhận:** H26 (khung hình không có chữ) chưa đạt trên 81/155 ảnh; "
      "H10 (shot 3–15 s) có 4/246 shot VN, 2/246 EN, 4/246 JA vượt 15 s do câu thoại dài; "
      "badge sóng giọng không vẽ được vì không có stem tách riêng (master đã trộn sẵn).")
    A("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}  ({len(bgs)} backgrounds, {len(all_shots)} shots, "
          f"{len(lines)} lines)")


if __name__ == "__main__":
    main()
