import sys, os
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
os.environ["AE_EP"]="03"
import edition as ED
print("OUT_DIR:", ED.OUT_DIR)
print("MASTER:", ED.MASTER, "| SRT:", ED.SRT)
for n in ("audio_master.wav","shots.json","video3","timeline_s.json","qc_final"):
    print(n, "->", ED.w(n))
