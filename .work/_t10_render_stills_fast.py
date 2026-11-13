#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render stills cho Tập 10 song song bằng multiprocessing để đạt hiệu năng cao."""
import os
import sys
import json
import time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"

def render_one_shot(args):
    shot_id, ep, lang = args
    import os
    import sys
    from pathlib import Path
    
    os.environ["AE_EP"] = str(ep)
    if lang:
        os.environ["AE_LANG"] = str(lang)
    elif "AE_LANG" in os.environ:
        del os.environ["AE_LANG"]
        
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / ".work"))
    import edition as ED
    import build_video3 as BV
    
    vd = ED.w("video3")
    sd = vd / "stills"
    sd.mkdir(parents=True, exist_ok=True)
    
    by_id = {s["id"]: s for s in BV.SH}
    if shot_id not in by_id:
        return shot_id, False, "not in SH"
        
    s = by_id[shot_id]
    t_sec = 0.5 * (s["start"] + s["end"])
    fi = int(t_sec * BV.FPS)
    name = f"shot_{s['id']}.png"
    out_path = sd / name
    
    try:
        BV.render(fi).convert("RGB").save(out_path)
        return shot_id, True, str(out_path)
    except Exception as e:
        return shot_id, False, str(e)

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--ep", default="10")
    ap.add_argument("--lang", default="")
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()
    
    os.environ["AE_EP"] = args.ep
    if args.lang:
        os.environ["AE_LANG"] = args.lang
    elif "AE_LANG" in os.environ:
        del os.environ["AE_LANG"]
        
    import edition as ED
    shots_p = ED.w("shots.json")
    shots = json.loads(shots_p.read_text(encoding="utf-8"))["shots"]
    shot_ids = [s["id"] for s in shots]
    
    print(f"[{args.lang or 'vi'}] Rendering {len(shot_ids)} stills for Ep {args.ep} using {args.workers} workers...")
    t0 = time.time()
    
    pool_args = [(sid, args.ep, args.lang) for sid in shot_ids]
    
    success = 0
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        for sid, ok, msg in executor.map(render_one_shot, pool_args):
            if ok:
                success += 1
            else:
                print(f"  FAILED: {sid} -> {msg}")
                
    elapsed = time.time() - t0
    print(f"[{args.lang or 'vi'}] Done: {success}/{len(shot_ids)} stills in {elapsed:.1f}s ({elapsed/len(shot_ids):.2f}s/shot)")

if __name__ == "__main__":
    main()
