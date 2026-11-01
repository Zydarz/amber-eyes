"""Gop output VONG 2 (§7) vao thu muc san xuat de do CER + chon ban chung.

Input : .work/kaggle_higgs/out_higgs_r2/**/higgs_manifest.json + wav
        .work/kaggle_higgs/out_higgs_prod/out_higgs_prod/higgs_manifest.json
Output: wav vong 2 chep vao thu muc san xuat; manifest san xuat them dong vong 2 (key moi, khong ghi de)
        sao luu manifest cu: higgs_manifest.before_r2.json (L5)

Sau do: measure_cer_prod.py --rounds 2 (cache -> chi do file moi) -> finish_prod.py

Usage: python .work/merge_r2.py
"""
import json
import os
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
# Tap (L8) + ngon ngu (AE_LANG=en): file rieng; Tap 02 VN giu ten cu (hoi quy L9).
sys.path.insert(0, str(HERE))
import higgs_paths as P  # noqa: E402
EPN = P.EPN
PROD = P.PROD_EP / P.PROD_EP.name
R2 = P.R2

man_p = PROD / "higgs_manifest.json"
bak = PROD / "higgs_manifest.before_r2.json"
if not bak.exists():
    shutil.copy2(man_p, bak)
base = json.loads(bak.read_text(encoding="utf-8-sig"))          # luon gop tu ban truoc vong 2
r2_man = next(R2.rglob("higgs_manifest.json"))
r2 = [r for r in json.loads(r2_man.read_text(encoding="utf-8-sig")) if r.get("ok")]

keys = {r["key"] for r in base}
files = {r["file"] for r in base}
add = []
for r in r2:
    if r["key"] in keys or r["file"] in files:
        raise SystemExit("!! trung key/file voi luot 1: %s" % r["file"])
    shutil.copy2(r2_man.parent / r["file"], PROD / r["file"])
    add.append(dict(r, round=2))
man_p.write_text(json.dumps(base + add, ensure_ascii=False, indent=1), encoding="utf-8")
print("luot 1: %d dong | vong 2 them: %d | tong: %d" % (len(base), len(add), len(base) + len(add)))
print("sao luu manifest truoc vong 2:", bak)
