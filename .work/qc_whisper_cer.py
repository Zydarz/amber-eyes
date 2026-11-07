"""Tinh CER + tong hop UTMOS tu qc.json cua kernel QC Kaggle (build_qc_nb.py).

  AE_EP=06 py -3 .work/qc_whisper_cer.py --qc <qc.json> [--qc <qc_r2.json>]

Van ban goc lay tu higgs_manifest.json cua cac lan sinh (prod + r2 neu co). CER = vi_cer.cer_pair
(chuan hoa ca hai ve, Q3a) — cung bo chuan hoa voi measure_cer_prod.py. Whisper la ASR KHAC
listen_audio => KHONG tron so lieu hai ASR; ghi ro nguon trong bao cao.
Ghi: .work/qc_whisper_rows_<TAG>.json + .work/qc_whisper_report_<TAG>.md
"""
import argparse
import json
import pathlib
import statistics as st
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import higgs_paths as P  # noqa: E402
# Chuan hoa theo ngon ngu (cung cach measure_cer_prod.py). Truoc 06/11/2026 luon dung vi_cer
# => ban EN/JA ra CER gia (Tap06 JA: 161/212 cau "> 2%").
if P.EN:
    import en_cer as vi_cer  # noqa: E402
elif P.JA:
    import ja_cer as vi_cer  # noqa: E402
else:
    import vi_cer  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--qc", action="append", required=True)
ap.add_argument("--max-cer", type=float, default=0.02)
a = ap.parse_args()

text, meta = {}, {}
for d in (P.PROD, P.R2):
    for m in sorted(pathlib.Path(d).rglob("higgs_manifest.json")) if pathlib.Path(d).exists() else []:
        for r in json.loads(m.read_text(encoding="utf-8-sig")):
            if r.get("ok"):
                text[r["file"]] = r.get("text_plain") or r.get("text_sent") or ""
                meta[r["file"]] = r

rows, missing = [], []
for q in a.qc:
    for r in json.loads(pathlib.Path(q).read_text(encoding="utf-8"))["rows"]:
        if r["file"] not in text:
            missing.append(r["file"])
            continue
        m = meta[r["file"]]
        h = r["transcription"]
        rows.append({**r, "id": m["id"], "role": m["role"], "ref_wav": m["ref_wav"],
                     "cer": vi_cer.cer_pair(text[r["file"]], h) if h else None,
                     "cer_prop": vi_cer.cer_pair_prop(text[r["file"]], h) if h else None})
if missing:
    print("CANH BAO: %d file trong qc.json khong co trong manifest: %s" % (len(missing), missing[:3]))
n_ok = sum(r["cer"] is not None for r in rows)
if n_ok < 0.5 * max(1, len(rows)):  # cung chot chan nhu measure_cer_prod.py (L3)
    raise SystemExit("LOI: chi %d/%d file co ban chep => KHONG ghi bao cao" % (n_ok, len(rows)))

by_id = defaultdict(list)
for r in rows:
    by_id[r["id"]].append(r)
by_role = defaultdict(list)
for r in rows:
    by_role[r["role"]].append(r)

md = ["# QC Whisper + UTMOS — %s" % P.EP_TAG, "",
      "ASR: `openai/whisper-large-v3` (greedy, Kaggle GPU) · CER = `vi_cer.cer_pair` (Q3a). "
      "MOS: `utmos22_strong` — mô hình tiếng Anh, **chỉ so tương đối** giữa các bản/vai.", "",
      "| Vai | n | CER tb | CER max | file > %.0f%% | UTMOS tb | UTMOS min |" % (100 * a.max_cer),
      "|---|---:|---:|---:|---:|---:|---:|"]
for role, v in sorted(by_role.items()):
    c = [r["cer"] for r in v if r["cer"] is not None]
    u = [r["utmos"] for r in v]
    md.append("| %s | %d | %.2f%% | %.1f%% | %d | %.2f | %.2f |" % (
        role, len(v), 100 * st.mean(c), 100 * max(c), sum(x > a.max_cer for x in c), st.mean(u), min(u)))
fail = sorted(sid for sid, v in by_id.items()
              if min((r["cer"] for r in v if r["cer"] is not None), default=9) > a.max_cer)
md += ["", "## Câu mà MỌI bản đều > %.0f%% (%d/%d câu)" % (100 * a.max_cer, len(fail), len(by_id)), "",
       "| Câu | Vai | CER tốt nhất | CER bỏ tên riêng | UTMOS | Bản chép (bản tốt nhất) |", "|---|---|---:|---:|---:|---|"]
for sid in fail:
    b = min(by_id[sid], key=lambda r: r["cer"] if r["cer"] is not None else 9)
    md.append("| %s | %s | %.1f%% | %.1f%% | %.2f | %s |" % (
        sid, b["role"], 100 * b["cer"], 100 * (b["cer_prop"] or 0), b["utmos"], b["transcription"][:120]))
low = sorted(rows, key=lambda r: r["utmos"])[:10]
md += ["", "## 10 file UTMOS thấp nhất (nghe kiểm tạp âm / méo)", "", "| File | Vai | UTMOS | CER |", "|---|---|---:|---:|"]
md += ["| %s | %s | %.2f | %s |" % (r["file"], r["role"], r["utmos"],
                                   "-" if r["cer"] is None else "%.1f%%" % (100 * r["cer"])) for r in low]

out_rows = HERE / ("qc_whisper_rows_%s.json" % P.EP_TAG)
out_md = HERE / ("qc_whisper_report_%s.md" % P.EP_TAG)
out_rows.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
out_md.write_text("\n".join(md) + "\n", encoding="utf-8")
print("\n".join(md[:12 + len(by_role)]))
print("->", out_md)
