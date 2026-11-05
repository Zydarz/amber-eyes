import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Fix JA
with open('01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md', 'r', encoding='utf-8') as f:
    ja = f.read()

ja = ja.replace('解剖します。すなわち', '解剖します、すなわち')
ja = ja.replace('見て取れます。すなわち', '見て取れます、すなわち')
ja = ja.replace('説明してくれます。すなわち', '説明してくれます、すなわち')
ja = ja.replace('暴き出しました。Michelle Carter', '暴き出しました、Michelle Carter')
ja = ja.replace('シグネチャー（Signature）」でした。すなわち', 'シグネチャー（Signature）」でした、すなわち')
ja = ja.replace('戦慄を覚えるほどでした。事件当夜', '戦慄を覚えるほどでした、事件当夜')
ja = ja.replace('宣言しました。「被告人Michelle Carterを有罪とする。罪名は過失致死罪である。」', '宣言しました、「被告人Michelle Carterを有罪とする、罪名は過失致死罪である」と。')
ja = ja.replace('お寄せください。それでは、次回の事件ファイルでお会いしましょう。', 'お寄せください、それでは次回の事件ファイルでお会いしましょう。')

with open('01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md', 'w', encoding='utf-8', newline='') as f:
    f.write(ja)

# Fix KO
with open('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md', 'r', encoding='utf-8') as f:
    ko = f.read()

ko = ko.replace('해부하고자 합니다. 바로', '해부하고자 합니다, 바로')
ko = ko.replace('목격하게 됩니다. 바로', '목격하게 됩니다, 바로')
ko = ko.replace('설명해 줍니다. 바로', '설명해 줍니다, 바로')
ko = ko.replace('밝혀냈습니다. 바로', '밝혀냈습니다, 바로')
ko = ko.replace('시그니처（Signature）’였습니다. 즉', '시그니처（Signature）’였습니다, 즉')
ko = ko.replace('지경이었습니다. 사건 당일 밤', '지경이었습니다, 사건 당일 밤')
ko = ko.replace('선언했습니다. “피고인 Michelle Carter에게 과실치사 유죄를 선고한다.”', '선언했습니다, ‘피고인 Michelle Carter에게 과실치사 유죄를 선고한다.’')

with open('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md', 'w', encoding='utf-8', newline='') as f:
    f.write(ko)

print("Fixes applied successfully to JA and KO")
