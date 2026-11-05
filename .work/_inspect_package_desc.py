import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

txt = Path(".work/package.py").read_text(encoding='utf-8')
import re
pos = txt.find("def description")
if pos != -1:
    print(txt[pos:pos+2500])
else:
    print("def description not found, searching for mo_ta...")
    pos2 = txt.find("mo_ta")
    print(txt[pos2:pos2+2000])
