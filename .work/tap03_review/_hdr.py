import os, glob
p = r"D:\TEST\Gax\Audi\assets\sfx\t2"
for f in sorted(glob.glob(os.path.join(p, "*.wav")))[:4]:
    with open(f,"rb") as fh: head = fh.read(4)
    print(os.path.basename(f), "->", head, os.path.getsize(f))
d = r"C:\Users\ADMIN\Downloads"
for f in sorted(os.listdir(d), key=lambda x: os.path.getmtime(os.path.join(d,x)), reverse=True)[:3]:
    fp = os.path.join(d,f)
    with open(fp,"rb") as fh: head = fh.read(4)
    print("DL:", f, "->", head, os.path.getsize(fp))
