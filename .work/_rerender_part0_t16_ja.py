import sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import build_video3 as B
f1 = math.ceil(int(B.TOTAL * B.FPS) / 3)
vd = B.ED.w("video3")
print("render part_00 frames 0 ->", f1, flush=True)
print("code", B.work((0, f1, vd / "part_00.mp4")))
