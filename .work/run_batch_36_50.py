# -*- coding: utf-8 -*-
import json, re
from pathlib import Path

META = json.load(open(".work/meta_clean.json", encoding="utf-8"))

SUBS = [
    (r"\btyped text\b", "graphic lines"),
    (r"\bnewspaper\b", "press gazette"),
    (r"\bnewspapers\b", "press gazettes"),
    (r"\bletter\b", "mail piece"),
    (r"\bletters\b", "documents"),
    (r"\bprinted\b", "published"),
    (r"\bwriting\b", "penning"),
    (r"\btext\b", "lines"),
    (r"\bwords\b", "markings"),
    (r"\bfont\b", "scripture"),
    (r"\btypography\b", "ink styling"),
    (r"\bwritten\b", "inscribed"),
    (r"\bscript\b", "calligraphy"),
    (r"\bheadline\b", "header"),
    (r"\bheadlines\b", "headers"),
    (r"\blabel\b", "tag"),
    (r"\blabels\b", "tags"),
    (r"\bplacard\b", "board"),
    (r"\bbanner\b", "streamer"),
    (r"\bsignpost\b", "marker"),
    (r"\bstreet sign\b", "road marker"),
    (r"\blogo\b", "emblem"),
    (r"\bbadge\b", "plate"),
    (r"\bbadges\b", "plates")
]

def clean_p(text):
    for pat, rep in SUBS:
        text = re.sub(pat, rep, text, flags=re.I)
    return text

total_all = 0

for ep_str, data in META.items():
    ep = int(ep_str)
    target = data["target"]
    splits = data["splits"]
    loc = data["loc"]
    kw = data["keywords"]
    
    script_file = Path(f"01_KICH_BAN/Ho_So_Toi_Pham/Tap{ep}/kichban_tap{ep}_19112026.md")
    raw_text = script_file.read_text(encoding="utf-8")
    acts = re.split(r"## HỒI \d.*", raw_text)[1:]
    
    jobs = []
    
    for a_idx, (act_txt, act_target) in enumerate(zip(acts, splits), 1):
        lines = [l.strip() for l in act_txt.splitlines() if l.strip() and not l.startswith("**[") and not l.startswith("**") and not l.startswith("#") and not l.startswith("---")]
        step = max(1, len(lines) / act_target)
        
        for b_idx in range(act_target):
            l_idx = min(int(b_idx * step), len(lines) - 1)
            line = lines[l_idx]
            
            p_num = b_idx + 1
            key = kw[b_idx % len(kw)]
            job_name = f"t{ep}_a{a_idx}_{p_num:02d}_{key}"
            cue = f"{a_idx}.{max(1, (b_idx // 3) + 1):02d}#{(b_idx % 3) + 1}"
            desc = f"Hồi {a_idx} Tập {ep} ({key}): {line[:90]}..."
            
            if a_idx == 1:
                if b_idx < 4:
                    base = f"Cinematic establishing wide shot of {loc}, cold mist hovering over dark terrain at twilight, deep chiaroscuro noir shadows, distant amber lampposts."
                elif b_idx < 12:
                    base = f"Atmospheric street scene in {loc}, subtle social blindspot concept, misty drizzle, faceless pedestrian silhouettes, 1990s realistic graphic novel tone."
                elif b_idx < 24:
                    base = f"Forensic high-contrast tabletop still life in {loc}, macro view of vintage investigative items and shadowed room, directional amber desk lighting."
                else:
                    base = f"Dramatic action still in {loc}, sudden rupture of routine peace, dynamic diagonal shadows, flashing emergency vehicle beacons illuminating mist."
            elif a_idx == 2:
                if b_idx < 10:
                    base = f"Psychological chiaroscuro composition in {loc}, mental compartmentalization, fractured antique mirror reflection, ominous creeping shadows."
                elif b_idx < 22:
                    base = f"Desolate nocturnal scene in {loc}, solitary predatory silhouette concealed in deep woodland shadows, cold blue moonlight cutting through branches."
                else:
                    base = f"Intimate forensic interior of vehicle or room in {loc}, evidence markers, analytical lighting, graphic novel chiaroscuro realism."
            elif a_idx == 3:
                if b_idx < 10:
                    base = f"Late-night police command center in {loc}, tactical wall maps crisscrossed with red yarn, detectives in shirtsleeves under green banker lamps."
                elif b_idx < 20:
                    base = f"Sterile police interrogation room in {loc}, suspect silhouette seated opposite veteran interrogators under single harsh overhead fluorescent lamp."
                else:
                    base = f"Forensic laboratory scene in {loc}, comparison microscope glowing with split circular circular fields, unshakeable forensic breakthrough."
            elif a_idx == 4:
                if b_idx < 10:
                    base = f"Historic courtroom interior in {loc}, elevated judge bench under seal, crowded gallery of spectators, shaft of daylight cutting across wooden benches."
                elif b_idx < 20:
                    base = f"Emotional witness stand perspective in {loc}, dignified testimony under spotlight, tragic human resilience contrasting with judicial solemnity."
                else:
                    base = f"Judicial hardwood gavel striking sounding block firmly in {loc}, dramatic dust particles rising in sharp beam of light, absolute final sentence."
            else:
                if b_idx < 8:
                    base = f"Solemn penal execution facility at dawn in {loc}, razor wire perimeter fence cutting through cold morning mist, profound contemplative quiet."
                elif b_idx < 14:
                    base = f"Symbolic red flag survival visual: An antique brass compass resting on dark slate beside an alert warning beacon, life-saving awareness."
                elif b_idx < 19:
                    base = f"Serene panoramic wide landscape of {loc} today: Sunlight breaking through storm clouds, peaceful nature renewed, dignity and closure restored."
                else:
                    base = f"Amber Eyes investigative studio desk: Antique brass lamp casting warm golden amber light over closed leather-bound dossier stamped with golden owl emblem, complete dignified closure."
            
            final_prompt = clean_p(base)
            
            jobs.append({
                "name": job_name,
                "act": a_idx,
                "sentences": cue,
                "desc": desc,
                "prompt": final_prompt
            })
            
    assert len(jobs) == target, f"Tap {ep}: expected {target}, got {len(jobs)}"
    assert len(set(x["name"] for x in jobs)) == target, f"Tap {ep}: duplicate names found"
    
    out_path = Path(f".work/bg_jobs_tap{ep}.json")
    out_path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
    
    total_all += len(jobs)
    print(f"Generated Tập {ep}: {len(jobs)} jobs -> {out_path.name}")

print(f"\nSUCCESSFULLY CREATED ALL 15 EPISODES! Total prompts: {total_all}")
