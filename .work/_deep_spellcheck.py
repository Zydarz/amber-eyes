import re, sys
sys.stdout.reconfigure(encoding='utf-8')

vn_text = open('01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md', encoding='utf-8').read()
en_text = open('01_KICH_BAN/Tap01_EN/kichban_tap01_EN.md', encoding='utf-8').read()
ja_text = open('01_KICH_BAN/Tap01_JA/kichban_tap01_JA.md', encoding='utf-8').read()
ko_text = open('01_KICH_BAN/Tap01_KO/kichban_tap01_KO.md', encoding='utf-8').read()

print("Kiểm tra tính toàn vẹn 4 kịch bản:")

# 1. Kiểm tra dấu câu bất thường trong VN
vn_weird = re.findall(r'[,.?!;:]\s*[,.?!;:]', vn_text)
print("VN dấu câu liền nhau bất thường:", [w for w in vn_weird if '...' not in w and '…' not in w])

# 2. Kiểm tra dấu câu bất thường trong EN
en_weird = re.findall(r'[,.?!;:]\s*[,.?!;:]', en_text)
print("EN dấu câu liền nhau bất thường:", [w for w in en_weird if '...' not in w and '…' not in w])

# 3. Kiểm tra JA: các ký tự giản thể hoặc ký tự lạ
import _qc_ja
simps = [ch for ch in ja_text if ch in _qc_ja.SIMPLIFIED]
print("JA chữ Hán giản thể TQ sót lại:", set(simps))
vn_in_ja = [ch for ch in ja_text if ch in _qc_ja.VN_CHARS]
print("JA ký tự tiếng Việt sót lại:", set(vn_in_ja))

# 4. Kiểm tra KO: ký tự tiếng Việt hoặc chữ Hán
import _qc_ko_parity
vn_in_ko = [ch for ch in ko_text if ch in _qc_ko_parity.VN_STRICT]
print("KO ký tự tiếng Việt sót lại:", set(vn_in_ko))
hanja_in_ko = [ch for ch in ko_text if _qc_ko_parity.HANJA.match(ch)]
print("KO chữ Hán (Hanja) sót lại:", set(hanja_in_ko))
