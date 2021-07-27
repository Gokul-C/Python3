#while True:
 #   name = input("Enter your name :  ")
 #   if name != "":
  #      break

#if we dont use break statement the loop will continue even we enter name .
# means the loop will continue after we enter our name 

myname = "gokulneeli"
for i in myname:
    if i == "neeli":
        continue
    print (i,end = "")

for i in range(1,10):
    if i == 7:
        pass  
    else:
        print (i) 




