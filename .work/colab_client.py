import requests
import json
import base64
import os
import sys
import time

BASE_URL = "https://decor-starting-provisions-positioning.trycloudflare.com"

prompt = "A cinematic graphic novel noir illustration of a mysterious owl detective perched on an old vintage crime case file, amber ambient light, noir aesthetic, high detail"
if len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])

payload = {
    "prompt": prompt,
    "width": 768,
    "height": 768,
    "steps": 4,
    "seed": 42
}

print(f"Submitting job to Colab...")
try:
    res = requests.post(f"{BASE_URL}/submit", json=payload, timeout=20)
    res.raise_for_status()
    submit_data = res.json()
    job_id = submit_data.get("job_id")
    print(f"Job queued successfully! Job ID: {job_id}")
    
    print("Waiting for Colab to render image...")
    max_wait = 300 # 5 minutes
    start_time = time.time()
    
    while time.time() - start_time < max_wait:
        time.sleep(5)
        status_res = requests.get(f"{BASE_URL}/status/{job_id}", timeout=20)
        status_res.raise_for_status()
        status_data = status_res.json()
        current_status = status_data.get("status")
        
        elapsed = int(time.time() - start_time)
        print(f"[{elapsed}s] Job status: {current_status}")
        
        if current_status == "completed":
            img_b64 = status_data["image_base64"]
            img_bytes = base64.b64decode(img_b64)
            out_file = os.path.abspath("flux2_klein_result.png")
            with open(out_file, "wb") as f:
                f.write(img_bytes)
            print(f"\nSUCCESS! Image generated in {status_data.get('time_taken')}s and saved to:\n{out_file}")
            sys.exit(0)
        elif current_status == "failed":
            print(f"\nFAILED: {status_data.get('error')}")
            sys.exit(1)
            
    print("TIMEOUT: Image rendering took too long.")
except Exception as e:
    print(f"ERROR: {e}")
