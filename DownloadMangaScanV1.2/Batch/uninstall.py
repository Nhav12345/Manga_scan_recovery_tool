#!/usr/bin/python3
import os
os.system("cd C:\ ")
path="C:\ScansManga"
all_manga=os.listdir(path)
for e in all_manga:
    all_chapter = os.listdir(path+f"\{e}")
    for i in all_chapter:
        os.system(f"del {path}\{e}\{i} /Q")
        os.system(f"rmdir {path}\{e}\{i}")
        print(f"{path}\{e}\{i}: deleted.")
    os.system(f"rmdir {path}\{e}")
    print(f"Directory '{e}' deleted.")