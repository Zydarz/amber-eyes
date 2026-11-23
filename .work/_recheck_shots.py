import json, os, re

report = json.load(open('.work/_accurate_final_report.json', encoding='utf-8'))

# Read shots files for episodes 1 to 24
for r in report:
    ep = r['ep']
    fn = '.work/shots.json' if ep == 1 else f'.work/shots_t{ep:02d}.json'
    if os.path.exists(fn):
        d = json.load(open(fn, encoding='utf-8'))
        shots = d.get('shots', [])
        r['shots'] = len(shots)
        r['shot_type'] = "Bảng shot timeline đã neo audio master"
    else:
        # Check KeHoach table
        plan_p = f"02_SAN_XUAT/Ho_So_Toi_Pham/Tap{ep:02d}/KeHoach_Video_Tap{ep:02d}.md"
        plan_shots = 0
        if os.path.exists(plan_p):
            lines = open(plan_p, encoding='utf-8').read().splitlines()
            shot_lines = [l for l in lines if re.match(r'^\|\s*`?\d+[\.\d]*', l)]
            if len(shot_lines) > 0:
                plan_shots = len(shot_lines)
        if plan_shots > 0:
            r['shots'] = plan_shots
            r['shot_type'] = "Bảng shot chi tiết trong kế hoạch"
        else:
            r['shots'] = r['sentences'] + 5
            r['shot_type'] = f"Quy tắc chuẩn ({r['sentences']} câu + 5 thẻ chuyển/kết)"

# Print sample to verify
print("Sample checked:")
for r in report[:10]:
    print(f"Tap {r['ep']:02d}: {r['title'][:30]} | {r['country']} | Câu: {r['sentences']} | Ảnh: {r['images']} | Shot: {r['shots']} ({r['shot_type']})")

open('.work/_accurate_final_report.json', 'w', encoding='utf-8').write(json.dumps(report, ensure_ascii=False, indent=2))
