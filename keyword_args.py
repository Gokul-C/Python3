#keyword arguments = arguments proceeded by an identifier when we pass them to a function the order of arguments doesnt matter,
#                    unlike positional arguments python knows the names of the arguments that our function receives.

def hello(first,middle,last):
    print("hello " + first + " " + middle + " " + last)

#hello("chintha","gokul","neeli")    
hello (first = "chintha",last = "gokul",middle="neeli")