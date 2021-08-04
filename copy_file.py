#copyfile() = it copies contents of the file
#copy() = copyfile() + permission mode + destination can be directory
#copy2() = copy() + copies metadata (files creation and modification times)

import shutil

shutil.copyfile('if.py' , 'if.txt')    #source file , destination file