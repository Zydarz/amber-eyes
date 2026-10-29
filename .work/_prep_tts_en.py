import json
import shutil
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
AUDIO_DIR = WORK / "audio_s_EN_t02"
BACKUP_DIR = WORK / "_cu" / "audio_s_EN_t02_pre_directors_cut"

# 1. Backup full directory
if not BACKUP_DIR.exists():
    print(f"Creating backup at {BACKUP_DIR}...")
    shutil.copytree(AUDIO_DIR, BACKUP_DIR)
    print("Backup complete!")
else:
    print(f"Backup already exists at {BACKUP_DIR}")

# 2. Identify unchanged vs changed sentences
old_manifest = {item["id"]: item for item in json.load(open(WORK / "tts_manifest_EN_t02.json", encoding="utf-8"))}
new_script = json.load(open(WORK / "script_tap02_EN.json", encoding="utf-8"))

def fname(sid):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}.mp3"

to_remove = []
to_keep = []

for e in new_script:
    if e["kind"] != "LOI":
        continue
    for s in e["sentences"]:
        sid = s["id"]
        old_item = old_manifest.get(sid)
        fn = fname(sid)
        fpath = AUDIO_DIR / fn
        # Nếu câu cũ có display text giống hệt câu mới -> GIỮ
        if old_item and old_item.get("display") == s["text"] and fpath.exists():
            to_keep.append(fn)
        else:
            to_remove.append((sid, fn, s["text"]))

print(f"\nSentences to keep (unchanged): {len(to_keep)}")
print(f"Sentences to re-TTS: {len(to_remove)}")

# Xóa các file cũ của những câu cần đọc lại
deleted_count = 0
for sid, fn, txt in to_remove:
    p = AUDIO_DIR / fn
    if p.exists():
        p.unlink()
        deleted_count += 1

# Xóa các file thừa (những câu không còn nằm trong new_script)
new_sids = {s["id"] for e in new_script if e["kind"] == "LOI" for s in e["sentences"]}
new_files = {fname(sid) for sid in new_sids}
extra_deleted = 0
for f in list(AUDIO_DIR.glob("*.mp3")):
    if f.name not in new_files:
        f.unlink()
        extra_deleted += 1

remaining = list(AUDIO_DIR.glob("*.mp3"))
print(f"\nDeleted for re-TTS: {deleted_count} files")
print(f"Deleted extra unused files: {extra_deleted} files")
print(f"Remaining files in audio_s_EN_t02: {len(remaining)} (should be {len(to_keep)})")
