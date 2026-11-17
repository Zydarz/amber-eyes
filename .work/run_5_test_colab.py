import requests
import json
import base64
import os
import sys
import time

BASE_URL = "https://decor-starting-provisions-positioning.trycloudflare.com"

# Load jobs
jobs = json.load(open('.work/bg_jobs_tap14_extra68.json', encoding='utf-8'))
jobs_5 = jobs[:5]

artifact_dir = "C:/Users/ADMIN/.gemini/antigravity/brain/f042e153-f50a-43be-a4f3-bf2d6842bba5"

print(f"=== BẮT ĐẦU TẠO THỬ 5 ẢNH ĐẦU TIÊN QUA COLAB ===")

for idx, job in enumerate(jobs_5, 1):
    name = job["name"]
    prompt = job["prompt"]
    print(f"\n[{idx}/5] Gửi job '{name}' lên Colab...")
    
    payload = {
        "prompt": prompt,
        "width": 1056,  # 16:9 base resolution
        "height": 592,
        "steps": 4,
        "seed": 42 + idx
    }
    
    try:
        res = requests.post(f"{BASE_URL}/submit", json=payload, timeout=20)
        res.raise_for_status()
        job_id = res.json().get("job_id")
        print(f"  -> Đã xếp hàng! Job ID: {job_id}. Đang chờ Colab render...")
        
        start_time = time.time()
        completed = False
        while time.time() - start_time < 300:
            time.sleep(5)
            st_res = requests.get(f"{BASE_URL}/status/{job_id}", timeout=20)
            st_res.raise_for_status()
            st_data = st_res.json()
            st = st_data.get("status")
            elapsed = int(time.time() - start_time)
            print(f"  [{elapsed}s] Trạng thái: {st}")
            
            if st == "completed":
                img_bytes = base64.b64decode(st_data["image_base64"])
                
                # Save to assets/bg
                target_bg = os.path.abspath(f"assets/bg/{name}.png")
                with open(target_bg, "wb") as f:
                    f.write(img_bytes)
                
                # Copy to artifact dir for preview
                artifact_path = os.path.join(artifact_dir, f"{name}.png")
                with open(artifact_path, "wb") as f:
                    f.write(img_bytes)
                    
                print(f"  -> XONG trong {st_data.get('time_taken')}s! Đã lưu: {name}.png")
                completed = True
                break
            elif st == "failed":
                print(f"  -> THẤT BẠI: {st_data.get('error')}")
                break
                
        if not completed:
            print("  -> TIMEOUT!")
    except Exception as e:
        print(f"  -> LỖI KẾT NỐI: {e}")

print("\n=== HOÀN TẤT TẠO 5 ẢNH THỬ NGHIỆM ===")
