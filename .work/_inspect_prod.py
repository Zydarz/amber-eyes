import os, sys, glob, json
from pathlib import Path

ROOT = Path(r"d:\TEST\Gax\amber-eyes")

print("Checking 02_SAN_XUAT structure:")
for p in (ROOT / "02_SAN_XUAT").glob("*Tap*"):
    print(p.name)

print("\nFiles in 02_SAN_XUAT/Ho_So_Toi_Pham/Tap39:")
for p in (ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap39").glob("*"):
    print(p.name)

print("\nFiles in 02_SAN_XUAT/Ho_So_Toi_Pham/Tap10:")
for p in (ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap10").glob("*"):
    print(p.name)
