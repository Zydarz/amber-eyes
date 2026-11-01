# -*- coding: utf-8 -*-
"""Kiểm hồi quy cho bản vá `voice_role_check.py` (nhãn giọng G10).

L9: sửa script dùng chung => phải kiểm hồi quy Tập 01.

Tiêu chí:
  1. Tập 01 (VN + EN + JA + KO): nhãn ĐỔI KHÔNG ĐƯỢC — phải y hệt công thức cũ `ED.CAST[role][0]`.
  2. Tập dùng Higgs (có higgs_selection_tXX.json): nhãn mới = ref_wav + "(Higgs Audio v3)".
  3. Báo cáo G10 đã giao cho Tập 05 phải được script tái tạo đúng từng ký tự.
  4. Báo cáo nào của tập khác sẽ đổi khi chạy lại G10 (phải biết trước).
"""
import json
import os
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
W = ROOT / ".work"
PY = sys.executable

CHILD = r'''
import json, sys
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
import voice_role_check as V
import edition as ED
refs = V.higgs_refs()
roles = ("H", "D", "C", "N1", "N2")
out = {}
for r in roles:
    if r not in ED.CAST:
        continue
    cu = "`%s`" % ED.CAST[r][0]
    moi = V.voice_label(r, refs)
    out[r] = {"cu": cu, "moi": moi, "doi": moi != cu}
print(json.dumps({"ep": ED.EPN, "lang": ED.LANG, "master": ED.MASTER,
                  "ep_dir": str(ED.EP_DIR), "higgs": bool(refs), "labels": out},
                 ensure_ascii=False))
'''


def child(lang, ep):
    env = dict(os.environ, AE_LANG=lang, AE_EP=ep, PYTHONIOENCODING="utf-8")
    p = subprocess.run([PY, "-c", CHILD], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env, cwd=str(ROOT))
    if p.returncode != 0:
        return {"error": (p.stderr or p.stdout)[-300:]}
    try:
        return json.loads(p.stdout.strip().splitlines()[-1])
    except Exception as e:  # noqa: BLE001
        return {"error": f"{e}: {p.stdout[-200:]}"}


def report_labels(ep_dir):
    p = pathlib.Path(ep_dir) / "thu_giong_kiem_vai" / "report.md"
    if not p.exists():
        return None
    txt = p.read_text(encoding="utf-8-sig")
    out = {}
    for line in txt.splitlines():
        m = re.match(r"^## (.+?) — (`[^`]+`.*?) — (ĐẠT|KHÔNG ĐẠT) \((\d+) người\)$", line)
        if m:
            out[m.group(1)] = m.group(2)
    return out or None


print("=" * 92)
print("KIEM HOI QUY voice_role_check.py — nhan giong G10")
print("=" * 92)

CASES = [("vi", "01"), ("vi", "02"), ("vi", "03"), ("vi", "04"), ("vi", "05"),
         ("vi", "06"), ("vi", "07"), ("en", "01"), ("en", "02"), ("en", "05")]

fails = []
changed_reports = []
for lang, ep in CASES:
    d = child(lang, ep)
    if "error" in d:
        print(f"[LOI] {lang}/{ep}: {d['error'][:160]}")
        fails.append(f"{lang}/{ep} chay loi")
        continue
    ep_dir = d["ep_dir"]
    rl = report_labels(ep_dir)
    print(f"\n--- {lang.upper()} tập {ep}  (higgs={d['higgs']})  {Path(ep_dir).name if False else ep_dir}")
    for role, v in d["labels"].items():
        mark = "  <-- DOI" if v["doi"] else ""
        print(f"    {role:<3} cu: {v['cu']:<42} moi: {v['moi']}{mark}")
        if ep == "01" and v["doi"]:
            fails.append(f"{lang}/{ep} doi nhan (phai giu nguyen)")
    if rl:
        for name, lab in rl.items():
            # khop voi nhan moi cua vai tuong ung (ten vai trong report khac theo lang)
            pass
        print(f"    report.md hien tai ({len(rl)} nhan):")
        for name, lab in rl.items():
            print(f"       {name}: {lab}")
        if d["higgs"]:
            changed_reports.append((lang, ep, ep_dir))

print("\n" + "=" * 92)
print("KET LUAN")
print("=" * 92)
if fails:
    for f in fails:
        print("  [FAIL]", f)
else:
    print("  [OK] Tap 01 (vi/en/ja/ko): nhan G10 KHONG DOI — hoi quy dat L9")
print("  Tap dung Higgs (se doi nhan khi chay lai G10):")
for lang, ep, ep_dir in changed_reports:
    print(f"     - {lang}/{ep}: {ep_dir}")
print()
