import os

path = "/home//gokul-c//Documents//vscode//Python3//2dlist.py"

if os.path.exists(path):
    print ("the location exits")
    if os.path.isdir(path):
        print("its an directory")   

    elif os.path.isfile(path):
        print("its a file")         

else :
    print("this location doesnt exist ")
