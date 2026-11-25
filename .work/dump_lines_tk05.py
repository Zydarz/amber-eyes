import json
from pathlib import Path

ROOT = Path(".")
spec_files = {
    "vi": ROOT / "02_SAN_XUAT/TIKTOK/Tap05/SPEC_AUDIO_CLIP_TAP05.json",
    "en": ROOT / "02_SAN_XUAT/TIKTOK/Tap05_EN/SPEC_AUDIO_CLIP_TAP05.json",
    "ja": ROOT / "02_SAN_XUAT/TIKTOK/Tap05_JA/SPEC_AUDIO_CLIP_TAP05.json"
}

for lang, sp in spec_files.items():
    data = json.loads(sp.read_text(encoding="utf-8"))
    items = []
    for cid in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
        c = data["clips"][cid]
        for l in c["lines"]:
            items.append({
                "clip": cid,
                "id": l["clip_line_id"],
                "role": l["role"],
                "text": l["text"],
                "emotion": l.get("emotion", "neutral"),
                "speed": l.get("speed_offset", 0.0),
                "pause_after": l.get("pause_after_s", 0.5)
            })
    print(f"Lang {lang}: {len(items)} lines parsed. Sample: {items[0]}")

