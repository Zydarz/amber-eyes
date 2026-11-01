# -*- coding: utf-8 -*-
"""Sửa nhãn giọng G10 trong report.md cho các tập đã chạy Higgs
(dùng ĐÚNG logic của voice_role_check.py sau bản vá, không tự chế).

Chỉ đổi phần nhãn giọng trên dòng "## <vai> — <nhãn> — ĐẠT/KHÔNG ĐẠT (n người)";
không đụng nội dung câu hỏi, kết luận hay đánh giá của người nghe.
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

CHILD = r'''
import json, sys
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
import voice_role_check as V
import edition as ED
refs = V.higgs_refs()
roles = [r for r in ("H", "D", "C", "N1", "N2") if r in ED.CAST and r in refs]
print(json.dumps({"ep_dir": str(ED.EP_DIR), "ep": ED.EPN, "lang": ED.LANG,
                  "labels": {r: V.voice_label(r, refs) for r in roles}}, ensure_ascii=False))
'''

TARGETS = [("vi", "04"), ("en", "02")]

for lang, ep in TARGETS:
    env = dict(os.environ, AE_LANG=lang, AE_EP=ep, PYTHONIOENCODING="utf-8")
    p = subprocess.run([sys.executable, "-c", CHILD], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env, cwd=str(ROOT))
    d = json.loads(p.stdout.strip().splitlines()[-1])
    labels = list(d["labels"].values())
    rp = pathlib.Path(d["ep_dir"]) / "thu_giong_kiem_vai" / "report.md"
    txt = rp.read_text(encoding="utf-8-sig")
    lines = txt.splitlines()
    out, idx, changed = [], 0, 0
    for line in lines:
        m = re.match(r"^(## .+? — )(.+?)( — (?:ĐẠT|KHÔNG ĐẠT) \(\d+ người\))$", line)
        if m and idx < len(labels):
            new = m.group(1) + labels[idx] + m.group(3)
            out.append(new)
            if new != line:
                changed += 1
            idx += 1
        else:
            out.append(line)
    rp.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"[{lang}/{ep}] {rp} — sua {changed}/{idx} dong nhan")
    for line in out:
        if line.startswith("## "):
            print("   ", line)
