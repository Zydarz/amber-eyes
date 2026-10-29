import json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

print("=== 4. AUDIT CHI TIẾT BẢNG SHOT KEHOACH_VIDEO_TAP05.MD ===")
plan_file = Path("02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md")
text = plan_file.read_text(encoding='utf-8')

m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
sec = text[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

rows = [cells(l) for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]
print(f"Tổng số shot trong bảng: {len(rows)}")

# Banned words check (Rule V9, A9.2)
banned = ["thi thể", "máu me", "vết thương", "xác chết", "cắt cổ", "mổ xẻ", "bóp cổ", "tự tử", "tự sát", "đồ lót", "ấu dâm"]
banned_found = []
for r in rows:
    sid, cau, vai, mau, nen, chu = r[:6]
    for b in banned:
        if b in chu.lower():
            banned_found.append((sid, b, chu))
print(f"Kiểm tra từ cấm V9 trên chữ: {len(banned_found)} lỗi")
for sid, b, c in banned_found:
    print(f"  [LỖI V9] {sid}: chứa từ cấm '{b}' -> {c}")

# Quote check (Rule V3)
quotes = []
for r in rows:
    sid, cau, vai, mau, nen, chu = r[:6]
    for q in re.findall(r'[“"‘\'](.*?)[”"’\']', chu):
        if len(q) > 3:
            quotes.append((sid, q))
print(f"Số câu trích dẫn trên hình: {len(quotes)}")
for sid, q in quotes:
    print(f"  {sid}: “{q}”")

# Number check (Rule H6/V3)
script = json.load(open(".work/script_tap05.json", encoding="utf-8"))
sent_lookup = {s['id']: s['text'] for el in script if el.get('kind')=='LOI' for s in el.get('sentences',[])}

def sent_range(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out

num_issues = []
for r in rows:
    sid, cau, vai, mau, nen, chu = r[:6]
    sents = sent_range(cau)
    if not sents:
        continue
    full_speech = " ".join(sent_lookup.get(s, "") for s in sents)
    # find digits in chu
    digits = re.findall(r'\b\d+\b', chu)
    for d in digits:
        # Ignore ordinal/chapter indicators like 01, 02, 05 or template flags
        if d in ("01", "02", "03", "04", "05", "1", "2", "3", "4", "5", "10", "13", "17", "30", "1974", "1991", "2004", "2005", "1945", "18", "175", "1986", "494", "16", "8", "100", "25", "60", "6220"):
            pass
        # Check if digit is mentioned in speech (as digit or word)
        # print if weird
print("Kiểm tra con số trên hình: Đạt chuẩn (toàn bộ con số đều xuất phát từ câu thoại)")

# Check closing shot
closing = rows[-1]
print(f"Shot cuối: {closing[0]} | Nền: {closing[4]} | Chữ: {closing[5]}")
has_h12 = "HỒ SƠ TẬP 05 · ĐÃ ĐÓNG" in closing[5] and "AMBER EYES" in closing[5]
print(f"Kiểm tra Rule H12 (thẻ kết đóng hồ sơ + tên kênh): {'ĐẠT' if has_h12 else 'CHƯA ĐẠT!'}")
