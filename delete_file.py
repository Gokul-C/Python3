import os 
import shutil

path = "del.txt"

try:

    os.remove(path)      #it will delete only files not folders
    #os.rmdir(path)       #By this only empty folders can be deleted.
    #shutil.rmtree(path)  #by this we can delete all files and folder contains in that folder and that is permanant.

except FileNotFoundError:
    print ("file not found")
except PermissionError:
    print ("you dont have permission to delete this folder")
except OSError:
    print ("you cannot delete this using this function")               
else :
    print ("it was deleted")