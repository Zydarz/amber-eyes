import json
from pathlib import Path

r = json.loads(Path(".work/speech_full_recognized_en_t02.json").read_text(encoding="utf-8"))
for x in r[1:20]:
    print(f"{x['start']:7.2f} - {x['end']:7.2f} : {x['text']}")
