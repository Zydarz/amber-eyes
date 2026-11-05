import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Fix EN
with open('01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md', 'r', encoding='utf-8') as f:
    en = f.read()

en = en.replace('the 988 Suicide and Crisis Lifeline', 'the 988 Mental Health and Crisis Lifeline')

with open('01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md', 'w', encoding='utf-8', newline='') as f:
    f.write(en)
with open('01_KICH_BAN/Tap07/kichban_tap07_EN.md', 'w', encoding='utf-8', newline='') as f:
    f.write(en)

# Fix KO
with open('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md', 'r', encoding='utf-8') as f:
    ko = f.read()

ko = ko.replace('자살예방 상담전화 109번', '정신건강 및 위기 상담전화 109번')

with open('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md', 'w', encoding='utf-8', newline='') as f:
    f.write(ko)

print("Replaced taboo words in EN and KO")
