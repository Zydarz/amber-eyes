import shutil, datetime, pathlib
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03\xuat_ban\Tap03.srt")
bk = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\_cu")
bk.mkdir(exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
if p.exists():
    shutil.copy2(str(p), str(bk/f"Tap03.srt.bak_{stamp}"))
    print(f"backup SRT cu -> {bk.name}/Tap03.srt.bak_{stamp}")
