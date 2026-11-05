# -*- coding: utf-8 -*-
import sys, os
os.environ["AE_EP"] = "06"
os.environ["AE_LANG"] = "en"
sys.path.insert(0, ".work")
import edition as ED

print("LANG:", getattr(ED, "LANG", None))
print("PLAN:", getattr(ED, "PLAN", None))
print("TL:", ED.w("timeline_s.json"))
print("SHOTS:", ED.w("shots.json"))
print("SCRIPT:", getattr(ED, "SCRIPT", None))
