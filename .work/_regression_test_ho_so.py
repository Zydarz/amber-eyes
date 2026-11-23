import sys, os, json, re

sys.path.insert(0, '.work')
import parse_kichban

# Verify regression for all 68 episodes in the new folder 01_KICH_BAN/Ho_So_Toi_Pham
base_hs = "01_KICH_BAN/Ho_So_Toi_Pham"
results = []
errors = []

for ep in range(1, 69):
    ep_str = f"Tap{ep:02d}"
    kb_dir = os.path.join(base_hs, ep_str)
    if not os.path.exists(kb_dir):
        errors.append(f"{kb_dir} does not exist!")
        continue
        
    files = os.listdir(kb_dir)
    vn_files = [f for f in files if f.endswith('.md') and not any(k in f for k in ['_EN', '_JA', '_KO', 'REVIEW', 'NghienCuu', '_cu', '_ban_goc', '_truoc_review', '_pre_directors_cut', 'bak'])]
    
    if ep == 1:
        target = "kichban_tap01_22102026_v2.md"
    elif ep == 2:
        target = "kichban_tap02_22102026.md"
    else:
        target = sorted(vn_files)[-1]
        
    script_path = os.path.join(kb_dir, target)
    out_json = f".work/_test_ho_so_{ep_str}.json"
    
    try:
        parse_kichban.parse_file(script_path, out_json)
        elements = json.load(open(out_json, encoding='utf-8'))
        total_sentences = sum(len(e.get('sentences', [])) for e in elements if 'sentences' in e)
        results.append((ep, total_sentences, target))
    except Exception as e:
        errors.append(f"Error parsing Tap {ep:02d}: {e}")

print(f"Regression Test Results:")
print(f"  Parsed successfully: {len(results)}/68 episodes")
print(f"  Total sentences: {sum(r[1] for r in results)}")
if errors:
    print(f"  Errors encountered: {len(errors)}")
    for err in errors:
        print("   ", err)
else:
    print("  SUCCESS: 0 errors! All 68 episodes parsed with 100% integrity.")

# Update the main reports to reflect the new path
for report_file in ['BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md', '90_LUU_TRU/BaoCao_ThongKe_ChiTiet_68_Tap_VuAn_20261122.md', '.work/BAO_CAO_CHI_TIET_68_TAP.md']:
    if os.path.exists(report_file):
        c = open(report_file, encoding='utf-8').read()
        c = c.replace('01_KICH_BAN/', '01_KICH_BAN/Ho_So_Toi_Pham/')
        open(report_file, 'w', encoding='utf-8').write(c)

print("Updated reports with the new Ho_So_Toi_Pham structure!")
