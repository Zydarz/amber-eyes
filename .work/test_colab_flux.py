import requests
import json
import base64
import os
import sys

URL = "https://measured-chamber-pink-gold.trycloudflare.com/generate"

prompt = "A cinematic graphic novel illustration of a mysterious owl detective perched on an old vintage crime case file, amber ambient light, noir aesthetic, high detail"
if len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])

payload = {
    "prompt": prompt,
    "width": 768,
    "height": 768,
    "steps": 4,
    "seed": 42
}

print(f"Sending prompt to Colab: {prompt}")
try:
    response = requests.post(URL, json=payload, timeout=120)
    response.raise_for_status()
    data = response.json()
    if data.get("status") == "success":
        img_bytes = base64.b64decode(data["image_base64"])
        out_path = os.path.abspath("colab_flux_generated.png")
        with open(out_path, "wb") as f:
            f.write(img_bytes)
        print(f"SUCCESS: Image saved to {out_path}")
    else:
        print(f"ERROR: {data}")
except Exception as e:
    print(f"FAILED: {e}")
