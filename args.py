#*args = paramater that will pack all arguments into a tuple
#        useful so that a function can accept a varying amount of arguments.        

def add (*args):   #args is not important than "*" ...so we can keep any name instead of args.
    sum = 0
    for i in args:
        sum += i

    return sum  

print(add(1,2,3,4,5,5))        