"""Verify sau khi sua ROOT: import cac script pipeline va kiem tra ROOT tro dung."""
import importlib.util
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")

ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
NAMES = ("build_audio3", "build_video3", "tts_sentences", "subtitles", "package",
         "parse_shots", "edition", "voice_audition", "voice_role_check",
         "make_acting_tap02", "make_sfx3", "qc_asr")

ok = fail = 0
for name in NAMES:
    p = ROOT / ".work" / f"{name}.py"
    if not p.exists():
        print(f"  {name:20} THIEU")
        fail += 1
        continue
    try:
        spec = importlib.util.spec_from_file_location(name, str(p))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        r = getattr(m, "ROOT", None)
        good = (r is None) or (pathlib.Path(r).resolve() == ROOT)
        print(f"  {name:20} {'OK  ' if good else 'SAI '} ROOT={r}")
        ok += 1 if good else 0
        fail += 0 if good else 1
    except Exception as e:
        print(f"  {name:20} FAIL {type(e).__name__}: {str(e)[:90]}")
        fail += 1

print(f"\nOK={ok} FAIL={fail}")
print("ROOT mong doi:", ROOT)
