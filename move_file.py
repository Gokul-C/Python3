#it is used to move files from one place to another place...
#if the file is not in current directory , you should write the whole path

import os

source = "sample.txt"
destination = "/home//gokul-c//Downloads//sample.txt"

try:
    if os.path.exists(destination):
        print(source + " " + "file already exists here")

    else:
        os.replace(source,destination)
        print (source +" " + "this file was moved")
except FileNotFoundError:
    print(source + " " + "is not found")