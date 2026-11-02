import sys, os, time
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
os.environ["AE_EP"]="03"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import numpy as np
from PIL import Image
import build_video3 as B
from pathlib import Path
P = Path(r"D:\TEST\Gax\amber-eyes\.work\video3_t03\stills")
for sid in ("2-13","3-05","1-13"):
    s = [x for x in B.SH if x["id"]==sid][0]
    t = (s["start"]+s["end"])/2
    fi = int(t*B.FPS)
    new = B.render(fi).convert("RGB")
    old = Image.open(P/f"shot_{sid}.png").convert("RGB")
    a = np.asarray(new).astype(np.int16); b = np.asarray(old).astype(np.int16)
    d = np.abs(a-b)
    print(f"  {sid}: max|sai lech|={d.max()}  px khac={int((d.max(axis=2)>0).sum())} / {d.shape[0]*d.shape[1]}")
t0=time.perf_counter()
s = B.SH[40]; fi = int(((s["start"]+s["end"])/2)*B.FPS)
for _ in range(5): B.render(fi)
dt=(time.perf_counter()-t0)/5
print(f"  render(): {dt*1000:.1f} ms -> {1/dt:.1f} fps (co tai build chay)")
