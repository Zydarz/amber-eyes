import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

txt = Path(".work/package.py").read_text(encoding='utf-8')
pos_ja = txt.find("def description_ja")
print(txt[pos_ja:pos_ja+2000])
