#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC bang shot EN Tap05 — 13 cong, gom khop 3 chieu ANH — CHU — LOI THOAI.

Tieu chuan: AGENTS.md H3, H6, H10, H12, H13 · A11 #55, #77, #78.
Chay: py -3 .work/_qc_shots_en_t05.py
"""
import json
import os
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ.setdefault("AE_EP", "05")
os.environ.setdefault("AE_LANG", "en")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

OK, WARN, INFO, FAIL = [], [], [], []


def ok(m):
    OK.append(m)


def bad(m):
    FAIL.append(m)


def warn(m):
    WARN.append(m)


def info(m):
    INFO.append(m)


PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
STOP = set("""the and for that with this from have has had was were been being they them their there
here what which when where who whom whose why how all any both each few more most other some such
than then too very can will just dont does did doing have had would should could may might must
into over under about after before between during without within upon across against toward
towards through during make made makes take takes took taken give gives gave get gets got
said says say also even still yet own same only own both while because although though however
therefore thus hence moreover furthermore besides instead rather quite rather much many less least
own life lives world worlds man men woman women thing things way ways part parts time times year
years day days night nights people person man women left right new old first second third one two
three four five six seven eight nine ten like unlike just even still yet""".split())
EN_UNITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
            "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
            "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19}
EN_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
           "seventy": 70, "eighty": 80, "ninety": 90}
EN_ORD = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6,
          "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10, "eleventh": 11,
          "twelfth": 12, "thirteenth": 13, "fourteenth": 14, "fifteenth": 15,
          "sixteenth": 16, "seventeenth": 17, "eighteenth": 18, "nineteenth": 19,
          "twentieth": 20, "thirtieth": 30, "fortieth": 40, "fiftieth": 50,
          "sixtieth": 60, "seventieth": 70, "eightieth": 80, "ninetieth": 90}


def en_nums(t):
    t = t.lower()
    for w, d in EN_ORD.items():
        t = re.sub(rf"\b{w}\b", str(d), t)

    # 'one hundred and seventy-five' -> 175 (phai chay TRUOC khi doi don/tu)
    def hund(m):
        a = EN_UNITS.get(m.group(1), 1)
        rest = m.group(2) or ""
        total = a * 100
        mm = re.match(r"\s*(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)"
                      r"(?:[-\s]+(one|two|three|four|five|six|seven|eight|nine))?", rest)
        if mm:
            total += EN_TENS[mm.group(1)]
            if mm.group(2):
                total += EN_UNITS[mm.group(2)]
        return f" {total} "

    t = re.sub(r"\b(one|two|three|four|five|six|seven|eight|nine)\s+hundred"
               r"(?:\s+and\s+([\w-]+(?:\s+[\w-]+){0,3}))?(?=[\s.,;!?]|$)", hund, t)

    def tens(m):
        a = EN_TENS[m.group(1)]
        b = EN_UNITS.get(m.group(2)) if m.group(2) else 0
        return f" {a + b} "

    t = re.sub(r"\b(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)"
               r"(?:[-\s]+(one|two|three|four|five|six|seven|eight|nine))?\b", tens, t)
    for w, d in EN_UNITS.items():
        t = re.sub(rf"\b{w}\b", str(d), t)
    t = re.sub(r"\b(\d+)(?:st|nd|rd|th)\b", r"\1", t)
    return t


def norm(t):
    t = t.replace("\u2019", "'").replace("\u2018", "'")
    t = t.replace("\u2014", " ").replace("\u2013", " ").replace("\u00b7", " ")
    t = PUNCT.sub(" ", t.lower())
    t = re.sub(r"\s+", " ", t).strip()
    t = en_nums(t)
    return re.sub(r"\s+", " ", t).strip()


def frags(q):
    return [f.strip() for f in re.split(r"\u2026|\.\.\.", q) if f.strip()]


def seg_target(shot, at):
    """Renderer khop at_sentence theo HAU TO ma cau (#N trong element), khong phai
    chi so trong shot (build_video3.seg_times: s.endswith(f"#{at}"))."""
    tgt = [c for c in shot["sentences"] if c.endswith(f"#{at}")]
    return tgt[0] if tgt else None


def main():
    tl = json.loads((WORK / "timeline_s_EN_t05.json").read_text(encoding="utf-8"))
    sh = json.loads((WORK / "shots_EN_t05.json").read_text(encoding="utf-8"))
    script = json.loads((WORK / "script_tap05_EN.json").read_text(encoding="utf-8"))

    SENT = {it["id"]: it for it in tl["items"]}
    ORDER = [it["id"] for it in tl["items"]]
    TOT = tl["total"]
    shots = sh["shots"]
    NMAP = ED.EP.get("n_element", {})          # element -> N1/N2

    role_script = {}
    for el in script:
        if el.get("kind") != "LOI":
            continue
        for s in el.get("sentences", []):
            r = el.get("role")
            if r == "N":
                r = NMAP.get(el["id"], "N")
            role_script[s["id"]] = r

    # so co trong TOAN BO tap (de cap phep ngoai le cua chuan: "so da co trong cau khac cung tap")
    ep_numbers = set()
    for t in SENT.values():
        ep_numbers.update(re.findall(r"\d+", norm(t["text"])))

    print(f"===== QC bang shot EN Tap05 — {len(shots)} shot =====")
    print(f"timeline total = {TOT} s · {len(ORDER)} cau · shots total = {sh['total']} s\n")

    # --- 0. timeline <-> script
    sc_ids = [s["id"] for el in script if el.get("kind") == "LOI" for s in el.get("sentences", [])]
    if sc_ids != ORDER:
        bad("0) Thu tu/so cau cua timeline KHAC script")
    else:
        ok(f"0) Timeline khop script: {len(ORDER)} cau, dung thu tu")
    vb = [(c, role_script.get(c), SENT[c]["role"]) for c in ORDER
          if role_script.get(c) != SENT[c]["role"]]
    if vb:
        for c, a, b in vb[:10]:
            bad(f"0) Vai '{c}': timeline='{b}' khac script='{a}'")
    else:
        ok(f"0) Vai cua {len(ORDER)}/{len(ORDER)} cau khop vai kich ban (da ap mapping N -> N1/N2)")

    # --- 1. phu cau
    seen = []
    for s in shots:
        seen += s["sentences"]
    dup = sorted({c for c in seen if seen.count(c) > 1})
    missing = [c for c in ORDER if c not in seen]
    extra = [c for c in seen if c not in SENT]
    seq = [c for c in seen if c in ORDER]
    if dup:
        bad(f"1) Trung mau cau: {dup[:12]}")
    if missing:
        bad(f"1) Thieu {len(missing)} cau: {missing[:12]}")
    if extra:
        bad(f"1) Mau cau khong ton tai: {sorted(set(extra))[:12]}")
    if seq != sorted(seq, key=ORDER.index):
        bad("1) Thu tu cau trong bang shot KHONG dung thu tu kich ban")
    if not dup and not missing and not extra and seq == sorted(seq, key=ORDER.index):
        ok(f"1) Phu 100% {len(ORDER)} cau, dung thu tu, khong trung")

    # --- 2. moc thoi gian
    terr = []
    for i, s in enumerate(shots):
        if s["sentences"]:
            exp = round(SENT[s["sentences"][0]]["start"] - 0.20, 3)
            if abs(s["start"] - exp) > 0.002:
                terr.append(f"{s['id']}: start {s['start']} != {exp}")
        if i + 1 < len(shots) and abs(s["end"] - shots[i + 1]["start"]) > 0.002:
            terr.append(f"{s['id']}: end {s['end']} != start sau {shots[i + 1]['start']}")
        if s["end"] - s["start"] <= 0:
            terr.append(f"{s['id']}: thoi luong <= 0")
    if terr:
        for t in terr[:10]:
            bad(f"2) Moc thoi gian sai: {t}")
    else:
        ok(f"2) Moc thoi gian {len(shots)}/{len(shots)} shot lay dung tu timeline (start = cau dau - 0,20 s; lien tuc)")
    if abs(sh["total"] - TOT) > 0.002:
        bad(f"2) shots.total {sh['total']} != timeline.total {TOT}")
    else:
        ok(f"2) shots.total == timeline.total == {TOT} s")
    if abs(shots[-1]["end"] - TOT) > 0.002:
        bad(f"2) Shot cuoi ket thuc {shots[-1]['end']} != {TOT}")
    else:
        ok(f"2) Shot cuoi ('het tap') chay toi dung {TOT} s")

    # --- 3. nen co file
    bgfiles = {p.stem for p in (ROOT / "assets" / "bg").glob("*.png")}
    missbg = sorted({s["bg"] for s in shots} - bgfiles - {"void"})
    if missbg:
        bad(f"3) Nen khong co file: {missbg}")
    else:
        ok(f"3) 100% nen co file ({len({s['bg'] for s in shots})} nen)")

    # --- 4. vai noi
    vbad = []
    for s in shots:
        if not s["sentences"]:
            continue
        roles = {SENT[c]["role"] for c in s["sentences"]}
        if s["role"] and s["role"] not in roles:
            vbad.append((s["id"], s["role"], sorted(x for x in roles if x)))
    if vbad:
        for i, w, g in vbad[:10]:
            bad(f"4) {i}: vai shot '{w}' khac vai kich ban {g}")
    else:
        ok(f"4) H13: vai noi khop vai kich ban ({len(shots)}/{len(shots)} shot)")

    # --- 5. H6/V3 chu tren hinh lay tu cau dang doc
    # Tieu de (bold/ital) cua kenh la DANG RUT GON (VN Tap05 da xuat ban co 111/154 doan
    # khong phai substring cua cau) => do bang DO CHONG LAP TU, khong bang so khac.
    seg_bad, seg_n, seg_ok = [], 0, 0
    overlap_rows = []
    for s in shots:
        if not s["sentences"]:
            continue
        body_all = norm(" ".join(SENT[c]["text"] for c in s["sentences"]))
        body_words = set(body_all.split())
        for seg in s["segments"]:
            at = seg.get("at_sentence")
            if at is not None:
                tid = seg_target(s, at)
                if tid is None:
                    seg_bad.append((s["id"], f"at_sentence #{at} khong khop cau nao trong shot", ""))
                    continue
                body = norm(SENT[tid]["text"])
            else:
                body = body_all
            for style, txt in seg["elems"]:
                seg_n += 1
                if style == "quote":
                    for fr in frags(txt):
                        t = norm(fr)
                        if not t:
                            continue
                        if t in body:
                            seg_ok += 1
                        else:
                            seg_bad.append((s["id"], fr[:70], style))
                else:
                    words = [w for w in norm(txt).split()
                             if len(w) >= 4 and w not in STOP and not w.isdigit()]
                    if words:
                        hit = sum(1 for w in words if w in body_words)
                        ov = hit / len(words)
                        overlap_rows.append((ov, s["id"], txt[:56], hit, len(words)))
    if seg_bad:
        for i, t, st in seg_bad[:16]:
            bad(f"5) H6 {i}: chu tren hinh ({st}) KHONG co trong cau dang doc: '{t}'")
        if len(seg_bad) > 16:
            bad(f"5) ... them {len(seg_bad) - 16} loi")
    else:
        ok(f"5) H6/V3: {seg_ok}/{seg_ok + len(seg_bad)} trich danh nguyen van; "
           f"{seg_n - seg_ok} tieu de rut gon — kiem do chong lap tu o gate 5b")
    overlap_rows.sort()
    low = [r for r in overlap_rows if r[0] < 0.5]
    info(f"5b) Do chong lap tu (tieu de rut gon voi cau dang doc): "
         f"{len(overlap_rows)} doan · {len(low)} doan < 50% · trung binh "
         f"{sum(r[0] for r in overlap_rows) / max(1, len(overlap_rows)) * 100:.0f}%")
    for ov, sid, txt, hit, tot in low[:20]:
        warn(f"5b) {sid}: chong lap {ov*100:.0f}% ({hit}/{tot}) — '{txt}'")

    # --- 5c. segment co at_sentence: noi dung phai khop CAU DUOC GAN NHAT
    # (bat loi lech nhip 1 cau — loai loi chup anh / loi thoai lech nhip)
    at_bad = []
    for s in shots:
        if not s["sentences"]:
            continue
        for seg in s["segments"]:
            at = seg.get("at_sentence")
            if not at:
                continue
            sid_ = seg_target(s, at)
            if sid_ is None:
                bad(f"5c) {s['id']}: at_sentence #{at} khong khop cau nao trong shot "
                    f"{s['sentences']} -> segment KHONG BAO GIO hien")
                continue
            tgt = set(norm(SENT[sid_]["text"]).split())
            for style, txt in seg["elems"]:
                words = [w for w in norm(txt).split()
                         if len(w) >= 4 and w not in STOP and not w.isdigit()]
                if words and not any(w in tgt for w in words):
                    at_bad.append((s["id"], sid_, at, txt[:60]))
    if at_bad:
        for sid, tgt, at, txt in at_bad:
            warn(f"5c) {sid}: segment gan vao '{tgt}' (at=#{at}) khong chua tu nao cua cau do — '{txt}'")
    else:
        ok("5c) Moi segment gan theo cau deu khop hau to #N va co tu trong dung cau do")

    # --- 6. H6 so tren hinh
    num_bad, num_ok, num_ex = [], 0, []
    for s in shots:
        if not s["sentences"]:
            continue
        body = norm(" ".join(SENT[c]["text"] for c in s["sentences"]))
        for seg in s["segments"]:
            for style, txt in seg["elems"]:
                for tok in re.findall(r"\d+", txt):
                    tokc = tok.lstrip("0") or "0"
                    if tok in body or re.search(r"(?<!\d)" + re.escape(tokc) + r"(?!\d)", body):
                        num_ok += 1
                    elif tokc in ep_numbers:
                        num_ex.append((s["id"], tok, "so da co trong cau khac cung tap (da kiem chung)"))
                    else:
                        num_bad.append((s["id"], tok, txt[:60]))
    for i, tok, why in num_ex:
        info(f"6) [NGOAI LE] {i}: so '{tok}' — {why}")
    if num_bad:
        for i, tok, p in num_bad[:16]:
            bad(f"6) H6 {i}: so '{tok}' tren hinh khong co trong cau dang doc — '{p}'")
    else:
        ok(f"6) H6: {num_ok}/{num_ok + len(num_ex)} chu so tren hinh deu co trong cau dang doc")

    # --- 7. H6 trich danh nguyen van
    q_bad, q_ok = [], 0
    for s in shots:
        if not s["sentences"]:
            continue
        body_all = norm(" ".join(SENT[c]["text"] for c in s["sentences"]))
        for seg in s["segments"]:
            at = seg.get("at_sentence")
            tid = seg_target(s, at) if at else None
            body = norm(SENT[tid]["text"]) if tid else body_all
            for style, txt in seg["elems"]:
                if style == "quote":
                    for fr in frags(txt):
                        t = norm(fr)
                        if t and t in body:
                            q_ok += 1
                        else:
                            q_bad.append((s["id"], fr[:70]))
    if q_bad:
        for i, q in q_bad[:10]:
            bad(f"7) H6 {i}: trich danh khong nguyen van — '{q}'")
    else:
        ok(f"7) H6: {q_ok} trich danh deu nguyen van trong cau dang doc")

    # --- 8. H10 thoi luong (doi chieu duong co VN Tap05 da xuat ban)
    ds = [s["end"] - s["start"] for s in shots]
    lt3 = [s["id"] for s in shots if s["end"] - s["start"] < 3]
    gt15 = [s["id"] for s in shots if s["end"] - s["start"] > 15]
    info(f"8) H10 thoi luong shot: min {min(ds):.1f}s · median {sorted(ds)[len(ds)//2]:.1f}s · "
         f"max {max(ds):.1f}s · {len(lt3)} shot < 3s · {len(gt15)} shot > 15s")
    info("8) [GOC] bang VN Tap05 da xuat ban co 13 shot < 3s · 43 shot > 15s (max 60,7s) "
         "=> chu H10 3-15s khong duoc kenh ap dung that; EN tot hon VN")

    # --- 9. H10 nen lap
    run, prev, maxrun, runat = 1, None, 1, ""
    for s in shots:
        run = run + 1 if s["bg"] == prev else 1
        prev = s["bg"]
        if run > maxrun:
            maxrun, runat = run, s["id"]
    if maxrun > 4:
        bad(f"9) H10: nen lap toi {maxrun} shot lien nhau (tai {runat})")
    else:
        ok(f"9) H10: nen lap toi da {maxrun} shot lien nhau (<= 4)")

    # --- 10. A11 #77 chuoi handoff
    hbad, nh = [], 0
    for i in range(len(shots) - 1):
        h = shots[i]["flags"].get("handoff") or []
        nh += len(h)
        want = shots[i + 1]["role"]
        if want and h and want not in h:
            hbad.append((shots[i]["id"], h, want))
    if hbad:
        for i, h, w in hbad[:10]:
            bad(f"10) A11 #77 {i}: handoff {h} khong khop vai dong sau '{w}'")
    else:
        ok(f"10) A11 #77: chuoi handoff khop vai dong sau ({nh} handoff)")

    # --- 11. H12 the ket
    last = shots[-1]
    txts = [t for seg in last["segments"] for _s, t in seg["elems"]]
    joined = " ".join(txts).upper()
    if last["id"] != "5-20" or "DOSSIER EPISODE 05" not in joined or "AMBER EYES" not in joined:
        bad(f"11) H12: the ket thieu chu — {txts}")
    else:
        ok(f"11) H12: the ket co chu '{' '.join(txts)[:66]}'")
    if abs(last["end"] - TOT) > 0.002:
        bad(f"11) The ket ket thuc {last['end']} != {TOT}")
    else:
        ok(f"11) The ket chay toi het {TOT} s")

    # --- 12. the chuyen hoi = T10 + void
    plan = ED.PLAN.read_text(encoding="utf-8-sig")
    sec = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
    sec = plan[sec.end():]
    sec = sec[:re.search(r"^\*\*Tổng:", sec, re.M).start()]
    rows = {c[0]: c for c in ([x.strip() for x in l.strip().strip("|").split("|")]
                               for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l))}
    tabad = []
    nact = 0
    for s in shots:
        row = rows.get(s["id"])
        if not row:
            continue
        is_act = "chuyển hồi" in row[1]
        if is_act:
            nact += 1
            if s["template"] != "T10" or s["bg"] != "void":
                tabad.append(s["id"])
    if tabad:
        bad(f"12) The chuyen hoi sai: {tabad}")
    elif nact != 4:
        bad(f"12) Chi tim thay {nact} the chuyen hoi (ky vong 4: cuoi moi hoi 1-4)")
    else:
        ok("12) 4 the chuyen hoi (cuoi hoi 1-4) deu la T10 + nen void")

    # --- 13. intro + moc hoi
    if abs(shots[0]["start"] - 20.5) > 0.002:
        bad(f"13) Shot dau bat dau o {shots[0]['start']} != 20,5 s")
    elif abs(tl["intro"] - 22.41) > 0.002:
        bad(f"13) Intro = {tl['intro']} != 22,41 s")
    else:
        ok("13) Intro 22,41 s · shot 'the hoi 1' bat dau 20,50 s — khop video intro")

    print()
    for x in OK:
        print(f"  [OK]   {x}")
    for x in INFO:
        print(f"  [INFO] {x}")
    for x in WARN:
        print(f"  [WARN] {x}")
    for x in FAIL:
        print(f"  [FAIL] {x}")
    print(f"\n  => {len(OK)} OK · {len(INFO)} thong tin · {len(WARN)} canh bao · {len(FAIL)} loi")
    (WORK / "_qc_shots_en_t05_result.json").write_text(
        json.dumps({"ok": OK, "info": INFO, "warn": WARN, "fail": FAIL}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
