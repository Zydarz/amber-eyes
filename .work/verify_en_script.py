#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verification script for English scripts against Vietnamese scripts.
Ensures 100% 1-to-1 match for element IDs, kinds, roles, and sentence IDs.
"""
import sys, os, glob, json, subprocess
from pathlib import Path
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def verify_episode(ep_num):
    ep_str = f"{ep_num:02d}"
    root = Path(__file__).resolve().parents[1]
    
    # 1. Find Vietnamese script
    vn_dir = root / "01_KICH_BAN" / f"Tap{ep_str}"
    if ep_str == "01":
        vn_candidates = [vn_dir / "kichban_tap01_22102026_v2.md"]
    else:
        vn_candidates = [f for f in glob.glob(str(vn_dir / f"kichban_tap{ep_str}_*.md")) 
                         if not any(x in f for x in ['ban_goc', 'truoc_review', 'EN'])]
    if not vn_candidates or not os.path.exists(vn_candidates[0]):
        print(f"Error: VN script not found for Tap{ep_str}")
        return False
    vn_file = Path(vn_candidates[0])
    
    # 2. Find English script
    en_file = root / "01_KICH_BAN" / f"Tap{ep_str}_EN" / f"kichban_tap{ep_str}_EN.md"
    if not en_file.exists():
        en_file = root / "01_KICH_BAN" / f"Tap{ep_str}" / f"kichban_tap{ep_str}_EN.md"
    if not en_file.exists():
        print(f"Error: EN script not found: {en_file}")
        return False
        
    # 3. Parse both with parse_kichban.py
    work = root / ".work"
    vn_json = work / f"temp_verify_vn_t{ep_str}.json"
    en_json = work / f"temp_verify_en_t{ep_str}.json"
    
    p1 = subprocess.run(["py", "-3", str(work / "parse_kichban.py"), str(vn_file), str(vn_json)], capture_output=True, text=True)
    if p1.returncode != 0:
        print(f"Error parsing VN script: {p1.stderr}")
        return False
        
    p2 = subprocess.run(["py", "-3", str(work / "parse_kichban.py"), str(en_file), str(en_json)], capture_output=True, text=True)
    if p2.returncode != 0:
        print(f"Error parsing EN script: {p2.stderr}")
        return False
        
    vn_data = json.load(open(vn_json, encoding='utf-8'))
    en_data = json.load(open(en_json, encoding='utf-8'))
    
    # 4. Compare elements
    errors = []
    if len(vn_data) != len(en_data):
        errors.append(f"Element count mismatch: VN has {len(vn_data)}, EN has {len(en_data)}")
        
    min_len = min(len(vn_data), len(en_data))
    for i in range(min_len):
        v = vn_data[i]
        e = en_data[i]
        v_id, e_id = v.get("id"), e.get("id")
        v_kind, e_kind = v.get("kind"), e.get("kind")
        if v_id != e_id:
            errors.append(f"Element [{i}] ID mismatch: VN={v_id}, EN={e_id}")
        if v_kind != e_kind:
            errors.append(f"Element [{v_id}] kind mismatch: VN={v_kind}, EN={e_kind}")
        if v_kind == "LOI":
            if v.get("role") != e.get("role"):
                errors.append(f"Element [{v_id}] role mismatch: VN={v.get('role')}, EN={e.get('role')}")
            v_s = v.get("sentences", [])
            e_s = e.get("sentences", [])
            if len(v_s) != len(e_s):
                errors.append(f"Element [{v_id}] sentence count mismatch: VN has {len(v_s)}, EN has {len(e_s)}")
                errors.append(f"  VN sentences: {[s['id'] for s in v_s]}")
                errors.append(f"  EN sentences: {[s['id'] for s in e_s]}")
                for s_idx in range(max(len(v_s), len(e_s))):
                    vt = v_s[s_idx]['text'] if s_idx < len(v_s) else "<NONE>"
                    et = e_s[s_idx]['text'] if s_idx < len(e_s) else "<NONE>"
                    errors.append(f"    #{s_idx+1}: VN='{vt}'")
                    errors.append(f"         EN='{et}'")
            else:
                for s_idx in range(len(v_s)):
                    if v_s[s_idx]['id'] != e_s[s_idx]['id']:
                        errors.append(f"Sentence ID mismatch: VN={v_s[s_idx]['id']}, EN={e_s[s_idx]['id']}")
                        
    if errors:
        print(f"❌ Episode {ep_str} FAILED with {len(errors)} issues:")
        for err in errors[:20]:
            print("  -", err)
        return False
    else:
        vn_s_total = sum(len(e.get("sentences", [])) for e in vn_data)
        print(f"✅ Episode {ep_str} PASSED: {len(vn_data)} elements, {vn_s_total} sentences perfectly matched!")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py -3 .work/verify_en_script.py <ep_num_or_all>")
        sys.exit(1)
    arg = sys.argv[1].lower()
    if arg == "all":
        results = [verify_episode(i) for i in range(1, 30)]
        print(f"\nSummary: {sum(results)}/29 episodes passed.")
        sys.exit(0 if all(results) else 1)
    else:
        success = verify_episode(int(arg))
        sys.exit(0 if success else 1)
