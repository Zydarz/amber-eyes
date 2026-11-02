import sys, os
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
os.environ["AE_EP"]="03"
import edition as ED
print("mux_af  =", repr(ED.EP.get("mux_af", "<mac dinh>")))
print("MASTER  =", ED.MASTER, "| SRT:", ED.SRT)
print("thumb   =", ED.EP.get("thumb"))
print("thumb_bg=", ED.EP.get("thumb_bg"))
print("act_titles:", ED.EP.get("act_titles"))
print("SUB_TAG:", ED.SUB_TAG)
