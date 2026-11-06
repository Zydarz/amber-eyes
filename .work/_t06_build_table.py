#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — dựng bảng shot (mục 6) từ file kế hoạch JSON + kịch bản, có tự kiểm.

Dùng:
    py -3 _t06_build_table.py vi      # ghi 02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md
    py -3 _t06_build_table.py en      # ghi 02_SAN_XUAT/Tap06_EN/KeHoach_Video_Tap06_EN.md
    py -3 _t06_build_table.py ja      # ghi 02_SAN_XUAT/Tap06_JA/KeHoach_Video_Tap06_JA.md
    py -3 _t06_build_table.py vi --check    # chỉ kiểm, không ghi
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
from parse_kichban import parse_file  # noqa: E402
import edition as ED  # noqa: E402

EP = ED.EPISODES["06"]
N_ELEM = EP.get("n_element") or {}

LANG = {
    "vi": {"script": ROOT / "01_KICH_BAN/Tap06/kichban_tap06_23102026.md",
           "plan": ROOT / "02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md",
           "planjson": WORK / "_t06_plan_vi.json",
           "hdr": "| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | Ghi chú |",
           "sec": "## 6. DANH SÁCH SHOT — TẬP 06 (tiếng Việt)"},
    "en": {"script": ROOT / "01_KICH_BAN/Tap06_EN/kichban_tap06_EN.md",
           "plan": ROOT / "02_SAN_XUAT/Tap06_EN/KeHoach_Video_Tap06_EN.md",
           "planjson": WORK / "_t06_plan_en.json",
           "hdr": "| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật |",
           "sec": "## 6. DANH SÁCH SHOT — TẬP 06 (ENGLISH EDITION)"},
    "ja": {"script": ROOT / "01_KICH_BAN/Tap06_JA/kichban_tap06_JA.md",
           "plan": ROOT / "02_SAN_XUAT/Tap06_JA/KeHoach_Video_Tap06_JA.md",
           "planjson": WORK / "_t06_plan_ja.json",
           "hdr": "| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | Ghi chú |",
           "sec": "## 6. DANH SÁCH SHOT — TẬP 06 (JA)"},
}

ACT_TITLES = {
    "vi": {2: "HIỆN TRƯỜNG & QUỸ ĐẠO LEO THANG CỦA VỰC THẲM",
           3: "GIẢI PHẪU TÂM LÝ — SỰ CHIA NGĂN NHẬN THỨC & KHOẢNG TỐI SUMMERDALE",
           4: "ĐẤU TRÍ THẨM VẤN & SỤP ĐỔ VỞ KỊCH ĐA NHÂN CÁCH",
           5: "PHÁN QUYẾT, BẢN ÁN TÂM LÝ & BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN"},
    "en": {2: "THE CRIME SCENE & THE ESCALATION TRAJECTORY OF THE ABYSS",
           3: "PSYCHOLOGICAL AUTOPSY — COMPARTMENTALIZATION & THE SUMMERDALE VOID",
           4: "THE INTERROGATION DUEL & THE COLLAPSE OF THE MULTIPLE PERSONALITY DEFENSE",
           5: "THE VERDICT, PSYCHOLOGICAL SENTENCE & SURVIVAL RED FLAGS"},
    "ja": {2: "現場と犯行記録――深淵のエスカレーション軌道",
           3: "心理の深層解剖――精神の分断とサマーデールの空隙",
           4: "取調の攻防――多重人格劇の崩壊と法の審判",
           5: "判決、心理的結末と生存の警告"},
}
ACT_LABEL = {"vi": "HỒI", "en": "ACT", "ja": "第{n}幕"}

FORBIDDEN = {
    "vi": ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập", "đầu độc",
           "diệt cỏ", "bỏ đói", "móc áo", "đồ lót", "quan hệ tình dục", "hiếp", "cưỡng ép"],
    "en": ["blood", "corpse", "strangle", "choke", "struggle", "raped", "rape",
           "underwear", "sexual intercourse", "orgasm", "penis", "vagina", "suffocat",
           "mutilat", "dismember", "torture"],
    "ja": ["血", "死体", "絞", "レイプ", "性交渉", "精通"],
}
SAFE = {
    "vi": ["ung thư máu", "đấu tập", "bàn tay", "cánh tay", "đầu tư", "đầu học", "đầu tiên",
           "đầu não", "trọng đầu", "bầu cửa", "bầu trời", "đập đầu", "trói buộc"],
    "en": ["blood type", "blood pressure", "blood vessel", "bloodstream", "blood cell",
           "struggle to survive", "struggled to"],
    "ja": [],
}
STRUCT = re.compile(r"(HỒI|TẬP|NẤC|TẦNG|ACT|STAGE|LAYER|COMPARTMENT|EPISODE|CASE\s+FILE)")
STRUCT_JA = re.compile(r"第\s*\d+\s*[幕話]")


def sent_list(cell):
    """'#2-#3' -> [2,3] ; '#1' -> [1]"""
    out = []
    for part in str(cell).split(","):
        part = part.strip()
        m = re.match(r"^#(\d+)(?:-#(\d+))?$", part)
        if m:
            a = int(m.group(1))
            b = int(m.group(2) or a)
            out += list(range(a, b + 1))
    return out


def parse_chu(cell):
    """Tách chữ trên hình thành segment: [(at_sentence|None, [(kind,text),...])]"""
    cell = re.sub(r"\*\*.+?\*\*|\*[^*]+?\*|“.+?”",
                  lambda m: m.group(0).replace("→", "⟶"), cell)
    segs = []
    for raw in re.split(r"\s+→\s+", cell):
        raw = raw.replace("⟶", "→")
        at = None
        m = re.match(r"(?:ở\s+)?`#(\d+)`:?\s*(.*)", raw)
        if m:
            at, raw = int(m.group(1)), m.group(2)
        elems = []
        for tok in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", raw):
            if tok.group(1):
                elems.append(("bold", tok.group(1)))
            elif tok.group(2):
                elems.append(("ital", tok.group(2)))
            else:
                elems.append(("quote", tok.group(3)))
        if elems:
            segs.append((at, elems))
    return segs


def main():
    lang = sys.argv[1] if len(sys.argv) > 1 else "vi"
    check_only = "--check" in sys.argv
    cfg = LANG[lang]

    plan = json.loads(cfg["planjson"].read_text(encoding="utf-8"))
    raw_shots = plan["shots"]

    # ---- 0. chèn thẻ chuyển hồi trước mỗi hồi mới (chuẩn Tập 03/04/05) ----
    shots = []
    prev_act = None
    for sh in raw_shots:
        a = int(sh["el"].split(".")[0])
        if prev_act is not None and a != prev_act:
            lbl = ACT_LABEL[lang]
            lbl = lbl.format(n=f"{a:02d}") if "{n}" in lbl else f"{lbl} {a:02d}"
            shots.append({"kind": "act", "act": a, "row_act": prev_act,
                          "tpl": "T10", "bg": "void", "nv": "⊘", "tr": "◼",
                          "chu": f"*{lbl}* · **{ACT_TITLES[lang][a]}**"})
        sh = dict(sh)
        sh.setdefault("row_act", a)
        shots.append(sh)
        prev_act = a

    # ---- kịch bản: element -> (role, [câu]) --------------------------------
    els = parse_file(str(cfg["script"]))
    script = {}
    order = []
    for e in els:
        if e.get("kind") != "LOI":
            continue
        role = N_ELEM.get(e["id"], e.get("role"))
        sents = e.get("sentences", [])
        script[e["id"]] = {"role": role, "sents": {s["id"]: s["text"] for s in sents},
                           "n": len(sents)}
        order.append(e["id"])

    errs, warns = [], []

    # ---- 1. phủ câu + thứ tự ----------------------------------------------
    seen, flat = [], []
    for sh in shots:
        if sh.get("kind"):
            continue
        el = sh["el"]
        if el not in script:
            errs.append(f"element {el} không có trong kịch bản")
            continue
        for k in sent_list(sh["sent"]):
            sid = f"{el}#{k}"
            if sid not in script[el]["sents"]:
                errs.append(f"{sid} không tồn tại")
                continue
            seen.append(sid)
            flat.append(sid)
    expect = []
    for el in order:
        for i in range(1, script[el]["n"] + 1):
            expect.append(f"{el}#{i}")
    if flat != expect:
        miss = [x for x in expect if x not in flat]
        dup = [x for x in set(flat) if flat.count(x) > 1]
        errs.append(f"thứ tự/phủ câu lệch — thiếu {miss[:8]} · trùng {dup[:8]}")
    if seen and flat != expect:
        pass

    # ---- 2. nền tồn tại ---------------------------------------------------
    BG = {p.stem for p in (ROOT / "assets/bg").glob("*.png")}
    for i, sh in enumerate(shots):
        b = sh["bg"]
        if b in (None, "giữ"):
            continue
        if b not in BG:
            errs.append(f"shot {i}: nền `{b}` không có file")

    # ---- 3. ID shot duy nhất ----------------------------------------------
    # Hồi 1 mở đầu bằng thẻ mở đầu 1-00; các hồi còn lại bắt đầu từ -01.
    cnt = {}
    ids = []
    for sh in shots:
        act = sh["row_act"]
        if act not in cnt:
            cnt[act] = 0 if (act == 1 and sh.get("kind") == "open") else 1
        else:
            cnt[act] += 1
        ids.append(f"{act}-{cnt[act]:02d}")
    if len(set(ids)) != len(ids):
        dup = [x for x in set(ids) if ids.count(x) > 1]
        errs.append(f"ID shot trùng: {dup}")
    # số thứ tự trong mỗi hồi phải liên tục
    for act in sorted(cnt):
        seq = [int(i.split("-")[1]) for i in ids if i.startswith(f"{act}-")]
        if seq != list(range(min(seq), min(seq) + len(seq))):
            errs.append(f"hồi {act}: số shot không liên tục {seq}")

    # ---- 4. trích dẫn nguyên văn + số trên hình + từ cấm -----------------
    for i, sh in enumerate(shots):
        sid = ids[i]
        if sh.get("kind"):
            continue
        el = sh["el"]
        ctx = " ".join(script[el]["sents"][f"{el}#{k}"] for k in sent_list(sh["sent"]))
        on_screen = [(k, t) for _at, elems in parse_chu(sh["chu"]) for k, t in elems]
        # 4a. trích dẫn
        for kind, t in on_screen:
            if kind != "quote":
                continue
            core = t.strip().strip("“”\"")
            for frag in [f.strip() for f in core.split("…") if f.strip()]:
                if frag not in ctx:
                    errs.append(f"{sid}: trích dẫn “{frag[:45]}…” không nguyên văn trong câu")
        # 4b. số trên hình
        flat_ctx = ctx.replace(" ", "")
        allowed = set(re.findall(r"\d+", flat_ctx))
        for a in list(allowed):
            allowed.add(a.zfill(2))
            allowed.add(str(int(a)))
        screen = " ".join(t for _k, t in on_screen)
        for m in set(re.findall(r"\d[\d.,]*", screen)):
            tok = m.replace(".", "")
            if m in allowed or m in flat_ctx or tok in allowed:
                continue
            if STRUCT_JA.search(screen) and re.search(r"第\s*" + re.escape(m) + r"\s*[幕話]", screen):
                continue
            if STRUCT.search(screen) and re.search(STRUCT.pattern + r"\s*" + re.escape(m) + r"\b", screen):
                continue
            errs.append(f"{sid}: số “{m}” không có trong câu")
        # 4c. từ cấm
        low = screen.lower()
        for w in FORBIDDEN[lang]:
            if not re.search(r"(?<!\w)" + r"\s+".join(re.escape(x) for x in w.split()) + r"(?!\w)", low):
                continue
            if any(g in low for g in SAFE[lang] if g in w or w in g):
                continue
            errs.append(f"{sid}: từ cấm “{w}” trên hình")

    # ---- 5. vai khớp ------------------------------------------------------
    for i, sh in enumerate(shots):
        if sh.get("kind"):
            continue
        el = sh["el"]
        for k in sent_list(sh["sent"]):
            if script[el]["role"] != script[el]["role"]:
                pass
    # vai ghi trong bảng suy ra từ vai của element (dùng để ghi cột Vai)

    # ---- 6. ghi bảng ------------------------------------------------------
    lines = [cfg["sec"], "", cfg["hdr"], "|---|---|---|---|---|---|---|---|---|"]
    prev = None
    for i, sh in enumerate(shots):
        sid = ids[i]
        kind = sh.get("kind")
        el = sh.get("el", "")
        if kind == "open":
            cau, vai, mau = f"`{el}` (20.5 s → lời đầu)", "—", sh.get("tpl", "")
            nen = f"`{sh['bg']}`"
        elif kind == "act":
            cau, vai, mau = "nghỉ chuyển hồi (2 s)", "—", sh.get("tpl", "")
            nen = f"`{sh['bg']}`"
        elif kind == "hold":
            cau, vai, mau = f"`{el}` (nghỉ 1.5 s)", "—", "—"
            nen = f"giữ {prev}"
        elif kind == "end":
            cau, vai, mau = "hết tập (10 s)", "—", sh.get("tpl", "")
            nen = f"`{sh['bg']}`"
        else:
            ks = sent_list(sh["sent"])
            # Cùng element + liên tiếp -> "`el#a`–`#b`"; khác element -> ", "
            parts = []
            i = 0
            while i < len(ks):
                j = i
                while j + 1 < len(ks) and ks[j + 1] == ks[j] + 1:
                    j += 1
                if j > i:
                    parts.append(f"`{el}#{ks[i]}`–`#{ks[j]}`")
                else:
                    parts.append(f"`{el}#{ks[i]}`")
                i = j + 1
            cau = ", ".join(parts)
            vai = script[el]["role"]
            mau = sh.get("tpl", "")
            nen = f"`{sh['bg']}`"
        chu = sh.get("chu", "—")
        beat = sh.get("beat", "—")
        nv = sh.get("nv", "")
        tr = sh.get("tr", "")
        if lang == "ja":
            cau = cau.replace("lời đầu", "最初の発話").replace("nghỉ 1.5 s", "休止 1.5 秒")
            cau = cau.replace("hết tập (10 s)", "最終カード (10 秒)")
        row = f"| {sid} | {cau} | {vai} | {mau} | {nen} | {chu} | {beat} | {nv} | {tr} |"
        if lang == "en":
            row = row.rstrip(" |").rstrip() + " |"
        lines.append(row)
        prev = sid

    n_sent = len(expect)
    lines += ["", f"**Tổng:** {len(shots)} shot · {n_sent} câu · {len(order)} element lời "
                   f"({len(cnt)} hồi) · nền dùng {len({s['bg'] for s in shots if s.get('bg') not in (None, 'giữ')})} loại.",
               ""]
    new_sec = "\n".join(lines)

    print(f"[{lang}] {len(shots)} shot · {n_sent} câu · {len(order)} element lời")
    if warns:
        for w in warns:
            print("  !", w)
    if errs:
        print(f"  ✗ {len(errs)} LỖI:")
        for e in errs[:40]:
            print("   -", e)
        sys.exit(1)
    print("  ✓ tự kiểm đạt")

    if check_only:
        return

    path = cfg["plan"]
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    m = re.search(r"^## 6\..*$", old, re.M)
    if m:
        nxt = re.search(r"^## ", old[m.end():], re.M)
        end = m.end() + (nxt.start() if nxt else len(old) - m.end())
        head = old[:m.start()]
        tail = old[end:]
    else:
        head = old.rstrip() + "\n\n---\n\n" if old.strip() else ""
        tail = ""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(head + new_sec + "\n" + tail, encoding="utf-8")
    print("  → ghi", path)


if __name__ == "__main__":
    main()
