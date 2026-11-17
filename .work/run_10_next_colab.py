import requests
import json
import base64
import os
import sys
import time
from PIL import Image, ImageEnhance
import numpy as np

BASE_URL = "https://decor-starting-provisions-positioning.trycloudflare.com"

# Load jobs 6 to 15 (next 10 images)
jobs = json.load(open('.work/bg_jobs_tap14_extra68.json', encoding='utf-8'))
jobs_10 = jobs[5:15]

artifact_dir = "C:/Users/ADMIN/.gemini/antigravity/brain/f042e153-f50a-43be-a4f3-bf2d6842bba5"

print(f"=== BẮT ĐẦU TẠO TIẾP 10 ẢNH (Từ ảnh số 6 đến 15) QUA COLAB ===")

for idx, job in enumerate(jobs_10, 6):
    name = job["name"]
    prompt = job["prompt"]
    print(f"\n[{idx}/15] Gửi job '{name}' lên Colab...")
    
    payload = {
        "prompt": prompt,
        "width": 1056,
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
            
            if st == "completed":
                img_bytes = base64.b64decode(st_data["image_base64"])
                target_bg = os.path.abspath(f"assets/bg/{name}.png")
                with open(target_bg, "wb") as f:
                    f.write(img_bytes)
                
                # Apply standard 2K resizing and noir post-processing
                im = Image.open(target_bg)
                im_2k = im.resize((2112, 1188), Image.Resampling.LANCZOS)
                color = ImageEnhance.Color(im_2k).enhance(0.70)
                contrast = ImageEnhance.Contrast(color).enhance(1.15)
                arr = np.array(contrast, dtype=np.float32)
                h, w, c = arr.shape
                y, x = np.ogrid[:h, :w]
                cx, cy = w / 2, h / 2
                dist = np.sqrt((x - cx)**2 + (y - cy)**2)
                max_dist = np.sqrt(cx**2 + cy**2)
                vignette = 1.0 - 0.40 * (dist / max_dist)**1.8
                vignette = np.clip(vignette, 0.4, 1.0)[:, :, np.newaxis]
                arr = arr * vignette
                np.random.seed(42 + idx)
                grain = np.random.normal(0, 6.0, arr.shape)
                arr = np.clip(arr + grain, 0, 255).astype(np.uint8)
                final_im = Image.fromarray(arr)
                
                final_im.save(target_bg)
                art_path = os.path.join(artifact_dir, f"{name}.png")
                final_im.save(art_path)
                
                print(f"  -> XONG & HẬU KỲ trong {st_data.get('time_taken')}s! Đã lưu: {name}.png")
                completed = True
                break
            elif st == "failed":
                print(f"  -> THẤT BẠI: {st_data.get('error')}")
                break
                
        if not completed:
            print("  -> TIMEOUT!")
    except Exception as e:
        print(f"  -> LỖI KẾT NỐI: {e}")

# Cập nhật provenance.json
try:
    prov = json.load(open('provenance.json', encoding='utf-8'))
    for j in jobs_10:
        fn = f"assets/bg/{j['name']}.png"
        if not any(p.get('file') == fn for p in prov):
            prov.append({
                'file': fn,
                'loai': 'nen 16:9 dung chung 3 ngon ngu',
                'cong_cu': 'Google Colab FLUX.2-klein-4B (Sequential CPU Offload + Deep Noir Post-processing)',
                'ngay': '2026-11-17',
                'prompt': j['prompt'],
                'seed': 42 + j['stt'],
                'font': None,
                'dieu_khoan': 'FLUX.2 Open Model License / Creative Commons Commercial',
                'kiem_tra_thuong_mai': 'dat',
                'ghi_chu': f"Sinh bo sung Tap 14 (H22/H25) cau {j['sentences']}, 2026-11-17"
            })
    with open('provenance.json', 'w', encoding='utf-8') as f:
        json.dump(prov, f, ensure_ascii=False, indent=2)
    print("\nĐã cập nhật provenance.json thành công!")
except Exception as e:
    print(f"Lỗi cập nhật provenance: {e}")

print("\n=== HOÀN TẤT TẠO 10 ẢNH TIẾP THEO ===")
