import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/_tap10_sentences.json', 'r', encoding='utf-8') as f:
    raw_sentences = json.load(f)

text_corpus = ' '.join([item['text']['text'] for item in raw_sentences])
cleaned = re.sub(r'[\.,:;!\?\"“”\(\)\[\]–\-\'\’\/]', ' ', text_corpus)
tokens = cleaned.split()
unique_tokens = sorted(list(set(tokens)), key=lambda x: x.lower())

with open('.work/_tap10_unique_tokens.txt', 'w', encoding='utf-8') as f:
    for t in unique_tokens:
        f.write(t + '\n')

print(f'Wrote {len(unique_tokens)} unique tokens to .work/_tap10_unique_tokens.txt')
