import sys, json
from pathlib import Path
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
import voxcpm_do_mau as M
M.F0_TARGET.update({"D_NEW": (82, 95), "C_NEW": (200, 218), "H": (100, 115)})
use_asr = "--asr" in sys.argv
D = M.ROOT / "assets" / "voice_ref_voxcpm2_dc"
refs = json.loads((D / "refs.json").read_text(encoding="utf-8"))
rows = []
KEEP = set(a for a in sys.argv[2:] if not a.startswith("--"))
for name, meta in refs.items():
    if KEEP and name not in KEEP: continue
    p = D / f"{name}.wav"
    r = M.measure(meta["role"], p, meta["target_text"], use_asr, final=True)
    r["name"] = name; r["mac_f0"] = meta["f0_median_hz"]; rows.append(r)
out = Path(sys.argv[1]); out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{'take':28} {'F0':>6} {'mac':>6} {'tieng':>5} {'gap':>5} {'am/s':>5} {'LUFS':>6} {'TP':>5} {'spr':>4} {'CER':>6}  loi")
for r in rows:
    cer = "-" if r["cer"] is None else f"{100*r['cer']:.1f}%"
    f = [x for x in r["fails"] if not x.startswith("V3 chưa")]
    print(f"{r['name']:28} {r['f0']:6.1f} {r['mac_f0']:6.1f} {r['speech_s']:5.1f} {r['max_gap_s']:5.2f} {r['syl_per_s']:5.2f} "
          f"{r['lufs']:6.1f} {r['true_peak']:5.1f} {r['f0_spread_nc']:4.1f} {cer:>6}  {'; '.join(f+r['warns']) or 'OK'}"
          + (f"  tone={r['tone_errors']}" if r['tone_errors'] else ""))
