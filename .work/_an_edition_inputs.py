#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sánh các đầu vào RENDER của Tap03: HEAD vs bản hiện tại (edition.py)."""
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"

src = subprocess.run(["git", "show", "HEAD:.work/edition.py"], cwd=ROOT, capture_output=True).stdout.decode("utf-8")
tmp = Path(tempfile.gettempdir()) / "_edition_old.py"
tmp.write_text(src, encoding="utf-8")

import os
os.environ["AE_EP"] = "03"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


OLD = load(tmp, "ed_old")
NEW = load(WORK / "edition.py", "ed_new")

FIELDS = ["title", "act_titles", "n1", "n2", "roles_en", "sub_tags_en", "thumb", "thumb_bg"]
for f in FIELDS:
    a = OLD.EP.get(f)
    b = NEW.EP.get(f)
    if json.dumps(a, ensure_ascii=False, sort_keys=True) != json.dumps(b, ensure_ascii=False, sort_keys=True):
        print(f"### EP['{f}'] ĐỔI:")
        print(f"  CŨ : {str(a)[:260]}")
        print(f"  MỚI: {str(b)[:260]}")
    else:
        print(f"    EP['{f}'] không đổi")

for label, mod in (("CŨ ", OLD), ("MỚI", NEW)):
    print(f"{label} ROLE_NAME = {json.dumps(mod.ROLE_NAME, ensure_ascii=False)}")
    print(f"{label} SUB_TAG  = {json.dumps(getattr(mod, 'SUB_TAG', None), ensure_ascii=False)}")
    print(f"{label} UI       = {json.dumps(mod.UI, ensure_ascii=False)}")
