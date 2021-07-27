# there are 2 types of variables golbal and local variables.
#global = it can be created and used anywhere in the program,
#local = it should be created with in the region to be used.

fav = "kali"    #its an global variable coz its out side region .
def my_name():
    name = "gokul"   #this is local variable coz its in region i mean under a function.
    print(name)
  

my_name()
print(fav)