#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng kiểm mapping kịch bản <-> bg_jobs (chạy TRƯỚC khi sinh ảnh / dựng bảng shot).

Dùng:  py -3 .work/qc_bg_mapping.py [--from 25] [--to 68] [XX ...]
Exit 1 nếu có tập TRƯỢT. Ba luật:
  M1  mọi mã `sentences` của job phải tồn tại trong kịch bản VN hiện tại
  M2  không có hai tập trùng prompt (md5) — dấu hiệu bộ prompt bị chép nhầm tập
  M5  mọi câu của kịch bản phải được >=1 job phủ
  M4  >= 90% prompt phải khác nhau (H22/H25: mỗi shot một cảnh; bộ mẫu chung 17 prompt = TRƯỢT)
  M3  (chỉ cảnh báo, không tính TRƯỢT) nhãn "Tập NN" ghi trong desc (nếu có) chỉ là cảnh báo; tên riêng chính của
      kịch bản (từ tiêu đề kịch bản) phải xuất hiện trong desc/prompt >= 1 job
"""
import argparse, glob, hashlib, importlib.util, json, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
spec = importlib.util.spec_from_file_location("pk", WORK / "parse_kichban.py")
pk = importlib.util.module_from_spec(spec); spec.loader.exec_module(pk)


def script_file(n):
    fs = [f for f in glob.glob(str(ROOT / f"01_KICH_BAN/Ho_So_Toi_Pham/Tap{n:02d}/kichban_tap{n:02d}_*.md"))
          if not re.search(r"_cu|_EN|_JA|_KO", f)]
    return sorted(fs)[-1] if fs else None


def title_names(path):
    """Tên riêng trong dòng tiêu đề sau 'HỒ SƠ' (vd 'TRƯƠNG TỬ CƯỜNG')."""
    h = open(path, encoding="utf-8").readline()
    m = re.search(r"(?:HỒ SƠ|VỤ ÁN|KỲ ÁN)\s+(.+?)(?:\s+[—-]\s+|$)", h)
    return [w for w in re.split(r"\W+", m.group(1).lower()) if len(w) >= 3] if m else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("eps", nargs="*", type=int)
    ap.add_argument("--from", dest="a", type=int, default=25)
    ap.add_argument("--to", dest="b", type=int, default=68)
    a = ap.parse_args()
    eps = a.eps or range(a.a, a.b + 1)
    jobs, md5 = {}, {}
    for p in sorted(WORK.glob("bg_jobs_tap[0-9][0-9].json")):
        n = int(p.stem[-2:]); jobs[n] = json.load(open(p, encoding="utf-8"))
        md5[n] = hashlib.md5("|".join(x["prompt"] for x in jobs[n]).encode()).hexdigest()
    fail = 0
    for n in eps:
        sf = script_file(n)
        if n not in jobs:
            print(f"Tập {n:02d}: CHƯA CÓ bg_jobs" + ("" if sf else " · chưa có kịch bản")); continue
        if not sf:
            print(f"Tập {n:02d}: TRƯỢT · không có kịch bản"); fail += 1; continue
        codes = {s["id"] for e in pk.parse_file(sf) for s in (e.get("sentences") or [])}
        bad = [c for x in jobs[n] for c in re.split(r"[,;\s]+", str(x.get("sentences", ""))) if c and c not in codes]
        dup = [m for m in jobs if m != n and md5[m] == md5[n]]
        names = title_names(sf)
        blob = " ".join((x.get("desc", "") + " " + x.get("prompt", "") + " " + x["name"]).lower() for x in jobs[n])
        named = [w for w in names if w in blob]
        m3 = bool(named) or not names
        cnt = {}
        for x in jobs[n]:
            for c in re.split(r"[,;\s]+", str(x.get('sentences', ''))):
                if c: cnt[c] = cnt.get(c, 0) + 1
        miss = [c for c in codes if c not in cnt]
        m5 = not miss
        distinct = len({x['prompt'] for x in jobs[n]})
        m4 = distinct >= 0.9 * len(jobs[n])
        ok = not bad and not dup and m4 and m5   # M3 chỉ cảnh báo: tên Việt/Hoa không xuất hiện trong prompt tiếng Anh
        fail += not ok
        print(f"Tập {n:02d}: {'ĐẠT ' if ok else 'TRƯỢT'} · M1 mã sai {len(bad)}/{len(jobs[n])}"
              f" · M2 trùng {dup or '—'} · M5 câu chưa phủ {len(miss)}/{len(codes)} · M4 prompt riêng {distinct}/{len(jobs[n])}{'' if m4 else ' MẪU CHUNG'}"
              f" · M3(cảnh báo) tên {names or '?'} có trong job: {named or 'KHÔNG'}")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
