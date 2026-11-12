import io, json, os, re
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sh = json.loads((ROOT/".work/shots_t07.json").read_text(encoding="utf-8"))["shots"]
multi = [s for s in sh if len(s["sentences"]) > 1]
print(f"Tập 07: {len(sh)} shot · {len(multi)} shot nhiều câu")
for s in multi[:3]:
    print(json.dumps(s, ensure_ascii=False, indent=1)[:1200]); print("---")

print()
print("=== dòng bảng shot Tập 07 (mục 6 trong kế hoạch) có nhiều câu ===")
plan = (ROOT/"02_SAN_XUAT/Tap07/KeHoach_Video_Tap07.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]
for line in sec.splitlines():
    if re.match(r"\|\s*\d-\d+", line) and ("–" in line or "#" in line):
        print(line[:260])
        if line.count("|") > 0:
            pass
