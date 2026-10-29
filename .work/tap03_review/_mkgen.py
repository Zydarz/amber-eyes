import io, re
src = io.open(r"D:\TEST\Gax\Audi\.work\gen_one.py", encoding="utf-8").read()
src = src.replace(
    'JOBS = WORK / "bg_jobs_tap03.json"',
    'JOBS = WORK / "bg_jobs_tap03_extra.json"')
src = src.replace(
    'PROV = Path(os.environ.get("AE_PROV") or (ROOT / "provenance.json"))',
    'PROV = Path(os.environ.get("AE_PROV") or (WORK / "prov_tap03_extra.json"))')
io.open(r"D:\TEST\Gax\Audi\.work\gen_one_extra.py", "w", encoding="utf-8", newline="\n").write(src)
print("gen_one_extra.py written")
