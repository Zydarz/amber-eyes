import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(r"D:\TEST\Gax\Audi\.work")

en_table = json.load(open(W / "shots_text_tap02_EN.json", encoding="utf-8"))
shots_analysis = json.load(open(W / "_shots_analysis.json", encoding="utf-8"))

# Check task-1140 completion
print(f"Loaded {len(en_table)} shots from EN table")
