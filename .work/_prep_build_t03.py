import shutil, pathlib, datetime
W = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
vd = W/"video3_t03"
bk = W/"_cu"
bk.mkdir(exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
old = vd/"picture.mp4"
if old.exists():
    dst = bk/f"picture_t03.CU_BAN.bak_{stamp}.mp4"
    shutil.move(str(old), str(dst))
    print(f"backup picture.mp4 cũ (1911s, sai timeline) -> {dst.name}")
for p in list(vd.glob("part_*.mp4")) + [vd/"parts.txt"]:
    if p.exists():
        p.unlink()
        print("xoa", p.name)
print("san sach:", sorted(x.name for x in vd.iterdir()))
