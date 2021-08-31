import os

gokul = "gokul.txt"
linux = "/home//gokul-c//Downloads//gokul.txt"

try:
    if os.path.exists(linux):
        print (gokul + " " + " file already exists")
    else:
         os.replace(gokul,linux)
         print (gokul + " " + "files was moved")    
except FileNotFoundError:
    print (gokul + " " + "file not found")         

