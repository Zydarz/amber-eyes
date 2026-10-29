import sys

with open('AGENTS.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = "| H3 | **Ảnh phải khớp lời, không chỉ khớp chủ đề.** Kịch bản nói \"ngồi đối diện\" mà ảnh hai người ngồi cạnh nhau → sai. Chữ \"trần tầng hầm\" mà ảnh hộp nằm trên sàn → sai |"

replacement = "| H3 | **Ảnh phải khớp lời, không chỉ khớp chủ đề.** Kịch bản nói \"ngồi đối diện\" mà ảnh hai người ngồi cạnh nhau → sai. Đang nói \"mức lương 5$\" mà ảnh chuyển sang tủ áo khoác → sai. Gom trọn các câu cùng chủ đề vào cùng một shot |"

if target not in text:
    print("Target not found in AGENTS.md!")
    sys.exit(1)

new_text = text.replace(target, replacement)
with open('AGENTS.md', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated AGENTS.md successfully!")
