from pathlib import Path
P = Path(r"D:\TEST\Gax\amber-eyes\.work\build_video3.py")
s = P.read_bytes().decode("utf-8")
i = s.find("def finishing")
print(repr(s[i-120:i+700]))
print("---- VIGNETTE decl ----")
j = s.find("VIGNETTE = None")
print(repr(s[j-80:j+120]))
