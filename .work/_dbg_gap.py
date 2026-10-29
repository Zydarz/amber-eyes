from pathlib import Path
p=Path("02_SAN_XUAT/Danh_Sach_SFX_Tap03-29.md")
lines=p.read_text(encoding="utf-8").splitlines()
print("total lines:", len(lines))
idx=[i for i,l in enumerate(lines) if l.startswith("### 5.2")]
print("5.2 at:", idx)
if idx:
    i0=idx[0]
    for j in range(i0, i0+8):
        print(f"{j}: {lines[j][:150]}")
