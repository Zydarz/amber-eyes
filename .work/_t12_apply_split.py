# -*- coding: utf-8 -*-
"""Tập 12 — áp dụng kế hoạch tách nền H25 vào bảng shot + dựng jobs v2.

    py -3 .work/_t12_apply_split.py --dry-run     # chỉ kiểm
    py -3 .work/_t12_apply_split.py --apply       # ghi file

Ghi:
  02_SAN_XUAT/Tap12/KeHoach_Video_Tap12.md   (mã nền ở cột "Nền + bóng")
  .work/bg_jobs_tap12_v2.json                (83 job cũ + 68 mới + 1 thẻ kết = 152)
"""
import collections
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, r"D:/TEST/Gax/amber-eyes/.work")
from _t12_new_bg_jobs import NEW, END_CARD  # noqa: E402

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PLAN = ROOT / "02_SAN_XUAT/Tap12/KeHoach_Video_Tap12.md"
JOBS_V1 = ROOT / ".work/bg_jobs_tap12.json"
JOBS_V2 = ROOT / ".work/bg_jobs_tap12_v2.json"
BACKUP = ROOT / ".work/_cu/t12_split_20261116"
ROW = re.compile(r"^(\|\s*[1-5]-\d+\s*\|)(.*)$")
BG_RE = re.compile(r"`(t\d+_[a-z0-9_]+)`")


def load_chunks():
    d = json.loads((ROOT / ".work/_t12_chunks.json").read_text(encoding="utf-8"))
    return d["chunks"], d.get("end_card")


def parse_plan(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        m = ROW.match(line.rstrip("\n"))
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        bg = BG_RE.search(cells[3] if len(cells) > 3 else "")
        cau = re.search(r"`([^`]+)`", cells[0])
        sid = re.search(r"[1-5]-\d+", m.group(1)).group(0)
        rows.append(dict(sid=sid,
                         cau=cau.group(1) if cau else cells[0],
                         bg=bg.group(1) if bg else None,
                         card=bool(re.search(r"nghỉ chuyển hồi|hết tập", cells[0]))))
    return rows


def assign_codes(chunks):
    """Nhóm đầu tiên của mỗi mã cũ GIỮ mã cũ; nhóm sau cần MÃ MỚI."""
    keep = collections.Counter()
    codes = {}
    for i, c in enumerate(chunks):
        keep[c["parent"]] += 1
        if keep[c["parent"]] == 1:
            codes[i] = c["parent"]
        else:
            if i not in NEW:
                raise SystemExit(f"THIEU prompt cho nhóm {i} (mã cũ {c['parent']})")
            codes[i] = NEW[i][0]
    return codes


def rewrite(text, sid2code, end_sid):
    out = []
    n = 0
    for line in text.split("\n"):
        m = ROW.match(line)
        if not m:
            out.append(line)
            continue
        cells = m.group(2).split("|")
        idx = None
        for i, c in enumerate(cells):
            if BG_RE.search(c):
                idx = i
                break
        if idx is None:
            out.append(line)
            continue
        sid = re.search(r"[1-5]-\d+", m.group(1)).group(0)
        code = sid2code.get(sid)
        if code is None:
            raise SystemExit(f"shot {sid} không có mã nền")
        cells[idx] = BG_RE.sub(f"`{code}`", cells[idx])
        out.append(m.group(1) + "|".join(cells))
        n += 1
    return "\n".join(out), n


def main():
    apply_ = "--apply" in sys.argv
    chunks, end_card_sid = load_chunks()
    rows = parse_plan(PLAN)
    codes = assign_codes(chunks)

    # mã nền theo shot
    sid2code = {}
    shots_of = collections.defaultdict(list)
    for c in chunks:
        for r in c["sids"]:
            sid2code[r] = codes[chunks.index(c)] if False else None
    for i, c in enumerate(chunks):
        for r in c["sids"]:
            sid2code[r] = codes[i]
    end_code = END_CARD[0]
    end_sid = end_card_sid
    sid2code[end_sid] = end_code

    all_codes = set(codes.values()) | {end_code}
    used_in_plan = {sid2code.get(r["sid"]) for r in rows if r["bg"]}
    print(f"nhóm nền: {len(chunks)} + thẻ kết 1 = {len(all_codes)} mã nền")
    print(f"mã cũ giữ nguyên: {len(set(codes.values())) - sum(1 for i in codes if codes[i] != chunks[i]['parent'])}"
          f" · MÃ MỚI: {sum(1 for i in codes if codes[i] != chunks[i]['parent'])} + 1 thẻ kết")
    assert len(all_codes) == len(set(all_codes)), "TRÙNG MÃ NỀN"

    # --- kiểm H22/H25 trên bảng shot ---
    used = collections.Counter()
    for r in rows:
        if r["bg"] or r["card"]:
            code = sid2code.get(r["sid"])
            if code:
                used[code] += 1
    over = [(b, k) for b, k in used.items() if k > 3]
    print(f"nền dùng trên bảng: {len(used)} · shot/nền = {sum(used.values())/len(used):.2f} · "
          f"vi phạm >3 shot: {len(over)} {over[:6]}")
    assert not over, "còn nền vượt 3 shot"

    # --- kiểm job ---
    old = json.loads(JOBS_V1.read_text(encoding="utf-8"))
    old_by = {j["name"]: j for j in old}
    chunk_by_code = {codes[i]: c for i, c in enumerate(chunks)}
    jobs = []
    for code in sorted(all_codes):
        if code in old_by:
            j = dict(old_by[code])
            c = chunk_by_code.get(code)
            if c:
                j["sentences"] = "–".join(c["caus"])
            jobs.append(j)
        elif code == end_code:
            name, desc, prompt = END_CARD
            jobs.append({"name": code, "act": 5, "sentences": "", "desc": desc, "prompt": prompt})
        else:
            idx = next(i for i in codes if codes[i] == code)
            name, desc, prompt = NEW[idx]
            c = chunk_by_code[code]
            jobs.append({"name": code, "act": int(c["caus"][0].split(".")[0]),
                         "sentences": "–".join(c["caus"]), "desc": desc, "prompt": prompt})
    names = [j["name"] for j in jobs]
    assert len(names) == len(set(names)), "trùng tên job"
    # mọi job phải được dùng trong bảng shot
    unused = [n for n in names if n not in used]
    print(f"job: {len(jobs)} (cũ {len(old_by)} · mới {len(jobs) - len(old_by)}) · job không shot nào dùng: {len(unused)} {unused}")
    assert not unused, "còn job không dùng"
    # mọi mã nền trên bảng phải có job
    nojob = sorted(c for c in used if c not in set(names))
    print(f"mã nền trên bảng thiếu job: {len(nojob)} {nojob[:5]}")
    assert not nojob, "thiếu job"

    if not apply_:
        print("\nDRY-RUN — chưa ghi file. Chạy lại với --apply để ghi.")
        return

    BACKUP.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PLAN, BACKUP / PLAN.name)
    shutil.copy2(JOBS_V1, BACKUP / JOBS_V1.name)
    print(f"\nđã sao lưu vào {BACKUP}")

    text = PLAN.read_text(encoding="utf-8")
    new_text, n = rewrite(text, sid2code, end_sid)
    PLAN.write_text(new_text, encoding="utf-8")
    print(f"  {PLAN.name}: đổi mã nền {n} dòng")

    JOBS_V2.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  {JOBS_V2.name}: {len(jobs)} job ({len(old_by)} cũ giữ + {len(jobs) - len(old_by)} mới)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
