#this can able to create a file and write anything into that file....


text = "hello this is GokuL C \n its an sample txt file related to python file\n gokul@linux"
with open ("write_file.txt",'w')as file:    #here 'w' means it can write a file and if we keep 'r' it will read a file
     file.write(text)
