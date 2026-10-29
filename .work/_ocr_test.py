import pytesseract
from PIL import Image

try:
    txt = pytesseract.image_to_string(Image.open("assets/bg/t5_newspaper_classified_494.png"))
    print("OCR result:", repr(txt[:200]))
except Exception as e:
    print("Tesseract error:", e)
