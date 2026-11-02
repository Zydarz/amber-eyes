import sys, json, pathlib
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
import os
os.environ["AE_EP"] = "03"
import edition as ED
print("PLAN:", ED.PLAN)
print("EP keys:", list(ED.EP.keys()))
for k in ("combo","inset","bg2","cast"):
    v = ED.EP.get(k)
    print(k, "->", type(v).__name__, (len(v) if hasattr(v,'__len__') else v))
print("w() ->", ED.w("timeline_s.json"))
print("EP sub-dict sample:", json.dumps({k:v for k,v in list(ED.EP.items())[:12] if k not in ('combo','inset','bg2')}, ensure_ascii=False, default=str)[:1200])
