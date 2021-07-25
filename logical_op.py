#Logical operators are used to check if two or more conditions are true or flase . the basic logical operators are (and,or,not)

temp = int(input("what is the temparature outside ? : "))

#both conditions need to be true to use AND

if (temp >= 0 and temp <=30):
    print ("Good! The temparature is good outside ")
    print ("go and play outside,instead of playing pubg")

# atleast one condition need to be true to execute OR

elif (temp < 0 or temp > 30):
    print ("Bad Weather !")
    print ("keep calm and play pubg")

# NOT is used to make true statements false and false statement true....its just flip the statement

#if not(temp >= 0 and temp <=30):
 #   print ("Good! The temparature is good outside ")
  #  print ("go and play outside,instead of playing pubg")

#elif not(temp < 0 or temp > 30):
 #   print ("Bad Weather !")
  #  print ("keep calm and play pubg")

