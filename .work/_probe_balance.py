import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, r"D:\TEST\Gax\Audi\.work")
import tts_sentences as TS  # noqa: E402

af = Path(r"D:\TEST\Gax\Audi\.work\tts_probe.json")
af.write_text(json.dumps({"requests": [{"text": "Balance probe.", "voice_id": "English_Trustworth_Man",
                                        "emotion": "neutral", "speed": 0.97, "pitch": 0,
                                        "volume": 1.0, "output_file": "probe_001"}]},
                          ensure_ascii=False), encoding="utf-8")
res = TS.mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)], 300)
print(json.dumps(res, ensure_ascii=False)[:600])
