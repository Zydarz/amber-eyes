# Re-render one worker part of picture.mp4 (after a shots.json fix) and re-concat.
import sys, subprocess, math
from multiprocessing import Pool
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import build_video3 as bv

if __name__ == "__main__":
    k = int(sys.argv[1]); n = 6
    total_f = int(bv.TOTAL * bv.FPS)
    step = math.ceil(total_f / n)
    f0, f1 = k * step, min(total_f, (k + 1) * step)
    vd = bv.ED.w("video3")
    sub = math.ceil((f1 - f0) / 6)
    jobs = [(f0 + i * sub, min(f1, f0 + (i + 1) * sub), vd / f"fix{k}_{i}.mp4") for i in range(6)]
    with Pool(6) as p:
        assert not any(p.map(bv.work, jobs))
    lst = vd / f"fix{k}.txt"
    lst.write_text("".join(f"file '{j[2].as_posix()}'\n" for j in jobs))
    subprocess.run([str(bv.FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", str(vd / f"part_{k:02d}.mp4")], check=True)
    parts = vd / "parts.txt"
    subprocess.run([str(bv.FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(parts),
                    "-c", "copy", str(vd / "picture.mp4")], check=True)
    print("part", k, "frames", f0, f1, "re-rendered; picture.mp4 rebuilt")
