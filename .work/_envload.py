from pathlib import Path
P = Path(r"D:\TEST\Gax\amber-eyes\.work\build_video3.py")
s = P.read_bytes().decode("utf-8").replace("\r\r\n", "\n")
i = s.find("def env_load")
print(s[i-200:i+1400])
