import random 

#print (random.randint(1,10))

numbers = [1,2,3,6,5,4,8,7,9,5,4,6,4,13,6,4]
random.shuffle(numbers)
#print(numbers)

mylist = ["gokul" , "neeli" , "kali" , "linux" , "python"]
x = random.choice(mylist)
#print (x)

names = ["asus" , "dell" , "mac" , "lenovo" , "hp"]
y = random.choices(names)
print (y)