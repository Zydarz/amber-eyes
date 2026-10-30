#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra suc khoe dich vu: sinh 1 anh thu nghiem voi prompt don gian."""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
WORK = Path(__file__).resolve().parents[1] / ".work"
LOG = WORK / "gen_log"
TOOL = "connector__matrix__generate_image"

STYLE = ("Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink "
         "linework, deep chiaroscuro lighting, subtle mist and film grain, desaturated muted "
         "palette, ominous quiet tension, highly detailed. ")
NEG = (" Strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, "
       "no watermark, no frame, no letterbox bars, full-bleed image.")

PROMPT = STYLE + "A plain empty wooden crate sitting on a bare metal shelf in a dim storeroom, one cold shaft of light, deep shadow, nobody present." + NEG

req = {"prompt": PROMPT, "aspect_ratio": "16:9", "resolution": "2K", "output_file": "healthcheck_tmp"}
af = LOG / "probe_health.json"
af.write_text(json.dumps({"requests": [req]}, ensure_ascii=False), encoding="utf-8")
try:
    r = subprocess.run(["cmd", "/c", "mcode-tools", "connector", "call", TOOL,
                        "--args-file", str(af)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=420)
except subprocess.TimeoutExpired:
    print("TIMEOUT — dich vu treo")
    sys.exit(2)
if r.returncode != 0:
    print(f"rc={r.returncode}: {r.stderr[:300]}")
    sys.exit(2)
rj = json.loads(r.stdout)
if rj.get("success_items"):
    print("DICH VU OK — prompt don gian sinh duoc:", rj["success_items"][0]["file_name"])
    sys.exit(0)
print("DICH VU LO — ca prompt don gian cung fail:")
print("  ", rj.get("message", "")[:300])
sys.exit(2)
