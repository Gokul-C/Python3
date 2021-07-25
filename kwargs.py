#**kwargs = paramater that will pack all arguments into a dictionary .so that a function can accepy a varying amount of keyword argument.

#def names(first_name , last_name):    #in this we can add only 2 names and if we want to add 3rd name error will arise.
 #   print ("hello " + first_name + " " + last_name )  #to arise this problem kwargs will be implemented.
#names(first_name = "gokul",last_name = "neeli")  #by using kwargs we can add as many names we wamt...


def names(**kwargs):
    print ("hello " + kwargs["first_name"] + " " + kwargs["last_name"] + " " + kwargs["middle_name"])

names(first_name ="chintha" , last_name = "neeli" , middle_name = "gokul")    

# another easiest method on kwargs2.py open it.