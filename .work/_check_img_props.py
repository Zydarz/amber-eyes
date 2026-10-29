from PIL import Image
import numpy as np

files = [
    "t5_btk_signature_letter.png",
    "t5_newspaper_classified_494.png",
    "t5_metadata_screen.png",
    "t5_church_website_search.png",
    "t5_handwritten_note_floppy.png"
]

for f in files:
    im = Image.open(f"assets/bg/{f}")
    print(f"{f}: size={im.size}, mode={im.mode}")
