# dictionaries = a changable , unorderd collection of unique key : value pairs
#                 fast because they are hashing , allow us to access a value quickly


capitals = {"india":"delhi" , "usa":"washington dc" , "germany":"berlin","russia":"moscow"}

#print(capitals.keys())
#capitals.pop("usa")
#print(capitals.get("germany"))
#print(capitals.values())
#capitals.update({'india':'andhra'})
  

for key , values in capitals.items():
    print(key , values)