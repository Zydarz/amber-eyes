import json

old = json.load(open(".work/_cu/shots_EN_t02_20261031_233834.json", encoding="utf-8"))
manifest = json.load(open(".work/tts_manifest_EN_t02.json", encoding="utf-8"))
m_sents = set(x["id"] for x in manifest)

old_sents = []
for s in old["shots"]:
    for sid in s.get("sentences", []):
        old_sents.append(sid)

print(f"Old shots count: {len(old['shots'])}")
print(f"Old shot sentence references: {len(old_sents)}")
print(f"Unique sentences in old shots: {len(set(old_sents))}")
print(f"Manifest sentences count: {len(m_sents)}")
diff = set(old_sents) - m_sents
print(f"Old shots sentences NOT in manifest: {diff}")
diff2 = m_sents - set(old_sents)
print(f"Manifest sentences NOT in old shots: {diff2}")
