import os
import subprocess
import sys
import time

os.environ['AE_EP'] = '06'
os.environ['PYTHONIOENCODING'] = 'utf-8'

print("=== STARTING BUILD_VIDEO3 (WORKERS 6) ===")
t0 = time.time()
res = subprocess.run([sys.executable, '.work/build_video3.py', '--workers', '6'])
print(f"build_video3 exited with returncode {res.returncode} in {time.time()-t0:.1f}s")

if res.returncode != 0:
    print("Error during build_video3!")
    sys.exit(res.returncode)

print("\n=== STARTING PACKAGE --MUX ===")
t1 = time.time()
res_mux = subprocess.run([sys.executable, '.work/package.py', '--mux'])
print(f"package --mux exited with returncode {res_mux.returncode} in {time.time()-t1:.1f}s")

if res_mux.returncode != 0:
    print("Error during package --mux!")
    sys.exit(res_mux.returncode)

print("\n=== PIPELINE FINISHED SUCCESSFULLY ===")
