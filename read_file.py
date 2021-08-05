# This will print the information that present in the file and we should present the file path to execute
#or if file presents in same  folder then only file name will be given.

#with open ("list.py")as file:
    #print(file.read())

#if file name not exist then error wil be occured then we can use exception    

try:
    with open ("/home//gokul-c//Documents//vscode//Python3//list.p")as file:
        print(file.read())

except:
    print("file name you enterd not found")        