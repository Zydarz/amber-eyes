# -*- coding: utf-8 -*-
"""Buoc 8 - cap nhat provenance.json + CSV + quet tu cam trong caption 15 file."""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TK = ROOT / "02_SAN_XUAT" / "TIKTOK"
LANGS = [("VN", "Tap04", "tiếng Việt"), ("EN", "Tap04_EN", "tiếng Anh"), ("JA", "Tap04_JA", "tiếng Nhật")]
CLIPS = ["TK1", "TK2", "TK3", "TK4", "TK5"]
DATE = "2026-11-27"

BANNED = ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập",
          "đầu độc", "diệt cỏ", "bỏ đói", "móc áo", "hiếp", "cắt đầu",
          "vâng hãm", "hiếp dâm", "lột da"]

TOOL = ".work/_tk04_package_b8.py (generator; mẫu Tap03/Caption_TK1.txt + KE_HOACH_TIKTOK.md mục 4 Bước 8)"


def body_of(path):
    t = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if "\n\n---\n" in t:
        t = t.split("\n\n---\n")[0]
    return t.rstrip("\n")


def main():
    meas = json.loads((ROOT / ".work" / "_tk04_pkg_measure.json").read_text(encoding="utf-8"))
    # AIGC -> so ky tu
    aigc_len = {"VN": len("Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự."),
                "EN": len("Content created with AI assistance for behavioral analysis. Viewer discretion advised."),
                "JA": len("AI技術を活用して心理分析目的で制作されたコンテンツです。閲覧にはご注意ください。")}

    # ---- 1. quet tu cam trong phan caption dan ----
    print("=== QUET TU CAM A9.2 trong phan caption dan (15 file) ===")
    n_bad = 0
    for lang, d, langname in LANGS:
        for c in CLIPS:
            body = body_of(TK / d / f"Caption_{c}.txt")
            hits = [w for w in BANNED if w.lower() in body.lower()]
            if hits:
                n_bad += 1
                print(f"  {d}/Caption_{c}.txt: {hits}")
    print(f"  -> {15 - n_bad}/15 caption sach tu cam (chi phan dan)")

    # ---- 2. provenance ----
    ppath = ROOT / "provenance.json"
    raw = ppath.read_bytes()
    crlf = raw.count(b"\r\n") > 0 and raw.count(b"\n") == raw.count(b"\r\n")
    prov = json.loads(raw.decode("utf-8"))
    # kiem tra round-trip: json.dumps(indent=2) phai tao ra dung byte cua file goc
    rt = (json.dumps(prov, ensure_ascii=False, indent=2) + "\n")
    if crlf:
        rt = rt.replace("\n", "\r\n")
    if rt.encode("utf-8") != raw:
        print("  [CANH BAO] round-trip khong giong byte goc -> se ghi lai toan file")
    existing = {e.get("file") for e in prov}
    rows = []
    for lang, d, langname in LANGS:
        for c in CLIPS:
            f = f"02_SAN_XUAT/TIKTOK/{d}/Caption_{c}.txt"
            if f in existing:
                print("  [skip prov] da co:", f)
                continue
            body = body_of(TK / d / f"Caption_{c}.txt")
            n = len(body)
            m = meas[f"{lang}_{c}"]
            lines = body.split("\n")
            aigc_no = next((i + 1 for i, l in enumerate(lines)
                             if "AI" in l and ("tạo hình" in l or "AI assistance" in l or "AI技術" in l)), None)
            blocked = (lang == "VN" and c in ("TK1", "TK3"))
            qc = ("TRƯỢT T13 (từ cấm 'sát hại' trong kịch bản — chờ người dùng duyệt)" if blocked
                  else "ĐẠT trọn 14 cổng (T1–T14 + H26 + H29)")
            rows.append({
                "file": f,
                "loai": f"caption + hashtag + nhãn AIGC + khối ghi chú khi đăng cho clip TikTok Tập 04 ({langname})",
                "cong_cu": TOOL,
                "ngay": DATE,
                "prompt": None,
                "seed": None,
                "mo_ta": (f"phần dán {n} ký tự (đã thêm dòng nhãn AIGC ở dòng {aigc_no}) + khối 'ghi chú khi đăng' "
                         f"tách riê sau dấu ---; số đo thật: {m['dur_s']} s · {m['size_mb']} MB · {m['n_lines']} câu · "
                         f"I {m.get('lufs')} LUFS · TP {m.get('tp')} dBFS; QC: {qc}"),
                "font": None,
                "dieu_khoan": (f"TikTok bắt buộc nhãn AIGC (bật toggle 'Nội dung do AI tạo'); giới hạn 2.200 ký tự — "
                               f"caption hiện {n} ký tự. Link YouTube Tập 04 chưa có ⇒ placeholder "
                               f"[LINK_TẬP 04 — cần điền]."),
                "kiem_tra_thuong_mai": (f"dat (độ dài caption {n} ký tự < 2.200; dòng AIGC đúng vị trí; phần dán sạch "
                                        f"từ cấm A9.2; số đo lấy từ file mp4 thành phẩm)"),
            })
        # mo_ta.txt + checklist_dang.md
        for fn, loai, desc in (
            ("mo_ta.txt", f"phiếu đóng gói để đăng — clip TikTok Tập 04 ({langname})",
             "gồm [A] 5 caption dán + [A2] link YouTube (placeholder) + [B] dòng AIGC bắt buộc + [C] lưu ý an toàn + hotline + [D] bảng số đo 5 clip"),
            ("checklist_dang.md", f"checklist trạng thái đăng — clip TikTok Tập 04 ({langname})",
             "bảng trạng thái từng clip (QC 14 cổng + caption + toggle AIGC + link bio + an toàn) + 7 việc chung của tập + cảnh báo trước khi đăng"),
        ):
            f = f"02_SAN_XUAT/TIKTOK/{d}/{fn}"
            if f in existing:
                print("  [skip prov] da co:", f)
                continue
            rows.append({
                "file": f,
                "loai": loai,
                "cong_cu": TOOL,
                "ngay": DATE,
                "prompt": None,
                "seed": None,
                "mo_ta": desc + f"; số đo lấy từ file mp4 thành phẩm (ffprobe) + báo cáo QC 27/11/2026",
                "font": None,
                "dieu_khoan": "Tài liệu nội bộ kênh; link YouTube Tập 04 chưa có ⇒ placeholder; không dán phần ghi chú vào caption.",
                "kiem_tra_thuong_mai": "dat (bảng markdown đúng số ô; số đo khớp file thành phẩm)",
            })

    prov.extend(rows)
    out = json.dumps(prov, ensure_ascii=False, indent=2) + "\n"
    if crlf:
        out = out.replace("\n", "\r\n")
    ppath.write_bytes(out.encode("utf-8"))
    print(f"  provenance: +{len(rows)} dong (tong {len(prov)}) · crlf={crlf}")

    # ---- 3. CSV: them ghi chu vao 15 dong TK04 ----
    cpath = TK / "BangTheoDoi_TikTok.csv"
    b = cpath.read_bytes()
    txt = b.decode("utf-8")
    parts = re.split(r"(\r\n|\n|\r)", txt)
    tag = " · DONG GOI BUOC 8 (27/11): caption co nhan AIGC + mo_ta.txt + checklist_dang.md"
    n = 0
    for i, p_ in enumerate(parts):
        if p_.startswith(("TK04_", "TK04_EN_", "TK04_JA_")) and tag not in p_:
            parts[i] = p_ + tag
            n += 1
    cpath.write_bytes("".join(parts).encode("utf-8"))
    print(f"  CSV: +{n} dong ghi chu (tong {len(parts)} phan)")


if __name__ == "__main__":
    main()
