# -*- coding: utf-8 -*-
import json, re, sys
from pathlib import Path
from gen_core import clean_prompt
from ep_metadata import EP_META

ROOT = Path('.').resolve()
WORK_DIR = ROOT / '.work'

def build_all_episodes():
    total_generated = 0
    results = {}
    
    for ep_num, meta in EP_META.items():
        script_path = Path(f'01_KICH_BAN/Tap{ep_num}/kichban_tap{ep_num}_19112026.md')
        txt = script_path.read_text(encoding='utf-8')
        raw_acts = re.split(r'## HỒI \d.*', txt)[1:]
        
        target = meta['target']
        splits = meta['splits']
        title = meta['title']
        loc = meta['loc']
        kw = meta['keywords']
        
        ep_jobs = []
        
        for act_idx, (act_txt, act_target) in enumerate(zip(raw_acts, splits), 1):
            lines = [l.strip() for l in act_txt.splitlines() if l.strip() and not l.startswith('**[') and not l.startswith('**') and not l.startswith('#') and not l.startswith('---')]
            
            # Divide lines into act_target visual beats
            total_lines = len(lines)
            step = max(1, total_lines / act_target)
            
            for beat_idx in range(act_target):
                line_idx = min(int(beat_idx * step), total_lines - 1)
                context_line = lines[line_idx]
                
                # Derive semantic prompt elements
                prompt_num = beat_idx + 1
                name = ft{ep_num}_a{act_idx}_{prompt_num:02d}_{kw[beat_idx % len(kw)].lower().replace(' ', '_')}
                cue = f{act_idx}.{max(1, (beat_idx // 3) + 1):02d}#{(beat_idx % 3) + 1}
                
                # Vietnamese description derived from narrative beat
                desc = fHồi {act_idx} Tập {ep_num} ({kw[beat_idx % len(kw)]}): {context_line[:90]}...
                
                # Deep Noir English Prompt construction (4-tier standard)
                if act_idx == 1:
                    if beat_idx < 3:
                        p_core = fCinematic establishing wide shot of {loc}, atmospheric dusk fog rolling across shadowy terrain, sharp noir chiaroscuro, distant dim streetlamps.
                    elif beat_idx < 10:
                        p_core = fAtmospheric 1990s realistic street scene in {loc}, subtle social blindspot concept, moody overcast sky, deep dark silhouettes.
                    elif beat_idx < 25:
                        p_core = fForensic high-contrast still life in {loc}, intimate macro composition of vintage investigative tools and shadowed domestic interior, dramatic side lighting.
                    else:
                        p_core = fDramatic cinematic composition capturing the sudden rupture of peace in {loc}, dynamic diagonal shadows, emergency amber beacon reflections.
                elif act_idx == 2:
                    if beat_idx < 10:
                        p_core = fHigh-contrast psychological visual in {loc}, compartmentalization and split reflection in antique cracked mirror, ominous shadow casting.
                    elif beat_idx < 25:
                        p_core = fDesolate nocturnal scene in {loc}, predatory stalker silhouette concealed behind dense trees, cold steel-blue moonlight, sharp tension.
                    else:
                        p_core = fMacro forensic still life of evidence markers and shadowed vehicle interior in {loc}, clinical detachment, graphic novel realism.
                elif act_idx == 3:
                    if beat_idx < 10:
                        p_core = fLate-night police task force operations room in {loc}, desks cluttered with geographic profiling maps and forensic dossiers under green banker lamps.
                    elif beat_idx < 20:
                        p_core = fSterile police interrogation room in {loc}, high-contrast chiaroscuro, suspect silhouette seated across metal table under harsh single overhead lamp.
                    else:
                        p_core = fForensic laboratory comparison scene in {loc}, dual-view comparison microscope glowing in dark room, scientific breakthrough and collapse of false alibis.
                elif act_idx == 4:
                    if beat_idx < 10:
                        p_core = fHistoric courtroom interior during formal proceedings in {loc}, solemn judge bench, packed spectator gallery, dramatic chiaroscuro window shafts.
                    elif beat_idx < 20:
                        p_core = fSolemn witness stand perspective in {loc}, emotional testimony under directional spotlight, quiet dignified defiance of justice.
                    else:
                        p_core = fJudicial gavel striking hardwood sounding block firmly in {loc}, dramatic spotlight beam cutting through courtroom dust, definitive sentence finality.
                else: # Act 5
                    if beat_idx < 8:
                        p_core = fSolemn penal execution facility exterior at dawn in {loc}, razor wire perimeter fence cutting through cold steel-blue morning mist, absolute quiet.
                    elif beat_idx < 14:
                        p_core = fConceptual red flag survival visual: An antique brass compass resting on dark slate beside an alert warning beacon, life-saving vigilance.
                    elif beat_idx < 19:
                        p_core = fSerene panoramic wide shot of {loc} today: Sunlight breaking through storm clouds, lush landscape renewed, peaceful human dignity restored.
                    else:
                        p_core = fAmber Eyes studio desk closing shot: Antique brass desk lamp casting warm golden amber light over closed leather-bound dossier stamped with golden owl emblem, dignified complete closure.
                
                # Clean prompt to guarantee 0 text triggers (H2/H26)
                clean_p = clean_prompt(p_core)
                
                ep_jobs.append({
                    name: name,
                    act: act_idx,
                    sentences: cue,
                    desc: desc,
                    prompt: clean_p
                })
        
        # Ensure exact count and unique names
        assert len(ep_jobs) == target, fTap {ep_num}: Expected {target}, got {len(ep_jobs)}
        assert len(set(x['name'] for x in ep_jobs)) == target, fTap {ep_num}: Names not unique
        
        # Save output JSON
        out_file = WORK_DIR / fbg_jobs_tap{ep_num}.json
        out_file.write_text(json.dumps(ep_jobs, ensure_ascii=False, indent=2), encoding='utf-8')
        
        total_generated += len(ep_jobs)
        results[ep_num] = len(ep_jobs)
        print(fTap {ep_num}: Done {len(ep_jobs)} prompts -> {out_file.name})
        
    print(f\n==========================================)
    print(fALL 15 EPISODES COMPLETED! Total: {total_generated} prompts.)
    print(f==========================================)

if __name__ == '__main__':
    build_all_episodes()
