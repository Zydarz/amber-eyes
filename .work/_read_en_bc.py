import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path("90_LUU_TRU/BaoCao_QC_Tap02_EN_MasterVideo_20261105.md")
if p.exists():
    print(p.read_text(encoding="utf-8")[:1500])
