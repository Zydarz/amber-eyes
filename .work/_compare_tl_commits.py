import subprocess
import json

cmd = ["git", "show", "7970dbea~1:.work/timeline_s_JA_t02.json"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
tl_old = json.loads(res.stdout)
print("Old timeline total:", tl_old.get("total"))
print("Old timeline intro:", tl_old.get("intro"))
print("Old timeline items count:", len(tl_old.get("items", [])))

cmd2 = ["git", "show", "HEAD:.work/timeline_s_JA_t02.json"]
res2 = subprocess.run(cmd2, capture_output=True, text=True, encoding="utf-8")
tl_head = json.loads(res2.stdout)
print("HEAD timeline total:", tl_head.get("total"))
print("HEAD timeline intro:", tl_head.get("intro"))
print("HEAD timeline items count:", len(tl_head.get("items", [])))

cmd3 = ["git", "show", "7970dbea~1:.work/shots_JA_t02.json"]
res3 = subprocess.run(cmd3, capture_output=True, text=True, encoding="utf-8")
shots_old = json.loads(res3.stdout)
print("Old shots total:", shots_old.get("total") if isinstance(shots_old, dict) else len(shots_old))
if isinstance(shots_old, dict):
    print("Old shots count:", len(shots_old.get("shots", [])))
