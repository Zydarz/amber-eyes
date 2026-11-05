import os, sys
sys.path.insert(0, r"D:/TEST/Gax/amber-eyes/.work")
for lang in ("vi","en","ja","ko"):
    os.environ["AE_LANG"] = lang; os.environ["AE_EP"] = "02"
    for m in ("edition",):
        sys.modules.pop(m, None)
    import edition as ED
    print(f"{lang}: PLAN={ED.PLAN.name if ED.PLAN else None} exists={ED.PLAN.exists() if ED.PLAN else False}")
    print(f"    shots->{ED.w('shots.json').name}  tl->{ED.w('timeline_s.json').name}  video3->{ED.w('video3').name}")
    print(f"    roles N1={ED.ROLE_NAME.get('N1')} N2={ED.ROLE_NAME.get('N2')}")
    print(f"    act1={ED.EP['act_titles'][1][:60]}")
