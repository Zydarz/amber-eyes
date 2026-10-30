import shutil, sys
from pathlib import Path
INBOX = Path(__file__).resolve().parents[1] / "02_SAN_XUAT" / "sfx_youtube"
CONF = INBOX / "_conflict"
a, b = sys.argv[1], sys.argv[2]
CONF.mkdir(parents=True, exist_ok=True)
pa, pb = INBOX / (a + ".mp3"), INBOX / (b + ".mp3")
if not pa.exists() or not pb.exists():
    sys.exit(f"thieu file: {pa.exists()} {pb.exists()}")
ta, tb = CONF / (a + "_tmp.mp3"), CONF / (b + "_tmp.mp3")
shutil.move(str(pa), str(ta)); shutil.move(str(pb), str(tb))
shutil.move(str(ta), str(pb)); shutil.move(str(tb), str(pa))
print(f"swapped {a} <-> {b}")
for m in (a, b):
    print("  ", m, (INBOX / (m + ".mp3")).stat().st_size)