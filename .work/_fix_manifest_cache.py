# -*- coding: utf-8 -*-
"""Khop manifest EN 5 entry (giu TK1/TK3/TK4/TK5 cu, thay TK2 bang ban moi) + khoi phuc cache JA TK3.

Ly do:
- Render chi TK2 nen manifest bi ghi de con 1 entry => phai ghep lai 5.
- Cache ASR JA TK3 da refresh khi kiem chung, nhung timeline JA TK3 KHONG duoc viet lai
  (khong render lai clip JA) => ton tai mau thuan cache/timeline. Khoi phuc cache tu HEAD
  de clip JA da xuat ban giu dung mo hinh cua ban giao.
"""
import json
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")

# ---- 1. manifest EN: ghep 5 entry ----
MP = ROOT / ".work" / "_tk_notext_manifest_EN_t04.json"
cur = json.loads(MP.read_text(encoding="utf-8"))
head = json.loads(subprocess.check_output(
    ["git", "show", "HEAD:.work/_tk_notext_manifest_EN_t04.json"]).decode("utf-8"))
tk2 = next(e for e in cur if e["clip"] == "TK2")
merged = []
for e in head:
    merged.append(tk2 if e["clip"] == "TK2" else e)
MP.write_text(json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
print("manifest EN:", len(merged), "entry ->",
      ", ".join(f"{e['clip']}={e['audio_s']:.2f}s" for e in merged))

# ---- 2. khoi phuc cache ASR JA TK3 tu HEAD ----
JC = ".work/_tk_asr_tk04_TK3_JA.json"
old = subprocess.check_output(["git", "show", f"HEAD:{JC}"])
(ROOT / JC).write_bytes(old)
d = json.loads((ROOT / JC).read_text(encoding="utf-8"))
print("cache JA TK3 da khoi phuc: dur", d["duration"], "words", len(d["words"]))
