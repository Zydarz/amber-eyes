import sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from flux_client import generate_16_9_background, get_account_pool

pool = get_account_pool()
print("accounts in pool:", len(pool))
t0 = time.perf_counter()
try:
    img = generate_16_9_background(
        prompt="Rural lane in Dong Nai province, Vietnam at night, rows of shuttered village houses with dark windows, faint mist, one distant dim lamp, ominous stillness.",
        steps=4, out_size=(2112, 1188), with_noir_style=True)
    img.save(ROOT / ".work" / "_cf_smoke_t37.png", "PNG")
    print("OK size:", img.size, "time:", round(time.perf_counter() - t0, 1), "s")
except Exception as e:
    print("FAIL:", type(e).__name__, e)
