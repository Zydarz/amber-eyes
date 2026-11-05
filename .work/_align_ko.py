import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read KO file
with open('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md', 'r', encoding='utf-8') as f:
    ko = f.read()

# Fix proper noun in 1.06
ko = ko.replace('Conrad Henri Roy III가', 'Conrad Henri Roy가')

# Fix numbers in 5.04
ko = ko.replace('자살예방 상담전화 109번 등을', '자살예방 상담전화 109번, 또는 지원 핫라인 096 306 1414 및 111번 등을')

# Clean quotes in KO so only the 8 quotes matching VN exist
# Currently in VN:
# 1. 'Vật hóa' -> ‘객체화’
# 2. 'Hiệu ứng Hào quang' -> ‘후광 효과’
# 3. 'Chữ ký tâm lý' -> ‘심리적 시그니처’
# 4. 'Chia ngăn nhận thức' -> ‘인지적 구획화’
# 5. 'Homers for Conrad' -> ‘Homers for Conrad’
# 6. 'say thuốc không tự nguyện' -> ‘비자발적 약물 취약 상태’
# 7. 'Sự sụp đổ cái tôi ái kỷ' -> ‘자기애적 붕괴’
# 8. 'Đạo luật Conrad' -> ‘Conrad 법’

# Remove extra quotes from KO:
ko = ko.replace('‘비접촉 범죄’', '비접촉 범죄')
ko = ko.replace('‘망상 중독과 가속화 궤적’', '망상 중독과 가속화 궤적')
ko = ko.replace('‘망상의 굶주림’', '망상의 굶주림')
ko = ko.replace('‘이토록 잔혹한 행위 이면에 숨겨진 진짜 동기는 무엇인가’', '이토록 잔혹한 행위 이면에 숨겨진 진짜 동기는 무엇인가')
ko = ko.replace('‘디지털 뮌하우젠 증후군’', '디지털 뮌하우젠 증후군')
ko = ko.replace('‘살아있는 소품’', '살아있는 소품')
ko = ko.replace('‘후광 효과（Halo Effect）’', '‘후광 효과’')
ko = ko.replace('‘Glee’', 'Glee')
ko = ko.replace('‘심리적 시그니처（Signature）’', '‘심리적 시그니처’')
ko = ko.replace('‘인지적 구획화（Compartmentalization）’', '‘인지적 구획화’')
ko = ko.replace('‘도덕적 중화 기술’', '도덕적 중화 기술')
ko = ko.replace('‘피고인 Michelle Carter에게 과실치사 유죄를 선고한다.’', '피고인 Michelle Carter에게 과실치사 유죄를 선고한다')
ko = ko.replace('‘자기애적 붕괴（Narcissistic Collapse）’', '‘자기애적 붕괴’')
ko = ko.replace('‘Conrad 법（Conrad’s Law）’', '‘Conrad 법’')
ko = ko.replace('‘생존을 위한 붉은 깃발（Red Flags）’', '생존을 위한 붉은 깃발')

with open('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md', 'w', encoding='utf-8', newline='') as f:
    f.write(ko)

print("KO file updated")
