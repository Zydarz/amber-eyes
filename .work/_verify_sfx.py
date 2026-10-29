from pathlib import Path
SFX=Path("assets/sfx")
files=list(SFX.rglob("*.wav"))
stems={p.stem for p in files}
print("file .wav:", len(files), "| stem duy nhất:", len(stems))
print("=> khac biet:", len(files)-len(stems), "file trung ten o cac thu muc tXX khac nhau")
others=[p for p in SFX.rglob("*") if p.suffix.lower() in (".mp3",".ogg",".m4a",".aiff",".flac")]
print("file khac dinh dang (mp3/ogg/...) trong assets/sfx:", len(others))
for p in others[:10]: print("   ", p)
