import json

accurate = json.load(open('.work/_accurate_sentences.json', encoding='utf-8'))
for r in accurate:
    print(f"Tap {r['ep']:02d}: sentences={r['sentences']} | turns={r['dialogue_elements']} | words={r['words']} | file={r['script_file']}")
