#nested function calls  = function calls inside other functions 
                    #     innermost function calls are resolved first
                    #     returned value is used as argument for the next outer function

# for example:

#num = input("enter the whole positive number : ") 
#num = float (num)
#num = int (num)
#num = round (num)
#num = abs (num)

#print(num)

#now The above example can be created in nested fucntion calls :

print(round(abs(int(float(input("enter the whole positive number : "))))))   

#6 lines of code can be printed in single line of code.... this  is nested function calls.