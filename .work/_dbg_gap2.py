import re
from pathlib import Path
DOC=Path("02_SAN_XUAT/Danh_Sach_SFX_Tap03-29.md")
lines=DOC.read_text(encoding="utf-8").splitlines()
i0=next(i for i,l in enumerate(lines) if l.startswith("### 5.2"))
i1=next(i for i,l in enumerate(lines) if i>i0 and l.startswith("## 6."))
print("i0,i1 =", i0, i1)
CODE_RE=re.compile(r"`([a-z0-9_]+\.wav)`")
n_rows=0; n_codes=0
for line in lines[i0:i1]:
    if not line.startswith("|"): continue
    cols=[c.strip() for c in line.strip().strip("|").split("|")]
    if len(cols)<3: continue
    if not cols[0].isdigit(): continue
    n_rows+=1
    last=cols[-1]
    codes=CODE_RE.findall(last)
    n_codes+=len(codes)
    if codes: print(f"  tap {cols[0]}: {codes}")
print("rows:", n_rows, "codes found:", n_codes)
