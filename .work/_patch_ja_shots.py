import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(r"D:\TEST\Gax\Audi\.work")

ja_shots = json.load(open(W / "shots_text_tap02_JA.json", encoding="utf-8"))

# Apply fixes
ja_shots["2-16"] = ["*不気味な捕食者の本能* → `#2`: **NISSAN PATHFINDER**", [], None]
ja_shots["2-17"] = ["*雪の夜の侵入* · **JESSICA LLOYDの家** · *雪の上のタイヤ痕*", [], None]
ja_shots["2-21"] = ["*一つの引き出しに閉じ込める* → `#8`: **完全に独立した二重生活**", [], None]
ja_shots["3-17"] = ["**二つの引き出し** · *互いに侵犯しない*", [], None]
ja_shots["4-13"] = ["*令状に基づく捜索* · **オタワの住宅とツイードの別荘**", ["令状に基づいて"], None]
ja_shots["4-14"] = ["*現場の雪中の靴跡と本人の靴跡* → “まったく同じだ”", [], None]
ja_shots["4-27"] = ["**二つの引き出しの間の仕切りが砕け散った**", [], None]
ja_shots["4-31"] = ["*約十時間の尋問の末* · **完璧な仮面は完全に瓦解した**", [], None]
ja_shots["5-14"] = ["**見逃してはならない四つの危険信号** · *心理学者と捜査官の助言*", [], None]

out_path = W / "shots_text_tap02_JA.json"
out_path.write_text(json.dumps(ja_shots, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated {out_path}")
