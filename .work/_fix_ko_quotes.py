import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md', 'r', encoding='utf-8') as f:
    ko = f.read()

# Add quote to 객체화 at 3.03
ko = ko.replace('철저히 객체화（Objectification）되었습니다.', '철저히 ‘객체화’（Objectification）되었습니다.')

# Remove the second quote on Conrad 법 at 5.04
ko = ko.replace('‘Conrad 법’으로 명명된 법안의 제정을 위해 끈질기게 입법 운동을 전개했습니다.\n이 법안은 타인을 심리적으로 강요하거나 조작하여 스스로를 해치도록 몰아넣는 행위를 명백한 범죄로 규정하고, 온라인 포식자들이 악용해 온 법적 사각지대를 완전히 차단하는 것을 목표로 합니다.\n가상 공간의 유해한 관계로부터 여러분 자신과 사랑하는 사람들을 보호하기 위해, Amber Eyes는 이 사건 기록을 통해 도출된 네 가지 생존을 위한 붉은 깃발을 공유하고자 합니다.\n첫 번째 붉은 깃발',
                '‘Conrad 법’으로 명명된 법안의 제정을 위해 끈질기게 입법 운동을 전개했습니다.\n이 법안은 타인을 심리적으로 강요하거나 조작하여 스스로를 해치도록 몰아넣는 행위를 명백한 범죄로 규정하고, 온라인 포식자들이 악용해 온 법적 사각지대를 완전히 차단하는 것을 목표로 합니다.\n가상 공간의 유해한 관계로부터 여러분 자신과 사랑하는 사람들을 보호하기 위해, Amber Eyes는 이 사건 기록을 통해 도출된 네 가지 생존을 위한 붉은 깃발을 공유하고자 합니다.\n첫 번째 붉은 깃발')

# Let's check where Conrad 법 appears with quotes in KO:
import re
print("Found quotes:", re.findall(r"‘([^’]{2,})’", ko))

# If there's another ‘Conrad 법’, remove the quote
# Let's count occurrences of ‘Conrad 법’
parts = ko.split('‘Conrad 법’')
if len(parts) > 2:
    # keep only the first one
    ko = parts[0] + '‘Conrad 법’' + 'Conrad 법'.join(parts[1:])

with open('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md', 'w', encoding='utf-8', newline='') as f:
    f.write(ko)

print("Quotes fixed in KO")
