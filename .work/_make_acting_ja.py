import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

# Đọc acting VN của Tập 02 (Director's Cut)
vn_acting = json.loads((WORK / "acting_tap02.json").read_text(encoding="utf-8"))
ja_script = json.loads((WORK / "script_tap02_JA.json").read_text(encoding="utf-8"))

ja_acting = {
    "_doc": "Diễn xuất từng câu cho bản tiếng Nhật (Tap02_JA). Kế thừa cảm xúc từ bản chuẩn Tap 02 Director's Cut; pitch = 0 (G5); speed clamp G4.",
    "_pause_after": vn_acting.get("_pause_after", {})
}

sent_count = 0
for e in ja_script:
    if e.get("kind") == "LOI":
        for s in e.get("sentences", []):
            sid = s["id"]
            sent_count += 1
            if sid in vn_acting:
                emo, sp, pitch, aside = vn_acting[sid]
                # Pitch luôn = 0 theo G5
                ja_acting[sid] = [emo, sp, 0, None]
            else:
                ja_acting[sid] = ["neutral", 0.0, 0, None]

out_p = WORK / "acting_tap02_JA.json"
out_p.write_text(json.dumps(ja_acting, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Created {out_p.name} with {sent_count} sentences and {len(ja_acting.get('_pause_after', {}))} pauses.")
