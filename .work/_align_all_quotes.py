import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Fix EN
with open('01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md', 'r', encoding='utf-8') as f:
    en = f.read()

en = en.replace('was psychologically objectified into a living prop', 'was psychologically ‘Objectified’ into a living prop')
en = en.replace('‘Conrad’s Law’', '‘Conrad\'s Law’')

with open('01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md', 'w', encoding='utf-8', newline='') as f:
    f.write(en)
with open('01_KICH_BAN/Tap07/kichban_tap07_EN.md', 'w', encoding='utf-8', newline='') as f:
    f.write(en)

# Fix JA
with open('01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md', 'r', encoding='utf-8') as f:
    ja = f.read()

ja = ja.replace('「非接触の犯罪」', '非接触の犯罪')
ja = ja.replace('「妄想の飢餓状態」', '妄想の飢餓状態')
ja = ja.replace('「臆病」', '臆病')
ja = ja.replace('「これほどの冷酷な行為の背後にある真の動機は一体何だったのか」', 'これほどの冷酷な行為の背後にある真の動機は一体何だったのか')
ja = ja.replace('「デジタル・ミュンヒハウゼン症候群」', 'デジタル・ミュンヒハウゼン症候群')
ja = ja.replace('「生きた小道具（living props）」として客体化（Objectification）されていたのです。', '生きた小道具として「客体化」（Objectification）されていたのです。')
ja = ja.replace('「ハロー効果（Halo Effect）」', '「ハロー効果」')
ja = ja.replace('「心理的シグネチャー（Signature）」', '「心理的シグネチャー」')
ja = ja.replace('「Conradが行方不明になった」', 'Conradが行方不明になった')
ja = ja.replace('「精神の分断（コンパートメンタライゼーション）」', '「精神の分断」')
ja = ja.replace('「人助け」', '人助け')
ja = ja.replace('「被告人Michelle Carterを有罪とする、罪名は過失致死罪である」と。', '被告人Michelle Carterを有罪とする、罪名は過失致死罪である、と。')
ja = ja.replace('「自己愛の完全崩壊（Narcissistic Collapse）」', '「自己愛の完全崩壊」')
ja = ja.replace('「Conrad法（Conrad\'s Law）」', 'Conrad法')
ja = ja.replace('「生存のための赤信号（Red Flags）」', '生存のための赤信号')

with open('01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md', 'w', encoding='utf-8', newline='') as f:
    f.write(ja)

print("Quotes aligned across EN and JA")
