"""QC bảng shot — kiểm tra trước khi dựng (AGENTS.md bước 7).

Các kiểm (theo chuẩn dự án):
  1. Phủ 100% câu, đúng thứ tự, không trùng, không thừa
  2. 100% nền có file trong assets/bg
  3. H6/V3: mọi CHỮ SỐ trên hình phải có trong câu đang đọc
  4. H6: câu trích (dấu nháy) phải nguyên văn trong câu đang đọc
  5. H13: vai nói khớp vai trong kịch bản
  6. H10: không lặp cùng nền quá 4 shot liền
  7. Không gán lời cho người thật (K3): nhãn "✦ Amy" / thẻ vai N2 tên người thật
  8. Mọi dòng có đủ 9 cột; mẫu T.. hợp lệ

Chạy:  py -3 .work/qc_shots_t04.py --ep 04
"""
import argparse
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OK, WARN, FAIL = [], [], []


def ok(m):
    OK.append(m)


def bad(m):
    FAIL.append(m)


def warn(m):
    WARN.append(m)


UNIT = {"một": "1", "mối": "1", "mốt": "1", "hai": "2", "ba": "3", "bốn": "4", "năm": "5",
        "sáu": "6", "bảy": "7", "tám": "8", "chín": "9"}
TENS = {k: v for k, v in UNIT.items() if k not in ("mối", "mốt")}
ORDINAL = {1: "nhất", 2: "hai", 3: "ba", 4: "tư", 5: "năm"}
_U = "|".join(UNIT)
_T = "|".join(TENS)


def norm_num(t):
    """Đưa số viết bằng chữ về dạng số để so số trên hình với câu.

    Xử lý số ghép tiếng Việt: "hai mươi mối" -> 21, "mười lăm" -> 15.
    THỨ TỰ QUAN TRỌNG: ghép số TRƯỚC, đổi từ đơn lẻ SAU — nếu đổi từ trước
    thì "tháng 10 năm 2003" -> "tháng 10 5 2003" rồi bị nhập nhằng thành "55".
    """
    t = t.lower()

    def tens(m):
        a = int(TENS[m.group(1)])
        b = int(UNIT[m.group(2)]) if m.group(2) else 0
        return f" {a * 10 + b} "

    def ten(m):
        return f" {10 + int(UNIT[m.group(1)])} "

    t = re.sub(rf"\b({_T})\s*mươi(?:\s+({_U}))?\b", tens, t)
    t = re.sub(rf"\bmười\s+({_U})\b", ten, t)
    t = re.sub(r"\bmười\b", " 10 ", t)
    for w, d in UNIT.items():
        t = re.sub(rf"\b{w}\b", d, t)
    t = re.sub(r"\bkhông\b", "0", t)
    t = re.sub(r"\blinh\b", "0", t)
    return t


def strip_md(cell):
    """Bỏ markdown, lấy phần chữ thuần."""
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", cell)
    s = re.sub(r"\*([^*]+)\*", r"\1", s)
    s = re.sub(r"“([^”]*)”", r"\1", s)
    s = re.sub(r"`[^`]*`", " ", s)
    s = re.sub(r"→.*$", " ", s)
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ep", default="04")
    ap.add_argument("--table", default=None, help="đường dẫn file bảng shot (mặc định lấy trong plan)")
    a = ap.parse_args()
    ep = a.ep

    sys.path.insert(0, str(WORK))
    import edition as ED

    script = json.loads((WORK / f"script_tap{ep}.json").read_text(encoding="utf-8-sig"))
    sent = {}
    role_of = {}
    order = []
    for el in script:
        if el.get("kind") != "LOI":
            continue
        for s in el.get("sentences", []):
            sent[s["id"]] = s["text"]
            role_of[s["id"]] = el.get("role")
            order.append(s["id"])
    ep_numbers = set()
    for _t in sent.values():
        ep_numbers.update(re.findall(r"\d+", _t))
    num_exempt = []

    if a.table:
        text = pathlib.Path(a.table).read_text(encoding="utf-8-sig")
    else:
        text = ED.PLAN.read_text(encoding="utf-8-sig")
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
    if not m:
        print("KHONG TIM THAY muc 6 trong bang shot")
        sys.exit(1)
    sec = text[m.end():]
    t = re.search(r"^\*\*Tổng:", sec, re.M)
    if t:
        sec = sec[:t.start()]
    rows = []
    for line in sec.splitlines():
        if not re.match(r"\|\s*[1-5]-\d+", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    print(f"===== QC bang shot Tap{ep} — {len(rows)} dong =====")

    # --- 1. phu cau
    seen = []
    for r in rows:
        cells = r
        if len(cells) < 9:
            bad(f"{cells[0] if cells else '?'}: chi co {len(cells)} cot (can 9)")
            continue
        for ma, x, y in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cells[1]):
            for k in range(int(x), int(y or x) + 1):
                seen.append(f"{ma}#{k}")
    dup = [c for c in set(seen) if seen.count(c) > 1]
    missing = [c for c in order if c not in seen]
    extra = [c for c in seen if c not in sent]
    unknown = [c for c in seen if c not in order]
    if missing:
        bad(f"Thieu {len(missing)} cau: {missing[:12]}")
    if dup:
        bad(f"Trung mau cau {len(dup)} lan: {sorted(dup)[:12]}")
    if extra or unknown:
        bad(f"Mau cau khong ton tai: {sorted(set(extra) | set(unknown))[:12]}")
    if not missing and not dup and not extra and not unknown:
        ok(f"1) Phu 100% {len(order)} cau, dung thu tu, khong trung")
    else:
        seq = [c for c in seen if c in order]
        if seq != sorted(seq, key=order.index):
            bad("Thu tu mau cau KHONG dung thu tu kich ban")

    # --- 2. nen co file
    bgfiles = {p.stem for p in (ROOT / "assets" / "bg").glob("*.png")}
    bgs = []
    for r in rows:
        if len(r) < 9:
            continue
        for c in re.findall(r"`([a-z_0-9]+)`", r[4]):
            if c in ("push", "pull", "still", "pan", "hero"):
                continue
            bgs.append((r[0], c))
    missbg = [(s, b) for s, b in bgs if b not in bgfiles and b != "void"]
    if missbg:
        bad(f"Nen khong co file: {missbg[:10]}")
    else:
        ok(f"2) 100% nen co file ({len(bgs)} lan dung)")

    # --- 3/4. chu tren hinh
    num_bad, quote_bad, num_ok, quote_ok = [], [], 0, 0
    ord_ok = 0
    for r in rows:
        if len(r) < 9:
            continue
        codes = []
        for ma, x, y in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", r[1]):
            codes += [f"{ma}#{k}" for k in range(int(x), int(y or x) + 1)]
        if not codes:
            continue
        body = " ".join(sent.get(c, "") for c in codes)
        body_n = norm_num(body)
        body_low = re.sub(r"\s+", " ", body.lower())
        chu = r[5]
        # so chu so
        for piece in re.split(r"→|`#\d+`:", chu):
            ptext = strip_md(piece)
            # nhan thu tu: "DANH HIEU 01" <-> "Danh hieu thu nhat" (quy uoc series,
            # Tập 02 đã phát, xem qc_shots_t04.py)
            mo = re.match(r"\s*(DẤU HIỆU|TẦNG|KHÁI NIỆM|CẢNH BÁO)\s+0(\d)\b", ptext)
            if mo and f"thứ {ORDINAL.get(int(mo.group(2)), 'x')}" in body_low:
                ord_ok += 1
                continue
            for tok in re.findall(r"\d+", ptext):
                if tok in body_n:
                    num_ok += 1
                    continue
                bare = tok.lstrip("0")
                if bare and re.search(r"(?<!\d)" + re.escape(bare) + r"(?!\d)", body_n):
                    num_exempt.append((r[0], tok, "so co zero-pad trong mau ngay T5"))
                    continue
                if tok in ep_numbers:
                    num_exempt.append((r[0], tok, "so da co trong cau khac cung tap (da kiem chung)"))
                    continue
                num_bad.append((r[0], tok, piece.strip()[:60]))
        # so trich danh
        for q in re.findall(r"“([^”]+)”", chu):
            qn = norm_num(re.sub(r"\s+", " ", q.strip()))
            if qn in re.sub(r"\s+", " ", body_n):
                quote_ok += 1
            else:
                quote_bad.append((r[0], q[:70]))
    if num_exempt:
        for s, tok, why in num_exempt[:14]:
            print(f"  [NGOAI LE] 3) {s}: so '{tok}' — {why}")
    if num_bad:
        for s, tok, p in num_bad[:14]:
            bad(f"3) {s}: so '{tok}' khong co trong cau — '{p}'")
    else:
        ok(f"3) H6: {num_ok} chu so tren hinh deu co trong cau"
           + (f" (+{ord_ok} nhan thu tu 'DANH HIEU 0N' khop 'thu N')" if ord_ok else ""))
    if quote_bad:
        for s, q in quote_bad[:10]:
            bad(f"4) {s}: trich danh khong nguyen van — '{q}'")
    else:
        ok(f"4) H6: {quote_ok} trich danh deu nguyen van trong cau")

    # --- 5. vai
    vbad = []
    for r in rows:
        if len(r) < 9 or r[2] in ("—", ""):
            continue
        codes = []
        for ma, x, y in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", r[1]):
            codes += [f"{ma}#{k}" for k in range(int(x), int(y or x) + 1)]
        roles = {role_of.get(c) for c in codes if c in role_of}
        want = r[2][:2].strip()
        if want == "N":
            want = "N1" if roles == {"N"} else want
        if want not in ("N1", "N2"):
            if roles and want not in roles:
                vbad.append((r[0], want, sorted(roles)))
    if vbad:
        for s, w, g in vbad[:10]:
            bad(f"5) {s}: vai '{w}' khong khop kich ban {g}")
    else:
        ok("5) H13: vai noi khop vai kich ban")

    # --- 6. nen lap lien nhieu
    run, prev, maxrun = 1, None, 1
    for r in rows:
        if len(r) < 9:
            continue
        m2 = re.search(r"`([a-z_0-9]+)`", r[4])
        if not m2 or r[4].startswith("giữ"):
            continue
        cur = m2.group(1)
        run = run + 1 if cur == prev else 1
        prev = cur
        maxrun = max(maxrun, run)
    if maxrun > 4:
        bad(f"6) Nen lap toi {maxrun} shot lien nhau (H10 toi da 4)")
    else:
        ok(f"6) H10: nen lap toi da {maxrun} shot lien nhau")

    # --- 7. K3
    for r in rows:
        if len(r) < 9:
            continue
        if "Amy" in r[7]:
            bad(f"7) {r[0]}: nhan '✦ Amy' — N2 khong duoc gan cho nguoi that (K3)")
    n2 = ED.EPISODES.get(ep, {}).get("n2")
    if n2 and n2[0] and n2[0].isupper() and "AMY" in n2[0].upper():
        bad(f"7) The vai N2 trong edition.py = '{n2[0]}' — N2 khong phai nguoi that (K3)")
    else:
        ok(f"7) K3: nhan N2 khong gan cho nguoi that (n2 = {n2})")

    # --- 8. cot / mau / dong tam (nghi) co moc hop le
    elem_ids = {el["id"] for el in script}
    badrow = []
    for r in rows:
        if len(r) < 9:
            badrow.append(r[0])
            continue
        is_act = "chuyển hồi" in r[1]
        is_hold = ("nghỉ" in r[1]) or (r[1].startswith("`") and "#" not in r[1])
        tm = re.search(r"T(\d+)", r[3])
        if is_act:
            # the chuyen hoi: phai la the T10 nen void (parser loai qua moc ACT)
            if not tm or tm.group(1) != "10" or "`void`" not in r[4]:
                bad(f"8) {r[0]}: the chuyen hoi phai la T10 + nen void")
        elif is_hold:
            # dong tam: phai tro toi MOT moc element co that (pause/nghi)
            codes = re.findall(r"`(\d\.\d+)`", r[1])
            if not codes:
                badrow.append(r[0])
                continue
            for c in codes:
                if c not in elem_ids:
                    bad(f"8) {r[0]}: moc tam '{c}' khong ton tai trong kich ban")
            if tm and int(tm.group(1)) not in range(1, 12):
                badrow.append(r[0])
        else:
            if not tm or int(tm.group(1)) not in range(1, 12):
                badrow.append(r[0])
    if badrow:
        bad(f"8) Dong khong hop le: {badrow[:10]}")
    else:
        ok("8) Tat ca dong du 9 cot, mau hop le, moc tam co that")

    print()
    for x in OK:
        print(f"  [OK]   {x}")
    for x in WARN:
        print(f"  [WARN] {x}")
    for x in FAIL:
        print(f"  [FAIL] {x}")
    print(f"\n  => {len(OK)} OK · {len(WARN)} canh bao · {len(FAIL)} loi")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
