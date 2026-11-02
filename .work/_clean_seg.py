import pathlib
vd = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_t03")
for p in list(vd.glob("part_*.mp4")) + [vd/"parts.txt", vd/"picture.mp4"]:
    if p.exists():
        p.unlink(); print("xoa", p.name)
log = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\_build_seg_t03.log")
if log.exists(): log.unlink()
print("san sach")
