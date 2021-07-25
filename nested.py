#Nested loops = the inner loop will finishes all its iteration before outer loop completes one iterartion.
#in below example for i is inner loop and for j is outer loop....


rows = int(input("Enter the number of rows? : "))
coloumns = int(input("Enter the number of coloumns ? : "))
symbol = input("Enter the symbol : ")

for i in range (rows):
    for j in range (coloumns):
        print (symbol,end="")
    print()