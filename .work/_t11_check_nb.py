import json
import pathlib

CHECKS = [
    'job.get("seed"',
    "batch_gpu1 = []",
    "ret0 = p0.wait()",
    "ret1 = 0",
    "p1 = ",
    "zip_name",
    "JOBS_FILE",
]
for d in ["d1", "d2"]:
    p = pathlib.Path(f".work/kaggle_flux/{d}/flux2_generator.ipynb")
    nb = json.loads(p.read_text(encoding="utf-8"))
    code = "".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code")
    md = "".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "markdown")
    print(f"=== {d} | code {len(code)} chars")
    for k in CHECKS:
        print(f"    {k!r:<26} x{code.count(k)}")
    heads = [l for l in md.split("\n") if l.strip().startswith("#")]
    print("    markdown:", heads[:2])
    print("    zip:", [l for l in code.split("\n") if "flux2_tap11_detext" in l][:1])
