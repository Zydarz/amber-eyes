# -*- coding: utf-8 -*-
"""Tập 11 — áp dụng kế hoạch tách nền H25 vào bảng shot 3 ngôn ngữ + dựng jobs v3.

    py -3 .work/_t11_apply_split.py --dry-run     # chỉ kiểm
    py -3 .work/_t11_apply_split.py --apply       # ghi file

Ghi:
  02_SAN_XUAT/Tap11/KeHoach_Video_Tap11.md        (mã nền ở cột "Nền + bóng")
  02_SAN_XUAT/Tap11_EN/KeHoach_Video_Tap11_EN.md
  02_SAN_XUAT/Tap11_JA/KeHoach_Video_Tap11_JA.md
  .work/bg_jobs_tap11_v3.json                     (136 job = 66 cũ + 70 mới)
"""
import collections
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, r"D:/TEST/Gax/amber-eyes/.work")
from _t11_chunk_plan import parse, build, MD  # noqa: E402
from _t11_new_bg_jobs import NEW, END_CARD  # noqa: E402

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PLAN = {
    "vi": ROOT / "02_SAN_XUAT/Tap11/KeHoach_Video_Tap11.md",
    "en": ROOT / "02_SAN_XUAT/Tap11_EN/KeHoach_Video_Tap11_EN.md",
    "ja": ROOT / "02_SAN_XUAT/Tap11_JA/KeHoach_Video_Tap11_JA.md",
}
JOBS_V2 = ROOT / ".work/bg_jobs_tap11_v2.json"
JOBS_V3 = ROOT / ".work/bg_jobs_tap11_v3.json"
BACKUP = ROOT / ".work/_cu/t11_split_20261116"
ROW = re.compile(r"^(\|\s*[1-5]-\d+\s*\|)(.*)$")


def assign_codes():
    rows = parse(str(PLAN["vi"]))
    chunks, end_card = build(rows)
    keep = collections.Counter()
    codes = {}          # chunk index -> mã nền
    shots_of = {}       # mã nền -> [sid]
    for i, c in enumerate(chunks):
        keep[c["parent"]] += 1
        k = keep[c["parent"]]
        if k == 1:
            code = c["parent"]
        else:
            if i not in NEW:
                raise SystemExit(f"THIEU prompt cho chunk {i} (parent {c['parent']})")
            code = NEW[i][0]
        codes[i] = code
        shots_of[code] = [r["sid"] for r in c["rows"]]
    # thẻ kết
    end_code = END_CARD[0]
    shots_of[end_code] = [end_card["sid"]]
    sid2code = {}
    for code, sids in shots_of.items():
        for s in sids:
            sid2code[s] = code
    return rows, chunks, codes, sid2code, end_card, end_code


def rewrite(text, sid2code, lang):
    out = []
    n = 0
    for line in text.split("\n"):
        m = ROW.match(line)
        if not m:
            out.append(line)
            continue
        cells = m.group(2).split("|")
        # cột "Nền + bóng" = index 3 trong phần sau mã shot
        idx = None
        for i, c in enumerate(cells):
            if re.search(r"`t\d+_[a-z0-9_]+`", c):
                idx = i
                break
        if idx is None:
            out.append(line)
            continue
        sid = re.search(r"[1-5]-\d+", m.group(1)).group(0)
        if sid not in sid2code:
            raise SystemExit(f"[{lang}] shot {sid} không có trong bảng VI")
        new_code = sid2code[sid]
        cells[idx] = re.sub(r"`t\d+_[a-z0-9_]+`", f"`{new_code}`", cells[idx])
        out.append(m.group(1) + "|".join(cells))
        n += 1
    return "\n".join(out), n


def build_jobs(codes, chunks, sid2code, end_code):
    old = json.loads(JOBS_V2.read_text(encoding="utf-8"))
    old_by = {j["name"]: j for j in old}
    used_codes = set(codes.values()) | {end_code}
    # code cũ giữ nguyên -> dùng lại job cũ (nhưng cập nhật sentences theo chunk hiện tại)
    chunk_by_code = {}
    for i, c in enumerate(chunks):
        chunk_by_code[codes[i]] = c
    jobs = []
    for code in sorted(used_codes):
        if code in old_by:
            j = dict(old_by[code])
            c = chunk_by_code.get(code)
            if c:
                j["sentences"] = "–".join(r["cau"] for r in c["rows"])
            jobs.append(j)
        else:
            if code == end_code:
                name, desc, prompt = END_CARD
                act = 5
                sids = [end_code]
            else:
                idx = next(i for i, v in codes.items() if v == code)
                name, desc, prompt = NEW[idx]
                c = chunk_by_code[code]
                act = int(c["rows"][0]["cau"].split(".")[0])
                sids = None
            jobs.append({"name": code, "act": act, "sentences": "", "desc": desc, "prompt": prompt})
    # điền sentences cho job mới
    for j in jobs:
        if not j.get("sentences"):
            sids = [s for s, c in sid2code.items() if c == j["name"]]
            caus = []
            for s in sorted(sids):
                pass
            j["sentences"] = ""
    return jobs


def main():
    apply_ = "--apply" in sys.argv
    rows, chunks, codes, sid2code, end_card, end_code = assign_codes()
    new_codes = [codes[i] for i in range(len(chunks)) if codes[i] != chunks[i]["parent"]]
    print(f"mã nền: {len(set(codes.values()))} + thẻ kết 1 = {len(set(codes.values())) + 1}")
    print(f"giữ tên cũ: {len(set(codes.values())) - len(new_codes)} · MÃ MỚI: {len(new_codes)} + 1 thẻ kết = {len(new_codes) + 1}")
    # trùng tên?
    allnames = list(set(codes.values())) + [end_code]
    dup = [k for k, v in collections.Counter(allnames).items() if v > 1]
    assert not dup, f"TRÙNG TÊN: {dup}"
    old_names = {j["name"] for j in json.loads(JOBS_V2.read_text(encoding='utf-8'))}
    clash = [n for n in new_codes if n in old_names]
    print("trùng với job cũ (sẽ ghi đè file có sẵn):", clash)

    # ---- kiểm ràng buộc H22/H25 cho 3 ngôn ngữ (đo trên KẾ HOẠCH) ----
    print("\n--- kiểm ≤3 shot & ≤30 s theo từng ngôn ngữ ---")
    for lang, path in PLAN.items():
        rr = parse(str(path))
        used = collections.Counter()
        sec = collections.defaultdict(float)
        cur = None
        for r in rr:
            if r["bg"]:                       # dòng có mã nền -> mã KẾ HOẠCH
                cur = sid2code.get(r["sid"], r["bg"])
            if not cur:
                continue
            used[cur] += 1
            sec[cur] += r["dur"]
        over = [(b, used[b], round(sec[b], 1)) for b in used if used[b] > 3 or sec[b] > 30]
        print(f"  {lang}: {len(used)} mã nền · {sum(used.values())} dòng · "
              f"{sum(used.values())/max(len(used),1):.2f} shot/nền · vi phạm: {len(over)}")
        for b, k, s in sorted(over, key=lambda x: -x[2])[:8]:
            print(f"      {b}: {k} shot · {s}s")
        assert len(used) == len(allnames), f"{lang}: số mã nền lệch ({len(used)} vs {len(allnames)})"
        assert len(rr) == len(rows), f"{lang}: số dòng lệch ({len(rr)} vs {len(rows)})"
        assert not over, f"{lang}: còn {len(over)} nền vi phạm H22"

    if not apply_:
        print("\nDRY-RUN — chưa ghi file. Chạy lại với --apply để ghi.")
        return

    BACKUP.mkdir(parents=True, exist_ok=True)
    for lang, path in PLAN.items():
        shutil.copy2(path, BACKUP / path.name)
    print(f"\nđã sao lưu 3 bảng shot vào {BACKUP}")

    for lang, path in PLAN.items():
        text = path.read_text(encoding="utf-8")
        new_text, n = rewrite(text, sid2code, lang)
        path.write_text(new_text, encoding="utf-8")
        print(f"  {lang}: đổi mã nền {n} dòng → {path.name}")

    # ---- jobs v3 ----
    old = json.loads(JOBS_V2.read_text(encoding="utf-8"))
    old_by = {j["name"]: j for j in old}
    chunk_by_code = {codes[i]: chunks[i] for i in range(len(chunks))}
    jobs = []
    for code in sorted(set(codes.values()) | {end_code}):
        if code in old_by:
            j = dict(old_by[code])
            c = chunk_by_code.get(code)
            if c:
                j["sentences"] = "–".join(r["cau"] for r in c["rows"])
            jobs.append(j)
        else:
            if code == end_code:
                name, desc, prompt = END_CARD
                act = 5
                sids = [end_card["sid"]]
                sent = ""
            else:
                idx = next(i for i, v in codes.items() if v == code)
                name, desc, prompt = NEW[idx]
                c = chunk_by_code[code]
                act = int(c["rows"][0]["cau"].split(".")[0])
                sids = [r["sid"] for r in c["rows"]]
                sent = "–".join(r["cau"] for r in c["rows"])
            jobs.append({"name": code, "act": act, "sentences": sent,
                         "desc": desc, "prompt": prompt})
    JOBS_V3.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n→ {JOBS_V3.name}: {len(jobs)} job "
          f"({len(old_by)} cũ giữ + {len(jobs) - len(old_by)} mới)")
    names = [j["name"] for j in jobs]
    assert len(names) == len(set(names))


if __name__ == "__main__":
    main()
