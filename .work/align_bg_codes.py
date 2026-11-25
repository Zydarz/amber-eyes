#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Căn chỉnh job↔câu theo NGHĨA, đơn điệu theo thứ tự job (quy hoạch động).
Mỗi hồi: job i nhận cụm 1..MAXG câu liền kề; tối đa hoá tổng điểm khớp từ khoá
(IDF, trên desc+tên job) trừ phạt lệch khỏi vị trí tỉ lệ và lệch cỡ cụm lý tưởng.
Dùng: py -3 .work/align_bg_codes.py XX [--write] [--act A]
Nguồn job: bản gốc trong .work/_cu/bg_jobs_remap_20261124/ nếu có (không phụ thuộc lượt remap trước)."""
import sys, json, re, math, shutil, collections, unicodedata
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
import importlib.util
W = Path(__file__).parent
spec = importlib.util.spec_from_file_location("q", W / "qc_bg_mapping.py"); q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
MAXG, LAM_POS, LAM_SZ = 4, 0.6, 0.35

def toks(s):
    s = unicodedata.normalize("NFC", s.lower())
    return set(w for w in re.findall(r"\w{4,}", s))

def align(sents, jobs):
    """Neo theo nghĩa (không ép tuần tự): mỗi job tìm cửa sổ 1-3 câu khớp từ khoá nhất;
    job không có tín hiệu nội suy giữa hai job có neo kề (theo thứ tự danh sách);
    sắp theo neo, rải đều neo trùng, rồi mỗi câu thuộc job có neo gần nhất."""
    n, k = len(sents), len(jobs)
    df = collections.Counter(w for s in sents for w in s["t"])
    idf = {w: math.log((n + 1) / (c + 0.5)) for w, c in df.items()}
    jt = [toks(re.sub(r"^Hồi \d+ Tập \d+ \([^)]*\):", "", j.get("desc", "")) + " " + j["name"].replace("_", " ")) for j in jobs]
    anc = [None] * k; strong = [0.0] * k
    for i in range(k):
        bs, bc = 0.0, None
        for p in range(n):
            for g in (1, 2, 3):
                if p + g > n: break
                ws = set().union(*[sents[x]["t"] for x in range(p, p + g)])
                sc = sum(idf.get(w, 0) for w in jt[i] & ws) / g ** 0.5
                if sc > bs + 1e-9: bs, bc = sc, p + (g - 1) / 2
        if bs >= 2.5: anc[i], strong[i] = bc, bs
    known = [i for i in range(k) if anc[i] is not None]
    for i in range(k):
        if anc[i] is None:
            l = max([x for x in known if x < i], default=None); r = min([x for x in known if x > i], default=None)
            lv = anc[l] if l is not None else 0; rv = anc[r] if r is not None else n - 1
            li = l if l is not None else -1; ri = r if r is not None else k
            anc[i] = lv + (rv - lv) * (i - li) / (ri - li)
    order = sorted(range(k), key=lambda i: (anc[i], i))
    gap = max((n - 1) / max(k, 1), 1) * 0.5
    pos = []
    for j, i in enumerate(order):
        a0 = anc[i] if not pos else max(anc[i], pos[-1] + gap * 0.6)
        pos.append(min(a0, n - 1))
    assign = {}  # job index -> list of sentence idx
    for i in range(k): assign[i] = []
    for x in range(n):
        d = min(range(k), key=lambda j: abs(pos[j] - x))
        assign[order[d]].append(x)
    out = []
    for i in range(k):
        xs = assign[i]
        if not xs:
            c = min(n - 1, max(0, int(round(pos[order.index(i)]))))
            xs = [c]
        out.append((min(xs), max(xs) + 1))
    return out

def run(n, write, only):
    els = q.pk.parse_file(q.script_file(n))
    acts = collections.defaultdict(list)
    for e in els:
        for s in e.get("sentences") or []:
            acts[e["act"]].append({"id": s["id"], "t": toks(s["text"]), "txt": s["text"]})
    cur = W / f"bg_jobs_tap{n:02d}.json"
    bk = W / "_cu" / "bg_jobs_remap_20261124"; src = bk / cur.name if (bk / cur.name).exists() else cur
    jobs = json.load(open(src, encoding="utf-8"))
    for a in sorted(set(j["act"] for j in jobs)):
        if only and a != only: continue
        js = [j for j in jobs if j["act"] == a]; ss = acts[a]
        for j, (x, y) in zip(js, align(ss, js)):
            j["sentences"] = ",".join(s["id"] for s in ss[x:y])
            if only: print(j["name"].split("_", 2)[2][:42].ljust(42), f"s{x+1}-{y}", "|", ss[x]["txt"][:60])
    if write:
        bk.mkdir(parents=True, exist_ok=True)
        if not (bk / cur.name).exists(): shutil.copy2(cur, bk / cur.name)
        with open(cur, "w", encoding="utf-8", newline="") as f:
            json.dump(jobs, f, ensure_ascii=False, indent=2); f.write("\n")
        print("đã ghi", cur.name)

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if x.isdigit()]
    only = int(sys.argv[sys.argv.index("--act") + 1]) if "--act" in sys.argv else None
    run(int(a[0]), "--write" in sys.argv, only)
