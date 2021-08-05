#exception handling = if any error occurs during execution of program,this exception handling can be used to uderstand the error
#                     and display to the user.

#exception handling defination = events detected during execution that interrupts the flow of the program.

try:

    numerator = int(input("Enter a number to divide : "))
    denominator = int(input("Enter a number to divide by : "))
    result = numerator / denominator

#print(result) 

except ZeroDivisionError:           #this will print if we enter zero in denominator.
    print ("you cant divide any nymber with zero")

except ValueError:                  #this will print if we enter anything other than numbers.
    print("enter only numbers !")

except Exception:                  #this will print if any other errors occur.
    print("something went wrong")    

else:
    print("The result is : "+str(result))