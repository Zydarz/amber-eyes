import sys
sys.path.insert(0,".work")
from freesound_client import FreesoundClient
c=FreesoundClient()
tests = {
 "amb_lawyers_discussion": [("lawyers discussion",8,90),("lawyer talking",8,90),("office discussion",8,90),("people talking office",8,90)],
 "amb_library_quiet": [("library",8,90),("library ambience",8,90),("quiet room",8,90),("reading room",8,90)],
 "fx_courtroom_dead_silence": [("courtroom",8,90),("court",8,90),("courtroom ambience",8,90),("empty hall room tone",8,90)],
 "fx_crowd_relief_sigh": [("crowd sigh",0.2,12),("sighing crowd",0.2,12),("audience sigh",0.2,12),("sigh",0.2,12)],
 "fx_sigh_emotional": [("sigh",0.2,12),("man sigh",0.2,12),("sighing",0.2,12),("emotional sigh",0.2,12)],
 "fx_wooden_lid_slam_latch": [("wooden lid",0.2,12),("latch",0.2,12),("box lid close",0.2,12),("wooden box",0.2,12)],
}
for code,qs in tests.items():
    print(f"\n== {code}")
    for q,lo,hi in qs:
        try:
            r=c.search(q, limit=6, license="cc0", duration_max=hi, fallback=False)
            ids=[f"{x['id']}/{x.get('duration',0):.1f}s" for x in r]
            print(f"   {q:<28} n={len(r):<3} {ids[:6]}")
        except Exception as e:
            print(f"   {q:<28} EXC {e}")
