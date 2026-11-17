import json

with open('.work/_t15_67_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

jobs = []
for i, it in enumerate(items):
    parent = it['parent_bg']
    sids = it['sids']
    txt = it['text']
    
    clean_parent = parent.replace('t15_', '').replace('_', ' ')
    name = f"t15_b{i+1:02d}_{parent.replace('t15_', '')[:28]}"
    if len(name) > 45:
        name = name[:45]
    
    clean_txt = txt.replace('"', '').replace('\n', ' ')
    prompt_context = f"Atmospheric crime scene investigative details in Mesa Arizona, thematic concept of {clean_parent}, deep shadows, abandoned space, forensic still life, cinematic compositions"
    
    prompt = (
        "Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink linework, "
        "high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
        f"{prompt_context}, "
        "gloomy overcast suffocating pale grey sky, cold mist floating over the ground, unsettling silence, "
        "creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, decayed autumn tones, "
        "fine 35mm film grain, David Fincher meets vintage crime comic style. "
        "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, "
        "no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, "
        "no signs, no labels, no logos, no watermark, full-bleed 16:9."
    )
    
    jobs.append({
        'name': name,
        'seed': 15000 + i,
        'sids': sids,
        'parent': parent,
        'desc': f"Ảnh bổ sung H25 ({name}): {clean_txt[:100]}...",
        'prompt': prompt
    })

print(f"Generated {len(jobs)} jobs.")
with open('.work/bg_jobs_tap15_new67.json', 'w', encoding='utf-8') as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)
print("Saved to .work/bg_jobs_tap15_new67.json")
