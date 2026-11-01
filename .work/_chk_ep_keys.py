import sys, pathlib
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes")
import edition as ED
print("EPISODES keys:", list(ED.EPISODES.keys()))
for ep in ("02", "03", "04"):
    d = ED.EPISODES.get(ep) or {}
    print("EP%s keys: %s" % (ep, sorted(d.keys())))
print()
print("EP (active) keys:", sorted(ED.EP.keys()))
