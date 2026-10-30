import json
import sys
from pathlib import Path

sys.path.insert(0, r"D:\TEST\Gax\Audi\.work")
import tts_sentences as TS  # noqa: E402

af = Path(__file__).resolve().parents[1] / ".work" / "tts_probe2.json"
af.write_text(json.dumps({"text": "And then Smyth laid it bare: this matter had reached its end.",
                          "voice_id": "English_Trustworth_Man", "emotion": "neutral",
                          "speed": 0.91, "pitch": 0, "volume": 1.0,
                          "output_file": "probe_single_001"}, ensure_ascii=False), encoding="utf-8")
res = TS.mcode(["connector", "call", "connector__matrix__synthesize_speech", "--args-file", str(af)], 300)
print(json.dumps(res, ensure_ascii=False)[:600])
