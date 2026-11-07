import os,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
env=dict(os.environ,AE_EP="03",AE_LANG="en",PYTHONIOENCODING="utf-8")
r=subprocess.run([sys.executable,str(R/".work"/"package.py"),"--mux"],env=env,cwd=str(R),text=True,encoding="utf-8",errors="replace",stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
print(r.stdout[-2500:]); sys.exit(r.returncode)
