import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

txt = Path(".work/package.py").read_text(encoding='utf-8')
pos_en = txt.find("def description_en")
print(txt[pos_en:pos_en+4000])
