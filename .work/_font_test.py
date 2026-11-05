from PIL import Image, ImageDraw, ImageFont
im = Image.new("RGB", (900, 200), (18, 18, 22))
d = ImageDraw.Draw(im)
d.text((20, 20), "제2막 · 심연의 4단계", font=ImageFont.truetype("C:/Windows/Fonts/malgunbd.ttf", 40), fill=(240, 220, 120))
d.text((20, 90), "犯罪心理学 · 대령의 두 얼굴", font=ImageFont.truetype("C:/Windows/Fonts/malgun.ttf", 34), fill=(255, 255, 255))
d.text((20, 145), "2009년 7월 · 46세 · JESSICA LLOYD", font=ImageFont.truetype("C:/Windows/Fonts/malgun.ttf", 30), fill=(200, 200, 220))
im.save(r"D:/TEST/Gax/amber-eyes/.work/_font_test_ko.png")
print("ok")
