"""Dời 18 file đã khôi phục (giọng cũ English_Deep-VoicedGentleman) sang thư mục dự phòng.

Bắt buộc: tts_sentences.py BỎ QUA câu đã có file mp3. Nếu giữ nguyên tên ở audio_s_EN_t02/
thì sau khi nạp tiền nó sẽ KHÔNG đọc lại ⇒ vai D vẫn lệch giọng ở 18 câu đó.
"""
import json
import shutil
from pathlib import Path

W = Path(r"D:\TEST\Gax\Audi\.work")
OUT = W / "audio_s_EN_t02"
BAK = OUT / "_dg_backup"
BAK.mkdir(exist_ok=True)
man = json.loads((W / "tts_manifest_EN_t02.json").read_text(encoding="utf-8"))
TARGET = {"4.08#9"} | {f"4.10#{k}" for k in range(1, 11)} | {f"5.08#{k}" for k in range(1, 8)}
n = 0
for m in man:
    if m["id"] in TARGET:
        src = OUT / m["file"]
        if src.exists():
            shutil.move(str(src), str(BAK / m["file"]))
            n += 1
print(f"đã dời {n} file sang {BAK.name}/")
print("còn lại trong audio_s_EN_t02:", len(list(OUT.glob('*.mp3'))))
