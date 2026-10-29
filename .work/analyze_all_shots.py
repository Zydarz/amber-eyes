import json
import re
import sys

# Read _shots_full_alignment.txt
with open('.work/_shots_full_alignment.txt', 'r', encoding='utf-8') as f:
    content = f.read()

shot_blocks = re.findall(r'(SHOT \d+-\d+ \([^)]+\) \| BG: [^\n]+)\n\s+CHỮ TRÊN HÌNH: ([^\n]*)\n\s+LỜI ĐỌC THẬT : ([^\n]*)', content)

out_lines = []
out_lines.append(f"Total parsed shots from alignment: {len(shot_blocks)}")

for header, overlay, spoken in shot_blocks:
    m = re.match(r'SHOT (\d+-\d+) \((\d+\.\d+)s -> (\d+\.\d+)s, (\d+\.\d+)s\) \| BG: ([^\s]+)', header)
    if not m:
        continue
    shot_id, start_s, end_s, dur, bg = m.groups()
    start_s, end_s, dur = float(start_s), float(end_s), float(dur)
    
    cues = re.findall(r'\[([^\]]+)\] ([^\[]+)', spoken)
    
    out_lines.append(f"\n{'='*70}")
    out_lines.append(f"[{shot_id}] ({start_s:.1f}s - {end_s:.1f}s, dur {dur:.1f}s) BG: {bg}")
    out_lines.append(f"  Overlay: {overlay.strip()}")
    if cues:
        for cue_id, cue_text in cues:
            out_lines.append(f"    * {cue_id}: {cue_text.strip()}")
    else:
        out_lines.append(f"    * (Không lời / Pause / Chapter Card)")

with open('.work/shot_semantic_review.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))

print("Wrote .work/shot_semantic_review.txt successfully with utf-8.")
