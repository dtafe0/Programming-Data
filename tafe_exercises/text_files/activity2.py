import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    print(os.name)
    print("item exists:" + str(path.exists("textfile.txt")))
    print("item is a file:" + str(path.isfile("textfile.txt")))
    print("item is a directory:" + str(path.isdir("textfile.txt")))

    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        dst = src + ".bak"
        shutil.copy(src,dst)
    
    os.rename ("textfile.txt.bak", "newfile.txt")

    root_dir, tail = path.split(src)
    shutil.make_archive("archive", "zip", root_dir)
    
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("main.py")


if __name__ == "__main__":
    main()

