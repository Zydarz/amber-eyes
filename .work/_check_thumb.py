import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import edition as ED
ep = ED.EPISODES["05"]
print("thumb:", ep.get("thumb"))
print("thumb_bg:", ep.get("thumb_bg"))
