import json, pathlib
d=json.loads(pathlib.Path(".work/freesound_candidates.json").read_text(encoding="utf-8"))
rows=[c for e in d["codes"] for c in e["candidates"]]
ok=[c for c in rows if c.get("duration_file")]
print("ung vien:", len(rows), "| co do duoc:", len(ok))
print("tac gia khac nhau:", len({c.get("author") for c in rows}))
print("license:", {c["license_id"] for c in rows})
print("thoi luong: min %.2fs  max %.2fs" % (min(c["duration_file"] for c in ok), max(c["duration_file"] for c in ok)))
print("mean dBFS: min %.1f  max %.1f" % (min(c["mean_db"] for c in ok), max(c["mean_db"] for c in ok)))
print("ma khong co ung vien:", [e["code"] for e in d["codes"] if not e["candidates"]] or "khong co")
print()
print("=== ung vien theo ma ===")
for e in d["codes"]:
    names = " | ".join(f"{c['sound_id']}({c.get('duration_file')}s)" for c in e["candidates"])
    print(f"  {e['code']:<34} {len(e['candidates'])} : {names}")
